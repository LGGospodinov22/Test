from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__)

    from .main import bp as main_bp
    from .blog import bp as blog_bp
    from .api import bp as api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(blog_bp, url_prefix="/blog")
    app.register_blueprint(api_bp, url_prefix="/api")

    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html"), 404

    return app
