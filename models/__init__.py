#!/usr/bin/python3
"""
Initialization module
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
