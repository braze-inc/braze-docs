---
nav_title: "Crear notificaciones enriquecidas"
article_title: "Creación de notificaciones push enriquecidas para Android"
page_order: 3
page_layout: tutorial
description: "Este tutorial explica cómo configurar las notificaciones enriquecidas de Android para sus campañas Braze."
platform: Android
channel:
  - Push
tool:
  - Campaigns
  
---

# Creación de notificaciones push enriquecidas para Android

> Las notificaciones enriquecidas permiten una mayor personalización de las notificaciones push mediante la adición de contenido adicional más allá de la mera copia. Desde hace algún tiempo, las notificaciones de Android incluyen imágenes en las notificaciones push, lo que se conoce como "imagen de notificación ampliada".

## Requisitos previos

Antes de crear una notificación push enriquecidas para Android, ten en cuenta los siguientes detalles:

- Las notificaciones enriquecidas de Android no están disponibles al crear una campaña push rápida.
- Las imágenes de las notificaciones ampliadas de Android deben tener una proporción de 2:1, pero no tienen límite de tamaño.
- Android también permite establecer una imagen independiente para la vista de notificaciones estándar. Estas son las imágenes de tamaño recomendado: 
  - **Pequeño:** 512x256
  - **Medio:** 1024x512 
  - **Grande:** 2048x1024
- Actualmente, las notificaciones enriquecidas de Android solo permiten imágenes estáticas, incluidos los formatos de imagen JPEG y PNG. GIF y otros formatos de imagen aún no son compatibles.
- Añadir botones de acción a su notificación push puede afectar al área de la imagen que se puede visualizar. Prueba con la vista previa del panel y con dispositivos en vivo para confirmar que los resultados son los esperados.

{% alert note %}
Aunque Braze proporciona instrucciones sobre cómo configurar las notificaciones push enriquecidas, la representación real de las notificaciones push enriquecidas puede variar en función de factores externos como la relación de aspecto del dispositivo, la versión de Android, las restricciones específicas de los fabricantes de equipos originales y otros. Te recomendamos que realices una prueba de envío a varios dispositivos Android para asegurarte de que tus notificaciones push enriquecidas aparecen como pretendes.
{% endalert %}

## Configuración de las notificaciones enriquecidas de Android

### Paso 1: Crear una campaña push

Sigue los pasos para [crear una campaña]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) para redactar una notificación push para Android. Utilizarás el mismo compositor para configurar notificaciones push que no contengan contenido enriquecido.

### Paso 2: Añadir subtítulos

Añade el **texto de resumen/título de imagen** que deseas mostrar antes de la imagen en la notificación.

![La sección Ampliada de imágenes de notificación donde puedes añadir una imagen o introducir una URL de imagen.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### Paso 3: Añadir medios

Añade tu imagen en el campo **Imagen de notificación expandida** del redactor del mensaje. Las imágenes pueden cargarse directamente a través del panel de control o especificando una URL de contenido alojada en otro lugar.

Para más detalles sobre las imágenes compatibles, consulta [Especificaciones de imagen]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push).

![Un usuario recibe una notificación push para iOS con "Hola" como título y "¡Gracias por unirte a nuestro programa de fidelización!" como texto.]({% image_buster /assets/img_archive/android_rich_image.png %})

### Paso 4: Sigue creando tu campaña

Una vez cargado el contenido de tu notificación enriquecida en el panel, puedes continuar [programando tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

