from django.shortcuts import render

from .form import ReviewForm

from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Bid
# Create your views here.

class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form) -> HttpResponse:
        form.send_email()
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        review = form.cleaned_data['review']

        Bid.objects.get_or_create(
            name = name,
            email = email,
            review = review
        )   
      
        msg = "Thanks for the review"
        return HttpResponseRedirect('/')    

def home(request):
    return render(request,'base.html')
