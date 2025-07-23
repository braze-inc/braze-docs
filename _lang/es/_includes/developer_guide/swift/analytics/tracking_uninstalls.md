## Configuración de Uninstall Tracking

### Paso 1: Habilitar el push en segundo plano

En tu proyecto de Xcode, ve a **Capacidades** y asegúrate de que tienes habilitados **los Modos de Fondo**. Para más información, consulta [Notificación push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Paso 2: Ignorar notificaciones push internas

El SDK de Swift Braze utiliza notificaciones push en segundo plano para recopilar análisis de seguimiento de desinstalaciones. Para asegurarte de que tu aplicación no realiza acciones no deseadas cuando se envían, tendrás que asegurarte de que [se ignoran las notificaciones push internas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications).

### Paso 3: Envía un push de prueba (opcional)

A continuación, envíate una notificación push de prueba desde el panel de Braze (no te preocupes, no actualizará tu perfil de usuario).

1. Ve a **Mensajería** > **Campañas** y crea una campaña de notificación push utilizando la plataforma correspondiente.
2. Ve a **Configuración** > **Configuración de la aplicación** y añade la clave `appboy_uninstall_tracking` con el valor `true` correspondiente, luego marca **Añadir indicador de contenido disponible**.
3. Utiliza la página **Vista previa** para enviarte un push de seguimiento de desinstalación de prueba.
4. Comprueba que tu aplicación no realiza ninguna acción automática no deseada cuando recibe una notificación push.

{% alert note %}
Se enviará un número de señal junto con la notificación push de prueba; sin embargo, una notificación push de seguimiento de desinstalación real no enviará ningún número de señal.
{% endalert %}

### Paso 3: Habilitar el seguimiento de Uninstall Tracking

Por último, habilita el Uninstall Tracking en Braze. Para obtener un tutorial completo, consulta [Habilitar el seguimiento de desinstalación]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

{% alert important %}
El seguimiento de las desinstalaciones puede ser impreciso. Las métricas que ves en Braze pueden sufrir retrasos o ser inexactas.
{% endalert %}
