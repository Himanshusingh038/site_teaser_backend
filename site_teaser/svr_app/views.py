from telnetlib import STATUS
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
import json
import requests
from .serializers import PropertySurroundingSerializer
from django.views.decorators.http import require_POST
from django.db import connection
from django.http import JsonResponse

# Create your views here.


@require_POST
def create_announcement(request):
    try:
        serializer = PropertySurroundingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=STATUS.HTTP_201_CREATED)
        else:
            return response(serializer.errors, status=STATUS.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def get_properties(request):
    try:
        id = request.GET.get('id')
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM properties where id = {id}")
            properties = cursor.fetchall()
        return JsonResponse({'properties': properties})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def insert_properties(request):
    name = request.GET.get('name')
    desc = request.GET.get('property_desc')
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO properties(name, property_desc) VALUES('{name}', '{desc}') returning *")
            data = cursor.fetchall()
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'properties': data})


def get_surroundings(request):
    property_id = request.GET.get('property_id')
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM property_surroundings WHERE property_id = {property_id}")
            data = cursor.fetchall()
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'surroundings_data': data})


def insert_surrounding(request):
    try:
        body = json.loads(request.body)
        property_id = body.get('property_id')
        title = body.get('title')
        desc = body.get('desc')
        distance = body.get('distance')
        property_type = body.get('type')
        with connection.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO property_surroundings(property_id, title,desc,distance,property_type) values({property_id}, '{title}', '{desc}', {distance}, '{property_type}') returning *")
            data = cursor.fetchall()
        return JsonResponse({'inserted data': data})
    except json.decoder.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON body.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def send_msg(request):
    body = json.loads(request.body)
    parameters = body.get('parameters',{})
    name = parameters[0].get('value','')
    phone = request.GET.get('phone')
    template = request.GET.get('template')
    try:
        url = f"https://live-server-11407.wati.io/api/v1/sendTemplateMessage?whatsappNumber=91{phone}"
        payload = {
            "parameters": parameters,
            "broadcast_name": "POC",
            "template_name": template
        }
        headers = {
            "content-type": "text/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJkOTNkMzcyMy05MGI2LTRmZDEtYjg2Ny00NGNmMGZhYjJlNDAiLCJ1bmlxdWVfbmFtZSI6ImRldmVsb3BlckBhbmFyb2NrLmNvbSIsIm5hbWVpZCI6ImRldmVsb3BlckBhbmFyb2NrLmNvbSIsImVtYWlsIjoiZGV2ZWxvcGVyQGFuYXJvY2suY29tIiwiYXV0aF90aW1lIjoiMTAvMjYvMjAyMiAxOToyNTozNCIsImRiX25hbWUiOiIxMTQwNyIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.iHx_Hx4bLwvHO_Cmhhx3DM8BNGtGAe_wQTPEtik1Un0"
        }
        response = requests.post(url, json=payload, headers=headers)
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO user_prompts(user_name, prompt_sent, phone) VALUES('{name}','True', '{phone}') returning *")
            data = cursor.fetchall()
            print(data)
        return JsonResponse({'message data': response.text})
    except json.decoder.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON body.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def add_user_prompt(request):
    breakpoint()
    id  = request.GET.get('id')
    body = json.loads(request.body)
    schedule = body.get('schedule')
    status = 'failed'
    with connection.cursor() as cursor:
        cursor.execute(f"UPDATE user_prompts set sv_scheduled='{schedule}' WHERE id = '{id}' returning *")
        data  = cursor.fetchall()
        if data.length>0:
            status = 'success'
    return JsonResponse({'message data': data, 'status': status});
