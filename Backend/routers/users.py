from flask import Flask, request, jsonify, Response
import json
import pandas as pd
import numpy as np



def setup(app: Flask, key: str):

    app.route('/', methods=['GET'])
    def get_all_users():
        pass


    app.route('/<id>', methods=['GET'])
    def get_user_by_id(id: str):
        pass


    app.route('/', methods=['POST'])
    def create_user():
        pass


    app.route('/<id>', methods=['PATCH'])
    def patch_user(id: str):
        pass


    app.route('/<id>', methods=['DELETE'])
    def delete_user(id: str):
        pass
