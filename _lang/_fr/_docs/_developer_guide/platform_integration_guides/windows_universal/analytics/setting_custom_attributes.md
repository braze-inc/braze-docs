---
nav_title: Réglage des attributs personnalisés
article_title: Réglage des attributs personnalisés pour Windows Universal
platform: Univers Windows
page_order: 3
description: "Cet article de référence couvre la façon de définir des attributs personnalisés sur la plate-forme Windows Universelle."
---

# Paramétrage des attributs personnalisés

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. attributs personnalisés par rapport aux événements d'achat dans notre section [Meilleures pratiques][7].

Les attributs de l'utilisateur peuvent être assignés à l'actuel `IAppboyUser`. Pour obtenir une référence à l'actuel `IAppboyUser`, appelez `Appboy.SharedInstance.AppboyUser`

## Attribution des attributs par défaut de l'utilisateur

Les attributs suivants doivent être définis comme des propriétés de `IAppboyUser`:

- `Prénom`
- `Nom de famille`
- `Courriel`
- `Sexe`
- `Date de naissance`
- `Pays`
- `Ville natale`
- `Numéro de téléphone`
- `Données Facebook`
- `Données Twitter`

**Exemple d'implémentation**

```csharp
Appboy.SharedInstance.AppboyUser.FirstName = "Prénom de l'utilisateur"
```

## Attribution d'attributs utilisateur personnalisés

Au-delà des attributs ci-dessus, Braze vous permet également de définir des attributs personnalisés en utilisant un certain nombre de types de données différents : Pour plus d'informations concernant les options de segmentation, et comment chacun de ces attributs vous affectera, consultez notre documentation ["Meilleures pratiques"][1] dans cette section.

### Définition des valeurs d'attributs personnalisés

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
{% onglet Double/Float %}
```csharp
bool SetCustomAttribute(STRING_KEY, DOUBLE_VALUE);
```
Braze traite exactement les valeurs FLOAT et DOUBLE dans notre base de données.
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
> Les dates passées à Braze doivent soit être au format [ISO 8601][2] , e. `2013-07-16T19:20:30+01:00` ou dans le `yyyy-MM-dd'T'H:mm:ss:SSSZ` format e.g `2016-12-14T13:32:31.601-0800` 
> 
> {% endtab %}
> 
> 
> 
> {% tab Array %}
```csharp
// Définition d'un attribut personnalisé avec une valeur de tableau
Appboy.SharedInstance.EventLogger.SetCustomAttributeArray("custom_attribute_array_test", testSetArray);
// Ajout à un attribut personnalisé avec une valeur de tableau
Appboy.SharedInstance.EventLogger. ddToCustomAttributeArray("custom_attribute_array_test", testAddString);
// Suppression d'une valeur d'un attribut personnalisé de type tableau
Appboy.SharedInstance.EventLogger.RemoveFromCustomAttributeArray("custom_attribute_array_test", testRemString);
```
{% endtab %}
{% endtabs %}

### Incrément/décrémentation d'attributs personnalisés

Ce code est un exemple d'attribut personnalisé incrémenté. Vous pouvez incrémenter la valeur d'un attribut personnalisé par n'importe quelle valeur entière positive ou négative.

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### Annuler la définition d'un attribut personnalisé

Les attributs personnalisés peuvent également être supprimés en utilisant la méthode suivante :

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### Définition d'un attribut personnalisé via l'API REST

Vous pouvez également utiliser notre API REST pour définir les attributs de l'utilisateur. Pour ce faire, reportez-vous à la [documentation de l'API utilisateur][4].

### Limites de valeur d'attribut personnalisé

Les valeurs d'attributs personnalisés ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.

## Gestion des statuts d'abonnement aux notifications

Pour configurer un abonnement pour vos utilisateurs (e-mail ou push), vous pouvez définir les statuts d'abonnement ci-dessous comme propriétés de `IAppboyUser`. Les statuts de l'abonnement à Braze ont trois états différents pour l'e-mail et le push :

| Statut de l'abonnement | Définition                                 |
| ---------------------- | ------------------------------------------ |
| `OptedIn`              | Abonné, et explicitement choisi dans       |
| `Inscrit`              | Abonné, mais pas explicitement choisi dans |
| `Désabonné`            | Désabonné et/ou explicitement désabonné    |
{: .reset-td-br-1 .reset-td-br-2}

- `Type d'abonnement à la notification par e-mail`
  - Les utilisateurs seront configurés sur `Abonné` automatiquement à la réception d'une adresse e-mail valide. Nous vous suggérons d'établir un processus d'opt-in explicite et de définir cette valeur à `OptedIn` sur réception du consentement explicite de votre utilisateur. Visitez notre doc [Gérer les abonnements][10] pour plus de détails.
- `Type d'abonnement à la notification Push`
  - Les utilisateurs seront automatiquement configurés sur `Abonné` lors de l'inscription push valide, cependant, Nous vous suggérons d'établir un processus d'opt-in explicite et de définir cette valeur à `OptedIn` sur réception du consentement explicite de votre utilisateur. Visitez notre doc [Gérer les abonnements][10] pour plus de détails.

> Ces types tombent sous `AppboyPlatform.PCL.Models.NotificationSubscriptionType`

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices--notes
[2]: http://en.wikipedia.org/wiki/ISO_8601
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
