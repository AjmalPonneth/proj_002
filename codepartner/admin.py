from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([UserSkills, Session, Discussion,
                    Vote, Comment, CommentVote])
