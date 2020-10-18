from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class SampleView(APIView):
    def get(self,request,format=None):
        return Response({'name':"Hemanth",'message':"GET"})

    def post(self,request,format=None):
        return Response({'name':"Hemanth",'message':"POST"})

    def put(self,request,format=None):
        return Response({'name':"Hemanth",'message':"PUT"})

    def patch(self,request,format=None):
        return Response({'name':"Hemanth",'message':"PATCH"})

    def delete(self,request,format=None):
        return Response({'name':"Hemanth",'message':"DELETE"})
