from re import S
from unicodedata import category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InfoSerializer
from .models import Info
from api import serializers


@api_view(['GET'])  
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/info/',
            'method' : 'GET',
            'subcategories' : [],
            'title' : None,
            'position_id' : None,
            'buy_or_sell' : None,
            'description': 'Returns an array of info/posts'
        },
        {
            'Endpoint': '/info/id/',
            'method' : 'GET',
            'subcategories' : [],
            'title' : None,
            'position_id' : None,
            'buy_or_sell' : None,
            'decsription': 'Returns a single info/post'
        },
        {
            'Endpoint': '/notes/create/',
            'method' : 'POST',
            'subcategories' : [],
            'title' : None,
            'position_id' : None,
            'buy_or_sell' : None,
            'description': 'Creates new info/post with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method' : 'PUT',
            'subcategories' : {'subcategories':"[]"},
            'title': {'title': ""},
            'position_id': {'position_id': ""},
            'buy_or_sell': {'buy_or_sell': ""},
            'description': 'Updates an existing info/post with data sent in'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method' : 'DELETE',
            'subcategories' : [],
            'title' : None,
            'position_id' : None,
            'buy_or_sell' : None,
            'description': 'Deletes an existing info/post'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getInfo(request):
    info=Info.objects.all()
    serializer = InfoSerializer(info, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSingleInfo(request, pk):
    singleinfo = Info.objects.get(id=pk)
    serializer = InfoSerializer(singleinfo, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createInfo(request):
    data=request.data

    info = Info.objects.create(
        title = data['title'],
        position_id = data['position_id'],
        buy_or_sell = data['buy_or_sell'],
        subcategories = (data['subcategories']),
    )
    serializer = InfoSerializer(info, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateInfo(request, pk):
    data=request.data

    info = Info.objects.get(id=pk)

    serializer = InfoSerializer(info, data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteInfo(request, pk):
    info = Info.objects.get(id=pk)
    info.delete()
    return Response('Post deleted successfully')