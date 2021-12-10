---
nav_title: Réglage des attributs personnalisés
article_title: Réglage des attributs personnalisés pour l'unité
platform:
  - Unité
  - iOS
  - Android
page_order: 2
description: "Cet article de référence couvre la façon de définir des attributs personnalisés sur la plate-forme Unity."
---

# Paramétrage des attributs personnalisés

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. attributs personnalisés par rapport aux événements d'achat dans notre section [Meilleures pratiques][1].

## Attribution des attributs par défaut de l'utilisateur

Pour assigner les attributs de l'utilisateur, vous devez appeler la méthode appropriée sur l'objet BrazeBinding . Ce qui suit est une liste d'attributs intégrés qui peuvent être appelés en utilisant cette méthode.

### Prénom
`AppboyBinding.SetUserFirstName("prénom");`

### Nom de famille
`AppboyBinding.SetUserLastName("last name");`

### E-mail de l'utilisateur
`AppboyBinding.SetUserEmail("email@email.com");`

> Il est toujours utile de définir des adresses e-mail même si vous n'envoyez pas de courriels par l'intermédiaire du Brésil. Le courrier électronique facilite la recherche de profils utilisateur individuels et permet de résoudre les problèmes au fur et à mesure qu'ils se présentent.

### Sexe
`AppboyBinding.SetUserGender(Appboy.Models.Gender);`

### Date de naissance
`AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)));`

### Pays de l'utilisateur
`AppboyBinding.SetUserCountry("nom du pays");`

### Ville de la maison de l'utilisateur
`AppboyBinding.SetUserHomeCity("nom de la ville");`

### Abonnement par e-mail de l'utilisateur
`AppboyBinding.Set.UserNotificationNotificationNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### Abonnement push de l'utilisateur
`AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType) ;`

### Numéro de téléphone de l'utilisateur
`AppboyBinding.SetUserPhoneNumber("numéro de téléphone");`

## Attribution d'attributs utilisateur personnalisés

Au-delà des attributs ci-dessus, Braze vous permet également de définir des attributs personnalisés en utilisant un certain nombre de types de données différents : Pour plus d'informations concernant les options de segmentation, chacun de ces attributs vous permettra de voir notre documentation ["Meilleures pratiques"][1] dans cette section.

### Définition des valeurs d'attributs personnalisés

{% tabs %}
{% tab Boolean Value %}

```csharp
AppboyBinding.SetCustomUserAttribute("clé d'attribut boolean personnalisée", 'valeur booléenne');
```

{% endtab %}
{% tab Integer %}

```csharp
// Set Integer Attribute
AppboyBinding.SetCustomUserAttribute("custom int attribute key", 'integer value');
// Increment Integer Attribute
AppboyBinding.IncrementCustomUserAttribute("key", increment(int))
```

{% endtab %}
{% tab Double %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom double attribute key", 'double valeur');
```

{% endtab %}
{% tab String %}

```csharp
AppboyBinding.SetCustomUserAttribute("clé d'attribut de chaîne personnalisée", "attribut personnalisé de la chaîne de caractères");
```

{% endtab %}
{% tab Date %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("clé d'attribut de date personnalisée");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

> Les dates passées à Braze doivent soit être au format [ISO 8601][2] , e. `2013-07-16T19:20:30+01:00` ou dans le `yyyy-MM-dd'T'H:mm:ss:SSSZ` format e.g `2016-12-14T13:32:31.601-0800`

{% endtab %}
{% tab Array %}

```csharp
// Définition d'un tableau
AppboyBinding.SetCustomUserAttributeArray("key", array(List), sizeOfTheArray(int))
// Ajout à un tableau
AppboyBinding. ddToCustomUserAttributeArray("key", "Attribute")
// Suppression d'un élément d'un tableau
AppboyBinding.RemoveFromCustomUserAttributeArray("key", "Attribute")
```
{% endtab %}
{% endtabs %}
### Annuler la définition d'un attribut personnalisé

Les attributs personnalisés peuvent également être supprimés en utilisant la méthode suivante :

```csharp
AppboyBinding.UnsetCustomUserAttribute("clé d'attribut personnalisé");
```

## Définition d'un attribut personnalisé via l'API REST
Vous pouvez également utiliser notre API REST pour définir les attributs de l'utilisateur. Pour ce faire, reportez-vous à la [documentation de l'API utilisateur][3].

## Limites de valeur d'attribut personnalisé
Les valeurs d'attributs personnalisés ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.

## Mise en place des abonnements utilisateurs

Pour configurer un abonnement pour vos utilisateurs (e-mail ou push), appelez les fonctions     
`AppboyBinding. etUserEmailNotificationSubscriptionType()` ou `AppboyBinding.SetPushNotificationSubscriptionType()`, respectivement. Les deux fonctions prennent les paramètres `Appboy.Models.AppboyNotificationSubscriptionType` comme arguments. Ce type a trois états différents :

| Statut de l'abonnement | Définition                                 |
| ---------------------- | ------------------------------------------ |
| `Inscrit`              | Abonné, et explicitement choisi dans       |
| `ABONNEMENT`           | Abonné, mais pas explicitement choisi dans |
| `Désabonné`            | Désabonné et/ou explicitement désabonné    |
{: .reset-td-br-1 .reset-td-br-2}

> Windows n'a pas d'opt-in explicite pour envoyer des notifications push aux utilisateurs. Lorsqu'un utilisateur est enregistré pour push, il est réglé sur `ABONNEMENT` plutôt que `OPTED_IN` par défaut. Pour en savoir plus, consultez notre documentation sur [l'implémentation d'abonnements et d'opt-ins explicites][10].

- `Type d'abonnement à la notification par e-mail`
  - Les utilisateurs seront automatiquement mis à `S'ABONNER` dès réception d'une adresse e-mail valide. Cependant, nous vous suggérons d'établir un processus opt-in explicite et de définir cette valeur à `OPTED_IN` dès réception du consentement explicite de votre utilisateur. Visitez notre doc [Modifier les abonnements aux utilisateurs][8] pour plus de détails.
- `Type d'abonnement à la notification Push`
  - Les utilisateurs seront automatiquement mis à `S'ABONNER` lors d'une inscription push valide. Cependant, nous vous suggérons d'établir un processus opt-in explicite et de définir cette valeur à `OPTED_IN` dès réception du consentement explicite de votre utilisateur. Visitez notre doc [Modifier les abonnements aux utilisateurs][8] pour plus de détails.

> Ces types tombent sous `Appboy.Models.AppboyNotificationSubscriptionType`.

## Exemple de code

### Abonnement par e-mail:

```csharp
AppboyBinding.SetUserNotificationNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Abonnement à la notification push :

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

[1]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection

[1]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: http://en.wikipedia.org/wiki/ISO_8601
[3]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[8]: {{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
