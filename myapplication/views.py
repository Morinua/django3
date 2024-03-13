from django.shortcuts import render
from myapplication.serializers import EmployeesSerializer
from myapplication.models import Employees
from django.http import JsonResponse
# Create your views here.
def employeesview(request):
  employee = Employees.objects.all()
  serializer = EmployeesSerializer(employee, many=True)
  return JsonResponse({"employee":serializer.data},safe=False)
