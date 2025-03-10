from .models import CarMake, CarModel
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate
from .restapis import get_request, analyze_review_sentiments, post_review
from django.contrib.auth.models import User


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Get all car models and their corresponding makes
def get_cars(request):
    count = CarMake.objects.count()

    if count == 0:
        initiate()

    car_models = CarModel.objects.select_related("car_make")
    cars = [
        {"CarModel": car_model.name, "CarMake": car_model.car_make.name}
        for car_model in car_models
    ]
    return JsonResponse({"CarModels": cars})


# Handle sign-in request
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data["userName"]
    password = data["password"]

    user = authenticate(username=username, password=password)
    response_data = {"userName": username}

    if user is not None:
        login(request, user)
        response_data["status"] = "Authenticated"

    return JsonResponse(response_data)


# Handle sign-out request
def logout_request(request):
    logout(request)
    return JsonResponse({"userName": ""})


# Handle user registration request
@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data["userName"]
    password = data["password"]
    first_name = data["firstName"]
    last_name = data["lastName"]
    email = data["email"]

    username_exist = User.objects.filter(username=username).exists()

    if username_exist:
        return JsonResponse({
            "userName": username,
            "error": "Already Registered"})

    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        password=password,
        email=email,
    )

    login(request, user)
    return JsonResponse({"userName": username, "status": "Authenticated"})


def get_dealerships(request, state="All"):
    endpoint = "/fetchDealers"
    if state != "All":
        endpoint = f"/fetchDealers/state/{state}"

    dealerships = get_request(endpoint)

    if not dealerships or "error" in dealerships:
        return JsonResponse(
            {
                "status": 500,
                "error": dealerships.get("error", "Unknown error")
            }, status=500)

    return JsonResponse({"status": 200, "dealers": dealerships})


# Fetch dealer reviews
def get_dealer_reviews(request, dealer_id):
    if not dealer_id:
        return JsonResponse({"status": 400, "message": "Bad Request"})

    endpoint = f"/fetchReviews/dealer/{dealer_id}"
    reviews = get_request(endpoint)

    for review_detail in reviews:
        sentiment_analysis = analyze_review_sentiments(review_detail["review"])
        review_detail["sentiment"] = sentiment_analysis["sentiment"]

    return JsonResponse({"status": 200, "reviews": reviews})


# Fetch dealer details
def get_dealer_details(request, dealer_id):
    if not dealer_id:
        return JsonResponse({"status": 400, "message": "Bad Request"})

    endpoint = f"/fetchDealers/id/{dealer_id}"
    dealership = get_request(endpoint)
    return JsonResponse({"status": 200, "dealer": dealership})


# Submit a review
def add_review(request):
    if request.user.is_anonymous:
        return JsonResponse({"status": 403, "message": "Unauthorized"})

    try:
        data = json.loads(request.body)
        post_review(data)
        return JsonResponse({"status": 200})
    except Exception as e:
        return JsonResponse({
            "status": 401,
            "message": f"Error in posting review: {str(e)}"})
