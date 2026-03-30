from flask import Blueprint, flash, render_template, request
from flask_login import login_required


robot_control = Blueprint("robot_control", __name__)


@robot_control.route("/robot", methods=["GET", "POST"])
@login_required
def dashboard():
    command_sent = None
    if request.method == "POST":
        command_sent = request.form.get("command")
        if command_sent:
            flash(f"Robot command sent: {command_sent}", "success")
    return render_template("robot_dashboard.html", command_sent=command_sent)
