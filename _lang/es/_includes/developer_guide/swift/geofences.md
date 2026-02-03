{% alert important %}
A partir de iOS 14, las geovallas no funcionan de forma fiable para los usuarios que eligen dar permiso sólo a su ubicación aproximada.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Configuración de geovallas {#setting-up-geofences}

### Paso 1: Habilitación en Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Paso 2: Habilita los servicios de ubicación de tu aplicación

Por defecto, los servicios de ubicación de Braze no están habilitados. Para habilitarlas en tu aplicación, sigue estos pasos. Para ver un tutorial paso a paso, consulta [Tutorial: Ubicaciones y geovallas de Braze](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/).

#### Paso 2.1: Añade el módulo `BrazeLocation` 

En Xcode, abre la pestaña **General**. En **Frameworks, Bibliotecas y Contenido incrustado**, añade el módulo `BrazeLocation`.

![Añade el módulo BrazeLocation en tu proyecto Xcode]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### Paso 2.2: Actualiza tu `Info.plist`

En tu `info.plist`, asigna un valor `String` a una de las siguientes claves que describa por qué tu aplicación necesita hacer un seguimiento de la ubicación. Esta cadena se mostrará cuando se pregunte a tus usuarios por los servicios de ubicación, así que asegúrate de explicar claramente el valor de habilitar esta característica para tu aplicación.

- `NSLocationAlwaysAndWhenInUseUsageDescription` 
- `NSLocationWhenInUseUsageDescription`

![Info.plist cadenas de ubicación en Xcode]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
Apple ha dejado de utilizar `NSLocationAlwaysUsageDescription`. Para más información, consulta [la documentación para desarrolladores de Apple.](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription)
{% endalert %}

### Paso 3: Habilita geovallas en tu código

En el código de tu aplicación, habilita las geovallas estableciendo `location.geofencesEnabled` en `true` en el objeto `configuration` que inicializa la instancia [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) instancia. Para otras opciones de configuración de `location`, consulta [la referencia del SDK Swift de Braze](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).

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

#### Paso 3.1: Habilitar la notificación en segundo plano (opcional)

Por predeterminado, los eventos de geovalla sólo se supervisan si tu aplicación está en primer plano o tiene autorización `Always`, que supervisa todos los estados de la aplicación.

Sin embargo, puedes optar por controlar también los eventos de geovalla si tu aplicación está en segundo plano o tiene [autorización`When In Use` ](#swift_request-authorization). 

Para controlar estos eventos de geovalla adicionales, abre tu proyecto Xcode y ve a **Firmar & Capacidades**. En **Modos en segundo plano**, marca **Actualizaciones de ubicación**.

![En Xcode, Modo en segundo plano > Actualizaciones de ubicación]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

A continuación, habilita `allowBackgroundGeofenceUpdates` en el código de tu aplicación. Esto permite a Braze ampliar el estado "Cuando está en uso" de tu aplicación supervisando continuamente las actualizaciones de ubicación. Esta configuración sólo funciona cuando tu aplicación está en segundo plano. Cuando se vuelve a abrir la aplicación, se detienen todos los procesos en segundo plano existentes y, en su lugar, se da prioridad a los procesos en primer plano.

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
Para evitar el agotamiento de la batería y la limitación de tasas, configura `distanceFilter` con un valor que satisfaga las necesidades específicas de tu aplicación. Si configuras `distanceFilter` con un valor más alto, evitarás que tu aplicación solicite la ubicación de tu usuario con demasiada frecuencia.
{% endalert %}

### Paso 4: Solicitar autorización {#request-authorization}

Cuando solicites autorización a un usuario, pídela a `When In Use` o a `Always`.

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

Sin embargo, puedes optar por avisar inmediatamente a tu usuario llamando primero a `requestWhenInUseAuthorization()` y llamando después a `requestAlwaysAuthorization()` tras recibir tu autorización inicial `When In Use`.

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

### Paso 5: Verificar el push en segundo plano

Braze sincroniza las geovallas con los dispositivos mediante notificaciones push en segundo plano. Sigue estas instrucciones para [configurar las notificaciones push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) para que las actualizaciones de geovallas del servidor se gestionen correctamente.

{% alert note %}
Para asegurarte de que tu aplicación no realiza ninguna acción no deseada al recibir notificaciones de sincronización de geovallas Braze, sigue el artículo [Ignorar el push silencioso]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications).
{% endalert %}

## Solicitar geovallas manualmente {#manually-request-geofences}

Cuando el SDK de Braze solicita geovallas al backend, informa de la ubicación actual del usuario y recibe geovallas que se determinan como óptimamente relevantes en función de la ubicación comunicada.

Para controlar la ubicación que el SDK informa con el fin de recibir los geovallados más relevantes, puedes solicitar manualmente geovallados proporcionando las coordenadas deseadas.

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

### Paso 2: Llama manualmente a `requestGeofences` 

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

#### ¿Por qué no recibo geovallas en mi dispositivo?

Para confirmar si se están recibiendo geovallas en tu dispositivo, utiliza primero la [herramienta Depurador SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk) para comprobar los registros de SDK. Así podrás ver si se están recibiendo correctamente geovallas del servidor y si hay algún error destacable.

A continuación se indican otras posibles razones por las que puede que no se reciban geovallas en tu dispositivo:

##### Limitaciones del sistema operativo iOS

El sistema operativo iOS sólo permite almacenar hasta 20 geovallas para una aplicación determinada. Con las geovallas habilitadas, Braze utilizará algunas de estas 20 plazas disponibles.

Para evitar interrupciones accidentales o no deseadas de otras funciones relacionadas con geovallas en tu aplicación, debes habilitar geovallas de ubicación para aplicaciones individuales en el panel. Para que nuestros servicios de ubicación funcionen correctamente, comprueba que tu aplicación no esté utilizando todos los puntos de geovalla disponibles.

##### Limitación de velocidad

Braze tiene un límite de 1 actualización de geovalla por sesión para evitar peticiones innecesarias.

#### ¿Cómo funciona si estoy utilizando características de geovalla Braze y no Braze?

Como ya se ha mencionado, iOS permite que una sola aplicación almacene un máximo de 20 geovallas. Este almacenamiento lo comparten tanto las geovallas Braze como las que no lo son, y lo administra [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager).

Por ejemplo, si tu aplicación contiene 20 geovallas que no son de Braze, no habría almacenamiento para seguir ninguna geovalla de Braze (o viceversa). Para recibir nuevas geovallas, tendrás que utilizar [las API de ubicación de Apple](https://developer.apple.com/documentation/corelocation) para dejar de controlar algunas de las geovallas existentes en el dispositivo.

#### ¿Puede utilizarse la característica de geovallas mientras un dispositivo está desconectado?

Un dispositivo sólo necesita estar conectado a Internet cuando se produce una actualización. Una vez que ha recibido correctamente geovallas del servidor, es posible registrar una entrada o salida de geovalla aunque el dispositivo esté desconectado. Esto se debe a que la ubicación de un dispositivo funciona independientemente de su conexión a Internet.

Por ejemplo, supongamos que un dispositivo ha recibido y registrado correctamente geovallas al iniciar la sesión y se desconecta. Si entonces entra en una de esas geovallas registradas, puede desencadenar una campaña Braze.

#### ¿Por qué no se supervisan las geovallas cuando mi aplicación está en segundo plano/terminada?

Sin la autorización de `Always`, Apple restringe la ejecución de los servicios de ubicación mientras una aplicación no está en uso. Esto lo impone el sistema operativo y está fuera del control del SDK de Braze. Aunque Braze ofrece configuraciones independientes para ejecutar servicios mientras la aplicación está en segundo plano, no hay forma de eludir estas restricciones para las aplicaciones que se terminan sin recibir autorización explícita del usuario.