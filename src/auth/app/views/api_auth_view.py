import json
# framework
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout

from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

# https://www.it-swarm.dev/ja/django/django-rest-framework-remove-csrf/1052949749/
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class ApiLoginAuth(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request):
        params = json.loads(request.body)
        email = params['email']
        password = params['password']
        # https://docs.djangoproject.com/en/3.0/topics/auth/default/#how-to-log-a-user-in
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': True})
        else:
            return JsonResponse({'status': False})

    def delete(self, request):
        logout(request)
        return JsonResponse({'status': True})

class RedirectToAllAuthLogin(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request):
        return redirect('/admin/login/')
