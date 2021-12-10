---
nav_title: Réglage des attributs personnalisés
article_title: Réglage des attributs personnalisés pour Roku
platform: Roku
page_order: 4
page_type: Référence
description: "Cette page décrit les méthodes pour assigner des attributs personnalisés aux utilisateurs via le Braze SDK."
---

# Paramétrage des attributs personnalisés

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. Attributs utilisateur vs. achat événements dans notre section [Meilleures pratiques][7]. Vous devriez également consulter nos notes sur [les conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Attribution des attributs par défaut de l'utilisateur

Les attributs de l'utilisateur seront assignés à l'utilisateur actuellement actif. Les champs suivants par défaut peuvent être définis :

- `Prénom`
- `Nom de famille`
- `Courriel`
- `Sexe`
- `Date de naissance`
- `Pays`
- `Langue`
- `Ville natale`
- `Numéro de téléphone`
- `AvatarImageUrl`

**Exemple d'implémentation**<br>C'est à quoi ressemblerait un prénom dans le code :

```javascript
m.Braze.setFirstName("Prénom de l'utilisateur")
```

## Attribution d'attributs utilisateur personnalisés

Au-delà des attributs par défaut ci-dessus, Braze vous permet également de définir des attributs personnalisés en utilisant plusieurs types de données. Pour plus d'informations concernant les options de segmentation, et comment chacun de ces attributs vous affectera, voir notre [documentation sur les meilleures pratiques][1] dans cette section.

### Paramètres des valeurs d'attributs personnalisés
{% tabs %}
{% tab Boolean %}
```javascript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}
{% tab Integer %}
```javascript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}
{% tab Float/Double %}
```javascript
m.Braze.setCustomAttribute("attribut flottant", 3.5)
```
Braze traite exactement les valeurs FLOAT et DOUBLE dans notre base de données.
{% endtab %}
{% tab String %}
```javascript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}
{% tab Date %}
```javascript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}
{% tab Array %}
```javascript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

### Incrément/décrémentation d'attributs personnalisés

Ce code est un exemple d'attribut personnalisé incrémenté. Vous pouvez incrémenter la valeur d'un attribut personnalisé par n'importe quelle valeur entière positive ou négative.

```javascript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Annuler la définition d'un attribut personnalisé

Les atributs personnalisés peuvent également être supprimés en utilisant la méthode suivante :

```javascript
m.Braze.unsetCustomAttribute("Nom")
```

### Définition d'un attribut personnalisé via l'API REST

Vous pouvez également utiliser notre API REST pour définir les attributs de l'utilisateur. Pour ce faire, reportez-vous à la [documentation de l'API utilisateur][4].

### Limites de valeur d'attribut personnalisé

Les valeurs d'attributs personnalisés ont une longueur maximale de 255 caractères.

## Gestion du statut d'abonnement aux e-mails

Vous pouvez définir les statuts d'abonnement suivants pour vos utilisateurs par le biais du SDK.

| Statut de l'abonnement | Définition                                 |
| ---------------------- | ------------------------------------------ |
| `OptedIn`              | Abonné, et explicitement choisi dans       |
| `Inscrit`              | Abonné, mais pas explicitement choisi dans |
| `Désabonné`            | Désabonné et/ou explicitement désabonné    |
{: .reset-td-br-1 .reset-td-br-2}

> Ces types tombent sous `BrazeConstants().SUBSCRIPTION_STATES`

The method for setting email subscription status is `setEmailSubscriptionState()`. Les utilisateurs seront configurés sur `Abonné` automatiquement à la réception d'une adresse e-mail valide. Nous vous suggérons d'établir un processus d'opt-in explicite et de définir cette valeur à `OptedIn` sur réception du consentement explicite de votre utilisateur. Visitez notre doc [Gérer les abonnements][10] pour plus de détails.

Exemple d'utilisation :
```javascript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_user_ids/#user-id-integration-best-practices--notes
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
