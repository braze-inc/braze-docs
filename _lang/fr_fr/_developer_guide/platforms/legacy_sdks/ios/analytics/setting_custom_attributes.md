---
nav_title: Définir des attributs personnalisés
article_title: Définir des attributs personnalisés pour iOS
platform: iOS
page_order: 3
description: "Cet article de référence montre comment définir des attributs personnalisés dans votre application iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Définir des attributs personnalisés pour iOS

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez ensuite filtrer et segmenter vos utilisateurs en fonction de ces attributs depuis le tableau de bord.

Avant de procéder à l'implémentation, pensez à consulter les exemples d'options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [bonnes pratiques]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), ainsi que nos notes sur les [conventions de nommage des événements]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

## Affecter des attributs utilisateur par défaut

Pour attribuer des attributs utilisateur, vous devez définir le champ approprié sur l'objet partagé `ABKUser`.

Voici un exemple de définition de l'attribut de prénom :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].user.firstName = @"first_name";
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.firstName = "first_name"
```

{% endtab %}
{% endtabs %}

Les attributs suivants doivent être définis sur l'objet `ABKUser` :

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `userID`
- `gender`

## Affecter des attributs utilisateur personnalisés

Au-delà des attributs utilisateur par défaut, Braze vous permet de définir des attributs personnalisés avec plusieurs types de données. Consultez notre documentation sur la [collecte de données utilisateur]({{site.baseurl}}/developer_guide/analytics/) pour en savoir plus sur les options de segmentation offertes par chacun de ces attributs.

### Attribut personnalisé avec une valeur de chaîne de caractères

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andStringValue:"your_attribute_value"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andStringValue: "your_attribute_value")
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur entière

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andIntegerValue: yourIntegerValue)
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur double

Braze traite les valeurs `float` et `double` de la même manière dans sa base de données.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDoubleValue: yourDoubleValue)
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur booléenne

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andBOOLValue: yourBoolValue)
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur de date

Les dates transmises à Braze avec cette méthode doivent être au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (par ex. `2013-07-16T19:20:30+01:00`) ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (`2016-12-14T13:32:31.601-0800`).

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDateValue:yourDateValue)
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur de tableau

Le nombre maximum d'éléments par défaut dans un tableau est de 500. Vous pouvez modifier le nombre maximum d'éléments dans le tableau de bord de Braze, sous **Data Settings** > **Custom Attributes**. Les tableaux dépassant le nombre maximum d'éléments sont tronqués pour ne conserver que le nombre maximum d'éléments.


{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Setting a custom attribute with an array value
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[[Appboy sharedInstance].user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% tab swift %}

```swift
// Setting a custom attribute with an array value
Appboy.sharedInstance()?.user.setCustomAttributeArrayWithKey("array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
Appboy.sharedInstance()?.user.addToCustomAttributeArrayWithKey("array_name", value: "value3")
// Removing a value from an array type custom attribute
Appboy.sharedInstance()?.user.removeFromCustomAttributeArrayWithKey("array_name", value: "value2")
```

{% endtab %}
{% endtabs %}

### Réinitialiser un attribut personnalisé

Il est également possible de réinitialiser un attribut personnalisé à l'aide de la méthode suivante :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.unsetCustomAttributeWithKey("your_attribute_key")
```

{% endtab %}
{% endtabs %}

### Incrémenter ou décrémenter des attributs personnalisés

Ce code illustre l'incrémentation d'un attribut personnalisé. Vous pouvez incrémenter la valeur d'un attribut personnalisé avec n'importe quel entier positif ou négatif, ou valeur longue :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.incrementCustomUserAttribute("your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% endtabs %}

### Définir un attribut personnalisé via l'API REST

Vous pouvez également utiliser notre API REST pour définir les attributs utilisateur. Reportez-vous à la [documentation de l'API utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) pour plus de détails.

### Limites de valeur des attributs personnalisés

Les valeurs d'attribut personnalisé ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.

#### Informations supplémentaires

- Vous trouverez plus de détails dans le fichier [`ABKUser.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).
- Reportez-vous à la [documentation `ABKUser`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html) pour plus d'informations.

## Configuration des abonnements utilisateur

Pour configurer un abonnement pour vos utilisateurs (par e-mail ou notification push), appelez respectivement les fonctions `setEmailNotificationSubscriptionType` ou `setPushNotificationSubscriptionType`. Ces deux fonctions prennent le type enum `ABKNotificationSubscriptionType` comme argument. Ce type comporte trois états :

| État de l'abonnement | Définition |
| ------------------- | ---------- |
| `ABKOptedin` | Abonné, avec consentement explicite |
| `ABKSubscribed` | Abonné, sans consentement explicite |
| `ABKUnsubscribed` | Désabonné ou refus explicite |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les utilisateurs qui autorisent une application à leur envoyer des notifications push ont par défaut le statut `ABKOptedin`, car iOS exige un consentement explicite.

Les utilisateurs sont automatiquement définis sur `ABKSubscribed` dès la réception d'une adresse e-mail valide. Nous vous recommandons toutefois de mettre en place un processus d'abonnement explicite et de définir cette valeur sur `OptedIn` dès réception du consentement explicite de votre utilisateur. Reportez-vous à [Gérer les abonnements des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) pour plus de détails.

### Définir les abonnements par e-mail

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setEmailNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setEmailNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

### Définir les abonnements aux notifications push

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setPushNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setPushNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

Reportez-vous à [Gérer les abonnements des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) pour plus de détails.