---
nav_title: Ubicaciones y geovallas
article_title: Ubicación y geovallas para iOS
platform: Swift
page_order: 4
description: "En este artículo de referencia se explica cómo implementar ubicaciones y geovallas en tu SDK Swift."
Tool:
  - Location

---

# Ubicaciones y geovallas

> Este artículo trata sobre la configuración de geovallas para tu integración de SDK de iOS. Las geovallas solo están disponibles en determinados paquetes Braze. Ponte en contacto con tu administrador del éxito del cliente de Braze para empezar.

El núcleo de la oferta de ubicación en tiempo real de Braze es el concepto de [geovalla]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences). Una geovalla es un área geográfica virtual, representada como latitud y longitud combinadas con un radio, formando un círculo alrededor de una posición global específica.

{% alert important %}
A partir de iOS 14, las geovallas no funcionan de forma fiable para los usuarios que deciden dar permiso a su ubicación aproximada.
{% endalert %}

## Paso 1: Habilitar el push en segundo plano

Para utilizar plenamente nuestra estrategia de sincronización de geovallas, debes tener habilitadas las [notificaciones push silenciosas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/), además de completar la integración push estándar.

## Paso 2: Habilitar los servicios de ubicación Braze
Los servicios de ubicación Braze [deben habilitarse](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) a través del SDK. No están habilitadas por defecto.

## Paso 3: Habilitar geovallas

Habilita las geovallas estableciendo `location.geofencesEnabled` en `true` en el objeto `configuration` que inicializa la instancia [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/). Puedes encontrar otras opciones de configuración de `location` [aquí](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).
{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.location.brazeLocationProvider = BrazeLocationProvider()
configuration.location.automaticLocationCollection = true
configuration.location.geofencesEnabled = true
configuration.location.automaticGeofenceRequests = true

// Configurations for background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true
configuration.location.distanceFilter = 8000

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];
configuration.logger.level = BRZLoggerLevelInfo;
configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
configuration.location.automaticLocationCollection = YES;
configuration.location.geofencesEnabled = YES;
configuration.location.automaticGeofenceRequests = YES;

// Configurations for background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

### Configurar geovallas para informes en segundo plano

De manera predeterminada, las geovallas solo se supervisan si tu aplicación está en primer plano, o si tiene autorización `Always` (que supervisa todos los estados de la aplicación).

Sin embargo, puedes elegir controlar los eventos de geovalla cuando tu aplicación esté en segundo plano o cuando tenga autorización `When In Use` añadiendo la capacidad `Background Mode -> Location updates` a tu proyecto de Xcode y habilitando `allowBackgroundGeofenceUpdates`. Esto permite a Braze ampliar el estado "en uso" de tu aplicación mediante el control continuo de las actualizaciones de ubicación.

`allowBackgroundGeofenceUpdates` sólo funciona cuando tu aplicación está en segundo plano. Cuando se vuelve a abrir, se detienen los procesos en segundo plano existentes, de modo que se puede dar prioridad a los procesos en primer plano.

{% alert important %}
Para evitar el agotamiento de la batería y la limitación de la tasa, asegúrate de configurar `distanceFilter` con un valor que satisfaga las necesidades específicas de tu aplicación. Si configuras `distanceFilter` con un valor más alto, evitarás que tu aplicación solicite la ubicación de tu usuario con demasiada frecuencia.
{% endalert %}

## Paso 4: Comprueba las notificaciones push en segundo plano de Braze

Braze sincroniza las geovallas con los dispositivos mediante notificaciones push en segundo plano. Sigue el artículo [Ignorar el push silencioso]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/) para asegurarte de que tu aplicación no realiza ninguna acción no deseada al recibir notificaciones de sincronización de geovallas Braze.

## Paso 5: Añade cadenas de descripción del uso de la ubicación a tu Info.plist

Añade la clave `NSLocationAlwaysUsageDescription`, `NSLocationAlwaysAndWhenInUseUsageDescription` o `NSLocationWhenInUseUsageDescription` a tu `info.plist` con un valor `String` que tenga una descripción de por qué tu aplicación necesita hacer un seguimiento de la ubicación.

Esta descripción se mostrará cuando el aviso de ubicación del sistema solicite autorización y debe explicar claramente a tus usuarios las ventajas del seguimiento de ubicación.

## Paso 6: Solicitar autorización al usuario

Cuando solicites autorización a un usuario, puedes pedirle [`When In Use`](#when-in-use) o [`Always`](#always) autorización.

### Cuando está en uso

Para solicitar la autorización de `When In Use`, utiliza el método `requestWhenInUseAuthorization()`:

{% tabs %}
{% tab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endtab %}

{% tab OBJETIVO-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endtab %}
{% endtabs %}

### Siempre

De manera predeterminada, `requestAlwaysAuthorization()` solo concede a tu aplicación la autorización `When In Use` y volverá a solicitar al usuario la autorización `Always` cuando haya transcurrido cierto tiempo. Sin embargo, puedes optar por avisar inmediatamente a tu usuario llamando primero a `requestWhenInUseAuthorization()`, y llamando después a `requestAlwaysAuthorization()` tras recibir tu autorización inicial `When In Use`.

{% alert important %}
Sólo puedes pedir autorización inmediata a `Always` una sola vez.
{% endalert %}

{% tabs %}
{% tab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endtab %}

{% tab OBJETIVO-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endtab %}
{% endtabs %}

## Paso 7: Habilitar geovallas en el panel

iOS solo permite almacenar hasta 20 geovallas para una aplicación determinada. Con las geovallas habilitadas, Braze utilizará algunas de estas 20 plazas disponibles. Para evitar interrupciones accidentales o no deseadas de otras funciones relacionadas con la geovalla en tu aplicación, las geovallas de ubicación deben estar habilitadas para aplicaciones individuales en el panel. Para que nuestros servicios de ubicación funcionen correctamente, comprueba que tu aplicación no esté utilizando todos los puntos de geovalla disponibles.

Hay dos formas de habilitar geovallas para una aplicación concreta: desde la página **Ubicaciones** o desde la página **Administrar configuración**.

### Habilitar geovallas desde la página Ubicaciones

Habilita las geovallas en la página **Ubicaciones** del panel.

1. Ve a **Audiencia** > **Ubicaciones**.
{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), puedes encontrar **Ubicaciones** en **Interacción**.
{% endalert %}

{:start="2"}
2\. Por ejemplo, debajo del mapa se muestra el número de aplicaciones de tu espacio de trabajo que actualmente tienen habilitado el geovallado: **0 de 1 aplicaciones con geovallas habilitadas**. Haz clic en este texto.
3\. Selecciona la aplicación para habilitar geovallas. Haz clic en **Listo.**
![Las opciones de geovalla en la página de ubicaciones de Braze.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Habilitar geovallas desde la página Administrar configuración

Habilita las geovallas desde la configuración de tu aplicación.

1. Ve a **Configuración** > **Configuración de la aplicación**.
{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), puedes encontrar geovallas en **Administrar configuración** > **Configuración**.
{% endalert %}

{:start="2"}
2\. Selecciona la aplicación para la que deseas habilitar geovallas.
3\. Selecciona la casilla de verificación **Geovallas habilitadas**. Haz clic en **Guardar.**

![La casilla de geovalla situada en las páginas de configuración de Braze.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Desactivar las solicitudes automáticas de geovallas

Puedes desactivar las solicitudes automáticas de geovallas en tu objeto `configuration` pasado a [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)). Configura `automaticGeofenceRequests` en `false`. Por ejemplo:

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "{BRAZE_API_KEY}",
  endpoint: "{BRAZE_ENDPOINT}"
)
configuration.automaticGeofencesRequest = false
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:{BRAZE_API_KEY}
                                  endpoint:{BRAZE_ENDPOINT}];
configuration.automaticGeofencesRequest = NO;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

Si decides utilizar esta opción, tendrás que solicitar manualmente geovallas para que la característica funcione.

## Solicitar manual de geovallas

Cuando el SDK de Braze solicita geovallas para supervisar desde el backend, informa de la ubicación actual del usuario y recibe geovallas que se determinan como óptimamente relevantes en función de la ubicación comunicada. Hay un límite de velocidad de una actualización de geovalla por sesión.

Para controlar la ubicación que el SDK informa con el fin de recibir los geovallados más relevantes, puedes solicitar manualmente geovallados proporcionando la latitud y longitud de una ubicación. Se recomienda desactivar las solicitudes automáticas de geovallas cuando utilices este método. Para ello, utiliza el siguiente código:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestGeofences(latitude: latitude, longitude: longitude)
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
[AppDelegate.braze requestGeofencesWithLatitude:latitude
                                      longitude:longitude];
```

{% endtab %}
{% endtabs %}

