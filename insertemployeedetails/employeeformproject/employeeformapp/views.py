from django.shortcuts import render


from employeeformapp.forms import EmployeeForm
from employeeformapp.models import Employee

# Create your views here.
def home_page(request):
	return render(request=request, template_name='html/employeeformapp/homepage.html')

def insert_details_page(request):
	return render(request=request, template_name='html/employeeformapp/homepageinput.html')

def select_records(request):
	emp_list=Employee.objects.all()

	my_dict={'emp_list' : emp_list}
	return render(request=request, template_name='html/employeeformapp/display1.html',context=my_dict)


def insert_records(request):
	emp_form=EmployeeForm()

	if request.method=="POST":
		emp_data=EmployeeForm(request.POST)
		if emp_data.is_valid():
			emp_data.save(commit=True)

	if request.method=="POST":
		emp_data=EmployeeForm(request.POST)
		if emp_data.is_valid():
			print(f'Name : {emp_data.cleaned_data["name"]}')
			print(f'Age : {emp_data.cleaned_data["age"]}')
			print(f'Address : {emp_data.cleaned_data["address"]}')

	my_dict={'emp_form' : emp_form}

	return render(request=request, template_name='html/employeeformapp/display.html',context=my_dict)
