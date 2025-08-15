---
nav_title: "Objet Attributs d’utilisateur"
article_title: Objet Attributs d’utilisateur de l’API
page_order: 11
page_type: reference
description: "Cet article de référence explique les différents composants de l’objet Attributs d’utilisateur."

---

# Objet Attributs d’utilisateur

> Une demande API contenant l’un des champs de l’objet Attributs créera ou mettra à jour un attribut de ce nom avec la valeur donnée sur le profil utilisateur spécifié. 

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
  // Setting this flag to true will put the API in "Update Only" mode.
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

#### Mettre à jour les profils existants uniquement

Si vous souhaitez mettre à jour uniquement les profils utilisateur existants dans Braze, vous devez passer la clé `_update_existing_only` avec la valeur `true` dans le corps de votre demande. Si cette valeur est omise, Braze créera un nouveau profil utilisateur si `external_id` n’existe pas déjà.

{% alert note %}
Si vous créez un profil utilisateur alias uniquement via l'endpoint `/users/track`, `_update_existing_only` doit être défini sur `false`. Si cette valeur est omise, le profil alias uniquement ne sera pas créé.
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
* Si le jeton existe déjà dans Braze, la demande est ignorée ; sinon, Braze créera un profil utilisateur temporaire et anonyme pour chaque jeton pour vous permettre de continuer à envoyer des messages à ces personnes

Après l’importation, lorsque chaque utilisateur lance la version compatible Braze de votre application, Braze déplace automatiquement leur jeton de notification push importé vers leur profil utilisateur Braze et efface le profil temporaire.

Braze vérifiera une fois par mois s’il existe des profils anonymes avec l’indicateur `push_token_import` qui n’ont pas de jeton de notification push. Si le profil anonyme n’a plus de jeton de notification push, nous le supprimerons. Cependant, si le profil anonyme a toujours un jeton de notification push, indiquant que l’utilisateur ne s’est pas encore connecté à l’appareil avec le jeton de notification push, nous ne ferons rien.

Pour plus d'informations, consultez [Migration des jetons Push]({{site.baseurl}}/help/help_articles/push/push_token_migration/).

#### Types de données des attributs personnalisés

Les types de données suivants peuvent être stockés en tant qu’attribut personnalisé :

| Type de données | Remarques |
| --- | --- |
| Tableaux | Les tableaux d'attributs personnalisés sont pris en charge. L’ajout d’un élément à un tableau d’attribut personnalisé ajoute l’élément à la fin du tableau, à moins qu’il ne soit déjà présent, auquel cas il passe de sa position actuelle à la fin du tableau.<br><br>Par exemple, si un tableau `['hotdog','hotdog','hotdog','pizza']` a été importé, il apparaîtra dans l’attribut de tableau comme `['hotdog', 'pizza']`, car seules des valeurs uniques sont prises en charge.<br><br>En plus de définir les valeurs d’un tableau en indiquant quelque chose comme `"my_array_custom_attribute":[ "Value1", "Value2" ]`, vous pouvez ajouter des tableaux existants en faisant quelque chose comme `"my_array_custom_attribute" : { "add" : ["Value3"] },` ou supprimer les valeurs d’un tableau en écrivant quelque chose comme `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`.<br><br>Le nombre maximum d’éléments dans les tableaux d’attributs personnalisés est par défaut de 25, mais peut être augmenté jusqu’à 100 pour un tableau donné. Pour plus d'informations, reportez-vous à la section [Tableaux]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays). |
| Tableau d’objets | Le tableau d'objets vous permet de définir une liste d'objets où chaque objet contient un ensemble d'attributs. Cela peut s'avérer utile si vous avez besoin de stocker plusieurs ensembles de données liées pour un utilisateur, comme les séjours à l'hôtel, l'historique des achats ou les préférences. <br><br> Par exemple, vous pouvez définir un attribut personnalisé sur un profil utilisateur nommé `hotel_stays`. Cet attribut personnalisé peut être défini comme un tableau d'objets représentant chacun un séjour distinct, avec des attributs tels que `hotel_name`, `check_in_date`, `nights_stayed`. Pour plus de détails, consultez [cet exemple.](#array-of-objects-example) |
| Booléens | `true` ou `false` |
| Dates | Doit être stocké dans le format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) ou dans l'un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Notez que le « T » est un indicateur de temps, et non une marque substitutive. Il ne doit pas être modifié ou supprimé. <br><br>Les attributs de temps sans fuseau horaire seront par défaut à minuit UTC (et seront formatés sur le tableau de bord comme l’équivalent de minuit UTC dans le fuseau horaire de la société). <br><br> Les événements avec des horodatages dans le futur seront par défaut à l’heure actuelle. <br><br> Pour les attributs personnalisés réguliers, si l'année est inférieure à 0 ou supérieure à 3 000, Braze stocke ces valeurs sous forme de chaînes de caractères sur l'utilisateur. |
| Floats | Les attributs personnalisés flottants sont des nombres positifs ou négatifs avec une virgule. Par exemple, vous pouvez utiliser des flottants pour stocker des soldes de comptes ou des évaluations de produits ou de services par les utilisateurs. |
| Entiers | Les attributs personnalisés entiers peuvent être incrémentés par des nombres entiers positifs ou négatifs en leur attribuant un objet avec le champ "inc" et la valeur par laquelle vous souhaitez les incrémenter. <br><br>Exemple : `"my_custom_attribute_2" : {"inc" : int_value},`|
| Attributs personnalisés imbriqués | Les attributs personnalisés imbriqués définissent un ensemble d'attributs en tant que propriété d'un autre attribut. Lorsque vous définissez un objet d'attribut personnalisé, vous définissez un ensemble d'attributs supplémentaires pour cet objet. Pour plus d'informations, reportez-vous à la section [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/). |
| Chaînes de caractères | Les attributs personnalisés de type chaîne sont des séquences de caractères utilisées pour stocker des données textuelles. Par exemple, vous pouvez utiliser des chaînes de caractères pour stocker les noms et prénoms, les adresses e-mail ou les préférences. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Pour savoir quand vous devez utiliser un événement personnalisé plutôt qu'un attribut personnalisé, consultez nos documentations respectives sur les [événements]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) et [attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).
{% endalert %}

##### Exemple de tableau d'objets 

Ce tableau d'objets vous permet de créer des segments basés sur des critères spécifiques au sein des séjours, et de personnaliser vos messages en utilisant les données de chaque séjour avec les modèles Liquid.

```json
"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
  ]
```

#### Champs Braze User Profile (Profil d’utilisateur Braze) {#braze-user-profile-fields}

{% alert important %}
Les champs de profil utilisateur suivants sont sensibles à la casse, veillez donc à référencer ces champs en minuscule.
{% endalert %}

| Champ profil utilisateur | Spécification des types de données |
| ---| --- |
| nom_alias | (string) |
| alias_label | (string) |
| braze_id | (chaîne de caractères, facultatif) Lorsqu'un profil utilisateur est reconnu par le SDK, un profil utilisateur anonyme est créé avec une adresse `braze_id`. Le `braze_id` est automatiquement attribué par Braze, ne peut pas être modifié et est spécifique à l’appareil de l’utilisateur. | 
| pays | (chaîne de caractères) Nous exigeons que les codes de pays soient transmis à Braze selon la [norme ISO-3166-1 alpha-2.](http://en.wikipedia.org/wiki/ISO_3166-1) Notre API s'efforcera de mapper les pays reçus dans différents formats. Par exemple, « Australie » peut correspondre à « AU ». Cependant, si l'entrée ne correspond pas à une [norme ISO-3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1) donnée, la valeur du pays sera définie sur `NULL`. <br><br>La définition de `country` sur un utilisateur par importation d'un CSV ou par API empêchera Braze de capturer automatiquement ces informations via le SDK. |
| lieu_actuel | (objet) du formulaire {"longitude": -73.991443, "latitude": 40.753824} |
| date_de_la_première_session | (date à laquelle l’utilisateur s’est servi de l’application pour la première fois) Chaîne de caractères au format ISO 8601 ou dans l’un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_de_la_dernière_session | (date à laquelle l’utilisateur s’est servi de l’application pour la dernière fois) Chaîne de caractères au format ISO 8601 ou dans l’un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| ddn | (date de naissance) Chaîne de caractères au format "AAAA-MM-JJ", par exemple, 1980-12-21. |
| e-mail | (string) |
| abonnement aux e-mails | (chaîne de caractères) Les valeurs disponibles sont "opted_in" (explicitement inscrit pour recevoir des messages e-mail), "unsubscribed" (explicitement désinscrit des messages e-mail) et "subscribed" (ni inscrit ni désinscrit).  |
| email_open_tracking_disabled |(booléen) `true` ou `false` accepté. Définissez ce paramètre sur `true` pour désactiver l'ajout du pixel de suivi des ouvertures dans tous les futurs e-mails envoyés à cet utilisateur. Disponible uniquement pour SparkPost et SendGrid.|
| email_click_tracking_disabled |(booléen) `true` ou `false` accepté. Définissez ce champ sur `true` pour désactiver le suivi des clics pour tous les liens contenus dans un prochain e-mail envoyé à cet utilisateur. Disponible uniquement pour SparkPost et SendGrid.|
| external_id | (string) Un identifiant unique pour un profil utilisateur. Après l'attribution d'un `external_id`, le profil utilisateur est identifié sur l'ensemble des appareils de l'utilisateur. Lors de la première instance d'attribution d'un identifiant externe à un profil utilisateur inconnu, toutes les données du profil utilisateur existant seront migrées vers le nouveau profil utilisateur. |
| facebook | hachage contenant l’un des `id` (string), `likes` (array of strings), `num_friends` (integer). |
| Prénom | (string) |
| genre | (string) « H », « F », « A » (autre), « S/O » (sans objet), « P » (préfère ne pas dire) ou nul (inconnu). |
| ville | (string) |
| langue | (chaîne de caractères), nous exigeons que la langue soit transmise à Braze selon la [norme ISO-639-1.](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) Pour connaître les langues prises en charge, consultez notre [liste des langues acceptées]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/).<br><br>La définition de `language` sur un utilisateur par importation d'un CSV ou par API empêchera Braze de capturer automatiquement ces informations via le SDK. |
| Nom | (string) |
| marked_email_as_spam_at | (chaîne de caractères) Date à laquelle l’e-mail de l’utilisateur a été marqué comme courrier indésirable. Apparaît au format ISO 8601 ou dans l’un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| téléphone | (chaîne de caractères) Nous recommandons de fournir les numéros de téléphone au format [E.164](https://en.wikipedia.org/wiki/E.164) format. Pour plus d'informations, reportez-vous à la section [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting).|
| abonnement aux notifications push | (chaîne) Les valeurs disponibles sont "opted_in" (explicitement enregistré pour recevoir des messages push), "unsubscribed" (explicitement exclu des messages push), et "subscribed" (ni in ni out).  |
| push_tokens | Tableau d’objets avec `app_id` et la chaîne de caractères `token`. Vous pouvez éventuellement fournir un `device_id` pour l’appareil auquel ce jeton est associé, par exemple, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Si aucun `device_id` n’est pas fourni, il sera généré de manière aléatoire. |
| groupes_d'abonnement| Tableau d'objets avec les chaînes de caractères `subscription_group_id` et `subscription_state`, par exemple, `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Les valeurs disponibles pour `subscription_state` sont « subscribed » (abonné) et unsubscribed » (désabonné).|
| fuseau horaire | (chaîne de caractères) Nom du fuseau horaire provenant de la [base de données des fuseaux horaires de l'IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (par exemple, "America/New_York" ou "Eastern Time (US & Canada)"). Seules les valeurs de fuseau horaire valides seront définies. |
| twitter | Hash contenant l'un des éléments suivants : `id` (nombre entier), `screen_name` (chaîne de caractères, identifiant X (anciennement Twitter)), `followers_count` (nombre entier), `friends_count` (nombre entier), `statuses_count` (nombre entier). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les valeurs linguistiques définies explicitement par le biais de cette API sont prioritaires sur les informations relatives aux paramètres linguistiques que Braze reçoit automatiquement de l'appareil.

####  Demande d’exemple d’attribut utilisateur

Cet exemple contient quatre objets d'attributs d'utilisateur, sur un total de 75 objets d'attributs autorisés par appel API.

```json
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

