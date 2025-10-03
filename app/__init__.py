# Aqui centraliza a criação do flask app e o registro dos Blueprints
from flask import Flask


# Criando a aplicação
def create_app():
  app = Flask(__name__)
  
  # Importando os Blueprints
  from app.auth.routes import auth
  from app.dashboard.routes import dashboard
  
  # Registra os Blueprints
  app.register_blueprint(auth, url_prefix="/auth")
  app.register_blueprint(dashboard, url_prefix="/dashboard")
  
  return app
  
