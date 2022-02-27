from flask import Flask, request, jsonify, Response
import json
import pandas as pd
import numpy as np



def setup(app: Flask, key: str):

    app.route('/', methods=['GET'])
    def get_all_quotes():
        pass


    app.route('/<id>', methods=['GET'])
    def get_quote_by_id(id: str):
        pass


    app.route('/', methods=['POST'])
    def create_quote():
        pass


    app.route('/<id>', methods=['PATCH'])
    def patch_quote(id: str):
        pass


    app.route('/<id>', methods=['DELETE'])
    def delete_quote(id: str):
        pass
