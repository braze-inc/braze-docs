---
nav_title: Attributs personnalisés
article_title: Attributs personnalisés
page_order: 10
page_type: reference
description: "Cette page décrit les attributs personnalisés et explique les différents types de données d'attributs personnalisés."
search_rank: 1
---

# ![cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"} Attributs personnalisés

> Cette page traite des attributs personnalisés, qui regroupent les caractéristiques uniques de vos utilisateurs. Les attributs personnalisés sont idéaux pour stocker des attributs sur vos utilisateurs ou des informations sur des actions de faible valeur au sein de votre application. 

Lorsqu'ils sont stockés dans Braze, les attributs personnalisés peuvent être utilisés pour créer des segments d'audience et personnaliser l'envoi de messages à l'aide de Liquid. Gardez à l'esprit que nous ne stockons pas d'informations sur les séries temporelles pour les attributs personnalisés. Vous ne pourrez donc pas obtenir de graphiques basés sur ces attributs, comme c'est le cas pour les événements personnalisés.

## Gérer les attributs personnalisés

Pour créer et gérer des attributs personnalisés dans le tableau de bord, allez dans **Paramètres des données** > Attributs personnalisés. 

Quatre attributs personnalisés qui sont des booléens.]({% image_buster /assets/img/export_custom_attributes.png %})

La colonne **Dernière mise à jour** indique la dernière fois que l'attribut personnalisé a été modifié, par exemple lorsqu'il a été défini comme liste de blocage ou actif pour la dernière fois.

{% alert important %}
Pour un ciblage correct des messages, assurez-vous que le type de données de votre attribut personnalisé correspond à l'attribut personnalisé réel.
{% endalert %}

Cette page vous permet d'afficher, de gérer, de créer ou de mettre sur liste de blocage des attributs personnalisés existants. Sélectionnez le menu à côté d'un attribut personnalisé pour les actions suivantes :

### Liste de blocage

Les attributs personnalisés peuvent être bloqués individuellement dans le menu d'actions, ou jusqu'à 100 attributs peuvent être sélectionnés et bloqués en bloc. Si vous bloquez un attribut personnalisé, aucune donnée ne sera collectée concernant cet attribut, les données existantes seront indisponibles à moins d'être réactivées, et les attributs bloqués n'apparaîtront pas dans les filtres ou les graphiques. En outre, si l'attribut est actuellement référencé par des filtres ou des déclencheurs dans d'autres zones du tableau de bord de Braze, une fenêtre modale d'avertissement s'affiche expliquant que toutes les instances des filtres ou des déclencheurs qui y font référence seront supprimées et archivées.

### Marquage en tant qu'information personnelle identifiable (PII)

Les administrateurs peuvent également créer des attributs personnalisés et les marquer comme IIP à partir de cette page. Ces attributs ne seront visibles que par les administrateurs et les utilisateurs du tableau de bord disposant de l'autorisation "Voir les attributs personnalisés marqués comme IIP".

### Ajout de descriptions

Vous pouvez ajouter une description à un attribut personnalisé après sa création si vous disposez de l' [autorisation utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases`. Modifiez l'attribut personnalisé et entrez ce que vous voulez, par exemple une note destinée à votre équipe.

### Ajout d'étiquettes

Vous pouvez ajouter des tags à un attribut personnalisé après sa création si vous disposez de l'autorisation utilisateur "Gérer les événements et les attributs, les achats". Les étiquettes peuvent ensuite être utilisées pour filtrer la liste des attributs. 

### Suppression des attributs personnalisés

Vous pouvez supprimer les attributs personnalisés des profils utilisateurs de deux manières :

* Sélectionnez le nom de l'attribut personnalisé à supprimer lors d'une [étape de mise à jour de l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes).
* Définissez la valeur `null` dans votre requête API vers l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

### Consultation des rapports d'utilisation

Le rapport d'utilisation répertorie toutes les toiles, campagnes et segments utilisant un attribut personnalisé spécifique. Cette liste ne comprend pas les utilisations du liquide. 

Vous pouvez consulter jusqu'à 100 rapports d'utilisation à la fois en cochant les cases situées à côté des attributs personnalisés respectifs, puis en sélectionnant **Afficher le rapport d'utilisation.**

### Exporter des données

Pour exporter la liste des attributs personnalisés sous forme de fichier CSV, sélectionnez **Exporter tout en** haut de la page. Le fichier CSV sera généré et un lien de téléchargement vous sera envoyé par e-mail.

## Définition d'attributs personnalisés

Vous trouverez ci-dessous la liste des méthodes utilisées pour définir les attributs personnalisés sur les différentes plateformes.

{% details Expand for documentation by platform %}

- [Android et FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## Stockage d'attributs personnalisés

Toutes les données stockées sur le **profil utilisateur**, y compris les données d'attribut personnalisé, sont conservées indéfiniment tant que chaque profil est [actif]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Types de données d'attributs personnalisés

Les attributs personnalisés sont des outils extraordinairement flexibles qui permettent un excellent ciblage.

Les types de données suivants peuvent être stockés en tant qu'attributs personnalisés :

- [Booléens](#booleans)
- [Chiffres](#numbers)
- [Chaînes de caractères](#strings)
- [Tableaux](#arrays)
- [L'heure](#time)
- [Objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)
- [Tableaux d'objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)

### Booléens (vrai/faux) {#booleans}

Les attributs booléens sont utiles pour stocker des données binaires simples sur vos utilisateurs, comme les statuts d'abonnement. Vous pouvez trouver des utilisateurs qui ont explicitement défini une variable à une valeur vraie ou fausse, en plus de ceux qui n'ont pas encore d'enregistrement de cet attribut.

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si la valeur booléenne **est** soit vraie, soit fausse, soit vraie ou non définie, soit fausse ou non définie. | **IS**  | **VRAI**, **FAUX**, **VRAI OU NON RÉGLER**, ou **FAUX OU NON RÉGLER** | Si ce filtre spécifie `coffee_drinker`, un utilisateur correspondra à ce filtre dans les circonstances suivantes : <br> {::nomarkdown}<ul><li>Si ce filtre est <code>vrai</code> et que l'utilisateur a la valeur <code>coffee_drinker</code></li><li>Si ce filtre est <code>faux</code> et que l'utilisateur n'a pas la valeur <code>coffee_drinker</code></li><li>Si ce filtre est <code>vrai ou non défini</code> et que l'utilisateur a la valeur <code>coffee_drinker</code> ou aucune valeur</li><li>Si ce filtre est <code>faux ou n'est pas défini</code> et que l'utilisateur n'a pas de <code>coffee_drinker</code> ou une valeur quelconque</li></ul>{:/} |
| Vérifier si la valeur booléenne **existe** dans le profil d'un utilisateur et si elle n'est pas nulle. | **N'EST PAS EN BLANC**  | **N/A** | Si ce filtre spécifie `coffee_drinker` et qu'un utilisateur possède une valeur pour l'attribut `coffee_drinker`, l'utilisateur correspondra à ce filtre. | 
| Vérifier si la valeur booléenne n **'existe pas** dans le profil de l'utilisateur ou si elle est nulle. | **EST BLANC**  | **N/A** | Si ce filtre spécifie `coffee_drinker`et qu'un utilisateur n'a pas l'attribut `coffee_drinker` ou que la valeur de `coffee_drinker` est nulle, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Chiffres {#numbers}

Les attributs numériques comprennent les [nombres entiers](https://en.wikipedia.org/wiki/Integer) et les [flottants](https://en.wikipedia.org/wiki/Floating-point_arithmetic), et ont une grande variété de cas d'utilisation. Les attributs personnalisés de type nombre incrémentiel sont utiles pour enregistrer le nombre de fois qu'une action ou un événement donné s'est produit sans que cela ne soit pris en compte dans votre plafond de données. Les numéros standard ont toutes sortes d'utilisations, comme l'enregistrement :

- Taille des chaussures
- Tour de taille
- Nombre de fois qu'un utilisateur a consulté une certaine fonctionnalité ou catégorie de produits

{% alert tip %}
L'argent dépensé ne doit pas être enregistré par cette méthode. Elle doit plutôt être enregistrée par le biais de nos [méthodes d'achat](#purchase-revenue-tracking).
{% endalert %}

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut numérique **est exactement** un **nombre**| **EXACTEMENT** | **NUMÉRO** | Si ce filtre spécifie `10` et qu'un profil utilisateur a la valeur `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **n'est pas égal à** un **nombre**| **N'EST PAS ÉGALE** | **NUMÉRO** | Si ce filtre spécifie `10` et qu'un profil utilisateur n'a pas la valeur `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **est plus qu'** un **nombre**| **PLUS QUE** | **NUMÉRO** | Si ce filtre spécifie `10` et qu'un profil utilisateur a une valeur supérieure à `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **est inférieur à** un **nombre**| **MOINS DE** | **NUMÉRO** | Si ce filtre spécifie `10` et que le profil utilisateur a une valeur inférieure à `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **existe** dans le profil d'un utilisateur et s'il n'est pas nul. | **N'EST PAS EN BLANC** | **N/A** | Si un profil utilisateur contient l'attribut numérique spécifié, quelle que soit sa valeur, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique n **'existe pas** dans le profil d'un utilisateur ou s'il est nul. | **EST BLANC** | **N/A** | Si un profil utilisateur ne contient pas l'attribut numérique spécifié ou si la valeur de l'attribut est nulle, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Détails de l'attribut du numéro

- Les filtres "Exactly 0" et "Less Than" incluent les utilisateurs ayant des champs NULL.
  - Pour exclure les utilisateurs sans valeur pour les attributs personnalisés, vous devez inclure le filtre **is not blank.** 

### Chaînes de caractères (caractères alphanumériques) {#strings}

Les attributs de type chaîne sont utiles pour stocker les données saisies par l'utilisateur, telles qu'une marque préférée, un numéro de téléphone ou la dernière chaîne de caractères utilisée pour une recherche dans votre application. Les attributs de type chaîne de caractères peuvent comporter jusqu'à 255 caractères.

Notez que si vous saisissez des valeurs avec des espaces entre, avant ou après les mots, Braze vérifiera également la présence de ces mêmes espaces.

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut string **correspond exactement à** une chaîne de caractères saisie| **ÉGAUX** | **CHAÎNE DE CARACTÈRES**<br>Respect des majuscules et des minuscules | Si ce filtre spécifie `book` et qu'un profil utilisateur possède un attribut de chaîne de caractères pour `last_item_purchased` qui contient `book`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut chaîne de caractères **correspond partiellement à** une chaîne saisie **OU** Expression régulière | **MATCHES REGEX** | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE** <br>Non sensible à la casse ; maximum de 32 764 caractères | 
| Vérifier si l'attribut chaîne de caractères **ne correspond pas partiellement à** une chaîne saisie **OU** Expression régulière | **NE CORRESPOND PAS À L'EXPRESSION RÉGULIÈRE** \* | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE**<br>Non sensible à la casse ; maximum de 32 764 caractères |
| Vérifier si l'attribut string **ne correspond pas à** une chaîne de caractères saisie| **N'EST PAS ÉGALE** | **CHAÎNE DE CARACTÈRES**<br>Non sensible à la casse  | Si ce filtre spécifie `book` et qu'un profil utilisateur possède une chaîne de caractères pour `last_item_purchased` qui ne contient pas `book`, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut string **existe** dans le profil d'un utilisateur et s'il ne s'agit pas d'une chaîne de caractères vide. | **N'EST PAS EN BLANC** | **N/A** | Si ce filtre spécifie `favorite_genre` et qu'un profil utilisateur possède l'attribut `favorite_genre`, l'utilisateur correspondra à ce filtre quelle que soit la valeur de son attribut. Par exemple, l'utilisateur peut avoir `sci-fi`, `romance`, ou une autre valeur.|
| Vérifier si l'attribut chaîne de caractères **n'existe pas** dans le profil d'un utilisateur | **BLANC** | **N/A** | Si ce filtre spécifie `favorite_genre` et qu'un profil utilisateur ne possède pas l'attribut `favorite_genre`, l'utilisateur correspondra à ce filtre.|
| Vérifier si la chaîne correspond exactement à l'**une des** chaînes de caractères saisies. | **EST-CE QUE L'UN OU L'AUTRE DES** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs chaînes de caractères autorisées (256 au maximum) | Si ce filtre spécifie `book`, `bookmark`, et `reading light`, et qu'un profil utilisateur contient au moins une de ces chaînes de caractères, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut chaîne **ne correspond pas exactement à l'une des** chaînes de caractères saisies. | **N'EST PAS** |**CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs chaînes de caractères autorisées (256 au maximum) | Si ce filtre spécifie `book`, `bookmark`, et `reading light`, et qu'un profil utilisateur ne contient aucune de ces chaînes de caractères, l'utilisateur correspondra au filtre.|
| Vérifier si l'attribut string **correspond partiellement à l'une des** chaînes de caractères saisies. | **CONTIENT L'UN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs chaînes de caractères autorisées (256 au maximum) | Si ce filtre spécifie `gold` et qu'un profil utilisateur contient `gold` dans une chaîne de caractères quelconque, telle que `gold_tier` ou `former_gold_tier`, l'utilisateur répondra au filtre. |
| Vérifier si l'attribut chaîne **ne correspond pas partiellement à l'une des** chaînes de caractères saisies. | **NE CONTIENT AUCUN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs chaînes de caractères autorisées (256 au maximum) | Si ce filtre spécifie `gold` et qu'un profil utilisateur ne contient pas `gold` dans une chaîne de caractères, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Une chaîne de caractères de date telle que "12-1-2021" ou "12/1/2021" sera convertie en objet datetime et traitée comme un [attribut time]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% alert important %}
Lorsque vous effectuez une segmentation à l'aide du filtre **DOES NOT MATCH REGEX**, vous devez déjà disposer d'un attribut personnalisé avec une valeur attribuée dans ce profil utilisateur. Braze suggère d'utiliser la logique "OU" pour vérifier si un attribut personnalisé est vide afin de s'assurer que les utilisateurs sont correctement ciblés.
{% endalert %}

### Tableaux {#arrays}

Les attributs de type tableau permettent de stocker des listes d'informations relatives à vos utilisateurs. Par exemple, le stockage des 100 derniers contenus regardés par un utilisateur dans un tableau permettrait une segmentation spécifique des intérêts.

Par défaut, la longueur d'un tableau pour un attribut est de 500 éléments maximum. Par exemple, si vous envoyez un attribut tel que "Films regardés" et qu'il est défini sur 500, lorsqu'un utilisateur regarde le 501e film, le premier film sera supprimé du tableau et le film le plus récent sera ajouté.

Notez que si vous saisissez des valeurs avec des espaces entre, avant ou après les mots, Braze vérifiera également la présence de ces mêmes espaces.

{% alert note %}
L'option permettant d'augmenter la longueur maximale n'est pas disponible si l'attribut est configuré pour détecter automatiquement le type de données ; le type de données doit être défini comme étant un tableau.
{% endalert %}

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut du tableau **contient une valeur qui correspond exactement à la** valeur saisie.| **INCLUT LA VALEUR** | **CHAÎNE DE CARACTÈRES** | Si ce filtre spécifie `sci-fi` et qu'un profil utilisateur a la valeur `sci-fi`, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut du tableau **ne contient pas une valeur correspondant exactement à la** valeur saisie.| **NE COMPREND PAS DE VALEUR** | **CHAÎNE DE CARACTÈRES** | Si ce filtre spécifie `sci-fi` et qu'un profil utilisateur n'a pas la valeur `sci-fi`, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut du tableau **contient une valeur qui correspond partiellement à** une valeur saisie **OU** Expression régulière | **MATCHES REGEX** | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE**<br>Maximum de 32 764 caractères | |
| Vérifier si l'attribut tableau **a une valeur** ou n'est pas vide | **A UNE VALEUR** | **N/A** | Si ce filtre spécifie `favorite_genres` et qu'un profil utilisateur contient `favorite_genres` avec n'importe quelle valeur, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut du tableau **est vide** ou n'existe pas | **EST VIDE** | **N/A** | Si ce filtre spécifie `favorite_genres` et qu'un profil utilisateur ne contient pas `favorite_genres` ou contient `favorite_genres` mais n'a pas de valeurs, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut du tableau **contient une valeur qui correspond exactement à l'une des** valeurs saisies. | **COMPREND L'UN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur comporte n'importe quelle combinaison de `sci-fi`, `fantasy` ou `romance`, y compris un seul d'entre eux (par exemple, uniquement `sci-fi`). Un utilisateur peut avoir `horror` ou une autre valeur dans sa chaîne de caractères s'il a également `sci-fi`, `fantasy` et `romance`.|
| Vérifier si l'attribut du tableau **ne contient pas de valeur correspondant exactement à l'une des** valeurs saisies. | **NE COMPREND AUCUN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur ne comporte aucune combinaison de `sci-fi`, `fantasy` ou `romance`, l'utilisateur correspondra à ce filtre. L'utilisateur peut avoir `horror` ou une autre valeur s'il n'a pas `sci-fi`, `fantasy` ou `romance`.|
| Vérifier si l'attribut du tableau **contient une valeur qui correspond partiellement à l'une des** valeurs saisies. | **CONTIENNENT L'UN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `gold` et qu'un tableau chaînes de profil utilisateur contient `gold` dans au moins une chaîne de caractères, l'utilisateur correspondra à ce filtre. Cela inclut les valeurs de chaînes de caractères telles que `gold_tier`, `former_gold_tier`, et autres.|
| Vérifier si l'attribut du tableau **ne contient pas de valeur correspondant partiellement à l'une des** valeurs saisies. | **NE CONTIENNENT AUCUN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `gold` et que le tableau d'un profil utilisateur ne contient pas `gold` dans une chaîne de caractères, l'utilisateur correspondra à ce filtre. Cela signifie que les utilisateurs ayant des valeurs de chaînes de caractères telles que `gold_tier` et `former_gold_tier` ne correspondront pas à ce filtre.|
| Vérifier si l'attribut du tableau **comprend toutes les** valeurs saisies. | **EST TOUT DE** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur possède toutes ces valeurs, l'utilisateur correspondra à ce filtre. L'utilisateur peut également avoir `horror` ou d'autres valeurs et correspondre à ce filtre.|
| Vérifier si l'attribut du tableau **n'inclut pas toutes les** valeurs saisies | **TOUT N'EST-IL PAS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum)|  Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur ne possède pas toutes ces valeurs, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Pour en savoir plus sur l'utilisation des expressions régulières (regex), consultez ces ressources :
- [Expressions régulières compatibles avec Perl (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Expression régulière avec Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Débogueur et testeur d'expressions régulières](https://www.regex101.com/)
- [Tutoriel sur les expressions régulières](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### L'heure {#time}

Les attributs temporels sont utiles pour stocker la dernière fois qu'une action spécifique a été effectuée, afin que vous puissiez offrir à vos utilisateurs des messages de réengagement spécifiques au contenu.

Les filtres temporels utilisant des dates relatives (par exemple, il y a plus d'un jour, il y a moins de deux jours) mesurent 1 jour comme 24 heures. Toute campagne menée à l'aide de ces filtres inclura tous les utilisateurs par tranches de 24 heures. Par exemple, `last used app more than 1 day ago` enregistrera tous les utilisateurs qui ont "utilisé l'application pour la dernière fois plus de 24 heures" à partir du moment exact où la campagne est lancée. Il en va de même pour les campagnes dont la période de validité est plus longue. Ainsi, cinq jours après l'activation correspondront aux 120 heures précédentes.

Par exemple, pour créer un segment qui cible les utilisateurs dont l'attribut temporel se situe entre 24 et 48 heures dans le futur, appliquez les filtres `in more than 1 day in the future` et `in less than 2 days in the future`.

{% alert warning %}
La dernière date à laquelle un événement personnalisé ou un événement d'achat s'est produit est automatiquement enregistrée et ne doit pas être enregistrée à nouveau via un attribut de temps personnalisé.
{% endalert %}

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut time **est antérieur à** une **date sélectionnée**| **AVANT** | **SÉLECTEUR DE DATE DU CALENDRIER** | Si ce filtre spécifie `2024-01-31` et que le profil d'un utilisateur a une date antérieure à `2024-1-31`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut time **est postérieur à** une **date sélectionnée**| **APRÈS** | **SÉLECTEUR DE DATE DU CALENDRIER** | Si ce filtre spécifie `2024-01-31` et que le profil d'un utilisateur a une date postérieure à `2024-1-31`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut time **date de plus** **de X** **jours.** | **PLUS QUE** | **NOMBRE DE JOURS ÉCOULÉS** | Si ce filtre spécifie `7` et que le profil utilisateur est daté de plus de sept jours, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut time est **inférieur à X** **jours.**| **MOINS DE** | **NOMBRE DE JOURS ÉCOULÉS** | Si ce filtre spécifie `7` et que le profil utilisateur est daté de moins de sept jours, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut temporel se **situe dans plus** **de X** **jours dans le futur** | **DANS PLUS DE** | **NOMBRE DE JOURS À VENIR** | Si ce filtre spécifie `7` et que le profil utilisateur a une date qui se situe plus de sept jours dans le futur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut temporel est **inférieur à un nombre X de** **jours dans le futur** | **EN MOINS DE** | **NOMBRE DE JOURS À VENIR**  | Si ce filtre spécifie `7` et que le profil utilisateur a une date qui se situe moins de sept jours dans le futur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut time **existe** dans le profil d'un utilisateur et s'il n'est pas null. | **N'EST PAS EN BLANC** | **N/A** | Si ce filtre spécifie un attribut temporel qui se trouve dans un profil utilisateur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut time n **'existe pas** dans le profil d'un utilisateur ou s'il est nul. | **EST BLANC** | **N/A** | Si ce filtre spécifie un attribut temporel qui ne figure pas dans un profil utilisateur, l'utilisateur correspondra à ce filtre. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Détails de l'attribut temporel

- Jour de l'événement récurrent
  - Lorsque vous utilisez le filtre "Jour de l'événement récurrent" et que vous êtes invité à sélectionner le "Jour du calendrier de l'événement récurrent", si vous sélectionnez `IS LESS THAN` ou `IS MORE THAN`, la date du jour sera prise en compte pour ce filtre de segmentation.
  - Par exemple, si le 10 mars 2020, vous avez sélectionné la date de l'attribut à `LESS THAN ... March 10, 2020`, les attributs seront pris en compte pour les jours allant jusqu'au 10 mars 2020 inclus. 
- Il y a moins de X jours : Le filtre "Il y a moins de X jours" inclut les dates comprises entre X jours et la date/heure actuelle.
- Moins de X jours dans le futur : Inclut les dates comprises entre la date/heure actuelle et X jours dans le futur.

### Objets

Vous pouvez utiliser des attributs personnalisés imbriqués pour envoyer des objets comme type de données pour les attributs personnalisés. Pour plus d'informations, reportez-vous à la section [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/).

### Tableaux d'objets

Utilisez un tableau d'objets pour regrouper des attributs connexes. Pour plus de détails, reportez-vous à notre article sur les [tableaux d'objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/).

### Opérateurs consolidés

Nous avons consolidé la liste des opérateurs disponibles pour les filtres d'attributs, les filtres d'attributs personnalisés et les filtres d'attributs personnalisés imbriqués. Si vous avez des filtres existants utilisant ces opérateurs, ils seront automatiquement mis à jour pour utiliser les nouveaux opérateurs.

| Type de données | Ancien opérateur | Nouvel opérateur | Valeur |
| --- | --- | --- | --- |
| Chaîne de caractères | équivaut | est l'un des éléments suivants | Au moins 1 valeur |
| Chaîne de caractères | n'est pas égal à | n'est pas | Au moins 1 valeur |
| Réseau | comprend la valeur | comprend l'un des éléments suivants | Au moins 1 valeur |
| Réseau | ne comprend pas de valeur | ne comprend aucun des éléments suivants | Au moins 1 valeur |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Suivi des achats et des chiffre d'affaires {#purchase-revenue-tracking}

L'utilisation de nos méthodes d'achat pour enregistrer les achats in-app établit la valeur vie (LTV) pour chaque profil utilisateur individuel. Ces données peuvent être consultées dans notre page sur les chiffres d'affaires sous forme de séries chronologiques.

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si le nombre total de dollars dépensés **est supérieur à** un **nombre.**| **PLUS GRAND QUE** | **NUMÉRO** | Si ce filtre spécifie `500` et qu'un profil utilisateur a une valeur supérieure à `500`, l'utilisateur correspondra à ce filtre. |
| Vérifier si le nombre total de dollars dépensés **est inférieur à** un **nombre.**| **MOINS DE** | **NUMÉRO** | Si ce filtre spécifie `500` et que le profil utilisateur a une valeur inférieure à `500`, l'utilisateur correspondra à ce filtre.|
| Vérifier si le nombre total de dollars dépensés **est exactement** un **nombre**| **EXACTEMENT** | **NUMÉRO** | Si ce filtre spécifie `500` et qu'un profil utilisateur a la valeur `500`, l'utilisateur correspondra à ce filtre. |
| Vérifiez si le dernier achat a eu lieu **après la date X** | **APRÈS** | **TEMPS** | Si ce filtre spécifie `2024/31/1` et que le dernier achat d'un utilisateur a eu lieu après `2024/31/1`, l'utilisateur correspondra à ce filtre.|
| Vérifiez si le dernier achat a eu lieu **avant la date X** | **AVANT** | **TEMPS** | Si ce filtre spécifie `2024/31/1` et que le dernier achat d'un utilisateur est antérieur à `2024/31/1`, l'utilisateur correspondra à ce filtre.|
| Vérifiez si l'achat a eu lieu **il y a plus de X jours.** | **PLUS QUE** | **TEMPS** | Si ce filtre spécifie `7` et que le dernier achat d'un utilisateur remonte à plus de sept jours à partir d'aujourd'hui, l'utilisateur correspondra à ce filtre.|
| Vérifiez si l'achat a eu lieu **il y a moins de X jours.** | **MOINS DE** | **TEMPS** |  Si ce filtre spécifie `7` et que le dernier achat d'un utilisateur date de moins de sept jours à partir d'aujourd'hui, l'utilisateur correspondra à ce filtre.|
| Vérifiez si l'achat a eu lieu **plus de X (Max = 50) fois.** | **PLUS QUE** | au cours des **Y** derniers **jours (Y = 1,3,7,14,21,30)** |  Si ce filtre spécifie `7` fois et `21` jours, et qu'un utilisateur a effectué plus de sept achats au cours des 21 derniers jours, l'utilisateur correspondra à ce filtre.|
| Vérifiez si l'achat a eu lieu **moins de X (Max = 50) fois.** | **MOINS DE** | au cours des **Y** derniers **jours (Y = 1,3,7,14,21,30)** | Si ce filtre spécifie `7` fois et `21` jours, et qu'un utilisateur a effectué moins de sept achats au cours des 21 derniers jours, l'utilisateur correspondra à ce filtre.|
| Vérifiez si l'achat a eu lieu **exactement X (Max = 50) fois.** | **EXACTEMENT** | au cours des **Y** derniers **jours (Y = 1,3,7,14,21,30)** | Si ce filtre spécifie `7` fois et `21` jours, et qu'un utilisateur a effectué sept achats au cours des 21 derniers jours, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Si vous souhaitez segmenter le nombre de fois qu'un achat spécifique a été effectué, vous devez également enregistrer cet achat individuellement en tant qu'[attribut personnalisé incrémentiel]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes).
{% endalert %}

Vous pouvez modifier le type de données de votre attribut personnalisé, mais vous devez être conscient des conséquences d'un [changement de type de données]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/).

