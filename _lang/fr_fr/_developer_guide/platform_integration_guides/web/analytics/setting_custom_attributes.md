---
nav_title: Définition des attributs personnalisés
article_title: Définir des attributs personnalisés pour le Web
platform: Web
page_order: 3
description: "Cet article de référence explique comment assigner et définir des attributs personnalisés pour le Web."

---

# Définition des attributs personnalisés

> Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pouvez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

Avant de procéder à la mise en œuvre, consultez les exemples d'options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [meilleures pratiques.]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#best-practices)

Pour affecter des attributs à vos utilisateurs, appelez la méthode `braze.getUser()` pour obtenir une référence à l’utilisateur actuel de votre application. Après avoir obtenu une référence à l'utilisateur actuel, vous pouvez appeler des méthodes pour définir des attributs prédéfinis ou personnalisés.

## Affecter des attributs utilisateur prédéfinis

Braze fournit des méthodes prédéfinies pour définir les attributs utilisateur suivants dans la [classe `User`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) :

- Prénom
- Nom
- Langue
- Pays
- Date de naissance
- E-mail
- Genre
- Ville d’origine
- Numéro de téléphone

### Exemples d’implémentation

#### Définir un prénom

```javascript
braze.getUser().setFirstName("SomeFirstName");
```

#### Définir un genre

```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```

#### Définir une date de naissance

```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```

## Affecter des attributs utilisateur personnalisés

En plus de nos méthodes prédéfinies d'attributs utilisateur, Braze fournit également des [attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) pour suivre les données de vos applications. 

Les spécifications complètes des méthodes pour les attributs personnalisés sont disponibles ici dans les [JSDocs.](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)

### Longueur d’attribut personnalisé

Les clés et les valeurs d’attribut personnalisé ont une longueur maximale de 255 caractères. Reportez-vous à la [documentation technique complète](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) pour plus de détails sur les valeurs d'attributs personnalisés valides.

### Exemples d’implémentation

#### Définir un attribut personnalisé avec une valeur de chaîne de caractères
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

#### Définir un attribut personnalisé avec une valeur d’entier
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_INT_VALUE
);

// Integer attributes may also be incremented using code like the following
braze.getUser().incrementCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);
```

#### Définir un attribut personnalisé avec une valeur de date
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_DATE_VALUE
);

// This method will assign the current time to a custom attribute at the time the method is called
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date()
);

// This method will assign the date specified by secondsFromEpoch to a custom attribute
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date(secondsFromEpoch * 1000)
);
```
>  Les dates transmises à Braze avec cette méthode doivent être des objets de date JavaScript.

#### Définir un attribut personnalisé avec une valeur de tableau

Le nombre maximum d’éléments dans les tableaux d’attributs personnalisés est par défaut de 25. Les tableaux individuels peuvent être augmentés jusqu'à 100 dans le tableau de bord de Braze sous **Paramètres des données** > **Attributs personnalisés**. Si vous souhaitez que ce maximum soit augmenté, contactez votre gestionnaire de service à la clientèle. Les [tableaux]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays) dépassant le nombre maximum d'éléments seront tronqués pour contenir le nombre maximum d'éléments.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

### Enlever la configuration d’un attribut personnalisé

Il est possible d’enlever la configuration d’un attribut personnalisé en définissant sa valeur sur `null`.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Définir un attribut personnalisé via l’API REST

Vous pouvez également utiliser notre API REST pour définir les attributs utilisateur. Reportez-vous à la documentation de l'[API des utilisateurs]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) pour plus de détails.

## Configuration des abonnements utilisateur

Pour configurer un abonnement pour vos utilisateurs (par e-mail ou notification push), appelez les fonctions `setEmailNotificationSubscriptionType()` ou `setPushNotificationSubscriptionType()`, respectivement. Ces deux fonctions prennent comme argument le type `enum` `braze.User.NotificationSubscriptionTypes` . Ce type a trois états différents :

| Statut d’abonnement | Définition |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Inscrit et explicitement abonné |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Inscrit et pas explicitement abonné |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Désinscrit ou explicitement désabonné |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Lorsqu’un utilisateur est enregistré pour les notifications push, le navigateur les force à choisir d’autoriser ou de bloquer les notifications. S’ils choisissent de les autoriser, ils sont définis `OPTED_IN` par défaut. 

Consultez la page [Gestion des abonnements des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) pour plus d'informations sur la mise en œuvre des abonnements et des abonnements explicites.

### Exemple de code

#### Désinscrire l’utilisateur par e-mail :
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

#### Désinscrire l’utilisateur par notification push :
```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

