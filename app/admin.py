from django.contrib import admin

# Register your models here.
from app.models import King, Kingdom, Subordinate, Question, Answer, Accept

admin.site.register(King)
admin.site.register(Kingdom)
admin.site.register(Subordinate)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Accept)