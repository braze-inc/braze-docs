---
nav_title: Réglage des attributs personnalisés
article_title: Réglage des attributs personnalisés pour le Web
platform: Web
page_order: 3
description: "Cet article de référence couvre la façon de définir des attributs personnalisés via le Braze Web SDK."
---

# Définition des attributs personnalisés pour le web

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. attributs personnalisés par rapport aux événements d'achat dans notre section [Meilleures pratiques][7].

Pour assigner des attributs à vos utilisateurs, appelez la méthode `appboy.getUser()` pour obtenir une référence à l'utilisateur actuel de votre application. Une fois que vous avez une référence à l'utilisateur courant, vous pouvez appeler des méthodes pour définir des attributs prédéfinis ou personnalisés.

Braze fournit des méthodes prédéfinies pour définir les attributs utilisateur suivants dans la classe [ab.User][1]:

- Prénom
- Nom de famille
- Chaînes biographiques
- Pays
- Date de naissance
- Courriel
- URL de l'image d'avatar pour les profils d'utilisateurs Braze
- Sexe
- Ville natale
- Numéro de téléphone

## Exemples d'implémentation

### Définir un prénom

```javascript
appboy.getUser().setFirstName("SomeFirstName");
```

### Définition d'un sexe

```javascript
appboy.getUser().setGender(appboy.User.Genders.FEMALE);
```

### Définir une date de naissance

```javascript
appboy.getUser().setDateOfBirth(2000, 12, 25);
```

## Attribution d'attributs utilisateur personnalisés

En plus de nos méthodes d'attribut utilisateur prédéfinies, Braze fournit également des attributs personnalisés pour suivre les données de vos applications. Les attributs personnalisés Braze peuvent être définis avec les types de données suivants :

- Chaînes de caractères
- Tableaux
  - Inclut des méthodes pour définir des tableaux, ajouter des éléments à des tableaux existants et supprimer des éléments des tableaux existants.
- Nombre entier
- Booléens
- Dates
- Longs
- Flottant

Les spécifications complètes de la méthode pour les attributs personnalisés peuvent être trouvées ici dans la classe [ab.User JSDocs][1].

### Exemples d'implémentation

#### Définir un attribut personnalisé avec une valeur de chaîne de caractères
```javascript
appboy.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  VOTRE_STRING_VALUE
);
```

#### Définition d'un attribut personnalisé avec une valeur entière
```javascript
appboy.getUser(). etCustomUserAttribute(
  VOTRE_ATTRIBUTE_KEY_STRING,
  VOTRE_INT_VALUE
) ;

// Les attributs entiers peuvent également être incrémentés en utilisant du code comme l'appboy
suivant. etUser().incrementCustomUserAttribute(
  VOTRE_ATTRIBUTE_KEY_STRING,
  THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);
```

#### Définition d'un attribut personnalisé avec une valeur de date
```javascript
appboy.getUser(). etCustomUserAttribute(
  VOTRE_ATTRIBUTE_KEY_STRING,
  VOTRE_DATE_VALUE
) ;

// Cette méthode va assigner l'heure courante à un attribut personnalisé au moment où la méthode est appelée
appboy. etUser(). etCustomUserAttribute(
  VOTRE_ATTRIBUTE_KEY_STRING,
  new Date()
);

// Cette méthode assignera la date spécifiée par secondsFromEpoch à un attribut personnalisé
appboy. etUser().setCustomUserAttribute(
  VOUS_ATTRIBUTE_KEY_STRING,
  nouvelle Date(secondsFromEpoch * 1000)
);
```
> Les dates passées à Braze avec cette méthode doivent être des objets JavaScript Date .

#### Définition d'un attribut personnalisé avec une valeur de tableau
Le nombre maximum d'éléments dans les tableaux d'attributs personnalisés est par défaut de 25. Le maximum pour chaque tableau peut être augmenté jusqu'à 100. Si vous souhaitez augmenter ce maximum, veuillez contacter votre responsable du service à la clientèle. Les tableaux dépassant le nombre maximum d'éléments seront tronqués pour contenir le nombre maximum d'éléments. Pour plus d'informations sur les tableaux d'attributs personnalisés et leur comportement, consultez notre [Documentation sur les tableaux][6].

```javascript
appboy.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Ajoute un nouvel élément à un attribut personnalisé avec une valeur tableau
appboy.getUser(). ddToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Suppression d'un élément d'un attribut personnalisé avec une valeur de tableau
appboy.getUser().removeFromCustomAttributeArray("custom_attribute_array_test", "valeur à supprimer");
```

### Annuler la définition d'un attribut personnalisé

Les attributs personnalisés peuvent être supprimés en définissant leur valeur à null.

```javascript
appboy.getUser().setCustomUserAttribute(VOTRE_ATTRIBUTE_KEY_STRING, null);
```

### Définition d'un attribut personnalisé via l'API REST

Vous pouvez également utiliser notre API REST pour définir les attributs de l'utilisateur. Pour ce faire, reportez-vous à la [documentation de l'API utilisateur][4].

### Longueur de l'attribut personnalisé

Les clés et valeurs d'attributs personnalisés ont une longueur maximale de 255 caractères. Consultez la [documentation technique complète][1] pour des détails sur les valeurs d'attributs personnalisés valides.

### Mise en place des abonnements utilisateurs

Pour configurer un abonnement pour vos utilisateurs (email ou push), appelez les fonctions `setEmailNotificationSubscriptionType()`  ou `setPushNotificationSubscriptionType()`, respectivement. Les deux fonctions prennent le type enum 'appboy.User.NotificationSubscriptionTypes' comme arguments. Ce type a trois états différents :

| Statut de l'abonnement | Définition                                 |
| ---------------------- | ------------------------------------------ |
| `Inscrit`              | Abonné, et explicitement choisi dans       |
| `ABONNEMENT`           | Abonné, mais pas explicitement choisi dans |
| `Désabonné`            | Désabonné et/ou explicitement désabonné    |
{: .reset-td-br-1 .reset-td-br-2}

> Lorsqu'un utilisateur est enregistré pour push, le navigateur les force à choisir d'autoriser ou de bloquer les notifications, et s'ils choisissent d'autoriser push, ils sont définis `OPTED_IN` par défaut. Pour plus d'informations sur l'implémentation des abonnements et des opt-ins explicites, visitez le sujet dans [notre documentation][10].

### Exemple de code

#### Se désabonner d'un utilisateur de l'e-mail:
```javascript
appboy.getUser().setEmailNotificationSubscriptionType(appboy.User.NotificationSubscriptionTypes.UNBSCRIBED);
```

#### Désinscription d'un utilisateur de push:
```java
appboy.getUser().setPushNotificationSubscriptionType(appboy.User.NotificationSubscriptionTypes.UNBSCRIBED);
```

[1]: https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html "ab.User"

[1]: https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html "ab.User"

[1]: https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html "ab.User"
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
