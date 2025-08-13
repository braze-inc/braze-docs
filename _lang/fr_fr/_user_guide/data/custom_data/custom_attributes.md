---
nav_title: Attributs personnalisés
article_title: Attributs personnalisés
page_order: 10
page_type: reference
description: "Cette page décrit les attributs personnalisés et explique les différents types de données d'attributs personnalisés."
search_rank: 1
---

# [![Cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Attributs personnalisés

> Cette page traite des attributs personnalisés, qui regroupent les caractéristiques uniques de vos utilisateurs. Les attributs personnalisés sont les plus appropriés pour stocker des attributs sur vos utilisateurs, ou des informations sur les actions à faible valeur dans votre application. 

Lorsqu'ils sont stockés dans Braze, les attributs personnalisés peuvent être utilisés pour créer des segments d'audience et personnaliser l'envoi de messages à l'aide de Liquid. Gardez à l'esprit que nous ne stockons pas d'informations sur les séries temporelles pour les attributs personnalisés. Vous ne pourrez donc pas obtenir de graphiques basés sur ces attributs, comme c'est le cas pour les événements personnalisés.

## Gestion des attributs personnalisés

Pour créer et gérer des attributs personnalisés dans le tableau de bord, sélectionnez **Paramètres des données** > **Attributs personnalisés**. 

![Quatre attributs personnalisés qui sont des booléens.]({% image_buster /assets/img/export_custom_attributes.png %})

La colonne **Dernière mise à jour** indique la dernière fois que l'attribut personnalisé a été modifié, par exemple lorsqu'il a été défini comme liste de blocage ou actif pour la dernière fois.

{% alert important %}
Pour un ciblage correct des messages, assurez-vous que le type de données de votre attribut personnalisé correspond à l'attribut personnalisé réel.
{% endalert %}

Cette page vous permet d'afficher, de gérer, de créer ou de mettre sur liste de blocage des attributs personnalisés existants. Sélectionnez le menu à côté d'un attribut personnalisé pour les actions suivantes :

### Mise en liste de blocage

Les attributs personnalisés peuvent être bloqués individuellement dans le menu d'actions, ou jusqu'à 100 attributs peuvent être sélectionnés et bloqués en bloc. Si vous bloquez un attribut personnalisé, aucune donnée ne sera collectée concernant cet attribut, les données existantes seront indisponibles à moins d'être réactivées, et les attributs bloqués n'apparaîtront pas dans les filtres ou les graphiques. En outre, si l'attribut est actuellement référencé par des filtres ou des déclencheurs dans d'autres zones du tableau de bord de Braze, une fenêtre modale d'avertissement s'affiche expliquant que toutes les instances des filtres ou des déclencheurs qui y font référence seront supprimées et archivées.

### Marquage en tant qu'information personnelle identifiable (PII)

Les administrateurs peuvent également créer des attributs personnalisés et les marquer comme IIP à partir de cette page. Ces attributs ne seront visibles que par les administrateurs et les utilisateurs du tableau de bord disposant de l'autorisation "Voir les attributs personnalisés marqués comme IIP".

### Ajout de descriptions

Vous pouvez ajouter une description à un attribut personnalisé après sa création si vous disposez de l' [autorisation utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases`. Modifiez l'attribut personnalisé et saisissez ce que vous voulez, par exemple une note destinée à votre équipe.

### Ajout d'étiquettes

Vous pouvez ajouter des tags à un attribut personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) « Gérer les événements et les attributs, les achats ». Les étiquettes peuvent ensuite être utilisées pour filtrer la liste des attributs. 

### Suppression des attributs personnalisés

Vous pouvez supprimer les attributs personnalisés des profils utilisateurs de deux manières :

* Sélectionnez le nom de l'attribut personnalisé à supprimer lors d'une [étape de mise à jour de l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes).
* Définissez la valeur `null` dans votre requête API à l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

### Consultation des rapports d'utilisation

Le rapport d'utilisation répertorie toutes les toiles, campagnes et segments utilisant un attribut personnalisé spécifique. Cette liste ne comprend pas les utilisations de Liquid. 

Vous pouvez consulter jusqu'à 100 rapports d'utilisation à la fois en cochant les cases situées à côté des attributs personnalisés respectifs, puis en sélectionnant **Afficher le rapport d'utilisation.**

### Exporter des données

Pour exporter la liste des attributs personnalisés sous forme de fichier CSV, sélectionnez **Exporter tout en** haut de la page. Le fichier CSV sera généré et un lien de téléchargement vous sera envoyé par e-mail.

## Définition des attributs personnalisés

La liste suivante énumère les méthodes utilisées pour définir des attributs personnalisés sur les différentes plateformes.

{% details Développer la documentation par plateforme %}

- [Android et FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## Stockage des attributs personnalisé

Toutes les données stockées sur le **profil utilisateur**, y compris les données d'attribut personnalisé, sont conservées indéfiniment tant que chaque profil est [actif]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Types de données des attributs personnalisés

Les attributs personnalisés sont des outils extraordinairement flexibles qui permettent un ciblage exceptionnel.

Les types de données suivants peuvent être stockés en tant qu’attributs personnalisés :

- [Booléens](#booleans)
- [Chiffres](#numbers)
- [Chaînes de caractères](#strings)
- [Tableaux](#arrays)
- [Date](#time)
- [Objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)
- [Tableaux d’objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)

### Booléens (vrai/faux) {#booleans}

Les attributs booléens sont utiles pour stocker des données binaires simples sur vos utilisateurs, comme le statut d’abonnement. Vous pouvez trouver des utilisateurs qui ont explicitement une variable définie sur Vrai ou Faux, en plus des personnes qui n’ont pas encore d’enregistrement pour cet attribut.

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si la valeur booléenne **est** soit vraie, soit fausse, soit vraie ou non définie, soit fausse ou non définie | **EST**  | **VRAI**, **FAUX**, **VRAI OU NON ENREGISTRÉ**, ou **FAUX OU NON ENREGISTRÉ** | Si ce filtre spécifie `coffee_drinker`, un utilisateur correspondra à ce filtre dans les circonstances suivantes : <br> {::nomarkdown}<ul><li>Si ce filtre est <code>true</code> et l'utilisateur a la valeur <code>coffee_drinker</code></li><li>Si ce filtre est <code>false</code> et l'utilisateur n'a pas la valeur <code>coffee_drinker</code></li><li>Si ce filtre est <code>true or not set</code> et l'utilisateur a la valeur <code>coffee_drinker</code> ou aucune valeur</li><li>Si ce filtre est <code>false or not set</code> et l'utilisateur n'a pas <code>coffee_drinker</code> ou toute valeur</li></ul>{:/} |
| Vérifier si la valeur booléenne **existe** dans le profil d'un utilisateur et si elle n'est pas nulle. | **N'EST PAS VIDE**  | **S.O.** | Si ce filtre spécifie `coffee_drinker` et qu'un utilisateur possède une valeur pour l'attribut `coffee_drinker`, l'utilisateur correspondra à ce filtre. | 
| Vérifier si la valeur booléenne **n'existe pas** dans le profil de l'utilisateur ou si elle est nulle. | **EST BLANC**  | **S.O.** | Si ce filtre spécifie `coffee_drinker`et qu'un utilisateur n'a pas l'attribut `coffee_drinker` ou que la valeur de `coffee_drinker` est nulle, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Nombre {#numbers}

Les attributs numériques comprennent les [entiers](https://en.wikipedia.org/wiki/Integer) et les [flottants](https://en.wikipedia.org/wiki/Floating-point_arithmetic), et ont une grande variété de cas d'utilisation. Les attributs personnalisés basés sur un un nombre incrémental sont utiles pour stocker le nombre de fois qu’une action ou un événement donné s’est produit sans que ce soit comptabilisé dans votre limite de données. Les numéros standard ont toutes sortes d’utilisations, comme l’enregistrement :

- Pointure
- Tour de taille
- Nombre de fois qu’un utilisateur a regardé une certaine caractéristique ou catégorie de produit

{% alert tip %}
L’argent dépensé ne doit pas être enregistré via cette méthode. Il vaut mieux l’enregistrer via nos [méthodes d’achat](#purchase-revenue-tracking).
{% endalert %}

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut numérique **est exactement** un **nombre**| **EXACTEMENT** | **NOMBRE** | Si ce filtre spécifie `10` et qu'un profil utilisateur a la valeur `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **n'est pas égal à** un **nombre**| **N'EST PAS ÉGAL À** | **NOMBRE** | Si ce filtre spécifie `10` et qu'un profil utilisateur n'a pas la valeur `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **est plus qu'** un **nombre**| **PLUS DE** | **NOMBRE** | Si ce filtre spécifie `10` et qu'un profil utilisateur a une valeur supérieure à `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **est inférieur à** un **nombre**| **MOINS DE** | **NOMBRE** | Si ce filtre spécifie `10` et qu'un profil utilisateur a une valeur inférieure à `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **existe** dans le profil d'un utilisateur et s'il n'est pas nul. | **N'EST PAS VIDE** | **S.O.** | Si un profil utilisateur contient l'attribut numérique spécifié, quelle que soit sa valeur, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **n'existe pas** dans le profil d'un utilisateur ou s'il est nul. | **EST BLANC** | **S.O.** | Si un profil utilisateur ne contient pas l'attribut numérique spécifié ou si la valeur de l'attribut est nulle, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Détails des attributs numériques

- Les filtres « Exactement 0 » et « Inférieur à » incluent les utilisateurs avec des champs NULL
  - Pour exclure les utilisateurs sans valeur pour les attributs personnalisés, vous devez inclure le filtre **is not blank.** 

### Chaînes de caractères (caractères alphanumériques) {#strings}

Les attributs au format string sont utiles pour stocker les entrées utilisateur, comme une marque préférée, un numéro de téléphone ou la dernière recherche dans votre application. Les attributs au format string peuvent avoir jusqu’à 255 caractères.

Prenez en compte le fait que, si vous saisissez des valeurs comprenant des espaces entre, avant ou après les mots, Braze cherchera à trouver ces espaces.

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut string **correspond exactement à** une chaîne de caractères saisie| **ÉGAL À** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse | Si ce filtre spécifie `book` et qu'un profil utilisateur possède un attribut de chaîne de caractères pour `last_item_purchased` qui contient `book`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut chaîne de caractères **correspond partiellement à** une chaîne saisie **OU** Expression régulière | **CORRESPOND À L’EXPRESSION RÉGULIÈRE** | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE** <br>Non sensible à la casse ; maximum de 32 764 caractères | 
| Vérifier si l'attribut de chaîne de caractères **ne correspond pas partiellement** à une chaîne de caractères **OU** à une expression régulière saisie | **NE CORRESPOND PAS À L'EXPRESSION RÉGULIÈRE** \* | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE**<br>Non sensible à la casse ; maximum de 32 764 caractères |
| Vérifier si l'attribut string **ne correspond pas à** une chaîne de caractères saisie| **N'EST PAS ÉGAL À** | **CHAÎNE DE CARACTÈRES**<br>Non sensible à la casse  | Si ce filtre spécifie `book` et qu'un profil utilisateur possède une chaîne de caractères pour `last_item_purchased` qui ne contient pas `book`, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut string **existe** dans le profil d'un utilisateur et s'il ne s'agit pas d'une chaîne de caractères vide. | **N'EST PAS VIDE** | **S.O.** | Si ce filtre spécifie `favorite_genre` et qu'un profil utilisateur possède l'attribut `favorite_genre`, l'utilisateur correspondra à ce filtre quelle que soit la valeur de son attribut. Par exemple, l'utilisateur peut avoir `sci-fi`, `romance` ou une autre valeur.|
| Vérifier si l'attribut chaîne de caractères **n'existe pas** dans le profil d'un utilisateur | **VIDE** | **S.O.** | Si ce filtre spécifie `favorite_genre` et qu'un profil utilisateur ne possède pas l'attribut `favorite_genre`, l'utilisateur correspondra à ce filtre.|
| Vérifier si la chaîne correspond exactement à l'**une des** chaînes de caractères saisies. | **EST-CE QUE L'UN OU L'AUTRE DES** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs chaînes de caractères autorisées (256 au maximum) | Si ce filtre spécifie `book`, `bookmark`, et `reading light`, et qu'un profil utilisateur contient au moins une de ces chaînes de caractères, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut chaîne **ne correspond pas exactement à l'une des** chaînes de caractères saisies. | **N'EST AUCUN DE** |**CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs chaînes de caractères autorisées (256 au maximum) | Si ce filtre spécifie `book`, `bookmark`, et `reading light`, et qu'un profil utilisateur ne contient aucune de ces chaînes de caractères, l'utilisateur correspondra au filtre.|
| Vérifier si l'attribut string **correspond partiellement à l'une des** chaînes de caractères saisies. | **CONTIENT L'UN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs chaînes de caractères autorisées (256 au maximum) | Si ce filtre spécifie `gold` et qu'un profil utilisateur contient `gold` dans une chaîne de caractères quelconque, comme `gold_tier` ou `former_gold_tier`, l'utilisateur correspondra au filtre. |
| Vérifier si l'attribut chaîne **ne correspond pas partiellement à l'une des** chaînes de caractères saisies. | **NE CONTIENT AUCUN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs chaînes de caractères autorisées (256 au maximum) | Si ce filtre spécifie `gold` et qu'un profil utilisateur ne contient pas `gold` dans une chaîne de caractères, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Une chaîne de caractères de date telle que "12-1-2021" ou "12/1/2021" sera convertie en objet datetime et traitée comme un [attribut time]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% alert important %}
Lorsque vous effectuez une segmentation à l'aide du filtre **DOES NOT MATCH REGEX**, vous devez déjà disposer d'un attribut personnalisé avec une valeur attribuée dans ce profil utilisateur. Braze suggère d’utiliser la logique « OR » (OU) pour vérifier si un attribut personnalisé est vide pour s’assurer que les utilisateurs sont correctement ciblés.
{% endalert %}

### Arrays {#arrays}

Les attributs de tableau sont appropriés pour stocker les listes d’informations associées à vos utilisateurs. Par exemple, le stockage en tableau des 100 derniers morceaux de contenu qu’un utilisateur a regardé permettrait une segmentation spécifique basée sur les intérêts.

Par défaut, la longueur d'un tableau pour un attribut est de 500 éléments maximum. Par exemple, si vous envoyez un attribut tel que "Films regardés" et qu'il est défini sur 500, lorsqu'un utilisateur regarde le 501e film, le premier film sera supprimé du tableau et le film le plus récent sera ajouté.

Notez que si vous saisissez des valeurs avec des espaces entre, avant ou après les mots, Braze vérifiera également la présence de ces mêmes espaces.

{% alert note %}
L'option permettant d'augmenter la longueur maximale n'est pas disponible si l'attribut est configuré pour détecter automatiquement le type de données ; le type de données doit être défini comme étant un tableau.
{% endalert %}

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l’attribut du tableau **inclut une valeur qui correspond exactement** à une valeur saisie| **INCLUT LA VALEUR** | **CHAÎNE DE CARACTÈRES** | Si ce filtre spécifie `sci-fi` et qu'un profil utilisateur a la valeur `sci-fi`, l'utilisateur correspondra à ce filtre.|
| Vérifier si l’attribut du tableau **n’inclut pas une valeur qui correspond exactement** à une valeur saisie| **NE COMPREND PAS DE VALEUR** | **CHAÎNE DE CARACTÈRES** | Si ce filtre spécifie `sci-fi` et qu'un profil utilisateur n'a pas la valeur `sci-fi`, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut du tableau **contient une valeur qui correspond partiellement** à une valeur **OU** à une expression régulière saisie | **CORRESPOND À L’EXPRESSION RÉGULIÈRE** | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE**<br>Maximum de 32 764 caractères | |
| Vérifier si l'attribut tableau **a une valeur** ou n'est pas vide | **A UNE VALEUR** | **S.O.** | Si ce filtre spécifie `favorite_genres` et qu'un profil utilisateur contient `favorite_genres` avec n'importe quelle valeur, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut du tableau **est vide** ou n'existe pas | **EST VIDE** | **S.O.** | Si ce filtre spécifie `favorite_genres` et qu'un profil utilisateur ne contient pas `favorite_genres` ou contient `favorite_genres` mais n'a pas de valeurs, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut du tableau **contient une valeur qui correspond exactement** à l’une des valeurs saisies | **COMPREND L'UN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur possède n'importe quelle combinaison de `sci-fi`, `fantasy`, ou `romance`, y compris un seul d'entre eux (par exemple uniquement `sci-fi`). Un utilisateur peut avoir `horror` ou une autre valeur dans sa chaîne de caractères s'il a également `sci-fi`, `fantasy` et `romance`.|
| Vérifier si l'attribut du tableau **ne contient pas de valeur correspondant exactement à l'une des** valeurs saisies. | **NE COMPREND AUCUN DES ÉLÉMENTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur ne comporte aucune combinaison de `sci-fi`, `fantasy` ou `romance`, l'utilisateur correspondra à ce filtre. L'utilisateur peut avoir `horror` ou une autre valeur s'il n'a pas `sci-fi`, `fantasy` ou `romance`.|
| Vérifier si l'attribut du tableau **contient une valeur qui correspond partiellement à l'une** des valeurs saisies | **CONTIENNENT L'UN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `gold` et qu'un tableau chaînes de profil utilisateur contient `gold` dans au moins une chaîne de caractères, l'utilisateur correspondra à ce filtre. Ceci inclut les valeurs de chaînes de caractères telles que `gold_tier`, `former_gold_tier` et autres.|
| Vérifier si l'attribut du tableau **ne contient pas de valeur correspondant partiellement à l'une des** valeurs saisies. | **NE CONTIENNENT AUCUN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `gold` et que le tableau d'un profil utilisateur ne contient pas `gold` dans une chaîne de caractères, l'utilisateur correspondra à ce filtre. Cela signifie que les utilisateurs ayant des valeurs de chaînes de caractères telles que `gold_tier` et `former_gold_tier` ne correspondront pas à ce filtre.|
| Vérifier si l'attribut du tableau **comprend toutes les** valeurs saisies. | **INCLUT TOUS LES ÉLÉMENTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur possède toutes ces valeurs, l'utilisateur correspondra à ce filtre. L'utilisateur peut également avoir `horror` ou d'autres valeurs et correspondre à ce filtre.|
| Vérifier si l'attribut du tableau **n'inclut pas toutes** les valeurs saisies | **N’EST PAS TOUS LES ÉLÉMENTS PARMI** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum)|  Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur ne possède pas toutes ces valeurs, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Pour en savoir plus sur l'utilisation des expressions régulières (regex), consultez ces ressources :
- [Expressions régulières compatibles avec Perl (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Braze et les expressions régulières]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Débogueur et testeur d'expressions régulières](https://www.regex101.com/)
- [Tutoriel sur les expressions régulières](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Date {#time}

Les attributs de temps sont utiles pour stocker la dernière fois qu’une action spécifique a été prise, car ils vous permettent d’envoyer des contenus spécifiques  de ré-engagement dans vos envois de messages client.

Les filtres temporels utilisant des dates relatives (par exemple, il y a plus d'un jour, il y a moins de deux jours) mesurent 1 jour comme 24 heures. Toute campagne que vous exécutez à l’aide de ces filtres inclura tous les utilisateurs par incréments de 24 heures. Par exemple, `last used app more than 1 day ago` va capturer tous les utilisateurs qui ont « utilisé l’application plus de 24 heures » à partir du lancement exact de la campagne. Il en va de même pour les campagnes définies avec des plages de dates plus longues. Ainsi, cinq jours après l’activation signifie les 120 heures précédentes.

Par exemple, pour créer un segment qui cible les utilisateurs avec un attribut temporel entre 24 et 48 heures dans le futur, appliquez les filtres `in more than 1 day in the future` et `in less than 2 days in the future`.

{% alert warning %}
La dernière date à laquelle un événement personnalisé ou événement d’achat s’est produit est automatiquement enregistrée et ne doit pas être enregistrée de nouveau avec un attribut de temps personnalisé.
{% endalert %}

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut time **est antérieur à** une **date sélectionnée**| **AVANT** | **SÉLECTEUR DE DATE DU CALENDRIER** | Si ce filtre spécifie `2024-01-31` et que le profil d'un utilisateur a une date antérieure à `2024-1-31`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut time **est postérieur à** une **date sélectionnée**| **APRÈS** | **SÉLECTEUR DE DATE DU CALENDRIER** | Si ce filtre spécifie `2024-01-31` et que le profil d'un utilisateur a une date postérieure à `2024-1-31`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut time **date de** **plus de X** jours. | **PLUS DE** | **NOMBRE DE JOURS ÉCOULÉS** | Si ce filtre spécifie `7` et qu’un profil utilisateur date d’il y a plus de sept jours, l'utilisateur correspondra à ce filtre. |
| Vérifier si l’attribut de temps est **antérieur** à **il y a moins de X jours**| **MOINS DE** | **NOMBRE DE JOURS ÉCOULÉS** | Si ce filtre spécifie `7` et que le profil utilisateur est daté de moins de sept jours, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut temporel se **situe dans** **plus de X** jours dans le futur | **DANS PLUS DE** | **NOMBRE DE JOURS À VENIR** | Si ce filtre spécifie `7` et que le profil utilisateur a une date qui se situe plus de sept jours dans le futur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut temporel est **inférieur à un nombre X de** **jours dans le futur** | **EN MOINS DE** | **NOMBRE DE JOURS À VENIR**  | Si ce filtre spécifie `7` et que le profil utilisateur a une date qui se situe moins de sept jours dans le futur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut time **existe** dans le profil d'un utilisateur et s'il n'est pas null. | **N'EST PAS VIDE** | **S.O.** | Si ce filtre spécifie un attribut temporel qui se trouve dans un profil utilisateur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut time **n'existe pas** dans le profil d'un utilisateur ou s'il est nul. | **EST BLANC** | **S.O.** | Si ce filtre spécifie un attribut temporel qui ne figure pas dans un profil utilisateur, l'utilisateur correspondra à ce filtre. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Détails des attributs temporels

- Jour de l’événement récurrent
  - Si vous utilisez le filtre « Jour d’événement récurrent », vous êtes invité à sélectionner le « Jour civil de l’événement récurrent » si vous sélectionnez `IS LESS THAN` ou `IS MORE THAN`, la date actuelle sera comptée pour ce filtre de segmentation.
  - Par exemple, si le 10 mars 2020, vous avez défini la date de l’attribut sur `LESS THAN ... March 10, 2020`, les attributs seront pris en compte pour les jours jusqu’au 10 mars 2020 inclus. 
- Il y a moins de X jours : Le filtre « Il y a moins de X jours » inclut des dates entre il y a X jours et la date/heure actuelle.
- Moins de X jours dans le futur : Inclut les dates entre la date/heure actuelle et les X jours à l’avenir.

### Objets

Vous pouvez utiliser des attributs personnalisés imbriqués pour envoyer des objets en tant que type de données pour des attributs personnalisés. Pour plus d'informations, reportez-vous à la section [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/).

### Tableaux d’objets

Utilisez un tableau d’objets pour regrouper des attributs associés. Pour plus de détails, reportez-vous à notre article sur les [tableaux d'objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/).

### Opérateurs consolidés

Nous avons consolidé la liste des opérateurs disponibles pour les filtres d'attributs, les filtres d'attributs personnalisés et les filtres d'attributs personnalisés imbriqués. Si vous avez des filtres existants utilisant ces opérateurs, ils seront automatiquement mis à jour pour utiliser les nouveaux opérateurs.

| Type de données | Ancien opérateur | Nouvel opérateur | Valeur |
| --- | --- | --- | --- |
| Chaîne de caractères | est égal à | est l’une des valeurs parmi | Au moins une valeur |
| Chaîne de caractères | n’est pas égal à | n’est aucun des éléments | Au moins une valeur |
| Tableau | inclut la valeur | comprend un des éléments | Au moins une valeur |
| Tableau | n’inclut pas la valeur | ne comprend aucun des éléments | Au moins une valeur |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Suivi des achats et des revenus {#purchase-revenue-tracking}

L’utilisation de nos méthodes d’achat pour enregistrer les achats dans l’application établit la Valeur à vie (LTV) pour chaque profil utilisateur individuel. Ces données sont consultables sur notre page de revenus dans les séries temporelles.

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si le nombre total de dollars dépensés **est supérieur à** un **nombre**| **SUPÉRIEUR À** | **NOMBRE** | Si ce filtre spécifie `500` et qu'un profil utilisateur a une valeur supérieure à `500`, l'utilisateur correspondra à ce filtre. |
| Vérifier si le nombre total de dollars dépensés **est inférieur à** un **nombre**.| **MOINS DE** | **NOMBRE** | Si ce filtre spécifie `500` et que le profil utilisateur a une valeur inférieure à `500`, l'utilisateur correspondra à ce filtre.|
| Vérifier si le nombre total de dollars dépensés **est exactement** un **nombre**| **EXACTEMENT** | **NOMBRE** | Si ce filtre spécifie `500` et qu'un profil utilisateur a la valeur `500`, l'utilisateur correspondra à ce filtre. |
| Vérifiez si le dernier achat a eu lieu **après la date X** | **APRÈS** | **DATE** | Si ce filtre spécifie `2024/31/1` et que le dernier achat d'un utilisateur a eu lieu après `2024/31/1`, l'utilisateur correspondra à ce filtre.|
| Vérifiez si le dernier achat a eu lieu **avant la date X** | **AVANT** | **DATE** | Si ce filtre spécifie `2024/31/1` et que le dernier achat d'un utilisateur est antérieur à `2024/31/1`, l'utilisateur correspondra à ce filtre.|
| Vérifier si l’achat a été effectué pour la dernière fois **il y a plus de X jours** | **PLUS DE** | **DATE** | Si ce filtre spécifie `7` et que le dernier achat d'un utilisateur remonte à plus de sept jours à partir d'aujourd'hui, l'utilisateur correspondra à ce filtre.|
| Vérifier si l’achat a été effectué pour la dernière fois **il y a moins de X jours** | **MOINS DE** | **DATE** |  Si ce filtre spécifie `7` et que le dernier achat d'un utilisateur date de moins de sept jours à partir d'aujourd'hui, l'utilisateur correspondra à ce filtre.|
| Vérifiez si l'achat a eu lieu **plus de X (Max = 50) fois.** | **PLUS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |  Si ce filtre spécifie `7` fois et `21` jours, et qu'un utilisateur a effectué plus de sept achats au cours des 21 derniers jours, l'utilisateur correspondra à ce filtre.|
| Vérifiez si l'achat a eu lieu **moins de X (Max = 50) fois.** | **MOINS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** | Si ce filtre spécifie `7` fois et `21` jours, et qu'un utilisateur a effectué moins de sept achats au cours des 21 derniers jours, l'utilisateur correspondra à ce filtre.|
| Vérifiez si l'achat a eu lieu **exactement X (Max = 50) fois.** | **EXACTEMENT** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** | Si ce filtre spécifie `7` fois et `21` jours, et qu'un utilisateur a effectué sept achats au cours des 21 derniers jours, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Si vous souhaitez segmenter le nombre de fois qu'un achat spécifique a été effectué, vous devez également enregistrer cet achat individuellement en tant qu'[attribut personnalisé incrémentiel.]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes)
{% endalert %}

Vous pouvez modifier le type de données de votre attribut personnalisé, mais vous devez être conscient des conséquences d'un [changement de type de données]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/).

