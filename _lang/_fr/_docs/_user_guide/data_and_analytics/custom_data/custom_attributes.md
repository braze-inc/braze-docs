---
nav_title: Attributs personnalisés
article_title: Attributs personnalisés
page_order: 3
page_type: Référence
description: "Cet article de référence décrit les attributs personnalisés et explique les différents types de données d'attributs personnalisés."
---

# Attributs personnalisés

Les attributs personnalisés sont une collection de traits uniques de vos utilisateurs. Les attributs personnalisés sont les meilleurs pour stocker des attributs à propos de vos utilisateurs, ou des informations sur les actions à faible valeur dans votre application. Vous devez garder à l'esprit que nous ne stockons pas les informations de séries temporelles pour les attributs personnalisés, de sorte que vous ne serez pas en mesure d'obtenir des graphiques basés sur eux comme vous le pouvez pour des événements personnalisés.

{% alert tip %}
Nous obtenons que les attributs personnalisés peuvent être confus. Pour en savoir plus sur l'utilisation d'attributs personnalisés dans vos stratégies de messagerie, consultez notre cours LAB [Événements et attributs personnalisés](http://lab.braze.com/custom-events-and-attributes)!
{% endalert %}

## Paramétrage des attributs personnalisés

Voici la liste des méthodes utilisées par les différentes plateformes pour définir des attributs personnalisés.

{% details Expand for documentation by platform %}

- [Android et FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/)
- [React Natif]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unité]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/setting_custom_attributes/)
- [Univers Windows]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_custom_attributes/)

{% enddetails %}

## Stockage d'attributs personnalisés

Toutes les données stockées sur le **Profil utilisateur**, y compris les données d'attributs personnalisés, sont conservées indéfiniment tant que chaque profil est actif.

## Types de données d'attributs personnalisés

Les attributs personnalisés sont des outils extraordinairement flexibles qui permettent un meilleur ciblage.

Les types de données suivants peuvent être stockés en tant qu'attributs personnalisés :

- [Booléens](#booleans)
- [Numéros](#numbers)
- [Chaînes de caractères](#strings)
- [Tableaux](#arrays)
- [Date et heure](#time)

### Booléens (vrai/faux) {#booleans}

Les attributs booléens sont utiles pour stocker des données binaires simples sur vos utilisateurs, comme les statuts d'abonnement. Vous pouvez trouver les utilisateurs qui ont explicitement une variable définie à une valeur vraie ou fausse, en plus de ceux qui n'ont aucun enregistrement de cet attribut enregistré.

| Options de segmentation                                                                                                           | Filtre de liste déroulante | Input Options                                                     |
| --------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ----------------------------------------------------------------- |
| Vérifiez si la valeur booléenne __est__ soit vraie, fausse, vraie, non définie, soit non définie, soit non définie ou non définie | __EST__                    | __TRUE__, __FALSE__, __VRAI OU PAS SET__, ou __FALSE OU PAS SET__ |
| Vérifier si la valeur booléenne __existe__ sur le profil d'un utilisateur                                                         | __N'EST PAS BLANQUE__      | __N/A__                                                           |
| Vérifier si la valeur booléenne __n'existe pas__ sur le profil d'un utilisateur                                                   | __EST BLANQUE__            | __N/A__                                                           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Numéros {#numbers}

Les attributs numériques incluent [entiers](https://en.wikipedia.org/wiki/Integer) et [floats](https://en.wikipedia.org/wiki/Floating-point_arithmetic), et ont une grande variété de cas d'utilisation. L'augmentation des nombres d'attributs personnalisés sont utiles pour stocker le nombre de fois qu'une action donnée ou un événement s'est produite sans compter la limite de vos données. Les nombres standards ont toutes sortes d'utilisations, telles que l'enregistrement:

- Taille de chaussure
- Taille de la taille
- Nombre de fois qu'un utilisateur a consulté une certaine caractéristique de produit, ou une catégorie

{% alert tip %}
L'argent dépensé ne devrait pas être enregistré par cette méthode. Il devrait plutôt être enregistré via nos [méthodes d'achat](#purchase-revenue-tracking).
{% endalert %}

| Options de segmentation                                                          | Filtre de liste déroulante | Input Options |
| -------------------------------------------------------------------------------- | -------------------------- | ------------- |
| Vérifier si l'attribut numérique __est plus que__ un __numéro__                  | __PLUS PAR__               | __NOMBRE__    |
| Vérifie si l'attribut numérique __est inférieur à__ un nombre ____               | __MOINS QUE__              | __NOMBRE__    |
| Vérifier si l'attribut numérique __est exactement__ un numéro ____               | __EXACTEMENT__             | __NOMBRE__    |
| Vérifier si l'attribut numérique __ne correspond pas à__ un nombre ____          | __N'EST PAS EQUALE__       | __NOMBRE__    |
| Vérifier si l'attribut numérique __existe__ sur le profil d'un utilisateur       | __EXISTES__                | __N/A__       |
| Vérifier si l'attribut numérique __n'existe pas__ sur le profil d'un utilisateur | __N'EXISTE PAS__           | __N/A__       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Chaînes de caractères (caractères alphanumériques) {#strings}

Les attributs de chaînes de caractères sont utiles pour stocker les entrées de l'utilisateur, comme une marque préférée, un numéro de téléphone ou une dernière chaîne de recherche dans votre application. Les attributs de chaîne de caractères peuvent contenir jusqu'à 256 caractères.

| Options de segmentation                                                                                                 | Filtre de liste déroulante | Input Options                              |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------------------------------------------ |
| Vérifie si l'attribut chaîne __correspond exactement à__ une chaîne de caractères saisie                                | __EQUALES__                | __STRING__                                 |
| Vérifie si l'attribut chaîne __correspond partiellement à__ une chaîne entrée __OU__ une expression régulière           | __REGEX DE MATCHES__       | __STRING__ __OU__ __EXPRESSION REGULAIRE__ |
| Vérifie si l'attribut de chaîne __ne correspond pas partiellement à__ une chaîne entrée __OU__ une expression régulière | __NE MATCH PAS REGEX__*    | __STRING__ __OU__ __EXPRESSION REGULAIRE__ |
| Vérifie si l'attribut de chaîne __ne correspond pas à__ une chaîne de caractères saisie                                 | __N'EST PAS EQUALE__       | __STRING__                                 |
| Vérifier si l'attribut chaîne __existe__ sur le profil d'un utilisateur                                                 | __N'EST PAS BLANQUE__      | __N/A__                                    |
| Vérifier si l'attribut chaîne __n'existe pas__ sur le profil d'un utilisateur                                           | __BLANQUE__                | __N/A__                                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Une chaîne de date telle que "12-1-2021" ou "12/1/2021" sera convertie en un objet datetime et traitée comme un attribut [time]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% alert important %}
Lors de la segmentation en utilisant le filtre __NE MATCH REGEX PAS__ , vous devez déjà avoir un attribut personnalisé avec une valeur assignée dans ce profil utilisateur. Braze suggère d'utiliser la logique "OU" pour vérifier si un attribut personnalisé est vide pour s'assurer que les utilisateurs sont correctement ciblés.<br>

Plus de ressources en regex:
- [Regex avec Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Débogueur et testeur Regex](https://regex101.com/)
- [Tutoriel Regex](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Tableaux {#arrays}

Les attributs des tableaux sont bons pour stocker des listes d'information connexes sur vos utilisateurs. Par exemple, stocker les 100 dernières parties de contenu qu'un utilisateur regardé dans un tableau permettrait de segmenter un intérêt spécifique.

Par défaut, la longueur maximale d'un tableau pour un attribut est définie à 25. Par exemple, si vous envoyez sur un attribut tel que "Films regardés" et qu'il est défini à 25, lorsqu'un utilisateur regarde un 26e film, le premier film sera retiré du tableau et le film le plus récent sera ajouté.

Le maximum pour chaque tableau peut être augmenté à 100. Si vous souhaitez augmenter ce maximum, veuillez contacter votre responsable du service à la clientèle.

| Options de segmentation                                                                                                             | Filtre de liste déroulante    | Input Options                              |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------ |
| Vérifier si l'attribut tableau __inclut une valeur qui correspond exactement à__ une valeur entrée                                  | __VALEUR INCLUDES__           | __STRING__                                 |
| Vérifier si l'attribut tableau __n'inclut pas une valeur qui correspond exactement à__ une valeur entrée                            | __NE PAS INCLUTER LA VALEUR__ | __STRING__                                 |
| Vérifier si l'attribut tableau __contient une valeur qui correspond partiellement à__ une valeur entrée __OU__ Expression régulière | __REGEX DE MATCHES__          | __STRING__ __OU__ __EXPRESSION REGULAIRE__ |
| Vérifier si l'attribut tableau __a une valeur__                                                                                     | __A UNE VALEUR__              | __N/A__                                    |
| Vérifier si l'attribut tableau __est vide__                                                                                         | __VIDE__                      | __N/A__                                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
Pour plus d'informations sur l'utilisation de notre filtre d'expressions régulières, consultez cette documentation sur [les expressions régulières compatibles Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
Plus de ressources en regex:
- [Regex avec Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Débogueur et testeur Regex](https://regex101.com/)
- [Tutoriel Regex](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Date et heure {#time}

Les attributs de temps sont utiles pour stocker la dernière fois qu'une action spécifique a été prise, de sorte que vous pouvez offrir des messages de réengagement spécifiques au contenu à vos utilisateurs.

Les filtres de temps utilisant des dates relatives (par exemple, il y a plus de 1 jour, il y a moins de 2 jours) mesurent une journée à 24 heures. Toute campagne que vous exécutez en utilisant ces filtres inclura tous les utilisateurs par incréments de 24 heures. Par exemple, `la dernière application utilisée il y a plus de 1 jour` capturera tous les utilisateurs qui "ont utilisé l'application pour la dernière fois plus de 24 heures" à partir de la période d'exécution de la campagne. Il en va de même pour les campagnes avec des plages de dates plus longues, donc cinq jours à partir de l'activation signifieront les 120 heures précédentes.

Par exemple, pour construire un segment qui cible les utilisateurs avec un attribut de temps entre 24 et 48 heures dans le futur, appliquer les filtres `dans plus d'un jour dans le futur` et `dans moins de 2 jours dans le futur`.

{% alert warning %}
La dernière date qu'un événement personnalisé ou un événement d'achat s'est produit est automatiquement enregistré et ne doit pas être enregistré à nouveau via un attribut de temps personnalisé.
{% endalert %}

| Options de segmentation                                                           | Filtre de liste déroulante | Input Options                      |
| --------------------------------------------------------------------------------- | -------------------------- | ---------------------------------- |
| Vérifier si l'attribut horaire __est avant__ une __date sélectionnée__            | __AVANT__                  | __SELECTEUR DE DATE DE CALENDEUR__ |
| Vérifier si l'attribut horaire __est après__ une __date sélectionnée__            | __APRES__                  | __SELECTEUR DE DATE DE CALENDEUR__ |
| Vérifie si l'attribut de temps est __plus que X nombre__ de __jours il y a__      | __PLUS PAR__               | __NOMBRE DES JOURS AGO__           |
| Vérifier si l'attribut de temps est __inférieur à X__ il y a __jours__            | __MOINS QUE__              | __NOMBRE DES JOURS AGO__           |
| Vérifier si l'attribut de temps est __dans plus de X__ de __jours dans le futur__ | __EN PLUS QUE__            | __NOMBRE DE JOURS EN FUTURE__      |
| Vérifie si l'attribut de temps est __inférieur à X__ de __jours dans le futur__   | __EN MOINS QUE__           | __NOMBRE DE JOURS EN FUTURE__      |
| Vérifier si l'attribut temporel __existe__ sur le profil d'un utilisateur         | __EXISTES__                | __N/A__                            |
| Vérifier si l'attribut de temps __n'existe pas__ sur le profil d'un utilisateur   | __N'EXISTE PAS__           | __N/A__                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Détails de l'attribut de temps

- Jour de l'événement récurrent
  - Lorsque vous utilisez le filtre "Jour de l'événement récurrent", et sont ensuite invités à sélectionner le "Calendrier de l'événement récurrent", si vous sélectionnez `EST PLUS DE` ou `EST PLUS DE`, la date courante sera comptée pour ce filtre de segmentation.
  - Par exemple, si le 10 mars 2020, vous avez sélectionné la date de l'attribut à être `moins que ... 10 mars 2020`, les attributs seront pris en compte pour les jours qui suivent et y compris le 10 mars 2020.
- Moins de X Jours Ago: Le filtre "Moins de X Jours Ago" inclut des dates entre X jours auparavant et la date/heure courante.
- Moins de X jours dans le futur : Inclut les dates entre la date/heure actuelle et X jours dans le futur.

## Suivi des achats et des revenus {#purchase-revenue-tracking}

L'utilisation de nos méthodes d'achat pour enregistrer les achats dans l'application établit la valeur à vie (LTV) pour chaque profil utilisateur individuel. Ces données sont visibles dans notre page de revenus en séries temporelles.

| Options de segmentation                                                           | Filtre de liste déroulante | Input Options                                      |
| --------------------------------------------------------------------------------- | -------------------------- | -------------------------------------------------- |
| Vérifie si le nombre total de dollars dépensés __est supérieur à__ un __nombre__  | __PLUS GRAND QUE__         | __NOMBRE__                                         |
| Vérifie si le nombre total de dollars dépensés __est inférieur à__ un __nombre__  | __MOINS QUE__              | __NOMBRE__                                         |
| Vérifier si le nombre total de dollars dépensés __est exactement__ un numéro ____ | __EXACTEMENT__             | __NOMBRE__                                         |
| Vérifier si l'achat a eu lieu la dernière fois __après la date X__                | __APRES__                  | __HEURE__                                          |
| Vérifier si l'achat a eu lieu la dernière fois __avant la date X__                | __AVANT__                  | __HEURE__                                          |
| Vérifier si l'achat a eu lieu pour la dernière fois __il y a plus de X jours__    | __PLUS PAR__               | __HEURE__                                          |
| Vérifier si l'achat a eu lieu la dernière fois __il y a moins de X jours__        | __MOINS QUE__              | __HEURE__                                          |
| Vérifier si l'achat a eu lieu __plus de X (Max = 50) nombre de fois__             | __PLUS PAR__               | dans les __derniers jours Y (Y = 1,3,7,14,21,30)__ |
| Vérifier si l'achat a eu lieu __moins de X (Max = 50) nombre de fois__            | __MOINS QUE__              | dans les __derniers jours Y (Y = 1,3,7,14,21,30)__ |
| Vérifier si l'achat a eu lieu __exactement X (Max = 50) nombre de fois__          | __EXACTEMENT__             | dans les __derniers jours Y (Y = 1,3,7,14,21,30)__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
Si vous souhaitez segmenter le nombre de fois qu'un achat spécifique a eu lieu, vous devriez également enregistrer cet achat individuellement en tant qu'attribut [incrémentant personnalisé]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes).
{% endalert %}

Vous pouvez modifier le type de données de votre attribut personnalisé, mais vous devez être conscient de [ce que d'autres changements cette action implique]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/).

