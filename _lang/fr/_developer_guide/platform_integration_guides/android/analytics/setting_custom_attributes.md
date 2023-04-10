---
nav_title: Définition des attributs personnalisés
article_title: Définir des attributs personnalisés pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 3
description: "Cet article de référence montre comment définir des attributs personnalisés dans votre application Android ou FireOS."

---

# Définir des attributs personnalisés pour Android et FireOS

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

Avant l’implémentation, assurez-vous d’étudier des exemples d’options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d’achat dans notre [aperçu d’analytique][7] ainsi que nos remarques sur les [conventions de dénominations des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Affecter des attributs utilisateur

Pour affecter des attributs à vos utilisateurs, appelez la méthode `getCurrentUser()` de votre instance Braze pour obtenir une référence à l’utilisateur actuel de votre application. Une fois que vous avez obtenu une référence à l’utilisateur actuel, vous pouvez appeler des méthodes pour définir des attributs personnalisés ou prédéfinis.

### Attributs utilisateur standard

Braze fournit des méthodes prédéfinies pour définir les attributs utilisateur suivants dans la [classe BrazeUser][2]. Consultez notre KDoc pour obtenir les [spécifications de la méthode][2] :

- Prénom
- Nom
- Pays
- Langue
- Date de naissance
- E-mail
- Sexe
- Ville d’origine
- Numéro de téléphone

Toutes les valeurs de chaîne de caractères telles que le prénom, le nom de famille, le pays et la ville d’origine sont limitées à 255 caractères.

#### Configurer la valeur d’attribut standard

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setFirstName("first_name");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setFirstName("first_name")
```

{% endtab %}
{% endtabs %}

#### Définir des valeurs d’attributs personnalisés

{% tabs local %}
{% tab String %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", "your_attribute_value");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", "your_attribute_value")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Integer %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute, "your_attribute_key", YOUR_INT_VALUE);
// Integer attributes may also be incremented using code like the following:
Braze.getInstance(context).getCurrentUser().incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute, "your_attribute_key", YOUR_INT_VALUE)
// Integer attributes may also be incremented using code like the following:
Braze.getInstance(context).currentUser?.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Boolean %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Long %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Float %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Double %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Date %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE);
// This method will assign the current time to a custom attribute at the time the method is called:
Braze.getInstance(context).getCurrentUser().setCustomUserAttributeToNow("your_attribute_key");
// This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
Braze.getInstance(context).getCurrentUser().setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE)
// This method will assign the current time to a custom attribute at the time the method is called:
Braze.getInstance(context).currentUser?.setCustomUserAttributeToNow("your_attribute_key")
// This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
Braze.getInstance(context).currentUser?.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH)
```

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
Les dates transmises à Braze avec cette méthode doivent être dans au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (par ex. `2013-07-16T19:20:30+01:00`) ou dans au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (par ex. `2016-12-14T13:32:31.601-0800`).
{% endalert %}

{% endtab %}
{% tab Array %}

Le nombre maximum d’éléments dans les tableaux d’attributs personnalisés est par défaut de 25. Le maximum pour les tableaux individuels peut être augmenté jusqu’à 100 dans le tableau de bord de Braze, sous **Manage Settings > Custom Attributes (Gérer les paramètres > Attributs personnalisés)**. Les tableaux dépassant le nombre maximum d’éléments seront tronqués pour contenir le nombre maximum d’éléments. Pour plus d’informations sur les tableaux d’attributs personnalisés et leur comportement, consultez notre documentation sur les [tableaux]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays).

{% subtabs global %}
{% subtab JAVA %}

```java
// Setting a custom attribute with an array value
Braze.getInstance(context).getCurrentUser().setCustomAttributeArray("your_attribute_key", testSetArray);
// Adding to a custom attribute with an array value
Braze.getInstance(context).getCurrentUser().addToCustomAttributeArray("your_attribute_key", "value_to_add");
// Removing a value from an array type custom attribute
Braze.getInstance(context).getCurrentUser().removeFromCustomAttributeArray("your_attribute_key", "value_to_remove");
```
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Setting a custom attribute with an array value
Braze.getInstance(context).currentUser?.setCustomAttributeArray("your_attribute_key", testSetArray)
// Adding to a custom attribute with an array value
Braze.getInstance(context).currentUser?.addToCustomAttributeArray("your_attribute_key", "value_to_add")
// Removing a value from an array type custom attribute
Braze.getInstance(context).currentUser?.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Enlever la configuration d’un attribut personnalisé

Les attributs personnalisés peuvent également être annulés à l’aide de la méthode suivante :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().unsetCustomUserAttribute("your_attribute_key");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.unsetCustomUserAttribute("your_attribute_key")
```

{% endtab %}
{% endtabs %}

#### Attribut personnalisé via l’API REST

Vous pouvez également utiliser notre API REST pour définir les attributs utilisateur. Pour ce faire, reportez-vous à la [documentation de l’API utilisateur][4].

## Configuration des abonnements utilisateur

Pour configurer un abonnement pour vos utilisateurs (par e-mail ou notification push), appelez les fonctions `setEmailNotificationSubscriptionType()` ou `setPushNotificationSubscriptionType()`, respectivement. Ces deux fonctions considèrent le type de enum `NotificationSubscriptionType` comme arguments. Ce type a trois états différents :

| Statut d’abonnement | Définition |
| ------------------- | ---------- |
| `OPTED_IN` | Inscrit et explicitement abonné |
| `SUBSCRIBED` | Inscrit et pas explicitement abonné |
| `UNSUBSCRIBED` | Désinscrit ou explicitement désabonné |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Aucun abonnement explicite n’est requis par Android pour envoyer des notifications push aux utilisateurs. Lorsqu’un utilisateur est enregistré pour les notifications push, il est défini sur `SUBSCRIBED` plutôt que `OPTED_IN` par défaut. Consultez la [gestion des inscriptions utilisateur]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) pour plus d’informations sur la mise en œuvre des inscriptions et des abonnements explicites.
{% endalert %}

### Définir des inscriptions par e-mail

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setEmailNotificationSubscriptionType(emailNotificationSubscriptionType);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

### Définir de l’inscription aux notifications push

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setPushNotificationSubscriptionType(pushNotificationSubscriptionType);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setPushNotificationSubscriptionType(pushNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

[2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
