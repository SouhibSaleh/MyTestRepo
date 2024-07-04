import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serialize import mySerializers
from firstapp.models import myitem
from .colorouput import mycolors


def pp():
    mycolors.print_blue(
        "/////////////////////////////////////////////////////////")


@api_view(['GET'])
def getData(requset):
    temp = myitem.objects.all()
    ser = mySerializers(temp, many=True)
    return Response(ser.data)


@api_view(['POST'])
def postData(request):
    temp = mySerializers(data=request.data)
    mycolors.print_blue(json.dumps(request.data, indent=4))

    if temp.is_valid():
        temp.save()
        return Response(temp.data)
    else:
        return Response(temp.errors)


@api_view(['DELETE'])
def delData(request, pk):
    try:
        item = myitem.objects.get(name=pk)
    except myitem.DoesNotExist:
        return Response("")
    item.delete()
    return Response("")


@api_view(['PUT'])
def upData(request):

    myid = request.data.get('id')
    myage = request.data.get('age')
    t = myitem.objects.get(id=int(myid))
    t.age = myage
    t.save()
    return Response(mySerializers(t).data)
