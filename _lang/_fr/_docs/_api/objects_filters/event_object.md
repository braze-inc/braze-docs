---
nav_title: "Objet de l'événement"
article_title: Objet événement API
page_order: 6
page_type: Référence
description: "Cet article de référence dépasse l'objet événementiel, ce qu'il est, et comment il est un élément crucial des stratégies de campagne basées sur des événements."
---

# Spécification de l'objet événement

> Cet article explique les différents composants d'un objet événementiel, comment vous pouvez utiliser cet objet, et des exemples à dessiner.

## Qu'est-ce que l'objet événement ?

Un objet Event Object est un objet qui passe à travers l'API lorsqu'un événement spécifique se produit. Les objets d'événements sont logés dans un tableau d'événements. Chaque objet événement dans le tableau des événements représente une seule occurrence d'un événement personnalisé par un utilisateur particulier à la valeur horaire désignée. L'objet événement a de nombreux champs différents qui vous permettent de personnaliser en définissant et en utilisant les propriétés d'événement dans les messages, la collecte de données et la personnalisation.

Vous pouvez voir comment configurer des événements personnalisés pour une plate-forme spécifique en lisant le Guide d'intégration de la plateforme dans le [Guide du développeur][1]. Vous pouvez trouver ces informations dans la page **Événements personnalisés de suivi** sous l'onglet __Analytiques__ des différentes plateformes. Nous en avons lié plusieurs pour vous.

- Suivi des événements personnalisés : <br>[Android][2]<br>[iOS][3]<br>[Web][4]

### Objet événement

```json
{
  // Un de "external_id" ou "user_alias" ou "braze_id" est requis
  "external_id" : (optionnel, string), ID d'utilisateur externe,
  "user_alias" : (optionnel, User Alias Object), User Alias Object,
  "braze_id" : (facultatif, string) Braze User Identifier,
  "app_id" : (optionnel, chaîne) voir App Identifier ci-dessous,
  "nome" : (obligatoire, chaîne) le nom de l'événement,
  "temps" : (requis, datetime en tant que chaîne au format ISO 8601 ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`),
  "properties" : (optionnel, Propriétés de l'objet Propriétés) de l'événement
  // Définir ce drapeau à true mettra l'API en mode "Mise à jour uniquement".
  // Lorsque vous utilisez un "user_alias", le mode "Update only" est toujours vrai.
  "_update_existing_only" : (optionnel, booléen)
  // Voir la note ci-dessous concernant les importations de jetons de poussage anonymes
}
```

- [ISO 8601 Time Code Wiki][22]
- [App Identifier][21]

#### Mettre à jour les profils existants uniquement

Si vous souhaitez mettre à jour uniquement les profils d'utilisateurs existants au Brésil, vous devez passer la clé `_update_existing_only` avec une valeur de `true` dans le corps de votre requête. Si cette valeur est omise, Braze créera un nouveau profil utilisateur si le `external_id` n'existe pas déjà.

{% alert note %}
Si vous créez un profil utilisateur uniquement en tant qu'alias via le point de terminaison utilisateur/piste, `_update_existing_only` doit être défini à `false`. Si cette valeur est omise, le profil des alias ne sera pas créé.
{% endalert %}

## Propriétés de l'événement
Les événements personnalisés et les achats peuvent avoir des propriétés d'événement. Les valeurs « propriétés » doivent être un objet où les clés sont les noms de propriété et les valeurs sont les valeurs de la propriété. Les noms de propriété doivent être des chaînes de caractères non vides inférieures ou égales à 255 caractères, sans signe de dollars ($).

Les valeurs de la propriété peuvent être l'un des types de données suivants :

| Type de données       | Libellé                                                                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Numéros               | En tant que [entiers](https://en.wikipedia.org/wiki/Integer) ou [flottent](https://en.wikipedia.org/wiki/Floating-point_arithmetic)                            |
| Booléens              |                                                                                                                                                                |
| Datetimes             | Formaté en tant que chaînes au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'H:mm:ss:SSSZ`. Non pris en charge dans les tableaux. |
| Chaînes de caractères | 255 caractères ou moins.                                                                                                                                       |
| Tableaux              | Les tableaux ne peuvent pas inclure les dates.                                                                                                                 |
| Objets                | Les objets seront ingérés en tant que chaînes.                                                                                                                 |
{: .reset-td-br-1 .reset-td-br-2}

Les objets de propriété événement qui contiennent des valeurs de tableau ou d'objet peuvent avoir une charge utile de propriété événement allant jusqu'à 50 Ko.

### Propriété événement persistance
Les propriétés d'événement sont conçues pour le filtrage des messages et la personnalisation de Liquid déclenchés par leurs événements parents. Par défaut, ils ne sont pas persistés sur le profil utilisateur de Braze. Pour utiliser les valeurs des propriétés d'événement dans la segmentation, veuillez consulter notre [documentation sur les événements personnalisés][5] qui détaille les différentes approches pour stocker les propriétés d'événement à long terme.

#### Demande d'exemple d'événement

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "votre-app-id",
      "nome" : "watched_trailer",
      "temps" : "2013-07-16T19:20:30+01:00"
    },
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "rented_movie",
      "temps" : "2013-07-16T19:20:45+01:00",
      "propriétés": {
        "movie": "Le Oeuf Sad",
        "directeur": "Dan Alexander"
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "temps" : "2013-07-16T19:20:50+01:00"
    }
  ]
}
```
- [ISO 8601 Time Code Wiki][19]

## Objets d'événement

En utilisant l'exemple fourni ci-dessus, nous pouvons voir que quelqu'un a regardé une remorque récemment, puis loué un film. Bien que nous ne puissions pas entrer dans une campagne et segmenter les utilisateurs en fonction de ces propriétés, nous pouvons utiliser ces propriétés stratégiquement en les utilisant sous la forme d'un reçu, pour envoyer un message personnalisé via un canal à l'aide de Liquid. Par exemple, "Bonjour __Beth__, Merci de louer __L'Oeuf Sad__ par __Dan Alexander__, Voici quelques films recommandés en fonction de votre location..."


[1]: {{site.baseurl}}/developer_guide/home/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Time Code Wiki"
[21]: {{site.baseurl}}/api/api_key/#the-app-identifier-api-key
[22]: https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Time Code"