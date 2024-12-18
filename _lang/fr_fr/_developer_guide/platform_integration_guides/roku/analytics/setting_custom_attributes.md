---
nav_title: Définition des attributs personnalisés
article_title: Définition des attributs personnalisés pour le Roku
platform: Roku
page_order: 4
page_type: reference
description: "Cet article de référence décrit les méthodes permettant d’assigner des attributs personnalisés aux utilisateurs de Roku via le SDK Braze."

---

# Définition des attributs personnalisés

> Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

Avant de procéder à la mise en œuvre, n'oubliez pas de consulter les exemples d'options de segmentation offertes par les événements personnalisés, les attributs utilisateurs et les événements d'achat dans nos [meilleures pratiques.]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) Nous vous recommandons également de vous familiariser avec nos [conventions de dénomination des événements.]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)

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

**Exemple de mise en œuvre**<br>C’est ce qui définit ce à quoi le prénom ressemblera dans le code :

```brightscript
m.Braze.setFirstName("User's First Name")
```

## Affecter des attributs utilisateur personnalisés

En plus des attributs utilisateur par défaut, Braze vous permet également de définir des attributs personnalisés en utilisant plusieurs types de données différents.

### Paramètres des valeurs d’attribut personnalisé
{% tabs %}
{% tab Booléen %}
```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}
{% tab Entier %}
```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}
{% tab Flottant ou double %}
```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
Braze traite les valeurs FLOAT et DOUBLE exactement de la même manière au sein de la base de données.
{% endtab %}
{% tab Chaîne de caractères %}
```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}
{% tab Date %}
```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}
{% tab Réseau %}
```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

### Incrémenter ou décrémenter les attributs personnalisés

Ce code est un exemple d’incrémentation d’un attribut personnalisé. Vous pouvez augmenter la valeur d’un attribut personnalisé par une valeur entière positive ou négative.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Enlever la configuration d’un attribut personnalisé

Les attributs personnalisés peuvent également être annulés à l’aide de la méthode suivante :

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### Définir un attribut personnalisé via l’API REST

Vous pouvez également utiliser notre API REST pour définir les attributs utilisateur. Reportez-vous à la documentation de l'[API des utilisateurs]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) pour plus de détails.

### Limites de valeur d’attribut personnalisé

Les valeurs d’attribut personnalisé ont une longueur maximale de 255 caractères.

## Gestion du statut d’abonnement aux e-mails

Vous pouvez définir les statuts d’abonnement aux e-mails suivants pour vos utilisateurs par programmation via le SDK.

| Statut d’abonnement | Définition |
| ------------------- | ---------- |
| `OptedIn` | Inscrit et explicitement abonné |
| `Subscribed` | Inscrit et pas explicitement abonné |
| `UnSubscribed` | Désinscrit ou explicitement désabonné |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

>  Ces types tombent dans la catégorie `BrazeConstants().SUBSCRIPTION_STATES`.

La méthode de définition du statut d’abonnement aux e-mails est `setEmailSubscriptionState()`. Les utilisateurs seront définis sur `Subscribed` automatiquement dès réception d’une adresse e-mail valide. Cependant, nous vous suggérons d’établir un processus d’abonnement explicite et de définir cette valeur sur `OptedIn` dès réception du consentement explicite de votre utilisateur. Pour plus de détails, consultez la page [Gestion des abonnements des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

Exemple d’utilisation :
```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```

