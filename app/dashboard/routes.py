from flask import Blueprint, render_template

dashboard = Blueprint("dashboard", __name__)

# -------------------------
# Rotas do Dashboard
# -------------------------
@dashboard.route("/")
def admin_dashboard():
  return render_template("dashboard/admin_dashboard.html")

@dashboard.route("/dashboard/post")
def dashboard_post():
  return render_template("components/postar_nova_tarefa.html")

@dashboard.route("/dashboard/funcionarios")
def dashboard_funcionarios():
  return render_template("components/todos_os_funcionarios.html")

@dashboard.route("/dashboard/setores")
def dashboard_setores():
  return render_template("components/todos_os_setores.html")
