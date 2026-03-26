{% multi_lang_include developer_guide/prerequisites/web.md %}

## Attributs par défaut de l'utilisateur

### Méthodes prédéfinies

Braze fournit des méthodes prédéfinies pour définir les attributs utilisateur suivants dans la [classe `User`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) :

- Prénom
- Nom
- Langue
- Pays
- Date de naissance
- E-mail
- Genre
- Ville d'origine
- Numéro de téléphone

### Définition des attributs par défaut

{% tabs %}
{% tab using methods %}
Pour définir un attribut par défaut pour un utilisateur, appelez la méthode `getUser()` sur votre instance Braze afin d'obtenir une référence à l'utilisateur actuel de votre application. Vous pouvez ensuite appeler des méthodes pour définir un attribut utilisateur.

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

{% tab google tag manager %}
Avec Google Tag Manager, les attributs utilisateur standard (tels que le prénom d'un utilisateur) doivent être enregistrés de la même manière que les attributs utilisateur personnalisés. Assurez-vous que les valeurs que vous transmettez pour les attributs standard correspondent au format attendu spécifié dans la documentation de la [classe User](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

Par exemple, l'attribut genre peut accepter l'une des valeurs suivantes : `"m" | "f" | "o" | "u" | "n" | "p"`. Par conséquent, pour définir le genre d'un utilisateur comme féminin, créez une balise HTML personnalisée avec le contenu suivant :

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### Suppression des attributs par défaut

Pour supprimer un attribut utilisateur par défaut, transmettez `null` à la méthode correspondante. Par exemple :

{% tabs local %}
{% tab First name %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab Gender %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## Attributs utilisateur personnalisés

### Définition des attributs personnalisés

{% tabs %}
{% tab using methods %}
En plus des méthodes d'attributs utilisateur par défaut, vous pouvez également définir des [attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) pour vos utilisateurs. Pour les spécifications complètes des méthodes, consultez [nos JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

{% subtabs local %}
{% subtab String %}
Pour définir un attribut personnalisé avec une valeur de type `string` :

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
Pour définir un attribut personnalisé avec une valeur de type `integer` :

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
Pour définir un attribut personnalisé avec une valeur de type `date` :

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

Le nombre maximum d'éléments par défaut dans un tableau est de 500. Vous pouvez modifier ce nombre maximum dans le tableau de bord de Braze, sous **Paramètres de données** > **Attributs personnalisés**. Les tableaux dépassant le nombre maximum d'éléments sont tronqués pour ne conserver que le nombre maximum d'éléments.


Pour définir un attribut personnalisé avec une valeur de type `array` :

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

{% alert important %}
Les dates transmises à Braze avec cette méthode doivent être des objets Date JavaScript.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Les clés et les valeurs des attributs personnalisés ne peuvent pas dépasser 255 caractères. Pour plus d'informations sur les valeurs d'attributs personnalisés valides, consultez la [documentation de référence](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).
{% endalert %}
{% endtab %}

{% tab google tag manager %}
Les attributs utilisateur personnalisés ne sont pas disponibles en raison d'une limitation du langage de script de Google Tag Manager. Pour enregistrer des attributs personnalisés, créez une balise HTML personnalisée avec le contenu suivant :

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

### Suppression des attributs personnalisés

Pour supprimer un attribut personnalisé, transmettez `null` à la méthode correspondante.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Imbrication d'attributs personnalisés

Vous pouvez également imbriquer des propriétés dans des attributs personnalisés. Dans l'exemple suivant, un objet `favorite_book` avec des propriétés imbriquées est défini comme attribut personnalisé sur le profil utilisateur. Pour plus de détails, consultez la section [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

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

Vous pouvez également utiliser notre API REST pour définir ou supprimer des attributs utilisateur. Pour plus d'informations, consultez les [endpoints de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configuration des abonnements des utilisateurs

Pour configurer un abonnement pour vos utilisateurs (par e-mail ou notification push), appelez respectivement les fonctions `setEmailNotificationSubscriptionType()` ou `setPushNotificationSubscriptionType()`. Ces deux fonctions prennent le type `enum` `braze.User.NotificationSubscriptionTypes` comme argument. Ce type possède trois états différents :

| Statut d'abonnement | Définition |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Abonné et explicitement inscrit |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Abonné, mais pas explicitement inscrit |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Désabonné et/ou explicitement désinscrit |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Lorsqu'un utilisateur est enregistré pour les notifications push, le navigateur l'oblige à choisir d'autoriser ou de bloquer les notifications. S'il choisit de les autoriser, son statut est défini sur `OPTED_IN` par défaut.

Consultez la page [Gestion des abonnements des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) pour plus d'informations sur la mise en œuvre des abonnements et des inscriptions explicites.

### Désabonnement d'un utilisateur des e-mails

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### Désabonnement d'un utilisateur des notifications push

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
