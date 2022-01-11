---
nav_title: Réglage des attributs personnalisés
article_title: Paramétrage des attributs personnalisés pour iOS
platform: iOS
page_order: 3
description: "Cet article de référence montre comment définir des attributs personnalisés dans votre application iOS."
---

# Définition des attributs personnalisés pour iOS

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. attributs personnalisés vs. achetez des événements dans notre section [Meilleures pratiques][1], ainsi que nos notes sur [les conventions de nommage d'événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Attribution des attributs par défaut de l'utilisateur

Pour assigner les attributs de l'utilisateur, vous devez définir le champ approprié sur l'objet partagé `ABKUser`.

Ce qui suit est un exemple de définition de l'attribut de prénom:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].user.firstName = @"prénom";
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.firstName = "prénom"
```

{% endtab %}
{% endtabs %}

Les attributs suivants doivent être définis sur l'objet `ABKUser`:

- `prénom`
- `Nom de famille`
- `Email`
- `date de naissance`
- `Pays`
- `Langue`
- `Ville natale`
- `Téléphone`
- `ID utilisateur`
- `twitterAccountIdentifier`
- `Sexe`

## Attribution d'attributs utilisateur personnalisés

Au-delà des attributs ci-dessus, Braze vous permet également de définir des attributs personnalisés en utilisant un certain nombre de types de données différents : Pour plus d'informations concernant les options de segmentation, chacun de ces attributs vous permettra, consultez notre documentation ["Meilleures pratiques"][1] dans cette section.

### Attribut personnalisé avec une valeur de chaîne

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"votre_attribute_key" andStringValue:"votre_attribute_valeur"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("votre_attribute_key", andStringValue: "votre_attribute_valeur")
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur entière

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"votre_attribute_key" andIntegerValue:votreIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("votre_attribute_key", andIntegerValue: yourIntegerValue)
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur double

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"votre_attribute_key" andDoubleValue:votreDoubleValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("votre_attribute_key", andDoubleValue: yourDoubleValue)
```

{% endtab %}
{% endtabs %}

> Braze traite `float` et `double` valeurs identiques dans notre base de données.

### Attribut personnalisé avec une valeur booléenne

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"votre_attribute_key" andBOOLValue:votreboOLValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("votre_attribute_key", andBOOLValue: yourBoolValue)
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé avec une valeur de date

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"votre_attribute_key" etDateValue:votreDateValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("votre_attribute_key", andDateValue:votreDateValue)
```

{% endtab %}
{% endtabs %}

> Les dates passées à Braze avec cette méthode doivent soit être au format [ISO 8601][2] , e. `2013-07-16T19:20:30+01:00` ou dans le `yyyy-MM-dd'T'H:mm:ss:SSSZ` format e.g `2016-12-14T13:32:31.601-0800`

### Attribut personnalisé avec une valeur de tableau
Le nombre maximum d'éléments dans les tableaux d'attributs personnalisés est par défaut de 25. Le maximum pour chaque tableau peut être augmenté jusqu'à 100. Si vous souhaitez augmenter ce maximum, veuillez contacter votre responsable du service à la clientèle. Les tableaux dépassant le nombre maximum d'éléments seront tronqués pour contenir le nombre maximum d'éléments. Pour plus d'informations sur les tableaux d'attributs personnalisés et leur comportement, consultez notre [documentation sur les tableaux][8].

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Définition d'un attribut personnalisé avec une valeur de tableau
[[Appboy sharedInstance]. ser setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1", @"value2"]];
// Ajouter à un attribut personnalisé avec une valeur de tableau
[[Appboy sharedInstance]. ser addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Supprimer une valeur d'un attribut personnalisé de type tableau
[[Appboy sharedInstance]. ser removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Suppression d'un tableau entier et d'une clé
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% tab swift %}

```swift
// Définition d'un attribut personnalisé avec une valeur de tableau
Appboy.sharedInstance()?.user. etCustomAttributeArrayWithKey("array_name", tableau: ["value1", "value2"])
// Ajoute à un attribut personnalisé avec une valeur tableau
Appboy. haredInstance()?.user.addToCustomAttributeArrayWithKey("array_name", value: "value3")
// Suppression d'une valeur d'un attribut personnalisé de type tableau
Appboy.sharedInstance()?.user.removeFromCustomAttributeArrayWithKey("array_name", valeur: "value2")
```

{% endtab %}
{% endtabs %}

### Annuler la définition d'un attribut personnalisé

Les attributs personnalisés peuvent également être supprimés en utilisant la méthode suivante :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user unsetCustomAttributeWithKey:@"votre_attribute_key"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.unsetCustomAttributeWithKey("votre_attribute_clé")
```

{% endtab %}
{% endtabs %}

### Incrément/décrémentation d'attributs personnalisés

Ce code est un exemple d'attribut personnalisé incrémenté. Vous pouvez incrémenter la valeur d'un attribut personnalisé par n'importe quel entier positif ou négatif ou par une valeur longue.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user incrementCustomUserAttribute:@"votre_attribute_key" par:incrementIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.incrementCustomUserAttribute("votre_attribute_key", par: incrementIntegerValue)
```

{% endtab %}
{% endtabs %}

### Définition d'un attribut personnalisé via l'API REST

Vous pouvez également utiliser notre API REST pour définir les attributs de l'utilisateur. Pour ce faire, reportez-vous à la [documentation de l'API utilisateur][3].

### Limites de valeur d'attribut personnalisé

Les valeurs d'attributs personnalisés ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.

#### Informations complémentaires

- Plus de détails peuvent être trouvés dans le fichier [`ABKUser.h`][5].
- En outre, vous pouvez vous référer à la [documentation ABKUser][6] pour plus d'informations.

## Mise en place des abonnements utilisateurs

Pour configurer un abonnement pour vos utilisateurs (e-mail ou push), appelez les fonctions `setEmailNotificationSubscriptionType` ou `setPushNotificationSubscriptionType`, respectivement. Les deux fonctions prennent le type enum `ABKNotificationSubscriptionType` comme arguments. Ce type a trois états différents :

| Statut de l'abonnement | Définition                                 |
| ---------------------- | ------------------------------------------ |
| `ABKOptedin`           | Abonné, et explicitement choisi dans       |
| `Abonné`               | Abonné, mais pas explicitement choisi dans |
| `ABKDésabonné`         | Désabonné et/ou explicitement désabonné    |
{: .reset-td-br-1 .reset-td-br-2}

Les utilisateurs qui accordent la permission à une application de leur envoyer des notifications push par défaut au statut de `ABKOptedin` car iOS nécessite un opt-in explicite.

> Les utilisateurs seront mis à `ABKSubscribed` automatiquement à la réception d'une adresse e-mail valide. Nous vous suggérons d'établir un processus d'opt-in explicite et de définir cette valeur à `OptedIn` sur réception du consentement explicite de votre utilisateur. [Consultez le Guide de l'utilisateur pour plus de détails][12].

### Paramétrage des abonnements aux emails

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

### Réglage des abonnements aux notifications push

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

Pour plus d'informations sur la mise en œuvre des abonnements, visitez notre page sur [la gestion des abonnements aux utilisateurs][10].

[1]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection

[1]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: http://en.wikipedia.org/wiki/ISO_8601
[3]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[5]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[6]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html
[8]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[12]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
