---
nav_title: Importation d’utilisateurs
article_title: Importation d’utilisateurs
page_order: 4
page_type: reference
description: "Cet article de référence décrit la façon et les bonnes pratiques pour importer des utilisateurs dans votre tableau de bord de Braze en utilisant l’API REST, l’ingestion de données cloud et le CSV."

---
# User Import

> Braze propose différentes manières d’importer les données des utilisateurs dans la plate-forme : SDK, API, Cloud Data Ingestion, intégrations de partenaires technologiques et fichiers CSV.

Avant de poursuivre, notez que Braze ne nettoie pas (valide ou formate correctement) les données HTML lors de l'importation. Cela signifie que les balises de script doivent être supprimées pour toutes les données d’importation destinées à la personnalisation Web.

Lorsque vous importez dans Braze des données spécifiquement destinées à la personnalisation dans un navigateur web, veillez à ce qu'elles soient dépourvues de HTML, de JavaScript ou de toute autre étiquette de script susceptible d'être utilisée à des fins malveillantes lorsqu'elles sont affichées dans un navigateur web.  

Pour le HTML, vous pouvez également utiliser les filtres Liquid de Braze (`strip_html`) afin d'extraire le texte rendu du HTML. Par exemple :

{% tabs local %}
{% tab Entrée %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Sortie %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## API REST

Utilisez l'endpoint [`/users/track`][12] pour enregistrer des événements personnalisés, des attributs utilisateurs et des achats pour les utilisateurs.

## Ingestion de données cloud

Utilisez Braze [Cloud Data Ingestion][14] ] pour importer et gérer les attributs des utilisateurs. 

## Importation CSV

Vous pouvez télécharger et mettre à jour les profils utilisateurs à l'aide de fichiers CSV à partir de **Audience** > Importer des **utilisateurs.**

L'importation d'un fichier CSV permet d'enregistrer et de mettre à jour les attributs des utilisateurs, tels que le prénom et l'e-mail, ainsi que des attributs personnalisés comme la pointure. Vous pouvez importer un fichier CSV en spécifiant l'un des deux identifiants uniques de l'utilisateur : un `external_id` ou un alias d'utilisateur.

{% alert note %}
Si vous téléchargez un mélange d'utilisateurs avec `external_id` et d'utilisateurs sans , vous devez créer un CSV pour chaque importation. Un CSV ne peut pas contenir à la fois des `external_ids` et des alias utilisateur.
{% endalert %}

### Création de votre fichier CSV

Il y a plusieurs types de données dans Braze. Lors de l'importation ou de la mise à jour de profils utilisateurs à l'aide d'un fichier CSV, vous pouvez créer ou mettre à jour des attributs utilisateurs par défaut ou des attributs personnalisés.

- Les attributs utilisateur par défaut sont des clés réservées à Braze. Par exemple, `first_name` ou `email`.
- Les attributs personnalisés sont spécifiques à votre entreprise. Par exemple, une application de réservation de voyages peut avoir un attribut personnalisé nommé `last_destination_searched`.

{% alert important %}
Lors de l’importation des données client, l’orthographe et la casse des en-têtes de colonnes que vous utilisez doivent correspondre exactement à celles des attributs d’utilisateur par défaut. Sinon, Braze créera automatiquement un attribut personnalisé sur le profil de cet utilisateur.
{% endalert %}

Braze accepte les données des utilisateurs au format CSV standard à partir de fichiers d'une taille maximale de 500 Mo. Reportez-vous aux sections précédentes sur l’importation pour avoir des modèles CSV téléchargeables.

#### Considérations relatives aux points de données

Chaque donnée client importée à partir d'un fichier CSV remplacera la valeur existante dans les profils utilisateurs et comptera comme un point de données, à l'exception des ID externes et des valeurs vides. 

- Les ID externes téléchargés à partir d'un fichier CSV ne consomment pas de points de données. Si vous chargez un CSV pour segmenter des utilisateurs de Braze existants en chargeant uniquement des ID externes, cela ne consommera pas de points de données. Si vous deviez ajouter des données supplémentaires telles que les e-mails ou les numéros de téléphone des utilisateurs dans votre importation, cela écraserait les données existantes sur les utilisateurs, consommant ainsi vos points de données.
  - Les importations CSV à des fins de segmentation (importations effectuées avec `external_id`, `braze_id`, ou `user_alias_name` comme seul champ) ne consommeront pas de points de données.
- Les valeurs vides ne remplacent pas les valeurs existantes du profil utilisateur, et vous n’avez pas besoin d’inclure tous les attributs utilisateur existants dans votre fichier CSV.
- La mise à jour de `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` n'est pas prise en compte dans la consommation des points de données.

{% alert important %}
La définition de `language` ou `country` sur un utilisateur via l'importation CSV ou l'API empêchera Braze de capturer automatiquement ces informations via le SDK.
{% endalert %}

#### En-têtes de colonne par défaut des données utilisateur

| CHAMP PROFIL UTILISATEUR | TYPE DE DONNÉES | INFORMATIONS | REQUIS |
|---|---|---|---|
| `external_id` | Chaîne de caractères | Un identifiant utilisateur unique pour votre client. | Oui, voir la note suivante |
| `user_alias_name` | Chaîne de caractères | Identificateur utilisateur unique pour les utilisateurs anonymes. Une alternative à l’`external_id`. | Non, voir la note suivante |
| `user_alias_label` | Chaîne de caractères | Un libellé commun pour regrouper les alias d’utilisateurs. | Oui si un `user_alias_name` est utilisé |
| `first_name` | Chaîne de caractères | Le prénom de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `Jane`). | Non |
| `last_name` | Chaîne de caractères | Le nom de famille de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `Doe`). | Non |
| `email` | Chaîne de caractères | L'e-mail de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `jane.doe@braze.com`). | Non |
| `country` | Chaîne de caractères | Les codes pays doivent être transmis à Braze selon la norme ISO-3166-1 alpha-2 (par exemple, `GB`). | Non |
| `dob` | Chaîne de caractères | Doit être transmis au format "YYYY-MM-DD" (par exemple, `1980-12-21`). Cela importe la date de naissance de vos utilisateurs et vous permet de cibler les utilisateurs dont l’anniversaire est « aujourd’hui ». | Non |
| `gender` | Chaîne de caractères | « H », « F », « A » (autre), « S » (sans objet), « P » (préfère ne pas dire) ou nul (inconnu). | Non |
| `home_city` | Chaîne de caractères | La ville de résidence de vos utilisateurs telle qu'ils l'ont indiquée (par exemple, `London`). | Non |
| `language` | Chaîne de caractères | La langue doit être transmise à Braze selon la norme ISO-639-1 (par exemple, `en`). <br>Consultez notre [liste des langues acceptées][1]. | Non |
| `phone` | Chaîne de caractères | Un numéro de téléphone tel qu'indiqué par vos utilisateurs, au format `E.164` (par exemple, `+442071838750`). <br> Reportez-vous à la section [Numéros de téléphone des utilisateurs][2] pour obtenir des conseils sur le formatage. | Non |
| `email_open_tracking_disabled` | Valeur booléenne | vrai ou faux accepté.  Définissez sur True pour désactiver le pixel de suivi d’ouverture dans tous les futurs e-mails envoyés à cet utilisateur.   | Non |
| `email_click_tracking_disabled` | Valeur booléenne | vrai ou faux accepté.  Définissez sur True pour désactiver le suivi de clic pour tous les liens dans les futurs e-mails envoyés à cet utilisateur. | Non |
| `email_subscribe` | Chaîne de caractères | Les valeurs disponibles sont `opted_in` (explicitement consenti à recevoir des e-mails), `unsubscribed` (explicitement refusé de recevoir des e-mails), et `subscribed` (ni accepté, ni refusé). | Non |
| `push_subscribe` | Chaîne de caractères | Les valeurs disponibles sont `opted_in` (explicitement consenti à recevoir des messages de notification push), `unsubscribed` (explicitement  refusé de recevoir des messages de notification push), et `subscribed` (ni accepté, ni refusé). | Non |
| `time_zone` | Chaîne de caractères | Le fuseau horaire doit être transmis à Braze dans le même format que la base de données des fuseaux horaires de l'IANA (par exemple, `America/New_York` ou `Eastern Time (US & Canada)`).  | Non |
| `date_of_first_session` <br><br> `date_of_last_session`| Chaîne de caractères | Peut être transmis dans l'un des formats ISO 8601 suivants : {::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (par exemple, 2019-11-20T18:38:57) </li> </ul> {:/} | Non |
| `subscription_group_id` | Chaîne de caractères | L’`id` de votre groupe d’abonnement. Cet identifiant se trouve sur la page du groupe d’abonnement de votre tableau de bord. | Non |
| `subscription_state` | Chaîne de caractères | Le statut d’abonnement du groupe d’abonnement spécifié par `subscription_group_id`. Les valeurs autorisées sont `unsubscribed` (pas dans le groupe d’abonnement) ou `subscribed` (dans le groupe d’abonnement). | Non, mais fortement recommandé si `subscription_group_id` est utilisé |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Bien que `external_id` ne soit pas obligatoire, vous **devez** inclure l'un de ces champs :
- `external_id` : Un identifiant unique pour votre client <br> \- OU -
- `braze_id` : Un identifiant unique tiré pour les utilisateurs existants de Braze <br> \- OU -
- `user_alias_name` : Un identifiant unique pour un utilisateur anonyme
{% endalert %}

### Importation d’un CSV

Pour importer votre fichier CSV, allez dans **Audiences** > Importation d'utilisateurs **.** Vous y trouverez un tableau qui répertorie les importations les plus récentes, avec des détails tels que la date de téléchargement, le nom du téléchargeur, le nom du fichier, la disponibilité du ciblage, le nombre de lignes importées et l'état de chaque importation.

![La page "Importation d'utilisateurs" du tableau de bord de Braze.][3]

Sélectionnez **Parcourir les fichiers** et votre fichier. Braze téléchargera votre fichier et vérifiera les en-têtes de colonne et les types de données de chaque colonne.

Pour télécharger un modèle CSV, reportez-vous aux sections [Importation avec ID externe](#importing-with-external-id) ou [Importation avec alias utilisateur](#importing-with-user-alias) sur cette page.

{% alert important %}
Les importations CSV sont sensibles à la casse. Cela signifie que les lettres majuscules dans les importations CSV écriront le champ comme un attribut personnalisé plutôt qu’un champ standard. Par exemple, « e-mails » est correct, mais « Email » sera considéré comme un attribut personnalisé.
{% endalert %}

Une fois le chargement terminé, une fenêtre modale s'affiche avec un aperçu du contenu de votre fichier. Toutes les informations de ce tableau sont basées sur les valeurs dans les premières lignes de votre fichier CSV. Pour les en-têtes de colonne, les attributs standard sont écrits en texte normal, tandis que les attributs personnalisés sont en italique et leur type est noté entre parenthèses. Un résumé de votre dossier figure également en haut de la fenêtre contextuelle.

Vous pouvez importer plusieurs CSV en même temps. Les importations CSV sont exécutées simultanément, de sorte que l'ordre des mises à jour n'est pas garanti. Si vous souhaitez que les importations CSV soient exécutées l'une après l'autre, attendez qu'une importation CSV soit terminée avant d'en télécharger une seconde.

Si Braze constate une anomalie dans votre fichier pendant le chargement, ces erreurs apparaîtront dans le résumé. Par exemple, si votre fichier contient une ligne mal formée, cette erreur est signalée dans l'aperçu lorsque vous importez le fichier. Ainsi, un fichier peut être importé avec des erreurs, mais une importation ne peut pas être annulée ou inversée une fois qu'elle a commencé. Examinez l’aperçu et, si vous trouvez des erreurs, annulez l’importation et modifiez votre fichier. 

{% alert important %}
Examinez le fichier CSV complet avant de le charger, car Braze ne scanne pas chaque ligne du fichier d'entrée pour la prévisualisation. Cela signifie qu'il peut y avoir des erreurs que Braze ne détecte pas lors de la génération de cet aperçu.
{% endalert %}

Les lignes mal formées et les lignes manquant une ID externe ne seront pas importées. Toutes les autres erreurs peuvent être importées, mais elles risquent d’interférer avec le filtrage lors de la création d’un segment. Pour plus d'informations, passez à la section [Résolution des problèmes](#troubleshooting).

![Chargement CSV terminé avec des erreurs de types de données mixtes dans une colonne][4]{: style="max-width:70%"}

{% alert warning %}
Les erreurs sont basées uniquement sur le type de données et la structure de fichier. Par exemple, une adresse e-mail mal formatée serait toujours importée car elle peut toujours être parsée comme une chaîne de caractères.
{% endalert %}

Lorsque vous êtes satisfait du chargement, démarrez l’importation. La fenêtre contextuelle se ferme et l’importation commence en arrière-plan. Vous pouvez suivre sa progression sur la page **Importations d'utilisateurs**, qui sera actualisée toutes les cinq secondes, ou en appuyant sur le bouton d'actualisation dans la boîte **Imports récents.** 

Sous **Lignes traitées** se trouve l'état d'avancement de l'importation ; l'état passera à **Terminé** lorsque l'importation sera terminée. Vous pouvez toujours utiliser le reste du tableau de bord de Braze pendant l’importation, et vous serez notifié lorsque l’importation commence et se termine.

Si le processus d'importation rencontre une erreur, une icône d'avertissement jaune s'affiche à côté du nombre total de lignes dans le fichier. Vous pouvez survoler l'icône pour obtenir des détails sur les raisons de l'échec de certaines lignes. Une fois l'importation terminée, toutes les données seront ajoutées aux profils existants ou de nouveaux profils seront créés.

### Importation avec ID Externe

Lors de l'importation de vos données clients, vous devrez spécifier l'identifiant unique de chaque client (`external_id`). Avant de commencer votre importation CSV, il est important de voir avec votre équipe d’ingénierie comment les utilisateurs seront identifiés dans Braze. Il s'agit généralement d'un ID de base de données interne. Cela devrait s'aligner sur la façon dont les utilisateurs seront identifiés par le SDK de Braze sur les mobiles et le web et est conçu pour que chaque client ait un profil utilisateur unique au sein de Braze sur l'ensemble de ses appareils. Découvrez plus d’informations sur le [cycle de vie du profil utilisateur][13] de Braze.

Lorsque vous indiquez un `external_id` dans votre importation, Braze mettra à jour un utilisateur existant avec le même `external_id`, ou créera un utilisateur nouvellement identifié avec cet `external_id` défini si Braze ne le trouve pas.

**Téléchargez :** [Modèle d'importation CSV][modèle]

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

**Télécharger :** [Modèle d'importation d'alias CSV][template_alias]

### Importation avec ID Braze

Pour mettre à jour les profils utilisateurs existants dans Braze en utilisant une valeur ID interne de Braze au lieu d'une valeur `external_id` ou `user_alias_name` et `user_alias_label`, spécifiez `braze_id` comme en-tête de colonne.

Cela peut s'avérer utile si vous avez exporté des données d'utilisateurs de Braze via notre option d'exportation CSV dans le cadre de la segmentation et que vous souhaitez ajouter un nouvel attribut personnalisé à ces utilisateurs existants.

{% alert important %}
Vous ne pouvez pas importer un CSV pour créer un nouvel utilisateur à l’aide d’un `braze_id`. Cette méthode ne peut être utilisée que pour mettre à jour les utilisateurs existants sur la plate-forme Braze.
{% endalert %}

{% alert tip %}
La valeur `braze_id` peut être étiquetée comme `Appboy ID` dans les exportations CSV du tableau de bord de Braze. Cet ID sera le même que le `braze_id` pour un utilisateur, vous pouvez donc renommer cette colonne en `braze_id` lorsque vous réimporterez le CSV.
{% endalert %}

### Importation d'adresses e-mail et de numéros de téléphone

Vous pouvez omettre un ID externe ou un alias utilisateur et utiliser une adresse e-mail ou un numéro de téléphone pour importer des utilisateurs. Avant d'importer un fichier CSV contenant des adresses e-mail ou des numéros de téléphone, vérifiez les points suivants :

- Vérifiez que vous n'avez pas d'ID externe ou d'aliasing de l'utilisateur pour ces profils dans votre fichier CSV. Si vous le faites, Braze utilisera en priorité l'ID externe ou l'alias d'utilisateur avant l'adresse e-mail pour identifier les profils.
- Confirmez que votre fichier CSV est correctement formaté.

{% alert note %}
Si vous incluez à la fois des adresses e-mail et des numéros de téléphone dans votre fichier CSV, l'adresse e-mail est prioritaire sur le numéro de téléphone lors de la recherche de profils.
{% endalert %}

Si un profil existant comporte cette adresse e-mail ou ce numéro de téléphone, ce profil sera mis à jour et Braze ne créera pas de nouveau profil. S'il existe plusieurs profils avec la même adresse e-mail, Braze utilisera la même logique que l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) où le profil le plus récemment mis à jour sera mis à jour.

Si un profil avec cette adresse e-mail ou ce numéro de téléphone n'existe pas, Braze créera un nouveau profil avec cet identifiant. Vous pouvez utiliser l'[endpoint`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) pour identifier ce profil ultérieurement. Pour supprimer un profil utilisateur, vous pouvez également utiliser l’enpoint [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete).

### Importation de données personnalisées

Tout en-tête qui ne correspond pas exactement aux données utilisateur par défaut créera un attribut personnalisé dans Braze.

Les types de données suivants sont acceptés dans l'importation d'utilisateurs :
- **Datetime :** Doit être stocké au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 
- **Booléen :** `true` ou `false`
- **Nombre :** Entier ou float sans espace ni virgule, les floats doivent utiliser un point (`.`) comme séparateur décimal.
- **Chaîne de caractères :** Peut contenir des virgules si des guillemets doubles (`""`) entourent la valeur de la colonne.
- **En blanc :** Les valeurs vides n'écraseront pas les valeurs existantes du profil utilisateur et vous n'avez pas besoin d'inclure tous les attributs existants de l'utilisateur dans votre fichier CSV.

{% alert important %}
Les tableaux, les jetons de poussée et les types de données d'événements personnalisés ne sont pas pris en charge dans l'importation d'utilisateurs.
En particulier pour les tableaux, les virgules dans votre fichier CSV seront interprétées comme un séparateur de colonnes, de sorte que toute virgule dans les valeurs provoquera des erreurs lors de l'analyse du fichier.<br><br>Pour charger ces types de valeurs, utilisez l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ou [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/).
{% endalert %}

### Importation CSV d’un utilisateur Lambda

Vous pouvez utiliser notre script d’importation CSV Lambda S3 sans serveur pour charger vos attributs utilisateurs vers la plateforme. Cette solution fonctionne comme un téléchargeur CSV où vous déposez vos CSV dans un compartiment S3, et les scripts les téléchargent via notre API.

Le temps d'exécution estimé pour un fichier de 1 000 000 de lignes devrait être d'environ cinq minutes. Pour plus d'informations, reportez-vous à la section [Importation d'un attribut utilisateur au format CSV vers Braze.]({{site.baseurl}}/user_guide/data/cloud_ingestion/) 

### Mise à jour du statut du groupe d’abonnement

Vous pouvez ajouter des utilisateurs à des groupes d'abonnement e-mail ou SMS par le biais de l'importation d'utilisateurs. Ceci est particulièrement utile pour les SMS, car un utilisateur doit être inscrit dans un groupe d'abonnement SMS pour recevoir des messages avec le canal de communication SMS. Pour plus d'informations, consultez [Groupes d'abonnement SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

Si vous mettez à jour les statuts du groupe d'abonnement, les deux colonnes suivantes doivent figurer dans votre fichier CSV :

- `subscription_group_id` : Le site `id` du [groupe d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).
- `subscription_state` : Les valeurs disponibles sont `unsubscribed` (pas dans le subscription groups) ou `subscribed` (dans le subscription groups).

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
Un seul `subscription_group_id` peut être défini par ligne dans User Import (Importation d’utilisateurs). Différentes lignes peuvent avoir différentes valeurs `subscription_group_id`. Toutefois, si vous devez inscrire les mêmes utilisateurs dans plusieurs groupes d'abonnement, vous devrez procéder à plusieurs importations.
{% endalert %}

## Création d'un filtre reciblage à partir d'une importation d'utilisateurs

L'importation d'utilisateurs peut être utilisée pour transformer le fichier CSV en filtre de reciblage en sélectionnant **Importer des utilisateurs dans ce CSV et permettre de recibler ce lot spécifique d'utilisateurs en tant que groupe**. Pour filtrer par fichier dans un segment ou partout où le filtrage est possible, sélectionnez le filtre **Mise à jour/Importation depuis CSV**, puis recherchez le nom exact du fichier.

![Un groupe de filtres avec le filtre "Mis à jour/Importé depuis CSV" comprenant un fichier CSV intitulé "Plaisirs de la saison d'Halloween".][5]

## Création de segmentations à partir d'une importation d'utilisateurs

L'importation d'utilisateurs peut également être utilisée pour créer des segments en sélectionnant **Importer des utilisateurs dans ce CSV et permettre de recibler ce lot spécifique d'utilisateurs en tant que groupe** et en cochant **Générer automatiquement un segment à partir des utilisateurs importés de ce CSV** avant de lancer l'importation.

Vous pouvez définir le nom du segment ou accepter la valeur par défaut, qui correspond au nom de votre fichier. Les fichiers qui ont été utilisés pour créer un segment comporteront un lien permettant de visualiser le segment une fois l'importation terminée.

Le filtre utilisé pour créer le segment sélectionne les utilisateurs qui ont été créés ou mis à jour dans une importation sélectionnée et sont disponibles avec tous les autres filtres sur la page Modifier le Segment.

## Considérations

{% multi_lang_include email-via-sms-warning.md %}

## Résolution des problèmes

###  Le téléchargement s'est terminé avec des erreurs

#### Ligne mal formée

Il doit y avoir une ligne d'en-tête pour que les données soient correctement importées. Chaque ligne doit avoir le même nombre de cellules que la ligne d’en-tête. Les lignes qui ont plus, ou moins, de valeurs que la ligne d’en-tête seront exclues de l’importation. Les virgules dans une valeur seront interprétées comme un séparateur et peuvent conduire à cette erreur. De plus, toutes les données doivent être encodées en UTF-8.

Si votre fichier CSV contient des lignes vides et importe moins de lignes que le nombre total de lignes du fichier CSV, cela n’indique pas forcément un problème puisque les lignes vides n’ont pas besoin d’être importées. Vérifiez le nombre de lignes correctement importées et assurez-vous qu’elles correspondent au nombre d’utilisateurs que vous essayez d’importer.

#### Adresses e-mail non valides

Braze a détecté des adresses e-mail cryptées non valides. Confirmez que toutes les adresses e-mail sont correctement cryptées avant de les importer dans Braze.

- **Lors de la [mise à jour ou de l'importation d'adresses e-mail]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)** dans Braze, utilisez la valeur hachée de l'e-mail chaque fois qu'un e-mail est inclus. Ces valeurs d'e-mail de hachage sont fournies par votre équipe interne. 
- **Lors de la création d'un nouvel utilisateur**, vous devez ajouter `email_encrypted` avec la valeur de l'e-mail crypté de l'utilisateur. Sinon, l'utilisateur ne sera pas créé. De même, si vous ajoutez une adresse e-mail à un utilisateur existant qui n'a pas d'e-mail, vous devez ajouter `email_encrypted`. Sinon, l'utilisateur ne sera pas mis à jour.

### Lignes manquantes

Plusieurs raisons peuvent expliquer pourquoi le nombre d’utilisateurs importés ne correspond pas forcément au total de lignes dans votre fichier CSV :

- **Dupliquer des ID externes, des alias d'utilisateurs, des ID Braze, des adresses e-mail ou des numéros de téléphone :** Si des colonnes d'ID externe sont dupliquées, cela peut entraîner des lignes mal formées ou non importées, même si les lignes sont correctement formatées. Dans certains cas, il se peut qu'aucune erreur spécifique ne soit signalée. Vérifiez si des ID externes dupliqués sont présents dans votre CSV. Si c’est le cas, retirez les doublons et essayez de les charger à nouveau.
- **Caractères accentués :** Votre CSV peut comporter des noms ou des attributs qui contiennent des accents. Assurez-vous que votre fichier est encodé UTF-8 pour éviter tout problème.
- **L'ID de Braze appartient à un utilisateur orphelin :** Lorsqu'un utilisateur est orphelin, l'utilisateur restant avec lequel l'orphelin a été fusionné peut encore ne pas associer l'ID Braze de l'utilisateur orphelin au profil. Dans ce cas, Braze ne trouvera pas d'utilisateur à mettre à jour, et la ligne ne sera donc pas considérée comme importée.
- **Rangée vide :** Il y a une ligne vide dans le fichier CSV. Cela peut être vérifié si vous ouvrez le fichier CSV dans un programme d'édition de texte (n'utilisez pas Excel ou Sheets). Si vous téléchargez le fichier CSV avec une ligne vide, un message d'erreur s'affichera, indiquant que certaines lignes contiennent des données mal formées.
- **Y compris les guillemets doubles (`"`) :** Ce caractère n'est pas valide et rendra la ligne malformée. Utilisez plutôt des guillemets simples (`'`).
- **Sauts de ligne incohérents :** Par exemple, si le fichier CSV utilise `\n` pour la première ligne et `\r\n` pour chaque ligne suivante, la première ligne de données sera traitée comme faisant partie de l'en-tête, et ces données ne seront pas importées comme prévu. Vous pouvez le vérifier dans un éditeur hexagonal ou un éditeur de texte spécialisé qui distingue les caractères d'espacement.
- **Fichier mal encodé :** Le fichier CSV peut inclure des noms ou des attributs comportant des accents, mais le fichier doit être codé en UTF-8 pour les importer correctement. D'autres codages de caractères peuvent fonctionner dans certaines instances, mais seul l'UTF-8 est totalement compatible.

### Dates incorrectement formatées

Les dates qui ne sont pas au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ne seront pas lues comme `datetimes` lors de l'importation.

### Quote de chaîne de caractères

Les valeurs encapsulées dans des guillemets simples (`''`) ou doubles (`""`) seront lues comme des chaînes de caractères lors de l'importation.

### Données importées comme attribut personnalisé

Si une donnée utilisateur par défaut (telle que `email` ou `first_name`) est importée en tant qu'attribut personnalisé, vérifiez la casse et l'espacement de votre fichier CSV. Par exemple, `First_name` serait importé comme attribut personnalisé, alors que `first_name` serait correctement importé dans le champ « prénom » sur le profil d’un utilisateur.

### Plusieurs types de données

Braze s’attend à ce que toutes les valeurs d’une colonne soient du même type de données. Les valeurs qui ne correspondent pas au type de données de leur attribut entraîneront des erreurs de segmentation.

En outre, le fait de commencer un attribut de nombre par zéro posera des problèmes, car les nombres commençant par des zéros sont considérés comme des chaînes de caractères. Lorsque Braze convertit cette chaîne de caractères, elle peut être traitée comme une valeur octale (qui utilise les chiffres de zéro à sept), ce qui signifie qu'elle sera convertie en sa valeur décimale correspondante. Par exemple, si la valeur du fichier CSV est 0130, le profil Braze affichera 88. Pour éviter ce problème, utilisez des attributs avec des chaînes de caractères. Toutefois, ce type de données n'est pas disponible dans la comparaison des numéros de segmentation.

### Types d'attribut par défaut

Certains attributs par défaut peuvent n'accepter que certaines valeurs comme valables pour les mises à jour de l'utilisateur. Pour plus d'informations, reportez-vous à la section [Construire votre CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Les espaces de fin et les différences de capitalisation peuvent entraîner l'interprétation d'une valeur comme non valide. Par exemple, dans le fichier CSV suivant, seul l'utilisateur de la première ligne (`brazetest1`) verra ses statuts d'e-mail et de push mis à jour avec succès car les valeurs acceptées sont `unsubscribed`, `subscribed`, et `opted_in`. 

```
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### Le bouton "Select CSV File" ne fonctionne pas

Il y a plusieurs raisons pour lesquelles le bouton **Sélectionner un fichier CSV** peut ne pas fonctionner :

- **Bloqueur de pop-up :** Cela peut empêcher l'affichage de la page. Confirmez que votre navigateur autorise les fenêtres pop-up sur le site web du tableau de bord de Braze. 
- **Navigateur obsolète :** Assurez-vous que votre navigateur est à jour ; si ce n'est pas le cas, mettez-le à jour.
- **Processus de base :** Fermez toutes les instances de votre navigateur, puis redémarrez votre ordinateur.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[5]: {% image_buster /assets/img/csvfilter.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
[erreurs] :#common-errors
[modèle] : {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[template_alias]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
