---
nav_title: "Migration à partir des cartes de contenu"
article_title: "Migrer des cartes de contenu vers les bannières"
description: "Découvrez comment migrer des cartes de contenu vers les bannières, y compris des exemples de code pour tous les SDK pris en charge, les limitations et les avantages."
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

# Migrer des cartes de contenu vers les bannières

> Ce guide vous aide à migrer des cartes de contenu vers les bannières pour les cas d'utilisation d'envoi de messages de type bannière. Les bannières sont idéales pour les messages in-app et web persistants, en ligne, qui apparaissent à des endroits spécifiques de votre application.

## Pourquoi migrer vers les bannières ?

- Si votre équipe d'ingénieurs crée ou maintient des cartes de contenu de type bannière personnalisées, la migration vers les bannières peut réduire cet investissement. Les bannières permettent aux marketeurs de contrôler directement l'interface utilisateur, libérant ainsi les développeurs pour d'autres tâches.
- Si vous lancez de nouveaux messages sur la page d'accueil, des flux d'onboarding ou des annonces persistantes, commencez par des bannières plutôt que de créer des cartes de contenu. Vous pouvez bénéficier d'une personnalisation en temps réel, d'une absence d'expiration de 30 jours, d'une absence de limite de taille et d'une priorisation native dès le premier jour.
- Si vous devez contourner la limite d'expiration de 30 jours, gérer une logique de rééligibilité complexe ou être frustré par une personnalisation périmée, Banners résout ces problèmes de manière native.

Les bannières offrent plusieurs avantages par rapport aux cartes de contenu de type bannière pour l'envoi de messages :

### Accélération de la production

- **Réduction de l'assistance technique permanente requise**: Les marketeurs peuvent créer des messages personnalisés à l'aide d'un éditeur par glisser-déposer et d'un code HTML personnalisé sans avoir besoin de l'aide d'un développeur pour la personnalisation.
- **Options de personnalisation souples**: Concevez directement dans l'éditeur, utilisez HTML ou exploitez les modèles de données existants avec des propriétés personnalisées.

### Meilleure interface utilisateur

- **Mise à jour dynamique du contenu**: Les bannières s'actualisent Liquid logic and eligibility à chaque actualisation, ce qui permet aux utilisateurs de toujours voir le contenu le plus pertinent.
- **Aide au placement des autochtones**: Les messages apparaissent dans des contextes spécifiques plutôt que dans un flux, offrant ainsi une meilleure pertinence contextuelle.
- **Priorité aux autochtones**: Contrôle de l'ordre d'affichage sans logique personnalisée, ce qui facilite la gestion de la hiérarchie des messages.

### Persistance

- **Pas de limite d'expiration :** Les campagnes de bannières n'ont pas de limite d'expiration de 30 jours comme les cartes de type bannière, ce qui permet une véritable persistance des messages.

## Quand migrer ?

Envisagez de migrer vers les bannières si vous utilisez les cartes de contenu de type bannière pour :

- Héros de la page d'accueil, promotions sur les pages de produits, offres à la caisse
- Annonces de navigation persistantes ou messages dans la barre latérale
- Messages toujours actifs pendant plus de 30 jours
- Messages où vous souhaitez une personnalisation et une éligibilité en temps réel.

## Quand conserver les cartes de contenu ?

Continuez à utiliser les cartes de contenu si nécessaire :

- **Expériences en matière d'alimentation :** Tout cas d'utilisation impliquant plusieurs messages défilants ou une boîte de réception basée sur des cartes.
- **Fonctionnalités spécifiques :** Les messages qui nécessitent un contenu connecté ou des codes promotionnels, car les bannières ne les prennent pas en charge de manière native.
- **Réception/distribution déclenchée :** Cas d'utilisation nécessitant strictement une réception/distribution déclenchée par l'API ou par événement. Bien que les bannières ne prennent pas en charge la réception/distribution déclenchée par l'API ou basée sur l'action, l'évaluation de l'éligibilité en temps réel signifie que les utilisateurs sont instantanément qualifiés ou disqualifiés en fonction de l'appartenance à un segment à chaque actualisation.

## Guide de migration

### Conditions préalables

Avant de procéder à la migration, assurez-vous que votre SDK Braze répond aux exigences minimales en matière de version :

{% multi_lang_include sdk_versions.md feature='banners' %}

### S'abonner aux mises à jour

#### L'approche des cartes de contenu

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

#### Approche par bannières

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
Les cartes de contenu peuvent être rendues manuellement avec une logique d'interface utilisateur personnalisée, alors que les bannières ne peuvent être rendues qu'avec les méthodes SDK prêtes à l'emploi.
{% endalert %}

#### L'approche des cartes de contenu

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

#### Approche par bannières

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

### Analyse/analytique des logs (implémentations personnalisées)

{% alert note %}
Les cartes de contenu et les bannières assurent automatiquement le suivi des analyses/analytiques lorsqu'elles utilisent leurs composants d'interface utilisateur par défaut. Les exemples ci-dessous concernent des implémentations personnalisées dans lesquelles vous créez votre propre interface utilisateur.
{% endalert %}

#### L'approche des cartes de contenu

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

#### Approche par bannières

{% tabs %}
{% tab Web %}

{% alert important %}
L'analyse/analytique est automatiquement suivie lors de l'utilisation de `insertBanner()`. L'enregistrement manuel ne doit pas être utilisé lorsque vous utilisez `insertBanner()`.
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
Les analyses/analytiques sont automatiquement suivies lors de l'utilisation de BannerView. L'enregistrement manuel ne doit pas être utilisé lors de l'utilisation de BannerView.
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
Les analyses/analytiques sont automatiquement suivies lors de l'utilisation de BannerUIView. L'enregistrement manuel ne doit pas être utilisé pour l'affichage par défaut de BannerUIView.
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
Les analyses/analytiques sont automatiquement suivies lors de l'utilisation de BrazeBannerView. Aucun enregistrement manuel n'est nécessaire.
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
Les analyses/analytiques sont automatiquement suivies lors de l'utilisation de BrazeBannerView. Aucun enregistrement manuel n'est nécessaire.
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

#### L'approche des cartes de contenu

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

#### Approche par bannières

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

Lors de la migration des cartes de contenu vers les bannières, tenez compte des limitations suivantes :

### Migration des messages déclenchés

Les bannières ne prennent en charge que les campagnes de réception/distribution planifiées. Pour faire migrer un message qui était auparavant déclenché par l'API ou basé sur des actions, convertissez-le en un ciblage basé sur des segments :

- **Exemple :** Au lieu de déclencher une carte "Compléter le profil" avec l'API, créez une segmentation pour les utilisateurs qui se sont inscrits au cours des 7 derniers jours mais qui n'ont pas complété leur profil.
- **Éligibilité en temps réel :** Les utilisateurs sont qualifiés ou disqualifiés pour la bannière instantanément à chaque actualisation en fonction de leur appartenance à un segment.

### Différences de fonctionnalité

| Fonctionnalité | Cartes de contenu | Bannières |
|---------|--------------|---------|
| **Structure du contenu** |
| Plusieurs cartes dans le flux | ✅ Supporté | ✅ Possibilité de créer des placements multiples pour obtenir une mise en œuvre de type carrousel. Une seule bannière est renvoyée par placement. |
| Placements multiples | S.O. | ✅ Prise en charge de placements multiples |
| Types de cartes (classique, légendée, image seule) | ✅ Plusieurs types prédéfinis | ✅ Bannière unique basée sur HTML (plus flexible) |
| **Gestion du contenu** |
| Éditeur par glisser-déposer | ❌ Nécessite un développeur pour la personnalisation | ✅ Les marketeurs peuvent créer/mettre à jour sans ingénierie |
| HTML/CSS personnalisé | ❌ Limité à la structure de la carte | ✅ Prise en charge complète de HTML/CSS |
| Paires clé-valeur pour la personnalisation | ✅ Nécessaire pour une personnalisation avancée | ✅ Des paires clé-valeur fortement typées appelées "propriétés" pour une personnalisation avancée. |
| **Persistance & Expiration** |
| Expiration de la carte | ✅ Pris en charge (limite de 30 jours) | ✅ Pris en charge (pas de limite d'expiration) |
| Une véritable persévérance | ❌ Maximum de 30 jours | ✅ Persistance illimitée |
| **Display & Ciblage** |
| Feed UI | ✅ Alimentation par défaut disponible | ❌ Basé sur le placement uniquement |
| Placement en fonction du contexte | ❌ Basé sur l'alimentation | ✅ Soutien au placement des autochtones |
| Priorité aux autochtones | ❌ Requiert une logique personnalisée | ✅ Priorité intégrée |
| **Interaction avec l'utilisateur** |
| Renvoi manuel | ✅ Supporté | ❌ Non pris en charge |
| Cartes épinglées | ✅ Supporté | S.O. |
| **Analyse** |
| Analyse/analytique automatique (si utilisée comme interface par défaut) | ✅ Supporté | ✅ Supporté |
| Tri par ordre de priorité | ❌ Non pris en charge | ✅ Supporté | 
| **Mises à jour du contenu** |
| Actualiser les modèles liquides | ❌ Une fois par carte lors de l'envoi/du lancement | ✅ S'actualise à chaque rafraîchissement |
| Actualiser l'éligibilité | ❌ Une fois par carte lors de l'envoi/du lancement | ✅ S'actualise à chaque séance |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Limites du produit

- Jusqu'à 25 messages actifs par placement.
- Jusqu'à 10 ID de placement par demande d'actualisation ; les demandes au-delà sont tronquées.

### Limitations du SDK

- Les bannières ne sont actuellement pas prises en charge sur les plateformes .NET MAUI (Xamarin), Cordova, Unity, Vega ou TV.
- Assurez-vous que vous utilisez les versions minimales du SDK indiquées dans les conditions préalables.

## Articles connexes

- [Placement de bannières]({{site.baseurl}}/developer_guide/banners/placements)
- [Tutoriel : Affichage d'une bannière par ID de placement]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Analyse/analytique des bannières (si utilisées anjectives)]({{site.baseurl}}/developer_guide/banners/analytics)
- [FAQ sur les bannières]({{site.baseurl}}/developer_guide/banners/faq)

