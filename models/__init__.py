#!/usr/bin/python3
"""
__init__ dunder method for the models directory
"""
from models.engine.file_storage import FileStorage


d_base = FileStorage()
d_base.reload()
