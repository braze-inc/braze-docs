---
nav_title: Définir des attributs personnalisés
article_title: Définir des attributs personnalisés pour Windows Universal
platform: Windows Universal
page_order: 3
description: "Cet article de référence explique comment définir des attributs personnalisés sur la plateforme Windows Universal."
hidden: true
---

# Définir des attributs personnalisés
{% multi_lang_include archive/windows_deprecation.md %}

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

Avant l’implémentation, assurez-vous d’étudier des exemples des options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d’achat dans nos [bonnes pratiques.][7].

Les attributs utilisateur peuvent être attribués au `IAppboyUser` actuel. Pour obtenir une référence au `IAppboyUser` actuel, appelez `Appboy.SharedInstance.AppboyUser`

## Affecter des attributs utilisateur par défaut

Les attributs suivants doivent être définis comme des propriétés du `IAppboyUser` :

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `HomeCity`
- `PhoneNumber`

**Exemple d’implémentation**

```csharp
Appboy.SharedInstance.AppboyUser.FirstName = "Prénom de l’utilisateur"
```

## Affecter des attributs utilisateur personnalisés

En plus des attributs utilisateur par défaut, Braze vous permet également de définir des attributs personnalisés en utilisant un certain nombre de types de données différents. Pour plus d’informations sur les options de segmentation et sur la manière dont chacun de ces attributs vous affectera, consultez nos [bonnes pratiques]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices-and-notes).

### Définir des valeurs d’attributs personnalisés

{% tabs %}
{% tab Boolean %}
```csharp
bool SetCustomAttribute(STRING_KEY, BOOL_VALUE);
```
{% endtab %}
{% tab Integer %}
```csharp
bool SetCustomAttribute(STRING_KEY, INT_VALUE);
```
{% endtab %}
{% tab Double/Float %}
```csharp
bool SetCustomAttribute(STRING_KEY, DOUBLE_VALUE);
```
Braze traite les valeurs FLOAT et DOUBLE exactement de la même manière au sein de la base de données.
{% endtab %}
{% tab String %}
```csharp
bool SetCustomAttribute(STRING_KEY, "STRING_VALUE");
```
{% endtab %}
{% tab Long %}
```csharp
bool SetCustomAttribute(STRING_KEY, LONG_VALUE);
```
{% endtab %}
{% tab Date %}
```csharp
bool SetCustomAttribute(STRING_KEY, "DATE_VALUE");
```
>  Les dates transmises à Braze doivent être au format [ISO 8601][2] par ex. `2013-07-16T19:20:30+01:00` ou au  format`yyyy-MM-dd'T'HH:mm:ss:SSSZ`, par exemple,`2016-12-14T13:32:31.601-0800`
{% endtab %}
{% tab Array %}
```csharp
// Définir un attribut personnalisé avec une valeur de tableau
Appboy.SharedInstance.EventLogger.SetCustomAttributeArray("custom_attribute_array_test", testSetArray);
// Ajouter un attribut personnalisé avec une valeur de tableau
Appboy.SharedInstance.EventLogger.AddToCustomAttributeArray("custom_attribute_array_test", testAddString);
// Supprimer une valeur d’un attribut personnalisé de type tableau
Appboy.SharedInstance.EventLogger.RemoveFromCustomAttributeArray("custom_attribute_array_test", testRemString);
```
{% endtab %}
{% endtabs %}

### Incrémenter ou décrémenter les attributs personnalisés

Ce code est un exemple d’incrémentation d’un attribut personnalisé. Vous pouvez augmenter la valeur d’un attribut personnalisé par une valeur entière positive ou négative.

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### Enlever la configuration d’un attribut personnalisé

Les attributs personnalisés peuvent également être annulés à l’aide de la méthode suivante :

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### Définir un attribut personnalisé via l’API REST

Vous pouvez également utiliser notre API REST pour définir les attributs utilisateur. Reportez-vous à la documentation de l’[API ][4] utilisateur pour plus de détails.

### Limites de valeur d’attribut personnalisé

Les valeurs d’attribut personnalisé ont une longueur maximale de 255 caractères. Les valeurs plus longues seront tronquées.

## Gérer les statuts d’abonnement aux notifications

Pour configurer un abonnement pour vos utilisateurs (par e-mail ou notification push), vous pouvez définir le suivi des statuts d’abonnement comme propriétés du `IAppboyUser`. Les statuts d’abonnement ont trois états différents concernant les e-mails et les notifications push dans Braze :

| Statut d’abonnement | Définition |
| ------------------- | ---------- |
| `OptedIn` | Inscrit et explicitement abonné |
| `Subscribed` | Inscrit et pas explicitement abonné |
| `UnSubscribed` | Désinscrit ou explicitement désabonné |
{: .reset-td-br-1 .reset-td-br-2}

- `EmailNotificationSubscriptionType`
  - Les utilisateurs seront définis sur `Subscribed` automatiquement dès réception d’une adresse e-mail valide. Cependant, nous vous suggérons d’établir un processus d’abonnement explicite et de définir cette valeur sur `OptedIn` dès réception du consentement explicite de votre utilisateur.
- `PushNotificationSubscriptionType`
  - Les utilisateurs seront définis sur `Subscribed` automatiquement dès l’enregistrement d’une notification push valide. Cependant, nous vous suggérons d’établir un processus d’abonnement explicite et de définir cette valeur sur `OptedIn` dès réception du consentement explicite de votre utilisateur.

>  Ces types tombent dans la catégorie `AppboyPlatform.PCL.Models.NotificationSubscriptionType`. Consultez [Gérer les abonnements utilisateur ][10] pour plus de détails.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices--notes
[2]: http://en.wikipedia.org/wiki/ISO_8601
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
