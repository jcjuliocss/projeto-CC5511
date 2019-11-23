"""."""
import psycopg2


class DB:
    """."""

    def __init__(self):
        """."""
        pass

    def conection(self):
        """."""
        conn = \
            psycopg2.connect(user="xqcfpjqsanbhpa",
                             password="ec295620870456a69cedc3a43ab9ffa2\
                                      44511e0033af2587df7f363d318e509c",
                             host="ec2-107-22-239-155.compute-1.amazonaws.com",
                             port="5432",
                             database="d9755uu1fjnkn3")

        return conn

    def monta_retorno(self, colunas, valores):
        """."""
        retorno = []
        for i in range(len(valores)):
            dict = {}
            for j in range(len(colunas)):
                dict[colunas[j][0]] = valores[i][j]
            retorno.append(dict)

        return retorno
