from msilib.schema import Component
from random import randint
from urllib import response
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from factoryapp import factory_utils

# Create your views here.



class MobileAPIView(APIView):
    def post(self, request, format=None):
        data = request.data
        components_list = data["components"]
        try:
            for com_ele in components_list:
                if com_ele.isupper():
                    pass
            result_dict = factory_utils.order_summery(components_list)
            final_result = result_dict["order_summery"]
            is_valid = result_dict["is_valid"]
            if is_valid is True:
                return Response(final_result)
            if is_valid is False:
                return Response({"Parts":"Do not chosse duplicate"})
        except:
            except_response = {"request_body":{ "components": ["I","A","D","F","K"] }}
            return Response(except_response)


        
                
        