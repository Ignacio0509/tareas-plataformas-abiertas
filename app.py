@@ -0,0 +1,14 @@
desde  flask  importar  Flask , solicitud

aplicación  =  Flask ( __nombre__ )

@ app . route ( '/usuarios' , métodos = [ 'GET' ])
def  usuarios ():
    user_id  =  solicitud . argumentos . get ( 'id' )   # Lee el parámetro 'id' desde la URL
    si  user_id :
        return  f"El id del usuario es { user_id } " , 200
    demás :
        return  "Lista de todos los usuarios". , 200

si  __nombre__  ==  '__principal__' :
    aplicación.ejecutar ( depuración = Verdadero )
