from flask import abort, render_template

from app.data import POSTS

from . import bp


@bp.route("/")
def post_list():
    return render_template("blog/list.html", posts=POSTS)


@bp.route("/<int:id>")
def post_detail(id: int):
    post = next((item for item in POSTS if item["id"] == id), None)
    if post is None:
        abort(404)
    return render_template("blog/detail.html", post=post)
