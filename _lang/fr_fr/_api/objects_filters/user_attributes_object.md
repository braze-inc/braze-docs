---
nav_title: "Objet Attributs d'utilisateur"
article_title: Objet Attributs d'utilisateur de l'API
page_order: 11
page_type: reference
description: "Cet article de référence explique les différents composants de l'objet Attributs d'utilisateur."

---

# Objet Attributs d'utilisateur

> Une requête API contenant des champs dans l'objet attributes crée ou met à jour un attribut de ce nom avec la valeur indiquée dans le profil utilisateur spécifié.

Utilisez les noms de champs de profil utilisateur Braze (énumérés ci-après ou tout autre répertorié dans la section [Champs de profil utilisateur Braze](#braze-user-profile-fields)) pour mettre à jour ces valeurs spéciales sur le profil utilisateur dans le tableau de bord, ou ajoutez vos propres données d'attributs personnalisés à l'utilisateur.

## Corps de l'objet

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" defaults to true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean),
  // Braze User Profile Fields
  "first_name" : "Jon",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
}
```

- [ID utilisateur externe]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Alias d'utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)

Pour supprimer un attribut de profil, définissez-le sur `null`. Certains champs, tels que `external_id` et `user_alias`, ne peuvent pas être supprimés après avoir été ajoutés à un profil utilisateur.

#### Résolution des identifiants

À moins que vous n'effectuiez une [importation anonyme de jetons de notification push](#push-token-import), chaque objet d'attributs utilisateur doit inclure au moins un identifiant : `external_id`, `user_alias`, `braze_id`, `email` ou `phone`. Dans la mesure du possible, incluez un seul identifiant par objet afin d'éviter toute ambiguïté quant au profil utilisateur mis à jour ou créé.

Gardez les points suivants à l'esprit lors de l'utilisation d'identifiants :

- **`external_id` et `user_alias` sont mutuellement exclusifs.** L'inclusion des deux dans le même objet d'attributs utilisateur renvoie une erreur. Pour ajouter un alias à un utilisateur qui possède déjà un `external_id`, utilisez l'[endpoint `/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/).
- **`email` a priorité sur `phone`.** Si `email` et `phone` sont tous deux inclus dans le même objet, Braze utilise `email` comme identifiant. Cela signifie que les attributs sont appliqués au profil utilisateur associé à cette adresse e-mail, même si le numéro de téléphone appartient à un profil différent.

{% alert important %}
Afin d'éviter tout comportement inattendu, utilisez un seul identifiant par objet d'attributs utilisateur. Fournir plusieurs identifiants qui renvoient à différents profils utilisateurs peut entraîner l'application d'attributs au mauvais profil.
{% endalert %}

#### Mettre à jour les profils existants uniquement

Si vous souhaitez mettre à jour uniquement les profils utilisateur existants dans Braze, vous devez passer la clé `_update_existing_only` avec la valeur `true` dans le corps de votre requête. Si cette valeur est omise, Braze crée un nouveau profil utilisateur si l'`external_id` n'existe pas encore.

{% alert note %}
Si vous créez un profil utilisateur avec alias uniquement via l'endpoint `/users/track`, vous devez définir `_update_existing_only` sur `false`. Si vous omettez cette valeur, Braze ne créera pas le profil contenant uniquement un alias.
{% endalert %}

#### Importation de jetons de notification push

Avant d'importer des jetons de notification push dans Braze, vérifiez si cela est nécessaire. Lorsque les SDK de Braze sont mis en place, ils gèrent automatiquement les jetons de notification push sans qu'il soit nécessaire de les télécharger via l'API.

Si vous devez les télécharger via l'API, vous pouvez le faire pour des utilisateurs identifiés ou anonymes. Cela signifie que soit un `external_id` doit être présent, soit les utilisateurs anonymes doivent avoir l'indicateur `push_token_import` défini sur `true`.

{% alert note %}
Lors de l'importation de jetons de notification push provenant d'autres systèmes, un `external_id` n'est pas toujours disponible. Pour maintenir la communication avec ces utilisateurs pendant votre transition vers Braze, vous pouvez importer les jetons existants pour les utilisateurs anonymes sans fournir d'`external_id`, en spécifiant `push_token_import` comme `true`.
{% endalert %}

Lorsque vous indiquez `push_token_import` comme `true` :

* `external_id` et `braze_id` **ne** doivent **pas** être spécifiés
* L'objet d'attribut **doit** contenir un jeton de notification push
* Si le jeton existe déjà dans Braze, la requête est ignorée ; dans le cas contraire, Braze crée un profil utilisateur temporaire et anonyme pour chaque jeton afin de vous permettre de continuer à envoyer des messages à ces personnes.

Après l'importation, lorsque chaque utilisateur lance la version de votre application compatible avec Braze, Braze transfère automatiquement son jeton de notification push importé vers son profil utilisateur Braze et supprime le profil temporaire.

Braze effectue une vérification mensuelle afin d'identifier tout profil anonyme marqué de l'indicateur `push_token_import` et ne disposant pas de jeton de notification push. Si le profil anonyme ne dispose plus d'un jeton de notification push, Braze supprime le profil. Toutefois, si le profil anonyme dispose toujours d'un jeton de notification push, ce qui indique que l'utilisateur réel ne s'est pas encore connecté à l'appareil avec ledit jeton, Braze ne prend aucune mesure.

Pour plus d'informations, consultez [Migration des jetons de notification push](#migrating-push-tokens).

#### Types de données des attributs personnalisés

Les types de données suivants peuvent être stockés en tant qu'attribut personnalisé :

| Type de données | Remarques |
| --- | --- |
| Tableaux | Les tableaux d'attributs personnalisés sont pris en charge. Lorsque vous ajoutez un élément, il est ajouté à la fin du tableau. Si l'élément existe déjà, il est déplacé de sa position actuelle vers la fin.<br><br>Seules les valeurs uniques sont enregistrées. Par exemple, l'importation de `['hotdog','hotdog','hotdog','pizza']` donne `['hotdog', 'pizza']`.<br><br>Vous pouvez définir un tableau directement (par exemple, `"my_array_custom_attribute":[ "Value1", "Value2" ]`), ajouter des éléments à un tableau existant avec `"my_array_custom_attribute" : { "add" : ["Value3"] }`, ou supprimer des valeurs avec `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`.<br><br>Le nombre maximum d'éléments par défaut est de 500 par tableau. Vous pouvez modifier le nombre maximum d'éléments dans le tableau de bord de Braze, sous **Paramètres des données** > **Attributs personnalisés**. Pour plus d'informations, consultez la section [Tableaux]({{site.baseurl}}/developer_guide/analytics/#arrays). |
| Tableau d'objets | Utilisez un tableau d'objets pour définir une liste d'objets où chaque objet contient un ensemble d'attributs. Utilisez ce type pour stocker plusieurs ensembles de données associées à un utilisateur, telles que les séjours à l'hôtel, l'historique des achats ou les préférences. <br><br>Par exemple, définissez un attribut personnalisé nommé `hotel_stays` sur un profil utilisateur sous forme de tableau où chaque objet représente un séjour distinct, avec des attributs tels que `hotel_name`, `check_in_date` et `nights_stayed`. Pour plus de détails, consultez l'[exemple de tableau d'objets](#array-of-objects-example). |
| Booléens | `true` ou `false` |
| Dates | Enregistrez les dates au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) ou dans l'un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Notez que le « T » est un indicateur de temps, et non une marque substitutive. Il ne doit pas être modifié ou supprimé. <br><br>Les attributs temporels sans fuseau horaire sont définis par défaut à minuit UTC (et sont formatés sur le tableau de bord comme l'équivalent de minuit UTC dans le fuseau horaire de l'entreprise). <br><br>Les événements dont l'horodatage est défini dans le futur sont automatiquement réglés sur l'heure actuelle. <br><br>Pour les attributs personnalisés standard, si l'année est inférieure à 0 ou supérieure à 3000, Braze enregistre la valeur sous forme de chaîne de caractères dans le profil utilisateur. |
| Floats | Les attributs personnalisés de type float sont des nombres positifs ou négatifs avec une virgule. Par exemple, vous pouvez utiliser des floats pour stocker des soldes de comptes ou des évaluations de produits ou de services par les utilisateurs. |
| Entiers | Vous pouvez incrémenter des attributs personnalisés de type entier en assignant un objet avec le champ « inc » et la valeur à ajouter. <br><br>Exemple : `"my_custom_attribute_2" : {"inc" : int_value},`|
| Attributs personnalisés imbriqués | Les attributs personnalisés imbriqués définissent un ensemble d'attributs en tant que propriété d'un autre attribut. Lorsque vous définissez un objet d'attribut personnalisé, vous ajoutez un ensemble d'attributs à cet objet. Pour plus d'informations, consultez la section [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/). |
| Chaînes de caractères | Les attributs personnalisés de type chaîne sont des séquences de caractères utilisées pour stocker des données textuelles. Par exemple, vous pouvez utiliser des chaînes de caractères pour stocker les noms et prénoms, les adresses e-mail ou les préférences. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Pour savoir quand utiliser un événement personnalisé plutôt qu'un attribut personnalisé, consultez les sections [Événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) et [Attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).
{% endalert %}

##### Exemple de tableau d'objets

Ce tableau d'objets vous permet de créer des segments en fonction de critères spécifiques au sein des séjours et de personnaliser vos messages à l'aide des données de chaque séjour grâce aux modèles Liquid.

```json
{"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
]}
```

#### Champs de profil utilisateur Braze {#braze-user-profile-fields}

{% alert important %}
Les champs de profil utilisateur suivants sont sensibles à la casse. Veillez à les référencer en minuscules.
{% endalert %}

| Champ de profil utilisateur | Spécification du type de données |
| ---| --- |
| alias_name | (string) |
| alias_label | (string) |
| braze_id | (chaîne de caractères, facultatif) Lorsqu'un profil utilisateur est reconnu par le SDK, un profil utilisateur anonyme est créé avec un `braze_id` associé. Le `braze_id` est automatiquement attribué par Braze, ne peut pas être modifié et est spécifique à l'appareil. |
| country | (chaîne de caractères) Nous exigeons que les codes de pays soient transmis à Braze selon la [norme ISO-3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1). Notre API s'efforce de mapper les pays reçus dans différents formats. Par exemple, « Australia » peut correspondre à « AU ». Toutefois, si la saisie ne correspond pas à une [norme ISO-3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1) donnée, la valeur du pays est définie sur `NULL`. <br><br>La définition de `country` sur un utilisateur par importation CSV ou API empêche Braze de capturer automatiquement cette information via le SDK. |
| current_location | (objet) De la forme {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (date à laquelle l'utilisateur a utilisé l'application pour la première fois) Chaîne de caractères au format ISO 8601 ou dans l'un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (date à laquelle l'utilisateur a utilisé l'application pour la dernière fois) Chaîne de caractères au format ISO 8601 ou dans l'un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | (date de naissance) Chaîne au format « AAAA-MM-JJ », par exemple, 1980-12-21. |
| email | (string) |
| email_subscribe | (chaîne de caractères) Les valeurs disponibles sont « opted_in » (explicitement inscrit pour recevoir des e-mails), « unsubscribed » (explicitement désabonné des e-mails) et « subscribed » (ni inscrit ni désabonné).  |
| email_open_tracking_disabled |(booléen) `true` ou `false` accepté. Définissez sur `true` pour désactiver l'ajout du pixel de suivi des ouvertures dans tous les futurs e-mails envoyés à cet utilisateur. Disponible uniquement pour SparkPost et Sendgrid.|
| email_click_tracking_disabled |(booléen) `true` ou `false` accepté. Définissez sur `true` pour désactiver le suivi des clics pour tous les liens contenus dans les futurs e-mails envoyés à cet utilisateur. Disponible uniquement pour SparkPost et Sendgrid.|
| external_id | (chaîne de caractères) Identifiant unique pour un profil utilisateur. Une fois un `external_id` attribué, Braze identifie le profil utilisateur sur l'ensemble des appareils de l'utilisateur. Lors de la première attribution d'un external_id à un profil utilisateur inconnu, Braze migre toutes les données existantes du profil utilisateur vers le nouveau profil. |
| facebook | hachage contenant l'un des éléments suivants : `id` (string), `likes` (tableau de chaînes de caractères), `num_friends` (integer). |
| first_name | (string) |
| gender | (chaîne de caractères) « M », « F », « O » (autre), « N » (sans objet), « P » (préfère ne pas dire) ou nil (inconnu). |
| home_city | (string) |
| language | (chaîne de caractères) Nous exigeons que la langue soit transmise à Braze selon la [norme ISO-639-1](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). Pour connaître les langues prises en charge, consultez notre [liste des langues acceptées]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/).<br><br>La définition de `language` sur un utilisateur par importation CSV ou API empêche Braze de capturer automatiquement cette information via le SDK. |
| last_name | (string) |
| marked_email_as_spam_at | (chaîne de caractères) Date à laquelle l'e-mail de l'utilisateur a été marqué comme courrier indésirable. Apparaît au format ISO 8601 ou dans l'un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| phone | (chaîne de caractères) Nous recommandons de fournir les numéros de téléphone au format [E.164](https://en.wikipedia.org/wiki/E.164). Pour plus de détails, consultez la section [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting).|
| push_subscribe | (chaîne de caractères) Les valeurs disponibles sont « opted_in » (explicitement inscrit pour recevoir des notifications push), « unsubscribed » (explicitement désabonné des notifications push) et « subscribed » (ni inscrit ni désabonné).  |
| push_tokens | Tableau d'objets avec `app_id` et la chaîne de caractères `token`. Vous pouvez éventuellement fournir un `device_id` pour l'appareil auquel ce jeton est associé, par exemple, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Si aucun `device_id` n'est fourni, un identifiant est généré de manière aléatoire. |
| subscription_groups| Tableau d'objets avec les chaînes de caractères `subscription_group_id` et `subscription_state`, par exemple, `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Les valeurs disponibles pour `subscription_state` sont « subscribed » et « unsubscribed ».|
| time_zone | (chaîne de caractères) Nom du fuseau horaire provenant de la [base de données des fuseaux horaires de l'IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (par exemple, « America/New_York » ou « Eastern Time (US & Canada) »). Seules les valeurs de fuseau horaire valides sont définies. |
| twitter | Hachage contenant l'un des éléments suivants : `id` (integer), `screen_name` (chaîne de caractères, identifiant X (anciennement Twitter)), `followers_count` (integer), `friends_count` (integer), `statuses_count` (integer). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les paramètres linguistiques explicitement définis via cette API ont priorité sur les informations régionales que Braze reçoit automatiquement de l'appareil.

####  Exemple de requête d'attributs utilisateur

Cet exemple contient quatre objets d'attributs utilisateur, sur un total de 75 objets d'attributs autorisés par appel API.

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes" : [
    {
      "external_id" : "user1",
      "first_name" : "Jon",
      "has_profile_picture" : true,
      "dob": "1988-02-14",
      "music_videos_favorited" : { "add" : [ "calvinharris-summer" ], "remove" : ["nickiminaj-anaconda"] }
    },
    {
      "external_id" : "user2",
      "first_name" : "Jill",
      "has_profile_picture" : false,
      "push_tokens": [{"app_id": "Your App Identifier", "token": "abcd", "device_id": "optional_field_value"}]

    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "first_name" : "Alice",
      "has_profile_picture" : false
    },
    {
      "external_id": "user3",
      "subscription_groups" : [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]
    }
  ]
}
```

## Migration des jetons de notification push

Si vous envoyiez des notifications push avant d'intégrer Braze, que ce soit par vous-même ou via un autre fournisseur, la migration des jetons de notification push vous permet de continuer à envoyer des notifications push à vos utilisateurs disposant de jetons enregistrés.

### Migration automatique via le SDK

Une fois [le SDK Braze intégré]({{site.baseurl}}/developer_guide/sdk_integration/), les jetons de notification push de vos utilisateurs abonnés sont automatiquement migrés lors de leur prochaine ouverture de l'application. Jusqu'à ce moment-là, il n'est pas possible d'envoyer des notifications push à ces utilisateurs via Braze.

Vous pouvez également [migrer vos jetons de notification push manuellement](#manual-migration-via-api), ce qui vous permet de réengager vos utilisateurs plus rapidement.

#### Considérations relatives aux jetons Web

En raison de la nature des jetons de notification push pour le Web, tenez compte des éléments suivants lors de la mise en œuvre du push pour le Web :

|Considération|Détails|
|----------------------|------------|
| **Service de traitement**  | Par défaut, le SDK Web recherche un service de traitement à l'adresse `./service-worker`, à moins qu'une autre option ne soit spécifiée, telle que `manageServiceWorkerExternally` ou `serviceWorkerLocation`. Si votre service de traitement n'est pas configuré correctement, les jetons de notification push de vos utilisateurs risquent d'expirer. |
| **Jetons expirés**   | Si un utilisateur n'a pas démarré de session Web dans les 60 jours, son jeton de notification push expire. Étant donné que Braze ne peut pas migrer les jetons expirés, vous devez envoyer un [message push d'amorce]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages) pour les réengager. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Migration manuelle via l'API

La migration manuelle des jetons de notification push consiste à importer ces clés précédemment créées dans votre plateforme Braze via l'API.

Migrez par programmation les jetons iOS (APNs) et Android (FCM) vers votre plateforme en utilisant l'[endpoint `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Vous pouvez migrer à la fois les utilisateurs identifiés (utilisateurs avec un ID externe associé) et les utilisateurs anonymes (utilisateurs sans ID externe).

Spécifiez l'`app_id` de votre application lors de la migration des jetons de notification push pour associer le jeton approprié à l'application correspondante. Chaque application (iOS, Android, etc.) possède son propre `app_id`, disponible dans la section **Identification** de la page [Clés API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). Assurez-vous d'utiliser le bon `app_id` pour chaque plateforme.

{% alert important %}
Il n'est pas possible de migrer les jetons de notification push Web via l'API. En effet, les jetons de notification push Web n'utilisent pas le même schéma que les autres plateformes.

<br>Si vous tentez de migrer des jetons de notification push Web par programmation, une erreur semblable à celle-ci peut s'afficher : `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
En guise d'alternative à la migration via l'API, nous vous recommandons d'intégrer le SDK et de permettre à votre base de jetons de se reconstituer naturellement.
{% endalert %}

{% tabs local %}
{% tab External ID present %}
Pour les utilisateurs identifiés, définissez l'indicateur `push_token_import` sur `false` (ou omettez le paramètre) et spécifiez les valeurs `external_id`, `app_id` et `token` dans l'objet `attributes` utilisateur.

Par exemple :

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab External ID missing %}
Lors de l'importation de jetons de notification push provenant d'autres systèmes, un `external_id` n'est pas toujours disponible. Dans ce cas, définissez votre indicateur `push_token_import` sur `true` et spécifiez les valeurs `app_id` et `token`. Braze crée un profil utilisateur temporaire et anonyme pour chaque jeton afin de vous permettre de continuer à envoyer des messages à ces personnes. Si le jeton existe déjà dans Braze, la requête est ignorée.

Par exemple :

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [
    {
      "push_token_import" : true,
      "email": "braze.test1@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },

    {
      "push_token_import" : true,
      "email": "braze.test2@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    }
  ]
}'
```

Après l'importation, lorsque l'utilisateur anonyme lance la version de votre application compatible avec Braze, Braze transfère automatiquement son jeton de notification push importé vers son profil utilisateur Braze et supprime le profil temporaire.

Braze effectue une vérification mensuelle afin d'identifier tout profil anonyme marqué de l'indicateur `push_token_import` et ne disposant pas de jeton de notification push. Si le profil anonyme ne dispose plus d'un jeton de notification push, Braze supprime le profil. Toutefois, si le profil anonyme dispose toujours d'un jeton de notification push, ce qui indique que l'utilisateur réel ne s'est pas encore connecté à l'appareil avec ledit jeton, Braze ne prend aucune mesure.
{% endtab %}
{% endtabs %}

### Importation de jetons de notification push Android

{% alert important %}
La remarque suivante s'applique uniquement aux applications Android. Les applications iOS ne nécessitent pas ces étapes, car cette plateforme ne dispose que d'un seul framework pour l'affichage des notifications push, et celles-ci s'affichent immédiatement dès lors que Braze dispose des jetons et certificats de notification push nécessaires.
{% endalert %}

Si vous devez envoyer des notifications push Android à vos utilisateurs avant que l'intégration du SDK Braze ne soit terminée, utilisez des paires clé-valeur pour valider les notifications push.

Vous devez disposer d'un récepteur pour gérer et afficher les charges utiles de notification push. Pour notifier le récepteur de la charge utile, ajoutez les paires clé-valeur nécessaires à la campagne push. Les valeurs de ces paires dépendent du partenaire push spécifique que vous utilisiez avant Braze.

{% alert note %}
Pour certains fournisseurs de notifications push, Braze doit aplatir les paires clé-valeur afin qu'elles puissent être correctement interprétées. Pour aplatir les paires clé-valeur d'une application Android spécifique, contactez votre Customer Success Manager.
{% endalert %}