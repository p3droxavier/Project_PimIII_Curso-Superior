# Blueprint para autentificação
from flask import Blueprint, flash, render_template, redirect, request, session, url_for
import json, os
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)


# Caminho para o arquivo json que ira armazenar os usuários
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "users.json")


# função auxiliar para o arquivo JSON
def load_users():
  if not os.path.exists(DATA_FILE): 
    return[]
  with open(DATA_FILE, "r", encoding="utf-8") as f:
    return json.load(f)
  
  
# função auxiliar para salvar usuários
def save_user(users):
  with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(users, f, indent=4, ensure_ascii=False)



# -------------------------
# Rotas do Login e Register
# -------------------------

# Criação da rota register e o salvamento do profissional no arquivo
@auth.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    nome = request.form.get("nome")
    email = request.form.get("email")
    documento = request.form.get("cpf")
    especialidade = request.form.get("especialidade")
    cargo = request.form.get("cargo")
    senha = request.form.get("senha")
    contato = request.form.get("telefone")
    senha = request.form.get("senha")
    confirma_senha = request.form.get("confirma_senha")
    
    # Carrega usuário existentes
    users = load_users()
    
    # Verifica duplicados
    if any(u["email"] == email for u in users):
      flash("E-mail já cadastrado!", "error")
      return redirect(url_for("auth.register"))
    
    if senha != confirma_senha:
      flash("As senhas não coincidem!", "error")
      return redirect(url_for("auth.register"))
    
    
    # Cria novo usuário
    new_user = {
      "nome": nome,
      "email": email,
      "documento": documento,
      "especialidade": especialidade,
      "cargo": cargo,
      "senha": generate_password_hash(senha) # senha criptografada
    }
    
    users.append(new_user)
    save_user(users)
    
    flash("Cadastro realizado com sucesso!", "success")
    return redirect(url_for("auth.login"))
    
  return render_template("register.html")



# Criação da rota de login e a verificação com os dados já salvos
@auth.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form.get("email")
    senha = request.form.get("senha")
    
    users = load_users()
    user = next((u for u in users if u["email"] == email), None)
    
    if user and check_password_hash(user["senha"], senha):
      # Guarda sessão 
      session["user"] = {
        "nome":user["nome"],
        "email":user["email"],
        "documento":user["documento"],
        "especialidade":user["especialidade"],
        "cargo":user["cargo"]
      }
      
      flash("Login realizado!", "success")
      return redirect(url_for("dashboard.admin_dashboard"))
    
    else: 
      flash("Credenciais inválidas!", "error")
      return redirect(url_for("auth.login"))
    
  return render_template("login.html")



@auth.route("/logout")
def logout():
  session.pop("user", None)
  flash("Sessão encerrada!", "info")
  return redirect(url_for("auth.login"))