from django.contrib import admin
from . import models 


admin.site.register(models.Contact)
admin.site.register(models.Portfolio)
admin.site.register(models.Testimonial)
admin.site.register(models.Payment)
admin.site.register(models.Team)


