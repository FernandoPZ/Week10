import web 

render=web.template.render('page/views/alumnos/')

class Insert():
    def GET(self):
      try:
        return render.insert()
      except Exception as e:
        return "--E-R-R-O-R--" + str(e.args)
        
    def POST(self):
      try:
        form = web.input()
        print(form)
        print(form.matricula)
        print(form.nombre)
        print(form.papellido)
        print(form.sapellido)
        print(form.edad)
        print(form.naci)
        print(form.genero)
        print(form.estado)
        return render.insert()
      except Exception as e:
        return "--E-R-R-O-R--" + str(e.args)