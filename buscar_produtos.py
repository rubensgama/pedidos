import dbmanager
from flask import Flask, url_for, render_template, request, abort, jsonify
from entidades.produto import Produto
import json
from sqlalchemy import Date
from datetime import date, datetime

app = Flask(__name__)


@app.route('/produtos', methods=['GET'])
def buscar(event, context):
    responseBody = json.dumps(dbmanager.find_all(Produto), default=myconverter)
    response = {
        "statusCode": 200,
        "headers": {
        },
        "body": responseBody,
        "isBase64Encoded": False
    }
    return response


def myconverter(obj):
    return obj.tostring()
