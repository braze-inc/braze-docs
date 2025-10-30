---
nav_title: Capacidad de entrega para dispositivos Android chinos
article_title: Capacidad de entrega push para dispositivos Android chinos
page_order: 10

page_type: reference
description: "Este artículo trata de los matices de la capacidad de entrega push que debes tener en cuenta cuando te dirijas a usuarios de dispositivos Android fabricados por fabricantes chinos."
channel: push

---

# Capacidad de entrega push para dispositivos Android chinos

> Algunos dispositivos Android fabricados por fabricantes chinos de equipos originales (OEM), como Xiaomi, OPPO y Vivo, optimizan la duración de la batería mediante una agresiva gestión del ciclo de vida de las aplicaciones. Esta optimización puede tener la consecuencia no deseada de cerrar el procesamiento en segundo plano de la aplicación, lo que puede reducir la capacidad de entrega de tus notificaciones push.<br><br>Para asegurarte de que el rendimiento de la mensajería de tu aplicación funciona como se espera en estos dispositivos, tus equipos de marketing e ingeniería deben colaborar y seguir los pasos que se indican en este artículo.

## Pasos para desarrolladores
Estos OEM llevan a cabo sus optimizaciones matando agresivamente las aplicaciones en segundo plano y bloqueándolas para que no se autoejecuten tareas en segundo plano. Como desarrollador, tendrás que configurar tu aplicación para pedir al usuario que facilite estas restricciones siempre que sea posible.

Esto puede conseguirse haciendo que tu aplicación se inicie automáticamente en el dispositivo de tu usuario final, lo que da permiso a tu aplicación para ejecutarse en segundo plano y escuchar los mensajes de Braze. Desgraciadamente, como se trata de un problema específico de cada OEM y no de Android, no hay API documentadas para que aparezca el aviso de permiso de inicio automático para cada OEM.

Para solucionarlo, integra una biblioteca como [AutoStarter](https://github.com/judemanutd/AutoStarter) en tu aplicación. AutoStarter es compatible con múltiples fabricantes, lo que te proporciona una forma sencilla de llamar al administrador de permisos de inicio en una amplia gama de dispositivos. Después de haber integrado AutoStarter, llama a `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` para que aparezca el administrador de permisos de inicio en el dispositivo de tu usuario final. Combina esta acción con un aviso que anime al usuario final a habilitar el "inicio automático" de tu aplicación. Tu equipo de marketing elaborará este mensaje: ¡consulta la siguiente sección!

## Pasos para especialistas en marketing
Después de que tus usuarios opten por recibir notificaciones push, hay pasos adicionales que pueden dar por su cuenta para mejorar la entrega de mensajes para estos dispositivos. Te recomendamos que sigas tu [mensaje push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) con un mensaje dentro de la aplicación dirigido a usuarios de dispositivos OEM chinos con estos pasos adicionales:

- Habilitar el "inicio automático" de la aplicación
- Desactivar la optimización de la batería para la aplicación

Para amplificar aún más tu mensaje, añade otros canales para hacer resurgir la información de las notificaciones push no abiertas a través de canales fuera de la aplicación, como SMS, WhatsApp y LINE, y canales dentro de la aplicación, como mensajes dentro de la aplicación y tarjetas de contenido. Tus usuarios podrán ver cualquier cosa que se hayan perdido la próxima vez que abran la aplicación.