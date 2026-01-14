---
nav_title: Cómo empezar
article_title: Primeros pasos con Braze Pilot
page_order: 2
page_type: reference
description: "Este artículo de referencia cubre brevemente los pasos de integración que deben dar tus ingenieros o desarrolladores."
---

# Primeros pasos con Braze Pilot

> Este artículo explica cómo empezar a utilizar Braze Pilot. Aquí te guiaremos en la descarga de la aplicación, la inicialización de la conexión con tu panel Braze y la finalización de la configuración.

## Paso 1: Descargar Braze Pilot

Para empezar a utilizar Braze Pilot, primero tendrás que descargar la aplicación de Apple App Store o de Google Play Store. Puedes buscar la aplicación en la tienda de aplicaciones o escanear los siguientes códigos QR para visitar la página de la aplicación para tu dispositivo.

## Paso 2: Acepta los términos y condiciones

A continuación, acepta los términos y condiciones, y luego introduce tu correo electrónico de trabajo en el formulario. Tu correo electrónico se utilizará únicamente para el análisis del uso de la aplicación y no para fines de marketing.

Página de bienvenida de Braze Pilot.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"}\![Opción de introducir la dirección de correo electrónico de tu trabajo.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## Paso 3: Inicializa la conexión con el SDK de Braze

Braze Pilot te habilita para inicializar el SDK de Braze contra cualquier panel de Braze. Una vez inicializado el SDK, Pilot empezará a enviar datos de interacción a Braze y te permitirá desencadenar cualquier mensajería lanzada desde ese panel Braze.

Hay dos métodos para configurar la conexión SDK en Piloto: Demo de códigos QR y asistente de configuración.

{% tabs local %}
{% tab Demo QR codes %}

### Método 1: Demo códigos QR

Escanea un código QR que incluye todos los detalles necesarios para inicializar el SDK, crear tu perfil de usuario y vincularte en profundidad a una simulación de aplicación concreta en Braze Pilot. Los códigos QR de demostración se muestran en el cajón de acompañamiento para determinadas campañas de demostración en tu prueba gratuita.

| Piloto para Android | Piloto para iOS |
| --- | --- |
| Código QR para Android.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | Código QR para iOS.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Setup wizard %}

### Método 2: Asistente de configuración

Sigue una guía paso a paso para inicializar la conexión con el espacio de trabajo de tu panel desde la página **Configuración de la aplicación** en tu panel Braze.

Paso 1 del asistente de configuración de Braze Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Esta conexión es específica del espacio de trabajo. Esto significa que si inicializas la conexión desde el espacio de trabajo de demostración y luego cambias al espacio de trabajo en vivo en tu panel de prueba gratuita, tendrás que volver a inicializar el SDK desde ese espacio de trabajo para recibir cualquier campaña lanzada allí.

El desplegable del espacio de trabajo en el panel de Braze con "Demo - Braze" seleccionado como espacio de trabajo activo.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## Paso 4: Permitir permisos push

Por último, se recomienda que permitas que la aplicación te envíe permisos push si quieres probar las capacidades push a través de la aplicación. Puedes dar a la aplicación estos permisos de las siguientes formas: actualizando la configuración de la aplicación en los ajustes de tu dispositivo, o lanzando un primer mensaje push desde Braze a la aplicación.

{% tabs local %}
{% tab Update the settings for the app %}

Abre la configuración de tu dispositivo y localiza Braze Pilot. A continuación, actualiza la configuración para permitir que las notificaciones aparezcan en tu pantalla de bloqueo.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/device_settings.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Launch a push primer message %}

Puedes utilizar un mensaje dentro de la aplicación Braze para solicitar permisos push para la aplicación, igual que harías con tus propios consumidores. Para saber cómo crear este tipo de mensaje en Braze, consulta [Mensajes push primer dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages#push-primer-in-app-messages).

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Paso 5: Experiencia de mensajería Braze en Piloto

¡Ahora estás listo para empezar a recibir campañas y Lienzos desde tu panel Braze como usuario de Braze Pilot! Visita cualquiera de las campañas lanzadas en tu espacio de trabajo de demostración para ver una demostración rápida de los casos de uso de Braze, y luego dirígete a tu espacio de trabajo en vivo para empezar a enviar las tuyas.

Para más información sobre cómo configurar campañas y Lienzos en Braze, consulta [Primeros pasos: Campañas y lonas]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases).