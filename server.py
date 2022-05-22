import json
from flask import Flask, Response, request
from flask_cors import CORS
import db

app = Flask(__name__)
CORS(app)

_tree={}

@app.route("/getChildren", methods=['GET'])
def getChildren():
    node_id = request.args.get('node_id', None, int)
    nodes=None
    if _tree.keys().__contains__(node_id):
        nodes= _tree[node_id]
    else:
        nodes = db.getChildren(node_id)
        _tree[node_id]=nodes
    resp = Response()
    resp.content_type='application/json'
    if nodes is None:
        resp.response='no such node exists'
        resp.status_code=404
    else:
        resp.response=json.dumps(nodes)
    return resp