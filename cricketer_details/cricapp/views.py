from django.shortcuts import render

# Create your views here.
from cricapp.models import cricketerfulldetails

def home_page(request):
	return render(request=request, template_name='html/cricapp/home.html')


def select_record(request):
	emp_list=cricketerfulldetails.objects.all()
	print(emp_list)
	print(type(emp_list))

	my_dict={'emp_list':emp_list}

	return render(request=request, template_name='html/cricapp/disp.html',context=my_dict)