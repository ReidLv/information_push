from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class Test(APIView):
	def get(self,request):
		print 'hello'
		return render(request,'hello.html')

