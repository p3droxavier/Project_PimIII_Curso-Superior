# Aqui é a entrada do sistema. Importa o app e executa ele. 
from app import create_app

app = create_app()

if __name__ == "__main__":
  app.run(debug=True)