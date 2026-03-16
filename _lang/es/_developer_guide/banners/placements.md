---
nav_title: Administrar colocaciones
article_title: Gestiona la ubicación de los banners para el SDK de Braze.
description: "Aprende a crear y administrar ubicaciones de banners en el SDK de Braze, incluido el acceso a sus propiedades únicas y el registro de impresiones."
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Administrar la ubicación de los banners

> Aprende a crear y administrar ubicaciones de banners en el SDK de Braze, incluido el acceso a sus propiedades únicas y el registro de impresiones. Para obtener información más general, consulta [Acerca de los banners]({{site.baseurl}}/developer_guide/banners).

## Acerca de las solicitudes de colocación {#requests}

{% multi_lang_include banners/placement_requests.md %}

## Crear una colocación

### Requisitos previos

Estas son las versiones mínimas del SDK necesarias para crear ubicaciones de banners:

{% multi_lang_include sdk_versions.md feature='banners' %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### Paso 2: Actualiza las ubicaciones en tu aplicación {#requestBannersRefresh}

Las ubicaciones se pueden actualizar llamando a los métodos de actualización que se describen a continuación. Estas ubicaciones se almacenarán automáticamente en caché cuando expire la sesión de un usuario o cuando cambies los identificadores de los usuarios utilizando el`changeUser`método .

{% alert tip %}
Actualiza las ubicaciones lo antes posible para evitar retrasos en la descarga o visualización de los banners.
{% endalert %}

{% tabs %}
{% tab Web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
Braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}

```dart
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Paso 3: Escucha las actualizaciones {#subscribeToBannersUpdates}

{% alert tip %}
Si insertas banners utilizando los métodos SDK de esta guía, todos los eventos de análisis (como impresiones y clics) se gestionarán automáticamente, y las impresiones solo se registrarán cuando el banner esté visible.
{% endalert %}

{% tabs %}
{% tab Web %}
{% subtabs %}
{% subtab JavaScript %}
Si utilizas JavaScript vanilla con el SDK de Braze, utiliza[`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates)  para escuchar las actualizaciones de ubicación y, a continuación, llama[`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh)a  para recuperarlas.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log("Banners were updated");
});

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}
{% subtab React %}
Si utilizas React con el SDK de Braze, configúralo[`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates)dentro de un`useEffect`hook y llama[`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh)a después del registro de tu listener.

```typescript
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    console.log("Banners were updated");
  });

  // always refresh after your subscriber function has been registered
  braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

  // cleanup listeners
  return () => {
    braze.removeSubscription(subscriptionId);
  }
}, []);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Swift %}

```swift
let cancellable = brazeClient.braze()?.banners.subscribeToUpdates { banners in
  banners.forEach { placementId, banner in
    print("Received banner: \(banner) with placement ID: \(placementId)")
  }
}
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  for (banner in update.banners) {
    Log.d(TAG, "Received banner: " + banner.placementId)
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
const bannerCardsSubscription = Braze.addListener(
  Braze.Events.BANNER_CARDS_UPDATED,
  (data) => {
    const banners = data.banners;
    console.log(
      `Received ${banners.length} Banner Cards with placement IDs:`,
      banners.map((banner) => banner.placementId)
    );
  }
);
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}

```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  for (final banner in banners) {
    print("Received banner: " + banner.toString());
  }
});
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Paso 4: Inserta utilizando el ID de ubicación. {#insertBanner}

{% alert tip %}
Para obtener un tutorial completo paso a paso, consulta [Mostrar un banner por ID de ubicación]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners).
{% endalert %}

{% tabs %}
{% tab Web %}

Crea un elemento contenedor para el banner. Asegúrate de establecer su ancho y alto.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

{% subtabs local %}
{% subtab JavaScript %}
Si utilizas JavaScript vanilla con el SDK de Braze, llama al[`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner)método  para sustituir el HTML interno del elemento contenedor.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("sdk-api-key", {
  baseUrl: "sdk-base-url",
  allowUserSuppliedJavascript: true, // banners require you to opt-in to user-supplied javascript
});

braze.subscribeToBannersUpdates((banners) => {
  // get this placement's banner. If it's `null` the user did not qualify for one.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  // choose where in the DOM you want to insert the banner HTML
  const container = document.getElementById("global-banner-container");

  // Insert the banner which replaces the innerHTML of that container
  braze.insertBanner(globalBanner, container);

  // Special handling if the user is part of a Control Variant
  if (globalBanner.isControl) {
    // hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}

{% subtab React %}
Si utilizas React con el SDK de Braze, llama al[`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner)método con un`ref`para sustituir el HTML interno del elemento contenedor.

```tsx
import { useRef } from 'react';
import * as braze from "@braze/web-sdk";

export default function App() {
    const bannerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
       const globalBanner = braze.getBanner("global_banner");
       if (!globalBanner || globalBanner.isControl) {
           // hide the container
       } else {
           // insert the banner to the container node
           braze.insertBanner(globalBanner, bannerRef.current);
       }
    }, []);
    return <div ref={bannerRef}></div>
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Para realizar el seguimiento de las impresiones, asegúrate de llamar`insertBanner`al  para `isControl`. A continuación, puedes ocultar o contraer el contenedor.
{% endalert %}

{% endtab %}
{% tab Swift %}

```swift
// To get access to the Banner model object:
let globalBanner: Braze.Banner?
AppDelegate.braze?.banners.getBanner(for: "global_banner", { banner in
  self.globalBanner = banner
})

// If you simply want the Banner view, you may initialize a `UIView` with the placement ID:
if let braze = AppDelegate.braze {
  let bannerUIView = BrazeBannerUI.BannerUIView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}

// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height according to your parent controller.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}
Para obtener el Banner en código Java, utiliza

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

Puedes crear banners en el diseño de tus vistas Android incluyendo este XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```
{% endsubtab %}

{% subtab Kotlin %}
Si utilizas Android Views, utiliza este XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

Si utilizas Jetpack Compose, puedes usar esto:

```kotlin
Banner(placementId = "global_banner")
```

Para obtener el Banner en Kotlin, utiliza
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

Si utilizas [la nueva arquitectura de React Native](https://reactnative.dev/architecture/landing-page), debes realizar el registro`BrazeBannerView`como componente Fabric en tu `AppDelegate.mm`.

```swift
#ifdef RCT_NEW_ARCH_ENABLED
/// Register the `BrazeBannerView` for use as a Fabric component.
- (NSDictionary<NSString *,Class<RCTComponentViewProtocol>> *)thirdPartyFabricComponents {
  NSMutableDictionary * dictionary = [super thirdPartyFabricComponents].mutableCopy;
  dictionary[@"BrazeBannerView"] = [BrazeBannerView class];
  return dictionary;
}
#endif
```
Para una integración más sencilla, añade el siguiente fragmento de código JavaScript XML (JSX) a tu jerarquía de vistas, proporcionando únicamente el ID de ubicación.

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```

Para obtener el modelo de datos del banner en React Native, o para comprobar la presencia de esa ubicación en la caché de tu usuario, utiliza:

```javascript
const banner = await Braze.getBanner("global_banner");
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}
Para una integración más sencilla, añade el siguiente widget a tu jerarquía de vistas, proporcionando solo el ID de ubicación.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

Puedes utilizar el`getBanner`método para comprobar si esa ubicación está presente en la caché del usuario.

```dart
braze.getBanner("global_banner").then((banner) {
  if (banner == null) {
    // Handle null cases.
  } else {
    print(banner.toString());
  }
});
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Paso 5: Enviar un banner de prueba (opcional) {#handling-test-cards}

Antes de lanzar una campaña de banners, puedes [enviar un banner de prueba]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) para verificar tu integración. Los banners de prueba se almacenarán en una caché independiente en memoria y no se conservarán tras reiniciar la aplicación. Aunque no se necesita ninguna configuración adicional, tu dispositivo de prueba debe ser capaz de recibir notificaciones push en primer plano para poder mostrar la prueba.

{% alert note %}
Los banners de prueba son como cualquier otro banner, salvo que se eliminan en la siguiente sesión de la aplicación.
{% endalert %}

## Impresiones de registro

Braze registra automáticamente las impresiones de los banners que están a la vista cuando utilizas métodos SDK para insertar un banner, por lo que no es necesario realizar un seguimiento manual de las impresiones.

## Registro de clics

El método utilizado para registrar los clics en los banners depende de cómo se muestre el banner y de la ubicación del controlador de clics.

### Contenido estándar del banner (automático)

Si utilizas métodos SDK predeterminados y listos para usar para insertar banners, y tu banner utiliza componentes de editor estándar (imágenes, botones, texto), los clics se registran automáticamente. El SDK añade detectores de clics a estos elementos, sin necesidad de código adicional.

### Bloques de código personalizados

Si tu banner utiliza el bloque de editor **de código personalizado** en el panel de Braze, debes utilizar`brazeBridge.logClick()`  para registrar los clics desde ese HTML personalizado. Esto se aplica incluso cuando se utilizan métodos SDK para renderizar el banner, ya que el SDK no puede adjuntar automáticamente escuchas a elementos dentro de tu código personalizado.

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Para obtener la referencia completa, consulta [Código personalizado y puente JavaScript para banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/custom_code/#javascript-bridge). `brazeBridge`Proporciona una capa de comunicación entre el HTML interno de Banner y el SDK principal de Braze.

### Implementaciones de interfaz de usuario personalizadas (sin interfaz gráfica)

Si estás creando una interfaz de usuario totalmente personalizada utilizando las [propiedades personalizadas](#custom-properties) del banner en lugar de renderizar el HTML del banner, debes registrar manualmente los clics (y las impresiones) desde el código de tu aplicación. Dado que el SDK no muestra el banner, no tiene forma de realizar un seguimiento automático de las interacciones con tus elementos de interfaz de usuario personalizados.

Utiliza el`logClick()`método en el objeto Banner.

## Dimensiones y tamaños

Esto es lo que debes saber sobre las dimensiones y el tamaño de los banners:

- Aunque el compositor te permite realizar una vista previa de los banners en diferentes dimensiones, esa información no se guarda ni se envía al SDK.
- El HTML ocupará todo el ancho del contenedor en el que se muestre.
- Recomendamos crear un elemento de dimensiones fijas y probar esas dimensiones en Composer.

## Propiedades personalizadas {#custom-properties}

Puedes utilizar propiedades personalizadas de tu campaña de Banner para recuperar datos clave-valor a través del SDK y modificar el comportamiento o la apariencia de tu aplicación. Por ejemplo, tú podrías:

- Envía metadatos para tus análisis o integraciones de terceros.
- Utiliza metadatos como un`timestamp`  o un objeto JSON para desencadear la lógica condicional.
- Controla el comportamiento de un banner basándote en metadatos incluidos como`ratio`  o `format`.

### Requisitos previos

Tendrás que [añadir propiedades personalizadas]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#custom-properties) a tu campaña de Banner. Además, estas son las versiones mínimas del SDK necesarias para acceder a las propiedades personalizadas:

{% sdk_min_versions swift:13.1.0 android:38.0.0 web:6.1.0 reactnative:17.0.0 flutter:15.1.0 %}

### Acceder a las propiedades personalizadas

Para acceder a las propiedades personalizadas de un banner, utiliza uno de los siguientes métodos según el tipo de propiedad definido en el panel. Si la clave no coincide con una propiedad de ese tipo o no existe, el método devuelve `null`.

{% tabs local %}
{% tab Web %}
```javascript
// Returns the Banner instance
const banner = braze.getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner) {

  // Returns the string property
  const stringProperty = banner.getStringProperty("color");

  // Returns the boolean property
  const booleanProperty = banner.getBooleanProperty("expanded");

  // Returns the number property
  const numberProperty = banner.getNumberProperty("height");

  // Returns the timestamp property (as a number)
  const timestampProperty = banner.getTimestampProperty("account_start");

  // Returns the image URL property as a string of the URL
  const imageProperty = banner.getImageProperty("homepage_icon");

  // Returns the JSON object property
  const jsonObjectProperty = banner.getJsonProperty("footer_settings");
}
```
{% endtab %}

{% tab Swift %}
```swift
// Passes the specified banner to the completion handler
AppDelegate.braze?.banners.getBanner(for: "placement_id_homepage_top") { banner in
  // Returns the string property
  let stringProperty: String? = banner.stringProperty(key: "color")

  // Returns the boolean property
  let booleanProperty: Bool? = banner.boolProperty(key: "expanded")

  // Returns the number property as a double
  let numberProperty: Double? = banner.numberProperty(key: "height")

  // Returns the Unix UTC millisecond timestamp property as an integer
  let timestampProperty: Int? = banner.timestampProperty(key: "account_start")

  // Returns the image property as a String of the image URL
  let imageProperty: String? = banner.imageProperty(key: "homepage_icon")

  // Returns the JSON object property as a [String: Any] dictionary
  let jsonObjectProperty: [String: Any]? = banner.jsonObjectProperty(key: "footer_settings")
}
```
{% endtab %}

{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
// Returns the Banner instance
Banner banner = Braze.getInstance(context).getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner != null) {
  // Returns the string property
  String stringProperty = banner.getStringProperty("color");
  
  // Returns the boolean property
  Boolean booleanProperty = banner.getBooleanProperty("expanded");
  
  // Returns the number property
  Number numberProperty = banner.getNumberProperty("height");
  
  // Returns the timestamp property (as a Long)
  Long timestampProperty = banner.getTimestampProperty("account_start");
  
  // Returns the image URL property as a String of the URL
  String imageProperty = banner.getImageProperty("homepage_icon");
  
  // Returns the JSON object property as a JSONObject
  JSONObject jsonObjectProperty = banner.getJSONProperty("footer_settings");
}
```
{% endsubtab %}

{% subtab Kotlin %}
```kotlin
// Returns the Banner instance
val banner: Banner = Braze.getInstance(context).getBanner("placement_id_homepage_top") ?: return

// Returns the string property
val stringProperty: String? = banner.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = banner.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = banner.getNumberProperty("height")

// Returns the timestamp property (as a Long)
val timestampProperty: Long? = banner.getTimestampProperty("account_start")

// Returns the image URL property as a String of the URL
val imageProperty: String? = banner.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = banner.getJSONProperty("footer_settings")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab React Native %}

```javascript
// Get the Banner instance
const banner = await Braze.getBanner('placement_id_homepage_top');
if (!banner) return;

// Get the string property
const stringProperty = banner.getStringProperty('color');

// Get the boolean property
const booleanProperty = banner.getBooleanProperty('expanded');

// Get the number property
const numberProperty = banner.getNumberProperty('height');

// Get the timestamp property (as a number)
const timestampProperty = banner.getTimestampProperty('account_start');

// Get the image URL property as a string
const imageProperty = banner.getImageProperty('homepage_icon');

// Get the JSON object property
const jsonObjectProperty = banner.getJSONProperty('footer_settings');
```

{% endtab %}
{% tab Flutter %}

```dart
// Fetch the banner asynchronously
_braze.getBanner(placementId).then(('placement_id_homepage_top') {
  // Get the string property
  final String? stringProperty = banner?.getStringProperty('color');
  
  // Get the boolean property
  final bool? booleanProperty = banner?.getBooleanProperty('expanded');
  
  // Get the number property
  final num? numberProperty = banner?.getNumberProperty('height');
  
  // Get the timestamp property
  final int? timestampProperty = banner?.getTimestampProperty('account_start');
  
  // Get the image URL property
  final String? imageProperty = banner?.getImageProperty('homepage_icon');
  
  // Get the JSON object propertyßß
  final Map<String, dynamic>? jsonObjectProperty = banner?.getJSONProperty('footer_settings');
  
  // Use these properties as needed in your UI or logic
});
```

{% endtab %}
{% endtabs %}
