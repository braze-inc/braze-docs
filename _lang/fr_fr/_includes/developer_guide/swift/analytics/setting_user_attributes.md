{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Attributs par défaut de l’utilisateur

### Attributs pris en charge

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

### Définition des attributs par défaut

Pour définir un attribut par défaut de l'utilisateur, définissez le champ approprié sur l'objet partagé `Braze.User`. Voici un exemple de définition de l’attribut de nom :

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "Alex")
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:@"Alex"];
```

{% endtab %}
{% endtabs %}

### Désactivation des attributs par défaut

Pour désactiver un attribut par défaut de l'utilisateur, passez `nil` à la méthode correspondante.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: nil)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:nil];
```

{% endtab %}
{% endtabs %}

## Attributs utilisateur personnalisés

Outre les attributs par défaut, Braze vous permet de définir des attributs personnalisés à l'aide de différents types de données. Pour plus d'informations sur l'option de segmentation de chaque attribut, voir [Collecte de données sur les utilisateurs]({{site.baseurl}}/developer_guide/analytics/).

{% alert important %}
Les valeurs d’attribut personnalisé ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées. Pour plus d'informations, reportez-vous à [`Braze.User`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class).
{% endalert %}

### Définition des attributs personnalisés

{% tabs local %}
{% tab chaîne de caractères %}
Pour définir un attribut personnalisé avec une valeur `string`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab entier %}
Pour définir un attribut personnalisé avec une valeur `integer`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab points flottants %}
Braze traite les valeurs `float` et `double` de la même manière dans notre base de données. Pour définir un attribut personnalisé avec une valeur double :

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab booléen %}
Pour définir un attribut personnalisé avec une valeur `boolean`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab date %}
Pour définir un attribut personnalisé avec une valeur `date`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab réseau %}
Le nombre maximum d'éléments dans les [tableaux d'attributs personnalisés]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays) est par défaut de 25. Les tableaux dépassant le nombre maximum d’éléments seront tronqués pour contenir le nombre maximum d’éléments. Le maximum pour les tableaux individuels peut être augmenté jusqu’à 100. Si vous souhaitez que cette limite soit augmentée, contactez votre gestionnaire de services clients.

Pour définir un attribut personnalisé avec une valeur `array`:

{% subtabs %}
{% subtab swift %}
```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```
{% endsubtab %}

{% subtab objective-c %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Incrémentation ou décrémentation des attributs personnalisés

Ce code est un exemple d’incrémentation d’un attribut personnalisé. Vous pouvez incrémenter la valeur d'un attribut personnalisé de n'importe quelle valeur `integer` ou `long`:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### Désactivation des attributs personnalisés

{% tabs %}
{% tab swift %}
Pour désactiver un attribut personnalisé, transmettez la clé de l'attribut concerné à la méthode `unsetCustomAttribute`.

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab objective-c %}
Pour désactiver un attribut personnalisé, transmettez la clé de l'attribut concerné à la méthode `unsetCustomAttributeWithKey`.

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### Imbrication d'attributs personnalisés

Vous pouvez également imbriquer des propriétés dans des attributs personnalisés. Dans l'exemple suivant, un objet `favorite_book` avec des propriétés imbriquées est défini comme un attribut personnalisé sur le profil utilisateur. Pour plus de détails, reportez-vous à la section [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

{% tabs %}
{% tab swift %}
```swift
let favoriteBook: [String: Any?] = [
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
]

braze.user.setCustomAttribute(key: "favorite_book", dictionary: favoriteBook)
```
{% endtab %}

{% tab objective-c %}
```objc
NSDictionary *favoriteBook = @{
  @"title": @"The Hobbit",
  @"author": @"J.R.R. Tolkien",
  @"publishing_date": @"1937"
};

[AppDelegate.braze.user setCustomAttributeWithKey:@"favorite_book" dictionary:favoriteBook];
```
{% endtab %}
{% endtabs %}

### Utiliser l'API REST

Vous pouvez également utiliser notre API REST pour définir ou désactiver les attributs des utilisateurs. Pour plus d'informations, reportez-vous aux [Endpoints de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configurer les abonnements des utilisateurs

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
{% tab objective-c %}

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
{% tab objective-c %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

Reportez-vous à [Gérer les inscriptions des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) pour plus de détails.
