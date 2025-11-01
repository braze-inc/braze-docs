---
nav_title: "Utilisation d'un fichier CSV"
article_title: "Importation CSV"
description: "Découvrez comment enregistrer et mettre à jour les événements personnalisés et les attributs des utilisateurs à l'aide de l'importation CSV."
page_order: 1.2
---

# Importation CSV

> Découvrez comment enregistrer et mettre à jour les événements personnalisés et les attributs des utilisateurs à l'aide de l'importation CSV.

## A propos de l'importation CSV

Vous pouvez utiliser l'importation CSV pour enregistrer et mettre à jour les événements personnalisés et les attributs utilisateurs suivants.

|Type|Définition|Exemple|Taille maximale du fichier|
|---|---|---|---|
|Attribut par défaut|Attributs réservés de l'utilisateur reconnus par Braze.|`first_name`, `email`|500 MO|
|Attributs personnalisés|Attributs de l'utilisateur uniques à votre entreprise.|`last_destination_searched`|500 MO|
|Événements personnalisés|Événements uniques à votre entreprise qui représentent des actions de l'utilisateur.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Utilisation de l'importation CSV

### Étape 1 : Téléchargez un modèle CSV

Pour ouvrir l'importation CSV, allez dans **Audiences** > Importer des **utilisateurs.** Vous y trouverez un tableau qui répertorie les détails des importations les plus récentes, tels que la date de téléchargement, le nom du téléchargeur, le nom du fichier, la disponibilité du ciblage, le nombre de lignes importées et l'état de l'importation.

Pour commencer votre CSV, téléchargez un modèle pour les attributs ou les événements.

La page "Importation d'utilisateurs" du tableau de bord de Braze.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### Étape 2 : Choisissez un identifiant {#choose-an-identifier}

Le fichier CSV que vous importez aura besoin d'un identifiant spécifique. Vous avez le choix entre les options suivantes :

{% tabs local %}
<!-- TAB -->
{% tab external id %}
Lors de l'importation de vos données clients, vous pouvez utiliser un `external_id` qui servira d'identifiant unique pour chaque client. Lorsque vous fournissez un `external_id` dans votre importation, Braze met à jour tout utilisateur existant avec le même `external_id` ou crée un nouvel utilisateur identifié avec ce jeu de `external_id` s'il n'y en a pas.

- Télécharger : [Modèle d'importation d'attributs CSV : ID externe]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Télécharger : [Modèle d'importation d'événements CSV : ID externe](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
Si vous téléchargez un mélange d'utilisateurs avec `external_id` et d'utilisateurs sans , vous devez créer un CSV pour chaque importation. Un CSV ne peut pas contenir à la fois `external_ids` et des aliasing de l'utilisateur.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
Pour cibler les utilisateurs qui n'ont pas d'alias `external_id`, vous pouvez importer une liste d'utilisateurs ayant des alias. Un alias sert d'identifiant unique alternatif pour l'utilisateur et peut être utile si vous essayez de marketeur des utilisateurs anonymes qui ne se sont pas inscrits ou n'ont pas créé de compte avec votre application.

Si vous téléchargez ou mettez à jour des profils utilisateurs qui sont uniquement des alias, vous devez avoir les deux colonnes suivantes dans votre CSV :

- `user_alias_name`: Un identifiant unique de l'utilisateur ; une alternative à l'identifiant de l'utilisateur. `external_id`  
- `user_alias_label`: Une étiquette commune permettant de regrouper les alias utilisateurs.

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | VRAI |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FAUX |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

Lorsque vous fournissez à la fois `user_alias_name` et `user_alias_label` dans votre importation, Braze mettra à jour tout utilisateur existant avec les mêmes `user_alias_name` et `user_alias_label`. Si un utilisateur n'est pas trouvé, Braze créera un nouvel utilisateur identifié avec ce jeu de `user_alias_name`.

{% alert important %}
Vous ne pouvez pas utiliser une importation CSV pour mettre à jour un utilisateur existant avec une adresse `user_alias_name` s'il a déjà une adresse `external_id`. Au lieu de cela, cela créera un nouveau profil utilisateur avec l'adresse `user_alias_name`. Pour associer un alias d'utilisateur à une adresse `external_id`, utilisez le [point de terminaison Identifier les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

Télécharger : [Modèle d'importation d'attributs CSV : Alias d'utilisateur]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
Pour mettre à jour les profils utilisateurs existants dans Braze en utilisant une valeur ID interne de Braze au lieu d'une valeur `external_id` ou `user_alias_name` et `user_alias_label`, spécifiez `braze_id` comme en-tête de colonne.

Cela peut s'avérer utile si vous avez exporté des données d'utilisateurs de Braze via notre option d'exportation CSV dans le cadre de la segmentation et que vous souhaitez ajouter un nouvel attribut personnalisé à ces utilisateurs existants.

{% alert important %}
Vous ne pouvez pas utiliser une importation d'utilisateurs au format CSV pour créer un nouvel utilisateur à l'aide de `braze_id`. Cette méthode ne peut être utilisée que pour mettre à jour des utilisateurs préexistants au sein de la plateforme Braze.  
{% endalert %}

{% alert tip %}
La valeur `braze_id` peut être étiquetée comme `Appboy ID` dans les exportations CSV du tableau de bord de Braze. Cet ID sera le même que le `braze_id` pour un utilisateur, vous pouvez donc renommer cette colonne en `braze_id` lorsque vous réimporterez le CSV.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab email address and phone numbers %}
Vous pouvez omettre un ID externe ou un alias utilisateur et utiliser une adresse e-mail ou un numéro de téléphone pour importer des utilisateurs. Avant d'importer un fichier CSV contenant des adresses e-mail ou des numéros de téléphone, vérifiez les points suivants :

- Vérifiez que vous n'avez pas d'ID externe ou d'aliasing de l'utilisateur pour ces profils dans votre fichier CSV. Si vous le faites, Braze utilisera en priorité l'ID externe ou l'alias d'utilisateur avant l'adresse e-mail pour identifier les profils.  
- Confirmez que votre fichier CSV est correctement formaté.  

{% alert note %}
Si vous incluez à la fois des adresses e-mail et des numéros de téléphone dans votre fichier CSV, l'adresse e-mail est prioritaire sur le numéro de téléphone lors de la recherche de profils.
{% endalert %}

Si un profil existant comporte cette adresse e-mail ou ce numéro de téléphone, ce profil sera mis à jour et Braze ne créera pas de nouveau profil. S'il existe plusieurs profils avec la même adresse e-mail, Braze utilisera la même logique que l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) où le profil le plus récemment mis à jour sera mis à jour.

Si un profil avec cette adresse e-mail ou ce numéro de téléphone n'existe pas, Braze créera un nouveau profil avec cet identifiant. Vous pouvez utiliser l'[endpoint`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) pour identifier ce profil ultérieurement. Pour supprimer un profil utilisateur, vous pouvez également utiliser le point de terminaison [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) endpoint.
{% endtab %}
{% endtabs %}

### Étape 3 : Créez votre fichier CSV

Vous pouvez télécharger l'un ou l'autre des types de données suivants sous la forme d'un fichier CSV unique. Pour télécharger plusieurs types de données, téléchargez plusieurs fichiers CSV.

- **Attributs de l'utilisateur :** Il s'agit des attributs par défaut et des attributs personnalisés de l'utilisateur. Les attributs utilisateur par défaut sont des clés réservées dans Braze (telles que `first_name` ou `email`) et les attributs personnalisés sont des attributs utilisateur uniques à votre entreprise (tels que `last_destination_searched`).  
- **Événements personnalisés :** Celles-ci sont uniques à votre entreprise et reflètent les actions qu'un utilisateur a effectuées, par exemple `trip_booked` pour une application de réservation de voyages.

Lorsque vous êtes prêt à créer votre fichier CSV, reportez-vous aux informations suivantes :

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### Identifiants requis {#required-identifiers-attributes}

Bien que `external_id` ne soit pas obligatoire, vous **devez** inclure l'**un** des identifiants suivants dans l'en-tête de votre fichier CSV. Pour en savoir plus sur chacun d'entre eux, consultez la rubrique [Choisir un identifiant](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **et** `user_alias_label`
- `email`
- `phone`

#### Attributs personnalisés

Les types de données suivants peuvent être utilisés comme attributs personnalisés pour l'importation de données CSV. Les en-têtes de colonne qui ne correspondent pas exactement à un [attribut par défaut](#default-attributes) se verront attribuer un attribut personnalisé dans Braze.

| Type de données | Description |
|---|---|
| Date | Doit être stocké au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601). |
| Booléen | Accepte `true` ou `false`. |
| Nombre | Il doit s'agir d'un nombre entier ou d'un float sans espace ni virgule. Les flottants doivent utiliser un point (`.`) comme séparateur décimal. |
| Chaîne de caractères | Peut contenir des virgules si la valeur est entre guillemets doubles (`""`). |
| Blanc | Les valeurs vides n'écraseront pas les valeurs existantes du profil utilisateur et vous n'avez pas besoin d'inclure tous les attributs existants de l'utilisateur dans votre fichier CSV. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Les tableaux, les jetons de poussée et les types de données d'événements personnalisés ne sont pas pris en charge dans l'importation utilisateur, car les virgules dans votre fichier CSV seront interprétées comme un séparateur de colonnes et provoqueront des erreurs lors de l'analyse de votre fichier.<br><br>Pour télécharger ce type de valeurs, utilisez plutôt l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ou [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/).
{% endalert %} 

#### Attributs par défaut

{% alert important %}
Lors de l'importation d'attributs par défaut, les en-têtes de colonne que vous utilisez doivent correspondre exactement à l'orthographe et aux majuscules des attributs utilisateurs par défaut. Dans le cas contraire, Braze les détectera comme des [attributs personnalisés](#custom-attributes).
{% endalert %}

| Champ du profil utilisateur | Type de données | Description | Nécessaire ? |
| :---- | :---- | :---- | :---- |
| `external_id` | Chaîne de caractères | Un identifiant utilisateur unique pour votre personnalisé. | Sous réserve. Voir [Identifiants requis](#required-identifiers-attributes). |
| `user_alias_name` | Chaîne de caractères | Un identifiant unique pour les utilisateurs anonymes qui est une alternative à `external_id`. Doit être utilisé avec `user_alias_label`. | Sous réserve. Voir [Identifiants requis](#required-identifiers-attributes). |
| `user_alias_label` | Chaîne de caractères | Étiquette commune permettant de regrouper les aliasing de l'utilisateur. Doit être utilisé avec `user_alias_name`. | Sous réserve. Voir [Identifiants requis](#required-identifiers-attributes). |
| `first_name` | Chaîne de caractères | Le prénom de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `Jane`). | Non |
| `last_name` | Chaîne de caractères | Le nom de famille de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `Doe`). | Non |
| `email` | Chaîne de caractères | L'e-mail de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `jane.doe@braze.com`). | Non |
| `country` | Chaîne de caractères | Les codes pays doivent être transmis à Braze selon la norme ISO-3166-1 alpha-2 (par exemple, `GB`). | Non |
| `dob` | Chaîne de caractères | Doit être transmis au format "YYYY-MM-DD" (par exemple, `1980-12-21`). Cela importera la date de naissance de votre utilisateur et vous permettra de cibler les utilisateurs dont l'anniversaire est "aujourd'hui". | Non |
| `gender` | Chaîne de caractères | M", "F", "O" (autre), "N" (sans objet), "P" (préfère ne pas se prononcer) ou "nil" (inconnu). | Non |
| `home_city` | Chaîne de caractères | La ville de résidence de vos utilisateurs telle qu'ils l'ont indiquée (par exemple, `London`). | Non |
| `language` | Chaîne de caractères | La langue doit être transmise à Braze selon la norme ISO-639-1 (par exemple, `en`). Consultez la [liste des langues acceptées]({{site.baseurl}}/user_guide/data/user_data_collection/language_codes/). | Non |
| `phone` | Chaîne de caractères | Un numéro de téléphone tel qu'indiqué par vos utilisateurs, au format `E.164` (par exemple, `+442071838750`). Reportez-vous à la section [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) pour obtenir des conseils sur le formatage. | Non |
| `email_open_tracking_disabled` | Booléen | vrai ou faux accepté. Définissez sur true pour désactiver l'ajout du pixel de suivi des ouvertures à tous les futurs e-mails envoyés à cet utilisateur. Disponible uniquement pour SparkPost et SendGrid. | Non |
| `email_click_tracking_disabled` | Booléen | vrai ou faux accepté. La valeur "true" permet de désactiver le suivi des clics pour tous les liens contenus dans un futur e-mail envoyé à cet utilisateur. Disponible uniquement pour SparkPost et SendGrid. | Non |
| `email_subscribe` | Chaîne de caractères | Les valeurs disponibles sont `opted_in` (explicitement inscrit pour recevoir des messages e-mail), `unsubscribed` (explicitement désinscrit des messages e-mail) et `subscribed` (ni inscrit ni désinscrit). | Non |
| `push_subscribe` | Chaîne de caractères | Les valeurs disponibles sont `opted_in` (explicitement inscrit pour recevoir des messages push), `unsubscribed` (explicitement abonné pour ne pas recevoir de messages push) et `subscribed` (ni abonné ni abonné). | Non |
| `time_zone` | Chaîne de caractères | Le fuseau horaire doit être transmis à Braze dans le même format que la base de données des fuseaux horaires de l'IANA (par exemple, `America/New_York` ou `Eastern Time (US & Canada)`). | Non |
| `date_of_first_session`  `date_of_last_session` | Chaîne de caractères | Peut être transmis dans l'un des formats ISO 8601 suivants : "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS" (par exemple, 2019-11-20T18:38:57) | Non |
| `subscription_group_id` | Chaîne de caractères | Le `id` de votre groupe d'abonnement. Cet identifiant se trouve sur la page du groupe d'abonnement de votre tableau de bord. | Non |
| `subscription_state` | Chaîne de caractères | L'état de l'abonnement pour le groupe d'abonnement spécifié par `subscription_group_id`. Les valeurs autorisées sont `unsubscribed` (pas dans le subscription groups) ou `subscribed` (dans le subscription groups). | Non, mais fortement recommandé si `subscription_group_id` est utilisé. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### Mise à jour du statut du groupe d'abonnement (facultatif)

En outre, vous pouvez ajouter des utilisateurs à des groupes d'abonnement par e-mail ou par SMS grâce à l'importation d'utilisateurs. Ceci est particulièrement utile pour les SMS, car un utilisateur doit être inscrit dans un groupe d'abonnement SMS pour recevoir des messages avec le canal de communication SMS. Pour plus d'informations, reportez-vous à la section [Groupes d'abonnement SMS.](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement)

Si vous mettez à jour les statuts du groupe d'abonnement, les deux colonnes suivantes doivent figurer dans votre fichier CSV :

- `subscription_group_id`: Le site `id` du [groupe d'abonnement](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).  
- `subscription_state`: Les valeurs disponibles sont `unsubscribed` (pas dans le subscription groups) ou `subscribed` (dans le subscription groups).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | s'abonner |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | s'abonner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert note %}
Une seule adresse `subscription_group_id` peut être définie par ligne dans l'importation d'utilisateurs. Des lignes différentes peuvent avoir des valeurs `subscription_group_id` différentes. Toutefois, si vous devez inscrire les mêmes utilisateurs dans plusieurs groupes d'abonnement, vous devrez procéder à plusieurs importations.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### Identifiants requis {#required-identifiers-custom-events}

Bien que `external_id` ne soit pas obligatoire, vous **devez** inclure l'**un** des identifiants suivants dans l'en-tête de votre fichier CSV. Pour en savoir plus sur chacun d'entre eux, consultez la rubrique [Choisir un identifiant](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **et** `user_alias_label`
- `email`
- `phone`

#### Champs d'événements personnalisés

Outre les éléments suivants, votre fichier CSV peut également contenir des en-têtes de colonne supplémentaires pour les propriétés d'événement. Ces propriétés doivent avoir un en-tête de colonne de `<event_name>.properties.<property name>.`

Par exemple, l'événement personnalisé `trip_booked` peut avoir les propriétés `destination` et `duration`. Ceux-ci peuvent être importés en ayant les en-têtes de colonne `trip_booked.properties.destination` et `trip_booked.properties.duration`.

| Champ du profil utilisateur | Type de données | Informations | Nécessaire ? |
| :---- | :---- | :---- | :---- |
| `external_id` | Chaîne de caractères | Un identifiant unique pour votre utilisateur. | Sous réserve. Voir [Identifiants requis](#required-identifiers-custom-events). |
| `braze_id` | Chaîne de caractères | Identifiant attribué par Braze à votre utilisateur. | Sous réserve. Voir [Identifiants requis](#required-identifiers-custom-events). |
| `user_alias_name` | Chaîne de caractères | Un identifiant unique pour les utilisateurs anonymes, qui est une alternative à `external_id`. Doit être utilisé avec `user_alias_label`. | Sous réserve. Voir [Identifiants requis](#required-identifiers-custom-events). |
| `user_alias_label` | Chaîne de caractères | Étiquette commune permettant de regrouper les aliasing de l'utilisateur. Doit être utilisé avec `user_alias_name`. | Sous réserve. Voir [Identifiants requis](#required-identifiers-custom-events). |
| `email` | Chaîne de caractères | L'e-mail de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `jane.doe@braze.com`). | Non, et ne peut être utilisé qu'en l'absence d'autres identifiants. Voir la note suivante. |
| `phone` | Chaîne de caractères | Un numéro de téléphone tel qu'indiqué par vos utilisateurs, au format `E.164` (par exemple, `+442071838750`). Reportez-vous à la section [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) pour obtenir des conseils sur le formatage. | Non, et ne peut être utilisé qu'en l'absence d'autres identifiants. Voir la note suivante. |
| `name` | Chaîne de caractères | Un événement personnalisé de vos utilisateurs. | Oui |
| `time` | Chaîne de caractères | L'heure de l'événement. Peut être transmis dans l'un des formats ISO-8601 suivants : "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS" (par exemple, 2019-11-20T18:38:57) | Oui |
| `<event name>.properties.<property name>` | Multiple | Une propriété d'événement associée à un événement personnalisé. En voici un exemple `trip_booked.properties.destination` | Non |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endtab %}
{% endtabs %}

### Étape 4 : Téléchargez et prévisualisez vos données

Avant de traiter votre fichier CSV, Braze génère un aperçu des premières lignes afin que vous puissiez vérifier qu'il n'y a pas de problème. Pour générer votre aperçu, choisissez **Attributs** ou **Événements**, puis sélectionnez **Parcourir les fichiers** et téléchargez votre fichier CSV. 

<!-- old image -->
Le téléchargement d'un fichier CSV s'est terminé par des erreurs impliquant des types de données mixtes dans une seule colonne.]({% image_buster /assets/img/csv_import/upload_csv.png %}){: style="max-width:70%"}

{% alert important %}
L'aperçu de l'importation d'utilisateurs n'analyse pas chaque ligne du fichier d'entrée. Les erreurs survenant après les premières lignes risquent de ne pas être détectées ; il convient donc d'examiner le fichier CSV dans son intégralité.
{% endalert %}

### Étape 5 : Choisissez les préférences de ciblage

Vous pouvez également choisir parmi les préférences de ciblage suivantes. Si vous n'avez pas besoin de créer un nouveau filtre de ciblage ou un segment à partir de votre importation, sélectionnez **Ne pas rendre cette liste disponible en tant que filtre de ciblage**.

| Option | Description |
|---|---|
| Filtre de ciblage | Pour convertir votre fichier CSV en une option de reciblage lorsque vous créez des segments d'utilisateurs, choisissez votre fichier dans le menu déroulant **Mise à jour/Importation du CSV**, puis sélectionnez **Créer un filtre de ciblage**. |
| Nouveaux segments | Pour créer également un nouveau segment à partir de votre nouveau filtre de ciblage, sélectionnez **Créer un filtre de ciblage et ajouter à un nouveau segment**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Un groupe de filtres avec le filtre "Updated/Imported from CSV" comprenant un fichier CSV intitulé "Halloween season fun".]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### Étape 6 : Commencez votre importation CSV

Lorsque vous êtes prêt, sélectionnez **Lancer l'importation**. Vous pouvez suivre l'évolution de la situation sur la page **Importations d'utilisateurs**, qui s'actualise automatiquement toutes les cinq secondes.

S'il n'y a pas de problème, l'état sera **mis** à jour et le nombre de lignes traitées s'affichera. Toutes les données des lignes traitées seront ajoutées aux profils existants ou aux profils nouvellement créés.

{% alert note %}
Vous pouvez importer plusieurs CSV en même temps. Les importations CSV sont exécutées simultanément, de sorte que l'ordre des mises à jour n'est pas garanti. Si vous souhaitez que les importations CSV soient exécutées l'une après l'autre, attendez qu'une importation CSV soit terminée avant d'en télécharger une seconde.
{% endalert %}

## Considérations sur les points de données

Chaque donnée client importée à partir d'un fichier CSV remplacera la valeur existante dans les profils utilisateurs et enregistrera un point de données, à l'exception des ID externes et des valeurs vierges. Si vous avez des questions sur les nuances des points de données de Braze, votre gestionnaire de compte Braze peut y répondre.

| Considération | Détails |
|---|---|
| ID externes | Le téléchargement d'un fichier CSV contenant uniquement `external_id` n'enregistrera pas les points de données. Cela vous permet de segmenter les utilisateurs existants de Braze sans impacter les limites de données. Toutefois, **l** 'inclusion de champs tels que `email` ou `phone` écrasera les données existantes de l'utilisateur et enregistrera des points de données. <br><br>Les importations CSV utilisées uniquement pour la segmentation n'enregistrent pas les points de données, tels que ceux qui ne contiennent que `external_id`, `braze_id` ou `user_alias_name`. |
| Valeurs en blanc | Les valeurs vides dans votre CSV n'écraseront pas les données de profil utilisateur existantes. Il n'est pas nécessaire d'inclure tous les événements personnalisés et tous les attributs utilisateurs lors de l'importation. |
| États d'abonnement | La mise à jour de `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` n'est **pas** prise en compte dans l'utilisation des points de données. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
La définition de `language` ou `country` sur un utilisateur via l'importation d'un CSV ou l'API empêchera Braze de capturer automatiquement ces informations via le SDK.
{% endalert %}

## Résolution des problèmes

Si vous rencontrez des difficultés avec l'importation de fichiers CSV, passez en revue les problèmes les plus courants. Vous avez encore besoin d'aide ? Contactez [support@braze.com](mailto:support@braze.com).

### Problèmes de formatage des fichiers

#### Ligne malformée

Si votre téléchargement s'est terminé avec des erreurs, il se peut que votre fichier CSV contienne une ligne mal formée. 

Pour importer correctement des données, il doit y avoir une ligne d'en-tête. Chaque ligne doit avoir le même nombre de cellules que la ligne d'en-tête. Les lignes dont la longueur est supérieure ou inférieure à celle de la ligne d'en-tête seront exclues de l'importation. Les virgules dans une valeur seront interprétées comme un séparateur et peuvent conduire à cette erreur. En outre, toutes les données doivent être codées en UTF-8.

Si votre fichier CSV contient des lignes vierges et que vous importez moins de lignes que le nombre total de lignes dans le fichier CSV, cela n'indique peut-être pas un problème d'importation puisque les lignes vierges n'ont pas besoin d'être importées. Vérifiez le nombre de lignes qui ont été correctement importées et assurez-vous qu'il correspond au nombre d'utilisateurs que vous tentez d'importer.

#### Ligne manquante

Il y a plusieurs raisons pour lesquelles le nombre d'utilisateurs importés peut ne pas correspondre au nombre total de lignes de votre fichier CSV :

| Enjeu | Résolution |
|---|---|
| Duplication d'ID externes, d'alias d'utilisateurs, d'ID Braze, d'adresses e-mail ou de numéros de téléphone. | Si des colonnes d'ID externe sont dupliquées, cela peut entraîner des lignes mal formées ou non importées, même si les lignes sont correctement formatées. Dans certains cas, il se peut qu'aucune erreur spécifique ne soit signalée. Vérifiez s'il y a des doublons et supprimez-les avant de procéder à un nouveau téléchargement. |
| Caractères accentués | Votre CSV peut contenir des noms ou des attributs avec des accents. Assurez-vous que le fichier est encodé en UTF-8 pour éviter les problèmes d'importation. |
| L'ID de Braze appartient à un utilisateur orphelin | Si un utilisateur a été fusionné avec un autre et que Braze ne peut pas associer l'ID de Braze au profil restant, la ligne ne sera pas importée. |
| Ligne vide | Les lignes vides dans le fichier CSV peuvent entraîner des erreurs de données mal formées. Vérifiez en utilisant un éditeur de texte simple, et non Excel ou Sheets. |
| Y compris les guillemets doubles (`"` ) | Ce caractère n'est pas valide et provoquera une ligne malformée. Utilisez plutôt des guillemets simples (`'`). |
| Sauts de ligne incohérents | Les sauts de ligne mixtes (e.g., `\n` et `\r\n`) peuvent entraîner le traitement de la première ligne de données comme faisant partie de l'en-tête. Utilisez un éditeur de texte hexagonal ou avancé pour inspecter et réparer. |
| Fichier mal encodé | Même si les accents sont autorisés, le fichier doit être encodé en UTF-8. D'autres encodages peuvent fonctionner partiellement mais ne sont pas entièrement pris en charge. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Chaîne de caractères

Les valeurs encapsulées dans des guillemets simples (`''`) ou doubles (`""`) seront lues comme des chaînes de caractères lors de l'importation.

#### Dates mal formatées

Les dates qui ne sont pas au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ne seront pas lues comme `datetimes` lors de l'importation.

### Questions relatives à la structure des données

#### Adresses e-mail non valides

Si votre téléchargement s'est terminé par des erreurs, il se peut qu'il y ait une ou plusieurs adresses e-mail cryptées non valides. Confirmez que toutes les adresses e-mail sont correctement cryptées avant de les importer dans Braze.

- **Lors de la [mise à jour ou de l'importation d'adresses e-mail]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)** dans Braze, utilisez la valeur hachée de l'e-mail chaque fois qu'un e-mail est inclus. Ces valeurs d'e-mail de hachage sont fournies par votre équipe interne. 
- **Lors de la création d'un nouvel utilisateur**, vous devez ajouter `email_encrypted` avec la valeur de l'e-mail crypté de l'utilisateur. Sinon, l'utilisateur ne sera pas créé. De même, si vous ajoutez une adresse e-mail à un utilisateur existant qui n'a pas d'e-mail, vous devez ajouter `email_encrypted`. Sinon, l'utilisateur ne sera pas mis à jour.

#### Données importées en tant qu'attribut personnalisé

Si une donnée utilisateur par défaut (telle que `email` ou `first_name`) est importée en tant qu'attribut personnalisé, vérifiez la casse et l'espacement de votre fichier CSV. Par exemple, `First_name` serait importé en tant qu'attribut personnalisé, tandis que `first_name` serait correctement importé dans le champ "prénom" du profil d'un utilisateur.

#### Plusieurs types de données

Braze s'attend à ce que chaque valeur d'une colonne soit du même type de données. Les valeurs qui ne correspondent pas au type de données de leur attribut entraîneront des erreurs de segmentation.

En outre, le fait de commencer un attribut de nombre par zéro posera des problèmes, car les nombres commençant par des zéros sont considérés comme des chaînes de caractères. Lorsque Braze convertit cette chaîne de caractères, elle peut être traitée comme une valeur octale (qui utilise les chiffres de zéro à sept), ce qui signifie qu'elle sera convertie en sa valeur décimale correspondante. Par exemple, si la valeur du fichier CSV est 0130, le profil Braze affichera 88. Pour éviter ce problème, utilisez des attributs avec des chaînes de caractères. Toutefois, ce type de données n'est pas disponible dans la comparaison des numéros de segmentation.

#### Types d'attribut par défaut

Certains attributs par défaut peuvent n'accepter que certaines valeurs comme valables pour les mises à jour de l'utilisateur. Pour plus d'informations, reportez-vous à la section [Construire votre CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Les espaces de fin et les différences de capitalisation peuvent entraîner l'interprétation d'une valeur comme non valide. Par exemple, dans le fichier CSV suivant, seul l'utilisateur de la première ligne (`brazetest1`) verra ses statuts d'e-mail et de push mis à jour avec succès car les valeurs acceptées sont `unsubscribed`, `subscribed`, et `opted_in`. 

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### La fonction "Sélectionner un fichier CSV" ne fonctionne pas.

Il y a plusieurs raisons pour lesquelles le bouton **Sélectionner un fichier CSV** peut ne pas fonctionner :

| Enjeu | Résolution |
|---|---|
| Bloqueur de fenêtres pop-up | Cela peut empêcher l'affichage de la page. Confirmez que votre navigateur autorise les fenêtres pop-up sur le site web du tableau de bord de Braze. |
| Navigateur obsolète | Assurez-vous que votre navigateur est à jour ; si ce n'est pas le cas, mettez-le à jour. |
| Processus d'arrière-plan | Fermez toutes les instances de votre navigateur, puis redémarrez votre ordinateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
