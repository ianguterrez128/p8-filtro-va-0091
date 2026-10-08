# Ian Gutierrez 0091
import cv2
import os

# Obtener la carpeta donde está este archivo
carpeta_codigo = os.path.dirname(os.path.abspath(__file__))

# Ruta de la imagen
ruta_imagen = os.path.join(
    carpeta_codigo,
    "..",
    "imagenes",
    "camello 0091.jpg"
)

# Carpeta de resultados
carpeta_resultados = os.path.join(
    carpeta_codigo,
    "..",
    "resultados"
)

# Crear carpeta resultados si no existe
os.makedirs(carpeta_resultados, exist_ok=True)

# Cargar la imagen
imagen = cv2.imread(ruta_imagen)

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    print("Ruta buscada:")
    print(ruta_imagen)
    input("Presiona ENTER para cerrar...")
    exit()

# Aplicar filtro Gaussiano
imagen_suavizada = cv2.GaussianBlur(
    imagen,
    (7, 7),
    0
)

# Mostrar imágenes
cv2.imshow(
    "Imagen original 0091",
    imagen
)

cv2.imshow(
    "Imagen suavizada 0091 - Filtro Gaussiano",
    imagen_suavizada
)

# Guardar resultado
ruta_guardado = os.path.join(
    carpeta_resultados,
    "camello_gaussiano_0091.jpg"
)

cv2.imwrite(
    ruta_guardado,
    imagen_suavizada
)

print("Filtro Gaussiano aplicado correctamente.")
print("Resultado guardado en:")
print(ruta_guardado)

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Programa realizado por Ian Gutierrez 0091")