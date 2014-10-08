# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from snippet.models import Snippet
# from snippet.serializers import SnippetSerializer
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.http import  Http404
# # this has been added to work with api_view, status and responce
#
# # We'll start off by creating a subclass of HttpResponse that we can
# # use to render any data we return into json
#
# #version 1 where we use JSONResponse to handle request
# # class JSONResponse(HttpResponse):
# #     """
# #     An HttpResponse that renders its content into JSON.
# #     """
# #     def __init__(self, data, **kwargs):
# #         content = JSONRenderer().render(data)
# #         kwargs['content_type'] = 'application/json'
# #         super(JSONResponse, self).__init__(content, **kwargs)
#
#
# #version 1 of the traditional views to handle request
# # we will refactor this code now
# # @csrf_exempt
# # def snippet_list(request):
# #     """
# #     List all code snippets, or create a new snippet.
# #     """
# #     if request.method == 'GET':
# #         snippets = Snippet.objects.all()
# #         serializer = SnippetSerializer(snippets, many=True)
# #         return JSONResponse(serializer.data)
# #
# #     elif request.method == 'POST':
# #         data = JSONParser().parse(request)
# #         serializer = SnippetSerializer(data=data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return JSONResponse(serializer.data, status=201)
# #         return JSONResponse(serializer.errors, status=400)
#
# # # version 2 snippet_list Still Old tech
# # @api_view(['GET', 'POST'])
# # def snippet_list(request, format=None):
# #     """
# #     We have added format because we can call like :
# #      http://example.com/api/items/4.json.
# #      For that we have to update urls.py file too.
# #     List all snippets, or create a new snippet.
# #     """
# #     if request.method == 'GET':
# #         snippets = Snippet.objects.all()
# #         serializer = SnippetSerializer(snippets, many=True)
# #         return Response(serializer.data)
# #
# #     elif request.method == 'POST':
# #         serializer = SnippetSerializer(data=request.DATA)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # Version 3 of Snippet_List
# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# # this version is one of details calling where we use JSonResponse to
# #  work with each request but now we add decoraters and eliminate JSOn code
# # @csrf_exempt
# # def snippet_detail(request, pk):
# #     """
# #     Retrieve, update or delete a code snippet.
# #     """
# #     try:
# #         snippet = Snippet.objects.get(pk=pk)
# #     except Snippet.DoesNotExist:
# #         return HttpResponse(status=404)
# #
# #     if request.method == 'GET':
# #         serializer = SnippetSerializer(snippet)
# #         return JSONResponse(serializer.data)
# #
# #     elif request.method == 'PUT':
# #         data = JSONParser().parse(request)
# #         serializer = SnippetSerializer(snippet, data=data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return JSONResponse(serializer.data)
# #         return JSONResponse(serializer.errors, status=400)
# #
# #     elif request.method == 'DELETE':
# #         snippet.delete()
# #         return HttpResponse(status=204)
#
# # # version 2 snippet_detail This is simply the function view
# # @api_view(['GET', 'PUT', 'DELETE'])
# # def snippet_detail(request, pk, format=None):
# #     """
# #     Retrieve, update or delete a snippet instance.
# #     """
# #     try:
# #         snippet = Snippet.objects.get(pk=pk)
# #     except Snippet.DoesNotExist:
# #         return Response(status=status.HTTP_404_NOT_FOUND)
# #
# #     if request.method == 'GET':
# #         serializer = SnippetSerializer(snippet)
# #         return Response(serializer.data)
# #
# #     elif request.method == 'PUT':
# #         serializer = SnippetSerializer(snippet, data=request.DATA)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# #     elif request.method == 'DELETE':
# #         snippet.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# # Vesion 3 of Snippet_detail This is class based View
# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#

# Version 4 of all above fuctions and class based views
# This is Generic Class view and refactored code also.
# there are no other changes in urls.py cause
# calling of CBV and GCV are the same
#  This code looks too preety.
from snippet.models import Snippet
from snippet.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer