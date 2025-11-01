{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Attributs par défaut de l’utilisateur

### Méthodes prédéfinies

Braze propose des méthodes prédéfinies pour définir les attributs utilisateur suivants à l'aide de l'objet `BrazeBinding`. Pour plus d'informations, consultez le [fichier de déclaration de Braze Unity](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs).

- Prénom
- Nom
- Adresse e-mail de l’utilisateur
- Genre
- Date de naissance
- Pays de l’utilisateur
- Ville de résidence de l’utilisateur
- Abonnement de l’utilisateur aux e-mails
- Abonnement de l’utilisateur aux notifications push
- Numéro de téléphone de l’utilisateur

### Définition des attributs par défaut

Pour définir un attribut par défaut, appelez la méthode correspondante sur l'objet `BrazeBinding`.

{% tabs local %}
{% tab Prénom %}
```csharp
BrazeBinding.SetUserFirstName("first name");
```
{% endtab %}
{% tab Nom de famille %}
```csharp
BrazeBinding.SetUserLastName("last name");
```
{% endtab %}
{% tab E-mail %}
```csharp
BrazeBinding.SetUserEmail("email@email.com");
```
{% endtab %}
{% tab Genre %}
```csharp
BrazeBinding.SetUserGender(Appboy.Models.Gender);
```
{% endtab %}
{% tab Date de naissance %}
```csharp
BrazeBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");
```
{% endtab %}
{% tab Pays %}
```csharp
BrazeBinding.SetUserCountry("country name");
```
{% endtab %}
{% tab Ville d'origine %}
```csharp
BrazeBinding.SetUserHomeCity("city name");
```
{% endtab %}
{% tab Abonnement à l'e-mail %}
```csharp
BrazeBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Abonnement poussé %}
```csharp
BrazeBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Numéro de téléphone %}
```csharp
BrazeBinding.SetUserPhoneNumber("phone number");
```
{% endtab %}
{% endtabs %}

### Désactivation des attributs par défaut

Pour désactiver un attribut par défaut de l'utilisateur, passez `null` à la méthode correspondante.

```csharp
BrazeBinding.SetUserFirstName(null);
```

## Attributs utilisateur personnalisés

Outre les attributs par défaut, Braze vous permet de définir des attributs personnalisés à l'aide de différents types de données. Pour plus d'informations sur l'option de segmentation de chaque attribut, voir [Collecte de données sur les utilisateurs]({{site.baseurl}}/developer_guide/analytics).

### Définition des attributs personnalisés

Pour définir un attribut personnalisé, utilisez la méthode correspondant au type d'attribut : 

{% tabs %}
{% tab Chaîne de caractères %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}

{% tab Entier %}

```csharp
// Set Integer Attribute
AppboyBinding.SetCustomUserAttribute("custom int attribute key", 'integer value');
// Increment Integer Attribute
AppboyBinding.IncrementCustomUserAttribute("key", increment(int))
```
{% endtab %}

{% tab Double %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom double attribute key", 'double value');
```

{% endtab %}

{% tab Booléen %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
```
{% endtab %}

{% tab Date %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

{% alert note %}
Les dates transmises à Braze doivent être au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (par exemple `2013-07-16T19:20:30+01:00`) ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (par exemple`2016-12-14T13:32:31.601-0800`).
{% endalert %}

{% endtab %}

{% tab Réseau %}

```csharp
// Setting An Array
AppboyBinding.SetCustomUserAttributeArray("key", array(List), sizeOfTheArray(int))
// Adding to an Array
AppboyBinding.AddToCustomUserAttributeArray("key", "Attribute")
// Removing an item from an Array
AppboyBinding.RemoveFromCustomUserAttributeArray("key", "Attribute")
```
{% endtab %}
{% endtabs %}

{% alert important %}
Les valeurs d’attribut personnalisé ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.
{% endalert %}

### Désactivation des attributs personnalisés

Pour désactiver un attribut personnalisé, transmettez la clé de l'attribut concerné à la méthode `UnsetCustomUserAttribute`. 

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### Utiliser l'API REST

Vous pouvez également utiliser notre API REST pour définir ou désactiver les attributs des utilisateurs. Pour plus d'informations, reportez-vous aux [Endpoints de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configurer les abonnements des utilisateurs

Pour configurer un abonnement e-mail ou push pour vos utilisateurs, appelez l'une des fonctions suivantes.

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

Les deux fonctions prennent comme argument `Appboy.Models.AppboyNotificationSubscriptionType`, qui a trois états différents :

| Statut de l'abonnement | Définition |
| ------------------- | ---------- |
| `OPTED_IN` | Inscrit et explicitement abonné |
| `SUBSCRIBED` | Inscrit et pas explicitement abonné |
| `UNSUBSCRIBED` | Désinscrit ou explicitement désabonné |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Aucun abonnement explicite n’est requis par Windows pour envoyer des notifications push aux utilisateurs. Lorsqu’un utilisateur est enregistré pour les notifications push, il est défini sur `SUBSCRIBED` plutôt que `OPTED_IN` par défaut. Pour en savoir plus, consultez notre documentation sur [l’implémentation des souscriptions et des abonnements explicites]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).
{% endalert %}

| Type d'abonnement                        | Description |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType`      | Les utilisateurs seront définis sur `SUBSCRIBED` automatiquement à la réception d’une adresse e-mail valide. Cependant, nous vous suggérons d’établir un processus d’abonnement explicite et de définir cette valeur sur `OPTED_IN` dès réception du consentement explicite de votre utilisateur. Pour plus de détails, consultez notre documentation [Modification des souscriptions utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions). |
| `PushNotificationSubscriptionType`       | Les utilisateurs seront définis sur `SUBSCRIBED` automatiquement après une inscription aux notifications push valide. Cependant, nous vous suggérons d’établir un processus d’abonnement explicite et de définir cette valeur sur `OPTED_IN` dès réception du consentement explicite de votre utilisateur. Pour plus de détails, consultez notre documentation [Modification des souscriptions utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Ces types tombent dans la catégorie `Appboy.Models.AppboyNotificationSubscriptionType`.
{% endalert %}

### Définir des inscriptions par e-mail

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Définition des abonnements par notification push

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```
