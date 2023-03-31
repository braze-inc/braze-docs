---
nav_title: Définition des attributs personnalisés
article_title: Définition des attributs personnalisés pour le Roku
platform: Roku
page_order: 4
page_type: reference
description: "Cette page décrit les méthodes permettant d’assigner des attributs personnalisés aux utilisateurs via le SDK Braze."

---

# Définition des attributs personnalisés

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

Avant l’implémentation, assurez-vous d’étudier des exemples des options de segmentation offertes par les événements personnalisés, les attributs utilisateur et les événements d’achat dans nos [bonnes pratiques][7]. Nous vous recommandons également de vous familiariser avec nos [conventions de dénomination des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Affecter des attributs utilisateur par défaut

Les attributs utilisateur seront assignés à l’utilisateur actuellement actif. Les champs par défaut suivants peuvent être définis :

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

**Exemple d’implémentation**<br>C’est ce qui définit ce à quoi le prénom ressemblera dans le code :

```javascript
m.Braze.setFirstName("User's First Name")
```

## Affecter des attributs utilisateur personnalisés

En plus des attributs utilisateur par défaut, Braze vous permet également de définir des attributs personnalisés en utilisant plusieurs types de données différents.

### Paramètres des valeurs d’attribut personnalisé
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
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
Braze traite les valeurs FLOAT et DOUBLE exactement de la même manière au sein de la base de données.
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

### Incrementing/decrementing (Incrémenter/décrémenter) les attributs personnalisés

Ce code est un exemple d’incrémentation d’un attribut personnalisé. Vous pouvez augmenter la valeur d’un attribut personnalisé par une valeur entière positive ou négative.

```javascript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Enlever la configuration d’un attribut personnalisé

Les attributs personnalisés peuvent également être annulés à l’aide de la méthode suivante :

```javascript
m.Braze.unsetCustomAttribute("attributeName")
```

### Définir un attribut personnalisé via l’API REST

Vous pouvez également utiliser notre API REST pour définir les attributs utilisateur. Reportez-vous à la documentation de l’[API utilisateur][4] pour plus de détails.

### Limites de valeur d’attribut personnalisé

Les valeurs d’attribut personnalisé ont une longueur maximale de 255 caractères.

## Gestion du statut d’abonnement aux e-mails

Vous pouvez définir les statuts d’abonnement aux e-mails suivants pour vos utilisateurs par programmation via le SDK.

| Statut d’abonnement | Définition |
| ------------------- | ---------- |
| `OptedIn` | Inscrit et explicitement abonné |
| `Subscribed` | Inscrit et pas explicitement abonné |
| `UnSubscribed` | Désinscrit ou explicitement désabonné |
{: .reset-td-br-1 .reset-td-br-2}

>  Ces types tombent dans la catégorie `BrazeConstants().SUBSCRIPTION_STATES`.

La méthode de définition du statut d’abonnement aux e-mails est `setEmailSubscriptionState()`. Les utilisateurs seront définis sur `Subscribed` automatiquement dès réception d’une adresse e-mail valide. Cependant, nous vous suggérons d’établir un processus d’abonnement explicite et de définir cette valeur sur `OptedIn` dès réception du consentement explicite de votre utilisateur. Consultez [Gérer les abonnements utilisateur][10] pour plus de détails.

Exemple d’utilisation :
```javascript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_user_ids/#user-id-integration-best-practices--notes
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
