from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MultiplicationSerializer

class MultiplicationView(APIView):    
  def post(self, request):
    serializer = MultiplicationSerializer(data=request.data)
    if serializer.is_valid():
      number1 = serializer.validated_data['number1']
      number2 = serializer.validated_data['number2']
      result = number1 * number2
      
      return Response(
        {
          'result': result,
          'numbers': {
            'number1': number1,
            'number2': number2
          }
        },
        status=status.HTTP_200_OK
      )
    return Response(
      serializer.errors,
      status=status.HTTP_400_BAD_REQUEST
    )