from email.policy import default
from mongoengine.document import Document
from mongoengine.fields import EnumField, LongField, ListField, StringField, DateTimeField, DictField
from mongoengine.errors import ValidationError
from utils import convertLocalTimeToUTCTime
from bson.objectid import ObjectId
from datetime import datetime
from enum import Enum
import time

_MAX_SIZE_IMAGES = 2

def RetricLengthMaxImages(list_image):
    if(len(list_image) > _MAX_SIZE_IMAGES):
        raise ValidationError("List images exceed max size: ", _MAX_SIZE_IMAGES)

class VehicleTypes(Enum):
    CAR = 'Car'
    MOTORCYCLE = "Motorcycle"
    BUS = "Bus"
    TRUCK = "Truck"
    BICYCLE = "Bicycle"

    def RetrictLengthMaxLengthImage(list_image):
        if(len(list_image) > _MAX_SIZE_IMAGES):
            raise ValidationError("List images exceed max size: ", _MAX_SIZE_IMAGES)
        
class Vehicles(Document):
    camera_id = StringField(required=True)
    video_id = StringField(required=True)
