print("Programa de evaluación de notas de alumnos")

notas_alumno=input("Introduce la nota del alumno")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
		calificacion=7
	return valoracion


print(evaluacion(int(notas_alumno)))