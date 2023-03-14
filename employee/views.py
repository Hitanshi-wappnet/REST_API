from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from employee.serializers import EmployeeSerializer
from employee.models import Employee


# Create your views here.
class EmployeeView(APIView):
    """
    List all Employees with the GET Request.
    """

    def get(self, request, pk=None):
        if pk is not None:
            emp = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)
        else:
            emp = Employee.objects.all()
            serializer = EmployeeSerializer(emp, many=True)
            return Response(serializer.data)

    """
    create a new Employee using POST Method.
    """

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created"},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Update a Employees using PUT Method.
    """

    def put(self, request, pk):
        emp = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Partially Update Employee using PATCH Method.
    """

    def patch(self, request, pk):
        emp = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(emp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Partial Data Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Delete Employee using  Method.
    """

    def delete(self, request, pk):
        emp = Employee.objects.get(pk=pk)
        emp.delete()
        return Response({"msg": "Data Deleted"})
