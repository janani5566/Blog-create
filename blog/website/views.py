from django.shortcuts import render,HttpResponse,get_object_or_404
from website.models import Blogpost

# Create your views here.
def home(request):
    blogposts = Blogpost.objects.all()
    context = {
        'blogposts':blogposts
    }
    return render(request,'home.html',context)

def postdetails(request,slug):
    postdetail = get_object_or_404(Blogpost,slug=slug)
    context = {
        'postdetail':postdetail
    }
    return render(request,'postdetails.html',context)