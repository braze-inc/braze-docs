---
nav_title: Création d’indicateurs de fonctionnalité
article_title: Création d’indicateurs de fonctionnalité
page_order: 2
description: "Cet article de référence explique comment créer des indicateurs de fonctionnalité pour coordonner les déploiements de nouvelles fonctionnalités."
platform:
  - iOS
  - Android
  - Web

---

# Création d’indicateurs de fonctionnalité

> Cet article décrit comment créer et mettre en œuvre des indicateurs de fonctionnalité. Si vous désirez en apprendre plus concernant les indicateurs de fonctionnalité et leur utilisation dans Braze, consultez la section [About feature flags (À propos des indicateurs de fonctionnalité)][5] avant de continuer.

Les indicateurs de fonctionnalité vous permettent d’activer ou de désactiver à distance la fonctionnalité d’une sélection d’utilisateurs. Créez un indicateur de fonctionnalité dans le tableau de bord de Braze. Donnez un nom et un `ID`, un public cible et un pourcentage d’utilisateurs pour lesquels vous pouvez activer cette fonction. Ensuite, en utilisant `ID` dans votre application ou le code du site Internet, vous pouvez exécuter certaines parties de votre logique commerciale.

{% alert important %} 
Les indicateurs de fonctionnalité sont actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé. 
{% endalert %}

## Conditions préalables

Pour utiliser des indicateurs de fonctionnalité, assurez-vous que vos SDK sont à jour avec au moins ces versions minimales :

{% sdk_min_versions android:24.2.0 web:4.6.0 swift:5.9.0 %}

## Mettre en œuvre des indicateurs de fonctionnalité dans le tableau de bord
Créer, modifier et archiver des indicateurs de fonctionnalité sur la page **Feature Flags (Indicateurs de fonctionnalité)**, située sous **Engagement (Engagement)**. Cette page affiche une liste des indicateurs de fonctionnalité existants pour ce groupe d’apps.

![Une liste des indicateurs de fonctionnalité créés précédemment sur le tableau de bord de Braze][1]{: style="max-width:75%"}

### Créer un nouvel indicateur de fonctionnalité
Pour créer un indicateur de fonctionnalité, cliquez sur le bouton **Create Feature Flag (Créer un indicateur de fonctionnalité)**. Définissez ensuite les [details (détails)](#details), [properties (propriétés)](#properties), [user targeting (ciblage des utilisateurs)](#targeting), et [rollout traffic (trafic de déploiement)](#rollout-traffic).

![Un formulaire d’indicateur de fonctionnalité vierge][2]{: style="float:right;max-width:55%;margin-left:15px;"}

#### Détails
Donnez à votre nouvel indicateur de fonctionnalité un **Name (Nom)** et **ID (Identifiant)**. 
* Le **Name (Nom)** vous permet de fournir un titre pouvant être lu par un humain pour cet indicateur de fonctionnalité qui sera utilisé par les marketeurs et les administrateurs. 
* Le **ID (Identifiant)** sera référencé dans votre code pour déterminer si la fonctionnalité est activée pour un utilisateur particulier. Il doit être unique et ne peut pas être modifié une fois créé.
* Le champ **Description** est facultatif, il vous permet de fournir un contexte supplémentaire autour de cet indicateur de fonctionnalité.

Choisissez un `ID` de manière réfléchie, car il sera utilisé lorsque vous développez votre fonctionnalité. Mettez en pratique des conventions de dénomination pour vous assurer que votre code est lisible par vos collègues (et votre futur).

Par exemple, il est fréquent d’utiliser une convention de dénomination de `{verb}_{product}_{feature}`, comme `enable_rider_new_profile_page` pour effacer ce qui permet d’activer l’indicateur de fonctionnalité.

{% alert important %} 
Pour éviter le comportement de l’application de production de rupture, l’indicateur de fonctionnalité `ID` doit être unique et ne peut pas être modifié une fois créé. 

Les indicateurs de fonctionnalité sont partagés entre les applications au sein d’un groupe d’apps afin que différentes plateformes (iOS/Android/Web) puissent partager des références avec la même fonctionnalité.
{% endalert %}

#### Propriétés
Les propriétés personnalisées peuvent être définies comme faisant partie de votre indicateur de fonctionnalité. Ces propriétés seront accessibles par votre application via le SDK Braze lorsque la fonctionnalité est activée. Définir des propriétés est une étape facultative.

Les variables peuvent être des **chaînes de caractères**, des valeurs **booléennes** ou des **chiffres**. Définissez la clé variable et la valeur par défaut pour chaque propriété.

##### Exemples de propriétés
Par exemple, si nous définissons un indicateur de fonctionnalité qui montre une bannière hors stock pour notre magasin de commerce électronique, nous pouvons définir les propriétés suivantes que notre application utilisera lors de l’affichage de la bannière :

|Nom de la propriété|Type|Valeur|
|--|--|--|
|`banner_height`|`number`|`75`|
|`banner_color`|`string`|`blue`|
|`banner_text`|`string`|`Widgets are out of stock until July 1.`|
|`dismissible`|`boolean`|`false`|

{% alert tip %}
Il n’y a pas de limite au nombre de propriétés que vous pouvez ajouter, bien que les propriétés d’un indicateur d’entité soient limitées à 10 Ko au total.
{% endalert %}

#### Ciblage
Pour commencer le déploiement d’un indicateur de fonctionnalité, vous devez choisir un [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) des utilisateurs.

Utilisez le menu déroulant **Add Filter (Ajouter un filtre)** pour filtrer les utilisateurs hors de votre public cible. Ajoutez plusieurs filtres pour affiner votre audience.

![Deux menus déroulants. Le premier indique les utilisateurs cibles par segment. Le second indique les filtres supplémentaires.][3]

#### Trafic de déploiement
Les indicateurs de fonctionnalité commencent toujours comme désactivés pour vous permettre de séparer le calendrier de la libération et de l’activation de l’entité dans l’expérience de vos utilisateurs. 

Lorsque vous êtes prêt à déployer votre nouvelle fonction, spécifiez un public, puis utilisez **Trafic de déploiement** pour définir le pourcentage aléatoire de votre base utilisateur ciblée pour recevoir la nouvelle fonctionnalité. Définir le **Trafic de déploiement** pour définir un pourcentage entre 0 % (pas d’utilisateurs) et 100 % (l’ensemble du public cible). 

![Un curseur intitulé Le trafic de déploiement, couvrant entre 0 et 100.][4]

{% alert tip %} 
Ne définissez pas votre trafic de déploiement au-dessus de 0 % jusqu’à ce que vous soyez prêt à lancer votre nouvelle fonctionnalité. Lorsque vous définissez initialement votre indicateur de fonctionnalité dans le tableau de bord, laissez ce paramètre à 0 %.
{% endalert %}

## Mettre en œuvre l’indicateur de fonctionnalité dans votre application
Une fois que vous avez défini votre indicateur de fonctionnalité, configurez votre application ou site pour vérifier si elle est activée ou non pour un utilisateur particulier. Lorsqu’il est activé, vous allez définir une action ou référencer les propriétés variables de l’indicateur d’entité en fonction de votre cas d’utilisation. Le SDK Braze fournit des méthodes de gestion de l’état de l’indicateur de fonctionnalité et de ses propriétés dans votre application. 

Les indicateurs de fonctionnalité sont actualisés automatiquement au début de la session afin que vous puissiez afficher la version la plus récente de votre fonction au moment du lancement. Le SDK cache ces valeurs afin qu’elles puissent être utilisées hors ligne. 

Imaginons que vous deviez déployer un nouveau type de profil utilisateur pour votre application. Vous pouvez définir `ID` comme `expanded_user_profile`. Ensuite, votre application vérifie si elle doit afficher ce nouveau profil utilisateur à un utilisateur particulier. Par exemple :

{% tabs %}
{% tab Javascript %}
```javascript
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```
{% endtab %}
{% tab Swift %}
```swift
let featureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")
if featureFlag.enabled {
  print("expanded_user_profile is enabled")
} else {
  print("expanded_user_profile is not enabled")
}
```
{% endtab %}
{% tab Java %}
```java
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag.getEnabled()) {
  Log.i(TAG, "expanded_user_profile is enabled");
} else {
  Log.i(TAG, "expanded_user_profile is not enabled");
}
```
{% endtab %}
{% tab Kotlin %}
```kotlin
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
if (featureFlag.enabled) {
  Log.i(TAG, "expanded_user_profile is enabled.")
} else {
  Log.i(TAG, "expanded_user_profile is not enabled.")
}
```
{% endtab %}
{% endtabs %}

### Accès aux propriétés {#accessing-properties}

Pour accéder aux propriétés d’un indicateur de fonctionnalité, utilisez l’une des méthodes suivantes en fonction du type que vous avez défini dans le tableau de bord.

Si un indicateur de fonctionnalité n’est pas activé, ou si une propriété que vous référencez n’existe pas, ces méthodes reviendront `null`.

{% tabs %}
{% tab Javascript %}
```javascript
// feature flag instance
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
// string properties
const stringProperty = featureFlag.getStringProperty("color");
// boolean properties
const booleanProperty = featureFlag.getBooleanProperty("expanded");
// number properties
const numberProperty = featureFlag.getNumberProperty("height");
```
{% endtab %}
{% tab Swift %}
```swift
// feature flag instance
let featureFlag: FeatureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")
// string properties
let stringProperty: String? = featureFlag.stringProperty(key: "color")
// boolean properties
let booleanProperty: Bool? = featureFlag.boolProperty(key: "expanded")
// number properties
let numberProperty: Double? = featureFlag.numberProperty(key: "height")
```
{% endtab %}
{% tab Java %}
```java
// feature flag instance
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
// string properties
String stringProperty = featureFlag.getStringProperty("color");
// boolean properties
Boolean booleanProperty = featureFlag.getBooleanProperty("expanded");
// number properties
Number numberProperty = featureFlag.getNumberProperty("height");
```
{% endtab %}
{% tab Kotlin %}
```kotlin
// feature flag instance
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
// string properties
val stringProperty = featureFlag.getStringProperty("color")
// boolean properties
val booleanProperty = featureFlag.getBooleanProperty("expanded")
// number properties
val numberProperty = featureFlag.getNumberProperty("height")
```
{% endtab %}
{% endtabs %}

Vous pouvez également obtenir une liste de tous les indicateurs de fonctionnalité activés :

{% tabs %}
{% tab Javascript %}
```javascript
const features = getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```
{% endtab %}
{% tab Swift %}
```swift
let features = braze.featureFlags.featureFlags
for let feature in features {
  print("Feature: \(feature.id)", feature.enabled)
}
```
{% endtab %}
{% tab Java %}
```java
List<FeatureFlag> features = braze.getAllFeatureFlags();
for (FeatureFlag feature: features) {
  Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
}
```
{% endtab %}
{% tab Kotlin %}
```kotlin
val featureFlags = braze.getAllFeatureFlags()
featureFlags.forEach { feature ->
  Log.i(TAG, "Feature: ${feature.id} ${feature.enabled}")
}
```
{% endtab %}
{% endtabs %}

### Actualiser les indicateurs de fonctionnalité {#refreshing}
Vous pouvez actualiser la mi-session de l’utilisateur actuel pour extraire les dernières valeurs de Braze.

{% alert tip %}
L’actualisation se produit automatiquement au début de la session. Vous n’avez besoin que d’une actualisation avant d’effectuer des actions importantes, comme avant de charger une page de paiement, ou si vous savez qu’un indicateur de fonctionnalité sera référencé.
{% endalert %}

{% tabs %}
{% tab Javascript %}
```javascript
braze.refreshFeatureFlags(() => {
  console.log(`Feature flags have been refreshed.`);
}, () => {
  console.log(`Failed to refresh feature flags.`);
});
```
{% endtab %}
{% tab Swift %}
```swift
braze.featureFlags.requestRefresh { result in
  switch result {
  case .success(let features):
    print("Feature flags have been refreshed:", features)
  case .failure(let error):
    print("Failed to refresh feature flags:", error)
  }
}
```
{% endtab %}
{% tab Java %}
```java
braze.refreshFeatureFlags();
```
{% endtab %}
{% tab Kotlin %}
```kotlin
braze.refreshFeatureFlags()
```
{% endtab %}
{% endtabs %}


### Écouter les changements {#updates}
Vous pouvez configurer le SDK Braze pour écouter et mettre à jour votre application lorsque les indicateurs de fonctionnalité ont été actualisés.

Cela est utile si vous souhaitez mettre à jour votre application si un utilisateur n’est plus admissible à une entité. Par exemple, en définissant un état dans votre application, en fonction de l’activation ou non d’une fonctionnalité ou de l’une de ses valeurs de propriété.

{% tabs %}
{% tab Javascript %}
```javascript
// register an event listener
const subscriptionId = braze.subscribeToFeatureFlagsUpdates((features) => {
  console.log(`Features were updated`, features);
});
// unregister this event listener
braze.removeSubscription(subscriptionId);
```
{% endtab %}
{% tab Swift %}
```swift
// Create the feature flags subscription
// - You must keep a strong reference to the subscription to keep it active
let subscription = braze.featureFlags.subscribeToUpdates { features in
  print("Feature flags were updated:", features)
}
// Cancel the subscription
subscription.cancel()
```
{% endtab %}
{% tab Java %}
```java
braze.subscribeToFeatureFlagsUpdates(event -> {
  Log.i(TAG, "Feature flags were updated.");
  for (FeatureFlag feature: event.getFeatureFlags()) {
    Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
  }
});
```
{% endtab %}
{% tab Kotlin %}
```kotlin
braze.subscribeToFeatureFlagsUpdates() { event ->
  Log.i(TAG, "Feature flags were updated.")
  event.featureFlags.forEach { feature ->
    Log.i(TAG, "Feature: ${feature.id}")
  }
}
```
{% endtab %}
{% endtabs %}


[1]: {% image_buster /assets/img/feature_flags/feature-flags-list.png %} 
[2]: {% image_buster /assets/img/feature_flags/feature-flags-create.png %}
[3]: {% image_buster /assets/img/feature_flags/feature-flags-targeting.png %}
[4]: {% image_buster /assets/img/feature_flags/feature-flags-rollout.png %}
[5]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/about/
