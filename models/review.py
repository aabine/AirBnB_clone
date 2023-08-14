#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    """A review of a place"""
    place_id = ""
    user_id = ""
    text = ""