import yt_dlp

def obtener_info_video(url):
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)
        print(f"Título: {info['title']}")
        print(f"Duración: {info['duration']} segundos")
        print(f"Autor: {info['uploader']}")

url = "https://www.youtube.com/watch?v=_bvtdS0QLa8"
obtener_info_video(url)

# Variables numéricas

metros_cuadrados_limpiados = 0
cantidad_producto_necesario = 0
numero_preguntas_evaluacion = 0
resultados_evaluativos = {}
frecuencia_pedidos = 0
puntos_fidelizacion = {}
progreso_formacion_mensual = {}
existencias_producidas = 0
existencias_stock = 0
existencias_vendidas = 0
numero_clientes = 0
numero_clientes_potenciales = 0
numero_proveedores = 0
numero_distribuidores = 0
costos_fijos = 0
costos_variables = 0
utilidad = 0

# Variables de tipo texto

Modulo_educativo = "Aprender a usar las pastillas"
Descripcion = "Descubre como nuestras pastilas transforman la rutina"
Feedback = "Gracias por las respuestas"
Mensaje_final = "Tus comentarios son importantes"
Titulo_programa= "Reconocimiento al cliente destacado"
Descripcion_del_programa = "Celebramos juntos los logros individuales"

# Variables boleano

respuestas = [True, False, True, True, False, True, True, True, True]

# Función que permite verificar el aprendizaje

def verificar_aprendizaje(respuestas):
    """Evalúa las respuestas de una encuesta y devuelve un resumen."""
    if not respuestas:
        return "No hay respuestas para evaluar."

    total_preguntas = len(respuestas)
    respuestas_correctas = sum(respuestas)  # Más directo que la comprensión de listas
    porcentaje = (respuestas_correctas / total_preguntas) * 100

    return f"Porcentaje de respuestas correctas: {porcentaje:.2f}%"

# Ejecución de la función
if __name__ == "__main__":
    resultado = verificar_aprendizaje(respuestas)
    print(resultado)

# Ciclo for

# Definir las estrategias
estrategias = ["Alianza", "Plataformas en línea", "Colaboración"]
 
# Implementar las estrategias
for estrategia in estrategias:
  print(f"Implementando la estrategia de {estrategia}...")
  # Aquí puedes agregar el código para implementar cada estrategia
  print(f"Estrategia de {estrategia} implementada con éxito.")
  # Definir la condición para mejorar la educación y capacitación
mejora_educacion = False
 
# Implementar estrategias hasta que se haya mejorado la educación y capacitación
while not mejora_educacion:
  print("Implementando estrategias para capacitar a aseadores...")
  # Aquí puedes agregar el código para implementar las estrategias
  mejora_educacion = True  # Cambiar a True cuando se haya mejorado la educación y capacitación
  print("Estrategias implementadas con éxito.")

# Impresión de las variables

print(metros_cuadrados_limpiados)
print(cantidad_producto_necesario)
print(Modulo_educativo)
print(Descripcion)
