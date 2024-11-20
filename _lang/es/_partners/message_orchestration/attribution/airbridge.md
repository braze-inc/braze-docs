---
nav_title: Airbridge
article_title: Airbridge
alias: /partners/airbridge/
description: "Este artículo de referencia describe la asociación entre Braze y Airbridge, que ofrece atribución basada en las personas y medición incremental para medir la verdadera eficacia del marketing a través de dispositivos, identidades y plataformas."
page_type: partner
search_tag: Partner

---

# Airbridge

> [Airbridge](https://www.airbridge.io/) es una plataforma unificada de medición móvil que le ayuda a descubrir las verdaderas fuentes de crecimiento a través de la atribución móvil, la medición incrementalista y el modelado de marketing mix.

La integración de Braze y Airbridge le permite pasar todos los datos de atribución de instalaciones no orgánicas de Airbridge a Braze para crear campañas de marketing personalizadas.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Airbridge | Se necesita una cuenta Airbridge para beneficiarse de esta asociación. |
| Aplicación para iOS o Android | Esta integración es compatible con aplicaciones iOS y Android. Dependiendo de su plataforma, es posible que se requieran fragmentos de código en su aplicación. |
| SDK de Airbridge | Además del SDK de Braze necesario, debes instalar el SDK de Airbridge [para Android](https://help.airbridge.io/en/developers/android-sdk) o [iOS](https://help.airbridge.io/en/developers/ios-sdk). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Mapear ID de dispositivo

La integración de servidor a servidor puede activarse incluyendo los siguientes fragmentos de código en sus aplicaciones.

#### Android

Si tienes una aplicación Android, tendrás que pasar un ID de dispositivo Braze único a Airbridge.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
// MainApplciation.java
@Override
public void onCreate() {
    super.onCreate();
    // Initialize Airbridge SDK
    AirbridgeConfig config = new AirbridgeConfig.Builder("APP_NAME", "APP_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build();
    Airbridge.init(this, config);
    
    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).getDeviceId());
    // Explicitly start tracking
    Airbridge.startTracking();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// MainApplication.kt
override fun onCreate() {
    super.onCreate()
    // Initialize Airbridge SDK
    val config = AirbridgeConfig.Builder("YOUR_APP_NAME", "YOUR_APP_SDK_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build()
    Airbridge.init(this, config)

    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).deviceId)
    // Explicitly start tracking
    Airbridge.startTracking()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### iOS

Si tiene una aplicación iOS, puede optar por recopilar IDFV estableciendo el campo useUUIDAsDeviceId en false. Si no se establece, es probable que la atribución de iOS no se asigne con precisión de Airbridge a Braze. Para más información, consulta Recopilación de IDFV.

{% tabs %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

```swift
// AppDelegate.swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]?
) {
    AirBridge.setAutoStartTrackingEnabled(false)
    AirBridge.getInstance("YOUR_APP_TOKEN", appName:"YOUR_APP_NAME", withLaunchOptions:launchOptions)

    AirBridge.state()?.addUserAlias(withKey:"braze_device_id", value:Appboy.sharedInstance()?.getDeviceId())
    AirBridge.startTracking()
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// AppDelegate.m
-           (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  AirBridge.autoStartTrackingEnabled = NO;
  [AirBridge getInstance:@"YOUR_APP_TOKEN" appName:@"YOUR_APP_NAME" withLaunchOptions:launchOptions];

    [AirBridge.state addUserAliasWithKey:@"braze_device_id" value:Appboy.sharedInstance.getDeviceId];
    [AirBridge startTracking];
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### React Native

{% tabs %}
{% tab TypeScript %}

```typescript
Braze.getInstallTrackingId(function (error, brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
    Airbirdge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Cordova

{% tabs %}
{% tab TypeScript %}

```typescript
AppboyPlugin.getDeviceId(function (brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Flutter

{% tabs %}
{% tab TypeScript %}

```typescript
BrazePlugin.getInstallTrackingId().then((brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Unity

{% tabs %}
{% tab C# %}

```c#
string BrazeID = AppboyBinding.GetInstallTrackingId();
AirbridgeUnity.SetDeviceAlias("braze_device_id", BrazeID);
AirbridgeUnity.StartTracking()
```

{% endtab %}
{% endtabs %}

### Paso 2: Obtener la clave de importación de datos Braze

En Braze, vaya a **Integraciones de socios** > **Socios tecnológicos** y seleccione **Airbridge**.

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), encontrará a **los socios tecnológicos** en **Integraciones**.
{% endalert %}

Aquí encontrarás el punto final REST y generarás tu clave de importación de datos Braze. Una vez generada la clave, puedes crear una nueva clave o invalidar una existente. La clave de importación de datos y el punto final REST se utilizan en el siguiente paso al configurar un postback en el panel de Airbridge.

![][1]

### Paso 3: Configura Braze en el panel de Airbridge

1. En Airbridge, vaya a **Integraciones > Integraciones de terceros** en la barra lateral izquierda y seleccione **Braze**.
2. Proporcione la clave de importación de datos y el punto final REST que encontró en el panel de Braze.
3. Selecciona el tipo de evento (Instalar evento o Instalar & Deeplink Abrir evento) y guárdalo.

{% alert note %}
Los datos de atribución de las campañas que dieron lugar a eventos de apertura de enlaces profundos se actualizan a nivel de dispositivo. Por ejemplo, si dos usuarios utilizan un mismo dispositivo y uno de ellos realiza un evento de apertura de enlace profundo, los datos de atribución de este evento también se reflejan en los datos del otro usuario.
{% endalert %}

Para obtener instrucciones más detalladas, visite [Airbridge](https://help.airbridge.io/en/guides/braze).

### Paso 4: Confirmar la integración

Una vez que Braze reciba los datos de atribución de Airbridge, el indicador de estado de la conexión en la página de socios tecnológicos de Airbridge en Braze cambiará de "No conectado" a "Conectado". También se incluirá una marca de tiempo de la última solicitud realizada con éxito.

Ten en cuenta que esto no ocurrirá hasta que recibamos datos sobre una instalación atribuida. Las instalaciones orgánicas, que deberían excluirse del postback de Airbridge, son ignoradas por nuestra API y no se tienen en cuenta a la hora de determinar si se ha establecido una conexión satisfactoria.

## Campos de datos disponibles

Airbridge puede enviar cuatro tipos de datos de atribución a Braze que se enumeran en el siguiente cuadro de campos de datos. Estos datos pueden visualizarse en el panel de control de Airbridge y se utilizan para atribuir y filtrar las instalaciones de los usuarios.

Suponiendo que configure su integración como se sugiere, Braze asignará los datos de instalación a los filtros de segmento.

| Campo de datos Airbridge | Filtro de segmento de soldadura | Descripción |
| -------------------- | ---------------------| ---- |
| `Channel` | Origen de atribución de instalación | El canal al que se atribuyen las instalaciones o las aperturas de enlaces profundos |
| `Campaign` | Campaña de atribución de instalación | Campaña a la que se atribuyen las instalaciones o aperturas de enlaces profundos |
| `Ad Group` | Grupo de anuncios de atribución de instalación | Grupo de anuncios al que se atribuyen las instalaciones o las aperturas de enlaces profundos |
| `Ad Creative` | Anuncio de atribución de instalación | La creatividad del anuncio al que se atribuyen las instalaciones o las aperturas de enlaces profundos |

Su base de usuarios puede segmentarse por datos de atribución en el cuadro de mandos de Braze utilizando los filtros Instalar atribución.

![][2]

## Datos de atribución de Meta Business

Los datos de atribución de las campañas de Meta Business no están disponibles a través de nuestros socios. Esta fuente de medios no permite a sus socios compartir datos de atribución con terceros y, por lo tanto, nuestros socios no pueden enviar esos datos a Braze.

## URL de seguimiento de clics de Airbridge en Braze (opcional)

El uso de enlaces de seguimiento de clics en tus campañas Braze te permitirá ver fácilmente qué campañas están impulsando la instalación de aplicaciones y la reactivación de la interacción. Como resultado, podrá medir sus esfuerzos de marketing con mayor eficacia y tomar decisiones basadas en datos sobre dónde invertir más recursos para obtener el máximo rendimiento de la inversión.

Para empezar a utilizar los enlaces de seguimiento de clics de Airbridge, visite [Airbridge](https://help.airbridge.io/en/guides/creating-a-new-tracking-link). Una vez finalizada la configuración, puede insertar directamente los enlaces de seguimiento de clics de Airbridge en sus campañas Braze. A continuación, Airbridge utilizará sus [metodologías de atribución probabilística](https://help.airbridge.io/en/guides/identity-matching) para atribuir al usuario que ha hecho clic en el enlace. Recomendamos añadir un identificador de dispositivo a los enlaces de seguimiento de Airbridge para mejorar la precisión de las atribuciones de sus campañas Braze. Esto atribuirá de forma determinista al usuario que ha hecho clic en el enlace.

{% tabs %}
{% tab Android %}
Para Android, Braze permite a los clientes la adhesión voluntaria a la [recopilación de ID de publicidad de Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). El GAID también se recoge de forma nativa a través de la integración de SDK de Airbridge. Puedes incluir el GAID en tus enlaces de seguimiento de clics de Airbridge utilizando la siguiente lógica de Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto Braze como Airbridge recopilan automáticamente el IDFV de forma nativa a través de nuestras integraciones SDK. Puede utilizarse como identificador del dispositivo. Puede incluir el IDFV en sus enlaces de seguimiento de clics de Airbridge utilizando la siguiente lógica de Liquid:

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
Si actualmente no utiliza ningún identificador de dispositivo -como el IDFV o el GAID- en sus enlaces de seguimiento de clics, o no tiene previsto hacerlo en el futuro, Airbridge podrá seguir atribuyendo estos clics a través de su modelado probabilístico.
{% endalert %}

[1]: {% image_buster /assets/img/airbridge/airbridge_integration_step_1.png %}
[2]: {% image_buster /assets/img/airbridge/airbridge_integration_step_2.png %}
