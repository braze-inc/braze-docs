---
nav_title: Expériences d’indicateurs de fonctionnalités
article_title: Expériences d’indicateurs de fonctionnalités
page_order: 40
description: "Les expériences d’indicateurs de fonctionnalités vous permettent d'effectuer des tests A/B sur les modifications apportées à vos applications afin d'optimiser les taux de conversion."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# Création d'une expérience de drapeau de fonctionnalité

> Les expériences d’indicateurs de fonctionnalités vous permettent d'effectuer des tests A/B sur les modifications apportées à vos applications afin d'optimiser les taux de conversion. Les marketeurs peuvent utiliser les feature flags pour déterminer si une nouvelle fonctionnalité a un impact positif ou négatif sur les taux de conversion, ou quel ensemble de propriétés de feature flags est le plus optimal.

## Conditions préalables

Avant de pouvoir suivre les données des utilisateurs dans l'expérience sur l'application, votre application doit enregistrer le moment où un utilisateur interagit avec un indicateur de fonctionnalité. C'est ce qu'on appelle l'impression d'un indicateur de fonctionnalité. Veillez à consigner l'impression d'un indicateur de fonctionnalité chaque fois qu'un utilisateur voit ou aurait pu voir la fonctionnalité que vous testez, même s'il fait partie du groupe de contrôle.

Pour en savoir plus sur l'enregistrement des impressions de drapeaux de fonctionnalité, reportez-vous à la section [Création de drapeaux de fonctionnalité]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#impressions).

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}

```

## Étape 1 : Créez une expérience

1. Allez dans **Messagerie** > **Campagnes** et cliquez sur **\+ Créer une campagne.**
2. Sélectionnez **Expérience d’indicateur de fonctionnalité**.
3. Donnez un nom clair et significatif à votre campagne.

## Étape 2 : Ajouter des variantes d'expérience

Ensuite, créez des variantes. Pour chaque variante, choisissez l'indicateur de fonctionnalité que vous souhaitez activer ou désactiver et examinez les propriétés attribuées.

Pour tester l'impact de votre fonctionnalité, utilisez des variantes pour diviser le trafic en deux groupes ou plus. Nommez un groupe "Mon groupe de contrôle" et désactivez ses drapeaux de fonctionnalité.

### Écrasement des propriétés

Bien que vous ayez spécifié des propriétés par défaut lors de la configuration initiale de votre indicateur de fonctionnalité, vous pouvez choisir d'écraser ces valeurs pour les utilisateurs qui reçoivent une variante de campagne spécifique.

![]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

Pour modifier, ajouter ou supprimer des propriétés par défaut supplémentaires, modifiez l'indicateur de fonctionnalité lui-même à partir de **Messagerie** > **Indicateurs de fonctionnalité**.

Lorsqu'une variante est désactivée, le SDK renvoie un objet de propriétés vide pour l'indicateur de fonctionnalité donné. 

## Étape 3 : Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) en choisissant des segments ou des filtres pour réduire votre audience. L'appartenance à un segment est calculée lorsque les indicateurs de fonctionnalité sont actualisés pour un utilisateur donné.

{% alert note %}
Les modifications sont mises à disposition après que votre application actualise les indicateurs de fonctionnalités, ou lorsqu'une nouvelle session est lancée.
{% endalert %}

## Étape 4 : Distribuer les variantes

Choisissez la distribution en pourcentage pour votre expérience. La meilleure pratique consiste à ne pas modifier la distribution après le lancement de l'expérience.

## Étape 5 : Attribuer des conversions

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), après avoir reçu une campagne. Spécifiez une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

## Étape 6 : Vérifier et lancer le test

Une fois que vous avez fini de créer la dernière partie de votre expérience, passez en revue ses détails, puis cliquez sur **Lancer l'expérience.**



