import cv2
# ian gutierrez NC 0091

# Cargar la imagen
imagen = cv2.imread("../imagenes/camello 0091.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(imagen, 7)

# Mostrar imágenes
cv2.imshow("Imagen original 0091", imagen)
cv2.imshow("Imagen con filtro de mediana 0091", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "../resultados/camello 0091_mediana.jpg",
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("../resultados/camello 0091_mediana.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows() 

print("programa realizado por ian gutierrez NC = 0091")

