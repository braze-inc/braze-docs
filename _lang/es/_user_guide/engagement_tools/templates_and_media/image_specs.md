---
nav_title: Especificaciones de imagen
article_title: Especificaciones de imagen
page_order: 4.1

page_type: reference
description: "Este artículo de referencia describe los tamaños de imagen recomendados y las especificaciones para cada tipo de canal."
tool:
  - Templates
  - Media

---

# Especificaciones de imagen

> En general, las imágenes más pequeñas y de alta calidad se cargarán más rápido, por lo que recomendamos utilizar el activo más pequeño posible para conseguir el resultado deseado. Para maximizar el uso de tus imágenes en canales específicos, consulta los detalles de este artículo.

Siempre debe [previsualizar y probar sus mensajes]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) en una variedad de dispositivos para confirmar que las áreas más importantes de su imagen y mensaje aparecen como se espera.

{% alert tip %} ¡Crea activos con confianza! Nuestras plantillas de imágenes de mensajes para aplicaciones y superposiciones de zonas seguras están diseñadas para adaptarse a dispositivos de todos los tamaños. [Descargar plantillas de diseño ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}). {% endalert %}

{% multi_lang_include image_specs.md variable_name='tamaño de la carga' %}

## Mensajes dentro de la aplicación

{% multi_lang_include image_specs.md variable_name='mensajes in-app' %}

### Fuente Awesome

Braze admite el uso de [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) para los iconos de mensajes modales dentro de la aplicación.

## Notificaciones push

{% multi_lang_include image_specs.md variable_name='notificaciones push' %}

## Correo electrónico

{% multi_lang_include image_specs.md variable_name='email' %}

## Comportamiento de la imagen

{% multi_lang_include image_specs.md variable_name='comportamiento de la imagen' %}
