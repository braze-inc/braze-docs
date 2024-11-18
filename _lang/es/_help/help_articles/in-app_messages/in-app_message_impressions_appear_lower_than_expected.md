---
nav_title: Baja impresión de mensajes dentro de la aplicación
article_title: Baja impresión de mensajes dentro de la aplicación
page_order: 2

page_type: solution
description: "Este artículo de ayuda explica las acciones que puedes emprender si las impresiones de tus mensajes dentro de la aplicación son inferiores a lo que te gustaría."
channel: in-app messages
---
# Pocas impresiones de mensajes dentro de la aplicación

Si tus impresiones son más bajas de lo que te gustaría, te recomendamos que compruebes:
* [Tamaño del segmento](#segment-size)
* [Registros de cambios](#segment-changelogs)
* [Ejecutar pruebas](#run-tests)
* [Desencadenantes de eventos](#event-triggers)
* [Impresiones de los mensajes](#message-impressions)

## Tamaño del segmento

Es importante asegurarse de que el tamaño de tu segmento en la campaña refleja la audiencia a la que te diriges. Puede que haya filtros aplicados que estén limitando tu audiencia y haciendo que tu campaña tenga menos impresiones.

## Registros de cambios de segmento

Si el recuento de impresiones es bajo en comparación con lo que era antes, asegúrate de que nadie haya alterado involuntariamente el segmento o la campaña desde el lanzamiento. Nuestros registros de cambios de segmento y de campaña te darán información sobre los cambios que se han hecho, quién los hizo y cuándo ocurrieron.

![Enlace para ver el registro de cambios en la página Detalles de la campaña con siete cambios desde la última vez que el usuario vio la campaña][10]

## Ejecutar pruebas

Una forma rápida de identificar cualquier problema obvio es clonar la campaña, apuntar a tu propio ID de usuario o correo electrónico y lanzar la campaña. Después de desencadenar el mensaje (inicio de sesión, evento personalizado, etc.), comprueba que lo has recibido correctamente. A continuación, ve al panel y actualiza la página para ver si tu impresión se ha registrado correctamente. Si no es así, es probable que el problema esté en tu aplicación.

## Desencadenantes de eventos

Si la campaña se desencadena por el inicio de una sesión o un evento personalizado, debes asegurarte de que este evento o sesión se produce con la frecuencia suficiente para desencadenar el mensaje. Comprueba estos datos en las páginas [Resumen][1] (para datos de sesión) o [Eventos personalizados][2]:

![Página de eventos personalizados que muestra un gráfico del número de veces que se ha producido el evento personalizado Añadido a Favoritos durante un periodo de un mes][11]

## Impresiones de los mensajes

La personalización de la interfaz de usuario de los mensajes dentro de la aplicación o de los mecanismos de entrega dentro del SDK puede requerir que tus desarrolladores utilicen nuestros métodos para registrar manualmente las impresiones de mensajes dentro de la aplicación. Comprueba con tus desarrolladores si utilizas la personalización de mensajes dentro de la aplicación para:
  * [iOS][12] 
  * [Android][13] 

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

_Última actualización el 6 de mayo de 2021_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[10]: {% image_buster /assets/img_archive/trouble4.png %}
[11]: {% image_buster /assets/img_archive/trouble5.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/handling_in_app_display/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/
