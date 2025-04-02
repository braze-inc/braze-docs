---
nav_title: Entregabilidad para dispositivos Android chinos
article_title: Entregabilidad push para dispositivos Android chinos
page_order: 10

page_type: reference
description: "Este artículo aborda los matices de la entregabilidad push que debe tener en cuenta al dirigirse a usuarios de dispositivos Android fabricados por fabricantes chinos."
channel: push

---

# Entregabilidad push para dispositivos Android chinos

> Algunos dispositivos Android fabricados por fabricantes chinos de equipos originales (OEM), como Xiaomi, OPPO y Vivo, optimizan la duración de la batería mediante una gestión agresiva del ciclo de vida de las aplicaciones. Esta optimización puede tener la consecuencia no deseada de cerrar el procesamiento de aplicaciones en segundo plano, lo que puede reducir la capacidad de entrega de sus notificaciones push.<br><br>Para asegurarse de que el rendimiento de la mensajería de su aplicación funciona como se espera en estos dispositivos, sus equipos de marketing e ingeniería deben colaborar y seguir los pasos descritos en este artículo.

## Pasos para desarrolladores
Estos OEM llevan a cabo sus optimizaciones matando de forma agresiva las aplicaciones en segundo plano y bloqueándolas para que no inicien por sí mismas la ejecución de tareas en segundo plano. Como desarrollador, tendrás que configurar tu aplicación para pedir al usuario que facilite estas restricciones siempre que sea posible.

Esto puede lograrse haciendo que su aplicación se inicie automáticamente en el dispositivo del usuario final, lo que da permiso a su aplicación para ejecutarse en segundo plano y escuchar los mensajes de Braze. Desafortunadamente, como este es un problema específico de cada OEM y no un problema de Android, no hay APIs documentadas para hacer aparecer el aviso de permiso de auto-inicio para cada OEM.

Para solucionarlo, integra una biblioteca como [AutoStarter](https://github.com/judemanutd/AutoStarter) en tu aplicación. AutoStarter es compatible con múltiples fabricantes, lo que le ofrece una forma sencilla de llamar al gestor de permisos de arranque en una amplia gama de dispositivos. Una vez que haya integrado AutoStarter, llame a `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` para que aparezca el gestor de permisos de inicio en el dispositivo de su usuario final. Acompañe esta acción con un aviso que anime al usuario final a activar el "inicio automático" de su aplicación. Su equipo de marketing elaborará este mensaje (véase la sección siguiente).

## Pasos para especialistas en marketing
Después de que sus usuarios opten por recibir notificaciones push, hay pasos adicionales que pueden tomar por su parte para mejorar la entrega de mensajes para estos dispositivos. Te recomendamos que sigas tu [mensaje push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) con un mensaje dentro de la aplicación dirigido a usuarios de dispositivos OEM chinos con estos pasos adicionales:

- Activar el inicio automático de la aplicación
- Desactivar la optimización de la batería de la aplicación

Para amplificar aún más su mensaje, añada otros canales para resurgir la información de las notificaciones push no abiertas a través de canales fuera de la aplicación como SMS, WhatsApp y LINE y canales dentro de la aplicación como mensajes dentro de la aplicación y tarjetas de contenido. Sus usuarios podrán ver cualquier cosa que se hayan perdido la próxima vez que abran la aplicación.