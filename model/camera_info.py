from mongoengine.document import Document, QuerySet
from mongoengine.fields import EnumField, DateTimeField, StringField, ListField, DictField, IntField, BooleanField
from bson.objectid import ObjectId
from random import choice
from tokenize import String
from enum import Enum
from datetime import datetime

class StreamingTypes(Enum):
    YOUTUBE="YOUTUBE",
    RTSP="RTSP"

class CameraInfos(Document):
    camera_name = StringField(required=True)
    camera_alias = StringField(required=True)
    camera_url = StringField(required=True)
    streaming_type = EnumField(StreamingTypes,required= True)
    address=DictField(default = {
        "lat": 0,
        "long": 0,
        "name": ""
    })
    status = BooleanField(required=True, default=False)
    roi_points = ListField(ListField(IntField(), max_length=2), default=[], required=True)
    lp_roi_points = ListField(ListField(IntField(), max_length=2), default=[])
    direction_vector = ListField(IntField(), max_length=2, default=[0,0], required = True)

    updated_at=DateTimeField(default=datetime.now())
    created_at=DateTimeField(default=datetime.now())
