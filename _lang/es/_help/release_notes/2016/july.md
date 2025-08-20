---
nav_title: Julio
page_order: 6
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de julio de 2016."
---

# Julio de 2016

## Filtrar el registro de errores de la consola para desarrolladores por tipo de error

Esta actualización te facilita el uso del Registro de mensajes de error de la consola para desarrolladores para solucionar problemas con sus integraciones Braze. Se trata de una actualización de usabilidad que te permite filtrar el Registro de errores de mensajes por tipo y hace que sea mucho más fácil encontrar e identificar problemas específicos de integración.

## Añadida marca de tiempo para el último push de seguimiento de desinstalación enviado

Braze detecta las desinstalaciones enviando un push silencioso a las aplicaciones de un cliente para ver qué dispositivos responden. Esta característica añade una marca de tiempo discreta que indica cuándo se ejecutó por última vez el seguimiento de la desinstalación. Esta marca de tiempo se encuentra en tu página de Configuración, donde está configurado el seguimiento de desinstalaciones. Más información sobre [Uninstall Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

![Casilla Uninstall Tracking]({% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %})

## Añadidas mejoras en las pruebas de webhooks

Ahora puedes probar el envío de un mensaje de webhook en vivo desde Braze antes de poner en marcha una campaña. El envío de un mensaje de prueba te permitirá verificar que tus mensajes y los puntos finales del servidor se han configurado correctamente en un entorno sandbox seguro. Más información sobre [los webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook).

## Añadida la variación de mensajes recibidos a la exportación CSV de destinatarios de campaña

Hemos añadido una columna que indica la variación del mensaje recibido a la exportación CSV de Destinatarios de campaña. Más información sobre la [exportación de datos]({{site.baseurl}}/user_guide/data/export_braze_data/) desde Braze.

## Límite aproximado del número de impresiones

Una vez que un mensaje dentro de la aplicación haya recibido un determinado número de impresiones, Braze dejará de permitir que los usuarios sean elegibles para recibir el mensaje. Más información sobre la configuración de [límites de impresiones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap) aproximados.

![Gorra de impresión IAM]({% image_buster /assets/img_archive/approx_limit_for_IAM.png %})

