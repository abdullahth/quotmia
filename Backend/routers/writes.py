from flask import Flask, request, jsonify, Response
import json
import pandas as pd
import numpy as np



def setup(app: Flask, key: str):

    app.route('/', methods=['GET'])
    def get_all_write():
        pass


    app.route('/<id>', methods=['GET'])
    def get_write_by_id(id: str):
        pass


    app.route('/', methods=['POST'])
    def create_write():
        pass


    app.route('/<id>', methods=['PATCH'])
    def patch_wrtie(id: str):
        pass


    app.route('/<id>', methods=['DELETE'])
    def delete_user(id: str):
        pass
