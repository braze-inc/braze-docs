---
nav_title: Desinstalar seguimiento
article_title: Uninstall Tracking para iOS
platform: Swift
page_order: 7
description: "Este artículo explica cómo configurar el seguimiento de desinstalación para el SDK de Swift."

---

# Uninstall Tracking

> Aprende a configurar el seguimiento de desinstalación para tu aplicación de iOS, para asegurarte de que tu aplicación no realiza ninguna acción automática no deseada al recibir un push de seguimiento de desinstalación de Braze. Uninstall Tracking utiliza notificaciones push en segundo plano con una flag de Braze en la carga útil. Para obtener información general, consulta [Uninstall Tracking][6].

{% alert important %}
Ten en cuenta que el Uninstall Tracking puede ser impreciso. Las métricas que ves en Braze pueden sufrir retrasos o ser inexactas.
{% endalert %}

## Paso 1: Habilitar el push en segundo plano

En tu proyecto de Xcode, ve a **Capacidades** y asegúrate de que tienes habilitados **los Modos de Fondo**. Para más información, consulta [Notificación push silenciosa]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/).

## Paso 2: Comprueba las notificaciones push en segundo plano de Braze

Braze utiliza notificaciones push en segundo plano para recopilar análisis de seguimiento de desinstalaciones. Asegúrate de que tu aplicación [no realiza ninguna acción no deseada]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/) al recibir nuestras notificaciones de seguimiento de desinstalación.

## Paso 3: Prueba desde el panel de Braze

A continuación, envíate un push de prueba desde el panel de Braze. Ten en cuenta que este push de prueba no actualizará tu perfil de usuario.

1. En la página **Campañas**, crea una campaña de notificación push y selecciona **iOS push** como plataforma.
2. En la página **Configuración**, añade la clave `appboy_uninstall_tracking` con el valor correspondiente `true` y marca **Añadir indicador de contenido disponible**.
3. Utiliza la página **Vista previa** para enviarte un push de seguimiento de desinstalación de prueba.
4. Comprueba que tu aplicación no realiza ninguna acción automática no deseada al recibir el push.

{% alert important %}
Estos pasos de prueba son un proxy para enviar un push de seguimiento de desinstalación desde Braze. Si tienes habilitado el recuento de placas, se enviará un número de placa junto con el push de prueba, pero los push de seguimiento de desinstalación de Braze no establecerán un número de placa en tu aplicación.
{% endalert %}

## Paso 4: Habilitar el seguimiento de Uninstall Tracking

Sigue las instrucciones para [habilitar Uninstall Tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

