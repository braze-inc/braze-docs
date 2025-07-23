## Manifiesto de Apple sobre la privacidad {#privacy-manifest}

### ¿Qué son los datos de seguimiento?

Apple define los "datos de seguimiento" como los datos recopilados en tu aplicación sobre un usuario final o dispositivo que están vinculados a datos de terceros (como publicidad dirigida), o a un intermediario de datos. Para una definición completa con ejemplos, consulta [Apple: Seguimiento](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

De manera predeterminada, el SDK de Braze no recopila datos de seguimiento. Sin embargo, dependiendo de la configuración de tu SDK de Braze, es posible que tengas que incluir datos específicos de Braze en el manifiesto de privacidad de tu aplicación.

### ¿Qué es un manifiesto de privacidad?

Un manifiesto de privacidad es un archivo de tu proyecto Xcode que describe el motivo por el que tu aplicación y los SDK de terceros recopilan datos, junto con sus métodos de recopilación de datos. Cada uno de tus SDK de terceros que hace un seguimiento de datos requiere su propio manifiesto de privacidad. Cuando [creas el informe de privacidad de tu aplicación](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), estos archivos de manifiesto de privacidad se agregan automáticamente en un único informe.

### Dominios de datos de seguimiento de la API

A partir de iOS 17.2, Apple bloqueará todos los puntos finales de seguimiento declarados en tu aplicación hasta que el usuario final acepte un [aviso de Transparencia de seguimiento de anuncios (ATT)](https://support.apple.com/en-us/HT212025). Braze proporciona puntos finales de seguimiento para dirigir tus datos de seguimiento, a la vez que te permite dirigir datos propios que no son de seguimiento al punto final original. 

## Declarar datos de seguimiento de Braze

{% alert tip %}
Para un recorrido completo, consulta el [tutorial Privacidad de los datos de seguimiento](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Requisitos previos

Para implementar esta característica se necesita la siguiente versión del SDK de Braze:

{% sdk_min_versions swift:9.0.0 %}

### Paso 1: Revisa tus políticas actuales

Revisa las políticas actuales de recopilación de datos de tu SDK de Braze con tu equipo legal para determinar si tu aplicación recopila datos de seguimiento [según la definición de Apple](#what-is-tracking-data). Si no recopilas datos de seguimiento, no necesitas personalizar tu manifiesto de privacidad para el SDK de Braze en este momento. Para más información sobre las políticas de recopilación de datos del SDK de Braze, consulta [Recopilación de datos del SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).

{% alert important %}
Si alguno de tus SDK que no sea de Braze recopila datos de seguimiento, tendrás que revisar esas políticas por separado.
{% endalert %}

### Paso 2: Crea un manifiesto de privacidad

Primero, comprueba si ya tienes un manifiesto de privacidad buscando un archivo `PrivacyInfo.xcprivacy` en tu proyecto de Xcode. Si ya tienes este archivo, puedes continuar con el paso siguiente. Si no, consulta [Apple: Crea un manifiesto de privacidad](sdk-tracking.iad-01.braze.com).

### Paso 3: Añade tu punto final al manifiesto de privacidad

En tu proyecto de Xcode, abre el archivo `PrivacyInfo.xcprivacy` de tu aplicación, luego haz clic con el botón derecho en la tabla y marca **Claves y valores sin procesar**.

{% alert note %}

{% endalert %}

![Un proyecto de Xcode con el menú contextual abierto y la opción "Claves y valores brutos" resaltada.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

En **Configuración de privacidad de la aplicación**, elige **NSPrivacyTracking** y establece su valor en **SÍ**.

![El archivo 'PrivacyInfo.xcprivacy' abierto con "NSPrivacyTracking" ajustado a "YES".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

En **Configuración de privacidad de la aplicación**, elige **NSPrivacyTrackingDomains**. En la matriz de dominios, añade un nuevo elemento y establece su valor en el punto final que [añadiste previamente a tu `AppDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate) con el prefijo `sdk-tracking`.

![El archivo 'PrivacyInfo.xcprivacy' abierto con un punto final de seguimiento Braze listado en "NSPrivacyTrackingDomains".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### Paso 4: Declara tus datos de seguimiento

A continuación, abre `AppDelegate.swift` y enumera cada [propiedad de seguimiento](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) que quieras declarar creando una lista de seguimiento estática o dinámica. Ten en cuenta que Apple bloqueará estas propiedades hasta que el usuario final acepte su solicitud de ATT, así que enumera sólo las propiedades que tú y tu equipo legal consideréis que pueden ser objeto de seguimiento. Por ejemplo:

{% tabs %}
{% tab ejemplo estático %}
En el siguiente ejemplo, `dateOfBirth`, `customEvent`, y `customAttribute` se declaran como datos de seguimiento dentro de una lista estática. 

```swift
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    // Declare which types of data you wish to collect for user tracking.
    configuration.api.trackingPropertyAllowList = [
      .dateOfBirth,
      .customEvent(["event-1"]),
      .customAttribute(["attribute-1", "attribute-2"])
    ]
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze
    return true
  }
}
```
{% endtab %}

{% tab ejemplo dinámico %}
En el siguiente ejemplo, la lista de seguimiento se actualiza automáticamente después de que el usuario final acepte el aviso de ATT.

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### Paso 5: Evitar bucles de reintento infinitos

Para evitar que el SDK entre en un bucle infinito de reintentos, utiliza el método `set(adTrackingEnabled: enableAdTracking)` para gestionar los permisos ATT. La propiedad `adTrackingEnabled` de tu método debe tratarse de forma similar a la siguiente:

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```

## Desactivar el seguimiento de datos

Para desactivar la actividad de seguimiento de datos en el SDK de Swift, establece la propiedad [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) a `false` en tu instancia de Braze. Cuando `enabled` está configurado como `false`, el SDK de Braze ignora cualquier llamada a la API pública. El SDK también cancela todas las acciones en vuelo, como solicitudes de red, procesamiento de eventos, etc. 

## Borrar datos almacenados previamente

Puedes utilizar el método [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) para borrar completamente los datos SDK almacenados localmente en el dispositivo de un usuario.

Para las versiones 7.0.0 y posteriores de Braze Swift, el SDK y el método `wipeData()` generan aleatoriamente un UUID para su ID de dispositivo. Sin embargo, si tu `useUUIDAsDeviceId` está configurado en `false` _o_ utilizas la versión 5.7.0 o anterior del SDK de Swift, también tendrás que realizar una solicitud de puesto a [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) ya que tu Identificador para Vendedores (IDFV) se utilizará automáticamente como ID del dispositivo de ese usuario.

## Reanudar el seguimiento de los datos

Para reanudar la recopilación de datos, configura [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) a `true`. Ten en cuenta que esto no restaurará los datos borrados previamente.

## Colección IDFV

En versiones anteriores del SDK de Braze para iOS, el campo IDFV (identificador del proveedor) se recogía automáticamente como ID del dispositivo del usuario. A partir de Swift SDK `v5.7.0`, el campo IDFV se desactivó opcionalmente y, en su lugar, Braze establecía un UUID aleatorio como ID del dispositivo. A partir de Swift SDK `v7.0.0`, el campo IDFV no se recogerá por defecto, y en su lugar se establecerá un UUID como ID del dispositivo.

La característica `useUUIDAsDeviceId` configura el [SDK Swift](https://github.com/braze-inc/braze-swift-sdk) para establecer el ID del dispositivo como UUID. Tradicionalmente, el SDK de iOS asignaba el ID del dispositivo igual al valor IDFV generado por Apple. Con esta característica habilitada por defecto en tu aplicación para iOS, a todos los nuevos usuarios creados a través del SDK se les asignaría un ID de dispositivo igual a un UUID.

Si todavía quieres recoger IDFV por separado, puedes utilizar [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

### Consideraciones

#### Versión del SDK

En el SDK de Swift `v7.0.0+`, cuando `useUUIDAsDeviceId` está habilitado (predeterminado), a todos los nuevos usuarios creados se les asignará un ID de dispositivo aleatorio. Todos los usuarios existentes anteriormente mantendrán su mismo valor de ID de dispositivo, que puede haber sido IDFV.

Si esta característica no está habilitada, se seguirá asignando IDFV a los dispositivos al crearlos.

#### Más adelante en el proceso 

**Socios tecnológicos**: Cuando se habilite esta característica, los socios tecnológicos que obtengan el valor IDFV del ID del dispositivo Braze dejarán de tener acceso a estos datos. Si el valor IDFV derivado del dispositivo es necesario para tu integración del socio, te recomendamos que configures esta característica en `false`.

**Currents**: `useUUIDAsDeviceId` en verdadero significa que el ID del dispositivo enviado en Currents ya no será igual al valor de IDFV.

### Preguntas más frecuentes

#### ¿Este cambio afectará a mis usuarios actuales en Braze?

No. Cuando esté habilitada, esta característica no sobrescribirá ningún dato de usuario en Braze. Sólo se crearán nuevos ID de dispositivo UUID para los dispositivos nuevos o cuando se llame a `wipedata()`.

#### ¿Puedo desactivar esta característica después de encenderla?

Sí, esta característica se puede alternar entre activarla y desactivarla a tu discreción. Los ID de dispositivo almacenados anteriormente nunca se sobrescribirán.

#### ¿Puedo seguir recopilando el valor IDFV a través de Braze en otro lugar?

Sí, aún puedes recopilar opcionalmente el IDFV a través del SDK de Swift (la recopilación está desactivada por defecto). 
