---
nav_title: Réglage des attributs personnalisés
article_title: Paramétrage des attributs personnalisés pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 3
description: "Cet article de référence montre comment définir des attributs personnalisés dans votre application Android."
---

# Définition des attributs personnalisés pour Android/FireOS

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. les attributs personnalisés vs les événements d'achat dans notre [Aperçu analytique][7], ainsi que nos notes sur les [conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Attribution des attributs par défaut de l'utilisateur

Pour assigner des attributs à vos utilisateurs, appelez la méthode `getCurrentUser()` sur votre instance Braze pour obtenir une référence à l'utilisateur actuel de votre application. Une fois que vous avez une référence à l'utilisateur courant, vous pouvez appeler des méthodes pour définir des attributs prédéfinis ou personnalisés.

Braze fournit des méthodes prédéfinies pour définir les attributs d'utilisateurs suivants dans la classe [BrazeUser][2]. Voir les [Javadocs pour les spécifications de méthodes][2]:

- Prénom
- Nom de famille
- Pays
- Langue
- Date de naissance
- Courriel
- URL de l'image d'avatar pour les profils d'utilisateurs Braze
- Sexe
- Ville natale
- Numéro de téléphone
- Données Facebook
- Données Twitter

Toutes les valeurs de chaîne telles que le prénom, le nom de famille, le pays et la ville d'accueil sont limitées à 255 caractères. Les URL des images d'avatar sont limitées à 1024 caractères.

**Exemple d'implémentation** C'est à quoi ressemblerait un prénom dans le code :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setFirstName("prénom");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setFirstName("prénom")
```

{% endtab %}
{% endtabs %}

## Attribution d'attributs utilisateur personnalisés

En plus de nos méthodes d'attribut utilisateur prédéfinies, Braze fournit également des attributs personnalisés pour suivre les données de vos applications. Les attributs personnalisés Braze peuvent être définis avec les types de données suivants :

- Chaînes de caractères
- Tableaux
  - Inclut des méthodes pour définir des tableaux, ajouter des éléments à des tableaux existants, et supprimer des éléments des tableaux existants.
- Nombre entier
- Booléens
- Dates
- Longs
- Flottant
- Doubles

Les spécifications complètes de la méthode pour les attributs personnalisés peuvent être trouvées ici dans la classe [BrazeUser dans les Javadocs][2].

### Définition des valeurs d'attributs personnalisés

{% tabs local %}
{% tab String %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("votre_attribute_key", "votre_attribute_valeur");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("votre_attribute_clé", "votre_attribute_valeur")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Integer %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute, "your_attribute_key", YOUR_INT_VALUE);
// Les attributs entiers peuvent également être incrémentés en utilisant le code suivant :
Braze.getInstance(context).getCurrentUser().incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute, "your_attribute_key", YOUR_INT_VALUE)
// Les attributs entiers peuvent également être incrémentés en utilisant le code suivant :
Braze.getInstance(context).currentUser?.incrementCustomUserAttribute("votre_attribute_key", VOTRE_INCREMENT_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Boolean %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("votre_attribute_key", VOTRE_BOOLEAN_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("votre_attribute_key", VOTRE_BOOLEAN_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Long %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("votre_attribute_key", VOTRE_LONG_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("votre_attribute_clé", VOTRE_LONG_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Float %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("votre_attribute_key", VOTRE_FLOAT_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("votre_attribute_key", VOTRE VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Double %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("votre_attribute_key", VOTRE_DOUBLE_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("votre_attribute_key", VOTRE_DOUBLE_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Date %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("votre_attribute_key", VOTRE_DATE_VALUE);
// Cette méthode assignera l'heure actuelle à un attribut personnalisé au moment où la méthode est appelée:
Braze.getInstance(context).getCurrentUser(). etCustomUserAttributeToNow("votre_attribute_key");
// Cette méthode assignera la date spécifiée par SECONDS_FROM_EPOCH à un attribut personnalisé :
Braze.getInstance(context).getCurrentUser().setCustomUserAttributeToSecondsFromEpoch("votre_attribute_key", SECONDS_FROM_EPOCH);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("votre_attribute_key", VOTRE_DATE_VALUE)
// Cette méthode assignera l'heure actuelle à un attribut personnalisé au moment où la méthode est appelée:
Braze.getInstance(context).currentUser?. etCustomUserAttributeToNow("votre_attribute_key")
// Cette méthode assignera la date spécifiée par SECONDS_FROM_EPOCH à un attribut personnalisé :
Braze.getInstance(context).currentUser?.setCustomUserAttributeToSecondsFromEpoch("votre_attribute_key", SECONDS_FROM_EPOCH)
```

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
Les dates passées à Braze avec cette méthode doivent soit être au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (e. `2013-07-16T19:20:30+01:00`) ou dans le `yyyy-MM-dd'T'H:mm:ss:SSSZ` format (par exemple `2016-12-14T13:32:31.601-0800`).
{% endalert %}

{% endtab %}
{% tab Array %}

Le nombre maximum d'éléments dans les tableaux d'attributs personnalisés est par défaut de 25. Le maximum pour les tableaux individuels peut être augmenté jusqu'à 100 dans le tableau de bord Braze, sous __Gérer les paramètres__ -> __Attributs personnalisés__. Les tableaux dépassant le nombre maximum d'éléments seront tronqués pour contenir le nombre maximum d'éléments. Pour plus d'informations sur les tableaux d'attributs personnalisés et leur comportement, consultez notre [documentation sur les tableaux]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays).

{% subtabs global %}
{% subtab JAVA %}

```java
// Définition d'un attribut personnalisé avec une valeur de tableau
Braze.getInstance(context).getCurrentUser().setCustomAttributeArray("your_attribute_key", testSetArray);
// Ajoutant à un attribut personnalisé avec une valeur de tableau
Braze.getInstance(context). etCurrentUser().addToCustomAttributeArray("votre_attribute_key", "value_to_add");
// Retrait d'une valeur d'un attribut personnalisé de type tableau
Braze.getInstance(context).getCurrentUser().removeFromCustomAttributeArray("votre_attribute_key", "value_to_remove");
```
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Définition d'un attribut personnalisé avec une valeur de tableau
Braze.getInstance(context).currentUser?.setCustomAttributeArray("your_attribute_key", testSetArray)
// Ajout à un attribut personnalisé avec une valeur de tableau
Braze.getInstance(context). urrentUser?.addToCustomAttributeArray("votre_attribute_key", "value_to_add")
// Suppression d'une valeur d'un attribut personnalisé de type tableau
Braze.getInstance(context).currentUser?.removeFromCustomAttributeArray("votre_attribute_key", "value_to_remove")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Annuler la définition d'un attribut personnalisé

Les attributs personnalisés peuvent également être supprimés en utilisant la méthode suivante :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().unsetCustomUserAttribute("votre_attribute_clé");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.unsetCustomUserAttribute("votre_attribute_clé")
```

{% endtab %}
{% endtabs %}

### Attribut personnalisé via l'API REST

Vous pouvez également utiliser notre API REST pour définir les attributs de l'utilisateur. Pour ce faire, reportez-vous à la [documentation de l'API utilisateur][4].

### Longueur de l'attribut personnalisé

Les clés et valeurs d'attributs personnalisés ont une longueur maximale de 255 caractères.  Les chaînes plus longues seront tronquées à 255 caractères.

Des informations complètes sur la classe peuvent être trouvées dans le [javadocs][2].

## Mise en place des abonnements utilisateurs

Pour configurer un abonnement pour vos utilisateurs (email ou push), appelez les fonctions `setEmailNotificationSubscriptionType()`  ou `setPushNotificationSubscriptionType()`, respectivement. Les deux fonctions prennent le type enum 'NotificationSubscriptionType' comme arguments. Ce type a trois états différents :

| Statut de l'abonnement | Définition                                 |
| ---------------------- | ------------------------------------------ |
| `Inscrit`              | Abonné, et explicitement choisi dans       |
| `ABONNEMENT`           | Abonné, mais pas explicitement choisi dans |
| `Désabonné`            | Désabonné et/ou explicitement désabonné    |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Aucun opt-in explicite n'est requis par Android pour envoyer des notifications push aux utilisateurs. Lorsqu'un utilisateur est enregistré pour push, il est réglé sur `ABONNEMENT` plutôt que `OPTED_IN` par défaut. Pour plus d'informations sur l'implémentation des abonnements et des opt-ins explicites, visitez le sujet dans notre [Guide de l'Utilisateur]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).
{% endalert %}

### Exemple de code

#### Paramétrage des abonnements aux emails

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setEmailNotificationSubscriptionType(emailNotificationSubscriptionType) ;
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(contexte).currentUser?.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

#### Réglage de l'abonnement aux notifications push

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setPushNotificationSubscriptionType(pushNotificationSubscriptionType) ;
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setPushNotificationSubscriptionType(pushNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

[2]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/BrazeUser.html

[2]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/BrazeUser.html

[2]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/BrazeUser.html

[2]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/BrazeUser.html
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
