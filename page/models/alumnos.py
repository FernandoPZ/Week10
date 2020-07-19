import mysql.connector

class Alumnos():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root', 
                password='1234',
                host='127.0.0.1',
                port=3308,
                database='escuela'
                )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)

    def select(self):
        try:
            self.connect()
            query = ("SELECT * from alumnos;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                r = {
                    'id_alumno':row[0],
                    'matricula':row[1],
                    'nombre':row[2],
                    'papellido':row[3],
                    'sapellido':row[4],
                    'edad':row[5],
                    'naci':row[6],
                    'genero':row[7],
                    'estado':row[8]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result

objeto = Alumnos()
objeto.connect()

for row in objeto.select():
    print(row)
