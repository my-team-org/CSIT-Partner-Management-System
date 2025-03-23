from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('review_page')
    else:
        form = ReviewForm()
    
    reviews = Review.objects.all()  # แสดงรีวิวทั้งหมด
    return render(request, 'review/review.html', {'form': form, 'reviews': reviews})