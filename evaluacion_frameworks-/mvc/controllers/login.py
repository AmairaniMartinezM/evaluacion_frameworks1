import web
from mvc.model.modelo_login import ModeloLogin

render = web.template.render('mvc/views/')

m_login = ModeloLogin() # Instancia de la clase ModeloIndex

class Login:
    def GET(self):
        try:
            return render.login(username=None, password=None, resultado=None)
        except Exception as e:
            print(f"Error  - login(){e.args}")
            return None
        
    def POST(self):
        try:
            form = web.input()
            username = form.username
            password = form.password
            resultado = m_login.consulta(username, password)
            if resultado == "si":
                web.setcookie("username", username, expires="", domain=None, secure=False)
                return render.pagina(username)
            else:
                return render.login(username=None, password=None, resultado=None)
            
        except Exception as e:
            print(f"Error login (){e.args}")
            return "no"
            