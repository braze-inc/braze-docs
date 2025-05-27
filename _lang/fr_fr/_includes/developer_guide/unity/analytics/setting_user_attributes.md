{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Attributs par défaut de l’utilisateur

Pour définir les attributs de l'utilisateur, vous devez appeler la méthode appropriée sur l'objet `BrazeBinding`. Voici une liste d’attributs intégrés qui peuvent être appelés à l’aide de cette méthode.

| Attribut                 | Exemple de code |
|---------------------------|-------------|
| Prénom                | `AppboyBinding.SetUserFirstName("first name");` |
| Nom                 | `AppboyBinding.SetUserLastName("last name");` |
| Adresse e-mail de l’utilisateur                | `AppboyBinding.SetUserEmail("email@email.com");` |
| Sexe                    | `AppboyBinding.SetUserGender(Appboy.Models.Gender);` |
| Date de naissance                | `AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");` |
| Pays de l’utilisateur              | `AppboyBinding.SetUserCountry("country name");` |
| Ville de résidence de l’utilisateur            | `AppboyBinding.SetUserHomeCity("city name");` |
| Abonnement de l’utilisateur aux e-mails   | `AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);` |
| Abonnement de l’utilisateur aux notifications push    | `AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);` |
| Numéro de téléphone de l’utilisateur         | `AppboyBinding.SetUserPhoneNumber("phone number");` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Attributs utilisateur personnalisés

Outre les attributs par défaut, Braze vous permet de définir des attributs personnalisés à l'aide de différents types de données. Pour plus d'informations sur l'option de segmentation de chaque attribut, voir [Collecte de données sur les utilisateurs]({{site.baseurl}}/developer_guide/analytics).

### Définition des attributs personnalisés

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

Pour désactiver un attribut personnalisé d'un utilisateur, utilisez la méthode suivante :

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
