from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'pub_date', 'was_published_recently']
    fieldsets = [("Question Info!",{'fields':['question']}),
("Date Information",{'fields':['pub_date'], "classes":['collapse']})]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
