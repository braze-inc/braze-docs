---
nav_title: "Importation de données utilisateurs et d'événements CSV"
article_title: "Importation de données utilisateurs et d'événements CSV"
permalink: "/csv_events/"
description: "Cet article de référence explique comment importer des données utilisateurs et comment importer des événements personnalisés à l'aide de fichiers CSV."
page_type: reference
---

# Importation des données utilisateurs (événements CSV en accès anticipé)

> Braze propose différentes manières d’importer les données des utilisateurs dans la plate-forme : SDK, API, ingestion de données Cloud, intégrations de partenaires technologiques et fichiers CSV. Cet article fournit des instructions détaillées sur la manière d'importer des données utilisateur, y compris sur l'[importation d'événements personnalisés via des fichiers CSV (accès anticipé).](#importing-custom-events)

{% multi_lang_include email-via-sms-warning.md %}

Avant de poursuivre, notez que Braze ne nettoie pas (valide ou formate correctement) les données HTML lors de l'importation. Cela signifie que les tags de script doivent être supprimés de toutes les données d'importation destinées à la personnalisation du web.

## API REST

Vous pouvez utiliser le [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour enregistrer des événements personnalisés, des attributs utilisateurs et des achats pour les utilisateurs.

## Importation CSV

Vous pouvez télécharger et mettre à jour les profils utilisateurs à l'aide de fichiers CSV à partir de **Audience** > Importer des **utilisateurs.**

L'importation de données utilisateurs à l'aide de fichiers CSV permet d'enregistrer et de mettre à jour les attributs utilisateurs tels que le prénom et l'e-mail, en plus des attributs personnalisés tels que la pointure. Vous pouvez importer un fichier CSV en spécifiant l'un des deux identifiants uniques de l'utilisateur : un `external_id` ou un alias d'utilisateur.

{% alert important %}
L'importation d'utilisateurs permet également d'enregistrer et de mettre à jour les événements personnalisés des utilisateurs. Comme pour les attributs d'utilisateurs, vous pouvez importer avec un `external_id`, un `braze_id` ou avec un `user_alias_name` avec `user_alias_label`. Pour plus de détails, consultez la rubrique [Importation d'événements personnalisés](#importing-custom-events).
{% endalert %}

{% alert note %}
Si vous téléchargez un mélange d'utilisateurs avec `external_id` et d'utilisateurs sans , vous devez créer un fichier CSV pour chaque importation. Un fichier CSV ne peut pas contenir à la fois `external_ids` et des alias d'utilisateurs.
{% endalert %}

### Importation avec ID Externe

Lors de l’importation des données client, vous devez spécifier l’identifiant unique de chaque client, également appelé `external_id`. Avant de commencer votre importation CSV, il est important de voir avec votre équipe d’ingénierie comment les utilisateurs seront identifiés dans Braze. Il s'agit généralement d'un ID de base de données interne. Cela devrait s'aligner sur la façon dont les utilisateurs seront identifiés par le SDK de Braze sur les mobiles et le web et est conçu pour que chaque client ait un profil utilisateur unique au sein de Braze sur l'ensemble de ses appareils. Découvrez plus d’informations sur le [cycle de vie du profil utilisateur][13] de Braze.

Lorsque vous indiquez un `external_id` dans votre importation, Braze mettra à jour un utilisateur existant avec le même `external_id`, ou créera un utilisateur nouvellement identifié avec cet `external_id` défini si Braze ne le trouve pas.

- **Télécharger :** [Modèle d'importation d'attributs CSV][import_template]
- **Télécharger :** [Modèle d'importation d'événements CSV][events_template]

### Importation avec alias utilisateur

Pour cibler les utilisateurs qui n’ont pas d’`external_id`, vous pouvez importer une liste d’utilisateurs avec des alias utilisateurs. Un alias sert d’identifiant unique pour un utilisateur, et peut être utile si vous essayez de vendre à des utilisateurs anonymes qui ne sont pas abonnés ou n’ont pas créé de compte sur votre application.

Si vous téléchargez ou mettez à jour des profils d’utilisateur qui sont alias uniquement, vous devez avoir les deux colonnes suivantes dans votre CSV :

- `user_alias_name` : Un identifiant unique de l'utilisateur ; une alternative à l'identifiant de l'utilisateur. `external_id`
- `user_alias_label` : Une étiquette commune permettant de regrouper les alias utilisateurs.

| nom_alias_utilisateur | étiquette_alias_utilisateur | Nom | e-mail | attribut_de_l'échantillon |
| --- | --- | --- | --- | --- |
| 182736485 | mon_identifiant_alt | Smith | smith@user.com | TRUE |
| 182736486 | mon_identifiant_alt | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Lorsque votre importation comporte à la fois un `user_alias_name` et un `user_alias_label`, Braze mettra à jour tous les utilisateurs existants avec les mêmes `user_alias_name` et `user_alias_label`. Si un utilisateur est trouvé, Braze va créer un utilisateur nouvellement identifié avec cet `user_alias_name` défini.

{% alert important %}
Vous ne pouvez pas importer un CSV pour mettre à jour un utilisateur existant avec un `user_alias_name` s’il a déjà un `external_id`. Cela créera plutôt un nouveau profil utilisateur avec les `user_alias_name` associés. Pour associer un utilisateur avec alias uniquement à un `external_id`, utilisez [l’endpoint Identifier les Utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

- **Télécharger :** [Modèle d'importation d'attributs d'alias CSV][template_alias_attributes]
- **Télécharger :** [Modèle d'importation d'alias d'événements CSV][template_alias_events]

### Importation avec ID Braze

Pour mettre à jour les profils utilisateurs existants dans Braze en utilisant une valeur ID interne de Braze au lieu d'une valeur `external_id` ou `user_alias_name` et `user_alias_label`, spécifiez `braze_id` comme en-tête de colonne.

Cela peut s'avérer utile si vous avez exporté des données d'utilisateurs de Braze via notre option d'exportation CSV dans le cadre de la segmentation et que vous souhaitez ajouter un nouvel attribut personnalisé à ces utilisateurs existants.

{% alert important %}
Vous ne pouvez pas importer un CSV pour créer un nouvel utilisateur à l’aide d’un `braze_id`. Cette méthode ne peut être utilisée que pour mettre à jour les utilisateurs existants sur la plate-forme Braze.
{% endalert %}

{% alert tip %}
La valeur `braze_id` peut être étiquetée comme `Appboy ID` dans les exportations CSV du tableau de bord de Braze. Cet ID sera le même que le `braze_id` pour un utilisateur, vous pouvez donc renommer cette colonne en `braze_id` lorsque vous réimporterez le CSV.
{% endalert %}

### Importation d'attributs par défaut

Pour importer des attributs par défaut pour les utilisateurs, allez dans **Importation d'utilisateurs** > Attributs **.** Les attributs utilisateur par défaut sont des clés réservées à Braze. Par exemple, `first_name` ou `email`. Les attributs personnalisés sont spécifiques à votre entreprise. Par exemple, une application de réservation de voyages peut avoir un attribut personnalisé nommé `last_destination_searched`.

{% alert important %}
Lorsque vous importez des données personnalisées sous forme d'attributs, les en-têtes de colonne que vous utilisez doivent correspondre exactement à l'orthographe et aux majuscules des attributs utilisateurs par défaut. Sinon, Braze créera automatiquement un attribut personnalisé sur le profil de cet utilisateur.
{% endalert %}

#### En-têtes de colonne par défaut des données utilisateur

| CHAMP PROFIL UTILISATEUR | TYPE DE DONNÉES | INFORMATIONS | REQUIS |
|---|---|---|---|
| `external_id` | Chaîne de caractères | Un identifiant utilisateur unique pour votre client. | Oui, voir la [note suivante.](#about-external-ids) |
| `user_alias_name` | Chaîne de caractères | Identificateur utilisateur unique pour les utilisateurs anonymes. Une alternative à l’`external_id`. | Non, voir la [note suivante](#about-external-ids). |
| `user_alias_label` | Chaîne de caractères | Un libellé commun pour regrouper les alias d’utilisateurs. | Oui, si `user_alias_name` est utilisé. |
| `first_name` | Chaîne de caractères | Le prénom de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `Jane`). | Non |
| `last_name` | Chaîne de caractères | Le nom de famille de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `Doe`). | Non |
| `email` | Chaîne de caractères | L'e-mail de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `jane.doe@braze.com`). | Non |
| `country` | Chaîne de caractères | Les codes pays doivent être transmis à Braze selon la norme ISO-3166-1 alpha-2 (par exemple, `GB`). | Non |
| `dob` | Chaîne de caractères | Doit être transmis au format "YYYY-MM-DD" (par exemple, `1980-12-21`). Cela importe la date de naissance de vos utilisateurs et vous permet de cibler les utilisateurs dont l’anniversaire est « aujourd’hui ». | Non |
| `gender` | Chaîne de caractères | « H », « F », « A » (autre), « S » (sans objet), « P » (préfère ne pas dire) ou nul (inconnu). | Non |
| `home_city` | Chaîne de caractères | La ville de résidence de vos utilisateurs telle qu'ils l'ont indiquée (par exemple, `London`). | Non |
| `language` | Chaîne de caractères | La langue doit être transmise à Braze selon la norme ISO-639-1 (par exemple, `en`). <br>Consultez notre [liste des langues acceptées][1]. | Non |
| `phone` | Chaîne de caractères | Un numéro de téléphone tel qu'indiqué par vos utilisateurs, au format `E.164` (par exemple, `+442071838750`). <br> Consultez la section [Numéros de téléphone des utilisateurs][2] pour obtenir des conseils sur le formatage. | Non |
| `email_open_tracking_disabled` | Valeur booléenne | vrai ou faux accepté.  Définissez sur True pour désactiver le pixel de suivi d’ouverture dans tous les futurs e-mails envoyés à cet utilisateur.   | Non |
| `email_click_tracking_disabled` | Valeur booléenne | vrai ou faux accepté.  Définissez sur True pour désactiver le suivi de clic pour tous les liens dans les futurs e-mails envoyés à cet utilisateur. | Non |
| `email_subscribe` | Chaîne de caractères | Les valeurs disponibles sont `opted_in` (explicitement consenti à recevoir des e-mails), `unsubscribed` (explicitement refusé de recevoir des e-mails), et `subscribed` (ni accepté, ni refusé). | Non |
| `push_subscribe` | Chaîne de caractères | Les valeurs disponibles sont `opted_in` (explicitement consenti à recevoir des messages de notification push), `unsubscribed` (explicitement  refusé de recevoir des messages de notification push), et `subscribed` (ni accepté, ni refusé). | Non |
| `time_zone` | Chaîne de caractères | Le fuseau horaire doit être transmis à Braze dans le même format que la base de données des fuseaux horaires de l'IANA (par exemple, `America/New_York` ou `Eastern Time (US & Canada)`).  | Non |
| `date_of_first_session` <br><br> `date_of_last_session`| Chaîne de caractères | Peut être transmis dans l'un des formats ISO-8601 suivants : {::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (par exemple, 2019-11-20T18:38:57) </li> </ul> {:/} | Non |
| `subscription_group_id` | Chaîne de caractères | L’`id` de votre groupe d’abonnement. Cet identifiant se trouve sur la page du groupe d’abonnement de votre tableau de bord. | Non |
| `subscription_state` | Chaîne de caractères | Le statut d’abonnement du groupe d’abonnement spécifié par `subscription_group_id`. Les valeurs autorisées sont `unsubscribed` (pas dans le groupe d’abonnement) ou `subscribed` (dans le groupe d’abonnement). | Non, mais fortement recommandé si `subscription_group_id` est utilisé. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

##### À propos des ID externes

Bien que l’`external_id` ne soit pas obligatoire, vous **devez** inclure l'un de ces champs : 
- `external_id` : Un identifiant unique pour votre client, **ou**
- `braze_id` : Un identifiant unique tiré pour les utilisateurs existants de Braze, **ou**
- `user_alias_name` et `user_alias_label`: Un identifiant unique pour un utilisateur anonyme

### Importation d'attributs personnalisés

Vous pouvez importer des attributs personnalisés pour les utilisateurs en allant dans **Importation d'utilisateurs** > Attributs **.** Tous les en-têtes qui ne correspondent pas exactement aux attributs par défaut créent un attribut personnalisé dans Braze.

Les types de données suivants sont acceptés dans l'importation d'utilisateurs :

| Type de données | Description |
|-----------|-------------|
| DateTime | Doit être stocké au format ISO-8601 |
| Valeur booléenne | VRAI ou FAUX |
| Nombre | Entier ou float sans espace ni virgule, les floats doivent utiliser un point (.) comme séparateur décimal. |
| Chaîne de caractères | Peut contenir des virgules à condition que des guillemets doubles entourent la valeur de la colonne. |
| Vide | Les valeurs vides n'écraseront pas les valeurs existantes du profil utilisateur et vous n'avez pas besoin d'inclure tous les attributs existants de l'utilisateur dans votre fichier CSV. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Les tableaux et les jetons ne sont pas pris en charge dans l'importation d'utilisateurs. En particulier pour les tableaux, les virgules dans votre fichier CSV seront interprétées comme un séparateur de colonnes, de sorte que les virgules dans les valeurs entraîneront des erreurs d’analyse du fichier. <br>Pour charger ces types de valeurs, utilisez l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ou [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/).
{% endalert %}

### Mise à jour du statut du groupe d’abonnement

Vous pouvez ajouter des utilisateurs à des groupes d'abonnement e-mail ou SMS par le biais de l'importation d'utilisateurs. Ceci est particulièrement utile pour les SMS, car un utilisateur doit être inscrit dans un groupe d'abonnement SMS pour recevoir des messages avec le canal de communication SMS. Pour plus d'informations, consultez [Groupes d'abonnement SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Si vous mettez à jour le statut du groupe d’abonnement, vous devez avoir les deux colonnes suivantes dans votre CSV :

- `subscription_group_id` : Le site `id` du [groupe d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).
- `subscription_state` : Les valeurs disponibles sont `unsubscribed` (pas dans le groupe d’abonnement) ou `subscribed` (dans le groupe d’abonnement).

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">external_id</th>
    <th class="tg-0pky">Prénom</th>
    <th class="tg-0pky">subscription_group_id</th>
    <th class="tg-0pky">statut_abonnement</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">A8i3mkd99</td>
    <td class="tg-0pky">Colby</td>
    <td class="tg-0pky">6ff593d7-cf69-448b-aca9-abf7d7b8c273</td>
    <td class="tg-0pky">abonné</td>
  </tr>
  <tr>
    <td class="tg-0pky">k2LNhj8KS</td>
    <td class="tg-0pky">Tom</td>
    <td class="tg-0pky">aea02307-a91e-4bc0-abad-1c0bee817dfa</td>
    <td class="tg-0pky">abonné</td>
  </tr>
</tbody>
</table>

{% alert important %}
Un seul `subscription_group_id` peut être défini par ligne dans User Import (Importation d’utilisateurs). Différentes lignes peuvent avoir différentes valeurs `subscription_group_id`. Cependant, si vous devez inscrire les mêmes utilisateurs dans plusieurs groupes d’abonnement, vous devrez effectuer plusieurs importations.
{% endalert %}

### Importation d'événements personnalisés (accès anticipé) {#importing-custom-events}

{% alert important %}
L'importation d'événements personnalisés est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

Pour importer des événements personnalisés pour vos utilisateurs, allez dans **Importation d'utilisateurs** > Événements **.**

Les événements personnalisés sont adaptés à votre entreprise. Par exemple, une application de streaming peut comporter un événement personnalisé appelé film_loué. Votre fichier CSV doit comporter des en-têtes de colonne pour :

- Un des éléments suivants :
  - `external_id`**ou**
  - `braze_id`**ou** 
  - `user_alias_name` et `user_alias_label`
- Nom
- Date

Les événements personnalisés peuvent avoir des propriétés d'événement. Par exemple, l'événement personnalisé film_loué peut inclure les propriétés titre et genre. Ces propriétés d'événement doivent avoir un en-tête de colonne de `<event_name>.properties.<property name>`. Un exemple est `rented_movie.properties.title`.

| CHAMP PROFIL UTILISATEUR                      | TYPE DE DONNÉES | INFORMATIONS                                                                                                                                                                                                             | REQUIS                                                                                        |
|-----------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `external_id`                           | Chaîne de caractères    | Un identifiant unique pour votre utilisateur.                                                                                                                                                                                 | Oui, l'un des éléments suivants est requis : `external_id`, `braze_id` ou `user_alias_name` et `user_alias_label`. |
| `braze_id`                              | Chaîne de caractères    | Identifiant attribué par Braze à votre utilisateur.                                                                                                                                                                              | Oui, l'un des éléments suivants est requis : `external_id`, `braze_id` ou `user_alias_name` et `user_alias_label`. |
| `user_alias_name`                       | Chaîne de caractères    | Identificateur utilisateur unique pour les utilisateurs anonymes. Une alternative à l'identifiant externe.                                                                                                                                        | Oui, l'un des éléments suivants est requis : `external_id`, `braze_id` ou `user_alias_name` et `user_alias_label`. |
| `user_alias_label`                      | Chaîne de caractères    | Un libellé commun pour regrouper les alias d’utilisateurs.                                                                                                                                                                          | Oui, l'un des éléments suivants est requis : `external_id`, `braze_id` ou `user_alias_name` et `user_alias_label`. |
| `name`                                  | Chaîne de caractères    | Un événement personnalisé de vos utilisateurs.                                                                                                                                                                                           | Oui                                                                                             |
| `time`                                  | Chaîne de caractères    | L'heure de l'événement. Peut être transmis dans l'un des formats ISO-8601 suivants : {::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (par exemple, 2019-11-20T18:38:57) </li> </ul> {:/} | Oui                                                                                             |
| `<event name>.properties.<property name>` | Plusieurs  | Une propriété d'événement associée à un événement personnalisé. En voici un exemple `rented_movie.properties.title`                                                                                                                        | Non                                                                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Bien que l'identifiant_externe lui-même ne soit pas obligatoire, vous devez inclure l'un des champs suivants : <br>- `external_id` : Un identifiant unique pour votre client <br>- `braze_id` : Un identifiant unique tiré pour les utilisateurs existants de Braze <br>- `user_alias_name` : Un identifiant unique pour un utilisateur anonyme
{% endalert %}

#### Taille du CSV

Braze accepte les données des utilisateurs au format CSV standard à partir de fichiers d'une taille maximale de 500 Mo. Pour télécharger l'un de nos modèles de fichier CSV, reportez-vous à la section [Importation avec ID externe](#importing-with-external-id) ou [Importation avec alias d'utilisateur](#importing-with-user-alias).

#### Considérations relatives aux points de données

Chaque donnée client importée via CSV remplacera la valeur existante dans les profils utilisateurs et comptera comme un point de données, à l'exception des ID externes et des valeurs vides.

- Les ID externes téléchargés via l'importation CSV ne consommeront pas de points de données. Si vous téléchargez un fichier CSV pour segmenter les utilisateurs existants de Braze en ne téléchargeant que des ID externes, cela peut se faire sans consommer de points de données. Si vous deviez ajouter des données supplémentaires telles que l'e-mail ou le numéro de téléphone d'un utilisateur dans votre importation, cela écraserait les données existantes de l'utilisateur et consommerait vos points de données.
    - Les importations CSV à des fins de segmentation (importations effectuées avec `external_id`, `braze_id`, ou `user_alias_name` comme seul champ) ne consommeront pas de points de données.
- Les valeurs vides n'écraseront pas les valeurs existantes dans le profil de l'utilisateur, et vous n'avez pas besoin d'inclure tous les attributs utilisateurs existants ou les événements personnalisés dans votre fichier CSV.
- La mise à jour de `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` n'est pas prise en compte dans la consommation des points de données.

{% alert important %}
La définition de la langue ou du pays sur un utilisateur via une importation CSV ou une API empêche Braze de capturer automatiquement ces informations via le SDK.
{% endalert %}

## Importation d’un CSV

Pour importer votre fichier CSV :
1. Sélectionnez **Audience** > **Importer des utilisateurs**. 
2. Sélectionnez **Parcourir les fichiers** et sélectionnez le fichier qui vous intéresse, puis sélectionnez **Lancer l'importation**. Braze chargera votre fichier et vérifiera les en-têtes de colonne ainsi que les types de données de chaque colonne.

{% alert important %}
Les importations CSV sont sensibles à la casse. Cela signifie que les lettres majuscules dans les importations CSV écriront le champ comme un attribut personnalisé plutôt qu’un champ standard. Par exemple, « e-mails » est correct, mais « Email » sera considéré comme un attribut personnalisé.
{% endalert %}

![L'option « Événements » est sélectionnée comme type d'informations utilisateur à importer.][5]

Une fois le téléchargement terminé, vous pouvez afficher un aperçu du contenu de votre fichier. Les informations contenues dans le tableau sont basées sur les valeurs des premières lignes de votre fichier CSV.

Vous pouvez suivre la progression sur la page **Import d'utilisateurs**, qui est actualisée toutes les cinq secondes, ou lorsque vous sélectionnez **Actualiser le tableau.** Vous pouvez toujours utiliser le reste du tableau de bord de Braze pendant l’importation, et vous serez notifié lorsque l’importation commence et se termine.

Vous pouvez également consulter vos importations les plus récentes, leur nom de fichier, le type CSV, le nombre de lignes dans le fichier, le nombre de lignes importées avec succès, le nombre total de lignes dans chaque fichier et l'état de chaque importation.

Vous pouvez importer plusieurs fichiers CSV en même temps. Les importations CSV sont exécutées simultanément, ce qui signifie que l'ordre des mises à jour n'est pas garanti en série. Si vous devez importer des CSV les uns après les autres, vous devez attendre qu’un fichier CSV soit terminé avant de commencer à charger le suivant.

Si le processus d'importation rencontre une erreur, une icône d'avertissement apparaît à côté du nombre total de lignes dans le fichier. Vous pouvez survoler l'icône pour obtenir des détails sur les raisons de l'échec de certaines lignes. Une fois l'importation terminée, toutes les données seront ajoutées aux profils existants ou de nouveaux profils seront créés.

![Le téléchargement d'un fichier CSV s'est achevé avec des erreurs impliquant des types de données mixtes dans une seule colonne.][4]{: style="max-width:70%"}

### Considérations

Si Braze remarque une erreur dans les premières lignes de votre fichier pendant le chargement, ces erreurs seront affichées dans le résumé. Par exemple, si votre fichier comprend une ligne mal formée, cette erreur sera notée dans l’aperçu lorsque vous importerez le fichier. Bien qu'un fichier puisse être importé avec des erreurs, il est recommandé de corriger ces erreurs dans votre fichier avant de poursuivre l'importation.

En outre, il est important d'examiner le fichier CSV complet avant le chargement, étant donné que Braze n'analyse pas chaque ligne du fichier d'entrée pour l’aperçu. Cela signifie qu'il peut y avoir des erreurs que Braze ne détecte pas lors de la génération de cet aperçu.

Les lignes mal formées et les lignes manquant une ID externe ne seront pas importées. Toutes les autres erreurs peuvent être importées, mais elles risquent d’interférer avec le filtrage lors de la création d’un segment. Pour plus d'informations, passez à la section [Résolution des problèmes](#troubleshooting).

{% alert warning %}
Les erreurs sont basées uniquement sur le type de données et la structure de fichier. Par exemple, une adresse e-mail mal formatée serait toujours importée car elle peut toujours être parsée comme une chaîne de caractères.
{% endalert %}

### Importation CSV d’un utilisateur Lambda

Vous pouvez utiliser notre script d’importation CSV Lambda S3 sans serveur pour charger vos attributs utilisateurs vers la plateforme. Cette solution fonctionne comme un téléchargeur CSV où vous déposez vos CSV dans un compartiment S3, et les scripts les téléchargent via notre API.

Le temps d'exécution estimé pour un fichier d'un million de lignes devrait être d'environ cinq minutes. Pour plus d'informations, consultez la section [Importation d'attributs utilisateurs CSV vers Braze]({{site.baseurl}}/user_csv_lambda/).

## Segmentation

User import (Importation d’utilisateurs) crée et met à jour les profils d’utilisateur, et peut également être utilisé pour créer des segments. Pour créer un segment, sélectionnez **Générer automatiquement un segment à partir des utilisateurs importés de ce CSV** avant de lancer l'importation.

Vous pouvez définir le nom du segment ou accepter la valeur par défaut, qui correspond au nom de votre fichier. Les fichiers qui ont été utilisés pour créer un segment comporteront un lien permettant de visualiser le segment une fois l'importation terminée.

Le filtre utilisé pour créer le segment sélectionne les utilisateurs qui ont été créés ou mis à jour dans une importation sélectionnée et sont disponibles avec tous les autres filtres sur la page Modifier le Segment.

## Résolution des problèmes{#troubleshooting}

### Lignes manquantes

Plusieurs raisons peuvent expliquer pourquoi le nombre d’utilisateurs importés ne correspond pas forcément au total de lignes dans votre fichier CSV :

- **ID externes en double :** S’il y a des doublons de colonnes d’ID externes, cela peut entraîner des lignes mal formées ou non importées, même si les lignes sont correctement formatées. Dans certains cas, cela n’indique pas une erreur spécifique. Vérifiez si des ID externes dupliqués sont présents dans votre CSV. Si c’est le cas, retirez les doublons et essayez de les charger à nouveau.
- **Caractères accentués :** Votre fichier CSV peut comporter des noms ou des attributs comportant des accents. Assurez-vous que votre fichier est encodé UTF-8 pour éviter tout problème.

### Ligne mal formée

Vous devez inclure une ligne d'en-tête dans votre fichier CSV pour importer correctement vos données. Chaque ligne doit avoir le même nombre de cellules que la ligne d’en-tête. Les lignes qui ont plus, ou moins, de valeurs que la ligne d’en-tête seront exclues de l’importation. Les virgules dans une valeur seront interprétées comme un séparateur et peuvent générer cette erreur. De plus, toutes les données doivent être encodées en UTF-8.

Si votre fichier CSV contient des lignes vides et importe moins de lignes que le nombre total de lignes du fichier CSV, cela n’indique pas forcément un problème puisque les lignes vides n’ont pas besoin d’être importées. Vérifiez le nombre de lignes correctement importées et assurez-vous qu’elles correspondent au nombre d’utilisateurs que vous essayez d’importer.

### Plusieurs types de données

Braze s’attend à ce que toutes les valeurs d’une colonne soient du même type de données. Les valeurs qui ne correspondent pas au type de données de leur attribut provoqueront des erreurs de segmentation.

### Dates incorrectement formatées

Les dates qui ne sont pas au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ne seront pas lues en tant que dates lors de l'importation.

### Quote de chaîne de caractères

Les valeurs encapsulées dans des guillemets simples (‘’) ou doubles (“”) seront lues comme des chaînes de caractères lors de l’importation.

### Données importées comme attribut personnalisé

Si vous constatez qu'une donnée utilisateur par défaut (par exemple, `email` ou `first_name`) est importée en tant qu'attribut personnalisé, vérifiez la casse et l'espacement de votre fichier CSV. Par exemple, `First_name` serait importé comme attribut personnalisé, alors que `first_name` serait correctement importé dans le champ « prénom » sur le profil d’un utilisateur.

[import_template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[events_template]: {% image_buster /assets/download_file/braze-csv-events-import-template.csv %}
[template_alias_attributes]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
[template_alias_events]: {% image_buster /assets/download_file/braze-events-csv-example-user-alias.csv %}
[errors]:#common-errors
[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[5]: {% image_buster /assets/img/importcsv3.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}