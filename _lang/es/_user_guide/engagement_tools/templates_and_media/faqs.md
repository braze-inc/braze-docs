---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre la biblioteca multimedia
page_order: 5
page_type: FAQ
tool: Media
description: "Este artículo responde a las preguntas más frecuentes sobre la biblioteca multimedia de Braze."

---

# Preguntas más frecuentes

> Esta página ofrece respuestas a las preguntas más frecuentes sobre la biblioteca multimedia de Braze.

### ¿Existen límites de almacenamiento para las imágenes dentro de la biblioteca multimedia?

No, no hay límites de almacenamiento para los activos de la biblioteca multimedia. Sin embargo, hay límites de tamaño para los activos (máximo 5 MB).

### ¿Existen fechas de caducidad para los activos cargados?

No, los activos cargados en la biblioteca multimedia se conservarán durante toda la vigencia de tu contrato con Braze.

### ¿Puedo cargar activos de video?

No, la biblioteca multimedia no admite archivos de video. Te recomendamos que los alojes externamente o en una plataforma como YouTube.

### ¿Puedo recortar todos los tipos de imagen?

No, la biblioteca multimedia no permite recortar imágenes GIF.

### ¿Cómo recorto una imagen existente?

Puedes recortar una imagen existente seleccionándola en la biblioteca multimedia y haciendo clic en **Recortar y guardar nueva imagen**. 

![Vista previa de la imagen de la biblioteca multimedia.]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

A continuación, se te redirigirá a un compositor de recorte donde podrás seleccionar el tipo de proporción y editar el nombre de la nueva imagen. Cuando selecciones **Guardar**, tu nueva imagen estará lista para usar.

![Ventana para recortar y guardar la imagen de la biblioteca multimedia.]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### Mi imagen se agota por tiempo de espera cuando intento cargarla. ¿Qué puedo hacer al respecto?

Esto puede ocurrir por varias razones, pero una solución común es asegurarte de que tu imagen está optimizada antes de intentar cargarla. Esto significa pasar tu imagen por un optimizador de imágenes como [ImageOptim](https://imageoptim.com/mac).

Además, si tu imagen se creó en Photoshop (o un programa similar) y tiene muchas capas, fusionarlas y reducir el número de capas también puede ayudar.

### Veo un "Error inesperado" al cargar una imagen aunque pesa menos de 5 MB y está en un formato compatible. ¿Qué ocurre?

Esto puede suceder por dos razones principales:

1. **Metadatos no válidos en el archivo:** El software que Braze utiliza para procesar imágenes puede rechazar archivos con metadatos no válidos o incompatibles. En algunos casos, el archivo también puede procesarse de una forma que supere el límite de 5 MB. Prueba a usar una imagen diferente (por ejemplo, vuelve a exportar o guardar la imagen desde tu editor de imágenes) o una imagen de otra fuente.
2. **Caracteres especiales en el nombre del archivo:** Los nombres de archivo que contienen caracteres especiales (como `&` o `%`) pueden provocar que la carga falle. Renombra el archivo para que solo use letras, números, guiones o guiones bajos, y luego intenta cargarlo de nuevo.

### ¿Por qué no puedo cargar las imágenes que quiera en los compositores push?

Esto se debe a que la mayoría de los compositores tienen restricciones sobre la proporción de imagen permitida.