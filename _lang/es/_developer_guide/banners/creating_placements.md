---
nav_title: Crear colocaciones
article_title: Creación de banners para el SDK de Braze
description: "Aprende a crear colocaciones de Banner para el SDK de Braze."
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Creación de banners

> Aprende a crear colocaciones de Banner para el SDK de Braze, para que puedas interactuar con los usuarios con una experiencia que parezca natural. Para más información general, consulta [Acerca de los banners]({{site.baseurl}}/developer_guide/banners).

## Solicitudes de colocación {#requests}

{% multi_lang_include banners/placement_requests.md %}

## Crear una colocación

### Requisitos previos

Estas son las versiones mínimas del SDK necesarias para Banners:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### Paso 2: Actualiza las ubicaciones en tu aplicación {#requestBannersRefresh}

Las ubicaciones pueden solicitarse una vez por sesión y se almacenarán en caché automáticamente cuando caduque la sesión de un usuario o cuando cambies los usuarios identificados utilizando el método `changeUser`. El SDK no recuperará las ubicaciones si vuelves a llamar al método de actualización durante la misma sesión. En su lugar, registrará un error y devolverá un mensaje de error a la persona que llama.

{% alert tip %}
Actualiza las ubicaciones lo antes posible para evitar retrasos en la descarga o visualización de los Banners.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

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
{% tab Java %}

```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

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
Si insertas banners utilizando los métodos del SDK de esta guía, todos los eventos de análisis se gestionarán automáticamente.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log(`Banners were updated`);
});

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

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
{% tab Java %}

```java
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  for (banner in update.banners) {
    Log.d(TAG, "Received banner: " + banner.placementId)
  }
}
```

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

### Paso 4: Insertar utilizando el ID de colocación {#insertBanner}

{% tabs %}
{% tab JavaScript %}

Crea un elemento contenedor para el Banner. Asegúrate de configurar su anchura y altura.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

A continuación, utiliza el método [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) para sustituir el HTML interno del elemento contenedor.

{% alert tip %}
Para hacer un seguimiento de las impresiones, asegúrate de llamar a `insertBanner` para `isControl`. Después puedes ocultar o colapsar tu contenedor.
{% endalert %}

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
{% tab Java %}
Para obtener el Banner en código Java, utiliza

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

Puedes crear Banners en el diseño de tus vistas de Android incluyendo este XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

{% endtab %}
{% tab Kotlin %}
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
{% endtab %}
{% tab React Native %}

Si utilizas [la Nueva Arquitectura de React Native](https://reactnative.dev/architecture/landing-page), tienes que registrar `BrazeBannerView` como componente Fabric en tu sitio `AppDelegate.mm`.

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
Para la integración más sencilla, añade el siguiente fragmento de código JavaScript XML (JSX) a tu jerarquía de vistas, proporcionando sólo el ID de colocación.

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```

Para obtener el modelo de datos del Banner en React Native, o para comprobar la presencia de esa colocación en la caché de tu usuario, utiliza:

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
Para la integración más sencilla, añade el siguiente widget a tu jerarquía de vistas, proporcionando sólo el ID de colocación.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

Puedes utilizar el método `getBanner` para comprobar la presencia de esa ubicación en la caché de tu usuario.

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

### Paso 5: Envía un Banner de prueba (opcional) {#handling-test-cards}

Antes de lanzar una campaña de Banner, puedes [enviar un Banner de prueba]({{site.baseurl}}/user_guide/message_building_by_channel/banners/testing/) para verificar tu integración. Los banners de prueba se almacenarán en una caché en memoria independiente y no persistirán al reiniciar la aplicación. Aunque no es necesaria ninguna configuración adicional, tu dispositivo de prueba debe ser capaz de recibir notificaciones push en primer plano para que pueda mostrar la prueba.

{% alert note %}
Los banners de prueba son como cualquier otro banner, excepto que se eliminan en la siguiente sesión de aplicación.
{% endalert %}

## Registro de impresiones

Braze registra automáticamente las impresiones cuando utilizas los métodos del SDK para insertar un Banner, por lo que no es necesario hacer un seguimiento manual de las impresiones. 

## Dimensiones y tamaño

Esto es lo que debes saber sobre las dimensiones y el tamaño de los estandartes:

- Aunque el compositor te permite previsualizar Banners en diferentes dimensiones, esa información no se guarda ni se envía al SDK.
- El HTML ocupará todo el ancho del contenedor en el que se muestre.
- Te recomendamos que hagas un elemento de dimensión fija y pruebes esas dimensiones en Compositor.
