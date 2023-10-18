from django.shortcuts import render, redirect
import requests
from django.http import JsonResponse
from .lib.utils import *
from .forms import FormDataForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FormDataSerializer

# Create your views here.
def index(request):
    """
    Base html to render all html
    """
    return render(request, 'base.html')

def get_licence_data(request):
    """
    licence details from rdw.nl open source
    queried json formatted as per the need
    """
    v = request.GET.get('v', '')

    try:
        response = requests.get(f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={v.replace('-', '')}")
        response.raise_for_status()  # Check if the response was successful

        # Checking if the response is in json format
        if "application/json" not in response.headers["Content-Type"]:
            raise ValueError("API response was not in JSON format")

        data = transform_response(response.json())
        return JsonResponse(data, safe=False)

    except requests.RequestException as e:
        # Handle specific request exceptions
        return JsonResponse({"error": f"Request failed: {str(e)}"}, status=400)
    except ValueError as e:
        # Handle specific ValueError exceptions (like if API response is not JSON)
        return JsonResponse({"error": str(e)}, status=400)
    except Exception as e:
        # Generic error handling for unexpected errors
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)


def get_address_details(request):
    """
    To get the address details from the postcode.nl website
    without headers for now
    """
    postcode = request.GET.get("postcode")
    house_number = request.GET.get("house_number")

    if not postcode or not house_number:
        data = {
            "street": None,
            "houseNumber": None,
            "houseNumberAddition": None,
            "postcode": None,
            "city": None
        }
        return JsonResponse(data, safe=False)

    url = f"https://www.postcode.nl/json/validate/address/AddressLookup/lookup?postcode={postcode}&houseNumber={house_number}"
    try:
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'valid':
            return JsonResponse(data['address'], safe=False)
    except Exception as e:
        print(e)

    data = {
        "street": None,
        "houseNumber": None,
        "houseNumberAddition": None,
        "postcode": None,
        "city": None
    }
    return JsonResponse(data, safe=False)

def handle_form(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url_or_name')
    else:
        form = FormDataForm()

    return render(request, 'template_name.html', {'form': form})

@api_view(['POST'])
def save_form_data(request):
    if request.method == 'POST':
        serializer = FormDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
