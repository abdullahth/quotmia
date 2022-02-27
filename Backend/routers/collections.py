from flask import Flask, request, jsonify, Response
import json
import pandas as pd
import numpy as np



def setup(app: Flask, key: str):

    app.route('/', methods=['GET'])
    def get_all_collections():
        pass


    app.route('/<id>', methods=['GET'])
    def get_collection_by_id(id: str):
        pass


    app.route('/', methods=['POST'])
    def create_collection():
        pass


    app.route('/<id>', methods=['PATCH'])
    def patch_collection(id: str):
        pass


    app.route('/<id>', methods=['DELETE'])
    def delete_collection(id: str):
        pass
