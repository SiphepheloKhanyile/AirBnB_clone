#!/usr/bin/env python3
"""
Module for `City` Class which inherits from `BaseModel`
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherits from BaseModel Class
    """
    state_id = ""
    name = ""
