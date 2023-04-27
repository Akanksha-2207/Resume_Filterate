from django.db import models
from django import forms
import io
import os
import re
import nltk
import spacy
import pandas as pd
import docx2txt
from resume_filterate import constants as cs
from spacy.matcher import Matcher
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords 
from resume_parser import resumeparse
from resume_filterate import utils


#import spacy
#spacy.load('en_core_web_sm')
# Create your models here.
class Resume(models.Model):
    pass


