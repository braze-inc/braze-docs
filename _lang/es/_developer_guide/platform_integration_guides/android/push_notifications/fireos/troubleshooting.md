---
nav_title: Solución de problemas
article_title: Solución de problemas push para FireOS
platform: FireOS
page_order: 20
page_type: solution
description: "Este artículo de referencia proporciona escenarios de solución de problemas del FireOS para posibles problemas que puedas experimentar con las notificaciones push."
channel: push

---

# Solución de problemas

> Este artículo proporciona varios escenarios de solución de problemas del FireOS.

## Utilizar los registros de errores push

Braze proporciona errores de notificación push dentro del registro de actividad de mensajes. Este registro de errores proporciona una serie de advertencias que pueden ser muy útiles para identificar por qué tus campañas no funcionan como esperabas. Si haces clic en un mensaje de error, se te redirigirá a la documentación pertinente para ayudarte a solucionar una incidencia concreta.

![]({% image_buster /assets/img_archive/message_activity_log.png %})

## Escenarios de solución de problemas

### No se muestran los usuarios "registrados push" en el panel de Braze (antes de enviar mensajes)

- Asegúrate de que tu aplicación está correctamente configurada para permitir notificaciones push.
- Asegúrate de que el ID de cliente y el Secreto de cliente configurados en tu panel Braze son correctos.

### Las notificaciones push no se muestran en los dispositivos de los usuarios

Hay algunas razones por las que esto podría estar ocurriendo:

- Si fuerzas el cierre de tu aplicación, tus notificaciones push no se mostrarán mientras tu aplicación no se esté ejecutando.
- Asegúrate de que la configuración de [Prioridad de notificación]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/fireos/customization/advanced_settings/#notification-display-priority) está establecida en `HIGH` en tu campaña.
- La clave de API de ADM en tu `api_key.txt` es incorrecta o contiene caracteres no válidos.
- El `BrazeAmazonDeviceMessagingReceiver` no está registrado correctamente en `AndroidManifest.xml` con filtros de intención para `<action android:name="com.amazon.device.messaging.intent.RECEIVE" />` y `<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />`.

### Los usuarios "registrados por push" ya no están habilitados después de enviar mensajes

Esto suele ocurrir cuando los usuarios han desinstalado la aplicación, lo que provoca que su ID de registro en ADM deje de ser válido.

