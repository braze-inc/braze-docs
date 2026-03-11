---
nav_title: "Migration depuis les cartes de contenu"
article_title: "Migration des cartes de contenu vers les bannières"
description: "Découvrez comment effectuer la migration des cartes de contenu vers les bannières, avec des exemples de code pour tous les SDK pris en charge, les limitations et les avantages."
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

# Migration des cartes de contenu vers les bannières

> Ce guide vous assiste dans la migration des cartes de contenu vers les bannières pour les cas d'utilisation d'envoi de messages de type bannière. Les bannières sont idéales pour les messages in-app, persistants dans les applications et sur le Web, qui apparaissent à des emplacements spécifiques dans votre application.

## Pourquoi effectuer la migration vers Banners ?

- Si votre équipe d'ingénieurs crée ou gère des cartes de contenu personnalisées, la migration vers Banners peut réduire cet investissement continu. Les bannières permettent aux marketeurs de contrôler directement l'interface utilisateur, libérant ainsi les développeurs pour d'autres tâches.
- Si vous lancez de nouveaux messages sur la page d'accueil, des flux d'onboarding ou des annonces persistantes, veuillez commencer par les bannières plutôt que de créer des cartes de contenu. Vous pouvez bénéficier d'une personnalisation en temps réel, sans expiration après 30 jours, sans limite de taille et avec une priorisation native dès le premier jour.
- Si vous travaillez avec une limite d'expiration de 30 jours, gérez une logique de rééligibilité complexe ou êtes confronté à une personnalisation obsolète, Banners résout ces problèmes de manière native.

Les bannières présentent plusieurs avantages par rapport aux cartes de contenu pour l'envoi de messages de type bannière :

### Production accélérée

- **Réduction du soutien technique continu requis** : Les marketeurs peuvent créer des messages personnalisés à l'aide d'un éditeur par glisser-déposer et d'un code HTML personnalisé sans avoir besoin de l'aide d'un développeur pour la personnalisation.
- **Options de personnalisation flexibles** : Concevez directement dans l'éditeur, utilisez le langage HTML ou exploitez les modèles de données existants avec des propriétés personnalisées.

### Une meilleure expérience utilisateur

- **Mises à jour dynamiques du contenu dynamique** : Les bannières actualisent la logique Liquid et l'éligibilité à chaque actualisation, garantissant ainsi que les utilisateurs voient toujours le contenu le plus pertinent.
- **Prise en charge du placement natif** : Les messages apparaissent dans des contextes spécifiques plutôt que dans un fil d'actualité, ce qui améliore la pertinence contextuelle.
- **Priorisation native** : Contrôle de l'ordre d'affichage sans logique personnalisée, facilitant la gestion de la hiérarchie des messages.

### Persistance

- **Aucune date d'expiration** : Les campagnes de bannières n'ont pas de limite d'expiration de 30 jours comme les cartes de contenu, ce qui permet une véritable persistance des messages.

## Quand migrer

Envisagez la migration vers Banners si vous utilisez les cartes de contenu pour :

- Héros de la page d'accueil, promotions sur les pages produits, offres à la caisse
- Annonces de navigation persistantes ou messages dans la barre latérale
- Messages permanents diffusés pendant plus de 30 jours
- Messages pour lesquels vous souhaitez une personnalisation et une adéquation en temps réel

## Quand conserver les cartes de contenu

Veuillez continuer à utiliser les cartes de contenu si nécessaire :

- **Expériences de nourrissage :** Tout cas d'utilisation impliquant plusieurs messages défilables ou une « boîte de réception » sous forme de cartes.
- **Fonctionnalités spécifiques :** Les messages qui nécessitent du contenu connecté ou des codes de promotion, car les bannières ne les prennent pas en charge de manière native.
- **Réception/distribution déclenchée :** Cas d'utilisation nécessitant strictement une réception/distribution déclenchée par une API ou basée sur une livraison par événement. Bien que les bannières ne prennent pas en charge la réception/distribution déclenchée par API ou basée sur des événements, l'évaluation d'éligibilité en temps réel signifie que les utilisateurs sont instantanément qualifiés ou disqualifiés en fonction de leur appartenance à un segment à chaque actualisation.

## Guide de migration

### Conditions préalables

Avant de procéder à la migration, veuillez vous assurer que votre SDK Braze répond aux exigences minimales en matière de version :

{% multi_lang_include sdk_versions.md feature='banners' %}

### S'abonner aux mises à jour

#### Approche par cartes de contenu

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

#### Approche des bannières

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

### Afficher le contenu

{% alert note %}
Les cartes de contenu peuvent être rendues manuellement à l'aide d'une logique d'interface utilisateur personnalisée, tandis que les bannières ne peuvent être rendues qu'à l'aide des méthodes SDK prêtes à l'emploi.
{% endalert %}

#### Approche par cartes de contenu

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

#### Approche des bannières

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

### Analyse des journaux (implémentations personnalisées)

{% alert note %}
Les cartes de contenu et les bannières effectuent automatiquement le suivi des analyses lorsqu'elles utilisent leurs composants d'interface utilisateur par défaut. Les exemples ci-dessous concernent des implémentations personnalisées dans lesquelles vous créez votre propre interface utilisateur.
{% endalert %}

#### Approche par cartes de contenu

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

#### Approche des bannières

{% tabs %}
{% tab Web %}

{% alert important %}
Les analyses sont automatiquement suivies lors de l'utilisation de `insertBanner()`. La journalisation manuelle ne devrait pas être utilisée lorsque vous utilisez `insertBanner()`.
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
Les analyses sont automatiquement suivies lorsque vous utilisez BannerView. La journalisation manuelle n'est pas recommandée lors de l'utilisation de BannerView.
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
Les analyses sont automatiquement suivies lors de l'utilisation de BannerUIView. La journalisation manuelle ne doit pas être utilisée pour BannerUIView par défaut.
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
Les analyses sont automatiquement suivies lors de l'utilisation de BrazeBannerView. Aucune connexion manuelle n'est nécessaire.
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
Les analyses sont automatiquement suivies lors de l'utilisation de BrazeBannerView. Aucune connexion manuelle n'est nécessaire.
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### Gestion des groupes de contrôle

#### Approche par cartes de contenu

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

#### Approche des bannières

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

## Restrictions

Lors de la migration des cartes de contenu vers les bannières, veuillez tenir compte des restrictions suivantes :

### Migration des messages déclenchés

Les bannières ne prennent en charge que les campagnes de livraison avec planification. Pour migrer un message précédemment déclenché par une API ou basé sur une action, veuillez le convertir en ciblage basé sur un segment :

- **Exemple :** Au lieu de déclencher une carte « Profil complet » avec l'API, veuillez créer un segment pour les utilisateurs qui se sont inscrits au cours des 7 derniers jours mais qui n'ont pas encore complété leur profil.
- **Admissibilité en temps réel :** Les utilisateurs sont automatiquement admissibles ou non à la bannière à chaque actualisation, en fonction de leur appartenance à un segment.

### Différences de fonctionnalités

| Fonctionnalité | Cartes de contenu | Bannières |
|---------|--------------|---------|
| **Structure du contenu** |
| Plusieurs cartes dans le flux | ✅ Pris en charge | ✅ Permet de créer plusieurs emplacements pour obtenir une mise en œuvre de type carrousel. Une seule bannière est renvoyée par emplacement. |
| Placements multiples | S.O. | ✅ Prise en charge de plusieurs emplacements |
| Types de cartes (classique, avec légende, image uniquement) | ✅ Plusieurs types prédéfinis | Bannière HTML unique (plus flexible) |
| **Gestion de contenu** |
| Éditeur par glisser-déposer | ❌ Nécessite l'intervention d'un développeur pour la personnalisation | ✅ Les marketeurs peuvent créer/mettre à jour sans intervention technique. |
| HTML/CSS personnalisé | Limité à la structure de la carte | ✅ Prise en charge complète HTML/CSS |
| Paires clé-valeur pour la personnalisation | ✅ Nécessaire pour une personnalisation avancée | ✅ Paires clé-valeur fortement typées appelées « propriétés » pour une personnalisation avancée |
| **Persistance&  Expiration** |
| Expiration de la carte | ✅ Pris en charge (limite de 30 jours) | ✅ Pris en charge (sans limite d'expiration) |
| Véritable persévérance | ❌ Maximum de 30 jours | Persévérance illimitée |
| **Ciblage &d'affichage** |
| Interface utilisateur du flux | ✅ Flux par défaut disponible | ❌ Basé uniquement sur le placement |
| Placement contextuel | ❌ Basé sur l'alimentation | ✅ Prise en charge native du placement |
| Priorisation native | ❌ Nécessite une logique personnalisée | ✅ Priorisation intégrée |
| **Interaction avec l'utilisateur** |
| Licenciement manuel | ✅ Pris en charge | ❌ Non pris en charge |
| Cartes épinglées | ✅ Pris en charge | S.O. |
| **Analyse** |
| Analyses automatiques (interface utilisateur par défaut) | ✅ Pris en charge | ✅ Pris en charge |
| Tri par priorité | ❌ Non pris en charge | ✅ Pris en charge | 
| **Mises à jour du contenu** |
| Actualisation du modèle liquide | Une fois par carte lors de l'envoi/du lancement | ✅ Se rafraîchit à chaque actualisation |
| Actualisation des conditions d'admissibilité | Une fois par carte lors de l'envoi/du lancement | ✅ Actualise à chaque session |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Limites du produit

- Jusqu'à 25 messages actifs par emplacement.
- Jusqu'à 10 ID de placement par demande d'actualisation ; les demandes supplémentaires sont tronquées.

### Limitations du SDK

- Les bannières ne sont actuellement pas prises en charge sur les plateformes .NET MAUI (Xamarin), cordova, Unity, Vega ou TV.
- Veuillez vous assurer que vous utilisez les versions minimales du SDK indiquées dans les prérequis.

## Articles connexes

- [Emplacements des bannières]({{site.baseurl}}/developer_guide/banners/placements)
- [Tutoriel : Affichage d'une bannière par ID de placement]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Analyse des bannières]({{site.baseurl}}/developer_guide/banners/analytics)
- [FAQ sur les bannières]({{site.baseurl}}/developer_guide/banners/faq)

