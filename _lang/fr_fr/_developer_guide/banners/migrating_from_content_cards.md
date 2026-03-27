---
nav_title: "Migration depuis les Cartes de contenu"
article_title: "Migration des Cartes de contenu vers les Bannières"
description: "Découvrez comment effectuer la migration des Cartes de contenu vers les Bannières, avec des exemples de code pour tous les SDK pris en charge, les limitations et les avantages."
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

# Migration des Cartes de contenu vers les Bannières

> Ce guide vous accompagne dans la migration des Cartes de contenu vers les Bannières pour les cas d'utilisation d'envoi de messages de type bannière. Les Bannières sont idéales pour les messages in-app persistants, intégrés dans vos applications et sur le Web, qui apparaissent à des emplacements spécifiques dans votre application.

## Pourquoi migrer vers les Bannières ?

- Si votre équipe d'ingénieurs crée ou maintient des Cartes de contenu personnalisées, la migration vers les Bannières peut réduire cet investissement continu. Les Bannières permettent aux marketeurs de contrôler directement l'interface utilisateur, libérant ainsi les développeurs pour d'autres tâches.
- Si vous lancez de nouveaux messages sur la page d'accueil, des flux d'onboarding ou des annonces persistantes, commencez par les Bannières plutôt que de créer des Cartes de contenu. Vous bénéficierez d'une personnalisation en temps réel, sans expiration après 30 jours, sans limite de taille et avec une priorisation native dès le premier jour.
- Si vous contournez la limite d'expiration de 30 jours, gérez une logique de rééligibilité complexe ou êtes confronté à une personnalisation obsolète, les Bannières résolvent ces problèmes de manière native.

Les Bannières présentent plusieurs avantages par rapport aux Cartes de contenu pour l'envoi de messages de type bannière :

### Production accélérée

- **Réduction du soutien technique continu requis** : Les marketeurs peuvent créer des messages personnalisés à l'aide d'un éditeur par glisser-déposer et de code HTML personnalisé, sans avoir besoin de l'aide d'un développeur pour la personnalisation.
- **Options de personnalisation flexibles** : Concevez directement dans l'éditeur, utilisez le HTML ou exploitez les modèles de données existants avec des propriétés personnalisées.

### Une meilleure expérience utilisateur

- **Mises à jour dynamiques du contenu** : Les Bannières actualisent la logique Liquid et l'éligibilité à chaque actualisation, garantissant ainsi que les utilisateurs voient toujours le contenu le plus pertinent.
- **Prise en charge native des emplacements** : Les messages apparaissent dans des contextes spécifiques plutôt que dans un fil d'actualité, ce qui améliore la pertinence contextuelle.
- **Priorisation native** : Contrôle de l'ordre d'affichage sans logique personnalisée, facilitant la gestion de la hiérarchie des messages.

### Persistance

- **Aucune limite d'expiration** : Les campagnes de Bannières n'ont pas de limite d'expiration de 30 jours comme les Cartes de contenu, ce qui permet une véritable persistance des messages.

## Quand migrer

Envisagez la migration vers les Bannières si vous utilisez les Cartes de contenu pour :

- Des héros de page d'accueil, des promotions sur les pages produits, des offres à la caisse
- Des annonces de navigation persistantes ou des messages dans la barre latérale
- Des messages permanents diffusés pendant plus de 30 jours
- Des messages pour lesquels vous souhaitez une personnalisation et une éligibilité en temps réel

## Quand conserver les Cartes de contenu

Continuez à utiliser les Cartes de contenu si vous avez besoin de :

- **Expériences de fil d'actualité :** Tout cas d'utilisation impliquant plusieurs messages défilables ou une « boîte de réception » sous forme de cartes.
- **Fonctionnalités spécifiques :** Les messages qui nécessitent du contenu connecté ou des codes promotionnels, car les Bannières ne les prennent pas en charge de manière native.
- **Réception déclenchée :** Cas d'utilisation nécessitant strictement une réception déclenchée par API ou une livraison par événement. Bien que les Bannières ne prennent pas en charge la réception déclenchée par API ou la livraison par événement, l'évaluation d'éligibilité en temps réel signifie que les utilisateurs sont instantanément qualifiés ou disqualifiés en fonction de leur appartenance à un segment à chaque actualisation.

## Guide de migration

### Conditions préalables

Avant de procéder à la migration, assurez-vous que votre SDK Braze répond aux exigences minimales en matière de version :

{% multi_lang_include sdk_versions.md feature='banners' %}

### S'abonner aux mises à jour

#### Approche par Cartes de contenu

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

#### Approche par Bannières

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

### Afficher le contenu

{% alert note %}
Les Cartes de contenu peuvent être rendues manuellement à l'aide d'une logique d'interface utilisateur personnalisée, tandis que les Bannières ne peuvent être rendues qu'à l'aide des méthodes SDK prêtes à l'emploi.
{% endalert %}

#### Approche par Cartes de contenu

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

#### Approche par Bannières

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

### Journalisation des analyses (implémentations personnalisées)

{% alert note %}
Les Cartes de contenu et les Bannières effectuent automatiquement le suivi des analyses lorsqu'elles utilisent leurs composants d'interface utilisateur par défaut. Les exemples ci-dessous concernent des implémentations personnalisées dans lesquelles vous créez votre propre interface utilisateur.
{% endalert %}

#### Approche par Cartes de contenu

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

#### Approche par Bannières

{% tabs %}
{% tab Web %}

{% alert important %}
Les analyses sont automatiquement suivies lors de l'utilisation de `insertBanner()`. La journalisation manuelle ne doit pas être utilisée avec `insertBanner()`.
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
Les analyses sont automatiquement suivies lorsque vous utilisez BannerView. La journalisation manuelle ne doit pas être utilisée avec BannerView.
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
Les analyses sont automatiquement suivies lors de l'utilisation de BannerUIView. La journalisation manuelle ne doit pas être utilisée pour BannerUIView par défaut.
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
Les analyses sont automatiquement suivies lors de l'utilisation de BrazeBannerView. Aucune journalisation manuelle n'est nécessaire.
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
Les analyses sont automatiquement suivies lors de l'utilisation de BrazeBannerView. Aucune journalisation manuelle n'est nécessaire.
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### Récupération des propriétés

#### Approche par Cartes de contenu

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

#### Approche par Bannières

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

### Gestion des groupes de contrôle

#### Approche par Cartes de contenu

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

#### Approche par Bannières

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

## Limitations

Lors de la migration des Cartes de contenu vers les Bannières, tenez compte des limitations suivantes :

### Migration des messages déclenchés

Les Bannières ne prennent en charge que les campagnes avec planification. Pour migrer un message précédemment déclenché par API ou par événement, convertissez-le en ciblage basé sur un segment :

- **Exemple :** Au lieu de déclencher une carte « Compléter le profil » via l'API, créez un segment pour les utilisateurs inscrits au cours des 7 derniers jours mais n'ayant pas encore complété leur profil.
- **Éligibilité en temps réel :** Les utilisateurs sont instantanément qualifiés ou disqualifiés pour la Bannière à chaque actualisation, en fonction de leur appartenance à un segment.

### Différences de fonctionnalités

| Fonctionnalité | Cartes de contenu | Bannières |
|---------|--------------|---------|
| **Structure du contenu** |
| Plusieurs cartes dans le flux | ✅ Pris en charge | ✅ Permet de créer plusieurs emplacements pour obtenir une implémentation de type carrousel. Une seule bannière est renvoyée par emplacement. |
| Emplacements multiples | S.O. | ✅ Prise en charge de plusieurs emplacements |
| Types de cartes (classique, avec légende, image uniquement) | ✅ Plusieurs types prédéfinis | ✅ Bannière HTML unique (plus flexible) |
| **Gestion du contenu** |
| Éditeur par glisser-déposer | ❌ Nécessite l'intervention d'un développeur pour la personnalisation | ✅ Les marketeurs peuvent créer/mettre à jour sans intervention technique |
| HTML/CSS personnalisé | ❌ Limité à la structure de la carte | ✅ Prise en charge complète HTML/CSS |
| Paires clé-valeur pour la personnalisation | ✅ Nécessaire pour une personnalisation avancée | ✅ Paires clé-valeur fortement typées appelées « propriétés » pour une personnalisation avancée |
| **Persistance et expiration** |
| Expiration de la carte | ✅ Pris en charge (limite de 30 jours) | ✅ Pris en charge (sans limite d'expiration) |
| Véritable persistance | ❌ Maximum de 30 jours | ✅ Persistance illimitée |
| **Affichage et ciblage** |
| Interface utilisateur du flux | ✅ Flux par défaut disponible | ❌ Basé uniquement sur l'emplacement |
| Placement contextuel | ❌ Basé sur le flux | ✅ Prise en charge native des emplacements |
| Priorisation native | ❌ Nécessite une logique personnalisée | ✅ Priorisation intégrée |
| **Interaction utilisateur** |
| Fermeture manuelle | ✅ Pris en charge | ❌ Non pris en charge |
| Cartes épinglées | ✅ Pris en charge | S.O. |
| **Analyse** |
| Analyses automatiques (interface utilisateur par défaut) | ✅ Pris en charge | ✅ Pris en charge |
| Tri par priorité | ❌ Non pris en charge | ✅ Pris en charge |
| **Mises à jour du contenu** |
| Actualisation du modèle Liquid | ❌ Une seule fois par carte lors de l'envoi/du lancement | ✅ Actualisé à chaque rafraîchissement |
| Actualisation de l'éligibilité | ❌ Une seule fois par carte lors de l'envoi/du lancement | ✅ Actualisé à chaque session |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Limites du produit

- Jusqu'à 25 messages actifs par emplacement.
- Jusqu'à 10 ID d'emplacement par demande d'actualisation ; les demandes au-delà de cette limite sont tronquées.

### Limitations du SDK

- Les Bannières ne sont actuellement pas prises en charge sur les plateformes .NET MAUI (Xamarin), Cordova, Unity, Vega ou TV.
- Assurez-vous d'utiliser les versions minimales du SDK indiquées dans les conditions préalables.

## Articles connexes

- [Emplacements des Bannières]({{site.baseurl}}/developer_guide/banners/placements)
- [Tutoriel : Afficher une Bannière par ID d'emplacement]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Analyse des Bannières]({{site.baseurl}}/developer_guide/banners/analytics)
- [FAQ sur les Bannières]({{site.baseurl}}/developer_guide/banners/faq)