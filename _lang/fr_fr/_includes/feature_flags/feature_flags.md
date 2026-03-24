# Indicateurs de fonctionnalité

> Les indicateurs de fonctionnalité vous permettent d'activer ou de désactiver à distance des fonctionnalités pour une sélection spécifique ou aléatoire d'utilisateurs. Point essentiel : ils vous permettent d'activer et de désactiver une fonctionnalité en production sans déploiement de code supplémentaire ni mise à jour sur les app stores. Vous pouvez ainsi déployer de nouvelles fonctionnalités en toute sécurité et en toute confiance.

{% alert tip %}
Lorsque vous êtes prêt à créer vos propres indicateurs de fonctionnalité, consultez la rubrique [Création d'indicateurs de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/create/).
{% endalert %}

## Conditions préalables

Voici les versions minimales du SDK nécessaires pour commencer à utiliser les indicateurs de fonctionnalité :

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## Cas d'utilisation

### Déploiements progressifs

Utilisez des indicateurs de fonctionnalité pour activer progressivement des fonctionnalités auprès d'un échantillon de population. Par exemple, vous pouvez lancer en douceur une nouvelle fonctionnalité auprès de vos utilisateurs VIP en priorité. Cette stratégie permet d'atténuer les risques liés au déploiement simultané de nouvelles fonctionnalités pour tout le monde et de détecter les bogues rapidement.

![Image animée du curseur de trafic de déploiement passant de 0 % à 100 %.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

Par exemple, imaginons que nous avons décidé d'ajouter un nouveau lien « Live Chat Support » à notre application pour accélérer le service client. Nous pourrions publier cette fonctionnalité pour tous les clients en même temps. Cependant, un déploiement global comporte des risques, tels que :

* Notre équipe d'assistance est encore en formation, et les clients pourront ouvrir des tickets d'assistance dès la mise en ligne. Cela ne nous laisse aucune marge de manœuvre si l'équipe d'assistance a besoin de plus de temps.
* Nous ne connaissons pas le volume réel de nouveaux cas d'assistance que nous recevrons, et nos effectifs pourraient ne pas être suffisants.
* Si notre équipe d'assistance est submergée, nous n'avons aucun moyen de désactiver rapidement cette fonctionnalité.
* Des bogues pourraient être introduits dans le widget de chat, et nous ne voulons pas que les clients aient une expérience négative.

Avec les indicateurs de fonctionnalité de Braze, nous pouvons déployer progressivement la fonctionnalité et atténuer tous ces risques :

* Nous activerons la fonctionnalité « Assistance en direct » lorsque l'équipe d'assistance indiquera qu'elle est prête.
* Nous activerons cette nouvelle fonctionnalité pour seulement 10 % des utilisateurs afin de vérifier si nos effectifs sont suffisants.
* En cas de bogues, nous pourrons rapidement désactiver la fonctionnalité au lieu de nous précipiter pour publier une nouvelle version.

Pour déployer progressivement cette fonctionnalité, nous pouvons [créer un indicateur de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/create/) nommé « Live Chat Widget ».

![Détails de l'indicateur de fonctionnalité pour un exemple nommé Live Chat Widget. L'ID est enable_live_chat. La description de cet indicateur de fonctionnalité indique que le widget de chat en direct s'affichera sur la page d'assistance.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

Dans le code de notre application, nous n'afficherons le bouton **Start Live Chat** que lorsque l'indicateur de fonctionnalité Braze est activé :

{% tabs %}
{% tab JavaScript %}

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
  Need help? <button>Email Our Team</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)
```

{% endtab %}
{% tab Java %}

```java
// Get the initial value from the Braze SDK
FeatureFlag featureFlag = braze.getFeatureFlag("enable_live_chat");
Boolean liveChatEnabled = featureFlag != null && featureFlag.getEnabled();

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(event -> {
  FeatureFlag newFeatureFlag = braze.getFeatureFlag("enable_live_chat");
  Boolean newValue = newFeatureFlag != null && newFeatureFlag.getEnabled();
  liveChatEnabled = newValue;
});

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Get the initial value from the Braze SDK
val featureFlag = braze.getFeatureFlag("enable_live_chat")
var liveChatEnabled = featureFlag?.enabled

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates() { event ->
  val newValue = braze.getFeatureFlag("enable_live_chat")?.enabled
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}

```

{% endtab %}
{% tab Swift %}

```swift
// Get the initial value from the Braze SDK
let featureFlag = braze.featureFlags.featureFlag(id: "enable_live_chat")
var liveChatEnabled = featureFlag?.enabled ?? false

// Listen for updates from the Braze SDK
braze.featureFlags.subscribeToUpdates() { _ in  
  let newValue = braze.featureFlags.featureFlag(id: "enable_live_chat")?.enabled ?? false
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
liveChatView.isHidden = !liveChatEnabled
```

{% endtab %}
{% endtabs %}

### Contrôle à distance des variables d'application

Utilisez des indicateurs de fonctionnalité pour modifier le comportement de votre application en production. Cela peut s'avérer particulièrement important pour les applications mobiles, où les validations des app stores empêchent de déployer rapidement des modifications pour tous les utilisateurs.

Par exemple, imaginons que notre équipe marketing souhaite afficher nos ventes et promotions en cours dans la navigation de notre application. Normalement, nos ingénieurs ont besoin d'une semaine de délai pour tout changement et de trois jours pour la validation de l'app store. Mais avec Thanksgiving, le Black Friday, le Cyber Monday, Hanukkah, Noël et le Nouvel An concentrés sur deux mois, nous ne serons pas en mesure de respecter ces délais serrés.

Grâce aux indicateurs de fonctionnalité, nous pouvons laisser Braze alimenter le contenu du lien de navigation de notre application, ce qui permet à notre responsable marketing d'effectuer des changements en quelques minutes plutôt qu'en plusieurs jours.

Pour configurer cette fonctionnalité à distance, nous allons créer un indicateur de fonctionnalité appelé `navigation_promo_link` et définir les propriétés initiales suivantes :

![Indicateur de fonctionnalité avec des propriétés de lien et de texte renvoyant à une page de vente générique.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

Dans notre application, nous utiliserons les méthodes getter de Braze pour récupérer les propriétés de cet indicateur de fonctionnalité et construire les liens de navigation en fonction de ces valeurs :

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">Home</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">Products</a>
    <a href="/categories">Categories
  </div>
</>)
```

{% endtab %}
{% tab Java %}

```java
// liveChatView is the View container for the Live Chat UI
FeatureFlag featureFlag = braze.getFeatureFlag("navigation_promo_link");
if (featureFlag != null && featureFlag.getEnabled()) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
liveChatView.setPromoLink(featureFlag.getStringProperty("link"));
liveChatView.setPromoText(featureFlag.getStringProperty("text"));

```

{% endtab %}
{% tab Kotlin %}

```kotlin
// liveChatView is the View container for the Live Chat UI
val featureFlag = braze.getFeatureFlag("navigation_promo_link")
if (featureFlag?.enabled == true) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}
liveChatView.promoLink = featureFlag?.getStringProperty("link")
liveChatView.promoText = featureFlag?.getStringProperty("text")
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "navigation_promo_link")
if let featureFlag {
  liveChatView.isHidden = !featureFlag.enabled
} else {
  liveChatView.isHidden = true
}
liveChatView.promoLink = featureFlag?.stringProperty("link")
liveChatView.promoText = featureFlag?.stringProperty("text")
```

{% endtab %}
{% endtabs %}

La veille de Thanksgiving, il nous suffit de modifier ces valeurs de propriété dans le tableau de bord de Braze.

![Indicateur de fonctionnalité avec des propriétés de lien et de texte renvoyant à une page de vente de Thanksgiving.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

Ainsi, la prochaine fois que quelqu'un ouvrira l'application, il verra les nouvelles offres de Thanksgiving.

### Coordination des messages

Utilisez des indicateurs de fonctionnalité pour synchroniser le déploiement d'une fonctionnalité et l'envoi de messages, et renforcer la collaboration entre les équipes produit et marketing. En coordonnant les sorties de fonctionnalités et les messages via les indicateurs de fonctionnalité, les deux équipes peuvent aligner leurs stratégies et créer des expériences utilisateur cohérentes.

Imaginons par exemple que nous lancions un nouveau programme de fidélité pour nos utilisateurs. Il peut être difficile pour les équipes marketing et produit de coordonner parfaitement le calendrier des messages promotionnels avec le déploiement d'une fonctionnalité. Cependant, avec les indicateurs de fonctionnalité dans Canvas, notre équipe produit peut appliquer une logique sophistiquée pour activer une fonctionnalité auprès d'une audience spécifique, tandis que notre équipe marketing contrôle les messages associés envoyés à ces mêmes utilisateurs.

Pour coordonner efficacement le déploiement et l'envoi de messages, nous allons créer un indicateur de fonctionnalité appelé `show_loyalty_program`. Pour notre première phase de déploiement, nous laisserons Canvas contrôler quand et pour qui l'indicateur de fonctionnalité est activé. Pour l'instant, nous laisserons le pourcentage de déploiement à 0 % et ne sélectionnerons aucun segment cible.

![Indicateur de fonctionnalité portant le nom Programme de fidélité. L'ID est show_loyalty_program, et la description indique que le nouveau programme de fidélité s'affiche sur l'écran d'accueil et la page de profil.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

Ensuite, dans Canvas, nous créerons une [étape Indicateur de fonctionnalité]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) qui active l'indicateur de fonctionnalité `show_loyalty_program` pour notre segment « Clients à forte valeur » :

![Exemple de Canvas avec une étape de répartition de l'audience où le segment des clients à forte valeur active l'indicateur de fonctionnalité show_loyalty_program.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

Les utilisateurs de ce segment commenceront alors à voir le nouveau programme de fidélité. Une fois la fonctionnalité activée, un e-mail et une enquête seront envoyés automatiquement pour aider nos équipes à recueillir des retours.

### Expérimentation des fonctionnalités

Utilisez des indicateurs de fonctionnalité pour expérimenter et valider vos hypothèses concernant une nouvelle fonctionnalité. En répartissant le trafic en deux groupes ou plus, vous pouvez comparer l'impact d'un indicateur de fonctionnalité entre les groupes et déterminer la meilleure marche à suivre en fonction des résultats.

Un [test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) est un outil puissant qui permet de comparer les réponses des utilisateurs à plusieurs versions d'une variable.

Dans cet exemple, notre équipe a créé un nouveau flux de paiement pour notre application e-commerce. Même si nous sommes convaincus qu'il améliore l'expérience utilisateur, nous souhaitons réaliser un test A/B pour mesurer son impact sur le chiffre d'affaires de notre application.

Pour commencer, nous allons créer un nouvel indicateur de fonctionnalité appelé `enable_checkout_v2`. Nous n'ajouterons ni audience ni pourcentage de déploiement. Nous utiliserons plutôt une expérience d'indicateur de fonctionnalité pour répartir le trafic, activer la fonctionnalité et mesurer le résultat.

Dans notre application, nous vérifierons si l'indicateur de fonctionnalité est activé ou non et basculerons le flux de paiement en conséquence :

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag?.enabled) {
  return <NewCheckoutFlow />  
} else {
  return <OldCheckoutFlow />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewCheckoutFlow();
} else {
  return new OldCheckoutFlow();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("enable_checkout_v2")
braze.logFeatureFlagImpression("enable_checkout_v2")
if (featureFlag?.enabled == true) {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "enable_checkout_v2")
braze.featureFlags.logFeatureFlagImpression(id: "enable_checkout_v2")
if let featureFlag, featureFlag.enabled {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% endtabs %}

Nous configurerons notre test A/B dans le cadre d'une [expérience d'indicateur de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/experiments/).

Désormais, 50 % des utilisateurs verront l'ancienne expérience, tandis que les 50 % restants verront la nouvelle. Nous pourrons ensuite analyser les deux variantes pour déterminer quel flux de paiement a généré le taux de conversion le plus élevé. {% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

![Une expérience d'indicateur de fonctionnalité répartissant le trafic en deux groupes de 50 %.]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

Une fois le gagnant identifié, nous pourrons arrêter cette campagne et porter le pourcentage de déploiement de l'indicateur de fonctionnalité à 100 % pour tous les utilisateurs, pendant que notre équipe d'ingénieurs intègre cette fonctionnalité en dur dans la prochaine version de l'application.

### Segmentation

Utilisez le filtre **Indicateur de fonctionnalité** pour créer un segment ou cibler l'envoi de messages aux utilisateurs selon qu'un indicateur de fonctionnalité est activé ou non. Par exemple, imaginons que nous ayons un indicateur de fonctionnalité qui contrôle le contenu premium dans notre application. Nous pourrions créer un segment filtrant les utilisateurs pour lesquels l'indicateur de fonctionnalité n'est pas activé, puis envoyer à ce segment un message les incitant à mettre leur compte à niveau pour accéder au contenu premium.

![]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

Pour en savoir plus sur le filtrage des segments, consultez [Créer un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

{% alert note %}
Pour éviter les segments récursifs, il n'est pas possible de créer un segment faisant référence à d'autres indicateurs de fonctionnalité.
{% endalert %}

## Limites selon le plan

Voici les limites des indicateurs de fonctionnalité pour les plans gratuits et payants.

| Fonctionnalité                                                                                                   | Version gratuite     | Version payante      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [Indicateurs de fonctionnalité actifs](#active-feature-flags)                                                                     | 10 par espace de travail | 110 par espace de travail |
| [Expériences de campagnes actives]({{site.baseurl}}/developer_guide/feature_flags/experiments/)          | 1 par espace de travail  | 100 par espace de travail |
| [Étapes du Canvas pour l'indicateur de fonctionnalité]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) | Illimité        | Illimité         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Un indicateur de fonctionnalité est considéré comme actif et sera comptabilisé dans votre limite si l'une des conditions suivantes est remplie :

- Le taux de déploiement est supérieur à 0 %
- Utilisé dans un Canvas actif
- Utilisé dans une expérience active

Même si un indicateur de fonctionnalité répond à plusieurs critères (par exemple, s'il est utilisé dans un Canvas et que le déploiement est à 50 %), il ne comptera que pour un seul indicateur de fonctionnalité actif dans votre limite.

{% alert note %}
Pour acheter la version payante des indicateurs de fonctionnalité, contactez votre Account Manager Braze ou demandez une mise à niveau dans le tableau de bord de Braze.
{% endalert %}