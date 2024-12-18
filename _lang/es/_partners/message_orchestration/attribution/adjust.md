---
nav_title: Adjust
article_title: Adjust
alias: /partners/adjust/
description: "Este artículo de referencia describe la asociación entre Braze y Adjust, una empresa de atribución y análisis de móviles que le permite importar datos de atribución de instalaciones no orgánicas para segmentar de forma más inteligente dentro de sus campañas de ciclo de vida."
page_type: partner
search_tag: Partner

---

# Adjust

> [Adjust](https://www.adjust.com/) es una empresa de atribución y análisis de móviles que combina la atribución de fuentes publicitarias con análisis avanzados para obtener una visión completa de la inteligencia empresarial.

La integración de Braze y Adjust le permite importar datos de atribución de instalaciones no orgánicas para segmentar de forma más inteligente dentro de sus campañas de ciclo de vida.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Ajustar la cuenta | Se necesita una cuenta Adjust para beneficiarse de esta asociación. |
| Aplicación para iOS o Android | Esta integración es compatible con aplicaciones iOS y Android. Dependiendo de su plataforma, es posible que se requieran fragmentos de código en su aplicación. Encontrará más detalles sobre estos requisitos en el paso 1 del proceso de integración. |
| Ajustar SDK | Además del SDK de Braze necesario, debes instalar el [SDK de Adjust](https://dev.adjust.com/en/sdk). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Mapear ID de dispositivos

#### Android

Si tienes una aplicación Android, debes pasar un ID de dispositivo Braze único a Adjust. Este ID puede establecerse en el método `addSessionPartnerParameter()` del SDK de ajuste. El siguiente fragmento de código debe incluirse antes de inicializar el SDK en `Adjust.onCreate.`

```
Adjust.addSessionPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getDeviceId()););
```

#### iOS

<!--
{% alert important %}
Prior to February 2023, our Adjust attribution integration used the IDFV as the primary identifier to match iOS attribution data. Braze customers don't need to use Objective-C to fetch the Braze `device_id` and send it to Adjust upon installation as there will be no service disruption. 
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration. 

If set to `true`, you must implement the iOS device ID mapping for Swift to pass the Braze `device_id` to Adjust upon app installation in order for Braze to match iOS attributions appropriately.
--->

{% tabs local %}
{% tab Objetivo-C %}

Si tienes una aplicación iOS, tu IDFV será recogido por Adjust y enviado a Braze. Este ID se asignará a un ID de dispositivo único en Braze.

Braze seguirá almacenando los valores IDFA de los usuarios que hayan optado por esta opción si está recopilando el IDFA con Braze, tal y como se describe en nuestra [Guía de actualización a iOS 14]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/archived_updates/ios_14/). En caso contrario, el IDFV se utilizará como identificador alternativo para asignar usuarios.

{% endtab %}
{% tab Swift %}

Si tienes una aplicación para iOS, puedes optar por recoger IDFV configurando el campo `useUUIDAsDeviceId` en `false`. Si no se establece, es probable que la atribución de iOS no se asigne con precisión de Adjust a Braze. Para más información, consulta [Recoger IDFV]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/).

{% endtab %}
{% endtabs %}

{% alert note %}
Si piensas enviar eventos posteriores a la instalación desde Adjust a Braze, tendrás que hacer lo siguiente: <br><br>1) Asegúrate de que añades `external_id` como parámetro de sesión y evento dentro del SDK de Adjust. Para el reenvío de eventos de ingresos, también tendrá que configurar `product_id` como parámetro para los eventos. Visite [la documentación de Adjust](https://github.com/adjust/sdks) para obtener más información sobre la definición de parámetros de interlocutor para el reenvío de eventos.<br><br>2) Genera una nueva clave de API para introducirla en Adjust. Para ello, seleccione el botón **Generar clave API** que encontrará en la página Ajustar socio del panel de control de Braze.
{% endalert %}

### Paso 2: Obtener la clave de importación de datos Braze

En Braze, vaya a **Integraciones** > **Socios tecnológicos** y seleccione **Ajustar**. 

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), encontrará a **los socios tecnológicos** en **Integraciones**.
{% endalert %}

Aquí encontrarás el punto final REST y generarás tu clave de importación de datos Braze. Una vez generada la clave, puede crear una nueva o invalidar una existente. La clave de importación de datos y el punto final REST se utilizan en el siguiente paso cuando se configura un postback en el panel de Adjust.<br><br>![Esta imagen muestra la casilla "Importación de datos para la atribución de instalación" que se encuentra en la página Ajustar tecnología. En este cuadro, se te muestra la clave de importación de datos y el punto final REST.][1]{: style="max-width:90%;"}

### Paso 3: Configurar Braze en Adjust

1. En el panel de control de Adjust, vaya a **Configuración de la aplicación** y vaya a **Configuración de socios** y, a continuación, **Añadir socios**.
2. Seleccione **Braze (anteriormente Appboy)** y proporcione la clave de importación de datos y el punto final REST de Braze.
3. Haga clic en **Guardar y cerrar**.

### Paso 4: Confirmar la integración

Una vez que Braze reciba los datos de atribución de Adjust, el indicador de estado de la conexión en la página de socios tecnológicos de Adjust en Braze cambiará de "No conectado" a "Conectado". También se incluirá una marca de tiempo de la última solicitud realizada con éxito. 

Ten en cuenta que esto no ocurrirá hasta que recibamos datos sobre una instalación atribuida. Las instalaciones orgánicas, que deben excluirse del postback de ajuste, son ignoradas por nuestra API y no se tienen en cuenta a la hora de determinar si se ha establecido una conexión correcta.

## Campos de datos disponibles

Suponiendo que configure su integración como se sugiere, Braze asignará los datos de Adjust a filtros de segmento como se describe en la siguiente tabla.

| Ajustar campo de datos | Filtro de segmento de soldadura |
| --- | --- |
| `{network_name}` | Fuente atribuida |
| `{campaign_name}` | Campaña atribuida |
| `{adgroup_name}` | Grupo de anuncios atribuidos |
| `{creative_name}` | Anuncio atribuido |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Datos de atribución de Facebook y X (antes Twitter)

Los datos de atribución de las campañas de Facebook y X (antes Twitter) no están disponibles a través de nuestros socios. Estas fuentes de medios no permiten a sus socios compartir datos de atribución con terceros y, por lo tanto, nuestros socios no pueden enviar esos datos a Braze.

## Ajustar las URL de seguimiento de clics en Braze (opcional)

El uso de enlaces de seguimiento de clics en tus campañas Braze te permitirá ver fácilmente qué campañas están impulsando la instalación de aplicaciones y la reactivación de la interacción. Como resultado, podrá medir sus esfuerzos de marketing con mayor eficacia y tomar decisiones basadas en datos sobre dónde invertir más recursos para obtener el máximo rendimiento de la inversión.

Para empezar a utilizar los enlaces de seguimiento de clics de Adjust, visite su [documentación](https://help.adjust.com/tracking/attribution/tracker-urls). Puede insertar directamente los enlaces de seguimiento de clics de Adjust en sus campañas Braze. Adjust utilizará entonces sus [metodologías de atribución probabilística](https://www.adjust.com/blog/attribution-compatible-with-ios14/) para atribuir al usuario que ha hecho clic en el enlace. Le recomendamos que añada un identificador de dispositivo a sus enlaces de seguimiento de ajustes para mejorar la precisión de las atribuciones de sus campañas Braze. Esto atribuirá de forma determinista al usuario que ha hecho clic en el enlace.

{% tabs local %}
{% tab Android %}
Para Android, Braze permite a los clientes la adhesión voluntaria a la [recopilación de ID de publicidad de Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection). El GAID también se recoge de forma nativa a través de la integración de SDK de Adjust. Puedes incluir el GAID en tus enlaces de seguimiento de clics de Adjust utilizando la siguiente lógica de Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto Braze como Adjust recopilan automáticamente el IDFV de forma nativa a través de nuestras integraciones SDK. Puede utilizarse como identificador del dispositivo. Puedes incluir el IDFV en tus enlaces de seguimiento de clics de Adjust utilizando la siguiente lógica Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Esta recomendación es meramente facultativa**<br>
Si actualmente no utilizas ningún identificador de dispositivo -como el IDFV o el GAID- en tus enlaces de seguimiento de clics, o no piensas hacerlo en el futuro, Adjust podrá seguir atribuyendo estos clics mediante su modelado probabilístico.
{% endalert %}

[1]: {% image_buster /assets/img/attribution/adjust.png %}
[2]: {% image_buster /assets/img/attribution/adjust2.png %}
