#!/usr/bin/env python3
"""
Module for class `User` that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class Inherits from BaseModel Class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
