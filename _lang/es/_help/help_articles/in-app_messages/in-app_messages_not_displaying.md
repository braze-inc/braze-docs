---
nav_title: No se muestran los mensajes dentro de la aplicación
article_title: No se muestran los mensajes dentro de la aplicación
page_order: 1

page_type: solution
description: "Este artículo de ayuda te guía a través de la solución de problemas con mensajes dentro de la aplicación que no se muestran o no se representan correctamente."
channel: in-app messages
---

# No se muestran los mensajes dentro de la aplicación

Si ves que tus mensajes dentro de la aplicación no se muestran o no se reproducen correctamente, puedes comprobarlo de varias formas:

* [Desencadenantes de eventos](#event-triggers)
* [Impresiones de los mensajes](#message-impressions)
* [Pruebas](#run-tests)
* [Tiempo de espera de la sesión](#session-timeout)
* [Intervalo de mensajería](#minimum-interval)

## Desencadenantes de eventos

Si la campaña se desencadena por el inicio de una sesión o un evento personalizado, debes asegurarte de que este evento o sesión se produce con la frecuencia suficiente para desencadenar el mensaje. Comprueba estos datos en las páginas [Resumen][1] (para datos de sesión) o [Eventos personalizados][2]:

![Página de eventos personalizados que muestra un gráfico del número de veces que se ha producido el evento personalizado Añadido a Favoritos durante un periodo de un mes][14]

## Impresiones de los mensajes

La personalización de la interfaz de usuario de los mensajes dentro de la aplicación o de los mecanismos de entrega dentro del SDK puede requerir que tus desarrolladores utilicen nuestros métodos para registrar manualmente las impresiones de mensajes dentro de la aplicación. Consulta con tus desarrolladores si utilizas la personalización de mensajes dentro de la aplicación.

## Ejecutar pruebas

Es importante determinar si el evento desencadenante no se está produciendo, o si el mensaje en sí no se puede mostrar. Para probarlo, desencadena el mensaje utilizando una acción diferente (como el inicio de sesión o un evento personalizado diferente) y comprueba si se muestra. Esto ayudará a aislar si se trata potencialmente de un problema de datos.

También puedes probar a utilizar otro tipo de plantilla de mensaje dentro de la aplicación o un tamaño de imagen diferente. Hay [especificaciones para los mensajes dentro de la aplicación][15] que deben seguirse. A veces, si una imagen es demasiado grande, impedirá que se muestre el mensaje dentro de la aplicación.

## Tiempo de espera de la sesión

Averigua si has personalizado el tiempo de espera de tu sesión. Por defecto, Braze recupera del servidor los mensajes dentro de la aplicación al inicio de la sesión.

Si has ampliado el tiempo de espera de la sesión, se ampliará el periodo de tiempo a partir del cual podemos actualizar los posibles mensajes dentro de la aplicación para los que eres elegible. Además, si tu campaña está configurada para desencadenarse a partir del inicio de una sesión, tendrás que asegurarte de que ha transcurrido el tiempo adecuado para que se registre una nueva sesión. Por ejemplo, el tiempo de espera de la sesión puede haberse personalizado para que sea de 30 segundos. Si abres y cierras la aplicación en menos de 30 segundos, no serás elegible para recibir otro mensaje dentro de la aplicación desencadenado al iniciar la sesión. 

Más información sobre cómo personalizar los tiempos de espera de sesión para las siguientes plataformas:
* [iOS][16]
* [Android][17]
* [Web][18]

## Intervalo mínimo

Hay un intervalo mínimo en el que permitimos que los mensajes dentro de la aplicación se desencadenen consecutivamente, por lo que puede que estés intentando desencadenarlos demasiado rápido. Más información sobre el intervalo mínimo para las siguientes plataformas: 
* [iOS][19]
* [Android][20]
* [Web][21]

Aunque los intervalos son personalizables, los mantenemos para evitar enviar demasiados mensajes a tus usuarios.

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

_Última actualización el 15 de julio de 2021_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[14]: {% image_buster /assets/img_archive/trouble5.png %}
[15]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/
[16]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#customizing-session-timeout
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#customizing-session-timeout
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[20]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[21]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#in-app-message-delivery
