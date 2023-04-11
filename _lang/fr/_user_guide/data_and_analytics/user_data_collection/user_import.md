---
nav_title: User Import
article_title: User Import
page_order: 4
page_type: reference
description: "Cet article de référence décrit la façon et les bonnes pratiques pour importer des utilisateurs dans votre tableau de bord de Braze en utilisant l’API REST, l’ingestion de données cloud et le CSV."

---
# User Import

Braze propose différentes manières d’importer les données des utilisateurs dans la plate-forme : SDK, API, ingestion de données Cloud, intégrations avec des partenaires technologiques et fichiers CSV.

{% alert important %}
Braze ne « nettoie » pas les données HTML pendant l’ingestion. Cela signifie que les balises de script doivent être supprimées pour toutes les données d’importation destinées à la personnalisation Web. Allez sur la section [Suppression de données HTML](#html-data-stripping) pour en savoir plus.
{% endalert %}

## API REST

Vous pouvez utiliser l’endpoint Suivi Utilisateur de l’API REST de Braze pour enregistrer les événements personnalisés, les attributs d’utilisateur et les achats des utilisateurs. Voir [Endpoint Suivi Utilisateur][12] pour plus d’informations.

## Ingestion de données Cloud

Vous pouvez utiliser l’ingestion de données cloud de Braze pour importer et maintenir les attributs utilisateurs. Pour plus d’informations, consultez la section [Ingestion de données Cloud][14].

## CSV

Vous pouvez également charger et mettre à jour les profils d’utilisateur via des fichiers CSV sur la page **User Import (Importation d’utilisateurs)**. Cette fonctionnalité prend en charge l’enregistrement et la mise à jour des attributs utilisateur tels que le prénom et l’e-mail, en plus des attributs personnalisés tels que la pointure. Il existe deux manières d’envisager l’importation CSV : importer avec un `external_id` ou avec un alias d’utilisateur.

{% alert note %}
Si vous chargez un mélange d’utilisateurs ayant un `external_id` et d’autres ne l’ayant pas, vous devez créer un CSV pour chaque importation. Un CSV ne peut pas contenir à la fois des `external_ids` et des alias utilisateur.
{% endalert %}

### Importation avec ID Externe

Lors de l’importation des données client, vous devez spécifier l’identifiant unique de chaque client, également appelé `external_id`. Avant de commencer votre importation CSV, il est important de voir avec votre équipe d’ingénierie comment les utilisateurs seront identifiés dans Braze. Ce sera généralement avec un ID d’une base de données interne. Il devra être aligné sur la façon d’identifier les utilisateurs mise en œuvre par le SDK Braze sur mobile et web, pour garantir que chaque client aura un seul profil utilisateur dans Braze pour tous ses appareils. En savoir plus sur le [cycle de vie du profil de l’utilisateur][13] dans Braze.

Lorsque vous indiquez un `external_id` dans votre importation, Braze mettra à jour un utilisateur existant avec le même `external_id`, ou créera un utilisateur nouvellement identifié avec cet `external_id` défini si Braze ne le trouve pas.

<i class="fas fa-file-download"></i> Télécharger : [Modèle d’importation CSV][template]

### Importation avec alias utilisateur

Pour cibler les utilisateurs qui n’ont pas d’`external_id`, vous pouvez importer une liste d’utilisateurs avec des alias utilisateurs. Un alias sert d’identifiant unique pour un utilisateur, et peut être utile si vous essayez de vendre à des utilisateurs anonymes qui ne sont pas abonnés ou n’ont pas créé de compte sur votre application.

Si vous téléchargez ou mettez à jour des profils d’utilisateur qui sont alias uniquement, vous devez avoir les deux colonnes suivantes dans votre CSV :

- `user_alias_name` : Un identifiant utilisateur unique ; une alternative à l’`external_id`.
- `user_alias_label` : un libellé commun pour regrouper les alias d’utilisateurs.

| user_alias_name | user_alias_label | last_name | e-mail | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Lorsque votre importation comporte à la fois un `user_alias_name` et un `user_alias_label`, Braze mettra à jour tous les utilisateurs existants avec les mêmes `user_alias_name` et `user_alias_label`. Si un utilisateur est trouvé, Braze va créer un utilisateur nouvellement identifié avec cet `user_alias_name` défini.

{% alert important %}
Vous ne pouvez pas importer un CSV pour mettre à jour un utilisateur existant avec un `user_alias_name` s’il a déjà un `external_id`. Cela créera plutôt un nouveau profil utilisateur avec les `user_alias_name` associés. Pour associer un utilisateur avec alias uniquement à un `external_id`, utilisez l’endpoint [Identifier les Utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

<i class="fas fa-file-download"></i> Télécharger : [Modèle d’importation d’alias via CSV][template_alias]

### Importation avec ID Braze

Pour mettre à jour les profils utilisateur existants dans Braze en utilisant une valeur d’ID Braze interne au lieu d’un `external_id` ou `user_alias_name` / `user_alias_label` vous pouvez spécifier un `braze_id` en tant qu’en-tête de colonne.

Cela peut être utile si vous avez exporté des données utilisateur segmentées depuis Braze via notre option d’exportation CSV, et que vous souhaitez ajouter un nouvel attribut personnalisé à ces utilisateurs existants.

{% alert important %}
Vous ne pouvez pas importer un CSV pour créer un nouvel utilisateur à l’aide d’un `braze_id`. Cette méthode ne peut être utilisée que pour mettre à jour les utilisateurs existants sur la plate-forme Braze.
{% endalert %}

{% alert tip %}
La valeur `braze_id` peut être étiquetée en tant que `Appboy ID` dans les exportations CSV depuis le tableau de bord de Braze. Cet ID sera identique à celui du `braze_id` pour un utilisateur, vous pouvez donc renommer cette colonne en `braze_id` lorsque vous réimportez le CSV.
{% endalert %}

### Construction de votre CSV

Il y a plusieurs types de données dans Braze. Lors de l’importation ou de la mise à jour des profils utilisateur via un CSV, vous pouvez créer ou mettre à jour des attributs par défaut ou des attributs personnalisés pour les utilisateurs.

- Les attributs utilisateur par défaut sont des clés réservées à Braze. Par exemple, `first_name` ou `email`.
- Les attributs personnalisés sont spécifiques à votre entreprise. Par exemple, une application de réservation de voyages peut avoir un attribut personnalisé nommé `last_destination_searched`.

{% alert important %}
Lors de l’importation des données client, l’orthographe et la casse des en-têtes de colonnes que vous utilisez doivent correspondre exactement à celles des attributs d’utilisateur par défaut. Sinon, Braze créera automatiquement un attribut personnalisé sur le profil de cet utilisateur.
{% endalert %}

Braze accepte les données utilisateur au format CSV standard à partir de fichiers dont la taille maximum est de 500 Mo. Reportez-vous aux sections précédentes sur l’importation pour avoir des modèles CSV téléchargeables.

#### Considérations relatives aux points de données

Chaque élément de données client importées via CSV écrasera la valeur existante sur le profil utilisateur et comptera comme point de données, à l’exception des ID externes et des valeurs vides. 

- Les ID externes chargées via CSV ne consomment pas de points de données. Si vous chargez un CSV pour segmenter des utilisateurs de Braze existants en chargeant uniquement des ID externes, cela ne consommera pas de points de données. Si vous deviez ajouter des données supplémentaires telles que l’e-mail ou le numéro de téléphone de l’utilisateur dans votre importation, cela écraserait les données utilisateur existantes, et consommerait vos points de données.
  - Les importations CSV à des fins de segmentation (importations effectuées avec external_id, braze_id, ou user_alias_name comme seul champ) ne consommeront pas de points de données.
- Les valeurs vides ne remplacent pas les valeurs existantes du profil utilisateur, et vous n’avez pas besoin d’inclure tous les attributs utilisateur existants dans votre fichier CSV.
- Mettre à jour `email_subscribe`, `push_subscribe`, `subscription_group_id`, ou `subscription_state` ne sera pas comptabilisé dans votre consommation de points de données.

{% alert important %}
Définir `language` ou `country` sur un utilisateur via une importation CSV ou une API empêchera Braze de capturer automatiquement ces informations via le SDK.
{% endalert %}

#### En-têtes de colonne par défaut des données utilisateur

| CHAMP PROFIL UTILISATEUR | TYPE DE DONNÉES | INFORMATIONS | REQUIS |
|---|---|---|---|
| `external_id` | String | Un identifiant utilisateur unique pour votre client. | Oui, voir la note suivante |
| `user_alias_name` | String | Identificateur utilisateur unique pour les utilisateurs anonymes. Une alternative à l’`external_id`. | Non, voir la note suivante |
| `user_alias_label` | String | Un libellé commun pour regrouper les alias d’utilisateurs. | Oui si un `user_alias_name` est utilisé |
| `first_name` | String | Le prénom de vos utilisateurs comme ils l’ont indiqué (par ex., `Jane`). | Non |
| `last_name` | String | Le nom de famille de vos utilisateurs comme ils l’ont indiqué (par ex., `Doe`). | Non |
| `email` | String | L’adresse e-mail de vos utilisateurs comme ils l’ont indiqué (par ex., `jane.doe@braze.com`). | Non |
| `country` | String | Les codes pays doivent être transmis à Braze selon la norme ISO-3166-1 alpha-2 (par ex., `GB`). | Non |
| `dob` | String | Doit être transmis au format « AAAA-MM-JJ » (par ex., `1980-12-21`). Cela importe la date de naissance de vos utilisateurs et vous permet de cibler les utilisateurs dont l’anniversaire est « aujourd’hui ». | Non |
| `gender` | String | « H », « F », « A » (autre), « S » (sans objet), « P » (préfère ne pas dire) ou nul (inconnu). | Non |
| `home_city` | String | La ville de vos utilisateurs telle qu’ils l’ont indiqué (par ex., `London`). | Non |
| `language` | String | La langue doit être transmise à Braze selon la norme ISO-639-1 (par ex., `en`). <br>Consultez notre [liste des langues acceptées][1]. | Non |
| `phone` | String | Un numéro de téléphone indiqué par vos utilisateurs, au format `E.164` (par ex., `+442071838750`). <br> Consultez la section [Numéros de téléphone des utilisateurs][2] pour obtenir des conseils de formatage. | Non |
| `email_open_tracking_disabled` | Booléen | vrai ou faux accepté.  Définissez sur True pour désactiver le pixel de suivi d’ouverture dans tous les futurs e-mails envoyés à cet utilisateur.   | Non |
| `email_click_tracking_disabled` | Booléen | vrai ou faux accepté.  Définissez sur True pour désactiver le suivi de clic pour tous les liens dans les futurs e-mails envoyés à cet utilisateur. | Non |
| `email_subscribe` | String | Les valeurs disponibles sont `opted_in` (explicitement consenti à recevoir des e-mails), `unsubscribed` (explicitement refusé de recevoir des e-mails), et `subscribed` (ni accepté, ni refusé). | Non |
| `push_subscribe` | String | Les valeurs disponibles sont `opted_in` (explicitement consenti à recevoir des messages de notification push), `unsubscribed` (explicitement  refusé de recevoir des messages de notification push), et `subscribed` (ni accepté, ni refusé). | Non |
| `time_zone` | String | Le fuseau horaire doit être transmis à Braze au même format que la Base de données des fuseaux horaires de l'IANA (par ex., `America/New_York` ou `Eastern Time (US & Canada)`).  | Non |
| `date_of_first_session` <br><br> `date_of_last_session`| String | Peut être transmis dans l’un des formats ISO 8601 suivants : {::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (e.g., 2019-11-20T18:38:57) </li> </ul> {:/} | Non |
| `subscription_group_id` | String | L’`id` de votre groupe d’abonnement. Cet identifiant se trouve sur la page du groupe d’abonnement de votre tableau de bord. | Non |
| `subscription_state` | String | Le statut d’abonnement du groupe d’abonnement spécifié par `subscription_group_id`. Les valeurs autorisées sont `unsubscribed` (pas dans le groupe d’abonnement) ou `subscribed` (dans le groupe d’abonnement). | Non, mais fortement recommandé si `subscription_group_id` est utilisé |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
Si l’`external_id` elle-même n’est pas obligatoire, vous **devez** inclure l’un de ces champs :
- `external_id` - Un identifiant utilisateur unique pour votre client <br> - OU -
- `braze_id` - Un identifiant utilisateur unique extrait pour les utilisateurs de Braze existants <br> - OU -
- `user_alias_name` - Un identifiant utilisateur unique pour un utilisateur anonyme
{% endalert %}

### Importation de données personnalisées

Les en-têtes qui ne correspondent pas exactement aux données utilisateur par défaut créent un attribut personnalisé dans Braze.

Les types de données suivants sont acceptés dans User Import :
- Date/heure (doit être stocké au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601))
- Booléen (VRAI/FAUX)
- Nombre (Integer ou Float, sans espaces ou virgules ; les floats doivent utiliser un point « . » comme séparateur décimal)
- String (pas de virgule)
- Vide (les valeurs vides ne remplacent pas les valeurs existantes du profil utilisateur, et vous n’avez pas besoin d’inclure dans votre fichier CSV tous les attributs utilisateur existants.)

{% alert important %}
Les tableaux, les jetons de notification push et les types de données d’événements personnalisés ne sont pas pris en charge dans User Import (Importation d’utilisateurs).
En particulier pour les tableaux, les virgules dans votre fichier CSV seront interprétées comme un séparateur de colonnes, de sorte que les virgules dans les valeurs entraîneront des erreurs d’analyse du fichier.

Pour charger ces types de valeurs, utilisez l’[endpoint Suivi Utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-track-endpoint) ou l’[ingestion de données cloud][14].
{% endalert %}

### Mise à jour du statut du groupe d’abonnement

Vous pouvez ajouter des utilisateurs dans des groupes d’abonnement E-mail ou SMS via User Import (Importation d’utilisateurs). Ceci est particulièrement utile pour les SMS, car un utilisateur doit être inscrit dans un groupe d’abonnement SMS pour recevoir des messages via le canal SMS. Pour plus d’informations, consultez [Groupes d’abonnement SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Si vous mettez à jour le statut du groupe d’abonnement, vous devez avoir les deux colonnes suivantes dans votre CSV :

- `subscription_group_id` : L’`id` du [groupe d’abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).
- `subscription_state` : Les valeurs disponibles sont `unsubscribed` (pas dans le groupe d’abonnement) ou `subscribed` (dans le groupe d’abonnement).

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">external_id</th>
    <th class="tg-0pky">first_name</th>
    <th class="tg-0pky">subscription_group_id</th>
    <th class="tg-0pky">subscription_state</th>
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

### Importation d’un CSV

Pour importer votre fichier CSV, allez sur la page **User Import (Importation d’utilisateurs)** dans la section Users (Utilisateurs). Dans le champ texte du bas, **Recent Imports (Importations récentes)**, un tableau qui répertorie vos importations les plus récentes (20 maximum), avec les noms des fichiers, le nombre de lignes dans le fichier, le nombre de lignes importées avec succès, le nombre de lignes totales dans chaque fichier et l’état de chaque importation.

La section supérieure, **Import CSV (Importer CSV)**, affiche les instructions d’importation et a un bouton pour commencer votre importation. Cliquez sur **Select CSV File (Sélectionner fichier CSV)** et sélectionnez votre fichier, puis cliquez sur **Start Upload (Démarrer le chargement)**. Braze chargera votre fichier et vérifiera les en-têtes de colonne ainsi que les types de données de chaque colonne. 

Pour charger un modèle CSV, reportez-vous aux sections [Importer avec ID externe](#import-with-external-id) ou [Importer avec Alias utilisateur](#import-with-user-alias) sur cette page.

{% alert important %}
Les importations CSV sont sensibles à la casse. Cela signifie que les lettres majuscules dans les importations CSV écriront le champ comme un attribut personnalisé plutôt qu’un champ standard. Par exemple, « e-mails » est correct, mais « Email » sera considéré comme un attribut personnalisé.
{% endalert %}

![][3]

Une fois le chargement terminé, un modal s’affiche avec un aperçu du contenu de votre fichier. Toutes les informations de ce tableau sont basées sur les valeurs dans les premières lignes de votre fichier CSV. Pour les en-têtes de colonne, les attributs standards seront écrits en texte normal, tandis que les attributs personnalisés seront en italique et auront leur type noté entre parenthèses. Un bref résumé de votre fichier sera également affiché en haut de la fenêtre contextuelle.

Vous pouvez importer plusieurs CSV en même temps. Les importations CSV s’exécuteront simultanément, et l’ordre des mises à jour n’est pas garanti. Si vous devez importer des CSV les uns après les autres, vous devez attendre qu’un fichier CSV soit terminé avant de commencer à charger le suivant.

Si Braze remarque quelque chose de mal formé dans votre fichier pendant le chargement, ces erreurs seront affichées dans le résumé. Par exemple, si votre fichier comprend une ligne mal formée, cette erreur sera notée dans l’aperçu lorsque vous importerez le fichier. Un fichier peut donc être importé avec des erreurs, mais une importation ne peut pas être interrompue ou annulée une fois lancée. Examinez l’aperçu et, si vous trouvez des erreurs, annulez l’importation et modifiez votre fichier. Il est important d’examiner le fichier CSV complet avant de le charger, car Braze ne scannera pas chaque ligne du fichier d’entrée pour l’aperçu. Cela signifie qu’il peut y avoir des erreurs non capturées par Braze au moment de générer cet aperçu.

Les lignes mal formées et les lignes manquant une ID externe ne seront pas importées. Toutes les autres erreurs peuvent être importées, mais elles risquent d’interférer avec le filtrage lors de la création d’un segment. Pour plus d’informations, consultez la section [Résolution des problèmes](#troubleshooting) .

![Téléchargement CSV terminé avec des erreurs de types de données mixtes dans une colonne][4]{: style="max-width:70%"}

{% alert warning %}
Les erreurs sont basées uniquement sur le type de données et la structure de fichier. Par exemple, une adresse e-mail mal formatée serait toujours importée car elle peut toujours être parsée comme une chaîne de caractères.
{% endalert %}

Lorsque vous êtes satisfait du chargement, démarrez l’importation. La fenêtre contextuelle se ferme et l’importation commence en arrière-plan. Vous pouvez suivre son avancement sur la page **User Import (Importation d’utilisateurs) **, qui est actualisée toutes les 5 secondes ou en utilisant le bouton d’actualisation de la section **Recent Imports (Importations récentes)**.

Sous **Lines Processed (Lignes traitées)**, vous verrez la progression de l’importation ; l’état passera à Complete (Terminé) lorsque vous aurez terminé. Vous pouvez toujours utiliser le reste du tableau de bord de Braze pendant l’importation, et vous serez notifié lorsque l’importation commence et se termine.

Si le processus d’importation rencontre une erreur, une icône jaune d’avertissement s’affichera à côté du nombre total de lignes dans le fichier. Vous pouvez survoler l’icône pour voir la cause de l’échec de certaines lignes. Une fois l’importation terminée, toutes les données seront ajoutées aux profils existants, ou de nouveaux profils seront créés.

### Importation CSV d’un utilisateur Lambda

Vous pouvez utiliser notre script d’importation CSV Lambda S3 sans serveur pour charger vos attributs utilisateurs vers la plateforme. Cette solution fonctionne comme un chargeur CSV dans lequel vous mettez votre CSV dans un compartiment S3 et il est chargé avec notre API.

Le temps d’exécution estimé pour un fichier ayant 1 million de lignes devrait être d’environ 5 minutes. Consultez la section [Importation CSV d’un attribut utilisateur vers Braze]({{site.baseurl}}/user_csv_lambda/) pour plus d’informations.

## Segmentation

User import (Importation d’utilisateurs) crée et met à jour les profils d’utilisateur, et peut également être utilisé pour créer des segments. Pour créer un segment, sélectionnez **Automatically generate a segment from the users who are imported from this CSV (Générer automatiquement un segment pour les utilisateurs importés par ce fichier CSV)** avant de démarrer l’importation.

Vous pouvez définir le nom du segment ou accepter la valeur par défaut, qui correspond au nom de votre fichier. Les fichiers utilisés pour créer un segment auront un lien vers le segment une fois l’importation terminée.

Le filtre utilisé pour créer le segment sélectionne les utilisateurs qui ont été créés ou mis à jour dans une importation sélectionnée et sont disponibles avec tous les autres filtres sur la page Modifier le Segment.

## Suppression de données HTML

Braze ne « nettoie » pas les données HTML pendant l’ingestion. Lors de l’importation de données dans Braze spécifiquement destinées à la personnalisation dans un navigateur Web, assurez-vous qu’elles ne contiennent pas de balises HTML, JavaScript ou de tout autre script susceptible d’être utilisé à des fins malveillantes dans un navigateur Web.  

Vous pouvez également utiliser les filtres Liquid de Braze (de type HTML) (`strip_html`) pour faire un échappement HTML sur le texte rendu. Par exemple :

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" &#124; strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Résolution des problèmes{#troubleshooting}

### Lignes manquantes

Plusieurs raisons peuvent expliquer pourquoi le nombre d’utilisateurs importés ne correspond pas forcément au total de lignes dans votre fichier CSV :

- **ID externes en double :** S’il y a des doublons de colonnes d’ID externes, cela peut entraîner des lignes mal formées ou non importées, même si les lignes sont correctement formatées. Dans certains cas, cela n’indique pas une erreur spécifique. Vérifiez si des ID externes dupliqués sont présents dans votre CSV. Si c’est le cas, retirez les doublons et essayez de les charger à nouveau.
- **Accents :** Votre CSV peut comporter des noms ou des attributs qui contiennent des accents. Assurez-vous que votre fichier est encodé UTF-8 pour éviter tout problème.

### Ligne mal formée

Pour importer correctement les données, il doit y avoir une ligne d’en-tête. Chaque ligne doit avoir le même nombre de cellules que la ligne d’en-tête. Les lignes qui ont plus, ou moins, de valeurs que la ligne d’en-tête seront exclues de l’importation. Les virgules dans une valeur seront interprétées comme un séparateur et peuvent générer cette erreur. De plus, toutes les données doivent être encodées en UTF-8.

Si votre fichier CSV contient des lignes vides et importe moins de lignes que le nombre total de lignes du fichier CSV, cela n’indique pas forcément un problème puisque les lignes vides n’ont pas besoin d’être importées. Vérifiez le nombre de lignes correctement importées et assurez-vous qu’elles correspondent au nombre d’utilisateurs que vous essayez d’importer.

### Plusieurs types de données

Braze s’attend à ce que toutes les valeurs d’une colonne soient du même type de données. Les valeurs qui ne correspondent pas au type de données de leur attribut provoqueront des erreurs de segmentation.

### Dates incorrectement formatées

Les Dates qui ne sont pas au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ne seront pas lus comme des dates lors de l’importation.

### Quote de chaîne de caractères

Les valeurs encapsulées dans des guillemets simples (‘’) ou doubles (“”) seront lues comme des chaînes de caractères lors de l’importation.

### Données importées comme attribut personnalisé

Si vous voyez un élément de données utilisateur par défaut (par ex., `email` ou `first_name`) importé en tant qu’attribut personnalisé, vérifiez la casse et l’espacement de votre fichier CSV. Par exemple, `First_name` serait importé comme attribut personnalisé, alors que `first_name` serait correctement importé dans le champ « prénom » sur le profil d’un utilisateur.

{% alert important %}
Braze interdit ou bloque les utilisateurs avec plus de 5 millions de sessions (« utilisateurs factices ») et cesse d’ingérer leurs événements SDK. Pour plus d’informations, consultez [Blocage des courriers indésirables]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).
{% endalert %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[3]: {% image_buster /assets/img/importcsv.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}
[12]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-track-endpoint
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/
[errors]:#common-errors
[template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[template_alias]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
