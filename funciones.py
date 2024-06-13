#Lista de Tareas
tareas = []

def agregar_tarea(lista):
  # Entrada para la tarea
  tarea = input("\nIngrese la tarea a realizar: ")
  
  if tarea != "":
    lista.append(tarea)
    
  # Informa de tarea añadida
    print("\n*******************************************")
    print("***** --- Tarea añadida con exito --- *****")
    print("*******************************************\n")
    
  # Imprime la tarea añadida
    print("------------------------------------------------")
    print(tarea)
    print("------------------------------------------------")

  # Informa del numero de tarea
    print(f"\nNumero de tarea: {len(lista)}")
  
def ver_tareas(lista):

  # Condicional que evalue si hay algo en la lista
  if lista:
    
    # Si hay algo en la lista se presenta
    print("\n***********************************")
    print("***** --- Lista de tareas --- *****")
    print("***********************************\n")
    
    for i in range(len(lista)):
      print(f"{i+1}. {lista[i]}")
      
  else:
    #Si la lista esta vacia se avisa de ello
    print("\n*********************************")
    print("***** --- No hay tareas --- *****")
    print("*********************************\n")
    
  #Mensaje de fin de listado 
  print("--- FIN DEL LISTADO DE TAREAS ---")
  
def marcar_tarea(lista):
  print(lista)

def eliminar_tarea(lista):
  print(lista)