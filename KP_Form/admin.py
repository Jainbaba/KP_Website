from django.contrib import admin
from .models import State, FamilyDetails, QualificationName, QualificationType, Person

admin.site.register(State)
admin.site.register(FamilyDetails)
admin.site.register(QualificationType)
admin.site.register(QualificationName)
admin.site.register(Person)