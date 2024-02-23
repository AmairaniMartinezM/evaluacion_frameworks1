import web 

class ModeloLogin:
    def __init__(self):
        pass

    def consulta(self, username, password):
        try:
            if username == "usuario" and password == "1234":
                return "si"
            else:
                return "no"
        except Exception as e:
            print(f"Error de login {e}")
            return None
 