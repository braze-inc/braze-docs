{% multi_lang_include developer_guide/prerequisites/web.md %}

## Attributs par défaut de l’utilisateur

### Méthodes prédéfinies

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

### Définition des attributs par défaut

{% tabs %}
{% tab l'utilisation de méthodes %}
Pour définir un attribut par défaut pour un utilisateur, appelez la méthode `getUser()` sur votre instance Braze pour obtenir une référence à l'utilisateur actuel de votre application. Vous pouvez ensuite appeler des méthodes pour définir un attribut utilisateur.

{% subtabs local %}
{% subtab First name %}
```javascript
braze.getUser().setFirstName("SomeFirstName");
```
{% endsubtab %}
{% subtab Gender %}
```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```
{% endsubtab %}
{% subtab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Google Tag Manager %}
Avec Google Tag Manager, les tags standards (tels que le prénom de l'utilisateur) doivent être enregistrés de la même manière que les attributs personnalisés. Assurez-vous que les valeurs que vous transmettez pour les attributs standard correspondent au format attendu spécifié dans la documentation de la [classe User](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

Par exemple, l'attribut gender peut accepter l'une des valeurs suivantes : `"m" | "f" | "o" | "u" | "n" | "p"`. Par conséquent, pour définir le sexe d’un utilisateur en tant que femme, créez une balise HTML personnalisée avec le contenu suivant :

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### Désactivation des attributs par défaut

Pour désactiver un attribut par défaut de l'utilisateur, passez `null` à la méthode correspondante. Par exemple :

{% tabs local %}
{% tab Prénom %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab Genre %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab Date de naissance %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## Attributs utilisateur personnalisés

### Définition des attributs personnalisés

{% tabs %}
{% tab l'utilisation de méthodes %}
Outre les méthodes d'attribut par défaut, vous pouvez également définir des [attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) pour vos utilisateurs. Pour connaître les spécifications complètes de la méthode, consultez [nos JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

{% subtabs local %}
{% subtab String %}
Pour définir un attribut personnalisé avec une valeur `string`:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
Pour définir un attribut personnalisé avec une valeur `integer`:

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

{% endsubtab %}
{% subtab Date %}
Pour définir un attribut personnalisé avec une valeur `date`:

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

{% endsubtab %}
{% subtab Array %}

Vous pouvez avoir jusqu'à 25 éléments dans les tableaux d'attributs personnalisés. Les tableaux individuels définis manuellement (et non détectés automatiquement) pour le **type de données** peuvent être augmentés jusqu'à 100 dans le tableau de bord de Braze, sous **Data Settings** > Custom Attributes. Si vous souhaitez augmenter ce maximum, contactez votre gestionnaire de compte Braze.

Les [tableaux]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays) dépassant le nombre maximum d'éléments seront tronqués pour contenir le nombre maximum d'éléments.

Pour définir un attribut personnalisé avec une valeur `array`:

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

{% alert important %}
Les dates transmises à Braze avec cette méthode doivent être des objets de date JavaScript.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Les clés et les valeurs des attributs personnalisés ne peuvent comporter que 255 caractères au maximum. Pour plus d'informations sur les valeurs valides des attributs personnalisés, reportez-vous à la [documentation de référence](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
Les attributs utilisateur personnalisés ne sont pas disponibles en raison d’une limitation dans la langue de script de Google Tag Manager. Pour enregistrer des attributs personnalisés, créez une balise HTML personnalisée avec le contenu suivant :

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
Le modèle GTM ne prend pas en charge les propriétés imbriquées pour les événements ou les achats. Vous pouvez utiliser le code HTML précédent pour enregistrer les événements ou les achats qui nécessitent des propriétés imbriquées.
{% endalert %}
{% endtab %}
{% endtabs %}

### Désactivation des attributs personnalisés

Pour désactiver un attribut personnalisé, transmettez `null` à la méthode correspondante.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Imbrication d'attributs personnalisés

Vous pouvez également imbriquer des propriétés dans des attributs personnalisés. Dans l'exemple suivant, un objet `favorite_book` avec des propriétés imbriquées est défini comme un attribut personnalisé sur le profil utilisateur. Pour plus de détails, reportez-vous à la section [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
```

### Utiliser l'API REST

Vous pouvez également utiliser notre API REST pour définir ou désactiver les attributs des utilisateurs. Pour plus d'informations, reportez-vous aux [Endpoints de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configurer les abonnements des utilisateurs

Pour configurer un abonnement pour vos utilisateurs (par e-mail ou notification push), appelez les fonctions `setEmailNotificationSubscriptionType()` ou `setPushNotificationSubscriptionType()`, respectivement. Les deux fonctions prennent comme arguments le type `enum` `braze.User.NotificationSubscriptionTypes` . Ce type a trois états différents :

| Statut d’abonnement | Définition |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Inscrit et explicitement abonné |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Inscrit et pas explicitement abonné |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Désinscrit ou explicitement désabonné |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Lorsqu’un utilisateur est enregistré pour les notifications push, le navigateur les force à choisir d’autoriser ou de bloquer les notifications. S’ils choisissent de les autoriser, ils sont définis `OPTED_IN` par défaut. 

Consultez la page [Gestion des abonnements des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) pour plus d'informations sur la mise en œuvre des abonnements et des abonnements explicites.

### Désinscription d'un utilisateur de l'e-mail

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### Désinscription d'un utilisateur du système push

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
