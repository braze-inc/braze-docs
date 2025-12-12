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

Pour plus d'informations, consultez [Migration des jetons Push](#migrating-push-tokens).

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
| alias_name | (string) |
| alias_label | (string) |
| braze_id | (chaîne de caractères, facultatif) Lorsqu'un profil utilisateur est reconnu par le SDK, un profil utilisateur anonyme est créé avec une adresse `braze_id`. Le `braze_id` est automatiquement attribué par Braze, ne peut pas être modifié et est spécifique à l’appareil de l’utilisateur. | 
| pays | (chaîne de caractères) Nous exigeons que les codes de pays soient transmis à Braze selon la [norme ISO-3166-1 alpha-2.](http://en.wikipedia.org/wiki/ISO_3166-1) Notre API s'efforcera de mapper les pays reçus dans différents formats. Par exemple, « Australie » peut correspondre à « AU ». Cependant, si l'entrée ne correspond pas à une [norme ISO-3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1) donnée, la valeur du pays sera définie sur `NULL`. <br><br>La définition de `country` sur un utilisateur par importation d'un CSV ou par API empêchera Braze de capturer automatiquement ces informations via le SDK. |
| current_location | (objet) De la forme {"longitude" : -73.991443, "latitude" : 40.753824} |
| date_of_first_session | (date à laquelle l’utilisateur s’est servi de l’application pour la première fois) Chaîne de caractères au format ISO 8601 ou dans l’un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (date à laquelle l’utilisateur s’est servi de l’application pour la dernière fois) Chaîne de caractères au format ISO 8601 ou dans l’un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| ddn | (date de naissance) Chaîne au format "AAAA-MM-JJ", par exemple, 1980-12-21. |
| e-mail | (string) |
| email_subscribe | (chaîne de caractères) Les valeurs disponibles sont "opted_in" (explicitement inscrit pour recevoir des messages e-mail), "unsubscribed" (explicitement désinscrit des messages e-mail) et "subscribed" (ni inscrit ni désinscrit).  |
| email_open_tracking_disabled |(booléen) `true` ou `false` accepté. Définissez ce paramètre sur `true` pour désactiver l'ajout du pixel de suivi des ouvertures dans tous les futurs e-mails envoyés à cet utilisateur. Disponible uniquement pour SparkPost et SendGrid.|
| email_click_tracking_disabled |(booléen) `true` ou `false` accepté. Définissez ce champ sur `true` pour désactiver le suivi des clics pour tous les liens contenus dans un prochain e-mail envoyé à cet utilisateur. Disponible uniquement pour SparkPost et SendGrid.|
| external_id | (string) Un identifiant unique pour un profil utilisateur. Après l'attribution d'un `external_id`, le profil utilisateur est identifié sur l'ensemble des appareils de l'utilisateur. Dans la première instance d’attribution d’un external_id à un profil utilisateur inconnu, toutes les données de profil utilisateur existantes seront migrées vers le nouveau profil utilisateur. |
| facebook | hachage contenant l’un des `id` (string), `likes` (array of strings), `num_friends` (integer). |
| first_name | (string) |
| genre | (string) « H », « F », « A » (autre), « S/O » (sans objet), « P » (préfère ne pas dire) ou nul (inconnu). |
| home_city | (string) |
| langue | (chaîne de caractères), nous exigeons que la langue soit transmise à Braze selon la [norme ISO-639-1.](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) Pour connaître les langues prises en charge, consultez notre [liste des langues acceptées]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/).<br><br>La définition de `language` sur un utilisateur par importation d'un CSV ou par API empêchera Braze de capturer automatiquement ces informations via le SDK. |
| last_name | (string) |
| marked_email_as_spam_at | (chaîne de caractères) Date à laquelle l’e-mail de l’utilisateur a été marqué comme courrier indésirable. Apparaît au format ISO 8601 ou dans l’un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| téléphone | (chaîne de caractères) Nous recommandons de fournir les numéros de téléphone au format [E.164](https://en.wikipedia.org/wiki/E.164) format. Pour plus d'informations, reportez-vous à la section [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting).|
| push_subscribe | (chaîne caractères) Les valeurs disponibles sont "opted_in" (explicitement enregistré pour recevoir des messages push), "unsubscribed" (explicitement opted out of push messages), et "subscribed" (ni opted in ni out).  |
| push_tokens | Tableau d’objets avec `app_id` et la chaîne de caractères `token`. Vous pouvez éventuellement fournir un `device_id` pour l’appareil auquel ce jeton est associé, par exemple, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Si aucun `device_id` n’est pas fourni, il sera généré de manière aléatoire. |
| subscription_groups| Tableau d'objets avec les chaînes de caractères `subscription_group_id` et `subscription_state`, par exemple, `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Les valeurs disponibles pour `subscription_state` sont « subscribed » (abonné) et unsubscribed » (désabonné).|
| time_zone | (chaîne de caractères) Nom du fuseau horaire provenant de la [base de données des fuseaux horaires de l'IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (par exemple, "America/New_York" ou "Eastern Time (US & Canada)"). Seules les valeurs de fuseau horaire valides seront définies. |
| twitter | Hachage contenant l'un des éléments suivants : `id` (nombre entier), `screen_name` (chaîne de caractères, identifiant X (anciennement Twitter)), `followers_count` (nombre entier), `friends_count` (nombre entier), `statuses_count` (nombre entier). |
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

## Migration des jetons Push

Si vous envoyiez des notifications push avant d'intégrer Braze, soit par vous-même, soit par un autre fournisseur, la migration des jetons push vous permet de continuer à envoyer des notifications push à vos utilisateurs avec des jetons push enregistrés.

### Migration automatique grâce au SDK

Après avoir [intégré le SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/), les jetons de push de vos utilisateurs abonnés seront automatiquement migrés la prochaine fois qu'ils ouvriront votre application. En attendant, vous ne pourrez pas envoyer à ces utilisateurs des notifications push via Braze.

Vous pouvez également [migrer vos jetons push manuellement](#manual-migration-via-api), ce qui vous permettra de réengager vos utilisateurs plus rapidement.

#### Considérations relatives aux jetons Web

En raison de la nature des jetons de push pour le web, veillez à prendre en compte les éléments suivants lors de la mise en œuvre du push pour le web :

|Considération|Détails|
|----------------------|------------|
| **Service de traitement**  | Par défaut, le SDK Web recherche un service de traitement à l'adresse `./service-worker`, sauf si une autre option est spécifiée, telle que `manageServiceWorkerExternally` ou `serviceWorkerLocation`. Si votre service de traitement n'est pas configuré correctement, vos utilisateurs risquent de voir leurs jetons push expirer. |
| **Jetons expirés**   | Si un utilisateur n'a pas démarré de session web dans les 60 jours, son jeton push expirera. Comme Braze ne peut pas migrer les jetons push expirés, vous devrez envoyer une [amorce de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages) pour les réengager. |
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

```json
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
Lors de l’importation de jetons de notification push provenant d’autres systèmes, un `external_id` n’est pas toujours disponible. Dans ce cas, définissez votre indicateur `push_token_import` sur `true` et spécifiez les valeurs `app_id` et `token`. Braze créera un profil utilisateur temporaire et anonyme pour chaque jeton pour vous permettre de continuer à envoyer des messages à ces personnes. Si le jeton existe déjà dans Braze, la demande sera ignorée.

Par exemple :

```json
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

Après l'importation, lorsque l'utilisateur anonyme lance la version de votre application activée par Braze, Braze déplacera automatiquement leur jeton de notification importé vers leur profil utilisateur Braze et nettoiera le profil temporaire.

Braze vérifiera une fois par mois s’il existe des profils anonymes avec l’indicateur `push_token_import` qui n’ont pas de jeton de notification push. Si le profil anonyme n’a plus de jeton de notification push, nous le supprimerons. Cependant, si le profil anonyme a toujours un jeton de notification push, indiquant que l’utilisateur ne s’est pas encore connecté à l’appareil avec le jeton de notification push, nous ne ferons rien.
{% endtab %}
{% endtabs %}

### Importation de jetons push Android

{% alert important %}
Les éléments suivants ne s’appliquent qu’aux applications Android. Les applications iOS ne nécessiteront pas ces étapes, car cette plateforme ne dispose que d’un seul cadre pour afficher les notifications push, et les notifications push s’afficheront immédiatement tant que Braze dispose des jetons push et des certificats nécessaires.
{% endalert %}

Si vous devez envoyer une notification push Android à vos utilisateurs avant d’avoir terminé l’intégration du SDK Braze, utilisez des paires clé-valeur pour valider les notifications push. 

Vous devez disposer d’un récepteur pour manipuler et afficher les charges utiles de push. Pour notifier le récepteur de la charge utile de push, ajoutez les paires valeur-clé nécessaires à la campagne push. Les valeurs de ces paires dépendent du partenaire push spécifique que vous utilisiez avant Braze.

{% alert note %}
Pour certains fournisseurs de notifications push, le Braze devra aplanir les paires clé-valeur pour qu’elles puissent être interprétées correctement. Pour aplatir les paires clé-valeur pour une application Android spécifique, contactez votre gestionnaire de satisfaction client.
{% endalert %}