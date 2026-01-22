{% multi_lang_include developer_guide/prerequisites/android.md %}

## Attributs par défaut de l’utilisateur

### Méthodes prédéfinies

Braze propose des méthodes prédéfinies pour définir les attributs utilisateur suivants au sein de la classe [`BrazeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html) dans la classe. Pour les spécifications de la méthode, reportez-vous à [notre KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html).

- Prénom
- Nom
- Pays
- Langue
- Date de naissance
- E-mail
- Genre
- Ville d’origine
- Numéro de téléphone

{% alert note %}
Toutes les valeurs de chaîne de caractères telles que le prénom, le nom de famille, le pays et la ville d’origine sont limitées à 255 caractères.
{% endalert %}

### Définition des attributs par défaut

Pour définir un attribut par défaut pour un utilisateur, appelez la méthode `getCurrentUser()` sur votre instance Braze pour obtenir une référence à l'utilisateur actuel de votre application. Vous pouvez ensuite appeler des méthodes pour définir un attribut utilisateur.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setFirstName("first_name");
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setFirstName("first_name")
}
```

{% endtab %}
{% endtabs %}

### Désactivation des attributs par défaut

Pour désactiver un attribut utilisateur, passez `null` à la méthode correspondante.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setFirstName(null);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setFirstName(null)
}
```

{% endtab %}
{% endtabs %}

## Attributs utilisateur personnalisés

Outre les attributs par défaut, Braze vous permet de définir des attributs personnalisés à l'aide de différents types de données. Pour plus d'informations sur l'option de segmentation de chaque attribut, voir [Collecte de données sur les utilisateurs]({{site.baseurl}}/developer_guide/analytics).

### Définition des attributs personnalisés

{% tabs local %}
{% tab Chaîne de caractères %}
Pour définir un attribut personnalisé avec une valeur `string`:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", "your_attribute_value");
  }
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", "your_attribute_value")
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Entiers %}
Pour définir un attribut personnalisé avec une valeur `int`:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE);
    
    // Integer attributes may also be incremented using code like the following:
    brazeUser.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE);
  }
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE)

  // Integer attributes may also be incremented using code like the following:
  brazeUser.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}

Pour définir un attribut personnalisé avec une valeur entière `long`:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Points flottants %}
Pour définir un attribut personnalisé avec une valeur `float`:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}

Pour définir un attribut personnalisé avec une valeur `double`:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Booléen %}
Pour définir un attribut personnalisé avec une valeur `boolean`:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Date %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE);
    // This method will assign the current time to a custom attribute at the time the method is called:
    brazeUser.setCustomUserAttributeToNow("your_attribute_key");
    // This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
    brazeUser.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE)
  // This method will assign the current time to a custom attribute at the time the method is called:
  brazeUser.setCustomUserAttributeToNow("your_attribute_key")
  // This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
  brazeUser.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH)
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
Les dates transmises à Braze avec cette méthode doivent être au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (e.g `2013-07-16T19:20:30+01:00`) ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (e.g `2016-12-14T13:32:31.601-0800`).
{% endalert %}

{% endtab %}
{% tab Réseau %}

Le nombre maximum d’éléments dans les tableaux d’attributs personnalisés est par défaut de 25. Le maximum pour les tableaux individuels peut être augmenté jusqu’à 100 dans le tableau de bord de Braze, sous **Paramètres des données** > **Attributs personnalisés**. Les tableaux dépassant le nombre maximum d’éléments seront tronqués pour contenir le nombre maximum d’éléments. Pour plus d'informations sur les tableaux d'attributs personnalisés et leur comportement, consultez notre documentation sur les [tableaux.]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays)

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    // Setting a custom attribute with an array value
    brazeUser.setCustomAttributeArray("your_attribute_key", testSetArray);
    // Adding to a custom attribute with an array value
    brazeUser.addToCustomAttributeArray("your_attribute_key", "value_to_add");
    // Removing a value from an array type custom attribute
    brazeUser.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove");
  }
});
```
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  // Setting a custom attribute with an array value
  brazeUser.setCustomAttributeArray("your_attribute_key", testSetArray)
  // Adding to a custom attribute with an array value
  brazeUser.addToCustomAttributeArray("your_attribute_key", "value_to_add")
  // Removing a value from an array type custom attribute
  brazeUser.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove")
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Désactivation des attributs personnalisés

Pour désactiver un attribut personnalisé, transmettez la clé de l'attribut concerné à la méthode `unsetCustomUserAttribute`.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.unsetCustomUserAttribute("your_attribute_key");
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.unsetCustomUserAttribute("your_attribute_key")
}
```

{% endtab %}
{% endtabs %}

### Imbrication d'attributs personnalisés

Vous pouvez également imbriquer des propriétés dans des attributs personnalisés. Dans l'exemple suivant, un objet `favorite_book` avec des propriétés imbriquées est défini comme un attribut personnalisé sur le profil utilisateur. Pour plus de détails, reportez-vous à la section [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

{% tabs %}
{% tab JAVA %}
```java
JSONObject favoriteBook = new JSONObject();
try {
  favoriteBook.put("title", "The Hobbit");
  favoriteBook.put("author", "J.R.R. Tolkien");
  favoriteBook.put("publishing_date", "1937");
} catch (JSONException e) {
  e.printStackTrace();
}

braze.getCurrentUser(user -> {
  user.setCustomUserAttribute("favorite_book", favoriteBook);
  return null;
});
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
val favoriteBook = JSONObject()
  .put("title", "The Hobbit")
  .put("author", "J.R.R. Tolkien")
  .put("publishing_date", "1937")

braze.getCurrentUser { user ->
  user.setCustomUserAttribute("favorite_book", favoriteBook)
}
```
{% endtab %}
{% endtabs %}

### Utiliser l'API REST

Vous pouvez également utiliser notre API REST pour définir ou désactiver les attributs des utilisateurs. Pour plus d'informations, reportez-vous aux [Endpoints de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configurer les abonnements des utilisateurs

Pour configurer un abonnement pour vos utilisateurs (par e-mail ou notification push), appelez les fonctions `setEmailNotificationSubscriptionType()` ou `setPushNotificationSubscriptionType()`, respectivement. Ces deux fonctions considèrent le type de enum `NotificationSubscriptionType` comme arguments. Ce type a trois états différents :

| Statut d’abonnement | Définition |
| ------------------- | ---------- |
| `OPTED_IN` | Inscrit et explicitement abonné |
| `SUBSCRIBED` | Inscrit et pas explicitement abonné |
| `UNSUBSCRIBED` | Désinscrit ou explicitement désabonné |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Aucun abonnement explicite n’est requis par Android pour envoyer des notifications push aux utilisateurs. Lorsqu’un utilisateur est enregistré pour les notifications push, il est défini sur `SUBSCRIBED` plutôt que `OPTED_IN` par défaut. Reportez-vous à la [gestion des inscriptions des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) pour plus d'informations sur la mise en œuvre des inscriptions et des abonnements explicites.
{% endalert %}

### Définir des inscriptions par e-mail

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType)
}
```

{% endtab %}
{% endtabs %}

### Définir de l’inscription aux notifications push

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setPushNotificationSubscriptionType(pushNotificationSubscriptionType);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setPushNotificationSubscriptionType(pushNotificationSubscriptionType)
}
```

{% endtab %}
{% endtabs %}

