---
nav_title: "Objet Attributs d’utilisateur"
article_title: Objet Attributs d’utilisateur de l’API
page_order: 11
page_type: reference
description: "Cet article de référence explique les différents composants de l’objet Attributs d’utilisateur."

---

# Objet Attributs d’utilisateur

> Une requête API contenant des champs dans l'objet attributes crée ou met à jour un attribut de ce nom avec la valeur indiquée dans le profil utilisateur spécifié.

Utilisez les noms de champs de profil utilisateur Braze (énumérés comme suit ou tout autre répertorié dans la section pour [Braze user profile fields](#braze-user-profile-fields)) pour mettre à jour ces valeurs spéciales sur le profil utilisateur dans le tableau de bord ou ajoutez vos propres données d'attributs personnalisés à l'utilisateur.

## Corps de l’objet

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
- [Alias utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)

Pour supprimer un attribut de profil, définissez-le sur `null`. Certains champs, tels que `external_id` et `user_alias`, ne peuvent pas être supprimés après avoir été ajoutés à un profil utilisateur.

#### Résolution des identifiants

À moins que vous n'effectuiez une [importation anonyme de jetons push](#push-token-import), chaque objet d'attributs utilisateur doit inclure au moins un identifiant : `external_id`,`user_alias` `braze_id`, `email`, ou `phone`. Dans la mesure du possible, veuillez inclure un seul identifiant par objet afin d'éviter toute ambiguïté quant au profil utilisateur en cours de mise à jour ou de création.

Veuillez garder à l'esprit les points suivants lors de l'utilisation d'identifiants :

- **`external_id` et`user_alias`sont mutuellement exclusifs.** L'inclusion des deux dans le même objet d'attributs utilisateur renvoie une erreur. Pour ajouter un alias à un utilisateur qui en possède déjà un`external_id`, veuillez utiliser [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/)l'[endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/).
- **`email` a priorité sur`phone`.** Si les`email`deux`phone`sont inclus dans le même objet, Braze utilise`email`comme identifiant. Cela signifie que les attributs sont appliqués au profil utilisateur associé à cette adresse e-mail, même si le numéro de téléphone appartient à un profil différent.

{% alert important %}
Afin d'éviter tout comportement inattendu, veuillez utiliser un seul identifiant par objet d'attributs utilisateur. Fournir plusieurs identifiants qui renvoient à différents profils utilisateurs peut entraîner l'application d'attributs au mauvais profil.
{% endalert %}

#### Mettre à jour les profils existants uniquement

Si vous souhaitez mettre à jour uniquement les profils utilisateur existants dans Braze, vous devez passer la clé `_update_existing_only` avec la valeur `true` dans le corps de votre demande. Si cette valeur est omise, Braze crée un nouveau profil utilisateur si celui-ci`external_id`n'existe pas encore.

{% alert note %}
Si vous créez un profil utilisateur avec alias uniquement via `/users/track`l'endpoint, il est nécessaire de définir`_update_existing_only`sur `false`. Si vous omettez cette valeur, Braze ne créera pas de profil contenant uniquement un alias.
{% endalert %}

#### Importation de jetons de notification push

Avant d’importer des jetons de notification push à Braze, vérifiez si cela est nécessaire. Lorsque les SDK de Braze sont mis en place, ils gèrent automatiquement les jetons de poussée sans qu'il soit nécessaire de les télécharger via l'API.

Si vous devez les télécharger via l'API, vous pouvez le faire pour des utilisateurs identifiés ou anonymes. Cela signifie que soit un `external_id` doit être présent, soit les utilisateurs anonymes doivent avoir l’indicateur `push_token_import` défini sur `true`.

{% alert note %}
Lors de l’importation de jetons de notification push provenant d’autres systèmes, un `external_id` n’est pas toujours disponible. Pour maintenir la communication avec ces utilisateurs pendant votre transition vers Braze, vous pouvez importer les jetons existants pour les utilisateurs anonymes sans fournir `external_id`, en spécifiant `push_token_import` comme `true`.
{% endalert %}

Lorsque vous indiquez `push_token_import` comme `true` :

* `external_id` et `braze_id` **ne** doivent **pas** être spécifiés
* L'objet d'attribut **doit** contenir un jeton de poussée.
* Si le jeton existe déjà dans Braze, la demande est ignorée ; dans le cas contraire, Braze crée un profil utilisateur temporaire et anonyme pour chaque jeton afin de vous permettre de continuer à envoyer des messages à ces personnes.

Après l'importation, lorsque chaque utilisateur lance la version de votre application compatible avec Braze, Braze transfère automatiquement son jeton push importé vers son profil utilisateur Braze et supprime le profil temporaire.

Braze effectue une vérification mensuelle afin d'identifier tout profil anonyme marqué d'un`push_token_import`drapeau et ne disposant pas de jeton push. Si le profil anonyme ne dispose plus d'un jeton push, Braze supprime le profil. Toutefois, si le profil anonyme dispose toujours d'un jeton push, ce qui indique que l'utilisateur réel ne s'est pas encore connecté à l'appareil avec ledit jeton push, Braze ne prend aucune mesure.

Pour plus d'informations, consultez [Migration des jetons Push](#migrating-push-tokens).

#### Types de données des attributs personnalisés

Les types de données suivants peuvent être stockés en tant qu’attribut personnalisé :

| Type de données | Remarques |
| --- | --- |
| Tableaux | Les tableaux d'attributs personnalisés sont pris en charge. Lorsque vous ajoutez un élément, il est ajouté à la fin du tableau. Si l'élément existe déjà, il est déplacé de sa position actuelle vers la fin.<br><br>Seules les valeurs uniques sont enregistrées. Par exemple, l'importation`['hotdog','hotdog','hotdog','pizza']`  donne les résultats suivants`['hotdog', 'pizza']`.<br><br>Vous pouvez définir un tableau directement (par exemple, `"my_array_custom_attribute":[ "Value1", "Value2" ]`), ajouter des éléments à un tableau existant avec `"my_array_custom_attribute" : { "add" : ["Value3"] }`, ou supprimer des valeurs avec `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`.<br><br>Le nombre maximum d'éléments est défini par défaut à 25 par tableau et peut être augmenté jusqu'à 500. Pour plus d'informations, reportez-vous à la section [Tableaux]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays). |
| Tableau d’objets | Utilisez un tableau d'objets pour définir une liste d'objets où chaque objet contient un ensemble d'attributs. Veuillez utiliser ce type pour stocker plusieurs ensembles de données associées à un utilisateur, telles que les séjours à l'hôtel, l'historique des achats ou les préférences. <br><br>Par exemple, définissez un attribut personnalisé nommé`hotel_stays`sur un profil utilisateur sous forme de tableau où chaque objet représente un séjour distinct, avec des attributs tels que `hotel_name`,`check_in_date` et `nights_stayed`. Pour plus de détails, veuillez consulter [l'exemple Array of objects](#array-of-objects-example). |
| Booléens | `true` ou `false` |
| Dates | Veuillez enregistrer les dates au format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) ou dans l'un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Notez que le « T » est un indicateur de temps, et non une marque substitutive. Il ne doit pas être modifié ou supprimé. <br><br>Les attributs temporels sans fuseau horaire sont définis par défaut à minuit UTC (et sont formatés sur le tableau de bord comme l'équivalent de minuit UTC dans le fuseau horaire de l'entreprise). <br><br>Les événements dont l'heure est définie dans le futur sont automatiquement réglés sur l'heure actuelle. <br><br>Pour les attributs personnalisés standard, si l'année est inférieure à 0 ou supérieure à 3000, Braze enregistre la valeur sous forme de chaîne de caractères dans le profil utilisateur. |
| Floats | Les attributs personnalisés flottants sont des nombres positifs ou négatifs avec une virgule. Par exemple, vous pouvez utiliser des flottants pour stocker des soldes de comptes ou des évaluations de produits ou de services par les utilisateurs. |
| Entiers | Vous pouvez incrémenter des attributs personnalisés de type entier en assignant un objet avec le champ « inc » et la valeur à ajouter. <br><br>Exemple : `"my_custom_attribute_2" : {"inc" : int_value},`|
| Attributs personnalisés imbriqués | Les attributs personnalisés imbriqués définissent un ensemble d'attributs en tant que propriété d'un autre attribut. Lorsque vous définissez un objet attribut personnalisé, vous ajoutez un ensemble d'attributs à cet objet. Pour plus d'informations, reportez-vous à la section [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/). |
| Chaînes de caractères | Les attributs personnalisés de type chaîne sont des séquences de caractères utilisées pour stocker des données textuelles. Par exemple, vous pouvez utiliser des chaînes de caractères pour stocker les noms et prénoms, les adresses e-mail ou les préférences. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Pour obtenir des conseils sur l'utilisation d'un événement personnalisé ou d'un attribut personnalisé, veuillez consulter [les sections Custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) et [Attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).
{% endalert %}

##### Exemple de tableau d'objets

Cet ensemble d'objets vous permet de créer des segments en fonction de critères spécifiques au sein des séjours et de réaliser la personnalisation de vos messages à l'aide des données de chaque séjour grâce aux modèles Liquid.

```json
{"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
]}
```

#### Champs Braze User Profile (Profil d’utilisateur Braze) {#braze-user-profile-fields}

{% alert important %}
Les champs de profil utilisateur suivants sont sensibles à la casse, veillez donc à référencer ces champs en minuscule.
{% endalert %}

| Champ profil utilisateur | Spécification des types de données |
| ---| --- |
| alias_name | (string) |
| alias_label | (string) |
| braze_id | (chaîne de caractères, facultatif) Lorsqu'un profil utilisateur est reconnu par le SDK, un profil utilisateur anonyme est créé avec une adresse `braze_id`. Le `braze_id` est automatiquement attribué par Braze, ne peut pas être modifié et est spécifique à l’appareil de l’utilisateur. |
| pays | (chaîne de caractères) Nous exigeons que les codes de pays soient transmis à Braze selon la [norme ISO-3166-1 alpha-2.](http://en.wikipedia.org/wiki/ISO_3166-1) Notre API s'efforce de réaliser le mappage des pays reçus dans différents formats. Par exemple, « Australie » peut correspondre à « AU ». Toutefois, si la saisie ne correspond pas à une [norme ISO-3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1) donnée, la valeur du pays est définie sur `NULL`. <br><br>La configuration`country`d'un utilisateur par importation CSV ou API empêche Braze de capturer automatiquement ces informations via le SDK. |
| current_location | (objet) De la forme {"longitude" : -73.991443, "latitude" : 40.753824} |
| date_of_first_session | (date à laquelle l’utilisateur s’est servi de l’application pour la première fois) Chaîne de caractères au format ISO 8601 ou dans l’un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (date à laquelle l’utilisateur s’est servi de l’application pour la dernière fois) Chaîne de caractères au format ISO 8601 ou dans l’un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| ddn | (date de naissance) Chaîne au format "AAAA-MM-JJ", par exemple, 1980-12-21. |
| e-mail | (string) |
| email_subscribe | Les valeurs disponibles sont"opted_in"« abonné » (enregistré explicitement pour recevoir des messages d'e-mail), « désabonné » (a explicitement choisi de ne plus recevoir de messages d'e-mail) et « non abonné » (n'a ni choisi de s'abonner ni choisi de se désabonner).  |
| email_open_tracking_disabled |(booléen) `true` ou `false` accepté. Définissez ce paramètre sur `true` pour désactiver l'ajout du pixel de suivi des ouvertures dans tous les futurs e-mails envoyés à cet utilisateur. Disponible uniquement pour SparkPost et SendGrid.|
| email_click_tracking_disabled |(booléen) `true` ou `false` accepté. Définissez ce champ sur `true` pour désactiver le suivi des clics pour tous les liens contenus dans un prochain e-mail envoyé à cet utilisateur. Disponible uniquement pour SparkPost et SendGrid.|
| external_id | (string) Un identifiant unique pour un profil utilisateur. Une fois attribué`external_id`, Braze identifie le profil utilisateur sur l'ensemble des appareils d'un utilisateur. Lors de la première instance d'attribution d'unexternal_id  à un profil utilisateur inconnu, Braze effectue la migration de toutes les données existantes du profil utilisateur vers le nouveau profil utilisateur. |
| facebook | hachage contenant l’un des `id` (string), `likes` (array of strings), `num_friends` (integer). |
| first_name | (string) |
| genre | (string) « H », « F », « A » (autre), « S/O » (sans objet), « P » (préfère ne pas dire) ou nul (inconnu). |
| home_city | (string) |
| langue | (chaîne de caractères), nous exigeons que la langue soit transmise à Braze selon la [norme ISO-639-1.](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) Pour connaître les langues prises en charge, consultez notre [liste des langues acceptées]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/).<br><br>La configuration`language`d'un utilisateur par importation CSV ou API empêche Braze de capturer automatiquement ces informations via le SDK. |
| last_name | (string) |
| marked_email_as_spam_at | (chaîne de caractères) Date à laquelle l’e-mail de l’utilisateur a été marqué comme courrier indésirable. Apparaît au format ISO 8601 ou dans l’un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| téléphone | (chaîne de caractères) Nous recommandons de fournir les numéros de téléphone au format [E.164](https://en.wikipedia.org/wiki/E.164) format. Pour plus d'informations, reportez-vous à la section [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting).|
| push_subscribe | Les valeurs disponibles sont"opted_in"« subscribed » (s'est explicitement abonné pour recevoir des messages push), « unsubscribed » (a explicitement choisi de ne pas recevoir de messages push) et « subscribed » (ni abonné, ni désabonné).  |
| push_tokens | Tableau d’objets avec `app_id` et la chaîne de caractères `token`. Vous pouvez éventuellement fournir un `device_id` pour l’appareil auquel ce jeton est associé, par exemple, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Si aucun`device_id`n'est fourni, un est généré de manière aléatoire. |
| subscription_groups| Tableau d'objets avec les chaînes de caractères `subscription_group_id` et `subscription_state`, par exemple, `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Les valeurs disponibles pour `subscription_state` sont « subscribed » (abonné) et unsubscribed » (désabonné).|
| time_zone | (chaîne de caractères) Nom du fuseau horaire provenant de [la base de données des fuseaux horaires de l'IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (par exemple,"America/New_York"« Eastern Time (US&Canada) »). Seules les valeurs de fuseau horaire valides sont définies. |
| twitter | Hachage contenant l'un des éléments suivants : `id` (nombre entier), `screen_name` (chaîne de caractères, identifiant X (anciennement Twitter)), `followers_count` (nombre entier), `friends_count` (nombre entier), `statuses_count` (nombre entier). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les paramètres linguistiques explicitement définis via cette API ont priorité sur les informations régionales que Braze reçoit automatiquement de l'appareil.

####  Demande d’exemple d’attribut utilisateur

Cet exemple contient quatre objets d'attributs d'utilisateur, sur un total de 75 objets d'attributs autorisés par appel API.

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

## Migration des jetons Push

Si vous envoyiez des notifications push avant d'intégrer Braze, soit par vous-même, soit par un autre fournisseur, la migration des jetons push vous permet de continuer à envoyer des notifications push à vos utilisateurs avec des jetons push enregistrés.

### Migration automatique via SDK

Une fois [le SDK Braze intégré]({{site.baseurl}}/developer_guide/sdk_integration/), les jetons push de vos utilisateurs en abonnement sont automatiquement migrés lors de leur prochaine ouverture de l'application. Jusqu'à ce moment-là, il n'est pas possible d'envoyer des notifications push à ces utilisateurs via Braze.

Vous pouvez également [migrer vos jetons push manuellement](#manual-migration-via-api), ce qui vous permettra de réengager vos utilisateurs plus rapidement.

#### Considérations relatives aux jetons Web

En raison de la nature des jetons de push pour le web, veillez à prendre en compte les éléments suivants lors de la mise en œuvre du push pour le web :

|Considération|Détails|
|----------------------|------------|
| **Service de traitement**  | Par défaut, le SDK Web recherche un service de traitement à l'adresse`./service-worker`  à moins qu'une autre option ne soit spécifiée, telle que`manageServiceWorkerExternally`  ou `serviceWorkerLocation`. Si votre service de traitement n'est pas configuré correctement, vos utilisateurs risquent de voir leurs jetons push expirer. |
| **Jetons expirés**   | Si un utilisateur n'a pas démarré de session Web dans les 60 jours, son jeton push expire. Étant donné que Braze ne peut pas effectuer la migration des jetons push expirés, il est nécessaire d'envoyer un [message push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages) pour assurer le réengagement. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Migration manuelle via l'API

La migration manuelle des jetons push est le processus d'importation de ces clés précédemment créées dans votre plateforme Braze via l'API.

Migrez par programme les jetons iOS (APNs) et Android (FCM) vers votre plateforme en utilisant le [`users/track` point de terminaison]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Vous pouvez migrer à la fois les utilisateurs identifiés (utilisateurs avec un ID externe associé) et les utilisateurs anonymes (utilisateurs sans ID externe).

Spécifiez votre `app_id` lors de la migration du jeton de notification pour associer le jeton de notification approprié à l'application appropriée. Chaque application (iOS, Android, etc.) a son propre `app_id`, qui peut être trouvé dans la section **Identification** de la page [Clés API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). Assurez-vous d’utiliser les bonnes `app_id` pour chaque plateforme.

{% alert important %}
Il n’est pas possible de faire migrer les jetons push Web via l’API. En effet, les jetons push Web n’utilisent pas le même schéma que les autres plateformes.

<br>Si vous tentez de migrer des jetons de notification push Web par programmation, une erreur semblable à celle-ci peut s’afficher :`Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
En guise d’alternative à la migration via API, nous vous recommandons d’intégrer le SDK et de permettre à votre base de jetons de se remplir naturellement de nouveau.
{% endalert %}

{% tabs local %}
{% tab External ID present %}
Pour les utilisateurs identifiés, définissez l’indicateur `push_token_import` sur `false` (ou omettez le paramètre) et spécifiez les valeurs `external_id`, `app_id` et `token` dans l’objet `attributes` utilisateur.

Par exemple :

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
Lors de l’importation de jetons de notification push provenant d’autres systèmes, un `external_id` n’est pas toujours disponible. Dans ce cas, définissez votre indicateur `push_token_import` sur `true` et spécifiez les valeurs `app_id` et `token`. Braze crée un profil utilisateur temporaire et anonyme pour chaque jeton afin de vous permettre de continuer à envoyer des messages à ces personnes. Si le jeton existe déjà dans Braze, la demande sera ignorée.

Par exemple :

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

Après l'importation, lorsque l'utilisateur anonyme lance la version de votre application compatible avec Braze, Braze transfère automatiquement son jeton push importé vers son profil utilisateur Braze et supprime le profil temporaire.

Braze effectue une vérification mensuelle afin d'identifier tout profil anonyme marqué d'un`push_token_import`drapeau et ne disposant pas de jeton push. Si le profil anonyme ne dispose plus d'un jeton push, Braze supprime le profil. Toutefois, si le profil anonyme dispose toujours d'un jeton push, ce qui indique que l'utilisateur réel ne s'est pas encore connecté à l'appareil avec ledit jeton push, Braze ne prend aucune mesure.
{% endtab %}
{% endtabs %}

### Importation de jetons push Android

{% alert important %}
La remarque suivante s'applique uniquement aux applications Android. Les applications iOS ne nécessitent pas ces étapes, car cette plateforme ne dispose que d'un seul framework pour l'affichage des notifications push, et celles-ci s'affichent immédiatement dès lors que Braze dispose des jetons et certificats push nécessaires.
{% endalert %}

Si vous devez envoyer une notification push Android à vos utilisateurs avant d’avoir terminé l’intégration du SDK Braze, utilisez des paires clé-valeur pour valider les notifications push.

Vous devez disposer d’un récepteur pour manipuler et afficher les charges utiles de push. Pour notifier le récepteur de la charge utile de push, ajoutez les paires valeur-clé nécessaires à la campagne push. Les valeurs de ces paires dépendent du partenaire push spécifique que vous utilisiez avant Braze.

{% alert note %}
Pour certains fournisseurs de notifications push, Braze doit aplatir les paires clé-valeur afin qu'elles puissent être correctement interprétées. Pour aplatir les paires clé-valeur d'une application Android spécifique, veuillez contacter votre gestionnaire de la satisfaction client.
{% endalert %}