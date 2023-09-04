#!/usr/bin/python3
"""creates a flask Blueprint and imports all myviews which use Blueprint"""

from flask import Blueprint
app_views = Blueprint('app_myviews', __name__, url_prefix='/api/v1')
from api.v1.myviews.songs import *
from api.v1.myviews.song_word import *
from api.v1.myviews.interpretations import *
from api.v1.myviews.words import *
from api.v1.myviews.suggestions import *
from api.v1.myviews.words_api import *
