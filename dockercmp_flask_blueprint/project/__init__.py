from flask import Flask
from flask_assets import Environment, Bundle
from config import Config

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    
    assets = Environment(app)
    assets.init_app(app)

    with app.app_context():
        from .assets import compile_assets
        from .home import home
        from .about import about

        app.register_blueprint(home.home_bp)
        app.register_blueprint(about.about_bp)
        compile_assets(assets)
        return app
