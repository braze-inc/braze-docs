---
nav_title: Integración de tarjetas Banner
article_title: Integración de tarjetas Banner
hidden: true
description: "Este artículo de referencia trata de las Tarjetas Banner y de cómo integrar esta característica en el SDK de Braze."
platform:
  - iOS
  - Android
  - Web
  
---

# Integración de tarjetas Banner

Al igual que [las tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about), las tarjetas de banners se incrustan directamente en tu aplicación o sitio web para que puedas atraer a los usuarios con una experiencia natural. Son una solución rápida y sin complicaciones para crear mensajes personalizados para tus usuarios, al tiempo que amplías el alcance de otros canales (como el correo electrónico o las notificaciones push).

{% alert important %}
Las tarjetas de estandarte están actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

Esta característica está disponible a partir de las siguientes [versiones del SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.6.0 %}

## Requisitos previos del panel de control

### Definir las colocaciones {#define-placements}

Antes de lanzar una campaña de tarjeta de banners en tu aplicación, debes configurar una ubicación en el panel de Braze. Las ubicaciones son localizaciones que defines en tu aplicación y que pueden mostrar tarjetas de presentación.

#### Paso 1: Crear una nueva colocación

Ve a **Configuración** > **Colocaciones de tarjetas de presentación** y, a continuación, selecciona **Crear colocación**.

![Sección de Colocaciones de Tarjetas para crear ID de colocación.]({% image_buster /assets/img/banner_cards/create_placement.png %})

#### Paso 2: Rellena los datos

Ponle un nombre a tu colocación y dale un **ID de colocación**. Opcionalmente, puedes añadir una descripción para tu colocación.

Trabaja con tu equipo de marketing para crear este ID. Este es el ID al que harás referencia en el código de tu aplicación, y tu equipo de marketing lo utilizará para asignar una campaña a la ubicación en tu aplicación. 

{% alert important %}
Evita editar tu ID de ubicación después del lanzamiento, ya que esto puede romper la integración con tu aplicación o sitio web.
{% endalert %}

![Los detalles de colocación que designan una Tarjeta Banner se mostrarán en la barra lateral izquierda para las campañas de promoción de ventas de primavera.]({% image_buster /assets/img/banner_cards/placement_details_example.png %})

Para saber cómo lanzar una campaña con una tarjeta Banner, consulta [Crear una tarjeta Banner]({{site.baseurl}}/create_banner_card/).

## Actualiza las ubicaciones en tu aplicación {#requestBannersRefresh}

Las ubicaciones pueden solicitarse en cada sesión y se almacenarán en caché automáticamente cuando caduque la sesión de un usuario o cuando cambies los usuarios identificados utilizando el método `changeUser`.

{% alert tip %}
Actualiza las ubicaciones lo antes posible para evitar retrasos en la descarga o visualización de los banners.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])
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
This feature is not currently supported on React Native.
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
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## Escucha las actualizaciones {#subscribeToBannersUpdates}

{% alert tip %}
Si insertas banners utilizando los métodos del SDK de esta guía, todos los eventos de análisis se gestionarán automáticamente. Si quieres renderizar manualmente el HTML, [háznoslo saber](mailto:banners-feedback@braze.com).
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log(`Banners were updated`);
})

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])
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
This feature is not currently supported on React Native.
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
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## Obtener e insertar una tarjeta Banner por ID de colocación {#insertBanner}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
   
    // get this placement's banner. If it's `null` the user did not qualify for one.
    const globalBanner = braze.getBanner("global_banner");

    // choose where in the DOM you want to insert the banner HTML
    const container = document.getElementById("global-banner-container");

    // Insert the banner which replacees the innerHTML of that container
    braze.insertBanner(globalBanner, container);

    // Special handling if the user is part of a Control Variant
    if (globalBanner.isControl) {
        // hide or collapse the container
        container.style.display = 'none';
    }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])

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
  let bannerUIView = BrazeBannerUI.BannerUIView(placementId: "global_banner", braze: braze)
}

// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(placementId: "global_banner", braze: braze)
}
```
{% endtab %}
{% tab Java %}
Para obtener el Banner en código Java, utiliza

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

Puedes crear tarjetas de presentación en el diseño de tus vistas de Android incluyendo este XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

{% endtab %}
{% tab Kotlin %}
Para obtener el Banner en Kotlin, utiliza
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```

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

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
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
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## Análisis

No tienes que preocuparte de hacer un seguimiento manual de las impresiones porque Braze gestiona automáticamente todo el registro de impresiones cuando utilizas los métodos del SDK para insertar tarjetas Banner.

Si necesitas analizar y representar el HTML en una vista personalizada, [ponte en contacto con nosotros](mailto:banners-feedback@braze.com).

{% details Más información para el seguimiento manual de las impresiones %}

{% alert important %}
Es probable que la personalización de tu integración sea innecesaria, así que considera detenidamente el siguiente paso.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const banner = braze.getBanner("global_banner");
if (banner?.html) {
  // do something with the html
  // then log an impression when the HTML is in view
  braze.logBannerImpressions([banner.id]);
}
```

{% endtab %}
{% tab Swift %}

```swift
// First, get the Banner object:
var globalBanner: Braze.Banner?
brazeClient.braze()?.banners.getBanner(for: "global_banner", { banner in
  globalBanner = banner
})

// Then log the impression on the Banner.
globalBanner?.context?.logImpression()
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(context).logBannerImpression(banner.getPlacementId());
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).logBannerImpression(banner.placementId)
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
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
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

{% enddetails %}

## Buenas prácticas

### Dimensiones y tamaño de la tarjeta Banner

- Braze no envía información sobre las dimensiones.

{% alert note %}
El compositor permite al usuario previsualizar los banners en diferentes dimensiones. Esa información no se guarda ni se envía al SDK.
{% endalert %}

- El HTML ocupará todo el ancho del contenedor en el que se muestre.
- Como práctica recomendada, recomendamos crear un elemento de dimensión fija y probar esas dimensiones en Compositor.
