---
nav_title: "Migrar desde tarjetas de contenido"
article_title: "Migrar de tarjetas de contenido a banners"
description: "Aprende a migrar de tarjetas de contenido a banners, incluidos ejemplos de código para todos los SDK compatibles, limitaciones y ventajas."
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

# Migrar de tarjetas de contenido a banners

> Esta guía te ayuda a migrar de tarjetas de contenido a banners para casos de uso de mensajería tipo banner. Los banners son ideales para mensajes en línea, persistentes dentro de la aplicación y en la Web, que aparecen en lugares específicos de tu aplicación.

## ¿Por qué migrar a Banners?

- Si tu equipo de ingeniería está creando o manteniendo tarjetas de contenido personalizadas, la migración a Banners puede reducir esa inversión continua. Los banners permiten a los especialistas en marketing controlar directamente la interfaz de usuario, liberando a los desarrolladores para otras tareas.
- Si vas a lanzar nuevos mensajes para la página de inicio, flujos de incorporación o anuncios persistentes, empieza con las pancartas en lugar de basarte en tarjetas de contenido. Puedes beneficiarte de personalización en tiempo real, sin caducidad de 30 días, sin límite de tamaño y con priorización nativa desde el primer día.
- Si estás trabajando con el límite de caducidad de 30 días, gestionando una compleja lógica de renovación de la elegibilidad o frustrado por una personalización obsoleta, Banners resuelve estos problemas de forma nativa.

Los banners ofrecen varias ventajas sobre las tarjetas de contenido para los mensajes tipo banner:

### Producción acelerada

- **Menor necesidad de soporte de ingeniería**: Los especialistas en marketing pueden crear mensajes personalizados utilizando un editor de arrastrar y soltar y HTML personalizado sin necesidad de ayuda del desarrollador para la personalización
- **Opciones de personalización flexibles**: Diseña directamente en el editor, utiliza HTML o aprovecha los modelos de datos existentes con propiedades personalizadas

### Mejor UX

- **Actualizaciones dinámicas de contenido**: Los banners se actualizan Lógica líquida y elegibilidad en cada actualización, garantizando que los usuarios vean siempre el contenido más relevante.
- **Soporte de colocación nativo**: Los mensajes aparecen en contextos específicos en lugar de en una fuente, lo que proporciona una mayor relevancia contextual
- **Priorización nativa**: Control del orden de visualización sin lógica personalizada, lo que facilita la gestión de la jerarquía de mensajes

### Persistencia

- **Sin límite de caducidad**: Las campañas de banners no tienen un límite de caducidad de 30 días como las tarjetas de contenido, lo que permite una verdadera persistencia de los mensajes.

## Cuándo migrar

Considera la posibilidad de migrar a Banners si utilizas tarjetas de contenido para:

- Héroes de la página de inicio, promociones en la página de producto, ofertas en la caja
- Anuncios persistentes de navegación o mensajes en la barra lateral
- Mensajes siempre activos durante más de 30 días
- Mensajes en los que deseas personalización y elegibilidad en tiempo real

## Cuándo guardar las tarjetas de contenido

Sigue utilizando las tarjetas de contenido si lo necesitas:

- **Alimentar experiencias:** Cualquier caso de uso que implique múltiples mensajes desplazables o un "buzón de entrada" basado en tarjetas.
- **Características específicas:** Mensajes que requieren contenido conectado o códigos promocionales, ya que los banners no los admiten de forma nativa.
- **Entrega desencadenada:** Casos de uso que requieren estrictamente una entrega desencadenada por API o basada en acciones. Aunque los banners no admiten la entrega basada en acciones o desencadenada por API, la evaluación de elegibilidad en tiempo real significa que los usuarios se califican o descalifican instantáneamente en función de su pertenencia a un segmento en cada actualización.

## Guía de migración

### Requisitos previos

Antes de migrar, asegúrate de que tu SDK de Braze cumple los requisitos mínimos de versión:

{% multi_lang_include sdk_versions.md feature='banners' %}

### Suscribirse a las actualizaciones

#### Enfoque de las tarjetas de contenido

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

#### Acercamiento de pancartas

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  // Get banner for specific placement
  const globalBanner = braze.getBanner("global_banner");
  if (globalBanner) {
    console.log("Banner received for placement:", globalBanner.placementId);
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  // Get banner for specific placement
  val globalBanner = Braze.getInstance(context).getBanner("global_banner")
  if (globalBanner != null) {
    Log.d(TAG, "Banner received for placement: ${globalBanner.placementId}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.subscribeToUpdates { banners in
  // Get banner for specific placement
  braze.banners.getBanner(for: "global_banner") { banner in
    if let banner = banner {
      print("Banner received for placement: \(banner.placementId)")
    }
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.BANNER_CARDS_UPDATED, (data) => {
  const banners = data.banners;
  // Get banner for specific placement
  Braze.getBanner("global_banner").then(banner => {
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
  braze.getBanner("global_banner").then((banner) {
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
Las tarjetas de contenido pueden renderizarse manualmente con una lógica de interfaz de usuario personalizada, mientras que las pancartas sólo pueden renderizarse con los métodos del SDK listos para usar.
{% endalert %}

#### Enfoque de las tarjetas de contenido

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

#### Acercamiento de pancartas

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  braze.insertBanner(globalBanner, container);

  if (globalBanner.isControl) {
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner"]);
```
{% endtab %}
{% tab Android %}
```kotlin
// Using BannerView in XML
// <com.braze.ui.banners.BannerView
//     android:id="@+id/banner_view"
//     android:layout_width="match_parent"
//     android:layout_height="wrap_content"
//     app:placementId="global_banner" />

// Or programmatically
val bannerView = BannerView(context).apply {
  placementId = "global_banner"
}
container.addView(bannerView)

Braze.getInstance(context).requestBannersRefresh(listOf("global_banner"))
```
{% endtab %}
{% tab Swift %}
```swift
// Using BannerUIView
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "global_banner",
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

braze.banners.requestBannersRefresh(placementIds: ["global_banner"])
```
{% endtab %}
{% tab React Native %}
```javascript
// Using BrazeBannerView component
<Braze.BrazeBannerView
  placementID='global_banner'
/>

// Or get banner data
const banner = await Braze.getBanner("global_banner");
if (banner) {
  // Render custom banner UI
}

Braze.requestBannersRefresh(["global_banner"]);
```
{% endtab %}
{% tab Flutter %}
```dart
// Using BrazeBannerView widget
BrazeBannerView(
  placementId: "global_banner",
)

// Or get banner data
final banner = await braze.getBanner("global_banner");
if (banner != null) {
  // Render custom banner UI
}

braze.requestBannersRefresh(["global_banner"]);
```
{% endtab %}
{% endtabs %}

### Análisis de registros (implementaciones personalizadas)

{% alert note %}
Tanto las tarjetas de contenido como las pancartas realizan un seguimiento automático de los análisis cuando utilizan sus componentes predeterminados de interfaz de usuario. Los ejemplos siguientes son para implementaciones personalizadas en las que construyes tu propia interfaz de usuario.
{% endalert %}

#### Enfoque de las tarjetas de contenido

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

#### Acercamiento de pancartas

{% tabs %}
{% tab Web %}

{% alert important %}
Los análisis se siguen automáticamente cuando se utiliza `insertBanner()`. El registro manual no debe utilizarse cuando se usa `insertBanner()`.
{% endalert %}

```javascript
// Analytics are automatically tracked when using insertBanner()
// Manual logging should not be used when using insertBanner()

// For custom implementations, use manual logging methods:
// Log impression
braze.logBannerImpressions([globalBanner]);

// Log click (with optional buttonId)
braze.logBannerClick("global_banner", buttonId);
```
{% endtab %}
{% tab Android %}

{% alert important %}
Los análisis se siguen automáticamente cuando se utiliza BannerView. El registro manual no debe utilizarse cuando se usa BannerView.
{% endalert %}

```kotlin
// Analytics are automatically tracked when using BannerView
// Manual logging should not be used for default BannerView

// For custom implementations, use manual logging methods:
// Log impression
Braze.getInstance(context).logBannerImpression("global_banner");

// Log click (with optional buttonId)
Braze.getInstance(context).logBannerClick("global_banner", buttonId);
```
{% endtab %}
{% tab Swift %}

{% alert important %}
Los análisis se siguen automáticamente al utilizar BannerUIView. El registro manual no debe utilizarse para el BannerUIView predeterminado.
{% endalert %}

```swift
// Analytics are automatically tracked when using BannerUIView
// Manual logging should not be used for default BannerUIView

// For custom implementations, use manual logging methods:
// Log impression
braze.banners.logImpression(placementId: "global_banner")

// Log click (with optional buttonId)
braze.banners.logClick(placementId: "global_banner", buttonId: buttonId)

// Control groups are automatically handled by BannerUIView
```
{% endtab %}
{% tab React Native %}

{% alert important %}
Los análisis se siguen automáticamente cuando se utiliza BrazeBannerView. No es necesario el registro manual.
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
Los análisis se siguen automáticamente cuando se utiliza BrazeBannerView. No es necesario el registro manual.
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### Manipulación de grupos de control

#### Enfoque de las tarjetas de contenido

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

#### Acercamiento de pancartas

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  
  // Always call insertBanner to track impression (including control)
  braze.insertBanner(globalBanner, container);
  
  // Hide if control group
  if (globalBanner.isControl) {
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
  placementId = "global_banner"
}
```
{% endtab %}
{% tab Swift %}
```swift
// BannerUIView automatically handles control groups
// No additional code needed
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "global_banner",
  braze: braze
)
```
{% endtab %}
{% tab React Native %}
```javascript
// BrazeBannerView automatically handles control groups
// No additional code needed
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```
{% endtab %}
{% tab Flutter %}
```dart
// BrazeBannerView automatically handles control groups
// No additional code needed
BrazeBannerView(
  placementId: "global_banner",
)
```
{% endtab %}
{% endtabs %}

## Limitaciones

Cuando migres de tarjetas de contenido a banners, ten en cuenta las siguientes limitaciones:

### Migración de mensajes desencadenados

Los banners sólo sirven para campañas de entrega programada. Para migrar un mensaje que antes estaba desencadenado por una API o basado en una acción, conviértelo en una orientación basada en segmentos:

- **Ejemplo:** En lugar de desencadenar una tarjeta de "Perfil completo" con la API, crea un segmento para los usuarios que se registraron en los últimos 7 días pero no han completado su perfil.
- **Elegibilidad en tiempo real:** Los usuarios se califican o descalifican para el Banner instantáneamente en cada actualización en función de su pertenencia a un segmento.

### Diferencias de características

| Característica | Tarjetas de contenido | Banners |
|---------|--------------|---------|
| **Estructura del contenido** |
| Múltiples tarjetas en la fuente | ✅ Compatible | ✅ Puedes crear múltiples colocaciones para conseguir una implementación tipo carrusel. Sólo se devuelve un banner por colocación. |
| Colocaciones múltiples | N/A | ✅ Se admiten múltiples colocaciones |
| Tipos de tarjeta (clásica, con subtítulos, sólo imagen) | ✅ Múltiples tipos predefinidos | ✅ Banner único basado en HTML (más flexible) |
| **Gestión de contenidos** |
| Editor de arrastrar y soltar | ❌ Requiere desarrollador para la personalización | ✅ Los especialistas en marketing pueden crear/actualizar sin ingeniería |
| HTML/CSS personalizado | ❌ Limitado a la estructura de la tarjeta | ✅ Soporte completo HTML/CSS |
| Pares clave-valor para la personalización | ✅ Necesario para una personalización avanzada | ✅ Pares clave-valor fuertemente tipados llamados "propiedades" para una personalización avanzada |
| **Persistencia & Expiración** |
| Caducidad de la tarjeta | ✅ Soportado (límite de 30 días) | ✅ Admitido (sin límite de caducidad) |
| Verdadera persistencia | ❌ Máximo de 30 días | ✅ Persistencia ilimitada |
| **Mostrar & Orientación** |
| IU de la fuente | ✅ Fuente predeterminada disponible | ❌ Sólo basado en la colocación |
| Colocación en función del contexto | ❌ Basado en la fuente | ✅ Soporte nativo de colocación |
| Priorización nativa | ❌ Requiere una lógica personalizada | ✅ Priorización incorporada |
| **Interacción con el usuario** |
| Despido manual | ✅ Compatible | ❌ No compatible |
| Tarjetas ancladas | ✅ Compatible | N/A |
| **Análisis** |
| Análisis automáticos (IU predeterminada) | ✅ Compatible | ✅ Compatible |
| Clasificación por prioridades | ❌ No compatible | ✅ Compatible | 
| **Actualizaciones de contenido** |
| Actualización de la plantilla Liquid | ❌ Una vez por tarjeta en el envío/lanzamiento | ✅ Se actualiza con cada actualización |
| Actualización de la elegibilidad | ❌ Una vez por tarjeta en el envío/lanzamiento | ✅ Se refresca en cada sesión |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Limitaciones del producto

- Hasta 25 mensajes activos por colocación.
- Hasta 10 ID de ubicación por solicitud de actualización; las solicitudes que superen este número se truncarán.

### Limitaciones del SDK

- Los banners no son compatibles actualmente con las plataformas .NET MAUI (Xamarin), Cordova, Unity, Vega o TV.
- Asegúrate de que utilizas las versiones mínimas del SDK indicadas en los requisitos previos.

## Artículos relacionados

- [Colocación de banners]({{site.baseurl}}/developer_guide/banners/placements)
- [Tutorial: Mostrar un Banner por ID de Colocación]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Análisis de banners]({{site.baseurl}}/developer_guide/banners/analytics)
- [Pancartas FAQ]({{site.baseurl}}/developer_guide/banners/faq)

