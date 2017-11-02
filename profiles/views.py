from django.shortcuts import render, redirect

from .forms import profileform
from .models import profiles
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

# Create your views here.



def index(request):
    
    if request.method == 'POST':
    

        form = profileform(request.POST)
       
        if form.is_valid():

        	post = form.save(commit=False)

        	post.save()
        	
            
            

        	form  = profileform()
            
            
            


            #all_profile = profiles.objects.all()
        	
           # return redirect('profiles/popup.html')
    else:
        form = profileform()
        


        
	        
    
    all_profile = profiles.objects.all() 
    return render(request,
	'profiles/popup.html',
	{'form': form, 'profile':all_profile} )