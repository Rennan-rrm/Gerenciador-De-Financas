usuarios=[
    {"id":*********, "nome":"*********"},
    {"id":*********, "nome":"*********"},
    {"id":*********, "nome":"*********"}
]
def identificar_usuario(usuario_id):

   for usuario in usuarios:
       if usuario["id"] == usuario_id:
           return usuario["nome"]
   return False


