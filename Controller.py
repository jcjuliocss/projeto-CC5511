"""."""
from Model import Model


class Controller:
    """."""

    def __init__(self):
        """."""
        self.model = Model()

    def add_user(self, nome, email, senha):
        """."""
        return self.model.inserir_usuario(nome=nome, login=email, senha=senha)

    def get_perguntas(self):
        """."""
        return self.model.buscar_perguntas()

    def get_usuario(self, login, senha):
        """."""
        return self.model.buscar_usuario(login=login, senha=senha)
