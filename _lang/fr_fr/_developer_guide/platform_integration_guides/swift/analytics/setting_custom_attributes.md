---
nav_title: Définition des attributs personnalisés
article_title: Définition des attributs personnalisés pour iOS
platform: Swift
page_order: 3
description: "Cet article de référence montre comment définir des attributs personnalisés pour le SDK Swift."

---

# Définition des attributs personnalisés

> Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

Avant la mise en œuvre, assurez-vous de consulter des exemples des options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [meilleures pratiques]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), ainsi que nos notes sur les [conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Affecter des attributs utilisateur par défaut

Pour attribuer des attributs utilisateur, vous devez définir le champ approprié sur les objets `ABKUser` partagés.

Voici un exemple de définition de l’attribut de nom :

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "first_name")
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze.user setFirstName:@"first_name"];
```

{% endtab %}
{% endtabs %}

Les attributs suivants doivent être définis sur l’objet `Braze.User` :

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `gender`

## Affecter des attributs utilisateur personnalisés

En plus des attributs utilisateur par défaut, Braze vous permet également de définir des attributs personnalisés en utilisant plusieurs types de données différents. Consultez notre [collecte de données utilisateur]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/) pour plus d'informations sur les options de segmentation que chacun de ces attributs vous offrira.

### Attribut personnalisé avec une valeur de chaîne de caractères

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur de nombre entier

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur double

Braze traite les valeurs `float` et `double` de la même manière dans notre base de données.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur booléenne

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur de date

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur de tableau

Le nombre maximum d'éléments dans les [tableaux d'attributs personnalisés]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays) est par défaut de 25. Les tableaux dépassant le nombre maximum d’éléments seront tronqués pour contenir le nombre maximum d’éléments. Le maximum pour les tableaux individuels peut être augmenté jusqu’à 100. Si vous souhaitez que cette limite soit augmentée, contactez votre gestionnaire de services clients. 


{% tabs %}
{% tab swift %}

```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
// Setting a custom attribute with an array value
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[AppDelegate.braze.user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[AppDelegate.braze.user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% endtabs %}

### Enlever la configuration d’un attribut personnalisé

Les attributs personnalisés peuvent également être annulés à l’aide de la méthode suivante :

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### Incrémenter ou décrémenter les attributs personnalisés

Ce code est un exemple d’incrémentation d’un attribut personnalisé. Vous pouvez incrémenter la valeur d’un attribut personnalisé avec n’importe quel entier positif ou négatif ou valeur longue :

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### Définir un attribut personnalisé via l’API REST

Vous pouvez également utiliser notre API REST pour définir les attributs utilisateur. Reportez-vous à la [Documentation de l'API utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) pour plus de détails.

### Limites de valeur d’attribut personnalisé

Les valeurs d’attribut personnalisé ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.

#### Informations supplémentaires

- Reportez-vous à la [documentation `Braze.User`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class) pour plus d'informations.

## Configuration des abonnements utilisateur

Pour configurer un abonnement pour vos utilisateurs (par e-mail ou notification push), appelez les fonctions `set(emailSubscriptionState:)` ou `set(pushNotificationSubscriptionState:)`, respectivement. Ces deux fonctions considèrent le type de enum `Braze.User.SubscriptionState` comme arguments. Ce type a trois états différents :

| Statut d’abonnement | Définition |
| ------------------- | ---------- |
| `optedIn` | Inscrit et explicitement abonné |
| `subscribed` | Inscrit et pas explicitement abonné |
| `unsubscribed` | Désinscrit ou explicitement désabonné |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les utilisateurs qui autorisent une application à leur envoyer des notifications push ont par défaut le statut `optedIn`, car iOS nécessite un abonnement explicite.

Les utilisateurs seront automatiquement définis sur `subscribed` dès la réception d’une adresse e-mail valide ; cependant, nous vous suggérons d’établir un processus d’abonnement explicite et de définir cette valeur sur `optedIn` dès réception du consentement explicite de votre utilisateur. Reportez-vous à [Gérer les inscriptions des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) pour plus de détails.

### Définir des inscriptions par e-mail

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(emailSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze.user setEmailSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

### Définition des abonnements par notification push

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(pushNotificationSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

Reportez-vous à [Gérer les inscriptions des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) pour plus de détails.

