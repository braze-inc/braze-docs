{% multi_lang_include developer_guide/prerequisites/roku.md %}

## Attributs par défaut de l’utilisateur

### Méthodes prédéfinies

Braze propose des méthodes prédéfinies pour définir les attributs utilisateur suivants à l'aide de l'objet `m.Braze`.

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

### Définition des attributs par défaut

Pour définir un attribut par défaut, appelez la méthode correspondante sur l'objet `m.Braze`.

{% tabs local %}
{% tab Prénom %}
```brightscript
m.Braze.setFirstName("Alex")
```
{% endtab %}
{% tab Nom de famille %}
```brightscript
m.Braze.setLastName("Smith")
```
{% endtab %}
{% tab E-mail %}
```brightscript
m.Braze.setEmail("alex@example.com")
```
{% endtab %}
{% tab Genre %}
```brightscript
m.Braze.setGender("m") ' Accepts: "m", "f", "o", "n", "u", "p"
```
{% endtab %}
{% tab Date de naissance %}
```brightscript
m.Braze.setDateOfBirth(1990, 5, 15) ' Year, month, day
```
{% endtab %}
{% tab Pays %}
```brightscript
m.Braze.setCountry("United States")
```
{% endtab %}
{% tab Langue %}
```brightscript
m.Braze.setLanguage("en")
```
{% endtab %}
{% tab Ville d'origine %}
```brightscript
m.Braze.setHomeCity("New York")
```
{% endtab %}
{% tab Numéro de téléphone %}
```brightscript
m.Braze.setPhoneNumber("+1234567890")
```
{% endtab %}
{% endtabs %}

## Attributs utilisateur personnalisés

Outre les attributs par défaut, Braze vous permet de définir des attributs personnalisés à l'aide de différents types de données.

### Définition des attributs personnalisés

{% tabs %}
{% tab Chaîne de caractères %}
Pour donner à un attribut personnalisé une valeur `string`:

```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}

{% tab Entier %}
Pour définir un attribut personnalisé avec une valeur `integer`:

```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}

{% tab Points flottants %}
Braze traite les valeurs `float` et `double` exactement de la même manière. Pour définir un attribut personnalisé avec l'une ou l'autre valeur :

```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
{% endtab %}

{% tab Booléen %}
Pour définir un attribut personnalisé avec une valeur `boolean`:

```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}

{% tab Date %}
Pour définir un attribut personnalisé avec une valeur `date`:

```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}

{% tab Réseau %}
Pour définir un attribut personnalisé avec une valeur `array`:

```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

{% alert important %}
Les valeurs d’attribut personnalisé ont une longueur maximale de 255 caractères ; les valeurs plus longues seront tronquées.
{% endalert %}

### Incrémentation et décrémentation des attributs personnalisés

Ce code est un exemple d’incrémentation d’un attribut personnalisé. Vous pouvez augmenter la valeur d’un attribut personnalisé par une valeur entière positive ou négative.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Désactivation des attributs personnalisés

Pour désactiver un attribut personnalisé, transmettez la clé de l'attribut concerné à la méthode `unsetCustomAttribute`.

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### Utiliser l'API REST

Vous pouvez également utiliser notre API REST pour définir ou désactiver les attributs des utilisateurs. Pour plus d'informations, reportez-vous aux [Endpoints de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Définir des inscriptions par e-mail

Vous pouvez définir les statuts d’abonnement aux e-mails suivants pour vos utilisateurs par programmation via le SDK.

| Statut d’abonnement | Définition |
| ------------------- | ---------- |
| `OptedIn` | Inscrit et explicitement abonné |
| `Subscribed` | Inscrit et pas explicitement abonné |
| `UnSubscribed` | Désinscrit ou explicitement désabonné |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Ces types tombent dans la catégorie `BrazeConstants().SUBSCRIPTION_STATES`.
{% endalert %}

La méthode de définition du statut d’abonnement aux e-mails est `setEmailSubscriptionState()`. Les utilisateurs seront définis sur `Subscribed` automatiquement dès réception d’une adresse e-mail valide. Cependant, nous vous suggérons d’établir un processus d’abonnement explicite et de définir cette valeur sur `OptedIn` dès réception du consentement explicite de votre utilisateur. Pour plus de détails, consultez la page [Gestion des abonnements des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```
