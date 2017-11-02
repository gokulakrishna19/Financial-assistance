from django.shortcuts import render


 #Create your views here.
def index(request):
	return render(request, 'machine/index.html')
def detail(request):
	return render(request, 'machine/index.html')
def detail1(request):
	return render(request, 'machine/indexs.html')
def detail2(request):
	return render(request, 'machine/plan.html')
def detail3(request):
	return render(request, 'machine/popup.html')
def detail4(request):
	return render(request, 'machine/login.html')
def detail5(request):
	return render(request, 'machine/logout.html')
def detail6(request):
	return render(request, 'machine/signup.html')
def detail7(request):
	return render(request, '/fixeddeposit/')

def detail8(request):
	return render(request, 'machine/gold.html')
def detail9(request):
	return render(request, 'machine/insurance.html')
def detail10(request):
	return render(request, 'machine/mutual fund.html')
def detail11(request):
	return render(request, 'machine/Real estate.html')
def detail12(request):
	return render(request, 'machine/stock market.html')

