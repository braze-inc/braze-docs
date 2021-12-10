---
nav_title: Import de l'utilisateur
article_title: Import de l'utilisateur
page_order: 4
page_type: Référence
description: "Cet article de référence traite de la façon d'importer des utilisateurs dans votre tableau de bord Braze et des meilleures pratiques."
---

# Importation de l'utilisateur

Il y a deux approches pour importer des données clients dans votre tableau de bord Braze : REST API et CSV.

{% alert important %}
Braze ne nettoie pas les données HTML pendant le temps d'ingestion. Cela signifie que les balises de script doivent être supprimées pour toutes les données d'importation destinées à la personnalisation du Web. Passez à [le stripping de données HTML](#html-data-stripping) ci-dessous pour en savoir plus.
{% endalert %}

## API REST

Vous pouvez utiliser le point de terminaison de l'API REST de Braze pour enregistrer des événements personnalisés, des attributs utilisateur et des achats pour les utilisateurs. Voir [le suivi utilisateur du point de terminaison][12] pour plus d'informations.

## CSV

Vous pouvez également télécharger et mettre à jour les profils d'utilisateurs via des fichiers CSV à partir de la page **Import des utilisateurs**. Cette fonctionnalité prend en charge l'enregistrement et la mise à jour des attributs utilisateur tels que le prénom et le courriel, en plus des attributs personnalisés tels que la taille des chaussures. Il y a deux façons différentes d'approcher une importation CSV, selon que vos utilisateurs ont ou non un `external_id`.

{% alert tip %}
Besoin de télécharger un fichier CSV supérieur à 100MB? Contactez-nous à smb-product@braze.com et nous pourrons peut-être vous aider!
{% endalert %}

### Importation avec ID externe

Lors de l'importation de vos données clients, vous devrez spécifier l'identifiant unique de chaque client, également connu sous le nom de `external_id`. Avant de commencer votre importation CSV, il est important de comprendre de la part de votre équipe d'ingénierie comment les utilisateurs seront identifiés en Brésil. Généralement, ce serait un ID de base de données utilisé en interne. Cela devrait s'aligner sur la façon dont les utilisateurs seront identifiés par le Braze SDK sur mobile et sur le web, et assure que chaque client aura un profil utilisateur unique à Braze sur tous ses appareils. En savoir plus sur le cycle de vie de [Braze sur le profil utilisateur][13].

Lorsque vous fournissez un `external_id` dans votre importation, Braze mettra à jour tout utilisateur existant avec le même `external_id` ou créera un utilisateur nouvellement identifié avec cet ensemble `external_id` si on n'est pas trouvé.

<i class="fas fa-file-download"></i> Téléchargement : \[Modèle d'importation CSV\]\[template\]

### Importation avec l'alias de l'utilisateur

Pour cibler les utilisateurs qui n'ont pas d' `external_id`, vous pouvez importer une liste d'utilisateurs avec des alias d'utilisateur. Un alias sert d'identifiant d'utilisateur unique alternatif, et peut être utile si vous essayez de commercialiser des utilisateurs anonymes qui n'ont pas créé de compte avec votre application.

Si vous téléchargez ou mettez à jour les profils d'utilisateurs qui ne sont que des pseudonymes, vous devez avoir les deux colonnes suivantes dans votre CSV :

- `user_alias_name`: Un identifiant utilisateur unique ; une alternative au `external_id`.
- `user_alias_label`: Une étiquette commune par laquelle regrouper les alias utilisateurs.

!\[User Alias Import CSV Example\]\[8\]{: style="max-width:80%" }

Lorsque vous fournissez un `user_alias_name` et `user_alias_label` dans votre importation, Braze mettra à jour tout utilisateur existant avec le même `user_alias_name` ou créera un utilisateur nouvellement identifié avec ce `user_alias_name` défini si on n'est pas trouvé.

{% alert important %}
Vous ne pouvez pas utiliser une importation CSV pour mettre à jour un utilisateur existant avec un `user_alias_name` s'il a déjà un `external_id`. À la place, cela va créer un nouveau profil utilisateur avec le `user_alias_name` associé. Pour associer un utilisateur seul à un `external_id`, utilisez le point de terminaison [Identifier les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

<i class="fas fa-file-download"></i> Téléchargement : \[Modèle d'importation d'alias CSV\]\[template_alias\]

### Construire votre CSV

Il existe plusieurs types de données en Brésil. Lors de l'importation ou de la mise à jour des profils d'utilisateurs via CSV, vous pouvez créer ou mettre à jour les attributs par défaut ou les attributs personnalisés.

- Les attributs d'utilisateurs par défaut sont des clés réservées en Brésil. Par exemple, `first_name` ou `email`.
- Les attributs personnalisés sont personnalisés pour votre entreprise. Par exemple, une application de réservation de voyages peut avoir un attribut personnalisé appelé `last_destination_searched`.

{% alert important %}
Lors de l'importation de données clients, les en-têtes de colonnes que vous utilisez doivent correspondre exactement à l'orthographe et à la majuscule des attributs utilisateur par défaut. Sinon, Braze créera automatiquement un attribut personnalisé sur le profil de cet utilisateur.
{% endalert %}

Braze accepte les données des utilisateurs au format CSV standard à partir de fichiers jusqu'à 100 Mo. Reportez-vous aux sections ci-dessus pour les modèles CSV.

### Considérations du point de données

Chaque élément de données client importé via CSV écrasera la valeur existante sur les profils des utilisateurs et comptera comme un point de données. sauf pour les identifiants externes et les valeurs vides.

- Les identifiants externes téléchargés via CSV ne consommeront pas les points de données. Si vous téléversez un CSV vers le segment des utilisateurs existants de Braze en téléversant uniquement des identifiants externes, cela peut être fait sans consommer de points de données. Si vous devez ajouter des données supplémentaires comme l'e-mail de l'utilisateur ou le numéro de téléphone dans votre importation, qui écraserait les données utilisateur existantes, en consommant vos points de données.
- Les valeurs vides n'écraseront pas les valeurs existantes sur le profil de l'utilisateur, et vous n'avez pas besoin d'inclure tous les attributs utilisateur existants dans votre fichier CSV.

{% alert important %}
Définir `langue` ou `pays` sur un utilisateur via une importation ou une API CSV empêchera Braze de capturer automatiquement ces informations via le SDK.
{% endalert %}

### En-têtes de colonne de données utilisateur par défaut

| FICHIER DE PROFIL D'UTILISATEUR                                     | Type de données      | INFORMATIONS                                                                                                                                                                                                                                                      | Requis                          |
| ------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `id externe`                                                        | Chaîne de caractères | Un identifiant d'utilisateur unique pour votre client.                                                                                                                                                                                                            | Oui, voir la note suivante      |
| `Alias de l'utilisateur`                                            | Chaîne de caractères | Un identifiant utilisateur unique pour les utilisateurs anonymes. Une alternative au `external_id`.                                                                                                                                                               | Non, voir la note suivante      |
| `Alias utilisateur`                                                 | Chaîne de caractères | Une étiquette commune par laquelle grouper les alias des utilisateurs.                                                                                                                                                                                            | Oui si `user_alias` est utilisé |
| `prénom`                                                            | Chaîne de caractères | Le prénom de vos utilisateurs comme ils l'ont indiqué (par exemple `Jane`).                                                                                                                                                                                       | Non                             |
| `nom_de famille`                                                    | Chaîne de caractères | Le nom de famille de vos utilisateurs comme ils l'ont indiqué (par exemple `Doe`).                                                                                                                                                                                | Non                             |
| `Email`                                                             | Chaîne de caractères | L'e-mail de vos utilisateurs comme ils l'ont indiqué (par exemple `jane.doe@braze.com`).                                                                                                                                                                          | Non                             |
| `Pays`                                                              | Chaîne de caractères | Les codes pays doivent être passés à Braze dans le standard ISO-3166-1 alpha-2 (par exemple `Go`).                                                                                                                                                                | Non                             |
| `chien`                                                             | Chaîne de caractères | Doit être passé au format « AAAA-MM-JJ » (par exemple `1980-12-21`). Cela importera la date de naissance de votre utilisateur et vous permettra de cibler les utilisateurs dont l'anniversaire est "aujourd'hui".                                                 | Non                             |
| `Sexe`                                                              | Chaîne de caractères | “M”, “F”, “O” (autre), “N” (non applicable), “P” (préfère ne pas le dire), ou nil (inconnu).                                                                                                                                                                      | Non                             |
| `ville_domicile`                                                    | Chaîne de caractères | La ville natale de vos utilisateurs comme ils l'ont indiqué (par exemple `Londres`).                                                                                                                                                                              | Non                             |
| `Langue`                                                            | Chaîne de caractères | La langue doit être passée à Braze dans le standard ISO-639-1 (par exemple `en`). <br>[Liste des langues acceptées][1]                                                                                                                                      | Non                             |
| `Téléphone`                                                         | Chaîne de caractères | Un numéro de téléphone tel qu'indiqué par vos utilisateurs, au format `E.164` (par exemple `+442071838750`). <br> Référez-vous à [numéros de téléphone d'utilisateur][2] pour obtenir des conseils de mise en forme.                                        | Non                             |
| `Email_open_tracking_désactivé`                                     | Boolean              | vrai ou faux accepté.  Définir à vrai pour désactiver le pixel de suivi ouvert d'être ajouté à tous les e-mails futurs envoyés à cet utilisateur.                                                                                                                 | Non                             |
| `Email_click_tracking_désactivé`                                    | Boolean              | vrai ou faux accepté.  Définir à vrai pour désactiver le suivi des clics pour tous les liens dans un e-mail futur, envoyé à cet utilisateur.                                                                                                                      | Non                             |
| `Inscription par e-mail`                                            | Chaîne de caractères | Les valeurs disponibles sont `opted_in` (explicitement enregistrées pour recevoir des messages), `désabonné` (explicitement exclu des messages électroniques) et `abonné` (ni pris part ni sortant).                                                              | Non                             |
| `Poussez vous abonner`                                              | Chaîne de caractères | Les valeurs disponibles sont `opted_in` (explicitement enregistrées pour recevoir des messages push), `désabonné` (explicitement exclu des messages push), et `souscrit` (ni pris en compte ni sortant).                                                          | Non                             |
| `fuseau horaire`                                                    | Chaîne de caractères | Le fuseau horaire doit être passé à Braze dans le même format que la base de données du fuseau horaire IANA (par ex. `Amérique/New_York` ou `Heure de l'Est (États-Unis & Canada)`).                                                                          | Non                             |
| `date_of_first_session` <br><br> `date_of_last_session` | Chaîne de caractères | Peut être passé dans l'un des formats ISO8601 suivants : <br> - "AAAA-MM-DD" <br> - "AAAA-MM-DDTHH:MM:SS+00:00" <br> - "AAAA-MM-DTHH:MM:SSZ" <br> - "AAAA-MM-DDTHH:MM:SS" <br> - "AAAA-MM-DDTHH:MM:SS" (e. . `2019-11-20T18:38:57`) | Non                             |
| `url de l'image`                                                    | Chaîne de caractères | Une URL d'une image.                                                                                                                                                                                                                                              | Non                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


{% alert note %}
Alors que `external_id` lui-même n'est pas obligatoire, vous **devez** inclure l'un de ces champs :
- `external_id` - Un identifiant utilisateur unique pour votre client <br> - OU -
- `braze_id` - Un identifiant utilisateur unique tiré pour les utilisateurs de Braze existant <br> - OU -
- `user_alias` - Un identifiant utilisateur unique pour un utilisateur anonyme
{% endalert %}


### Importation de données personnalisées via CSV

Tous les en-têtes qui ne correspondent pas exactement aux données utilisateur par défaut créeront un attribut personnalisé au Brésil.

Les types de données suivants sont acceptés dans l'importation des utilisateurs:
- Datetime (Doit être stocké au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601))
- Booléen (TRUE/FALSE)
- Nombre (nombre entier ou flottant sans espace ou virgule, les nombres décimaux doivent utiliser un point « .» comme séparateur décimal)
- Chaîne de caractères (sans virgules)
- Vide (Les valeurs vides n'écraseront pas les valeurs existantes sur le profil de l'utilisateur, et vous n'avez pas besoin d'inclure tous les attributs utilisateur existants dans votre fichier CSV.)

{% alert important %}
Les tableaux, les jetons push et les types d'événements personnalisés ne sont pas pris en charge dans l'importation des utilisateurs. Surtout pour les tableaux, les virgules dans votre fichier CSV seront interprétées comme un séparateur de colonnes, donc toute virgule dans les valeurs provoquera des erreurs lors de l'analyse du fichier.

Pour télécharger ce type de valeurs, veuillez utiliser le [point de terminaison de suivi utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-track-endpoint).
{% endalert %}

### Importation d'un CSV

Pour importer votre fichier CSV, accédez à la page **User Import** sous la section Utilisateurs sur la barre d'outils de gauche. Dans la zone de texte inférieure, **Imports récents**, il y aura une table qui répertorie jusqu'à vingt de vos dernières importations, leurs noms de fichiers, le nombre de lignes dans le fichier, le nombre de lignes importées avec succès, le nombre total de lignes dans chaque fichier et l'état de chaque importation.

La boîte supérieure, **Import CSV**, contiendra des directions d'importation et un bouton pour commencer votre importation. Cliquez sur **Sélectionnez le fichier CSV** et sélectionnez votre fichier d'intérêt, puis cliquez sur **Démarrer le téléchargement**. Braze téléversera votre fichier et vérifiera les en-têtes de colonne ainsi que les types de données de chaque colonne.

Pour télécharger un modèle CSV, reportez-vous aux sections [Importer avec un ID externe](#import-with-external-id) ou [Importer avec un alias d'utilisateur](#import-with-user-alias) sur cette page.

{% alert important %}
Les importations CSV sont sensibles à la casse. Cela signifie que les lettres majuscules dans les importations CSV écriront le champ en tant qu'attribut personnalisé au lieu d'un attribut standard. Par exemple, "email" est correct, mais "Email" serait écrit comme un attribut personnalisé.
{% endalert %}

!\[Import CSV\]\[3\]

Une fois le téléchargement terminé, vous verrez une fenêtre modale avec un tableau prévisualisant le contenu de votre fichier. Toutes les informations de ce tableau sont basées sur les valeurs dans les quelques lignes supérieures de votre fichier CSV. Pour les en-têtes de colonnes, les attributs par défaut seront écrits en texte normal, tandis que les attributs personnalisés seront en italique et auront leur type indiqué entre parenthèses. Il y aura également un bref résumé de votre dossier en haut de la pop-up.

Vous pouvez importer plus d'un CSV en même temps. Les importations CSV seront exécutées en même temps et, en tant que telles, l'ordre des mises à jour n'est pas garanti en série. Si vous avez besoin que les importations CSV s'exécutent les unes après les autres, vous devez attendre que l'importation CSV soit terminée avant d'en télécharger une seconde.

Si Braze remarque quelque chose de malformé dans votre fichier pendant le téléchargement, des erreurs seront affichées au-dessus du résumé. Un fichier peut être importé avec des erreurs, mais une importation ne peut pas être annulée ou annulée une fois commencée. Examinez l'aperçu, et si vous trouvez des erreurs, annulez l'importation et modifiez votre fichier. Il est important d'examiner le fichier CSV complet avant le téléchargement, car Braze ne scanne pas chaque ligne du fichier d'entrée pour l'aperçu. Cela signifie que des erreurs peuvent exister que Braze ne attrape pas lors de la génération de cet aperçu.

Les lignes mal formées et les lignes manquantes d'un ID externe ne seront pas importées. Toutes les autres erreurs peuvent être importées, mais peuvent interférer avec le filtrage lors de la création d'un segment. Pour plus d'informations, passez à [Dépannage](#troubleshooting) ci-dessous.

{% alert warning %}
Les erreurs sont basées uniquement sur le type de données et la structure du fichier. Par exemple, une adresse email mal formatée serait toujours importée car elle peut toujours être analysée comme une chaîne.
{% endalert %}

!\[Erreurs d'importation CSV\]\[6\]

Lorsque vous êtes satisfait du téléchargement, commencez l'importation. Le pop-up se fermera et l'importation commencera en arrière-plan. Vous pouvez suivre sa progression sur la page **Import utilisateur** qui sera actualisée toutes les 5 secondes, ou à l'appui du bouton de rafraîchissement dans la zone **Imports Récents**.

Sous **Lignes traitées**, vous verrez la progression de l'importation; le statut passera à Terminer une fois terminé. Vous pouvez toujours utiliser le reste du tableau de bord Braze pendant l'importation, et vous recevrez des notifications lorsque l'importation commencera et se terminera.

Si le processus d'importation se heurte à une erreur, une icône d'avertissement jaune s'affichera à côté du nombre total de lignes dans le fichier. Vous pouvez survoler l'icône pour voir les détails sur les raisons pour lesquelles certaines lignes ont échoué. Une fois l'import terminé, toutes les données seront ajoutées aux profils existants, ou de nouveaux profils seront créés.

## Segmentation

L'importation des utilisateurs crée et met à jour les profils des utilisateurs, et peut également être utilisée pour créer des segments. Pour créer un segment, sélectionnez **Créer un segment à partir de ce CSV**.

!\[Utilisateurs de Segmenting d'importation CSV\]\[7\]{: style="max-width:80%;"}

Vous pouvez définir le nom du segment ou accepter le nom par défaut, qui est le nom de votre fichier. Les fichiers qui ont été utilisés pour créer un segment auront un lien pour afficher le segment une fois l'importation terminée.

Le filtre utilisé pour créer le segment sélectionne les utilisateurs qui ont été créés ou mis à jour dans une importation sélectionnée et est disponible avec tous les autres filtres de la page d'édition du segment.

## Suppression des données HTML

Braze ne nettoie pas les données HTML pendant le temps d'ingestion. Lors de l'importation de données en Brésil, spécifiquement destinées à la personnalisation de l'utilisation dans un navigateur Web, assurez-vous qu'il est supprimé du HTML, JavaScript ou tout autre tag de script qui pourrait être utilisé de manière malveillante lors du rendu dans un navigateur Web.

Alternativement, pour HTML, vous pouvez utiliser les filtres Liquid de Braze (`strip_html`) pour échapper au texte rendu. Par exemple :

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{ "Avez-vous <em>vous</em> lu <strong>Ulysses</strong>? &#124; strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Avez-vous lu Ulysse ?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Dépannage {#troubleshooting}

### Lignes manquantes

Il y a quelques raisons pour lesquelles le nombre d'utilisateurs importés peut ne pas correspondre au nombre total de lignes dans votre fichier CSV :

- **ID externe dupliqué :** S'il y a des colonnes d'ID externes dupliquées, peut causer des lignes mal formées ou non importées, même si les lignes sont correctement formatées. Dans certains cas, cela peut ne pas signaler une erreur spécifique. Vérifiez s'il y a des identifiants externes en double dans votre CSV. Si c'est le cas, supprimez les doublons et essayez de télécharger à nouveau.
- **Caractères accentués :** Votre CSV peut avoir des noms ou des attributs qui incluent des accents. Assurez-vous que votre fichier est encodé en UTF-8 pour éviter tout problème.

### Ligne mal formée

Il doit y avoir une ligne d'en-tête afin d'importer correctement les données. Chaque ligne doit avoir le même nombre de cellules que la ligne d'en-tête. Les lignes dont la longueur a plus ou moins de valeurs que la ligne d'en-tête seront exclues de l'importation. Les virgules dans une valeur seront interprétées comme un séparateur et peuvent conduire à ce que cette erreur soit levée. De plus, toutes les données doivent être encodées en UTF-8.

### Types de données multiples

Braze attend que chaque valeur d'une colonne soit du même type de données. Les valeurs qui ne correspondent pas au type de données de leur attribut provoqueront des erreurs dans la segmentation.

### Dates mal formatées

Les dates non au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ne seront pas lues comme dates à l'importation.

### Citation de chaîne

Les valeurs encapsulées en guillemets simples (‘’) ou doubles (« ») seront lues comme des chaînes à l'importation.

### Données importées en tant qu'attribut personnalisé

Si vous voyez un morceau de données utilisateur par défaut (par ex. `email` ou `first_name`) importés en tant qu'attribut personnalisé, vérifiez la casse et l'espacement de votre fichier CSV. Par exemple, `Prénom` serait importé en tant qu'attribut personnalisé, alors que `first_name` serait correctement importé dans le champ « prénom» du profil d’un utilisateur.

{% alert important %}
Braze va bannir ou bloquer les utilisateurs avec plus de 5 millions de sessions (« utilisateurs factices ») et ne va plus ingérer leurs événements SDK. Pour plus d'informations, reportez-vous à [Blocage de spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).
{% endalert %}
[3]: {% image_buster /assets/img/importcsv.png %} [6]: {% image_buster /assets/img/csv-errors. ng %} [7]: {% image_buster /assets/img/segment-imported-users.png %} [8]: {% image_buster /assets/img_archive/user_alias_import_1. ng %} [template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %} [template_alias]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[12]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-track-endpoint
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
