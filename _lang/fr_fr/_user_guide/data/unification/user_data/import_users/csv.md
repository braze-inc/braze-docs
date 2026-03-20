---
nav_title: Importation CSV
article_title: "Importation CSV"
description: "Découvrez comment enregistrer et mettre à jour les attributs utilisateur et les événements personnalisés à l'aide de l'importation CSV."
page_order: 1.2
---

# Importation CSV

> Découvrez comment enregistrer et mettre à jour les attributs utilisateur et les événements personnalisés à l'aide de l'importation CSV.

## À propos de l'importation CSV

Vous pouvez utiliser l'importation CSV pour enregistrer et mettre à jour les attributs utilisateur et les événements personnalisés suivants.

|Type|Définition|Exemple|Taille maximale du fichier|
|---|---|---|---|
|Attributs par défaut|Attributs utilisateur réservés reconnus par Braze.|`first_name`, `email`|500 Mo|
|Attributs personnalisés|Attributs utilisateur propres à votre entreprise.|`last_destination_searched`|500 Mo|
|Événements personnalisés|Événements propres à votre entreprise qui représentent des actions de l'utilisateur.|`trip_booked`|50 Mo|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Utilisation de l'importation CSV

### Étape 1 : Télécharger un modèle CSV

Pour ouvrir l'importation CSV, accédez à **Audiences** > **Importer des utilisateurs**. Vous y trouverez un tableau répertoriant les détails des importations les plus récentes, tels que la date de téléchargement, le nom de la personne ayant effectué le téléchargement, le nom du fichier, la disponibilité du ciblage, le nombre de lignes importées et le statut de l'importation.

Pour démarrer avec votre CSV, téléchargez un modèle pour les attributs ou les événements.

![La page « Importer des utilisateurs » dans le tableau de bord de Braze.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### Étape 2 : Choisir un identifiant {#choose-an-identifier}

Le fichier CSV que vous importez nécessite un identifiant dédié. Vous pouvez choisir parmi les options suivantes :

{% tabs local %}
<!-- TAB -->
{% tab external id %}
Lors de l'importation de vos données clients, vous pouvez utiliser un `external_id` comme identifiant unique pour chaque client. Lorsque vous fournissez un `external_id` dans votre importation, Braze met à jour tout utilisateur existant avec le même `external_id` ou crée un nouvel utilisateur identifié avec cet `external_id` si aucun n'est trouvé.

- Télécharger : [Modèle d'importation des attributs CSV : ID externe]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Télécharger : [Modèle d'importation d'événements CSV : ID externe](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %} 
Si vous téléchargez un mélange d'utilisateurs avec un `external_id` et d'utilisateurs sans, vous devez créer un fichier CSV pour chaque importation. Un fichier CSV ne peut pas contenir à la fois des `external_ids` et des alias d'utilisateurs.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
Pour cibler les utilisateurs qui ne disposent pas d'un `external_id`, vous pouvez importer une liste d'utilisateurs avec des alias d'utilisateurs. Un alias sert d'identifiant utilisateur unique alternatif et peut être utile si vous souhaitez cibler des utilisateurs anonymes qui ne se sont pas inscrits ou n'ont pas créé de compte sur votre application.

Si vous téléchargez ou mettez à jour des profils utilisateur qui sont uniquement des alias, les deux colonnes suivantes doivent figurer dans votre CSV :

- `user_alias_name` : Un identifiant utilisateur unique ; une alternative à l'`external_id`  
- `user_alias_label` : Un libellé commun permettant de regrouper les alias d'utilisateurs

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

Lorsque vous fournissez à la fois un `user_alias_name` et un `user_alias_label` dans votre importation, Braze met à jour tout utilisateur existant avec le même `user_alias_name` et `user_alias_label`. Si aucun utilisateur n'est trouvé, Braze crée un nouvel utilisateur identifié avec ce `user_alias_name`.

{% alert important %}
Il n'est pas possible d'utiliser l'importation CSV pour mettre à jour un utilisateur existant avec un `user_alias_name` s'il dispose déjà d'un `external_id`. Cela crée à la place un nouveau profil utilisateur avec le `user_alias_name` associé. Pour associer un utilisateur avec alias uniquement à un `external_id`, utilisez l'[endpoint Identifier les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

Télécharger : [Modèle d'importation des attributs CSV : Alias d'utilisateur]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
Pour mettre à jour les profils utilisateur existants dans Braze en utilisant un ID Braze interne au lieu d'un `external_id` ou d'un `user_alias_name` et `user_alias_label`, spécifiez `braze_id` comme en-tête de colonne.

Cela peut s'avérer utile si vous avez exporté des données utilisateur depuis Braze via l'option d'exportation CSV dans la segmentation et que vous souhaitez ajouter un nouvel attribut personnalisé à ces utilisateurs existants.

{% alert important %}
Il n'est pas possible d'utiliser l'importation CSV pour créer un nouvel utilisateur avec `braze_id`. Cette méthode ne peut être utilisée que pour mettre à jour des utilisateurs existants sur la plateforme Braze.  
{% endalert %}

{% alert tip %}
La valeur `braze_id` peut être étiquetée comme `Appboy ID` dans les exportations CSV du tableau de bord de Braze. Cet ID est identique au `braze_id` d'un utilisateur, vous pouvez donc renommer cette colonne en `braze_id` lorsque vous réimportez le CSV.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab email address and phone numbers %}
Vous pouvez omettre un ID externe ou un alias d'utilisateur et utiliser une adresse e-mail ou un numéro de téléphone pour importer des utilisateurs. Avant d'importer un fichier CSV contenant des adresses e-mail ou des numéros de téléphone, vérifiez les points suivants :

- Vérifiez que vous n'avez pas d'ID externes ou d'alias d'utilisateurs pour ces profils dans votre fichier CSV. Si c'est le cas, Braze utilisera en priorité l'ID externe ou l'alias d'utilisateur avant l'adresse e-mail pour identifier les profils.  
- Confirmez que votre fichier CSV est correctement formaté.  

{% alert note %}
Si vous incluez à la fois des adresses e-mail et des numéros de téléphone dans votre fichier CSV, l'adresse e-mail est prioritaire sur le numéro de téléphone lors de la recherche de profils.
{% endalert %}

Si un profil existant possède cette adresse e-mail ou ce numéro de téléphone, ce profil est mis à jour et Braze ne crée pas de nouveau profil. S'il existe plusieurs profils avec la même adresse e-mail, Braze applique la même logique que l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) : le profil le plus récemment mis à jour sera mis à jour.

Si aucun profil n'existe avec cette adresse e-mail ou ce numéro de téléphone, Braze crée un nouveau profil avec cet identifiant. Vous pouvez utiliser l'[endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) pour identifier ce profil ultérieurement. Pour supprimer un profil utilisateur, vous pouvez également utiliser l'endpoint [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).
{% endtab %}
{% endtabs %}

### Étape 3 : Créer votre fichier CSV

Vous pouvez télécharger l'un des types de données suivants sous forme de fichier CSV unique. Pour télécharger plusieurs types de données, utilisez plusieurs fichiers CSV.

- **Attributs utilisateur :** Cela inclut les attributs utilisateur par défaut et personnalisés. Les attributs utilisateur par défaut sont des clés réservées dans Braze (telles que `first_name` ou `email`) et les attributs personnalisés sont des attributs utilisateur propres à votre entreprise (tels que `last_destination_searched`).  
- **Événements personnalisés :** Ces événements sont propres à votre entreprise et reflètent les actions effectuées par un utilisateur, par exemple `trip_booked` pour une application de réservation de voyages.

Lorsque vous êtes prêt à créer votre fichier CSV, consultez les informations suivantes :

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### Identifiants requis {#required-identifiers-attributes}

Bien que `external_id` ne soit pas obligatoire, vous **devez** inclure **l'un** des identifiants suivants comme en-tête dans votre fichier CSV. Pour plus de détails sur chacun d'entre eux, consultez [Choisir un identifiant](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **et** `user_alias_label`
- `email`
- `phone`

#### Attributs personnalisés

Les types de données suivants peuvent être utilisés comme attributs personnalisés pour l'importation CSV. Les en-têtes de colonne qui ne correspondent pas exactement à un [attribut par défaut](#default-attributes) sont importés en tant qu'attributs personnalisés dans Braze.

| Type de données | Description |
|---|---|
| Date et heure | Doit être enregistré au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601). |
| Valeur booléenne | Accepte `true` ou `false`. |
| Nombre | Doit être un nombre entier ou un float, sans espaces ni virgules. Les floats doivent utiliser un point (`.`) comme séparateur décimal. |
| Chaîne de caractères | Peut contenir des virgules si la valeur est encadrée par des guillemets doubles (`""`). |
| Vide | Les valeurs vides ne remplaceront pas les valeurs existantes dans le profil utilisateur, et il n'est pas nécessaire d'inclure tous les attributs utilisateur existants dans votre fichier CSV. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Les tableaux, les jetons de notification push et les types de données d'événements personnalisés ne sont pas pris en charge dans l'importation d'utilisateurs, car les virgules dans votre fichier CSV seront interprétées comme des séparateurs de colonnes et entraîneront des erreurs lors de l'analyse du fichier.<br><br>Pour télécharger ce type de valeurs, utilisez l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ou l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/cloud_ingestion/).
{% endalert %} 

#### Attributs par défaut

{% alert important %}
Lors de l'importation d'attributs par défaut, les en-têtes de colonne que vous utilisez doivent correspondre exactement à l'orthographe et à la casse des attributs utilisateur par défaut. Dans le cas contraire, Braze les détecte comme des [attributs personnalisés](#custom-attributes).
{% endalert %}

Les attributs par défaut suivants sont disponibles pour l'importation d'utilisateurs.

| Champ du profil utilisateur | Type de données | Description | Requis ? |
| :---- | :---- | :---- | :---- |
| `external_id` | Chaîne de caractères | Un identifiant utilisateur unique pour votre client. | Sous certaines conditions. Consultez [Identifiants requis](#required-identifiers-attributes). |
| `user_alias_name` | Chaîne de caractères | Un identifiant utilisateur unique pour les utilisateurs anonymes, constituant une alternative à `external_id`. Doit être utilisé avec `user_alias_label`. | Sous certaines conditions. Consultez [Identifiants requis](#required-identifiers-attributes). |
| `user_alias_label` | Chaîne de caractères | Un libellé commun pour regrouper les alias d'utilisateurs. Doit être utilisé avec `user_alias_name`. | Sous certaines conditions. Consultez [Identifiants requis](#required-identifiers-attributes). |
| `first_name` | Chaîne de caractères | Le prénom de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `Jane`). | Non |
| `last_name` | Chaîne de caractères | Le nom de famille de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `Doe`). | Non |
| `email` | Chaîne de caractères | L'adresse e-mail de vos utilisateurs telle qu'ils l'ont indiquée (par exemple, `jane.doe@braze.com`). | Non |
| `country` | Chaîne de caractères | Les codes pays doivent être transmis à Braze selon la norme ISO-3166-1 alpha-2 (par exemple, `GB`). | Non |
| `dob` | Chaîne de caractères | Doit être transmis au format « AAAA-MM-JJ » (par exemple, `1980-12-21`). Cela importe la date de naissance de vos utilisateurs et vous permet de cibler les utilisateurs dont l'anniversaire est « aujourd'hui ». | Non |
| `gender` | Chaîne de caractères | « M », « F », « O » (autre), « N » (sans objet), « P » (préfère ne pas dire) ou nil (inconnu). | Non |
| `home_city` | Chaîne de caractères | La ville de résidence de vos utilisateurs telle qu'ils l'ont indiquée (par exemple, `London`). | Non |
| `language` | Chaîne de caractères | La langue doit être transmise à Braze selon la norme ISO-639-1 (par exemple, `en`). Consultez notre [liste des langues acceptées]({{site.baseurl}}/user_guide/data/user_data_collection/language_codes/). | Non |
| `phone` | Chaîne de caractères | Un numéro de téléphone tel qu'indiqué par vos utilisateurs, au format `E.164` (par exemple, `+442071838750`). Consultez [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) pour des conseils de formatage. | Non |
| `email_open_tracking_disabled` | Valeur booléenne | true ou false accepté. Définissez sur true pour désactiver le pixel de suivi d'ouverture dans tous les futurs e-mails envoyés à cet utilisateur. Disponible uniquement pour SparkPost et Sendgrid. | Non |
| `email_click_tracking_disabled` | Valeur booléenne | true ou false accepté. Définissez sur true pour désactiver le suivi des clics pour tous les liens dans les futurs e-mails envoyés à cet utilisateur. Disponible uniquement pour SparkPost et Sendgrid. | Non |
| `email_subscribe` | Chaîne de caractères | Les valeurs disponibles sont `opted_in` (a explicitement consenti à recevoir des e-mails), `unsubscribed` (a explicitement refusé de recevoir des e-mails) et `subscribed` (ni accepté, ni refusé). | Non |
| `push_subscribe` | Chaîne de caractères | Les valeurs disponibles sont `opted_in` (a explicitement consenti à recevoir des notifications push), `unsubscribed` (a explicitement refusé de recevoir des notifications push) et `subscribed` (ni accepté, ni refusé). | Non |
| `time_zone` | Chaîne de caractères | Le fuseau horaire doit être transmis à Braze dans le même format que la base de données des fuseaux horaires de l'IANA (par exemple, `America/New_York` ou `Eastern Time (US & Canada)`). | Non |
| `date_of_first_session`  `date_of_last_session` | Chaîne de caractères | Peut être transmis dans l'un des formats ISO 8601 suivants : « AAAA-MM-JJ » « AAAA-MM-JJTHH:MM:SS+00:00 » « AAAA-MM-JJTHH:MM:SSZ » « AAAA-MM-JJTHH:MM:SS » (par exemple, 2019-11-20T18:38:57) | Non |
| `subscription_group_id` | Chaîne de caractères | L'`id` de votre groupe d'abonnement. Cet identifiant se trouve sur la page du groupe d'abonnement de votre tableau de bord. | Non |
| `subscription_state` | Chaîne de caractères | Le statut d'abonnement du groupe d'abonnement spécifié par `subscription_group_id`. Les valeurs autorisées sont `unsubscribed` (pas dans le groupe d'abonnement) ou `subscribed` (dans le groupe d'abonnement). | Non, mais fortement recommandé si `subscription_group_id` est utilisé |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### Mise à jour du statut du groupe d'abonnement (facultatif)

Vous pouvez également ajouter des utilisateurs à des groupes d'abonnement par e-mail ou SMS via l'importation d'utilisateurs. Ceci est particulièrement utile pour les SMS, car un utilisateur doit être inscrit dans un groupe d'abonnement SMS pour recevoir des messages via le canal SMS. Pour plus d'informations, consultez [Groupes d'abonnement SMS](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Si vous mettez à jour les statuts du groupe d'abonnement, les deux colonnes suivantes doivent figurer dans votre fichier CSV :

- `subscription_group_id` : L'`id` du [groupe d'abonnement](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).  
- `subscription_state` : Les valeurs disponibles sont `unsubscribed` (pas dans le groupe d'abonnement) ou `subscribed` (dans le groupe d'abonnement).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | subscribed |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | subscribed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert note %}
Un seul `subscription_group_id` peut être défini par ligne dans l'importation d'utilisateurs. Différentes lignes peuvent avoir différentes valeurs `subscription_group_id`. Toutefois, si vous devez inscrire les mêmes utilisateurs dans plusieurs groupes d'abonnement, vous devrez effectuer plusieurs importations.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### Identifiants requis {#required-identifiers-custom-events}

Bien que `external_id` ne soit pas obligatoire, vous **devez** inclure **l'un** des identifiants suivants comme en-tête dans votre fichier CSV. Pour plus de détails sur chacun d'entre eux, consultez [Choisir un identifiant](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **et** `user_alias_label`
- `email`
- `phone`

#### Champs des événements personnalisés

En plus des éléments suivants, votre fichier CSV peut également contenir des en-têtes de colonnes supplémentaires pour les propriétés d'événement. Ces propriétés doivent avoir un en-tête de colonne au format `<event_name>.properties.<property name>.`

Par exemple, l'événement personnalisé `trip_booked` peut avoir les propriétés `destination` et `duration`. Celles-ci peuvent être importées en utilisant les en-têtes de colonne `trip_booked.properties.destination` et `trip_booked.properties.duration`.

| Champ du profil utilisateur | Type de données | Information | Requis ? |
| :---- | :---- | :---- | :---- |
| `external_id` | Chaîne de caractères | Un identifiant utilisateur unique pour votre utilisateur. | Sous certaines conditions. Consultez [Identifiants requis](#required-identifiers-custom-events). |
| `braze_id` | Chaîne de caractères | Un identifiant attribué par Braze à votre utilisateur. | Sous certaines conditions. Consultez [Identifiants requis](#required-identifiers-custom-events). |
| `user_alias_name` | Chaîne de caractères | Un identifiant utilisateur unique pour les utilisateurs anonymes, constituant une alternative à `external_id`. Doit être utilisé avec `user_alias_label`. | Sous certaines conditions. Consultez [Identifiants requis](#required-identifiers-custom-events). |
| `user_alias_label` | Chaîne de caractères | Un libellé commun pour regrouper les alias d'utilisateurs. Doit être utilisé avec `user_alias_name`. | Sous certaines conditions. Consultez [Identifiants requis](#required-identifiers-custom-events). |
| `email` | Chaîne de caractères | L'adresse e-mail de vos utilisateurs telle qu'ils l'ont indiquée (par exemple, `jane.doe@braze.com`). | Non, et ne peut être utilisé qu'en l'absence d'autres identifiants. Consultez la note suivante. |
| `phone` | Chaîne de caractères | Un numéro de téléphone tel qu'indiqué par vos utilisateurs, au format `E.164` (par exemple, `+442071838750`). Consultez [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) pour des conseils de formatage. | Non, et ne peut être utilisé qu'en l'absence d'autres identifiants. Consultez la note suivante. |
| `name` | Chaîne de caractères | Un événement personnalisé de vos utilisateurs. | Oui |
| `time` | Chaîne de caractères | L'heure de l'événement. Peut être transmis dans l'un des formats ISO-8601 suivants : « AAAA-MM-JJ » « AAAA-MM-JJTHH:MM:SS+00:00 » « AAAA-MM-JJTHH:MM:SSZ » « AAAA-MM-JJTHH:MM:SS » (par exemple, 2019-11-20T18:38:57) | Oui |
| `<event name>.properties.<property name>` | Plusieurs | Une propriété d'événement associée à un événement personnalisé. Par exemple `trip_booked.properties.destination` | Non |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endtab %}
{% endtabs %}

### Étape 4 : Télécharger votre fichier

Pour télécharger votre fichier, sélectionnez **Attributs** ou **Événements**, cliquez sur **Parcourir les fichiers**, puis téléchargez votre fichier CSV. Braze affiche un aperçu des premières lignes et un résumé des champs détectés.

![La fenêtre modale de téléchargement terminé affichant un aperçu du fichier, le champ de nom d'importation, les préférences de ciblage et la case à cocher de validation du fichier.]({% image_buster /assets/img/csv_import/upload_completed.png %})

Dans le champ **Nom de l'importation**, vous pouvez renommer votre importation. Par défaut, le nom du fichier est utilisé.

{% alert note %}
L'aperçu du fichier n'affiche que les premières lignes de votre fichier. Pour vérifier chaque ligne avant l'importation, utilisez la [validation de fichier](#file-validation).
{% endalert %}

### Étape 5 : Valider votre fichier (facultatif) {#file-validation}

Avant de lancer votre importation, vous pouvez exécuter une validation de fichier pour vérifier chaque ligne à la recherche d'erreurs et d'avertissements. Pour valider votre fichier, sélectionnez **Valider le fichier avant l'importation**, puis cliquez sur **Démarrer l'importation**.

La validation peut prendre jusqu'à 2 minutes pour les fichiers à la taille maximale autorisée. Pendant l'exécution de la validation, vous pouvez sélectionner **Ignorer la validation** pour la contourner et continuer immédiatement.

#### Résultats de la validation

Une fois la validation terminée, l'un des résultats suivants s'affiche.

| Résultat | Signification | Étape suivante |
|---|---|---|
| **Validation terminée** | Aucun problème détecté. | Sélectionnez **Importer les données**. |
| **Problèmes détectés** | Certaines lignes contiennent des erreurs ou des avertissements. | Téléchargez le rapport d'erreurs pour les examiner, puis sélectionnez **Importer quand même** pour continuer ou **Annuler** pour corriger votre fichier au préalable. |
| **Délai de validation expiré** | La validation a expiré. Les lignes vérifiées ne présentaient aucun problème. | Sélectionnez **Importer les données**. Un rapport complet sera disponible dans quelques minutes. |
| **Délai de validation expiré avec des problèmes** | La validation a expiré et a détecté des erreurs dans certaines des lignes vérifiées. | Téléchargez le rapport partiel pour examiner les résultats, puis sélectionnez **Importer quand même** ou **Annuler**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

![La boîte de dialogue « Problèmes détectés » affichant le nombre de lignes contenant des erreurs et des avertissements, avec des options pour annuler, télécharger le rapport d'erreurs ou importer quand même.]({% image_buster /assets/img/csv_import/validation_issues.png %})

#### Comprendre le rapport d'erreurs

Le rapport d'erreurs est un fichier CSV qui contient toutes les lignes signalées, avec leurs données d'origine et une description du problème.

| Type de problème | Description |
|---|---|
| **Erreur** | La ligne sera entièrement ignorée lors de l'importation. |
| **Avertissement** | La ligne sera importée, mais certaines valeurs seront supprimées. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Après avoir examiné le rapport, vous pouvez corriger les problèmes dans votre fichier d'origine et le télécharger à nouveau, ou procéder à l'importation et accepter les résultats partiels.

### Étape 6 : Choisir les préférences de ciblage

Vous pouvez également choisir parmi les préférences de ciblage suivantes. Si vous n'avez pas besoin de créer un nouveau filtre de ciblage ou segment à partir de votre importation, sélectionnez **Ne pas rendre cette liste disponible en tant que filtre de ciblage**.

| Option | Description |
|---|---|
| Filtre de ciblage | Pour convertir votre fichier CSV en option de reciblage lors de la création de segments d'utilisateurs, sélectionnez votre fichier dans le menu déroulant **Mis à jour/Importé depuis CSV**, puis sélectionnez **Créer un filtre de ciblage**. |
| Nouveaux segments | Pour créer également un nouveau segment à partir de votre nouveau filtre de ciblage, sélectionnez **Créer un filtre de ciblage et ajouter au nouveau segment**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Un groupe de filtres avec le filtre « Mis à jour/Importé depuis CSV » incluant un fichier CSV intitulé « Halloween season fun ».]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### Étape 7 : Lancer votre importation CSV

Lorsque vous êtes prêt, sélectionnez **Démarrer l'importation**. Vous pouvez suivre la progression en cours sur la page **Importer des utilisateurs**, qui s'actualise automatiquement toutes les 5 secondes.

{% alert note %}
Vous pouvez importer plusieurs fichiers CSV en même temps. Les importations CSV s'exécutent simultanément, de sorte que l'ordre des mises à jour n'est pas garanti. Si vous souhaitez que les importations CSV s'exécutent l'une après l'autre, attendez qu'une importation CSV soit terminée avant d'en télécharger une seconde.
{% endalert %}

#### Statuts d'importation

Après avoir lancé votre importation, vous pouvez vérifier son statut sur la page **Importer des utilisateurs**.

| État | Description |
|---|---|
| **Terminé** | Toutes les lignes ont été importées avec succès. |
| **Succès partiel** | Certaines lignes ont échoué. Sélectionnez le menu à trois points à côté de l'importation pour télécharger un rapport d'erreurs ou le fichier CSV original téléchargé. |
| **En cours** | L'importation est actuellement en cours. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![La page Importer des utilisateurs affichant un statut de succès partiel avec le menu contextuel ouvert, présentant les options Télécharger le rapport d'erreurs et Télécharger le fichier CSV téléchargé.]({% image_buster /assets/img/csv_import/partial_success_menu.png %})

Le rapport d'erreurs post-importation inclut les lignes qui ont échoué pour des raisons non couvertes par la validation, par exemple lorsqu'un utilisateur n'existe pas dans Braze.

{% alert important %}
Les fichiers CSV précédemment téléchargés sont disponibles au téléchargement depuis la page **Importer des utilisateurs** pendant 14 jours après la date de téléchargement. Passé ce délai, le fichier est définitivement supprimé et ne peut plus être consulté.
{% endalert %}

## Considérations relatives aux points de données

Chaque donnée client importée à partir d'un fichier CSV remplace la valeur existante dans les profils utilisateur et enregistre un point de donnée, à l'exception des ID externes et des valeurs vides. Si vous avez des questions sur les subtilités des points de données Braze, votre Account Manager Braze peut y répondre.

| Considération | Détails |
|---|---|
| ID externes | Le téléchargement d'un fichier CSV contenant uniquement `external_id` n'enregistre pas de points de données. Cela vous permet de segmenter les utilisateurs Braze existants sans affecter les limites de données. Cependant, l'inclusion de champs tels que `email` ou `phone` écrase les données utilisateur existantes et **enregistre** des points de données. <br><br>Les importations CSV utilisées uniquement à des fins de segmentation n'enregistrent pas de points de données, comme celles contenant uniquement `external_id`, `braze_id` ou `user_alias_name`. |
| Valeurs vides | Les valeurs vides dans votre fichier CSV ne remplaceront pas les données existantes du profil utilisateur. Il n'est pas nécessaire d'inclure tous les attributs utilisateur ou événements personnalisés lors de l'importation. |
| Statuts d'abonnement | La mise à jour de `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` n'est **pas** comptabilisée dans l'utilisation des points de données. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Définir `language` ou `country` sur un utilisateur via l'importation CSV ou l'API empêche Braze de capturer automatiquement ces informations via le SDK.
{% endalert %}

## Résolution des problèmes

Si vous avez utilisé la [validation de fichier](#file-validation), commencez par le rapport d'erreurs, car il contient le problème spécifique pour chaque ligne signalée et une description de la manière de le résoudre. Pour les lignes qui ont échoué lors de l'importation plutôt que lors de la validation, téléchargez le rapport d'erreurs en survolant la ligne et en sélectionnant le bouton <i class="fas fa-download" title="Download"></i> sur la page **Importer des utilisateurs**.

Pour résoudre les problèmes d'importation CSV, consultez les problèmes courants ci-dessous.

### Problèmes de formatage des fichiers

#### Ligne mal formée

Si votre téléchargement s'est terminé avec des erreurs, il se peut qu'il y ait une ligne mal formée dans votre fichier CSV. 

Pour importer correctement les données, une ligne d'en-tête est nécessaire. Chaque ligne doit avoir le même nombre de cellules que la ligne d'en-tête. Les lignes ayant plus ou moins de valeurs que la ligne d'en-tête seront exclues de l'importation. Les virgules dans une valeur seront interprétées comme un séparateur et peuvent entraîner cette erreur. De plus, toutes les données doivent être encodées en UTF-8.

Si votre fichier CSV contient des lignes vides et que le nombre de lignes importées est inférieur au nombre total de lignes du fichier CSV, cela n'indique pas nécessairement un problème avec l'importation, car les lignes vides n'ont pas besoin d'être importées. Vérifiez le nombre de lignes correctement importées et assurez-vous qu'il correspond au nombre d'utilisateurs que vous essayez d'importer.

#### Ligne manquante

Plusieurs raisons peuvent expliquer pourquoi le nombre d'utilisateurs importés ne correspond pas au nombre total de lignes dans votre fichier CSV :

| Problème | Résolution |
|---|---|
| ID externes, alias d'utilisateurs, ID Braze, adresses e-mail ou numéros de téléphone en double | Si des colonnes d'ID externe sont dupliquées, cela peut entraîner des lignes mal formées ou non importées, même si les lignes sont correctement formatées. Dans certains cas, aucune erreur spécifique n'est signalée. Vérifiez s'il existe des doublons et supprimez-les avant de procéder à un nouveau téléchargement. |
| Caractères accentués | Votre fichier CSV peut contenir des noms ou des attributs comportant des accents. Assurez-vous que le fichier est encodé en UTF-8 afin d'éviter tout problème lors de l'importation. |
| L'ID Braze appartient à un utilisateur orphelin | Si un utilisateur a été fusionné avec un autre et que Braze ne parvient pas à associer l'ID Braze au profil restant, la ligne ne sera pas importée. |
| Ligne vide | Les lignes vides dans le fichier CSV peuvent entraîner des erreurs de données mal formées. Vérifiez à l'aide d'un éditeur de texte brut, et non d'Excel ou de Sheets. |
| Guillemets doubles non échappés ou non équilibrés (`"`) | Les guillemets doubles encadrent les valeurs de chaîne de caractères contenant des virgules. Si une valeur contient elle-même un guillemet double, échappez-le en le doublant (`""`). Les guillemets doubles non échappés ou déséquilibrés entraînent une ligne mal formée. |
| Sauts de ligne incohérents | Des sauts de ligne mixtes (par exemple, `\n` et `\r\n`) peuvent entraîner le traitement de la première ligne de données comme faisant partie de l'en-tête. Utilisez un éditeur hexadécimal ou un éditeur de texte avancé pour examiner et corriger. |
| Fichier mal encodé | Même si les accents sont autorisés, le fichier doit être encodé en UTF-8. D'autres encodages peuvent fonctionner partiellement, mais ne sont pas entièrement pris en charge. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Guillemets de chaîne de caractères

Les valeurs encadrées par des guillemets simples (`''`) ou doubles (`""`) seront lues comme des chaînes de caractères lors de l'importation.

#### Dates incorrectement formatées

Les dates qui ne sont pas au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ne seront pas lues comme `datetimes` lors de l'importation.

### Problèmes liés à la structure des données

#### Adresses e-mail non valides

Si votre téléchargement s'est terminé avec des erreurs, il se peut qu'une ou plusieurs adresses e-mail chiffrées soient non valides. Assurez-vous que toutes les adresses e-mail sont correctement chiffrées avant de les importer dans Braze.

- **Lors de la [mise à jour ou de l'importation d'adresses e-mail]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)** dans Braze, utilisez la valeur hachée de l'adresse e-mail chaque fois qu'une adresse e-mail est incluse. Ces valeurs hachées sont fournies par votre équipe interne. 
- **Lors de la création d'un nouvel utilisateur**, vous devez ajouter `email_encrypted` avec la valeur chiffrée de l'adresse e-mail de l'utilisateur. Dans le cas contraire, Braze ne créera pas l'utilisateur. De même, si vous ajoutez une adresse e-mail à un utilisateur existant qui n'en possède pas, vous devez ajouter `email_encrypted`. Dans le cas contraire, Braze ne mettra pas à jour l'utilisateur.

#### Données importées comme attribut personnalisé

Si une donnée utilisateur par défaut (telle que `email` ou `first_name`) est importée en tant qu'attribut personnalisé, vérifiez la casse et l'espacement de votre fichier CSV. Par exemple, `First_name` est importé en tant qu'attribut personnalisé, tandis que `first_name` est correctement importé dans le champ « prénom » du profil utilisateur.

#### Modifier le type de données d'un attribut personnalisé

Si vous devez modifier le type de données d'un attribut personnalisé existant (par exemple, de chaîne de caractères à valeur booléenne), mettez à jour le type de données sur la page [**Attributs personnalisés**]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) du tableau de bord avant d'importer votre CSV. Si le type de données dans votre CSV ne correspond pas au type de données actuellement défini pour l'attribut, l'importation échoue avec une erreur.

#### Plusieurs types de données

Braze s'attend à ce que toutes les valeurs d'une colonne soient du même type de données. Les valeurs qui ne correspondent pas au type de données de leur attribut entraînent des erreurs de segmentation.

De plus, commencer un attribut numérique par zéro peut entraîner des problèmes, car les nombres commençant par zéro sont considérés comme des chaînes de caractères. Lorsque Braze convertit cette chaîne, elle peut être traitée comme une valeur octale (qui utilise les chiffres de zéro à sept), ce qui signifie qu'elle est convertie en sa valeur décimale correspondante. Par exemple, si la valeur dans le fichier CSV est 0130, le profil Braze affiche 88. Pour éviter ce problème, utilisez des attributs avec des types de données de chaîne de caractères. Cependant, ce type de données n'est pas disponible dans la comparaison numérique de la segmentation.

#### Types d'attributs par défaut

Certains attributs par défaut n'acceptent que certaines valeurs comme valides pour les mises à jour utilisateur. Pour des conseils, consultez [Créer votre fichier CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Les espaces en fin de chaîne et les différences de casse peuvent entraîner l'interprétation d'une valeur comme non valide. Par exemple, dans le fichier CSV suivant, seul l'utilisateur de la première ligne (`brazetest1`) voit ses statuts e-mail et push mis à jour avec succès, car les valeurs acceptées sont `unsubscribed`, `subscribed` et `opted_in`. 

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### « Sélectionner un fichier CSV » ne fonctionne pas

Plusieurs raisons peuvent expliquer pourquoi le bouton **Sélectionner un fichier CSV** ne fonctionne pas :

| Problème | Résolution |
|---|---|
| Bloqueur de fenêtres contextuelles | Cela pourrait empêcher l'affichage de la page. Vérifiez que votre navigateur autorise les fenêtres contextuelles sur le site du tableau de bord de Braze. |
| Navigateur obsolète | Assurez-vous que votre navigateur est à jour ; si ce n'est pas le cas, mettez-le à jour vers la dernière version. |
| Processus en arrière-plan | Fermez toutes les instances de votre navigateur, puis redémarrez votre ordinateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}