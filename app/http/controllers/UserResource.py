from api.resources import Resource
from app.User import User
from api.serializers import JSONSerializer

class UserResource(Resource, JSONSerializer):
    model = User