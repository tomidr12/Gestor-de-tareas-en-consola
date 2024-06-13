import funciones

#Bucle Principal

while True:
  #Menu de opciones en pantalla
  print("\n**************************************************")
  print("***** --- Gestor de tareas de EstudioAud --- *****")
  print("**************************************************\n")
  print("1. Añadir Tarea")
  print("2. Ver Tareas")
  print("3. Marcar tarea como completada")
  print("4. Eliminar Tarea")
  print("5. Salir")

  # Entrada del usuario
  opcion = input("\nIngrese una opcion: ")
  
  #Logica de menu de opciones
  if opcion == "1":
    funciones.agregar_tarea(funciones.tareas)
  elif opcion == "2":
    funciones.ver_tareas(funciones.tareas)
  elif opcion == "3":
    funciones.marcar_tarea(funciones.tareas)
  elif opcion == "4":
    funciones.eliminar_tarea(funciones.tareas)
  elif opcion == "5":
    print("\nGracias por usar el gestor de tareas de EstudioAud")
    break
  else:
    print("\nOpcion no valida")
    input("\nPresione enter para continuar")
    print("\n")
  
  