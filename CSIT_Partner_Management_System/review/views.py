from django.shortcuts import render, redirect
from .models import Review, Company, JobPosition
from .forms import ReviewForm
from django.contrib import messages

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            messages.success(request, "ส่งรีวิวเรียบร้อยแล้ว")
            return redirect('review_page')
    else:
        form = ReviewForm()

    # ✅ กรองเฉพาะบริษัทที่ยังไม่เคยถูกรีวิว
    reviewed_company_ids = Review.objects.values_list('company_id', flat=True)
    form.fields['company'].queryset = Company.objects.exclude(id__in=reviewed_company_ids)

    reviews = Review.objects.all()

    # ✅ ดึงประเภทงานจาก JobPosition (เฉพาะที่ไม่ซ้ำกัน)
    job_types = JobPosition.objects.values_list('job_type', flat=True).distinct()

    return render(request, 'review/review.html', {
        'form': form,
        'reviews': reviews,
        'job_types': job_types  # ✅ ส่งไปให้ template
    })
