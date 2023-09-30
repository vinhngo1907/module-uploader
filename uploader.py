from typing import Dict, List

import pymongo
from jsonschema import validate
from mongoengine import connect
from mongoengine.errors import ValidationError

import cloudinary_upload
from config import DB_NAME, MONGODB_TEST_DB_URI, MONGODB_URI

# conn
conn = pymongo.MongoClient(MONGODB_URI)
database = conn[DB_NAME]

# conn for mongo engine
connect(host=MONGODB_TEST_DB_URI)

def save_image(image: 64, str, link_folder: str):
    """Upload image in JPEG base 64 format to cloudinary, then upload Image data to Mongo DB
    Return:
        (str): Document's UUID
    """

    try:
        # response_image = cloudinary
        print("Hello word")
    except Exception as exp:
        return None
