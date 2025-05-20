---
nav_title: Desinstalar seguimiento
article_title: Uninstall Tracking para iOS
platform: iOS
page_order: 7
description: "Este artículo explica cómo configurar el Uninstall Tracking para tu aplicación iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Uninstall Tracking para iOS

> Este artículo explica cómo configurar el seguimiento de desinstalación para tu aplicación de iOS, y cómo hacer pruebas para que tu aplicación no realice ninguna acción automática no deseada al recibir un push de seguimiento de desinstalación de Braze.

Uninstall Tracking utiliza notificaciones push en segundo plano con una flag de Braze en la carga útil. Para más información, consulta [Uninstall Tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking) en nuestra guía del usuario.

## Paso 1: Habilitación del push en segundo plano

Asegúrate de haber habilitado la opción **Notificaciones remotas** en la sección **Modos en segundo plano** de la pestaña **Capacidades** de tu proyecto de Xcode. Consulta nuestra documentación [sobre notificaciones push silenciosas]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications/) para obtener más detalles.

## Paso 2: Comprobación del push en segundo plano de Braze

Braze utiliza notificaciones push en segundo plano para recopilar análisis de seguimiento de desinstalaciones. Asegúrate de que tu aplicación [no realiza ninguna acción no deseada]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push/) al recibir nuestras notificaciones de seguimiento de desinstalación.

## Paso 3: Prueba desde el panel de control

A continuación, envíate un push de prueba desde el panel. Este push de prueba no actualizará tu perfil de usuario.

1. En la página **Campañas**, crea una campaña de notificación push y selecciona **iOS push** como plataforma.<br><br>
2. En la página **Configuración**, añade la clave `appboy_uninstall_tracking` con el valor correspondiente `true` y marca **Añadir indicador de contenido disponible**.<br><br>
3. Utiliza la página **Vista previa** para enviarte un push de seguimiento de desinstalación de prueba.<br><br>
4. Comprueba que tu aplicación no realiza ninguna acción automática no deseada al recibir el push.

{% alert important %}
Estos pasos de prueba son un proxy para enviar un push de seguimiento de desinstalación desde Braze. Si tienes habilitados los recuentos de placas, se enviará un número de placa junto con el push de prueba, pero los push de seguimiento de desinstalación de Braze no establecerán un número de placa en tu aplicación.
{% endalert %}

## Paso 4: Habilitar el seguimiento de Uninstall Tracking

Sigue las instrucciones para [habilitar Uninstall Tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

