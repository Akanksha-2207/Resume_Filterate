from django.db import models
from resume_parser import resumeparse
import spacy
spacy.load('en_core_web_sm')
# Create your models here.
class Resume(models.Model):
      nlp = spacy.load("en_core_web_sm")
      data = resumeparse.read_file('/media')