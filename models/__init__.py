#!/usr/bin/python3
"""its a init func for models"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
