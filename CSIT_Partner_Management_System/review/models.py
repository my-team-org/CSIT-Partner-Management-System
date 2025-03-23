from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Review(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    recommend = models.BooleanField()
    overall_rating = models.IntegerField()
    benefits_rating = models.IntegerField()
    environment_rating = models.IntegerField()
    management_rating = models.IntegerField()
    job_type = models.CharField(max_length=255)
    job_description = models.TextField()
    experience = models.TextField()
    advice = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.company.name}'

# filepath: /d:/Working Homework/year3/SE/csitcoop/review/admin.py
