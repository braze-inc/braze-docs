---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre exportación
page_order: 11
page_type: FAQ
description: "Este artículo cubre algunas preguntas frecuentes sobre las exportaciones API y CSV."

---

# Preguntas más frecuentes

> Esta página ofrece respuestas a algunas de las preguntas más frecuentes sobre las exportaciones API y CSV.

### ¿Puedes hacer que ciertas exportaciones aparezcan en tu contenedor de S3 y otras no?

No. Si ha proporcionado credenciales de S3, todas sus exportaciones aparecerán en su bucket de S3; de lo contrario, si no se proporcionan credenciales, todas las exportaciones aparecerán en un bucket de S3 perteneciente a Braze.

### ¿Tengo que añadir credenciales de S3 a Braze para exportar datos?

No. Si no añades credenciales de S3, tus exportaciones aparecerán en un contenedor de S3 perteneciente a Braze.

### ¿Qué ocurre si configuras las credenciales de S3 en el panel pero no seleccionas "Convertir en destino predeterminado de exportación de datos"?

La casilla de verificación **Hacer que éste sea el destino predeterminado de la exportación de datos** influye en si las exportaciones van a S3 o a Azure, suponiendo que hayas añadido credenciales para ambos.

### ¿Por qué he recibido varios archivos al exportar perfiles de usuario a S3?

Este es el comportamiento esperado para espacios de trabajo con muchos usuarios. Braze dividirá su exportación en varios archivos en función del número de usuarios de su espacio de trabajo. Por lo general, sale un archivo por cada 5000 usuarios. Tenga en cuenta que si está exportando un segmento pequeño dentro de un área de trabajo grande, es posible que reciba varios archivos.

### ¿Por qué veo duplicados cuando exporto usuarios por segmentos a través de la API REST?

Se trata de un caso muy poco frecuente causado por la arquitectura subyacente del proveedor de la base de datos. Los duplicados se eliminan cada semana; sin embargo, la mayoría de las semanas no se elimina ningún duplicado.
