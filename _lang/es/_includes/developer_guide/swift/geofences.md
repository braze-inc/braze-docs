{% alert important %}
A partir de iOS 14, las geovallas no funcionan de forma fiable para los usuarios que optan por dar solo permiso para su ubicación aproximada.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Configuración de geovallas {#setting-up-geofences}

### Paso 1: Habilitar en Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Paso 2: Habilita los servicios de ubicación de tu aplicación.

De forma predeterminada, los servicios de ubicación de Braze no están habilitados. Para habilitarlos en tu aplicación, sigue estos pasos. Para obtener un tutorial paso a paso, consulta [Tutorial: Ubicaciones y geovallas de ](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/)Braze.

#### Paso 2.1: Añadir el`BrazeLocation`módulo

En Xcode, abre la pestaña **General**. En **Marcos, bibliotecas y contenido incrustado**, añade el`BrazeLocation`módulo.

![Añade el módulo BrazeLocation en tu proyecto Xcode.]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### Paso 2.2: Actualiza tu `Info.plist`

En tu `info.plist`, asigna un`String`valor a una de las siguientes claves que describa por qué tu aplicación necesita realizar el seguimiento de la ubicación. Esta cadena se mostrará cuando se solicite a tus usuarios que activen los servicios de ubicación, así que asegúrate de explicar claramente la importancia de habilitar esta característica para tu aplicación.

- `NSLocationAlwaysAndWhenInUseUsageDescription` 
- `NSLocationWhenInUseUsageDescription`

![Info.plist cadenas de ubicación en Xcode]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
Apple ha dejado de utilizar `NSLocationAlwaysUsageDescription`. Para obtener más información, consulta [la documentación para desarrolladores de Apple](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription).
{% endalert %}

### Paso 3: Habilita las geovallas en tu código.

En el código de tu aplicación, habilita las geovallas estableciendo`location.geofencesEnabled`  en`true`  en el`configuration`objeto que inicializa la[`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/)instancia . Para otras opciones`location` de configuración, consulta [la referencia de Braze SWIFT SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).

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

// Additional configuration customization...

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];
configuration.logger.level = BRZLoggerLevelInfo;
configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
configuration.location.automaticLocationCollection = YES;
configuration.location.geofencesEnabled = YES;
configuration.location.automaticGeofenceRequests = YES;

// Additional configuration customization...

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

#### Paso 3.1: Habilitar informes en segundo plano (opcional)

De forma predeterminada, los eventos de geovalla solo se supervisan si la aplicación está en primer plano o tiene`Always`  autorización, lo que supervisa todos los estados de la aplicación.

Sin embargo, también puedes optar por supervisar los eventos de geovalla si tu aplicación está en segundo plano o tiene[`When In Use`](#swift_request-authorization) [ autorización](#swift_request-authorization). 

Para supervisar estos eventos de geovalla adicionales, abre tu proyecto Xcode y ve a **Capacidades& de firma**. En **Modos en segundo plano**, marca **Actualizaciones de ubicación**.

![En Xcode, Modo en segundo plano > Actualizaciones de ubicación]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

A continuación, habilita`allowBackgroundGeofenceUpdates`  en el código de tu aplicación. Esto permite a Braze ampliar el estado «En uso» de tu aplicación mediante la supervisión continua de las actualizaciones de ubicación. Esta configuración solo funciona cuando la aplicación está en segundo plano. Cuando la aplicación se vuelve a abrir, todos los procesos en segundo plano existentes se pausan y, en su lugar, se da prioridad a los procesos en primer plano.

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

{% alert important %}
Para evitar el agotamiento de la batería y el límite de velocidad, configura`distanceFilter`  con un valor que se ajuste a las necesidades específicas de tu aplicación. Si configuras `distanceFilter` con un valor más alto, evitarás que tu aplicación solicite la ubicación de tu usuario con demasiada frecuencia.
{% endalert %}

### Paso 4: Solicitar autorización {#request-authorization}

Cuando solicites autorización a un usuario, solicita la autorización`When In Use``Always`  o  .

{% tabs local %}
{% tab When In Use %}
Para solicitar la autorización de `When In Use`, utiliza el método `requestWhenInUseAuthorization()`:

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Always %}
De manera predeterminada, `requestAlwaysAuthorization()` solo concede a tu aplicación la autorización `When In Use` y volverá a solicitar al usuario la autorización `Always` cuando haya transcurrido cierto tiempo.

Sin embargo, puedes optar por solicitar inmediatamente al usuario que primero llame a`requestWhenInUseAuthorization()`  y luego a`requestAlwaysAuthorization()`  después de recibir tu autorización `When In Use`inicial .

{% alert important %}
Sólo puedes pedir autorización inmediata a `Always` una sola vez.
{% endalert %}

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Paso 5: Verificar push en segundo plano

Braze sincroniza las geovallas con los dispositivos mediante notificaciones push en segundo plano. Sigue estas instrucciones para [configurar notificaciones push silenciosas,]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) de modo que las actualizaciones de geovallas del servidor se gestionen correctamente.

{% alert note %}
Para asegurarte de que tu aplicación no realice ninguna acción no deseada al recibir notificaciones de sincronización de geovallas de Braze, sigue las instrucciones del artículo [sobre cómo ignorar las notificaciones push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications).
{% endalert %}

## Solicitar geovallas manualmente {#manually-request-geofences}

Cuando el SDK de Braze solicita geovallas al backend, informa de la ubicación actual del usuario y recibe las geovallas que se consideran más relevantes en función de la ubicación comunicada.

Para controlar la ubicación que el SDK informa con el fin de recibir las geovallas más relevantes, puedes solicitar geovallas manualmente proporcionando las coordenadas deseadas.

### Paso 1: Configura `automaticGeofenceRequests` en `false`

Puedes desactivar las solicitudes automáticas de geovallas en tu objeto `configuration` pasado a [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)). Configura `automaticGeofenceRequests` en `false`.

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
{% tab OBJECTIVE-C %}

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

### Paso 2: Llamar`requestGeofences`  manualmente

En tu código, solicita geovallas con la latitud y longitud adecuadas.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestGeofences(latitude: latitude, longitude: longitude)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze requestGeofencesWithLatitude:latitude
                                      longitude:longitude];
```

{% endtab %}
{% endtabs %}

## Preguntas más frecuentes (FAQ) {#faq}

#### ¿Por qué no recibo geovallas en tu dispositivo?

Para confirmar si se están recibiendo geovallas en tu dispositivo, primero utiliza la [herramienta SDK Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk) para comprobar los registros del SDK. A continuación, podrás ver si las geovallas se reciben correctamente desde el servidor y si hay algún error notable.

A continuación se indican otras posibles razones por las que es posible que no recibas geovallas en tu dispositivo:

##### Limitaciones del sistema operativo iOS

El sistema operativo iOS solo permite almacenar hasta 20 geovallas para una aplicación determinada. Con las geovallas habilitadas, Braze utilizará algunas de estas 20 plazas disponibles.

Para evitar interrupciones accidentales o no deseadas en otras funciones relacionadas con las geovallas de tu aplicación, debes habilitar las geovallas de ubicación para aplicaciones individuales en el panel. Para que nuestros servicios de ubicación funcionen correctamente, comprueba que tu aplicación no esté utilizando todos los puntos de geovalla disponibles.

##### Limitación de velocidad

Braze tiene un límite de una actualización de geovalla por sesión para evitar solicitudes innecesarias.

#### ¿Cómo funciona si utilizas tanto las características de geovalla de Braze como las que no son de Braze?

Como se ha mencionado anteriormente, iOS permite que una sola aplicación almacene un máximo de 20 geovallas. Este almacenamiento es compartido por las geovallas de Braze y las que no son de Braze, y es administrado por [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager).

Por ejemplo, si tu aplicación contiene 20 geovallas que no son de Braze, no habría almacenamiento para realizar el seguimiento de ninguna geovalla de Braze (o viceversa). Para recibir nuevas geovallas, tendrás que utilizar [las API de ubicación de Apple](https://developer.apple.com/documentation/corelocation) para dejar de supervisar algunas de las geovallas existentes en el dispositivo.

#### ¿Se puede utilizar la característica de geovalla cuando un dispositivo está desconectado?

Un dispositivo solo necesita estar conectado a Internet cuando se produce una actualización. Una vez que hayas recibido correctamente las geovallas del servidor, es posible registrar una entrada o salida de la geovalla incluso si el dispositivo está desconectado. Esto se debe a que la ubicación de un dispositivo funciona de forma independiente de su conexión a Internet.

Por ejemplo, supongamos que un dispositivo ha recibido y realizado el registro de las geovallas al inicio de la sesión y se desconecta. Si luego entra en una de esas geovallas registradas, puede desencadenar una campaña de Braze.

#### ¿Por qué no se supervisan las geovallas cuando tu aplicación se ejecuta en segundo plano o se cierra?

Sin`Always`autorización, Apple restringe el funcionamiento de los servicios de ubicación cuando una aplicación no está en uso. Esto lo impone el sistema operativo y queda fuera del control del SDK de Braze. Aunque Braze ofrece configuraciones independientes para ejecutar servicios mientras la aplicación está en segundo plano, no hay forma de eludir estas restricciones para las aplicaciones que se cierran sin recibir la autorización explícita del usuario.