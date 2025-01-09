from flask import Flask
from config import Config
import logging
import sys
from routes.assistant import assistant_bp
from dotenv import load_dotenv

def create_app(config_class=Config):
    """
    Create and configure the Flask application.
    
    Args:
        config_class: Configuration class for the application
        
    Returns:
        Flask application instance
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Basic logging configuration
    logging.basicConfig(level=logging.INFO)
    app.logger.setLevel(logging.INFO)
    
    # Setup console logging
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    app.logger.addHandler(console_handler)
    
    # Register blueprints
    app.register_blueprint(assistant_bp)

    return app

load_dotenv()
app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['FLASK_DEBUG']) 