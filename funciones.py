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
  print("\n--- FIN DEL LISTADO DE TAREAS ---")
  
def marcar_tarea(lista):
  # Llamamos a la funcion ver tareas
  ver_tareas(lista)
  # Entrada para que el usuraio introduzca una tarea
  completada = int(input("\nIntroduzca el numero de la tarea a marcar como completada: "))
  # Condicional para marcar las tareas completadas
  if completada > 0 and completada <= len(lista):
    # Condicional para evaluar si la tarea ya esta completada
    # Si la tarea ya esta completada
    if "(Completada)" in lista[completada - 1]:
      print("La tarea ya esta completada")
    # Si la tarea no esta completada
    else:
      # Marcar la tarea como completada
      lista[completada - 1] = f"{lista[completada - 1]} (Completada)"
      print("\n*************************************************")
      print("***** --- Tarea marcada como completada --- *****")
      print("*************************************************\n")
  # Avisar si la opcion elegida es invalida
  else:
    print("\nLa opcion elegida no es valida")

def eliminar_tarea(lista):
  # Si la lista contiene algo
  if lista:
    # Llamamos a la funcion ver_tareas()
    ver_tareas(lista)
    # Entrada para que el usuario introduza una tarea
    tarea_a_eliminar = int(input("\nIngrese el numero de la tarea que quiere eliminar: "))
    # Opcion invalida si la atrea no esta en el rango de la lista
    if tarea_a_eliminar <= 0 or tarea_a_eliminar > len(lista):
      print("\nLa opcion elegida no es valida")
    # Si la opcion es valida se elimina la tarea
    else:
      # Se elimina la tarea
      del lista[tarea_a_eliminar - 1]
      print("\n*********************************************")
      print("***** --- Tarea eliminada con exito --- *****")
      print("*********************************************\n")
  # Si la lista esta vacia se avisa de ello
  else:
    print("\n*********************************")
    print("***** --- No hay tareas --- *****")
    print("*********************************\n")