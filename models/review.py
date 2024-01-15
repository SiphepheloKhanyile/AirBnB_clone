#!/usr/bin/env python3
"""
Module for `Review` Class which inherits from `BaseModel`
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherits from BaseModel Class
    """
    place_id = ""
    user_id = ""
    text = ""
