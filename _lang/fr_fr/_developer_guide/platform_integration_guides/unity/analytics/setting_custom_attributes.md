---
nav_title: Définition des attributs personnalisés
article_title: Définition des attributs personnalisés pour Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "Cet article de référence explique comment activer et désactiver les attributs personnalisés sur la plateforme Unity."

---

# Définition des attributs personnalisés

> Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

Avant la mise en œuvre, assurez-vous de consulter des exemples des options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [Meilleures pratiques][1].

## Affecter des attributs utilisateur par défaut

Pour attribuer des attributs utilisateur, vous devez appeler la méthode appropriée sur l’objet BrazeBinding. Voici une liste d’attributs intégrés qui peuvent être appelés à l’aide de cette méthode.

### Prénom
`AppboyBinding.SetUserFirstName("first name");`

### Nom
`AppboyBinding.SetUserLastName("last name");`

### Adresse e-mail de l’utilisateur
`AppboyBinding.SetUserEmail("email@email.com");`

>  Il est toujours utile de définir des adresses e-mail même si vous n’envoyez pas d’e-mails via Braze. Le courrier électronique facilite la recherche de profils d’utilisateurs individuels et la résolution des problèmes au fur et à mesure qu’ils surviennent.

### Genre
`AppboyBinding.SetUserGender(Appboy.Models.Gender);`

### Date de naissance
`AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");`

### Pays de l’utilisateur
`AppboyBinding.SetUserCountry("country name");`

### Ville de résidence de l’utilisateur
`AppboyBinding.SetUserHomeCity("city name");`

### Abonnement de l’utilisateur aux e-mails
`AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### Abonnement de l’utilisateur aux notifications push
`AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### Numéro de téléphone de l’utilisateur
`AppboyBinding.SetUserPhoneNumber("phone number");`

## Affecter des attributs utilisateur personnalisés

Au-delà des attributs utilisateur par défaut, Braze vous permet également de définir des attributs personnalisés en utilisant un certain nombre de types de données différents :
Pour plus d'informations concernant les options de segmentation que chacun de ces attributs vous offrira, consultez notre [documentation des "Meilleures Pratiques"][1] dans cette section.

### Définir des valeurs d’attributs personnalisés

{% tabs %}
{% tab Valeur booléenne %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
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
{% tab Chaîne de caractères %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}
{% tab Date %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

>  Les dates transmises à Braze doivent être soit au format [ISO 8601][2], e.g `2013-07-16T19:20:30+01:00` ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` e.g `2016-12-14T13:32:31.601-0800`

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
{% endtabs
%}
### Enlever la configuration d’un attribut personnalisé

Les attributs personnalisés peuvent également être annulés à l’aide de la méthode suivante :

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

## Définir un attribut personnalisé via l’API REST
Vous pouvez également utiliser notre API REST pour définir les attributs utilisateur. Pour ce faire, consultez la [documentation de l'API utilisateur][3].

## Limites de valeur d’attribut personnalisé
Les valeurs d’attribut personnalisé ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.

## Configuration des abonnements utilisateur

Pour configurer un abonnement pour vos utilisateurs (par e-mail ou notification push), appelez les fonctions     
`AppboyBinding.SetUserEmailNotificationSubscriptionType()` ou `AppboyBinding.SetPushNotificationSubscriptionType()`, respectivement. Ces deux fonctions considèrent les paramètres `Appboy.Models.AppboyNotificationSubscriptionType` comme arguments. Ce type a trois états différents :

| Statut d’abonnement | Définition |
| ------------------- | ---------- |
| `OPTED_IN` | Inscrit et explicitement abonné |
| `SUBSCRIBED` | Inscrit et pas explicitement abonné |
| `UNSUBSCRIBED` | Désinscrit ou explicitement désabonné |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

>  Aucun abonnement explicite n’est requis par Windows pour envoyer des notifications push aux utilisateurs. Lorsqu’un utilisateur est enregistré pour les notifications push, il est défini sur `SUBSCRIBED` plutôt que `OPTED_IN` par défaut. Pour en savoir plus, consultez notre documentation sur [l’implémentation des souscriptions et des abonnements explicites][10].

- `EmailNotificationSubscriptionType`
  - Les utilisateurs seront définis sur `SUBSCRIBED` automatiquement à la réception d’une adresse e-mail valide. Cependant, nous vous suggérons d’établir un processus d’abonnement explicite et de définir cette valeur sur `OPTED_IN` dès réception du consentement explicite de votre utilisateur. Pour plus de détails, consultez notre documentation [Modification des souscriptions utilisateur][8].
- `PushNotificationSubscriptionType`
  - Les utilisateurs seront définis sur `SUBSCRIBED` automatiquement après une inscription aux notifications push valide. Cependant, nous vous suggérons d’établir un processus d’abonnement explicite et de définir cette valeur sur `OPTED_IN` dès réception du consentement explicite de votre utilisateur. Pour plus de détails, consultez notre documentation [Modification des souscriptions utilisateur][8].

>  Ces types tombent dans la catégorie `Appboy.Models.AppboyNotificationSubscriptionType`.

## Exemple de code

### Souscription aux e-mails :

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Souscription aux notifications push :

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

[1]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: http://en.wikipedia.org/wiki/ISO_8601
[3]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[8]: {{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
