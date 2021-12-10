---
nav_title: "Objet Attribut Utilisateur"
article_title: Objet Attribut Utilisateur API
page_order: 11
page_type: Référence
description: "Cet article explique les différents composants de l'objet User Alias."
---

# Spécification des attributs de l'utilisateur

Une requête API avec n'importe quel champ dans l'objet Attributes créera ou mettra à jour un attribut de ce nom avec la valeur donnée sur le profil utilisateur spécifié. Utilisez les noms de champs de profil utilisateur Braze (listés ci-dessous ou tous ceux listés dans le [graphique des champs de profil utilisateur][27]) pour mettre à jour ces valeurs spéciales sur le profil utilisateur dans le tableau de bord ou ajouter vos propres données d'attributs personnalisés à l'utilisateur.

```json
{
  // Un de "external_id" ou "user_alias" ou "braze_id" est requis
  "external_id" : (optionnel, string) voir ID utilisateur externe ci-dessous,
  "user_alias" : (optionnel, Objet User Alias),
  "braze_id" : (optionnel, chaîne) Braze User Identifier,
  // Mettre ce drapeau à true mettra l'API en mode "Mise à jour uniquement".
  // Lorsque vous utilisez un "user_alias", la valeur par défaut "Update Only" est true.
  "_update_existing_only" : (facultatif, booléen),
  // Voir la note ci-dessous concernant les importations de jetons de poussage anonymes
  "push_token_import" : (facultatif, boolean),
  // Braze User Profile Fields
  "first_name" : "Jon",
  "email" : "bob@example. om",
  // Attributs personnalisés
  "mon_custom_attribute" : valeur,
  "mon_custom_attribute_2" : {"inc" : int_value},
  "mon_array_custom_attribute":[ "Valeur1", "Valeur2" ],
  // Ajout d'une nouvelle valeur à un attribut personnalisé de tableau
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Suppression d'une valeur d'un attribut personnalisé tableau
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
}
```

Pour supprimer un attribut de profil, définissez-le à null. Certains champs, tels que `external_id` et `user_alias` ne peuvent pas être supprimés une fois ajoutés à un profil utilisateur.

#### Mettre à jour les profils existants uniquement

Si vous souhaitez mettre à jour uniquement les profils d'utilisateurs existants au Brésil, vous devez passer la clé `_update_existing_only` avec une valeur de `true` dans le corps de votre requête. Si cette valeur est omise, Braze créera un nouveau profil utilisateur si le `external_id` n'existe pas déjà.

{% alert note %}
Si vous créez un profil utilisateur uniquement en tant qu'alias via le point de terminaison utilisateur/piste, `_update_existing_only` doit être défini à `false`. Si cette valeur est omise, le profil des alias ne sera pas créé.
{% endalert %}

#### Importation du jeton Push

Avant d'importer des jetons push au Brésil, vérifiez si vous en avez besoin. Quand les SDK Braze sont mis en place, ils gèrent automatiquement les jetons push sans avoir besoin de les télécharger via l'API.

Si vous trouvez que vous devez les télécharger via l'API, elles peuvent être téléchargées pour les utilisateurs identifiés ou pour les utilisateurs anonymes. Cela signifie que soit un `external_id` doit être présent, ou les utilisateurs anonymes doivent avoir le drapeau `push_token_import` défini à `true`.

{% alert note %}
Lors de l'importation de jetons push depuis d'autres systèmes, un `external_id` n'est pas toujours disponible. Pour maintenir la communication avec ces utilisateurs pendant votre transition vers Braze, vous pouvez importer les jetons hérités pour les utilisateurs anonymes sans fournir `external_id` en spécifiant `push_token_import` comme `true`.
{% endalert %}

En spécifiant `push_token_import` comme `true`:

* `external_id` et `braze_id` ne doit __pas ętre spécifié__
* L'objet d'attribut __doit__ contenir un jeton push
* Si le jeton existe déjà au Brésil, la requête est ignorée ; sinon Braze créera un profil d'utilisateur temporaire et anonyme pour chaque jeton pour vous permettre de continuer à envoyer un message à ces personnes

Après l'importation, chaque utilisateur lance la version brésilienne de votre application, Braze déplacera automatiquement son jeton push importé vers son profil utilisateur Braze et nettoie le profil temporaire.

Braze vérifiera une fois par mois pour trouver un profil anonyme avec le drapeau `push_token_import` qui n'a pas de jeton push_token_import . Si le profil anonyme n'a plus de jeton push, nous supprimerons le profil. Cependant, si le profil anonyme a encore un jeton de push, suggérant que l'utilisateur actuel doit encore se connecter à l'appareil avec ce jeton push, nous ne ferons rien.

Pour plus d'informations, consultez [la migration de jetons Push][3].

#### Types de données d'attributs personnalisés

Les types de données suivants peuvent être stockés en tant qu'attribut personnalisé :

| Type de données       | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Tableaux              | Les tableaux d'attributs personnalisés sont des ensembles unidimensionnels; les tableaux multidimensionnels ne sont pas pris en charge. Ajouter un élément à un tableau d'attributs personnalisés ajoute l'élément à la fin du tableau, sauf si elle est déjà présente, auquel cas elle est déplacée de sa position courante à la fin du tableau.<br><br>Par exemple, si une table `['hotdog','hotdog','hotdog','hotdog','pizza']` a été importée, il affichera dans l'attribut tableau comme `['hotdog', 'pizza']` car seules les valeurs uniques sont prises en charge.<br><br>En plus de définir les valeurs d'un tableau en disant quelque chose comme `"my_array_custom_attribute":[ "Value1", "Value2" ]` vous pouvez ajouter aux tableaux existants en faisant quelque chose comme `"my_array_custom_attribute" : { "add" : ["Value3"] },` ou supprimez des valeurs d'un tableau en faisant quelque chose comme `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`<br><br>Le nombre maximum d'éléments dans les tableaux d'attributs personnalisés est de 25. Le maximum pour chaque tableau peut être augmenté jusqu'à 100. Si vous souhaitez augmenter ce maximum, veuillez contacter votre responsable du service à la clientèle. Les tableaux dépassant le nombre maximum d'éléments seront tronqués pour contenir le nombre maximum d'éléments. Pour plus d'informations sur les tableaux d'attributs personnalisés et leur comportement, consultez notre [documentation sur les tableaux][6]. |
| Booléens              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Dates                 | Doit être stocké au format [ISO 8601][19] ou `yyyy-MM-ddTHH:mm:ss:SSSZ`. Notez que "T" est un concepteur de temps, pas un placeholder. <br><br>Les attributs temporels sans fuseau horaire seront par défaut à Midnight UTC (et seront formatés sur le tableau de bord comme l'équivalent de Midnight UTC dans le fuseau horaire de l'entreprise). <br><br> Les événements avec horodatage dans le futur seront par défaut à l'heure courante.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Flottant              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Nombre entier         | Les attributs personnalisés entiers peuvent être incrémentés par des entiers positifs ou négatifs en leur attribuant un objet avec le champ "inc" et la valeur par laquelle vous souhaitez les incrémenter. <br><br>Exemple : `"my_custom_attribute_2" : {"inc" : int_value},`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Chaînes de caractères |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
{: .reset-td-br-1 .reset-td-br-2}

Pour plus d'informations concernant le moment où vous devriez utiliser un événement personnalisé vs un attribut personnalisé, consultez notre documentation [Meilleures pratiques - Collecte de données utilisateur][15].

#### Braze les champs de profil de l'utilisateur {#braze-user-profile-fields}

{% alert important %}
Les champs suivants du profil utilisateur sont sensibles à la casse, alors assurez-vous de les référencer en minuscule.
{% endalert %}

| Champ de profil utilisateur      | Spécification du type de données                                                                                                                                                                                                                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pays                             | (string) Nous exigeons que les codes pays soient passés à Braze dans la norme [ISO-3166-1 alpha-2][17].                                                                                                                                                                                                                   |
| emplacement actuel               | (objet) De la forme {"longitude": -73.991443, "latitude": 40.753824}                                                                                                                                                                                                                                                      |
| Date de la première session      | (date à laquelle l'utilisateur a utilisé l'application pour la première fois) Chaîne au format ISO 8601 ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`.                                                                                                                                                                        |
| Date de la dernière session      | (date à laquelle l'utilisateur a utilisé la dernière fois l'application) Chaîne au format ISO 8601 ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`.                                                                                                                                                                             |
| chien                            | (date de naissance) Chaîne au format "AAAA-MM-JJ", par exemple 1980-12-21.                                                                                                                                                                                                                                                |
| Email                            | (chaîne)                                                                                                                                                                                                                                                                                                                  |
| Inscription par e-mail           | (string) Les valeurs disponibles sont "opted_in" (explicitement enregistrées pour recevoir des messages électroniques), "unsubscribed" (explicitement opted out of email messages) et "subscribed" (ni opted in ni out).                                                                                                  |
| Email_open_tracking_désactivé  | (booléen) vrai ou faux accepté.  Définir à vrai pour désactiver le pixel de suivi ouvert d'être ajouté à tous les e-mails futurs envoyés à cet utilisateur.                                                                                                                                                               |
| Email_click_tracking_désactivé | (booléen) vrai ou faux accepté.  Définir à vrai pour désactiver le suivi des clics pour tous les liens dans un e-mail futur, envoyé à cet utilisateur.                                                                                                                                                                    |
| id externe                       | (chaîne) De l'identifiant unique de l'utilisateur.                                                                                                                                                                                                                                                                        |
| facebook                         | hash contenant un de `id` (chaîne), `likes` (tableau de chaînes), `num_friends` (entier).                                                                                                                                                                                                                                 |
| prénom                           | (chaîne)                                                                                                                                                                                                                                                                                                                  |
| Sexe                             | (chaîne) "M", "F", "O" (autre), "N" (non applicable), "P" (préfère ne pas dire) ou "nil (inconnu).                                                                                                                                                                                                                        |
| ville_domicile                   | (chaîne)                                                                                                                                                                                                                                                                                                                  |
| url de l'image                   | (chaîne) URL de l'image à associer au profil de l'utilisateur.                                                                                                                                                                                                                                                            |
| Langue                           | (chaîne) nous exigeons que le langage soit passé à Braze dans le [standard ISO-639-1][24].<br>[Liste des langues acceptées][2]                                                                                                                                                                                      |
| nom_de famille                   | (chaîne)                                                                                                                                                                                                                                                                                                                  |
| Marqué comme spam à              | (chaîne) Date à laquelle l'email de l'utilisateur a été marqué comme spam. Apparaît au format ISO 8601 ou au format yyyy-MM-dd'T'H:mm:ss:SSSZ.                                                                                                                                                                            |
| Téléphone                        | (chaîne)                                                                                                                                                                                                                                                                                                                  |
| Poussez vous abonner             | (string) Les valeurs disponibles sont "opted_in" (explicitement enregistrées pour recevoir des messages push), "unsubscribed" (explicitement opted out of push messages), et "subscribed" (ni opted in ni out).                                                                                                           |
| Pousse_tokens                    | Tableau d'objets avec la chaîne `app_id` et `token`. Vous pouvez éventuellement fournir un `device_id` pour l'appareil auquel ce jeton est associé. ., `[{"app_id": Identifiant d'application, "token": "abcd", "device_id": "optional_field_value"}]`. Si un `device_id` n'est pas fourni, on sera généré aléatoirement. |
| fuseau horaire                   | (string) Of time zone name from [IANA Time Zone Database][26] (e.g., "America/New_York" or "Eastern Time (US & Canada)"). Seules les valeurs de fuseau horaire valides seront définies.                                                                                                                                   |
| twitter                          | Hash contenant l'un des `id` (entier), `nom_écran` (chaîne, gestionnaire Twitter), `followers_count` (entier), `friends_count` (entier), `statuses_count` (entier).                                                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2}

Les valeurs de langue qui sont explicitement définies via cette API auront la priorité sur les informations locales que Braze reçoit automatiquement de l'appareil.

#### Exemple de demande d'attribut utilisateur

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes" : [
    {
      "external_id" : "user1",
      "prénom" : "Jon",
      "has_profile_picture" : true,
      "dobe": "1988-02-14",
      "music_videos_favorited" : { "add" : [ "calvinharris-summer" ], "remove" : ["nickiminaj-anaconda"] }
    },
    {
      "external_id" : "user2",
      "prénom" : "Jill",
      "has_profile_picture" : false,
      "push_tokens": [{"app_id": Identifiant d'application, "token": "abcd", "device_id": "optional_field_value"}]

    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "prénom" : "Alice",
      "has_profile_picture" : false,
    }
  ]
}
```

Cet exemple contient deux objets d'Attribut Utilisateur des 75 autorisés par appel API.


[2]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[3]: {{site.baseurl}}/help/help_articles/push/push_token_migration/
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[15]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[17]: http://en.wikipedia.org/wiki/ISO_3166-1 "ISO-3166-1 codes"
[19]: http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Time Code Wiki"
[24]: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes "ISO-639-1 codes"
[26]: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
[27]: #braze-user-profile-fields
