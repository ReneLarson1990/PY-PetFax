from flask import Flask 

def create_app(): 
    app = Flask(__name__)
    
    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'
    
    from.import pets
    app.register_blueprint(pets.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    return app
