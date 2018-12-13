import os

from flask_demo import create_app

if __name__ == '__main__':
    port = os.getenv('PORT')
    app = create_app()
    app.run(host='0.0.0.0', port=port)
