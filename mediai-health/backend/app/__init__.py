from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import redis
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
jwt = JWTManager()
limiter = Limiter(key_func=get_remote_address)
redis_client = redis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379'))


def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Configuration
    app.config.update(
        SECRET_KEY=os.getenv('SECRET_KEY', 'dev-secret-key'),
        SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY'),
        JWT_ACCESS_TOKEN_EXPIRES=3600,
        GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY'),
        MAX_CONTENT_LENGTH=16 * 1024 * 1024,  # 16MB max upload
    )
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    CORS(app, origins=[os.getenv('FRONTEND_URL', 'http://localhost:3000')])
    limiter.init_app(app)
    
    # Register blueprints
    from app.routes.symptoms import symptoms_bp
    from app.routes.chat import chat_bp
    from app.routes.drugs import drugs_bp
    from app.routes.auth import auth_bp
    from app.routes.health import health_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(symptoms_bp, url_prefix='/api/symptoms')
    app.register_blueprint(chat_bp, url_prefix='/api/chat')
    app.register_blueprint(drugs_bp, url_prefix='/api/drugs')
    app.register_blueprint(health_bp, url_prefix='/api/health')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    @app.route('/health')
    def health_check():
        return {'status': 'healthy', 'service': 'mediai-health-api'}
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=8001)


# Updated: 2026-06-03T13:07:00

# Updated: 2026-06-26T12:56:00

# Updated: 2026-06-26T11:45:00

# Updated: 2026-07-27T10:21:00

# Updated: 2026-06-05T13:26:00

# Updated: 2026-06-27T16:07:00

# Updated: 2026-10-24T16:49:00

# Updated: 2026-07-05T22:24:00

# Updated: 2026-10-09T18:38:00

# Updated: 2026-08-27T09:53:00

# Updated: 2026-10-24T11:35:00

# Updated: 2026-07-11T11:41:00

# Updated: 2026-05-23T16:21:00

# Updated: 2026-06-23T18:33:00

# Updated: 2026-07-29T14:37:00

# Updated: 2026-11-17T11:20:00

# Updated: 2026-07-03T15:38:00

# Updated: 2026-06-27T14:27:00

# Updated: 2026-06-24T11:31:00

# Updated: 2026-10-19T12:26:00

# Updated: 2026-07-14T22:00:00

# Updated: 2026-11-22T13:12:00

# Updated: 2026-10-26T12:25:00
