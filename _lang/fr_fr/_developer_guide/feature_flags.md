---
page_order: 2.5
nav_title: Indicateurs de fonctionnalité
article_title: Indicateurs de fonctionnalité du SDK Braze
description: "Cet article de référence couvre un aperçu des indicateurs de fonctionnalité, y compris les prérequis et les cas d’utilisation."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web
  - Unity
  - Cordova
  - React Native
  - Flutter
  - Roku

---

# Indicateurs de fonctionnalité

> Les indicateurs de fonctionnalité vous permettent d’activer ou de désactiver à distance la fonctionnalité d’une sélection d’utilisateurs spécifique ou aléatoire. Il est important de noter qu’ils vous permettent d’activer et de désactiver une fonction dans l'environnement de production sans déployer du code supplémentaire ou mettre à jour d’applications. Cela vous permet de déployer de nouvelles fonctionnalités en toute sécurité et en toute confiance.

{% alert tip %}
Lorsque vous serez prêt à créer vos propres indicateurs de fonctionnalité, consultez la rubrique [Création d’indicateurs de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/create/).
{% endalert %}

## Conditions préalables

Il s'agit des versions minimales du SDK nécessaires pour commencer à utiliser les indicateurs de fonctionnalité :

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## Cas d’utilisation

### Déploiements progressifs

Utilisez des indicateurs de fonctionnalités pour activer progressivement les entités à une population d’échantillons. Par exemple, vous pouvez commencer par lancer une nouvelle fonctionnalité pour vos utilisateurs VIP. Cette stratégie aide à atténuer les risques associés à l’expédition de nouvelles fonctionnalités à tout le monde en même temps et permet de détecter les bogues rapidement.

![Image animée de la barre de défilement du trafic passant de 0 % à 100 %.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

Par exemple, disons que nous avons décidé d'ajouter un nouveau lien "Live Chat Support" à notre application pour un service client plus rapide. Nous pourrions publier cette fonctionnalité à tous les clients en même temps. Cependant, une publication globale comporte des risques, tels que : 

* Notre équipe d'assistance est encore en formation, et les clients peuvent commencer à envoyer des tickets d'assistance après la sortie du logiciel. Cela ne nous laisse aucune marge de manœuvre au cas où l'équipe d'assistance aurait besoin de plus de temps.
* Nous ne sommes pas sûrs du volume réel de nouveaux cas d’assistance que nous recevrons. Nous risquons donc de ne pas disposer du personnel en quantité appropriée.
* Si notre équipe d’assistance est submergée, nous n’avons aucune stratégie pour à nouveau désactiver rapidement cette fonctionnalité.
* Il est possible que des bogues soient introduits dans le widget de chat, et nous ne voulons pas que les clients aient une expérience négative.

Avec les indicateurs de fonctionnalités de Braze, nous pouvons progressivement déployer la fonction et atténuer tous ces risques :

* Nous allons activer la fonction « Assistance en direct » lorsque l’équipe d’assistance indique qu’elle est prête.
* Nous allons activer cette nouvelle fonctionnalité pour seulement 10 % des utilisateurs afin de déterminer si nos effectifs sont appropriés.
* En cas de bogues, nous pouvons rapidement désactiver la fonction au lieu de nous précipiter pour expédier une nouvelle version.

Pour déployer progressivement cette fonctionnalité, nous pouvons [créer un indicateur de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/create/) nommé "Live Chat Widget".

![Détails de l’indicateur de fonctionnalité pour un exemple nommé Widget d’assistance en direct. L'ID est enable_live_chat. La description de cette fonctionnalité indique que le widget de ligne/en production/instantané s'affichera sur la page d'assistance.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

Dans le code de notre application, nous n'afficherons le bouton **Start Live Chat** que lorsque l’indicateur de fonctionnalité Braze sera activé :

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
{% endtabs %}

### Contrôle à distance des variables d’application

Utilisez des indicateurs de fonctionnalité pour modifier la fonctionnalité de votre application en production. Cela peut être particulièrement important pour les applications mobiles, où les approbations d’App Store empêchent de déployer rapidement les modifications à tous les utilisateurs.

Par exemple, imaginons que notre équipe marketing souhaite répertorier nos ventes et promotions en cours dans la navigation de notre appli. Normalement, nos ingénieurs ont besoin d’un délai d’exécution d’une semaine pour tout changement et de trois jours pour un examen d’App Store. Mais avec Thanksgiving, le Black Friday, le Cyber Monday, Hanukkah, Noël et le jour de l'An en l'espace de deux mois, nous ne serons pas en mesure de respecter ces délais serrés.

Avec des indicateurs de fonctionnalité, nous pouvons laisser Braze alimenter le contenu de notre lien de navigation de l’application, ce qui permet à notre gestionnaire marketing de changer en quelques minutes plutôt que de jours.

Pour configurer à distance cette fonctionnalité, nous allons créer un indicateur de fonctionnalité appelé `navigation_promo_link` et définissez les propriétés initiales suivantes :

![Indicateur de fonctionnalité avec lien et propriétés de texte renvoyant à une page de vente générique.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

Dans notre application, nous utiliserons les méthodes getter de Braze pour récupérer les propriétés de cet indicateur de fonctionnalité et créer les liens de navigation en fonction de ces valeurs :

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
{% endtabs %}

Aujourd'hui, veille de Thanksgiving, il nous suffit de modifier ces valeurs de propriété dans le tableau de bord de Braze.

![Indicateur de fonctionnalité avec lien et propriétés de texte renvoyant à une page de vente de Thanksgiving.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

Ainsi, la prochaine fois que quelqu'un chargera l'application, il verra les nouvelles offres de Thanksgiving.

### Coordination des messages

Utilisez des indicateurs de fonctionnalité pour synchroniser le déploiement et l’envoi de messages d’une entité. Cela vous permettra d’utiliser Braze comme source de vérité pour votre expérience utilisateur et l’envoi de messages correspondant. Pour ce faire, cibler la nouvelle entité dans un segment particulier ou une partie filtrée de votre public. Ensuite, créez une campagne ou un canvas qui cible uniquement ce segment. 

Imaginons que nous lancions un nouveau programme de fidélité pour nos utilisateurs. Il peut être difficile pour les équipes marketing et produit de coordonner parfaitement l'envoi de messages promotionnels avec le déploiement d'une fonctionnalité. Les indicateurs de fonctionnalité dans Canvas vous permettent d'appliquer une logique sophistiquée lorsqu'il s'agit d'activer une fonctionnalité pour une audience sélectionnée et de contrôler les envois de messages à ces mêmes utilisateurs.

Pour coordonner efficacement le déploiement et l’envoi de messages des entités, nous allons créer un indicateur de fonctionnalité appelé `show_loyalty_program`. Pour notre première version progressive, nous allons laisser Canvas contrôler quand et pour qui l’indicateur de fonctionnalité est activé. Pour l’instant, nous allons laisser le pourcentage de déploiement à 0 % et ne sélectionner aucun segment cible.

![Indicateur de fonctionnalité portant le nom de Programme de fidélité. L'ID est show_loyalty_program, et la description indique que ce programme affiche le nouveau programme de fidélisation sur l'écran d'accueil et la page de profil.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

Ensuite, dans Canvas Flow, nous allons créer une [étape d’indicateur de fonctionnalité]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) qui permet l’indicateur de fonctionnalité `show_loyalty_program` pour notre segment « Clients à valeur élevée » :

![Exemple d'un canvas avec une étape du découpage de l'audience où le segment des clients à forte valeur ajoutée active la fonctionnalité show_loyalty_program.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

Maintenant, les utilisateurs de ce segment vont commencer à voir le nouveau programme de fidélisation, et après son activation, un e-mail et une enquête seront envoyés automatiquement pour aider notre équipe à recueillir des commentaires.

### Expérimentation des fonctionnalités

Utilisez des indicateurs de caractéristiques pour expérimenter et confirmer vos hypothèses autour de votre nouvelle fonctionnalité. En répartissant le trafic en deux groupes ou plus, vous pouvez comparer l’impact d’un indicateur d’entité entre les groupes et déterminer le meilleur plan d’action en fonction des résultats.

Un [test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) est un outil puissant qui permet de comparer les réponses des utilisateurs à plusieurs versions d'une variable.

Dans cet exemple, notre équipe a créé un nouveau flux de paiement pour notre application de commerce électronique. Même si nous sommes convaincus que c’est une amélioration de l’expérience utilisateur, nous souhaitons exécuter un test A/B afin de mesurer son impact sur le chiffre d’affaires de notre application.

Pour commencer, nous allons créer un nouvel indicateur de fonctionnalité appelé `enable_checkout_v2`. Nous n’ajouterons pas d'audience ou de pourcentage de déploiement. Au lieu de cela, nous utiliserons une expérience d’indicateur de fonctionnalité pour diviser le trafic, activer la fonctionnalité et mesurer le résultat.

Dans notre application, nous vérifierons si l’indicateur de fonctionnalité est activé ou non et en annulant le flux de paiement en fonction de la réponse :

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
{% endtabs %}

Nous mettrons en place notre test A/B dans le cadre d'une [expérience d’indicateur de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/experiments/).

Désormais, 50 % des utilisateurs verront l'ancienne expérience, tandis que les 50 % restants verront la nouvelle expérience. Nous pouvons ensuite analyser les deux variantes pour déterminer quel flux de paiement a permis d'obtenir un taux de conversion plus élevé. {% multi_lang_include metrics.md metric='Conversion Rate' %}

![Une expérience d’indicateur de fonctionnalité divisant le trafic en deux groupes de 50 %.]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

Une fois que nous aurons déterminé le gagnant, nous pourrons arrêter cette campagne et augmenter le pourcentage de déploiement de l’indicateur de fonctionnalité à 100 % pour tous les utilisateurs pendant que notre équipe d'ingénieurs codera en dur cette fonctionnalité dans la prochaine version de l'application.

### Segmentation

Utilisez le filtre **Indicateur de fonctionnalité** pour créer un segment ou cibler l'envoi de messages aux utilisateurs en fonction de l'activation ou non d'un indicateur de fonctionnalité. Par exemple, disons que nous avons un indicateur de fonctionnalité qui contrôle le contenu premium dans notre application. Nous pourrions créer un segment qui filtrerait les utilisateurs dont la fonctionnalité n'est pas activée, puis envoyer à ce segment un message les incitant à mettre leur compte à niveau pour pouvoir consulter le contenu premium.

![]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

Pour plus d'informations sur le filtrage sur les segments, voir [Créer un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

{% alert note %}
Pour éviter les segments récursifs, il n'est pas possible de créer un segment faisant référence à d'autres indicateurs de fonctionnalité.
{% endalert %}

## Limites du régime

Il s'agit des limitations d’indicateur de fonctionnalité pour les plans gratuits et payants.

| Fonctionnalité                                                                                                   | Version gratuite     | Version payante      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [Indicateurs de fonctionnalité active](#active-feature-flags)                                                                     | 10 par espace de travail | 110 par espace de travail |
| [Expériences de campagnes actives]({{site.baseurl}}/developer_guide/feature_flags/experiments/)          | 1 par espace de travail  | 100 par espace de travail |
| [Étapes du canvas pour l’indicateur de fonctionnalité]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) | Illimité        | Illimité         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Un indicateur de fonctionnalité est considéré comme actif et sera pris en compte dans votre limite si l'une des conditions suivantes est remplie :

- Le taux de déploiement est supérieur à 0 %.
- Utilisé dans un Canvas actif
- Utilisé dans le cadre d'une expérience active

Même si le même indicateur de fonctionnalité répond à plusieurs critères, par exemple s'il est utilisé dans un Canvas et que le déploiement est de 50 %, il ne comptera que pour un seul indicateur de fonctionnalité actif dans votre limite.

{% alert note %}
Pour acheter la version payante des indicateurs de fonctionnalités, contactez votre gestionnaire de compte Braze ou demandez une mise à niveau dans le tableau de bord de Braze.
{% endalert %}
