---
nav_title: Attributs personnalisés
article_title: Attributs personnalisés
page_order: 10
page_type: reference
description: "Cette page décrit les attributs personnalisés et explique les différents types de données d'attributs personnalisés."
search_rank: 1
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"} Attributs personnalisés

> Cette page traite des attributs personnalisés, qui regroupent les caractéristiques uniques de vos utilisateurs. Les attributs personnalisés sont particulièrement adaptés pour stocker des informations sur vos utilisateurs ou sur les actions à faible valeur au sein de votre application. 

Lorsqu'ils sont stockés dans Braze, les attributs personnalisés peuvent servir à créer des segments d'audience et à personnaliser l'envoi de messages à l'aide de Liquid. Gardez à l'esprit que Braze ne stocke pas d'informations de séries temporelles pour les attributs personnalisés. Vous ne pourrez donc pas obtenir de graphiques basés sur ces attributs, contrairement aux événements personnalisés.

## Gestion des attributs personnalisés

Pour créer et gérer des attributs personnalisés dans le tableau de bord, accédez à **Paramètres des données** > **Attributs personnalisés**. 

![Quatre attributs personnalisés de type booléen.]({% image_buster /assets/img/export_custom_attributes.png %})

La colonne **Dernière mise à jour** indique la dernière modification de l'attribut personnalisé, par exemple lorsqu'il a été placé en liste de blocage ou réactivé.

{% alert important %}
Pour un ciblage correct des messages, assurez-vous que le type de données de votre attribut personnalisé correspond bien à l'attribut personnalisé réel. <br><br>Par exemple, si `newsletter_subscribed` est défini comme une chaîne de caractères, votre syntaxe Liquid devrait ressembler à {% raw %}```{% if {{custom_attribute.${newsletter_subscribed}}} == 'true' %}```{% endraw %}. Si `newsletter_subscribed` est défini comme une valeur booléenne, la syntaxe Liquid ne doit pas comporter de guillemets simples : {% raw %}```{% if {{custom_attribute.${newsletter_subscribed}}} == true %}```{% endraw %}.
{% endalert %}

Depuis cette page, vous pouvez afficher, gérer, créer ou mettre en liste de blocage des attributs personnalisés existants. Sélectionnez le menu à côté d'un attribut personnalisé pour accéder aux actions suivantes :

### Mise en liste de blocage

Les attributs personnalisés peuvent être bloqués individuellement via le menu d'actions, ou jusqu'à 100 attributs peuvent être sélectionnés et bloqués en bloc. Lorsque vous bloquez un attribut personnalisé, aucune donnée n'est collectée pour cet attribut, les données existantes deviennent indisponibles (sauf réactivation), et les attributs bloqués n'apparaissent plus dans les filtres ni les graphiques. De plus, si l'attribut est référencé par des filtres ou des déclencheurs dans d'autres zones du tableau de bord de Braze, une fenêtre modale d'avertissement s'affiche pour vous informer que toutes les instances de ces filtres ou déclencheurs seront supprimées et archivées.

### Marquage en tant qu'information personnelle identifiable (PII)

Les administrateurs peuvent également créer des attributs personnalisés et les marquer comme PII depuis cette page. Ces attributs ne seront visibles que par les administrateurs et les utilisateurs du tableau de bord disposant de l'autorisation « Voir les attributs personnalisés marqués comme PII ».

### Ajout de descriptions

Vous pouvez ajouter une description à un attribut personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases`. Modifiez l'attribut personnalisé et saisissez ce que vous souhaitez, par exemple une note destinée à votre équipe.

### Ajout d'étiquettes

Vous pouvez ajouter des étiquettes à un attribut personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) « Gérer les événements, les attributs et les achats ». Les étiquettes peuvent ensuite être utilisées pour filtrer la liste des attributs. 

### Suppression des attributs personnalisés

Il existe deux façons de supprimer des attributs personnalisés des profils utilisateurs :

* Sélectionnez le nom de l'attribut personnalisé à supprimer dans une [étape de mise à jour de l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes).
* Définissez la valeur `null` dans votre requête API vers l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

### Exportation des données

Pour exporter la liste des attributs personnalisés sous forme de fichier CSV, sélectionnez **Exporter tout** en haut de la page. Le fichier CSV sera généré et un lien de téléchargement vous sera envoyé par e-mail.

## Consultation des rapports d'utilisation

Le rapport d'utilisation répertorie tous les Canvas, campagnes et segments qui utilisent un attribut personnalisé spécifique. Cette liste n'inclut pas les utilisations de Liquid. 

Vous pouvez consulter jusqu'à 100 rapports d'utilisation à la fois en cochant les cases correspondantes à côté des attributs personnalisés, puis en sélectionnant **Afficher le rapport d'utilisation**.

### Onglet Valeurs

Lorsque vous consultez un rapport d'utilisation, sélectionnez l'onglet **Valeurs** pour afficher les principales valeurs des attributs personnalisés sélectionnés, sur la base d'un échantillon d'environ 250 000 utilisateurs. Les résultats étant issus d'un sous-ensemble d'utilisateurs, l'échantillon n'inclura pas nécessairement toutes les valeurs existantes. L'onglet **Valeurs** ne doit donc pas être utilisé pour la résolution des problèmes ni pour les cas d'utilisation nécessitant les données de l'ensemble des utilisateurs.

![Rapport d'utilisation pour les attributs personnalisés sélectionnés avec l'onglet « Valeurs » ouvert, présentant un graphique circulaire des valeurs d'attributs de pays, telles que « US » et « PR ».]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## Définition des attributs personnalisés

Voici les méthodes utilisées pour définir des attributs personnalisés sur les différentes plateformes.

{% details Développer pour la documentation par plateforme %}

- [Android et FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [.NET MAUI (anciennement Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## Stockage des attributs personnalisés

Toutes les données stockées dans le **profil utilisateur**, y compris les données d'attributs personnalisés, sont conservées indéfiniment tant que chaque profil est [actif]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Types de données des attributs personnalisés

Les attributs personnalisés sont des outils extrêmement flexibles qui permettent un ciblage très précis.

Les types de données suivants peuvent être stockés en tant qu'attributs personnalisés :

- [Booléens](#booleans)
- [Nombres](#numbers)
- [Chaînes de caractères](#strings)
- [Tableaux](#arrays)
- [Date](#time)
- [Objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)
- [Tableaux d'objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)

### Booléens (vrai/faux) {#booleans}

Les attributs booléens sont utiles pour stocker des données binaires simples sur vos utilisateurs, comme le statut d'abonnement. Vous pouvez rechercher les utilisateurs dont une variable est explicitement définie sur vrai ou faux, ainsi que ceux pour lesquels cet attribut n'a pas encore été enregistré.

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si la valeur booléenne **est** soit vraie, soit fausse, soit vraie ou non définie, soit fausse ou non définie | **EST**  | **VRAI**, **FAUX**, **VRAI OU NON ENREGISTRÉ**, ou **FAUX OU NON ENREGISTRÉ** | Si ce filtre spécifie `coffee_drinker`, un utilisateur correspondra à ce filtre dans les circonstances suivantes : <br> {::nomarkdown}<ul><li>Si ce filtre est <code>true</code> et l'utilisateur a la valeur <code>coffee_drinker</code></li><li>Si ce filtre est <code>false</code> et l'utilisateur n'a pas la valeur <code>coffee_drinker</code></li><li>Si ce filtre est <code>true or not set</code> et l'utilisateur a la valeur <code>coffee_drinker</code> ou aucune valeur</li><li>Si ce filtre est <code>false or not set</code> et l'utilisateur n'a pas <code>coffee_drinker</code> ou aucune valeur</li></ul>{:/} |
| Vérifier si la valeur booléenne **existe** dans le profil d'un utilisateur et n'est pas nulle | **N'EST PAS VIDE**  | **S.O.** | Si ce filtre spécifie `coffee_drinker` et qu'un utilisateur possède une valeur pour l'attribut `coffee_drinker`, l'utilisateur correspondra à ce filtre. | 
| Vérifier si la valeur booléenne **n'existe pas** dans le profil de l'utilisateur ou est nulle | **EST VIDE**  | **S.O.** | Si ce filtre spécifie `coffee_drinker` et qu'un utilisateur n'a pas l'attribut `coffee_drinker` ou que la valeur de `coffee_drinker` est nulle, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Nombres {#numbers}

Les attributs numériques comprennent les [entiers](https://en.wikipedia.org/wiki/Integer) et les [floats](https://en.wikipedia.org/wiki/Floating-point_arithmetic), et couvrent une grande variété de cas d'utilisation. Les attributs personnalisés numériques incrémentaux sont utiles pour comptabiliser le nombre de fois qu'une action ou un événement donné s'est produit, sans que cela soit décompté de votre limite de données. Les nombres standard ont toutes sortes d'utilisations, comme l'enregistrement :

- Pointure
- Tour de taille
- Nombre de fois qu'un utilisateur a consulté une fonctionnalité ou catégorie de produit donnée

{% alert tip %}
Les dépenses ne doivent pas être enregistrées via cette méthode. Utilisez plutôt nos [méthodes d'achat](#purchase-revenue-tracking).
{% endalert %}

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut numérique **est exactement** un **nombre**| **EXACTEMENT** | **NOMBRE** | Si ce filtre spécifie `10` et qu'un profil utilisateur a la valeur `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **n'est pas égal à** un **nombre**| **N'EST PAS ÉGAL À** | **NOMBRE** | Si ce filtre spécifie `10` et qu'un profil utilisateur n'a pas la valeur `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **est supérieur à** un **nombre**| **PLUS DE** | **NOMBRE** | Si ce filtre spécifie `10` et qu'un profil utilisateur a une valeur supérieure à `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **est inférieur à** un **nombre**| **MOINS DE** | **NOMBRE** | Si ce filtre spécifie `10` et qu'un profil utilisateur a une valeur inférieure à `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **existe** dans le profil d'un utilisateur et n'est pas nul | **N'EST PAS VIDE** | **S.O.** | Si un profil utilisateur contient l'attribut numérique spécifié, quelle que soit sa valeur, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **n'existe pas** dans le profil d'un utilisateur ou est nul | **EST VIDE** | **S.O.** | Si un profil utilisateur ne contient pas l'attribut numérique spécifié ou si la valeur de l'attribut est nulle, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Détails des attributs numériques

- Les filtres « Exactement 0 » et « Inférieur à » incluent les utilisateurs avec des champs NULL
  - Pour exclure les utilisateurs sans valeur pour les attributs personnalisés, vous devez inclure le filtre **n'est pas vide**.

### Chaînes de caractères (caractères alphanumériques) {#strings}

Les attributs de type chaîne de caractères sont utiles pour stocker les saisies utilisateur, comme une marque préférée, un numéro de téléphone ou la dernière recherche effectuée dans votre application. Les attributs de type chaîne de caractères peuvent contenir jusqu'à 255 caractères.

Notez que si vous saisissez des valeurs comportant des espaces entre, avant ou après les mots, Braze vérifiera également la présence de ces mêmes espaces.

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut chaîne de caractères **correspond partiellement à** une chaîne saisie **OU** une expression régulière | **CORRESPOND À L'EXPRESSION RÉGULIÈRE** | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE** <br>Non sensible à la casse ; maximum de 32 764 caractères | 
| Vérifier si l'attribut chaîne de caractères **ne correspond pas partiellement à** une chaîne saisie **OU** une expression régulière | **NE CORRESPOND PAS À L'EXPRESSION RÉGULIÈRE** * | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE**<br>Non sensible à la casse ; maximum de 32 764 caractères |
| Vérifier si l'attribut chaîne de caractères **existe** dans le profil d'un utilisateur et n'est pas une chaîne vide | **N'EST PAS VIDE** | **S.O.** | Si ce filtre spécifie `favorite_genre` et qu'un profil utilisateur possède l'attribut `favorite_genre`, l'utilisateur correspondra à ce filtre quelle que soit la valeur de l'attribut. Par exemple, l'utilisateur peut avoir `sci-fi`, `romance` ou une autre valeur.|
| Vérifier si l'attribut chaîne de caractères **n'existe pas** dans le profil d'un utilisateur | **VIDE** | **S.O.** | Si ce filtre spécifie `favorite_genre` et qu'un profil utilisateur ne possède pas l'attribut `favorite_genre`, l'utilisateur correspondra à ce filtre.|
| Vérifier si la chaîne correspond exactement à **l'une des** chaînes saisies | **EST L'UNE DES VALEURS PARMI** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs chaînes autorisées (256 au maximum) | Si ce filtre spécifie `book`, `bookmark` et `reading light`, et qu'un profil utilisateur contient au moins une de ces chaînes, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut chaîne **ne correspond exactement à aucune des** chaînes saisies | **N'EST AUCUNE DES VALEURS PARMI** |**CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs chaînes autorisées (256 au maximum) | Si ce filtre spécifie `book`, `bookmark` et `reading light`, et qu'un profil utilisateur ne contient aucune de ces chaînes, l'utilisateur correspondra au filtre.|
| Vérifier si l'attribut chaîne **correspond partiellement à l'une des** chaînes saisies | **CONTIENT L'UN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs chaînes autorisées (256 au maximum) | Si ce filtre spécifie `gold` et qu'un profil utilisateur contient `gold` dans une chaîne quelconque, comme `gold_tier` ou `former_gold_tier`, l'utilisateur correspondra au filtre. |
| Vérifier si l'attribut chaîne **ne correspond partiellement à aucune des** chaînes saisies | **NE CONTIENT AUCUN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs chaînes autorisées (256 au maximum) | Si ce filtre spécifie `gold` et qu'un profil utilisateur ne contient pas `gold` dans une chaîne, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

{% alert important %}
Lorsque vous effectuez une segmentation avec le filtre **NE CORRESPOND PAS À L'EXPRESSION RÉGULIÈRE**, l'attribut personnalisé doit déjà avoir une valeur attribuée dans le profil utilisateur. Braze recommande d'utiliser la logique « OR » (OU) pour vérifier si un attribut personnalisé est vide afin de s'assurer que les utilisateurs sont correctement ciblés.
{% endalert %}

### Tableaux {#arrays}

Les attributs de type tableau sont adaptés pour stocker des listes d'informations associées à vos utilisateurs. Par exemple, stocker dans un tableau les 100 derniers contenus consultés par un utilisateur permet une segmentation précise basée sur les centres d'intérêt.

Les tableaux ont une taille maximale de 100 Ko. La longueur par défaut d'un attribut est de 500 éléments maximum. Par exemple, si vous envoyez un attribut tel que « Films regardés » défini sur 500, lorsqu'un utilisateur regarde un 501e film, le premier film sera supprimé du tableau et le plus récent sera ajouté. 

Notez que si vous saisissez des valeurs avec des espaces entre, avant ou après les mots, Braze vérifiera également la présence de ces mêmes espaces.

{% alert note %}
L'option permettant d'augmenter la longueur maximale n'est pas disponible si l'attribut est configuré pour détecter automatiquement le type de données ; le type de données doit être défini sur tableau.
{% endalert %}

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut du tableau **inclut une valeur qui correspond exactement** à une valeur saisie| **INCLUT LA VALEUR** | **CHAÎNE DE CARACTÈRES** | Si ce filtre spécifie `sci-fi` et qu'un profil utilisateur a la valeur `sci-fi`, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut du tableau **n'inclut pas une valeur qui correspond exactement** à une valeur saisie| **NE COMPREND PAS DE VALEUR** | **CHAÎNE DE CARACTÈRES** | Si ce filtre spécifie `sci-fi` et qu'un profil utilisateur n'a pas la valeur `sci-fi`, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut du tableau **contient une valeur qui correspond partiellement** à une valeur saisie **OU** une expression régulière | **CORRESPOND À L'EXPRESSION RÉGULIÈRE** | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE**<br>Maximum de 32 764 caractères | |
| Vérifier si l'attribut du tableau **a une valeur** ou n'est pas vide | **A UNE VALEUR** | **S.O.** | Si ce filtre spécifie `favorite_genres` et qu'un profil utilisateur contient `favorite_genres` avec n'importe quelle valeur, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut du tableau **est vide** ou n'existe pas | **EST VIDE** | **S.O.** | Si ce filtre spécifie `favorite_genres` et qu'un profil utilisateur ne contient pas `favorite_genres` ou contient `favorite_genres` sans aucune valeur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut du tableau **contient une valeur qui correspond exactement à l'une des** valeurs saisies | **COMPREND L'UN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur possède n'importe quelle combinaison de `sci-fi`, `fantasy` ou `romance`, y compris un seul d'entre eux (par exemple uniquement `sci-fi`). Un utilisateur peut avoir `horror` ou une autre valeur dans sa chaîne s'il possède également `sci-fi`, `fantasy` ou `romance`.|
| Vérifier si l'attribut du tableau **ne contient pas de valeur correspondant exactement à l'une des** valeurs saisies | **NE COMPREND AUCUN DES ÉLÉMENTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur ne comporte aucune combinaison de `sci-fi`, `fantasy` ou `romance`, l'utilisateur correspondra à ce filtre. L'utilisateur peut avoir `horror` ou une autre valeur s'il n'a aucune des valeurs `sci-fi`, `fantasy` ou `romance`.|
| Vérifier si l'attribut du tableau **contient une valeur qui correspond partiellement à l'une des** valeurs saisies | **CONTIENNENT L'UN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `gold` et qu'un tableau de profil utilisateur contient `gold` dans au moins une chaîne, l'utilisateur correspondra à ce filtre. Cela inclut des valeurs telles que `gold_tier`, `former_gold_tier`, etc.|
| Vérifier si l'attribut du tableau **ne contient pas de valeur correspondant partiellement à l'une des** valeurs saisies | **NE CONTIENNENT AUCUN DES ÉLÉMENTS SUIVANTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `gold` et que le tableau d'un profil utilisateur ne contient pas `gold` dans aucune chaîne, l'utilisateur correspondra à ce filtre. Les utilisateurs ayant des valeurs telles que `gold_tier` et `former_gold_tier` ne correspondront donc pas à ce filtre.|
| Vérifier si l'attribut du tableau **comprend toutes les** valeurs saisies | **INCLUT TOUS LES ÉLÉMENTS** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur possède toutes ces valeurs, l'utilisateur correspondra à ce filtre. L'utilisateur peut également avoir `horror` ou d'autres valeurs et correspondre à ce filtre.|
| Vérifier si l'attribut du tableau **n'inclut pas toutes les** valeurs saisies | **N'EST PAS TOUS LES ÉLÉMENTS PARMI** | **CHAÎNE DE CARACTÈRES**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 au maximum)|  Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur ne possède pas toutes ces valeurs, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Pour en savoir plus sur l'utilisation des expressions régulières (regex), consultez ces ressources :
- [Expressions régulières compatibles avec Perl (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Braze et les expressions régulières]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Débogueur et testeur d'expressions régulières](https://www.regex101.com/)
- [Tutoriel sur les expressions régulières](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Date {#time}

Les attributs de date sont utiles pour stocker la dernière fois qu'une action spécifique a été effectuée, ce qui vous permet d'envoyer des messages de réengagement ciblés à vos utilisateurs.

Les filtres temporels utilisant des dates relatives (par exemple, il y a plus d'un jour, il y a moins de deux jours) comptent 1 jour comme 24 heures. Toute campagne utilisant ces filtres inclura tous les utilisateurs par incréments de 24 heures. Par exemple, `last used app more than 1 day ago` capturera tous les utilisateurs qui ont « utilisé l'application il y a plus de 24 heures » à partir du moment exact où la campagne est lancée. Il en va de même pour les campagnes avec des plages de dates plus longues : cinq jours après l'activation correspondent aux 120 heures précédentes.

Par exemple, pour créer un segment ciblant les utilisateurs avec un attribut de date situé entre 24 et 48 heures dans le futur, appliquez les filtres `in more than 1 day in the future` et `in less than 2 days in the future`.

{% alert warning %}
La dernière date à laquelle un événement personnalisé ou un événement d'achat s'est produit est automatiquement enregistrée et ne doit pas être enregistrée de nouveau via un attribut de date personnalisé.
{% endalert %}

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut de date **est antérieur à** une **date sélectionnée**| **AVANT** | **SÉLECTEUR DE DATE DU CALENDRIER** | Si ce filtre spécifie `2024-01-31` et que le profil d'un utilisateur a une date antérieure à `2024-1-31`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut de date **est postérieur à** une **date sélectionnée**| **APRÈS** | **SÉLECTEUR DE DATE DU CALENDRIER** | Si ce filtre spécifie `2024-01-31` et que le profil d'un utilisateur a une date postérieure à `2024-1-31`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut de date remonte à **plus de X** jours | **PLUS DE** | **NOMBRE DE JOURS ÉCOULÉS** | Si ce filtre spécifie `7` et qu'un profil utilisateur a une date remontant à plus de sept jours, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut de date remonte à **moins de X** jours| **MOINS DE** | **NOMBRE DE JOURS ÉCOULÉS** | Si ce filtre spécifie `7` et que le profil utilisateur a une date remontant à moins de sept jours, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de date se situe **dans plus de X** jours dans le futur | **DANS PLUS DE** | **NOMBRE DE JOURS À VENIR** | Si ce filtre spécifie `7` et que le profil utilisateur a une date située à plus de sept jours dans le futur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de date se situe **dans moins de X** jours dans le futur | **DANS MOINS DE** | **NOMBRE DE JOURS À VENIR**  | Si ce filtre spécifie `7` et que le profil utilisateur a une date située à moins de sept jours dans le futur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de date **existe** dans le profil d'un utilisateur et n'est pas nul | **N'EST PAS VIDE** | **S.O.** | Si ce filtre spécifie un attribut de date présent dans un profil utilisateur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de date **n'existe pas** dans le profil d'un utilisateur ou est nul | **EST VIDE** | **S.O.** | Si ce filtre spécifie un attribut de date absent du profil utilisateur, l'utilisateur correspondra à ce filtre. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Détails des attributs de date

- Jour de l'événement récurrent
  - Si vous utilisez le filtre « Jour d'événement récurrent » et êtes invité à sélectionner le « Jour civil de l'événement récurrent », si vous sélectionnez `IS LESS THAN` ou `IS MORE THAN`, la date actuelle sera comptée pour ce filtre de segmentation.
  - Par exemple, si le 10 mars 2020, vous avez défini la date de l'attribut sur `LESS THAN ... March 10, 2020`, les attributs seront pris en compte pour les jours jusqu'au 10 mars 2020 inclus. 
- Il y a moins de X jours : le filtre « Il y a moins de X jours » inclut les dates entre il y a X jours et la date/heure actuelle.
- Moins de X jours dans le futur : inclut les dates entre la date/heure actuelle et les X jours à venir.

### Objets

Vous pouvez utiliser des attributs personnalisés imbriqués pour envoyer des objets en tant que type de données pour des attributs personnalisés. Pour plus d'informations, consultez la section [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/).

### Tableaux d'objets

Utilisez un tableau d'objets pour regrouper des attributs associés. Pour plus de détails, consultez notre article sur les [tableaux d'objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/).

### Opérateurs consolidés

Nous avons consolidé la liste des opérateurs disponibles pour les filtres d'attributs, les filtres d'attributs personnalisés et les filtres d'attributs personnalisés imbriqués. Si vous avez des filtres existants utilisant ces opérateurs, ils seront automatiquement mis à jour pour utiliser les nouveaux opérateurs.

| Type de données | Ancien opérateur | Nouvel opérateur | Valeur |
| --- | --- | --- | --- |
| Chaîne de caractères | est égal à | est l'une des valeurs parmi | Au moins une valeur |
| Chaîne de caractères | n'est pas égal à | n'est aucune des valeurs parmi | Au moins une valeur |
| Tableau | inclut la valeur | comprend l'un des éléments | Au moins une valeur |
| Tableau | n'inclut pas la valeur | ne comprend aucun des éléments | Au moins une valeur |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Suivi des achats et du chiffre d'affaires {#purchase-revenue-tracking}

L'utilisation de nos méthodes d'achat pour enregistrer les achats in-app établit la valeur vie client (LTV) pour chaque profil utilisateur individuel. Ces données sont consultables sur notre page de chiffre d'affaires sous forme de séries temporelles.

| Options de segmentation | Filtre déroulant | Options d'entrée | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si le montant total dépensé en dollars **est supérieur à** un **nombre**| **SUPÉRIEUR À** | **NOMBRE** | Si ce filtre spécifie `500` et qu'un profil utilisateur a une valeur supérieure à `500`, l'utilisateur correspondra à ce filtre. |
| Vérifier si le montant total dépensé en dollars **est inférieur à** un **nombre**| **MOINS DE** | **NOMBRE** | Si ce filtre spécifie `500` et que le profil utilisateur a une valeur inférieure à `500`, l'utilisateur correspondra à ce filtre.|
| Vérifier si le montant total dépensé en dollars **est exactement** un **nombre**| **EXACTEMENT** | **NOMBRE** | Si ce filtre spécifie `500` et qu'un profil utilisateur a la valeur `500`, l'utilisateur correspondra à ce filtre. |
| Vérifier si le dernier achat a eu lieu **après la date X** | **APRÈS** | **DATE** | Si ce filtre spécifie `2024/31/1` et que le dernier achat d'un utilisateur a eu lieu après `2024/31/1`, l'utilisateur correspondra à ce filtre.|
| Vérifier si le dernier achat a eu lieu **avant la date X** | **AVANT** | **DATE** | Si ce filtre spécifie `2024/31/1` et que le dernier achat d'un utilisateur est antérieur à `2024/31/1`, l'utilisateur correspondra à ce filtre.|
| Vérifier si le dernier achat a été effectué **il y a plus de X jours** | **PLUS DE** | **DATE** | Si ce filtre spécifie `7` et que le dernier achat d'un utilisateur remonte à plus de sept jours, l'utilisateur correspondra à ce filtre.|
| Vérifier si le dernier achat a été effectué **il y a moins de X jours** | **MOINS DE** | **DATE** |  Si ce filtre spécifie `7` et que le dernier achat d'un utilisateur date de moins de sept jours, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'achat a eu lieu **plus de X (max. = 50) fois** | **PLUS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |  Si ce filtre spécifie `7` fois et `21` jours, et qu'un utilisateur a effectué plus de sept achats au cours des 21 derniers jours, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'achat a eu lieu **moins de X (max. = 50) fois** | **MOINS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** | Si ce filtre spécifie `7` fois et `21` jours, et qu'un utilisateur a effectué moins de sept achats au cours des 21 derniers jours, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'achat a eu lieu **exactement X (max. = 50) fois** | **EXACTEMENT** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** | Si ce filtre spécifie `7` fois et `21` jours, et qu'un utilisateur a effectué sept achats au cours des 21 derniers jours, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Si vous souhaitez segmenter en fonction du nombre de fois qu'un achat spécifique a été effectué, vous devez également enregistrer cet achat individuellement en tant qu'[attribut personnalisé incrémentiel]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes).
{% endalert %}

Vous pouvez modifier le type de données de votre attribut personnalisé, mais gardez à l'esprit les conséquences d'un [changement de type de données]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/).