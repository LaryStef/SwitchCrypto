from flask_restx import Namespace, Resource
from flask import request, make_response, jsonify
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import BadRequest

from ..database.redisdb import rediska
from ..shemas import RegisterSchema
from ..database.redisdb.services import create_register_request


api = Namespace("auth", path="/auth/")


@api.route("/sign-up")
class Sign_up(Resource):
    def post(self):
        try:
            # data = RegisterSchema().load(datadict)
            data = request.form.to_dict()

            if RegisterSchema().validate(data):
                raise BadRequest
            if data.get("email") in rediska.json().get("register", "$..email"):    # type: ignore
                raise BadRequest
            
            # TODO check uniqueness of username

            response = make_response("OK")
            response.status_code = 200
            response.headers["request-Id"] = create_register_request(data)

            return response
        except BadRequest:
            return "Bad request", 400


@api.route("/sign-in")
class Sign_in(Resource):
    def post(self):
        data = request.form        
        return make_response(jsonify(data), 200)
