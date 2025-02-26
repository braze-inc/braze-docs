---
nav_title: Singular
article_title: Singular
alias: /partners/singular/
description: "Este artículo de referencia describe la asociación entre Braze y Singular, una plataforma unificada de análisis de marketing que permite importar datos de atribución de instalaciones de pago."
page_type: partner
search_tag: Partner

---

# Singular

> Singular es una plataforma unificada de análisis de marketing que ofrece atribución, agregación de costes, análisis de marketing, informes creativos y automatización del flujo de trabajo.

La integración de Braze y Singular te permite importar datos de atribución de instalación de pago para segmentar de forma inteligente dentro de tus campañas según el ciclo de vida.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Singular | Es necesario tener una cuenta Singular para beneficiarse de esta asociación. |
| Aplicación para iOS o Android | Esta integración es compatible con aplicaciones iOS y Android. Dependiendo de su plataforma, es posible que se requieran fragmentos de código en su aplicación. Encontrarás más detalles sobre estos requisitos en el paso 1 del proceso de integración. |
| SDK de Singular | Además del SDK de Braze necesario, debes instalar el [SDK de Singular](https://support.singular.net/hc/en-us/articles/360037640172-Getting-Started-with-the-Singular-SDK-S2S). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Asignar ID de usuario

#### Android

Si tienes una aplicación Android, tendrás que incluir el siguiente fragmento de código, que pasa un ID de usuario Braze único a Singular.

```java
String appboyDeviceId = Braze.getInstance(context).getDeviceId();
SingularConfig config = new SingularConfig("SDK KEY", "SDK SECRET")
  .withGlobalProperty(“brazeDeviceID”, appboyDeviceId, true);
```
#### iOS

{% alert important %}
Antes de febrero de 2023, nuestra integración de atribución Singular utilizaba el IDFV como identificador principal para cotejar los datos de atribución de iOS. No es necesario que los clientes de Braze que utilicen Objective-C obtengan el Braze `device_id` y lo envíen a Singular al instalarlo, ya que no habrá interrupción del servicio.
{% endalert%}

Para los que utilicen Swift SDK v5.7.0+, si deseas seguir utilizando IDFV como identificador mutuo, debes asegurarte de que el campo `useUUIDAsDeviceId` está configurado en `false` para que no haya interrupciones en la integración. 

Si se establece en `true`, debes implementar el mapeado de ID de dispositivo iOS para Swift con el fin de pasar el `device_id` de Braze a Singular al instalar la aplicación para que Braze coincida adecuadamente con las atribuciones de iOS.

{% tabs local %}
{% tab Objetivo-C %}

```objc
SingularConfig* config = [[SingularConfig
  alloc] initWithApiKey:SDKKEY andSecret:SDKSECRET];

  [config setGlobalProperty:@"brazeDeviceId" withValue:brazeDeviceId
  overrideExisting:YES];
  [Singular start:config];
```

{% endtab %}
{% tab Swift%}

```swift
config.setGlobalProperty("brazeDeviceId", withValue: brazeDeviceId, overrideExisting: true)
```

{% endtab %}
{% endtabs %}

### Paso 2: Obtener la clave de importación de datos Braze

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Singular**. 

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), encontrará a **los socios tecnológicos** en **Integraciones**.
{% endalert %}

Aquí encontrarás el punto final REST y generarás tu clave de importación de datos Braze. Una vez generada la clave, puedes crear una nueva o invalidar una existente. 

Tendrás que proporcionar la clave de importación de datos y el punto final REST a tu administrador de cuentas de Singular para completar la integración.<br><br>![Esta imagen muestra la casilla "Importación de datos para la atribución de instalación" que se encuentra en la página de tecnología Singular. En este cuadro, se te muestra la clave de importación de datos y el punto final REST.][4]{: style="max-width:90%;"}

### Paso 3: Confirmar la integración

Una vez que Braze reciba los datos de atribución de Singular, el indicador de estado de la conexión en la página de socios tecnológicos de Singular en Braze cambiará de "No conectado" a "Conectado". También se incluirá una marca de tiempo de la última solicitud realizada con éxito. 

Ten en cuenta que esto no ocurrirá hasta que recibamos datos sobre una instalación atribuida. Las instalaciones orgánicas, que deben excluirse del postback de Singular, son ignoradas por nuestra API y no se tienen en cuenta a la hora de determinar si se ha establecido una conexión correcta.

## Datos de atribución de Facebook y X (antes Twitter)

Los datos de atribución de las campañas de Facebook y X (antes Twitter) no están disponibles a través de nuestros socios. Estas fuentes de medios no permiten a sus socios compartir datos de atribución con terceros y, por lo tanto, nuestros socios no pueden enviar esos datos a Braze.

## URL de seguimiento de clics singulares en Braze (opcional)

El uso de enlaces de seguimiento de clics en tus campañas Braze te permitirá ver fácilmente qué campañas están impulsando la instalación de aplicaciones y la reactivación de la interacción. Como resultado, podrás medir tus esfuerzos de marketing con mayor eficacia y tomar decisiones basadas en datos sobre dónde invertir más recursos para obtener el máximo ROI.

Para empezar a utilizar los enlaces de seguimiento de clics de Singular, visita su [documentación](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true). Puedes insertar directamente los enlaces de seguimiento de clics de Singular en tus campañas Braze. Singular utilizará entonces sus [metodologías de atribución probabilística](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true) para atribuir al usuario que ha hecho clic en el enlace. Te recomendamos que añadas a tus enlaces de seguimiento de Singular un identificador de dispositivo para mejorar la precisión de las atribuciones de tus campañas Braze. Esto atribuirá de forma determinista al usuario que ha hecho clic en el enlace.

{% tabs local %}
{% tab Android %}
Para Android, Braze permite a los clientes la adhesión voluntaria a la [recopilación de ID de publicidad de Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). El GAID también se recoge de forma nativa a través de la integración de SDK de Singular. Puedes incluir el GAID en tus enlaces de seguimiento de clics de Branch utilizando la siguiente lógica de Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto Braze como Singular recopilan automáticamente el IDFV de forma nativa a través de nuestras integraciones SDK. Puede utilizarse como identificador del dispositivo. Puedes incluir el IDFV en tus enlaces de seguimiento de clics de Singular utilizando la siguiente lógica Liquid:

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
**Esta recomendación es puramente opcional**<br>
Si actualmente no utilizas ningún identificador de dispositivo -como el IDFV o el GAID- en tus enlaces de seguimiento de clics, o no piensas hacerlo en el futuro, Singular podrá seguir atribuyendo estos clics mediante su modelado probabilístico.
{% endalert %}

[4]: {% image_buster /assets/img/attribution/singular.png %}
