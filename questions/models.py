from django.db import models

# Create your models here.
class MultiChoiceQuestion(models.Model):
    question = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class ShortQuestion(models.Model):
    question = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class EssayQuestion(models.Model):
    question = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class EssayResponse(models.Model):
    question = models.ForeignKey(EssayQuestion, null=False, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ShortResponse(models.Model):
    question = models.ForeignKey(ShortQuestion, null=False, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Choices(models.Model):
    mcq = models.ForeignKey(MultiChoiceQuestion, null=True, on_delete=models.CASCADE)
    choice = models.CharField(max_length=5000)

    def __str__(self):
        return self.choice