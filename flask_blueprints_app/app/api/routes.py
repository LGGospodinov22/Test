from flask import jsonify

from app.data import POSTS

from . import bp


@bp.route("/health")
def health():
    return jsonify({"status": "ok"})


@bp.route("/posts")
def posts():
    return jsonify(POSTS)
