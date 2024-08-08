---
nav_title: Attributs personnalisés
article_title: Attributs personnalisés
page_order: 10
page_type: reference
description: "Cet article de référence décrit les attributs personnalisés et explique les différents types de données pour les attributs personnalisés."
search_rank: 1
---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Attributs personnalisés

> Les attributs personnalisés sont une collection de caractéristiques uniques de vos utilisateurs. Les attributs personnalisés sont les plus appropriés pour stocker des attributs sur vos utilisateurs, ou des informations sur les actions à faible valeur dans votre application. 

Lorsqu’elles sont stockées dans Braze, ces caractéristiques peuvent être utilisées pour segmenter l’audience et personnaliser les envois de messages avec Liquid. Gardez à l’esprit que nous ne stockons pas d’informations sur les séries temporelles pour les attributs personnalisés. Vous ne pourrez donc pas voir de graphiques basés sur elles comme c’est le cas pour les événements personnalisés.

## Gestion des attributs personnalisés

Pour créer et gérer des attributs personnalisés dans le tableau de bord, allez sur **Manage Settings (Gérer les paramètres)** > **Custom Attributes (Attributs personnalisés)**. Depuis cette page, vous pouvez afficher, gérer ou bloquer les attributs personnalisés existants, ou en créer des nouveaux. Si vous bloquez un attribut personnalisé, aucune donnée ne sera collectée concernant cet attribut, les données existantes seront indisponibles, sauf si elles sont réactivées, et les attributs exclus ne seront pas affichés dans les filtres.

Si vous désirez enlever des attributs personnalisés des profils utilisateurs, définissez la valeur sur « null » dans votre requête API vers l’endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

## Définition des attributs personnalisés

La liste suivante énumère les méthodes utilisées pour définir des attributs personnalisés sur les différentes plateformes.

{% details Développer la documentation par plateforme %}

- [Android et FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/setting_custom_attributes/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_custom_attributes/)

{% enddetails %}

## Stockage des attributs personnalisé

Toutes les données stockées sur un **Profil utilisateur**, y compris les données d’attribut personnalisées, sont conservé indéfiniment tant que le profil est [actif]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Types de données des attributs personnalisés

Les attributs personnalisés sont des outils extraordinairement flexibles qui permettent un ciblage exceptionnel.

Les types de données suivants peuvent être stockés en tant qu’attributs personnalisés :

- [Booléens](#booleans)
- [Chiffres](#numbers)
- [Chaîne de caractères (string)](#strings)
- [Tableaux (arrays)](#arrays)
- [Date](#time)
- [Objets]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/)
- [Tableaux d’objets]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/)

### Booléens (true/false) {#booleans}

Les attributs booléens sont utiles pour stocker des données binaires simples sur vos utilisateurs, comme le statut d’abonnement. Vous pouvez trouver des utilisateurs qui ont explicitement une variable définie sur Vrai ou Faux, en plus des personnes qui n’ont pas encore d’enregistrement pour cet attribut.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifie si la valeur booléenne **est** vraie, fausse, vraie ou non définie, fausse ou non définie | **EST**  | **VRAI**, **FAUX**, **VRAI OU NON DÉFINI**, ou **FAUX OU NON DÉFINI** |
| Vérifie si la valeur booléenne **existe** sur le profil d’un utilisateur | **N’EST PAS VIDE**  | **S.O.** |
| Vérifie si la valeur booléenne **n’existe pas** sur le profil d’un utilisateur | **EST VIDE**  | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Nombre {#numbers}

Les attributs numériques incluent les [entiers (integer)](https://en.wikipedia.org/wiki/Integer) et [à virgule (floats) ](https://en.wikipedia.org/wiki/Floating-point_arithmetic)et ont une grande variété de cas d’utilisation. Les attributs personnalisés basés sur un un nombre incrémental sont utiles pour stocker le nombre de fois qu’une action ou un événement donné s’est produit sans que ce soit comptabilisé dans votre limite de données. Les numéros standard ont toutes sortes d’utilisations, comme l’enregistrement :

- Pointure
- Tour de taille
- Nombre de fois qu’un utilisateur a regardé une certaine caractéristique ou catégorie de produit

{% alert tip %}
L’argent dépensé ne doit pas être enregistré via cette méthode. Il vaut mieux l’enregistrer via nos [méthodes d’achat](#purchase-revenue-tracking).
{% endalert %}

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si l’attribut numérique **est supérieur à** un **nombre**| **PLUS DE** | **NOMBRE** |
| Vérifie si l’attribut numérique **est inférieur à** un **nombre**| **MOINS DE** | **NOMBRE** |
| Vérifie si l’attribut numérique **est exactement** un **nombre**| **EXACTEMENT** | **NOMBRE** |
| Vérifie si l’attribut numérique **n’est pas égal à ** un **nombre**| **N’EST PAS ÉGAL À** | **NOMBRE** |
| Vérifier si l’attribut numérique **existe** sur le profil d’un utilisateur | **EXISTE** | **S.O.** |
| Vérifier si l’attribut numérique **n’existe pas** sur le profil d’un utilisateur | **N’EXISTE PAS** | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Détails des attributs numériques

- Les filtres « Exactement 0 » et « Inférieur à » incluent les utilisateurs avec des champs NULL
  - Pour exclure les utilisateurs sans valeur pour les attributs personnalisés, vous devez inclure le filtre **n’est pas vide**.

### Strings (caractères alphanumériques) {#strings}

Les attributs au format string sont utiles pour stocker les entrées utilisateur, comme une marque préférée, un numéro de téléphone ou la dernière recherche dans votre application. Les attributs au format string peuvent avoir jusqu’à 255 caractères.

Prenez en compte le fait que, si vous saisissez des valeurs comprenant des espaces entre, avant ou après les mots, Braze cherchera à trouver ces espaces.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifie si l’attribut de chaîne de caractères est **exactement identique** à une chaîne de caractères saisie| **ÉGAL A** | **STRING**<br>Sensible à la casse |
| Vérifie si l’attribut de chaîne de caractères **correspond partiellement** à une chaîne de caractères **OU** une expression régulière | **CORRESPOND À L’EXPRESSION RÉGULIÈRE** | **STRING** **OU** **EXPRESSION RÉGULIÈRE**<br>Pas sensible à la casse. |
| Vérifie si l’attribut de chaîne de caractères **ne correspond pas partiellement** une chaîne de caractères **OU** une expression régulière saisie | **NE CORRESPOND PAS À L’EXPRESSION RÉGULIÈRE** * | **STRING** **OU** **EXPRESSION RÉGULIÈRE**<br>Pas sensible à la casse. |
| Vérifie si l’attribut de chaîne de caractères **ne correspond pas** à une chaîne de caractères saisie| **N’EST PAS ÉGAL À** | **STRING**<br>Pas sensible à la casse.  |
| Vérifie si l’attribut de chaîne de caractères **existe** sur le profil d’un utilisateur | **N’EST PAS VIDE** | **S.O.** |
| Vérifie si l’attribut de chaîne de caractères **n’existe pas** sur le profil d’un utilisateur | **VIDE** | **S.O.** |
| Vérifie si la chaîne de caractères est exactement identique une **quelconque** des chaînes de caractères saisies | **IS ANY OF (est un quelconque parmi)** | **STRING**<br>Sensibles à la casse, plusieurs chaînes de caractères sont autorisées |
| Vérifie si l’attribut de chaîne de caractères **ne correspond pas parfaitement** à une chaîne de caractères saisie | **IS NONE OF (n’est aucune de)** | **STRING**<br>Sensibles à la casse, plusieurs chaînes de caractères sont autorisées |
| Vérifie si l’attribut de chaîne **correspond partiellement** à une chaîne de caractères saisie | **CONTAINS ANY OF (contient un quelconque de)** | **STRING**<br>Sensibles à la casse, plusieurs chaînes de caractères sont autorisées |
| Vérifie si l’attribut de chaîne de caractères **ne correspond pas partiellement** à une chaîne de caractères saisie | **DOESN'T CONTAIN ANY OF (ne contient aucun de)** | **STRING**<br>Sensibles à la casse, plusieurs chaînes de caractères sont autorisées |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Une chaîne de caractères de date telle que « 12-1-2021 » ou « 12/1/2021 » sera convertie en objet datetime et traitée comme un [attribut temporel]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% alert important %}
Lors de la segmentation à l’aide de **NE CORRESPOND PAS À L’EXPRESSION RÉGULIÈRE** vous devez déjà avoir un attribut personnalisé avec une valeur attribuée dans ce profil utilisateur. Braze suggère d’utiliser la logique « OR » (OU) pour vérifier si un attribut personnalisé est vide pour s’assurer que les utilisateurs sont correctement ciblés.<br>

Plus de ressources sur les expressions régulières :
- [Braze et les expressions régulières]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Débogueur et testeur d’expression régulière](https://regex101.com/)
- [Didacticiel d’expression régulière](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Arrays {#arrays}

Les attributs de tableau sont appropriés pour stocker les listes d’informations associées à vos utilisateurs. Par exemple, le stockage en tableau des 100 derniers morceaux de contenu qu’un utilisateur a regardé permettrait une segmentation spécifique basée sur les intérêts.

Par défaut, la longueur maximale d’un tableau pour un attribut est définie sur 25 et peut être augmentée à 100 pour un tableau individuel. Par exemple, si vous envoyez un attribut tel que « Films regardés » et qu’il est défini sur 100, lorsqu’un utilisateur regarde un 101e film, le premier film est retiré du tableau et le film le plus récent sera ajouté.

Si vous souhaitez que cette limite soit augmentée, contactez votre gestionnaire du succès des clients. Votre administrateur de tableau de bord peut alors augmenter la longueur maximale pour les tableaux individuels au-delà de 100 sur l’onglet **Custom Attributes (Attributs personnalisés)** de la page **Manage Settings (Gérer les paramètres)**.

Prenez en compte le fait que, si vous saisissez des valeurs comprenant des espaces entre, avant ou après les mots, Braze cherchera à trouver ces espaces.

{% alert note %}
L’option d’augmentation de la longueur maximale ne sera pas disponible si la détection automatique du type de données est défini pour l’attibut ; le type de données doit être défini sur Array (Tableau).
{% endalert %}

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifie si l’attribut du tableau **inclut une valeur qui correspond exactement à** une valeur entrée| **INCLUT LA VALEUR** | **STRING** |
| Vérifie si l’attribut du tableau **n’inclut pas une valeur qui correspond exactement à** une valeur entrée| **N’INCLUT PAS LA VALEUR** | **STRING** |
| Vérifie si l’attribut du tableau **contient une valeur qui correspond partiellement à** une valeur entrée **OU** une Expression régulière | **CORRESPOND À L’EXPRESSION RÉGULIÈRE** | **STRING** **OU** **EXPRESSION RÉGULIÈRE** |
| Vérifie si l’attribut du tableau **a une valeur quelconque** | **A UNE VALEUR** | **S.O.** |
| Vérifie si l’attribut du tableau **est vide** | **EST VIDE** | **S.O.** |
| Vérifie si l’attribut du tableau **inclut une valeur qui correspond exactement à** une des valeurs entrées | **INCLUDES ANY OF (comprend une de)** | **STRING**<br>Sensible à la casse, plusieurs valeurs autorisées |
| Vérifie si l’attribut du tableau **ne comprend pas une valeur qui correspond exactement à** une des valeurs entrées | **INCLUDES NONE OF (ne comprend aucune de)** | **STRING**<br>Sensible à la casse, plusieurs valeurs autorisées |
| Vérifie si l’attribut du tableau **contient une valeur qui correspond partiellement à** une des valeurs entrées | **VALUES CONTAIN ANY OF (les valeurs contiennent une de)** | **STRING**<br>Sensible à la casse, plusieurs valeurs autorisées |
| Vérifie si l’attribut du tableau **ne comprend pas une valeur qui correspond partiellement à** une des valeurs entrées | **VALUES DON’T CONTAIN ANY OF (les valeurs ne contiennent aucune de)** | **STRING**<br>Sensible à la casse, plusieurs valeurs autorisées |
| Vérifie si l’attribut du tableau **contient toutes** les valeurs entrées | **IS ALL OF (est tout parmi)** | **STRING**<br>Sensible à la casse, plusieurs valeurs autorisées |
| Vérifie si l’attribut du tableau **ne contient pas toutes** les valeurs entrées | **ISN'T ALL OF (n’est pas tout parmi)** | **STRING**<br>Sensible à la casse, plusieurs valeurs autorisées |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
Pour en savoir plus sur la façon d’utiliser notre filtre d’expressions régulières, consultez la documentation sur les [expressions régulières compatibles Perl](http://www.regextester.com/pregsyntax.html) (PCRE).
<br>
Plus de ressources sur les expressions régulières :
- [Braze et les expressions régulières]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Débogueur et testeur d’expression régulière](https://regex101.com/)
- [Didacticiel d’expression régulière](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Date {#time}

Les attributs de temps sont utiles pour stocker la dernière fois qu’une action spécifique a été prise, car ils vous permettent d’envoyer des contenus spécifiques  de ré-engagement dans vos envois de messages client.

Les filtres temporels basés sur des dates relatives (par ex. il y a plus d’un jour, il y a moins de 2 jours) mesurent 1 journée en tant que 24 heures. Toute campagne que vous exécutez à l’aide de ces filtres inclura tous les utilisateurs par incréments de 24 heures. Par exemple, `last used app more than 1 day ago` va capturer tous les utilisateurs qui ont « utilisé l’application plus de 24 heures » à partir du lancement exact de la campagne. Il en va de même pour les campagnes définies avec des plages de dates plus longues. Ainsi, cinq jours après l’activation signifie les 120 heures précédentes.

Par exemple, pour créer un segment qui cible les utilisateurs avec un attribut temporel entre 24 et 48 heures dans le futur, appliquez les filtres `in more than 1 day in the future` et `in less than 2 days in the future`.

{% alert warning %}
La dernière date à laquelle un événement personnalisé ou événement d’achat s’est produit est automatiquement enregistrée et ne doit pas être enregistrée de nouveau avec un attribut de temps personnalisé.
{% endalert %}

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifie si l’attribut de temps est **avant** une **date sélectionnée**| **AVANT** | **SÉLECTEUR DE DATE** |
| Vérifie si l’attribut de temps **est après** une **date sélectionnée**| **APRÈS** | **SÉLECTEUR DE DATE** |
| Vérifie si l’attribut de temps est postérieur à **il y a plus de X** **jours** | **PLUS DE** | **IL Y A NOMBRE DE JOURS** |
| Vérifie si l’attribut de temps est antérieur à **il y a moins de X** **jours**| **MOINS DE** | **IL Y A NOMBRE DE JOURS** |
| Vérifie si l’attribut de temps est dans **plus de X** jours **dans le futur** | **DANS PLUS DE** | ** JOURS À L’AVENIR** |
| Vérifie si l’attribut de temps est dans **moins de X** jours **dans le futur** | **DANS MOINS DE** | ** JOURS À L’AVENIR**  |
| Vérifie si l’attribut de temps **existe** sur le profil d’un utilisateur | **N’EST PAS VIDE** | **S.O.** |
| Vérifie si l’attribut de temps **n’existe pas** sur le profil d’un utilisateur | **EST VIDE** | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Détails des attributs temporels

- Jour de l’événement récurrent
  - Si vous utilisez le filtre « Jour d’événement récurrent », vous êtes invité à sélectionner le « Jour civil de l’événement récurrent » si vous sélectionnez `IS LESS THAN` ou `IS MORE THAN`, la date actuelle sera comptée pour ce filtre de segmentation.
  - Par exemple, si le 10 mars 2020, vous avez défini la date de l’attribut sur `LESS THAN ... March 10, 2020`, les attributs seront pris en compte pour les jours jusqu’au 10 mars 2020 inclus. 
- Il y a moins de X jours : Le filtre « Il y a moins de X jours » inclut des dates entre il y a X jours et la date/heure actuelle.
- Moins de X jours dans le futur : Inclut les dates entre la date/heure actuelle et les X jours à l’avenir.

### Objets

Vous pouvez utiliser des attributs personnalisés imbriqués pour envoyer des objets en tant que type de données pour des attributs personnalisés. Pour plus d’informations, consultez [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/).

### Tableaux d’objets

Utilisez un tableau d’objets pour regrouper des attributs associés. Pour plus d’informations, consultez [Tableau d’objets]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/).

## Suivi des achats et des revenus {#purchase-revenue-tracking}

L’utilisation de nos méthodes d’achat pour enregistrer les achats dans l’application établit la Valeur à vie (LTV) pour chaque profil utilisateur individuel. Ces données sont consultables sur notre page de revenus dans les séries temporelles.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifie si le total de dollars dépensé **est supérieur à **un **nombre**| **SUPÉRIEUR À** | **NOMBRE** |
| Vérifie si le total de dollars dépensé **est inférieur à **un **nombre**| **MOINS DE** | **NOMBRE** |
| Vérifie si le nombre total de dollars dépensé **est exactement** un **nombre**| **EXACTEMENT** | **NOMBRE** |
| Vérifie si l’achat a été effectué **après la date X** | **APRÈS** | **DATE** |
| Vérifiez si l’achat a été effectué **avant la date X** | **AVANT** | **DATE** |
| Vérifiez si l’achat a été effectué **il y a plus de X jours** | **PLUS DE** | **DATE** |
| Vérifie si l’achat a été effectué **il y a moins de X jours** | **MOINS DE** | **DATE** |
| Vérifie si l’achat a eu lieu **plus de X (Max = 50) fois** | **PLUS DE** | in les **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifie si l’achat a eu lieu **moins de X (Max = 50) fois** | **MOINS DE** | in les **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifie si l’achat a eu lieu **exactement X (Max = 50) fois** | **EXACTEMENT** | in les **Y derniers jours (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
Si vous souhaitez segmenter sur le nombre de fois où un achat spécifique s’est produit, vous devez également enregistrer l’achat individuel en tant [ qu’attribut personnalisé incrémental.]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes).
{% endalert %}

Vous pouvez modifier le type de données de votre attribut personnalisé, mais vous devez être conscient des impacts de la [modification des types de données]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/).

