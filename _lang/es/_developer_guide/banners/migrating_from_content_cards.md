---
nav_title: "Migrar desde Tarjetas de contenido"
article_title: "Migrar de Tarjetas de contenido a banners"
description: "Aprende a realizar la migración de Tarjetas de contenido a banners, incluyendo ejemplos de código para todos los SDK compatibles, limitaciones y ventajas."
page_order: 5
toc_headers: h2
channel:
  - banners
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Migrar de Tarjetas de contenido a banners

> Esta guía te ayuda en la migración de Tarjetas de contenido a banners para casos de uso de mensajería tipo banner. Los banners son ideales para mensajes en línea, persistentes dentro de la aplicación y en la Web que aparecen en ubicaciones específicas de tu aplicación.

## ¿Por qué realizar la migración a banners?

- Si tu equipo de ingeniería está creando o manteniendo Tarjetas de contenido personalizadas, la migración a banners puede reducir esa inversión continua. Los banners permiten a los especialistas en marketing controlar directamente la interfaz de usuario, lo que libera a los desarrolladores para que puedan dedicarse a otras tareas.
- Si vas a lanzar nuevos mensajes en la página de inicio, flujos de incorporación o anuncios persistentes, empieza con banners en lugar de crear Tarjetas de contenido. Podrás beneficiarte de la personalización en tiempo real, sin caducidad a los 30 días, sin límite de tamaño y con priorización nativa desde el primer día.
- Si estás lidiando con el límite de caducidad de 30 días, administrando una lógica de reelegibilidad compleja o frustrado por una personalización obsoleta, los banners resuelven estos problemas de forma nativa.

Los banners ofrecen varias ventajas con respecto a las Tarjetas de contenido para la mensajería tipo banner:

### Producción acelerada

- **Reducción del soporte de ingeniería continuo necesario**: Los especialistas en marketing pueden crear mensajes personalizados utilizando un editor de arrastrar y soltar y HTML personalizado sin necesidad de ayuda de desarrolladores para la personalización.
- **Opciones de personalización flexibles**: Diseña directamente en el editor, utiliza HTML o aprovecha los modelos de datos existentes con propiedades personalizadas.

### Mejor experiencia de usuario

- **Actualizaciones dinámicas de contenido**: Los banners actualizan la lógica de Liquid y la elegibilidad en cada actualización, lo que garantiza que los usuarios siempre vean el contenido más relevante.
- **Compatibilidad con la ubicación nativa**: Los mensajes aparecen en contextos específicos en lugar de en una fuente, lo que proporciona una mayor relevancia contextual.
- **Priorización nativa**: Control sobre el orden de visualización sin lógica personalizada, lo que facilita la administración de la jerarquía de mensajes.

### Persistencia

- **Sin límite de caducidad**: Las campañas con banners no tienen un límite de caducidad de 30 días como las Tarjetas de contenido, lo que permite una verdadera persistencia de los mensajes.

## Cuándo realizar la migración

Considera la migración a banners si utilizas Tarjetas de contenido para:

- Héroes de la página de inicio, promociones en la página de productos, ofertas en el proceso de pago
- Anuncios de navegación persistentes o mensajes en la barra lateral
- Mensajes siempre activos con una duración superior a 30 días
- Mensajes en los que deseas personalización y elegibilidad en tiempo real

## Cuándo conservar las Tarjetas de contenido

Sigue utilizando las Tarjetas de contenido si necesitas:

- **Experiencias con la fuente:** Cualquier caso de uso que implique múltiples mensajes desplazables o un «buzón de entrada» basado en tarjetas.
- **Características específicas:** Mensajes que requieren contenido conectado o códigos promocionales, ya que los banners no los admiten de forma nativa.
- **Entrega desencadenada:** Casos de uso que requieren estrictamente una entrega desencadenada por API o basada en acciones. Aunque los banners no admiten la entrega desencadenada por API o basada en acciones, la evaluación de elegibilidad en tiempo real significa que los usuarios se clasifican o descartan instantáneamente en función de su pertenencia a un segmento cada vez que se actualiza la página.

## Guía de migración

### Requisitos previos

Antes de la migración, asegúrate de que tu SDK de Braze cumple los requisitos mínimos de versión:

{% multi_lang_include sdk_versions.md feature='banners' %}

### Suscribirse a las actualizaciones

#### Enfoque de las Tarjetas de contenido

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((cards) => {
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToContentCardsUpdates { cards ->
  // Handle array of cards
  cards.forEach { card ->
    Log.d(TAG, "Card: ${card.id}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.contentCards.subscribeToUpdates { cards in
  // Handle array of cards
  for card in cards {
    print("Card: \(card.id)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle array of cards
  for (final card in contentCards) {
    print("Card: ${card.id}");
  }
});
```
{% endtab %}
{% endtabs %}

#### Enfoque de los banners

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  // Get banner for specific placement
  const banner = braze.getBanner("sample_placement_id");
  if (banner) {
    console.log("Banner received for placement:", banner.placementId);
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  // Get banner for specific placement
  val banner = Braze.getInstance(context).getBanner("sample_placement_id")
  if (banner != null) {
    Log.d(TAG, "Banner received for placement: ${banner.placementId}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.subscribeToUpdates { banners in
  // Get banner for specific placement
  braze.banners.getBanner(for: "sample_placement_id") { banner in
    guard let banner = banner else { return }

    print("Banner received for placement: \(banner.placementId)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.BANNER_CARDS_UPDATED, (data) => {
  const banners = data.banners;
  // Get banner for specific placement
  Braze.getBanner("sample_placement_id").then(banner => {
    if (banner) {
      console.log("Banner received for placement:", banner.placementId);
    }
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  // Get banner for specific placement
  braze.getBanner("sample_placement_id").then((banner) {
    if (banner != null) {
      print("Banner received for placement: ${banner.placementId}");
    }
  });
});
```
{% endtab %}
{% endtabs %}

### Mostrar contenido

{% alert note %}
Las Tarjetas de contenido se pueden renderizar manualmente con lógica de interfaz de usuario personalizada, mientras que los banners solo se pueden renderizar con los métodos del SDK listos para usar.
{% endalert %}

#### Enfoque de las Tarjetas de contenido

{% tabs %}
{% tab Web %}
```javascript
// Show default feed UI
braze.showContentCards(document.getElementById("feed"));

// Or manually render cards
const cards = braze.getCachedContentCards();
cards.forEach(card => {
  // Custom rendering logic
  if (card instanceof braze.ClassicCard) {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// Using default fragment
val fragment = ContentCardsFragment()
supportFragmentManager.beginTransaction()
  .replace(R.id.content_cards_container, fragment)
  .commit()

// Or manually render cards
val cards = Braze.getInstance(context).getCachedContentCards()
cards.forEach { card ->
  when (card) {
    is ClassicCard -> {
      // Render classic card
    }
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
// Using default view controller
let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
navigationController?.pushViewController(contentCardsController, animated: true)

// Or manually render cards
let cards = braze.contentCards.cards
for card in cards {
  switch card {
  case let card as Braze.ContentCard.Classic:
    // Render classic card
  default:
    break
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
// Launch default feed
Braze.launchContentCards();

// Or manually render cards
const cards = await Braze.getContentCards();
cards.forEach(card => {
  if (card.type === 'CLASSIC') {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
// Launch default feed
braze.launchContentCards();

// Or manually render cards
final cards = await braze.getContentCards();
for (final card in cards) {
  if (card.type == 'CLASSIC') {
    // Render classic card
  }
}
```
{% endtab %}
{% endtabs %}

#### Enfoque de los banners

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  braze.insertBanner(banner, container);

  if (banner.isControl) {
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Android %}
```kotlin
// Using BannerView in XML
// <com.braze.ui.banners.BannerView
//     android:id="@+id/banner_view"
//     android:layout_width="match_parent"
//     android:layout_height="wrap_content"
//     app:placementId="sample_placement_id" />

// Or programmatically
val bannerView = BannerView(context).apply {
  placementId = "sample_placement_id"
}
container.addView(bannerView)

Braze.getInstance(context).requestBannersRefresh(listOf("sample_placement_id"))
```
{% endtab %}
{% tab Swift %}
```swift
// Using BannerUIView
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
  braze: braze,
  processContentUpdates: { result in
    switch result {
    case .success(let updates):
      if let height = updates.height {
        // Update height constraint
      }
    case .failure:
      break
    }
  }
)
view.addSubview(bannerView)

braze.banners.requestBannersRefresh(placementIds: ["sample_placement_id"])
```
{% endtab %}
{% tab React Native %}
```javascript
// Using BrazeBannerView component
<Braze.BrazeBannerView
  placementID='sample_placement_id'
/>

// Or get banner data
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  // Render custom banner UI
}

Braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Flutter %}
```dart
// Using BrazeBannerView widget
BrazeBannerView(
  placementId: "sample_placement_id",
)

// Or get banner data
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  // Render custom banner UI
}

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% endtabs %}

### Registro de análisis (implementaciones personalizadas)

{% alert note %}
Tanto las Tarjetas de contenido como los banners realizan un seguimiento automático de los análisis cuando se utilizan sus componentes de interfaz de usuario predeterminados. Los ejemplos siguientes son para implementaciones personalizadas en las que creas tu propia interfaz de usuario.
{% endalert %}

#### Enfoque de las Tarjetas de contenido

{% tabs %}
{% tab Web %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
  braze.logContentCardImpressions([card]);
});

// Manual click logging required for custom implementations
card.logClick();
```
{% endtab %}
{% tab Android %}
```kotlin
// Manual impression logging required for custom implementations
cards.forEach { card ->
  card.logImpression()
}

// Manual click logging required for custom implementations
card.logClick()
```
{% endtab %}
{% tab Swift %}
```swift
// Manual impression logging required for custom implementations
for card in cards {
  card.context?.logImpression()
}

// Manual click logging required for custom implementations
card.context?.logClick()
```
{% endtab %}
{% tab React Native %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
  Braze.logContentCardImpression(card.id);
});

// Manual click logging required for custom implementations
Braze.logContentCardClicked(card.id);
```
{% endtab %}
{% tab Flutter %}
```dart
// Manual impression logging required for custom implementations
for (final card in cards) {
  braze.logContentCardImpression(card);
}

// Manual click logging required for custom implementations
braze.logContentCardClicked(card);
```
{% endtab %}
{% endtabs %}

#### Enfoque de los banners

{% tabs %}
{% tab Web %}

{% alert important %}
El seguimiento de los análisis se realiza automáticamente cuando usas `insertBanner()`. No se debe utilizar el registro manual cuando se utiliza `insertBanner()`.
{% endalert %}

```javascript
// Analytics are automatically tracked when using insertBanner()
// Manual logging should not be used when using insertBanner()

// For custom implementations, use manual logging methods:
// Log impression
braze.logBannerImpressions([banner]);

// Log click (with optional buttonId)
braze.logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Android %}

{% alert important %}
Los análisis se rastrean automáticamente cuando usas BannerView. No se debe utilizar el registro manual cuando se utiliza BannerView.
{% endalert %}

```kotlin
// Analytics are automatically tracked when using BannerView
// Manual logging should not be used for default BannerView

// For custom implementations, use manual logging methods:
// Log impression
Braze.getInstance(context).logBannerImpression("sample_placement_id");

// Log click (with optional buttonId)
Braze.getInstance(context).logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Swift %}

{% alert important %}
El seguimiento de los análisis se realiza automáticamente cuando usas BannerUIView. No se debe utilizar el registro manual para el BannerUIView predeterminado.
{% endalert %}

```swift
// Analytics are automatically tracked when using BannerUIView
// Manual logging should not be used for default BannerUIView

// For custom implementations, use manual logging methods:
// Get banner for specific placement
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  // Log impression
  banner.context?.logImpression()

  // Log click (with optional buttonId)
  banner.context?.logClick(buttonId: buttonId)
}

// Control groups are automatically handled by BannerUIView
```
{% endtab %}
{% tab React Native %}

{% alert important %}
El seguimiento de los análisis se realiza automáticamente cuando usas BrazeBannerView. No es necesario registrar manualmente.
{% endalert %}

```javascript
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in React Native
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% tab Flutter %}

{% alert important %}
El seguimiento de los análisis se realiza automáticamente cuando usas BrazeBannerView. No es necesario registrar manualmente.
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### Obtener propiedades

#### Enfoque de las Tarjetas de contenido

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  Log.d(TAG, "Card id: ${card.id} Extras: ${card.extras}")
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  print("Card id: \(card.id) Extras: \(card.extras)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  print("Card id: ${card.id} Extras: ${card.extras}");
}
```
{% endtab %}
{% endtabs %}

#### Enfoque de los banners

{% tabs %}
{% tab Web %}
```javascript
const banner = braze.getBanner("sample_placement_id");
if (!banner) {
  return;
}

console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
```
{% endtab %}
{% tab Android %}
```kotlin
val banner = Braze.getInstance(context).getBanner("sample_placement_id")
if (banner != null) {
  Log.d(TAG, "Banner placement: ${banner.placementId} Properties: ${banner.properties}")
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  print("Banner placement: \(banner.placementId) Properties: \(banner.properties)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
}
```
{% endtab %}
{% tab Flutter %}
```dart
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  print("Banner placement: ${banner.placementId} Properties: ${banner.properties}");
}
```
{% endtab %}
{% endtabs %}

### Manejo de grupos de control

#### Enfoque de las Tarjetas de contenido

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  if card.isControl {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% endtabs %}

#### Enfoque de los banners

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  // Always call insertBanner to track impression (including control)
  braze.insertBanner(banner, container);

  // Hide if control group
  if (banner.isControl) {
    container.style.display = "none";
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// BannerView automatically handles control groups
// No additional code needed
val bannerView = BannerView(context).apply {
  placementId = "sample_placement_id"
}
```
{% endtab %}
{% tab Swift %}
```swift
// BannerUIView automatically handles control groups
// No additional code needed
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
  braze: braze
)
```
{% endtab %}
{% tab React Native %}
```javascript
// BrazeBannerView automatically handles control groups
// No additional code needed
<Braze.BrazeBannerView
  placementID='sample_placement_id'
/>
```
{% endtab %}
{% tab Flutter %}
```dart
// BrazeBannerView automatically handles control groups
// No additional code needed
BrazeBannerView(
  placementId: "sample_placement_id",
)
```
{% endtab %}
{% endtabs %}

## Limitaciones

Al realizar la migración de Tarjetas de contenido a banners, ten en cuenta las siguientes limitaciones:

### Migración de mensajes desencadenados

Los banners solo admiten campañas de entrega planificada. Para realizar la migración de un mensaje que anteriormente se desencadenaba mediante API o se basaba en acciones, conviértelo en una segmentación basada en segmentos:

- **Ejemplo:** En lugar de desencadenar una tarjeta «Completar perfil» con la API, crea un segmento para los usuarios que se hayan registrado en los últimos 7 días pero que no hayan completado su perfil.
- **Elegibilidad en tiempo real:** Los usuarios se clasifican o descalifican para el banner instantáneamente en cada actualización en función de su pertenencia al segmento.

### Diferencias entre características

| Característica | Tarjetas de contenido | Banners |
|---------|--------------|---------|
| **Estructura del contenido** |
| Varias tarjetas en la fuente | ✅ Compatible | ✅ Puedes crear múltiples ubicaciones para lograr una implementación similar a un carrusel. Solo se devuelve un banner por ubicación. |
| Múltiples ubicaciones | N/A | ✅ Compatible con múltiples ubicaciones |
| Tipos de tarjetas (clásicas, con leyenda, solo imagen) | ✅ Múltiples tipos predefinidos | ✅ Banner único basado en HTML (más flexible) |
| **Gestión de contenidos** |
| Editor de arrastrar y soltar | ❌ Requiere desarrollador para personalización | ✅ Los especialistas en marketing pueden crear/actualizar sin necesidad de ingeniería |
| HTML/CSS personalizado | ❌ Limitado a la estructura de la tarjeta | ✅ Compatibilidad total con HTML/CSS |
| Pares clave-valor para personalización | ✅ Necesario para la personalización avanzada | ✅ Pares clave-valor fuertemente tipados denominados «propiedades» para una personalización avanzada |
| **Persistencia y caducidad** |
| Caducidad de la tarjeta | ✅ Compatible (límite de 30 días) | ✅ Compatible (sin límite de caducidad) |
| Verdadera persistencia | ❌ Máximo 30 días | ✅ Persistencia ilimitada |
| **Visualización y segmentación** |
| Interfaz de usuario de fuente | ✅ Fuente predeterminada disponible | ❌ Solo basado en la ubicación |
| Colocación específica según el contexto | ❌ Basado en fuente | ✅ Compatibilidad con la ubicación nativa |
| Priorización nativa | ❌ Requiere lógica personalizada | ✅ Priorización integrada |
| **Interacción del usuario** |
| Descarte manual | ✅ Compatible | ❌ No compatible |
| Tarjetas ancladas | ✅ Compatible | N/A |
| **Análisis** |
| Análisis automático (interfaz de usuario predeterminada) | ✅ Compatible | ✅ Compatible |
| Ordenación por prioridad | ❌ No compatible | ✅ Compatible |
| **Actualizaciones de contenido** |
| Actualización de plantillas Liquid | ❌ Una vez por tarjeta al enviar/lanzar | ✅ Se actualiza cada vez que se refresca |
| Actualización de los requisitos de elegibilidad | ❌ Una vez por tarjeta al enviar/lanzar | ✅ Se actualiza en cada sesión |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Limitaciones del producto

- Hasta 25 mensajes activos por ubicación.
- Hasta 10 ID de ubicación por solicitud de actualización; las solicitudes que superen este límite se truncarán.

### Limitaciones del SDK

- Actualmente, los banners no son compatibles con las plataformas .NET MAUI (Xamarin), Cordova, Unity, Vega o TV.
- Asegúrate de que estás utilizando las versiones mínimas del SDK que se indican en los requisitos previos.

## Artículos relacionados

- [Ubicaciones de banners]({{site.baseurl}}/developer_guide/banners/placements)
- [Tutorial: Mostrar un banner por ID de ubicación]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Análisis de banners]({{site.baseurl}}/developer_guide/banners/analytics)
- [Preguntas frecuentes sobre banners]({{site.baseurl}}/developer_guide/banners/faq)