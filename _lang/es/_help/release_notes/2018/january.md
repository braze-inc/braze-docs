---
nav_title: Enero
page_order: 12
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de enero de 2018."
---
# Enero de 2018

## Inserción de CSS

Ahora puedes alternar entre activar y desactivar [la incrustación de CSS][84] para mensajes de correo electrónico individuales yendo a tu **Configuración de correo electrónico**.

## Nuevos filtros de segmento

Ahora puedes crear segmentos utilizando los siguientes filtros:
- Ha recibido el paso de Canvas
- Paso en Canvas abierto/hecho clic
- Último paso específico recibido en Canvas

{% alert update %}
A partir de marzo de 2019, `Received Canvas Step` ha pasado a llamarse `Received Message from Canvas Step`, y `Last Received Specific Canvas Step` ha pasado a llamarse `Last Received Message from Specific Canvas Step`.
{% endalert %}

## Exportar usuarios utilizando el ID del dispositivo

Este punto final acepta ahora un identificador de dispositivo como parámetro, lo que te permite [exportar perfiles de usuario anónimos][82].

Puedes utilizar el ID del dispositivo para exportar todos los perfiles de usuario de ese dispositivo.

## Actualización de los informes de interacción

Ahora hay estadísticas adicionales, como **la tarifa abierta push** y la **tasa de conversión**, disponibles en [los Informes de interacción][81].

## Certificados push de Apple: Utilizar archivos .p8

Ahora puedes utilizar un [archivo p8][80] al subir un certificado push de Apple, lo que garantiza que tus credenciales push de iOS nunca caducarán.


[80]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens
[81]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports
[82]: {{site.baseurl}}/developer_guide/rest_api/export/#users-by-identifier-endpoint
[84]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/#css-inlining
