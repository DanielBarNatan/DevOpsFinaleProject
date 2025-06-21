from flask import Flask, Blueprint, request, jsonify, Response, render_template
from datetime import datetime
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from .metrics import REQUEST_COUNTER, AGE_LEGAL_COUNTER, AGE_ILLEGAL_COUNTER


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/check-age", methods=["POST"])
def check_age():
    REQUEST_COUNTER.inc()
    data = request.get_json()
    birth_date_str = data.get("birth_date")

    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        today = datetime.today()
        age = (today - birth_date).days // 365
        is_legal = age >= 18
        if is_legal:
            AGE_LEGAL_COUNTER.inc()
        else:
            AGE_ILLEGAL_COUNTER.inc()
        return jsonify({"legal": is_legal, "age": age}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@main_bp.route("/requests", methods=["GET"])
def requests_count():
    count = REQUEST_COUNTER._value.get()
    return jsonify({"total_requests": int(count)}), 200


@main_bp.route("/health")
def health():
    return "OK", 200


@main_bp.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


# @main_bp.route("/cicd-test")
# def cicd_test():
#     return "CI/CD Pipeline Working!", 200


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app
