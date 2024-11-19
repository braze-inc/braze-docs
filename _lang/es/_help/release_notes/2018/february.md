---
nav_title: Febrero
page_order: 11
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de febrero de 2018."
---
# Febrero de 2018

## Recuento de señales push de iOS

Ahora puedes [actualizar el recuento de señales][89] dentro del compositor push desde Braze.
Para cada mensaje push, puedes especificar qué recuento de señales desencadena esa notificación.

## Exportación de usuarios mediante API utilizando direcciones de correo electrónico

Ahora puedes [exportar datos de perfil de usuario a través de la API][88] especificando direcciones de correo electrónico.
Esta exportación incluye todos los perfiles asociados a esa dirección de correo electrónico.

## API de plantillas de correo electrónico

Ahora puedes crear y actualizar [plantillas de correo electrónico a través de la API][87]. Cada plantilla tendrá un **email_template_id** al que se podrá hacer referencia en otras llamadas a la API.

## Permisos de las claves de API REST

Ahora puedes crear [varias claves de API REST][86] y configurar los permisos de acceso para cada una de ellas. Cada clave puede configurarse para conceder acceso a determinados puntos finales.

También puedes especificar una [lista blanca de direcciones IP][85] y subredes a las que se permite hacer solicitudes de API REST para una clave de API REST determinada.

[85]: {{site.baseurl}}/developer_guide/rest_api/basics/#api-ip-whitelisting
[86]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[87]: {{site.baseurl}}/developer_guide/rest_api/email_templates/#email-templates
[88]: {{site.baseurl}}/developer_guide/rest_api/export/#user-export
[89]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#utilizing-badge-count
