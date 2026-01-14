---
nav_title: "Crear notificaciones enriquecidas"
article_title: "Creación de notificaciones push enriquecidas para Android"
page_order: 3
page_layout: tutorial
description: "Este tutorial explica cómo configurar las notificaciones enriquecidas de Android para tus campañas Braze."
platform: Android
channel:
  - Push
tool:
  - Campaigns
  
---

# Creación de notificaciones push enriquecidas para Android

> Las notificaciones enriquecidas permiten una mayor personalización en tus notificaciones push añadiendo contenido adicional más allá de una simple copia. Desde hace algún tiempo, las notificaciones de Android incluyen imágenes en las notificaciones push, lo que se conoce como "imagen de notificación ampliada".

## Requisitos previos

Antes de crear una notificación push enriquecidas para Android, ten en cuenta los siguientes detalles:

- Las notificaciones enriquecidas de Android no están disponibles al crear una campaña push rápida.
- Las imágenes de notificación extendida de Android deben tener una proporción de 2:1, pero no tienen límite de tamaño.
- Android también permite configurar una imagen independiente para la vista de notificación estándar. Éstas son las imágenes de tamaño recomendado: 
  - **Pequeña:** 512x256
  - **Medio:** 1024x512 
  - **Grande:** 2048x1024
- Actualmente, las notificaciones enriquecidas de Android sólo permiten imágenes estáticas, incluidos los formatos de imagen JPEG y PNG. GIF y otros formatos de imagen aún no son compatibles.
- Añadir botones de acción a tu notificación push puede afectar al área de la imagen que se puede visualizar. Prueba con la vista previa del panel y con dispositivos en vivo para confirmar que los resultados son los esperados.
- El SDK para Android de Braze debe estar habilitado para que la imagen se renderice.

{% alert note %}
Aunque Braze proporciona instrucciones sobre cómo configurar las notificaciones push enriquecidas, la representación real de las notificaciones push enriquecidas puede variar en función de factores externos como la relación de aspecto del dispositivo, la versión de Android, las restricciones específicas de los OEM y otros. Te recomendamos que hagas una prueba de envío a varios dispositivos Android para asegurarte de que tus notificaciones push enriquecidas aparecen como pretendes.
{% endalert %}

## Configuración de las notificaciones enriquecidas de Android

### Paso 1: Crear una campaña push

Sigue los pasos para [crear una campaña]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) para redactar una notificación push para Android. Utilizarás el mismo compositor para configurar las notificaciones push que no contengan contenido enriquecido.

### Paso 2: Añadir subtítulos

Añade el **texto resumen/título de la** imagen que quieras mostrar antes de la imagen en la notificación.

La sección Ampliada de la imagen de notificación, donde puedes añadir una imagen o introducir una URL de imagen.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### Paso 3: Añadir medios

Añade tu imagen en el campo **Imagen de notificación ampliada** en el compositor del mensaje. Las imágenes pueden cargarse directamente a través del panel o especificando una URL de contenido alojada en otro lugar.

Para más detalles sobre las imágenes compatibles, consulta [Especificaciones de imagen]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push).

Un usuario recibe una notificación push para iOS con el título "Hola" y el texto "Gracias por unirte a nuestro programa de fidelización".]({% image_buster /assets/img_archive/android_rich_image.png %})

### Paso 4: Sigue creando tu campaña

Una vez cargado el contenido de tu notificación enriquecida en el panel, puedes seguir [programando tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

