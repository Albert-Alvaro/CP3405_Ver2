from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Question)
admin.site.register(models.MultiChoiceQuestion)
admin.site.register(models.ShortQuestion)
admin.site.register(models.EssayQuestion)
admin.site.register(models.EssayResponse)
admin.site.register(models.ShortResponse)
admin.site.register(models.Choices)