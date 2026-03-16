---
nav_title: Importation CSV
article_title: "Importation CSV"
description: "Veuillez découvrir comment enregistrer et mettre à jour les attributs utilisateur et les événements personnalisés à l'aide de l'importation CSV."
page_order: 1.2
---

# Importation CSV

> Veuillez découvrir comment enregistrer et mettre à jour les attributs utilisateur et les événements personnalisés à l'aide de l'importation CSV.

## À propos de l'importation CSV

Vous pouvez utiliser l'importation CSV pour enregistrer et mettre à jour les événements personnalisés et les attributs utilisateurs suivants.

|Type|Définition|Exemple|Taille maximale du fichier|
|---|---|---|---|
|Attributs par défaut|Attributs réservés de l'utilisateur reconnus par Braze.|`first_name`, `email`|500 MO|
|Attributs personnalisés|Attributs de l'utilisateur uniques à votre entreprise.|`last_destination_searched`|500 MO|
|Événements personnalisés|Événements uniques à votre entreprise qui représentent des actions de l'utilisateur.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Utilisation de l'importation CSV

### Étape 1 : Veuillez télécharger un modèle CSV.

Pour ouvrir l'importation CSV, veuillez vous rendre dans **Audiences** > **Importer des utilisateurs**. Vous trouverez ici un tableau répertoriant les détails des importations les plus récentes, tels que la date de téléchargement, le nom de la personne qui a effectué le téléchargement, le nom du fichier, la disponibilité du ciblage, le nombre de lignes importées et le statut de l'importation.

Pour vous aider à démarrer avec votre fichier CSV, veuillez télécharger un modèle pour les attributs ou les événements.

![La page "Importation d'utilisateurs" du tableau de bord de Braze.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### Étape 2 : Veuillez sélectionner un identifiant {#choose-an-identifier}

Le fichier CSV que vous importez nécessitera un identifiant spécifique. Vous avez le choix entre les options suivantes :

{% tabs local %}
<!-- TAB -->
{% tab external id %}
Lors de l'importation de vos données clients, vous pouvez utiliser un identifiant`external_id` unique pour chaque client. Lorsque vous fournissez un identifiant`external_id`dans votre importation d'utilisateurs, Braze met à jour tout utilisateur existant avec le même`external_id`identifiant ou crée un nouvel utilisateur identifié avec cet`external_id`identifiant défini si aucun n'est trouvé.

- Télécharger : [Modèle d'importation des attributs CSV : ID externe]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Télécharger : [Modèle d'importation d'événements CSV : ID externe](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
Si vous téléchargez un mélange d'utilisateurs avec un identifiant`external_id`et d'utilisateurs sans identifiant, vous devez créer un fichier CSV pour chaque importation d'utilisateurs. Un fichier CSV ne peut pas contenir à la fois des alias `external_ids`d'utilisateurs et des alias d'utilisateurs.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
Pour cibler les utilisateurs qui ne disposent pas d'un compte`external_id`, il est possible d'importer une liste d'utilisateurs avec leurs pseudonymes. Un pseudonyme sert d'identifiant utilisateur unique alternatif et peut être utile si vous souhaitez cibler des utilisateurs anonymes qui ne se sont pas inscrits ou n'ont pas créé de compte sur votre application.

Si vous téléchargez ou mettez à jour des profils d’utilisateur qui sont alias uniquement, vous devez avoir les deux colonnes suivantes dans votre CSV :

- `user_alias_name` : Un identifiant unique de l'utilisateur ; une alternative à l'identifiant de l'utilisateur. `external_id`  
- `user_alias_label` : Une étiquette commune permettant de regrouper les alias utilisateurs.

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

Lorsque vous fournissez à la fois un`user_alias_name`  et un`user_alias_label`  dans votre importation d'utilisateurs, Braze met à jour tout utilisateur existant avec le même`user_alias_name`  et le même`user_alias_label` . Si aucun utilisateur n'est trouvé, Braze crée un nouvel utilisateur identifié avec cet`user_alias_name`ensemble.

{% alert important %}
Il n'est pas possible d'utiliser l'importation CSV pour mettre à jour un utilisateur existant avec un`user_alias_name`  s'il dispose déjà d'un `external_id`. Au lieu de cela, cela crée un nouveau profil utilisateur avec le fichier `user_alias_name`. Pour associer un utilisateur avec alias uniquement à un `external_id`, utilisez [l’endpoint Identifier les Utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

Télécharger : [Modèle d'importation des attributs CSV : Alias d'utilisateur]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
Pour mettre à jour les profils utilisateurs existants dans Braze en utilisant une valeur ID interne de Braze au lieu d'une valeur `external_id` ou `user_alias_name` et `user_alias_label`, spécifiez `braze_id` comme en-tête de colonne.

Cela peut s'avérer utile si vous avez exporté des données d'utilisateurs de Braze via notre option d'exportation CSV dans le cadre de la segmentation et que vous souhaitez ajouter un nouvel attribut personnalisé à ces utilisateurs existants.

{% alert important %}
Il n'est pas possible d'utiliser l'importation CSV pour créer un nouvel utilisateur`braze_id`. Cette méthode ne peut être utilisée que pour mettre à jour les utilisateurs existants sur la plate-forme Braze.  
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

Si un profil existant contient cette adresse e-mail ou ce numéro de téléphone, ce profil est mis à jour et Braze ne crée pas de nouveau profil. S'il existe plusieurs profils avec la même adresse e-mail, Braze utilisera la même logique que l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) où le profil le plus récemment mis à jour sera mis à jour.

Si aucun profil n'existe avec cette adresse e-mail ou ce numéro de téléphone, Braze crée un nouveau profil avec cet identifiant. Vous pouvez utiliser l'[endpoint`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) pour identifier ce profil ultérieurement. Pour supprimer un profil utilisateur, vous pouvez également utiliser l’enpoint [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).
{% endtab %}
{% endtabs %}

### Étape 3 : Veuillez créer votre fichier CSV.

Vous pouvez télécharger l'un des types de données suivants sous forme de fichier CSV unique. Pour télécharger plusieurs types de données, veuillez télécharger plusieurs fichiers CSV.

- **Attributs utilisateur :** Cela inclut à la fois les attributs utilisateur par défaut et personnalisés. Les attributs utilisateur par défaut sont des clés réservées dans Braze (telles que`first_name`ou `email`) et les attributs personnalisés sont des attributs utilisateur uniques à votre entreprise (tels que `last_destination_searched`).  
- **Événements personnalisés :** Ces paramètres sont uniques à votre entreprise et reflètent les actions effectuées par un utilisateur, par exemple`trip_booked`pour une application de réservation de voyages.

Lorsque vous êtes prêt à commencer à créer votre fichier CSV, veuillez vous référer aux informations suivantes :

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### Identifiants requis {#required-identifiers-attributes}

Bien que`external_id`cela ne soit pas obligatoire, il **est nécessaire** d'inclure **l'un** des identifiants suivants en tant qu'en-tête dans votre fichier CSV. Pour plus de détails sur chacun d'entre eux, veuillez consulter [la section Choisir un identifiant](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **et** `user_alias_label`
- `email`
- `phone`

#### Attributs personnalisés

Les types de données suivants peuvent être utilisés comme attributs personnalisés pour l'importation CSV. Les en-têtes de colonne qui ne correspondent pas exactement à un [attribut par défaut](#default-attributes) sont importées en tant qu'attributs personnalisés dans Braze.

| Type de données | Description |
|---|---|
| Date et heure | Doit être enregistré au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601). |
| Valeur booléenne | Accepte `true` ou `false`. |
| Nombre | Doit être un nombre entier ou float, sans espaces ni virgules. Les nombres flottants doivent utiliser un point (`.`.) comme séparateur décimal. |
| Chaîne de caractères | Peut contenir des virgules si la valeur est entre guillemets doubles (`""`). |
| Blanc | Les valeurs vides ne remplaceront pas les valeurs existantes dans le profil utilisateur, et il n'est pas nécessaire d'inclure tous les attributs utilisateur existants dans votre fichier CSV. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Les tableaux, les jetons push et les types de données d'événements personnalisés ne sont pas pris en charge dans l'importation d'utilisateurs, car les virgules dans votre fichier CSV seront interprétées comme des séparateurs de colonnes et entraîneront des erreurs lors de l'analyse de votre fichier.<br><br>Pour télécharger ce type de valeurs, veuillez utiliser [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)l'[endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ou [l'ingestion de données]({{site.baseurl}}/user_guide/data/cloud_ingestion/).
{% endalert %} 

#### Attributs par défaut

{% alert important %}
Lors de l'importation d'attributs par défaut, les en-têtes de colonne que vous utilisez doivent correspondre exactement à l'orthographe et à la casse des attributs utilisateur par défaut. Dans le cas contraire, Braze les identifie comme [des attributs personnalisés](#custom-attributes).
{% endalert %}

Les attributs par défaut suivants sont disponibles pour l'importation d'utilisateurs.

| Champ profil utilisateur | Type de données | Description | Requise ? |
| :---- | :---- | :---- | :---- |
| `external_id` | Chaîne de caractères | Un identifiant utilisateur unique pour votre client. | Sous certaines conditions. Veuillez consulter [la section Identifiants requis](#required-identifiers-attributes). |
| `user_alias_name` | Chaîne de caractères | Identifiant utilisateur unique pour les utilisateurs anonymes, constituant une alternative à `external_id`. Doit être utilisé avec `user_alias_label`. | Sous certaines conditions. Veuillez consulter [la section Identifiants requis](#required-identifiers-attributes). |
| `user_alias_label` | Chaîne de caractères | Un libellé commun pour regrouper les alias d’utilisateurs. Doit être utilisé avec `user_alias_name`. | Sous certaines conditions. Veuillez consulter [la section Identifiants requis](#required-identifiers-attributes). |
| `first_name` | Chaîne de caractères | Le prénom de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `Jane`). | Non |
| `last_name` | Chaîne de caractères | Le nom de famille de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `Doe`). | Non |
| `email` | Chaîne de caractères | L'e-mail de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `jane.doe@braze.com`). | Non |
| `country` | Chaîne de caractères | Les codes pays doivent être transmis à Braze selon la norme ISO-3166-1 alpha-2 (par exemple, `GB`). | Non |
| `dob` | Chaîne de caractères | Doit être transmis au format « AAAA-MM-JJ » (par exemple, `1980-12-21`). Cette fonctionnalité permet d'importer la date de naissance de vos utilisateurs et vous permet de réaliser un ciblage sur les utilisateurs dont l'anniversaire est « aujourd'hui ». | Non |
| `gender` | Chaîne de caractères | « H », « F », « A » (autre), « S/O » (sans objet), « P » (préfère ne pas dire) ou nul (inconnu). | Non |
| `home_city` | Chaîne de caractères | La ville de résidence de vos utilisateurs telle qu'ils l'ont indiquée (par exemple, `London`). | Non |
| `language` | Chaîne de caractères | La langue doit être transmise à Braze selon la norme ISO-639-1 (par exemple, `en`). Consultez notre [liste des langues acceptées]({{site.baseurl}}/user_guide/data/user_data_collection/language_codes/). | Non |
| `phone` | Chaîne de caractères | Un numéro de téléphone tel qu'indiqué par vos utilisateurs, au format `E.164` (par exemple, `+442071838750`). Reportez-vous à la section [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) pour obtenir des conseils sur le formatage. | Non |
| `email_open_tracking_disabled` | Valeur booléenne | vrai ou faux accepté. Définissez sur True pour désactiver le pixel de suivi d’ouverture dans tous les futurs e-mails envoyés à cet utilisateur. Disponible uniquement pour SparkPost et SendGrid. | Non |
| `email_click_tracking_disabled` | Valeur booléenne | vrai ou faux accepté. Définissez sur True pour désactiver le suivi de clic pour tous les liens dans les futurs e-mails envoyés à cet utilisateur. Disponible uniquement pour SparkPost et SendGrid. | Non |
| `email_subscribe` | Chaîne de caractères | Les valeurs disponibles sont `opted_in` (explicitement consenti à recevoir des e-mails), `unsubscribed` (explicitement refusé de recevoir des e-mails), et `subscribed` (ni accepté, ni refusé). | Non |
| `push_subscribe` | Chaîne de caractères | Les valeurs disponibles sont `opted_in` (explicitement consenti à recevoir des messages de notification push), `unsubscribed` (explicitement  refusé de recevoir des messages de notification push), et `subscribed` (ni accepté, ni refusé). | Non |
| `time_zone` | Chaîne de caractères | Le fuseau horaire doit être transmis à Braze dans le même format que la base de données des fuseaux horaires de l'IANA (par exemple, `America/New_York` ou `Eastern Time (US & Canada)`). | Non |
| `date_of_first_session`  `date_of_last_session` | Chaîne de caractères | Peut être transmis dans l’un des formats ISO 8601 suivants : « AAAA-MM-JJ » « AAAA-MM-JJ HH:MM:SS+00:00 » « AAAA-MM-JJ HH:MM:SSZ » « AAAA-MM-JJ HH:MM:SS » (par exemple, 2019-11-20T18:38:57) | Non |
| `subscription_group_id` | Chaîne de caractères | L’`id` de votre groupe d’abonnement. Cet identifiant se trouve sur la page du groupe d’abonnement de votre tableau de bord. | Non |
| `subscription_state` | Chaîne de caractères | Le statut d’abonnement du groupe d’abonnement spécifié par `subscription_group_id`. Les valeurs autorisées sont `unsubscribed` (pas dans le groupe d’abonnement) ou `subscribed` (dans le groupe d’abonnement). | Non, mais fortement recommandé si `subscription_group_id` est utilisé |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### Mise à jour du statut du groupe d'abonnement (facultatif)

De plus, vous pouvez ajouter des utilisateurs à des groupes d'abonnement par e-mail ou SMS via l'importation d'utilisateurs. Ceci est particulièrement utile pour les SMS, car un utilisateur doit être inscrit dans un groupe d'abonnement SMS pour recevoir des messages avec le canal de communication SMS. Pour plus d'informations, consultez [Groupes d'abonnement SMS](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Si vous mettez à jour les statuts du groupe d'abonnement, les deux colonnes suivantes doivent figurer dans votre fichier CSV :

- `subscription_group_id` : Le site `id` du [groupe d'abonnement](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).  
- `subscription_state` : Les valeurs disponibles sont `unsubscribed` (pas dans le subscription groups) ou `subscribed` (dans le subscription groups).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | abonné |
| k2LNhj8KS | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | abonné |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert note %}
Un seul `subscription_group_id` peut être défini par ligne dans User Import (Importation d’utilisateurs). Différentes lignes peuvent avoir différentes valeurs `subscription_group_id`. Toutefois, si vous devez inscrire les mêmes utilisateurs dans plusieurs groupes d'abonnement, vous devrez effectuer plusieurs importations.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### Identifiants requis {#required-identifiers-custom-events}

Bien que`external_id`cela ne soit pas obligatoire, il **est nécessaire** d'inclure **l'un** des identifiants suivants en tant qu'en-tête dans votre fichier CSV. Pour plus de détails sur chacun d'entre eux, veuillez consulter [la section Choisir un identifiant](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **et** `user_alias_label`
- `email`
- `phone`

#### Événements personnalisés

En plus des éléments suivants, votre fichier CSV peut également contenir des en-têtes de colonnes supplémentaires pour les propriétés d'événement. Ces propriétés doivent comporter un en-tête de colonne intitulé `<event_name>.properties.<property name>.`

Par exemple, l'événement personnalisé`trip_booked` peut avoir les propriétés`destination`et `duration`. Ces données peuvent être importées en utilisant les en-têtes de colonne`trip_booked.properties.destination` et `trip_booked.properties.duration`.

| Champ profil utilisateur | Type de données | Information | Requise ? |
| :---- | :---- | :---- | :---- |
| `external_id` | Chaîne de caractères | Un identifiant unique pour votre utilisateur. | Sous certaines conditions. Veuillez consulter [la section Identifiants requis](#required-identifiers-custom-events). |
| `braze_id` | Chaîne de caractères | Identifiant attribué par Braze à votre utilisateur. | Sous certaines conditions. Veuillez consulter [la section Identifiants requis](#required-identifiers-custom-events). |
| `user_alias_name` | Chaîne de caractères | Identifiant utilisateur unique pour les utilisateurs anonymes, qui constitue une alternative à `external_id`. Doit être utilisé avec `user_alias_label`. | Sous certaines conditions. Veuillez consulter [la section Identifiants requis](#required-identifiers-custom-events). |
| `user_alias_label` | Chaîne de caractères | Un libellé commun pour regrouper les alias d’utilisateurs. Doit être utilisé avec `user_alias_name`. | Sous certaines conditions. Veuillez consulter [la section Identifiants requis](#required-identifiers-custom-events). |
| `email` | Chaîne de caractères | L'e-mail de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `jane.doe@braze.com`). | Non, et ne peut être utilisé qu'en l'absence d'autres identifiants. Veuillez consulter la note suivante. |
| `phone` | Chaîne de caractères | Un numéro de téléphone tel qu'indiqué par vos utilisateurs, au format `E.164` (par exemple, `+442071838750`). Reportez-vous à la section [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) pour obtenir des conseils sur le formatage. | Non, et ne peut être utilisé qu'en l'absence d'autres identifiants. Veuillez consulter la note suivante. |
| `name` | Chaîne de caractères | Un événement personnalisé de vos utilisateurs. | Oui |
| `time` | Chaîne de caractères | L'heure de l'événement. Peut être transmis dans l'un des formats ISO-8601 suivants : « AAAA-MM-JJ » « AAAA-MM-JJ HH:MM:SS+00:00 » « AAAA-MM-JJ HH:MM:SSZ » « AAAA-MM-JJ HH:MM:SS » (par exemple, 2019-11-20T18:38:57) | Oui |
| `<event name>.properties.<property name>` | Plusieurs | Une propriété d'événement associée à un événement personnalisé. En voici un exemple `trip_booked.properties.destination` | Non |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endtab %}
{% endtabs %}

### Étape 4 : Veuillez télécharger votre fichier

Pour télécharger votre fichier, veuillez sélectionner **Attributs** ou **Événements**, cliquer sur **Parcourir les fichiers**, puis télécharger votre fichier CSV. Braze affiche un aperçu des premières lignes et un résumé des champs détectés.

![La fenêtre modale/boîte de dialogue modale, etc. indiquant que le téléchargement est terminé affiche un aperçu du fichier, le champ de nom d'importation, les préférences de ciblage et la case à cocher de validation du fichier.]({% image_buster /assets/img/csv_import/upload_completed.png %})

Dans le champ **Nom de l'importation**, vous pouvez renommer votre importation. Par défaut, le nom du fichier est utilisé.

{% alert note %}
L'aperçu du fichier n'affiche que les premières lignes de votre fichier. Pour vérifier chaque ligne avant l'importation, veuillez utiliser [la validation de fichier](#file-validation).
{% endalert %}

### Étape 5 : Veuillez vérifier votre fichier (facultatif) {#file-validation}

Avant de procéder à l'importation, il est possible d'effectuer une validation des fichiers afin de vérifier chaque ligne à la recherche d'erreurs et d'avertissements. Pour valider votre fichier, veuillez sélectionner **Valider le fichier avant l'importation**, puis cliquer sur **Démarrer l'importation**.

La validation peut prendre jusqu'à 2 minutes pour les fichiers dont la taille est à la limite autorisée. Pendant l'exécution de la validation, vous pouvez sélectionner **Ignorer la validation** pour la contourner et continuer immédiatement.

#### Résultats de la validation

Une fois la validation terminée, l'un des résultats suivants s'affiche.

| Résultat | Ce que cela signifie | Étape suivante |
|---|---|---|
| **Validation terminée** | Aucun problème n'a été détecté. | Veuillez sélectionner **« Importer les données** ». |
| **Problèmes identifiés** | Certaines lignes contiennent des erreurs ou des avertissements. | Veuillez télécharger le rapport d'erreurs pour l'examiner, puis sélectionnez **« Importer quand même** » pour continuer ou **« Annuler** » pour corriger votre fichier au préalable. |
| **Délai de validation expiré** | La validation a expiré. Les lignes qui ont été vérifiées ne présentaient aucun problème. | Veuillez sélectionner **« Importer les données** ». Un rapport complet sera disponible dans quelques minutes. |
| **La validation a expiré en raison de problèmes** | La validation a rencontré des problèmes de délai et a détecté des erreurs dans certaines des lignes vérifiées. | Veuillez télécharger le rapport partiel pour examiner les résultats, puis sélectionner **Importer quand même** ou **Annuler**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

![La boîte de dialogue « Problèmes détectés » affiche le nombre de lignes contenant des erreurs et des avertissements, avec des options permettant d'annuler, de télécharger le rapport d'erreurs ou de procéder à l'importation malgré tout.]({% image_buster /assets/img/csv_import/validation_issues.png %})

#### Comprendre le rapport d'erreurs

Le rapport d'erreurs est un fichier CSV qui contient toutes les lignes signalées, ainsi que leurs données d'origine et une description du problème.

| Type de problème | Description |
|---|---|
| **Erreur** | La ligne sera entièrement ignorée lors de l'importation. |
| **Avertissement** | La ligne sera importée, mais certaines valeurs seront supprimées. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Après avoir examiné le rapport, vous pouvez corriger les problèmes dans votre fichier d'origine et le télécharger à nouveau, ou procéder à l'importation et accepter les résultats partiels.

### Étape 6 : Sélectionnez vos préférences de ciblage

Vous pouvez également sélectionner parmi les préférences de ciblage suivantes. Si vous n'avez pas besoin de créer un nouveau filtre de ciblage ou segment à partir de votre importation, veuillez sélectionner **Ne pas rendre cette liste disponible en tant que filtre de ciblage**.

| Option | Description |
|---|---|
| Filtre de ciblage | Pour convertir votre fichier CSV en option de reciblage lors de la création de segments d'utilisateurs, veuillez sélectionner votre fichier dans le menu déroulant **Mis à jour/Importé depuis CSV**, puis sélectionner **Créer un filtre de ciblage**. |
| Nouveaux segments | Pour créer un nouveau segment à partir de votre nouveau filtre de ciblage, veuillez sélectionner **Créer un filtre de ciblage et ajouter au nouveau segment**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![Un groupe de filtres avec le filtre « Mis à jour/Importé depuis CSV » comprenant un fichier CSV intitulé « Plaisirs de la saison d'Halloween ».]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### Étape 7 : Veuillez commencer l'importation CSV.

Lorsque vous êtes prêt, veuillez cliquer sur **« Commencer l'importation** ». Vous pouvez suivre la progression actuelle sur la page **Importer des utilisateurs**, qui s'actualise automatiquement toutes les 5 secondes.

{% alert note %}
Vous pouvez importer plusieurs CSV en même temps. Les importations CSV sont exécutées simultanément, de sorte que l'ordre des mises à jour n'est pas garanti. Si vous souhaitez que les importations CSV soient exécutées l'une après l'autre, attendez qu'une importation CSV soit terminée avant d'en télécharger une seconde.
{% endalert %}

#### Statuts d'importation

Une fois l'importation lancée, vous pouvez vérifier son statut sur la page **Importer des utilisateurs**.

| État | Description |
|---|---|
| **Terminé** | Toutes les lignes ont été importées avec succès. |
| **Succès partiel** | Certaines lignes ont échoué. Veuillez sélectionner le menu à trois points à côté de l'importation pour télécharger un rapport d'erreurs ou le fichier CSV original téléchargé. |
| **En cours** | L'importation est actuellement en cours. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![La page de l'importation d'utilisateurs affiche un statut de réussite partielle avec le menu contextuel ouvert, présentant les options Télécharger le rapport d'erreurs et Télécharger le fichier CSV téléchargé.]({% image_buster /assets/img/csv_import/partial_success_menu.png %})

Le rapport d'erreurs post-importation inclut les lignes qui ont échoué pour des raisons non couvertes par la validation, par exemple lorsqu'un utilisateur n'existe pas dans Braze.

## Considérations relatives aux points de données

Chaque donnée client importée à partir d'un fichier CSV remplace la valeur existante dans les profils utilisateurs et enregistre un point de donnée, à l'exception des ID externes et des valeurs vides. Si vous avez des questions concernant les subtilités des points de donnée Braze, votre gestionnaire de compte Braze se fera un plaisir d'y répondre.

| Considération | Détails |
|---|---|
| ID externe | Le téléchargement d'un fichier CSV contenant uniquement`external_id`  n'enregistre pas les points de donnée. Cela vous permet de segmenter les utilisateurs Braze existants sans affecter les limites de données. Cependant, l'inclusion de champs tels que`email`ou`phone`écrase les données utilisateur existantes et enregistre les points de donnée. <br><br>Les importations CSV utilisées uniquement à des fins de segmentation n'enregistrent pas les points de donnée, tels que ceux contenant uniquement `external_id`, `braze_id`, ou `user_alias_name`. |
| Valeurs vides | Les valeurs vides dans votre fichier CSV ne remplaceront pas les données existantes du profil utilisateur. Il n'est pas nécessaire d'inclure tous les attributs utilisateur ou custom events lors de l'importation. |
| Statuts d'abonnement | La mise à jour `email_subscribe`de , `push_subscribe`, `subscription_group_id`, ou`subscription_state`  n'est **pas** prise en compte dans l'utilisation des points de donnée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Définir`language`  ou`country`  sur un utilisateur via l'importation CSV ou l'API empêche Braze de capturer automatiquement ces informations via le SDK.
{% endalert %}

## Résolution des problèmes

Si vous avez utilisé [la validation des fichiers](#file-validation), veuillez commencer par consulter le rapport d'erreurs. Il contient le problème spécifique pour chaque ligne signalée et une description de la manière de le résoudre. Pour les lignes qui ont échoué lors de l'importation plutôt que lors de la validation, veuillez télécharger le rapport d'erreurs à partir du menu à trois points sur la page **Importer des utilisateurs**.

Si vous rencontrez des difficultés avec l'importation CSV, veuillez consulter les problèmes courants ci-dessous. Vous avez toujours besoin d’aide ? Veuillez contacter [support@braze.com](mailto:support@braze.com).

### Problèmes de formatage des fichiers

#### Ligne mal formée

Si votre téléchargement s'est terminé avec des erreurs, il se peut qu'il y ait une ligne mal formée dans votre fichier CSV. 

Pour importer correctement les données, il est nécessaire d'inclure une ligne d'en-tête. Chaque ligne doit avoir le même nombre de cellules que la ligne d’en-tête. Les lignes qui ont plus, ou moins, de valeurs que la ligne d’en-tête seront exclues de l’importation. Les virgules dans une valeur seront interprétées comme un séparateur et peuvent conduire à cette erreur. De plus, toutes les données doivent être encodées en UTF-8.

Si votre fichier CSV contient des lignes vides et que vous importez moins de lignes que le nombre total de lignes dans le fichier CSV, cela ne signifie pas nécessairement qu'il y a un problème avec l'importation, car les lignes vides n'ont pas besoin d'être importées. Vérifiez le nombre de lignes correctement importées et assurez-vous qu’elles correspondent au nombre d’utilisateurs que vous essayez d’importer.

#### Ligne manquante

Plusieurs raisons peuvent expliquer pourquoi le nombre d’utilisateurs importés ne correspond pas forcément au total de lignes dans votre fichier CSV :

| Problème | Résolution |
|---|---|
| ID externes, pseudonymes d'utilisateurs, ID Braze, adresses e-mail ou numéros de téléphone en double | Si des colonnes d'ID externe sont dupliquées, cela peut entraîner des lignes mal formées ou non importées, même si les lignes sont correctement formatées. Dans certains cas, cela peut ne pas signaler d'erreur spécifique. Veuillez vérifier s'il existe des doublons et les supprimer avant de procéder à un nouveau téléchargement. |
| Caractères accentués | Votre fichier CSV peut contenir des noms ou des attributs comportant des accents. Veuillez vous assurer que le fichier est encodé en UTF-8 afin d'éviter tout problème lors de l'importation. |
| Braze ID est associé à un utilisateur orphelin. | Si un utilisateur a été fusionné avec un autre et que Braze ne parvient pas à associer l'ID Braze au profil utilisateur restant, la ligne ne sera pas importée. |
| Ligne vide | Les lignes vides dans le fichier CSV peuvent entraîner des erreurs de données mal formées. Veuillez vérifier à l'aide d'un éditeur de texte brut, et non d'Excel ou de Sheets. |
| Guillemets doubles non échappés ou non équilibrés (`"`) | Les guillemets doubles encadrent les valeurs de chaîne de caractères qui contiennent des virgules. Si une valeur contient elle-même un guillemet double, veuillez l'échapper en le doublant (`""`). Les guillemets doubles non échappés ou déséquilibrés entraînent une ligne mal formée. |
| Coupures de ligne incohérentes | Les sauts de ligne mixtes (e.g.,`\n`et `\r\n`) peuvent entraîner le traitement de la première ligne de données comme faisant partie de l'en-tête. Veuillez utiliser un éditeur hexadécimal ou un éditeur de texte avancé pour examiner et corriger. |
| Fichier mal encodé | Même si les accents sont autorisés, le fichier doit être encodé en UTF-8. D'autres encodages peuvent fonctionner partiellement, mais ne sont pas entièrement pris en charge. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Quote de chaîne de caractères

Les valeurs encapsulées dans des guillemets simples (`''`) ou doubles (`""`) seront lues comme des chaînes de caractères lors de l'importation.

#### Dates incorrectement formatées

Les dates qui ne sont pas au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ne seront pas lues comme `datetimes` lors de l'importation.

### Problèmes liés à la structure des données

#### E-mails non valides

Si votre téléchargement s'est terminé avec des erreurs, il se peut qu'une ou plusieurs adresses e-mail cryptées ne soient pas valides. Veuillez vous assurer que toutes les adresses e-mail sont correctement cryptées avant de les importer dans Braze.

- **Lors de [la mise à jour ou ]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)de [l'importation d'adresses e-mail]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)** dans Braze, veuillez utiliser la valeur hachée de l'adresse e-mail chaque fois qu'une adresse e-mail est incluse. Ces valeurs de hachage des e-mails sont fournies par votre équipe interne. 
- **Lors de la création d'un nouvel utilisateur**, il est nécessaire d'ajouter la valeur `email_encrypted`cryptée de l'adresse e-mail de l'utilisateur. Dans le cas contraire, Braze ne créera pas l'utilisateur. De même, si vous ajoutez une adresse e-mail à un utilisateur existant qui n'en possède pas, vous devez ajouter `email_encrypted`. Dans le cas contraire, Braze ne mettra pas à jour les informations de l'utilisateur.

#### Données importées comme attribut personnalisé

Si une donnée utilisateur par défaut (telle que `email` ou `first_name`) est importée en tant qu'attribut personnalisé, vérifiez la casse et l'espacement de votre fichier CSV. Par exemple,`First_name`  est importé en tant qu'attribut personnalisé, tandis que`first_name`  est correctement importé dans le champ « prénom » du profil utilisateur.

#### Plusieurs types de données

Braze s’attend à ce que toutes les valeurs d’une colonne soient du même type de données. Les valeurs qui ne correspondent pas au type de données de leur attribut entraînent des erreurs de segmentation.

De plus, commencer un attribut numérique par zéro peut entraîner des problèmes, car les nombres commençant par zéro sont considérés comme des chaînes de caractères. Lorsque Braze convertit cette chaîne de caractères, elle peut être traitée comme une valeur octale (qui utilise les chiffres de zéro à sept), ce qui signifie qu'elle est convertie en sa valeur décimale correspondante. Par exemple, si la valeur dans le fichier CSV est 0130, le profil Braze affiche 88. Pour éviter ce problème, veuillez utiliser des attributs avec des types de données de chaîne de caractères. Cependant, ce type de données n'est pas disponible dans la comparaison des numéros de segmentation.

#### Types d'attributs par défaut

Certains attributs par défaut peuvent n'accepter que certaines valeurs comme valides pour les mises à jour utilisateur. Pour obtenir des conseils, veuillez vous référer à [la section Création de votre fichier CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Les espaces finaux et les différences dans l'utilisation des majuscules peuvent entraîner l'interprétation d'une valeur comme non valide. Par exemple, dans le fichier CSV suivant, seul l'utilisateur de la première ligne (`brazetest1`) a vu son e-mail et ses statuts push mis à jour avec succès, car les valeurs acceptées sont `unsubscribed`, `subscribed`, et `opted_in`. 

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### La fonction « Sélectionner un fichier CSV » ne fonctionne pas correctement.

Plusieurs raisons peuvent expliquer pourquoi le bouton **Sélectionner un fichier CSV** ne fonctionne pas :

| Problème | Résolution |
|---|---|
| Bloqueur de fenêtres publicitaires intempestives | Cela pourrait empêcher l'affichage de la page. Veuillez vérifier que votre navigateur autorise les fenêtres contextuelles sur le site Web du tableau de bord de Braze. |
| Navigateur obsolète | Veuillez vous assurer que votre navigateur est à jour ; si ce n'est pas le cas, veuillez le mettre à jour vers la dernière version. |
| Processus en arrière-plan | Veuillez fermer toutes les instances de votre navigateur, puis redémarrer votre ordinateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
