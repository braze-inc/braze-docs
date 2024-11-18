---
nav_title: "Objet Événement"
article_title: Objet Événement de l’API
page_order: 6
page_type: reference
description: "Cet article de référence explique l’objet Événement, ce qu’il est et en quoi il est essentiel dans les stratégies de campagne basées sur les événements."

---

# Objet Événement

> Cet article explique les différents composants d’un objet Événement, comment vous pouvez l’utiliser et des exemples dont vous pouvez vous inspirer.

## Qu’est-ce que l’objet Événement ?

Un objet Événement est un objet qui passe par l’API lorsqu’un événement spécifique se produit. Les objets Événements sont hébergés dans un tableau d’événements. Chaque objet Événement du tableau d’événements représente l’occurrence unique d’un événement personnalisé par un utilisateur particulier à la valeur de temps désignée. L’objet Événement comporte plusieurs champs qui vous permettent de le personnaliser en définissant et en utilisant les propriétés de l’événement dans les messages, la collecte de données et la personnalisation.

Vous pouvez vérifier comment mettre en place des événements personnalisés pour une plateforme spécifique en vous référant au Guide d'intégration des plateformes dans le [Guide du développeur][1]. Vous trouverez ces informations dans la page **Suivi des événements personnalisés** sous l'onglet **Analyse des** différentes plateformes. Nous en avons associé plusieurs pour vous.

Article sur le suivi des événements personnalisés :

- [Android][2]
- [iOS][3]
- [Web][4]

### Corps de l’objet

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  "name" : (required, string) the name of the event,
  "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
  // See following notes regarding anonymous push token imports
}
```

- [ID utilisateur externe]({{site.baseurl}}/api/basics/#user-ids)
- [Identifiant d’application]({{site.baseurl}}/api/identifier_types/)
- [Code temporel ISO 8601][22]

#### Mettre à jour les profils existants uniquement

Si vous souhaitez mettre à jour uniquement les profils utilisateur existants dans Braze, vous devez passer la clé `_update_existing_only` avec la valeur `true` dans le corps de votre demande. Si cette valeur est omise, Braze créera un nouveau profil utilisateur si `external_id` n’existe pas déjà.

{% alert note %}
Si vous créez un profil utilisateur alias uniquement via l'endpoint `/users/track`, `_update_existing_only` doit être défini sur `false`. Si cette valeur est omise, le profil alias uniquement ne sera pas créé.
{% endalert %}

## Objet de propriétés de l’événement
Les événements et achats personnalisés peuvent avoir des propriétés d’événement. Les valeurs des « Properties (Propriétés) » doivent être un objet dont les clés sont les noms de propriétés et les valeurs sont les valeurs de propriété. Les noms de propriété doivent être des chaînes de caractères non vides de moins de 255 caractères, qui ne commencent pas par un symbole de dollar ($).

Les valeurs de propriété peuvent être l’un des types de données suivants :

| Type de données | Description |
| --- | --- |
| Chiffres | Sous forme d'[entiers](https://en.wikipedia.org/wiki/Integer) ou de [float](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booléens | `true` ou `false` |
| Datetimes | Formatés sous forme de chaînes de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Non pris en charge dans les tableaux. |
| Chaînes de caractères | 255 caractères ou moins. |
| Tableaux | Les tableaux ne peuvent pas inclure des dates/horodatages. |
| Objets | Les objets seront ingérés en tant que chaînes de caractères. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les objets de propriété d'événement qui contiennent des valeurs de tableau ou d'objet peuvent avoir une charge utile de propriété d'événement allant jusqu'à 50 Ko.

### Persistance des propriétés de l’événement
Les propriétés de l’événement sont conçues pour filtrer et personnaliser avec Liquid les messages déclenchés par leurs événements parents. Par défaut, elles ne sont pas persistantes sur le profil utilisateur Braze. Pour utiliser les valeurs des propriétés d'événement dans la segmentation, reportez-vous aux [événements personnalisés][5], qui détaillent les différentes approches de stockage à long terme des valeurs des propriétés d'événement.

#### Demande d’exemple d’événement

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:30+01:00"
    },
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "rented_movie",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:50+01:00"
    }
  ]
}
```
- [ISO 8601 Time Code Wiki][22]

## Objets Événement

À l’aide de l’exemple fourni, nous pouvons voir que quelqu’un a regardé une bande-annonce récemment, puis a loué un film. Bien que nous ne puissions pas accéder à une campagne et segmenter les utilisateurs en fonction de ces propriétés, nous pouvons utiliser ces propriétés stratégiquement en les exploitant sous forme de reçu, pour envoyer un message personnalisé via un canal grâce à Liquid. Par exemple, "Hello **Beth**, Thanks for renting **The Sad Egg** by **Dan Alexander**, here are some recommended movies based on your rental..." (Bonjour **Beth**, Merci d'avoir loué **The Sad Egg** de **Dan Alexander**, voici quelques films recommandés en fonction de votre location).


[1]: {{site.baseurl}}/developer_guide/home/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Time Code Wiki"
[21]: {{site.baseurl}}/api/api_key/#the-app-identifier-api-key
[22]: https://en.wikipedia.org/wiki/ISO_8601 "Code temporel ISO 8601"
[23]: {{site.baseurl}}/api/basics/#external-user-id-explanation
