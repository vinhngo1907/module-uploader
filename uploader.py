from typing import Dict, List

import pymongo
from jsonschema import validate
from mongoengine import connect
from mongoengine.errors import ValidationError

import cloudinary_upload
from config import DB_NAME, MONGODB_TEST_DB_URI, MONGODB_URI
from model.images import Images
from model.record_videos import RecordVideos
from schema import ImageInfo

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
        response_image = cloudinary_upload.upload_image(image, link_folder)
        image_data = ImageInfo(
            asset_id=response_image["asset_id"],
            public_id=response_image["public_id"],
            url=response_image["url"],
            secure_url=response_image["secure_url"],
            format=response_image["format"],
            created_at=response_image["created_at"],
        )

        return ImageInfo.asDict()
    except Exception as exp:
        return None


def set_video_get_id(video_record: RecordVideos):
    try:
        video_data: RecordVideos = video_record.save()
        print({video_record})
        return video_data.id
    except ValidationError:
        return Exception("Record video data format is incorrect")
