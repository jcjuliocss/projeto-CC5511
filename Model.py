"""."""
from DB import DB


class Model:
    """."""

    def __init__(self):
        """."""
        pass

    def buscar_colunas(self, tabela):
        """."""
        db = DB()
        conn = db.conection()
        cursor = conn.cursor()

        query = 'select column_name from ' +\
                'information_schema.columns where table_name ' +\
                '= \'' + tabela + '\';'

        cursor.execute(query)
        q = cursor.fetchall()
        cursor.close()
        conn.close()

        return q

    def inserir_usuario(self, nome, login, senha):
        """."""
        db = DB()
        conn = db.conection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO usuarios(nome, login, senha) \
                VALUES(%s, %s, %s)", (nome, login, senha))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

        return True

    def buscar_usuario(self, login, senha):
        """."""
        db = DB()
        conn = db.conection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE login = %s\
            AND senha = %s;', (login, senha))

        valores = cursor.fetchall()

        cursor.close()
        conn.close()

        return valores

    def buscar_perguntas(self):
        """."""
        db = DB()
        conn = db.conection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM perguntas;")

        valores = cursor.fetchall()
        lista_colunas = self.buscar_colunas('perguntas')
        q = db.monta_retorno(lista_colunas, valores)

        cursor.close()
        conn.close()

        return q
