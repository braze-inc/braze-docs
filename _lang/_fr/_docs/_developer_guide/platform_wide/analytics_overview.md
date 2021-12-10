---
nav_title: Vue d'ensemble de l'analyse
article_title: Vue d'ensemble de l'analyse
page_order: 2
description: "Cet article de référence couvre la collecte de données des utilisateurs, y compris les données qui sont automatiquement collectées, les événements d'achat et les événements personnalisés, ainsi que les meilleures pratiques de collecte de données."
---

# Collecte de données utilisateur

Avant de terminer votre mise en œuvre de Braze, assurez-vous d'avoir une conversation entre votre équipe de marketing et votre équipe de développement au sujet de vos objectifs de marketing. Lorsque vous décidez de ce que vous voulez suivre, et comment vous voulez le suivre avec Braze, Il est utile de considérer ces objectifs et de revenir en arrière. Veuillez consulter notre cas d'une [application Taxi/Ride-Sharing][16] à la fin de ce guide pour un exemple de ce processus.

Ce guide des meilleures pratiques vous aidera à comprendre exactement ce que Braze considère comme un "événement personnalisé" ou un "attribut personnalisé".

## Données collectées automatiquement

Les événements et attributs suivants sont capturés et mis à jour automatiquement par le SDK Braze dans le cadre des données de début de session et de fin de session ou par le backend de Braze. Vous n'avez pas besoin de les enregistrer séparément en tant qu'événements personnalisés ou attributs personnalisés. Si vous souhaitez mettre en liste blanche les processus qui bloquent la collecte par défaut de certains éléments de données (non suggéré), consultez notre [SDK Primer]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/).

#### Informations d'utilisation
- Première application utilisée (heure)
- Dernière application utilisée (heure)
- Nombre total de sessions (Nombre)
- Nombre d'éléments de retour d'expérience (nombre)
- Nombre de sessions dans les Y derniers jours (nombre et heure)
- E-mail disponible (Booléen)
- Nombre de nouvelles vues du flux (nombre)

#### Repositionnement de la campagne
- Dernier message reçu (fois)
- Dernière campagne d'email reçue (fois)
- Dernière campagne de push reçue (fois)
- Dernier fil d'actualité (fois)
- Carte cliquée (Nombre)
- Message reçu de la campagne
  - Ce filtre vous permet de cibler les utilisateurs en fonction de leur réception (non) d'une campagne précédente.
- Message reçu de la Campagne avec Tag
  - Ce filtre vous permet de cibler les utilisateurs en fonction de leur avoir (non) reçu une campagne qui a actuellement un tag.
- Campagne de redistribution
  - Ce filtre vous permet de cibler les utilisateurs en fonction de leur ouverture, ou cliquez sur un message spécifique dans l'application, ou sur un message spécifique dans le passé

#### Informations sur l'appareil
- Emplacement disponible (Booléen)
- Localisation la plus récente (si l'autorisation de localisation est accordée à votre application)
- Push activé (Boolean)
- Localisation de l'appareil
- Langue (prise à partir de la locale de l'appareil)
- Pays (première prise à partir de l'adresse IP. Si ce n'est pas disponible, pris de la locale de l'appareil)
- Version de l'application la plus récente
- Modèle de l'appareil
- Version du système d'exploitation de l'appareil
- Résolution de l'appareil
- Opérateur sans fil de l'appareil
- Fuseau horaire de l'appareil
- Identifiant de l'appareil
- Désinstallé (Temps et Booléen)

## Événements personnalisés

Les événements personnalisés sont des actions prises par vos utilisateurs ; ils sont les mieux adaptés pour suivre les interactions utilisateur de grande valeur avec votre application. La journalisation d'un événement personnalisé peut déclencher n'importe quel nombre de campagnes de suivi avec des délais configurables, et active les filtres de segmentation suivants autour de la récurrence et de la fréquence de cet événement :

| Options de segmentation                                                                             | Filtre de liste déroulante | Input Options                                      |
| --------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------------------------------- |
| Vérifie si l'événement personnalisé s'est produit __plus de X fois__                                | __PLUS PAR__               | __NOMBRE__                                         |
| Vérifie si l'événement personnalisé s'est produit __moins de X fois__                               | __MOINS QUE__              | __NOMBRE__                                         |
| Vérifie si l'événement personnalisé s'est produit __exactement X fois__                             | __EXACTEMENT__             | __NOMBRE__                                         |
| Vérifie si l'événement personnalisé s'est produit pour la dernière fois __après la date X__         | __APRES__                  | __HEURE__                                          |
| Vérifie si l'événement personnalisé s'est produit pour la dernière fois __avant la date X__         | __AVANT__                  | __HEURE__                                          |
| Vérifie si l'événement personnalisé s'est produit pour la dernière fois __il y a plus de X jours__  | __PLUS PAR__               | __NOMBRE DE JOURS AGO__ (Numéro Positif)           |
| Vérifie si l'événement personnalisé s'est produit pour la dernière fois __il y a moins de X jours__ | __MOINS QUE__              | __NOMBRE DE JOURS AGO__ (Numéro Positif)           |
| Vérifie si l'événement personnalisé s'est produit __plus de X (Max = 50) nombre de fois__           | __PLUS PAR__               | dans les __derniers jours Y (Y = 1,3,7,14,21,30)__ |
| Vérifie si l'événement personnalisé s'est produit __moins de X (max = 50) nombre de fois__          | __MOINS QUE__              | dans les __derniers jours Y (Y = 1,3,7,14,21,30)__ |
| Vérifie si l'événement personnalisé s'est produit __exactement X (max = 50) nombre de fois__        | __EXACTEMENT__             | dans les __derniers jours Y (Y = 1,3,7,14,21,30)__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Braze note le nombre de fois où ces événements se sont produits ainsi que la dernière fois qu'ils ont été exécutés par chaque utilisateur pour la segmentation. Sur la page d'analyse **Événements personnalisés** vous pouvez voir dans l'agrégat la fréquence à laquelle chaque événement personnalisé se produit, ainsi que par segment au fil du temps pour une analyse plus détaillée. Ceci est particulièrement utile pour voir comment vos campagnes ont affecté l'activité de l'événement personnalisé en regardant les lignes grises que Braze superpose sur la série temporelle pour indiquer la dernière fois qu'une campagne a été envoyée.

!\[custom_event_analytics_example.png\]\[8\]

> [L'incrémentation d'attributs personnalisés][10] peut être utilisée pour garder un compteur sur une action utilisateur similaire à un événement personnalisé. Cependant, vous ne pourrez pas voir les données d'attributs personnalisés dans une série temporelle. Les actions de l'utilisateur qui n'ont pas besoin d'être analysées dans des séries temporelles doivent être enregistrées via cette méthode.

### Stockage d'événements personnalisés

Toutes les données du profil utilisateur (événements personnalisés, attributs personnalisés, données personnalisées) sont stockées tant que ces profils sont actifs. Les propriétés personnalisées des événements sont stockées et disponibles pour la Segmentation pendant trente (30) jours. Si vous souhaitez tirer parti des propriétés de l'événement pour Segmentation, veuillez contacter votre Responsable de compte Braze ou Responsable du Service Client.

### Propriétés personnalisées de l'événement

Avec des propriétés événementielles personnalisées, Braze vous permet de définir des propriétés sur des événements personnalisés et des achats. Ces propriétés peuvent ensuite être utilisées pour de nouvelles conditions de déclenchement qualifiantes, pour augmenter la personnalisation de la messagerie et pour générer des analyses plus sophistiquées grâce à l'exportation de données brutes. Les valeurs de la propriété peuvent être des objets de chaîne, de numéro, de booléen ou de temps. Cependant, les valeurs de propriété ne peuvent pas être des objets de tableau.

Par exemple, si une application eCommerce voulait envoyer un message à un utilisateur lorsqu'il abandonne son panier, il pourrait également améliorer son public cible et permettre une personnalisation accrue de la campagne en ajoutant une propriété événement personnalisée de la 'valeur du panier' des paniers.

!\[customEventProperties.png\]\[18\]

Les propriétés d'événements personnalisés peuvent également être utilisées pour la personnalisation dans le modèle de messagerie. Toute campagne utilisant \[Livraison à l'aide d'action\]\[19\] avec un événement déclencheur peut utiliser des propriétés d'événement personnalisées de cet événement pour la personnalisation de la messagerie. Si une application de jeu voulait envoyer un message aux utilisateurs qui avaient terminé un niveau, il pourrait mieux personnaliser le message avec une propriété pour le temps qu'il a fallu aux utilisateurs pour compléter ce niveau. Dans cet exemple, le message est personnalisé pour trois segments différents en utilisant \[la logique conditionnelle\]\[18\].  La propriété événement personnalisée appelée `time_spent`, peut être incluse dans le message en appelant `{% raw %} {{event_properties.${time_spent}}} {% endraw %}`.

!\[custom_event_properties_gaming.png\]\[19\]{: style="max-width:75%;"}

Les propriétés personnalisées de votre événement sont conçues pour vous aider à personnaliser votre messagerie ou à créer des campagnes de livraison granulaires basées sur des actions. Si vous souhaitez créer des segments en fonction de la récurrence et de la fréquence des propriétés de l'événement, veuillez contacter votre Customer Success Manager ou notre équipe d'assistance, car cela peut entraîner des coûts de données supplémentaires.

## Attributs personnalisés
Les attributs personnalisés sont les meilleurs pour stocker des attributs à propos de vos utilisateurs, ou des informations sur les actions à faible valeur dans votre application. Vous devez garder à l'esprit que nous ne stockons pas les informations de séries temporelles pour les attributs personnalisés, donc vous n'allez pas obtenir de graphes basés sur eux comme l'exemple ci-dessus pour les événements personnalisés.

### Stockage d'attributs personnalisés

Toutes les données du profil utilisateur (événements personnalisés, attributs personnalisés, données personnalisées) sont stockées tant que ces profils sont actifs. Les propriétés personnalisées des événements sont stockées et disponibles pour la Segmentation pendant trente (30) jours. Si vous souhaitez tirer parti des propriétés de l'événement pour Segmentation, veuillez contacter votre Responsable de compte Braze ou Responsable du Service Client.

### Types de données d'attributs personnalisés
Les attributs personnalisés sont des outils extraordinairement flexibles qui permettent un meilleur ciblage. Les types de données suivants peuvent être stockés en tant qu'attributs personnalisés :

#### Chaînes de caractères (caractères alphanumériques)
Les attributs de chaînes de caractères sont utiles pour stocker les entrées de l'utilisateur, comme une marque préférée, un numéro de téléphone ou une dernière chaîne de recherche dans votre application. Les attributs de chaîne de caractères peuvent contenir jusqu'à 256 caractères.

| Options de segmentation                                                                                                 | Filtre de liste déroulante | Input Options                              |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------------------------------------------ |
| Vérifie si l'attribut chaîne __correspond exactement à__ une chaîne de caractères saisie                                | __EQUALES__                | __STRING__                                 |
| Vérifie si l'attribut chaîne __correspond partiellement à__ une chaîne entrée __OU__ une expression régulière           | __REGEX DE MATCHES__       | __STRING__ __OU__ __EXPRESSION REGULAIRE__ |
| Vérifie si l'attribut de chaîne __ne correspond pas partiellement à__ une chaîne entrée __OU__ une expression régulière | __NE MATCH PAS REGEX__*    | __STRING__ __OU__ __EXPRESSION REGULAIRE__ |
| Vérifie si l'attribut de chaîne __ne correspond pas à__ une chaîne de caractères saisie                                 | __N'EST PAS EQUALE__       | __STRING__                                 |
| Vérifier si l'attribut chaîne __existe__ sur le profil d'un utilisateur                                                 | __EST BLANQUE__            | __N/A__                                    |
| Vérifier si l'attribut chaîne __n'existe pas__ sur le profil d'un utilisateur                                           | __N'EST PAS BLANQUE__      | __N/A__                                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
&#42; Lors de la segmentation en utilisant le filtre __NE MATCH PAS DE REGEX__ , il est nécessaire qu'il existe déjà un attribut personnalisé avec une valeur assignée dans ce profil d'utilisateur. Braze suggère d'utiliser la logique "OU" pour vérifier si un attribut personnalisé est vide afin de s'assurer que les utilisateurs sont correctement ciblés.
{% endalert %}

{% alert tip %}
Pour plus d'informations sur l'utilisation de notre filtre d'expressions régulières, consultez cette documentation sur [les expressions régulières compatibles Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
Plus de ressources en regex:
- [Regex avec Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Débogueur et testeur Regex](https://regex101.com/)
- [Tutoriel Regex](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

#### Tableaux
Les attributs des tableaux sont bons pour stocker des listes d'information connexes sur vos utilisateurs. Par exemple, stocker les 100 dernières parties de contenu qu'un utilisateur regardé dans un tableau permettrait de segmenter un intérêt spécifique.

Les tableaux d'attributs personnalisés sont des ensembles unidimensionnels; les tableaux multidimensionnels ne sont pas pris en charge. __Ajout d'un élément à un attribut personnalisé tableau ajoute l'élément à la fin de la table, sauf si elle est déjà présente, auquel cas elle est déplacée de sa position courante à la fin du tableau.__ Par exemple, si une table `['hotdog','hotdog','hotdog','hotdog','pizza']` a été importée, il affichera dans l'attribut tableau comme `['hotdog', 'pizza']` car seules les valeurs uniques sont prises en charge.

Si le tableau contient son nombre maximum d'éléments, le premier élément sera supprimé et le nouvel élément ajouté à la fin. Voici un exemple de code montrant le comportement du tableau dans le SDK web:

```
var abUser = appboy.getUser();
// initialise un tableau pour cet utilisateur, en supposant que la longueur maximale des favorite_foods est définie à 4.
abUser.setCustomUserAttribute('favorite_foods', ['pizza', 'wings', 'pasta']); // => ['pizza', 'wings', 'pasta']
abUser.addToCustomAttributeArray('favorite_foods', 'fries'); // => ['pizza', 'wings', 'pasta', 'frites ']
abUser. ddToCustomAttributeArray('favite_foods', 'pizza'); // => ['wings', 'pasta', 'frite', 'pizza']
abUser.addToCustomAttributeArray('favite_foods', 'ice cream'); // => ['pasta', 'frites', 'pizza', 'ice cream']

```

Le nombre maximum d'éléments dans les tableaux d'attributs personnalisés est par défaut de 25. Le maximum pour chaque tableau peut être augmenté jusqu'à 100. Si vous souhaitez augmenter ce maximum, veuillez contacter votre responsable du service à la clientèle. Les tableaux dépassant le nombre maximum d'éléments seront tronqués pour contenir le nombre maximum d'éléments.

| Options de segmentation                                                                                                             | Filtre de liste déroulante    | Input Options                              |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------ |
| Vérifier si l'attribut tableau __inclut une valeur qui correspond exactement à__ une valeur entrée                                  | __VALEUR INCLUDES__           | __STRING__                                 |
| Vérifier si l'attribut tableau __n'inclut pas une valeur qui correspond exactement à__ une valeur entrée                            | __NE PAS INCLUTER LA VALEUR__ | __STRING__                                 |
| Vérifier si l'attribut tableau __contient une valeur qui correspond partiellement à__ une valeur entrée __OU__ Expression régulière | __REGEX DE MATCHES__          | __STRING__ __OU__ __EXPRESSION REGULAIRE__ |
| Vérifier si l'attribut tableau __a une valeur__                                                                                     | __A UNE VALEUR__              | __N/A__                                    |
| Vérifier si l'attribut tableau __est vide__                                                                                         | __VIDE__                      | __N/A__                                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

> Nous utilisons [des expressions régulières compatibles Perl (PCRE)][11].

#### Dates
Les attributs de temps sont utiles pour stocker la dernière fois qu'une action spécifique a été prise, de sorte que vous pouvez offrir des messages de réengagement spécifiques au contenu à vos utilisateurs.

> La dernière date qu'un événement personnalisé ou un événement d'achat s'est produit est automatiquement enregistré, et ne doit pas être enregistré en double via un attribut de temps personnalisé.

Les filtres de date utilisant des dates relatives (par exemple, il y a plus de 1 jour, il y a moins de 2 jours) mesurent une journée à 24 heures. Toute campagne que vous exécutez en utilisant ces filtres inclura tous les utilisateurs en incréments de 24 heures. Par exemple, la dernière application utilisée il y a plus d'un jour capturera tous les utilisateurs qui "ont utilisé l'application pour la dernière fois plus de 24 heures" à partir de l'heure exacte où la campagne s'exécute. Il en va de même pour les campagnes avec des plages de dates plus longues – donc cinq jours à partir de l’activation signifieront les 120 heures précédentes.

| Options de segmentation                                                           | Filtre de liste déroulante | Input Options                      |
| --------------------------------------------------------------------------------- | -------------------------- | ---------------------------------- |
| Vérifier si l'attribut horaire __est avant__ une __date sélectionnée__            | __AVANT__                  | __SELECTEUR DE DATE DE CALENDEUR__ |
| Vérifier si l'attribut horaire __est après__ une __date sélectionnée__            | __APRES__                  | __SELECTEUR DE DATE DE CALENDEUR__ |
| Vérifie si l'attribut de temps est __plus que X nombre__ de __jours il y a__      | __PLUS PAR__               | __NOMBRE DES JOURS AGO__           |
| Vérifier si l'attribut de temps est __inférieur à X__ il y a __jours__            | __MOINS QUE__              | __NOMBRE DES JOURS AGO__           |
| Vérifier si l'attribut de temps est __dans plus de X__ de __jours dans le futur__ | __EN PLUS QUE__            | __NOMBRE DE JOURS EN FUTURE__      |
| Vérifie si l'attribut de temps est __inférieur à X__ de __jours dans le futur__   | __EN MOINS QUE__           | __NOMBRE DE JOURS EN FUTURE__      |
| Vérifier si l'attribut temporel __existe__ sur le profil d'un utilisateur         | __BLANQUE__                | __N/A__                            |
| Vérifier si l'attribut de temps __n'existe pas__ sur le profil d'un utilisateur   | __N'EST PAS BLANQUE__      | __N/A__                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Numéros {#integers}
Les attributs numériques ont une grande variété de cas d'utilisation. L'augmentation des nombres d'attributs personnalisés sont utiles pour stocker le nombre de fois qu'une action donnée ou un événement s'est produite. Les numéros standards ont toutes sortes d'usages, par exemple : enregistrer la taille des chaussures, la taille de la taille, ou le nombre de fois qu'un utilisateur a consulté une certaine fonctionnalité ou catégorie de produit.
> L'argent dépensé ne devrait pas être enregistré par cette méthode. Il devrait plutôt être enregistré via nos [méthodes d'achat][4].

| Options de segmentation                                                          | Filtre de liste déroulante | Input Options |
| -------------------------------------------------------------------------------- | -------------------------- | ------------- |
| Vérifier si l'attribut numérique __est plus que__ un __numver__                  | __PLUS PAR__               | __NUMVER__    |
| Vérifie si l'attribut numérique __est inférieur à__ un nombre ____               | __MOINS QUE__              | __NOMBRE__    |
| Vérifier si l'attribut numérique __est exactement__ un numéro ____               | __EXACTEMENT__             | __NOMBRE__    |
| Vérifier si l'attribut numérique __ne correspond pas à__ un __numver__           | __N'EST PAS EQUALE__       | __NOMBRE__    |
| Vérifier si l'attribut numérique __existe__ sur le profil d'un utilisateur       | __EXISTES__                | __N/A__       |
| Vérifier si l'attribut numérique __n'existe pas__ sur le profil d'un utilisateur | __N'EXISTE PAS__           | __N/A__       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Booléens (vrai/faux)
Les attributs booléens sont utiles pour stocker les statuts d'abonnement, et d'autres données binaires simples à propos de vos utilisateurs. Les options d'entrée que nous vous fournissons vous permettent de trouver les utilisateurs qui ont explicitement une variable définie à une valeur vrai/faux en plus de celles qui n'ont pas encore enregistré d'enregistrement.

| Options de segmentation                                                         | Filtre de liste déroulante | Input Options                                                     |
| ------------------------------------------------------------------------------- | -------------------------- | ----------------------------------------------------------------- |
| Vérifie si la valeur booléenne __est__                                          | __EST__                    | __TRUE__, __FALSE__, __VRAI OU PAS SET__, ou __FALSE OU PAS SET__ |
| Vérifier si la valeur booléenne __existe__ sur le profil d'un utilisateur       | __EXISTES__                | __N/A__                                                           |
| Vérifier si la valeur booléenne __n'existe pas__ sur le profil d'un utilisateur | __N'EXISTE PAS__           | __N/A__                                                           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Évènements d'achat / suivi des revenus

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

> Si vous souhaitez segmenter le nombre de fois qu'un achat spécifique a eu lieu, vous devriez également enregistrer cet achat individuellement en tant qu'attribut [incrémentant personnalisé][12].

## Taxi/Taxi-Partage application cas d'utilisation {#example-case}
Dans ce cas, envisageons une application Taxi/Ride-Sharing (comme Hailo, Lyft, etc.) qui veut décider quelles données utilisateur collecter. Les questions et le processus de brainstorming ci-dessous sont un excellent modèle pour les équipes de marketing et de développement à suivre. À la fin de cet exercice, les deux équipes devraient avoir une bonne compréhension de ce que les événements et attributs personnalisés ont un sens à collecter afin de contribuer à atteindre leur objectif.

__Question du cas n°1 : Quel est le but ?__

Leur objectif est simple dans la mesure où ils veulent que les utilisateurs dénigrent les trajets en taxi via leur application.

__Question de cas #2 : Quelles sont les étapes intermédiaires sur la voie menant à cet objectif à partir de l'installation de l'application?__

1. Ils ont besoin que les utilisateurs commencent le processus d'inscription et remplissent leurs informations personnelles.
2. Ils ont besoin d’utilisateurs pour terminer & vérifier le processus d’inscription en entrant un code dans l’application qu’ils reçoivent par SMS.
3. Ils doivent essayer de haïr un taxi.
4. Pour accabler un taxi, il doit être disponible lors de sa recherche.

Les actions ci-dessus pourraient alors être marquées comme les événements personnalisés suivants :

- Début de l'inscription
- Inscription terminée
- Taxi Hails Réussi
- Chaussures de Taxi échouées

Après avoir implémenté les événements, vous pouvez maintenant exécuter les campagnes suivantes :

1. Envoyer un message aux utilisateurs qui débutent l'inscription, mais qui n'ont pas terminé l'inscription dans un certain laps de temps.
2. Envoyez des messages de félicitations aux utilisateurs qui complètent l'inscription.
3. Envoyez des excuses et des crédits promotionnels aux utilisateurs qui ont échoué dans la grêle de taxi, qui n'ont pas été suivis par une grêle de taxi réussie dans un certain temps.
4. Envoyez des promotions aux utilisateurs avec beaucoup de Taxi Hails qui ont réussi à les remercier pour leur loyauté.
5. Nombreux, beaucoup plus.

__Question de cas n°3 : Quelles autres informations souhaiterions-nous savoir sur nos utilisateurs qui informeront notre message ?__

- Qu'ils disposent ou non de crédits promotionnels?
- La note moyenne qu'ils donnent à leurs chauffeurs?
- Codes promo uniques pour l'utilisateur ?

Les caractéristiques ci-dessus pourraient alors être marquées comme les attributs personnalisés suivants :

- Solde de crédit promotionnel (Type décimal)
- Notation moyenne des chauffeurs (Type de nombre)
- Code promo unique (Type de chaîne de caractères)

Ajouter ces attributs vous permettrait d'envoyer des campagnes aux utilisateurs comme :

1. Rappelant aux utilisateurs qui n'ont pas utilisé l'application en 7 jours qui ont encore du crédit promotionnel sur leur compte qu'il est là et qu'ils devraient revenir sur l'application et l'utiliser !
2. Les utilisateurs de messagerie qui donnent de faibles notes pour obtenir des commentaires directs des clients pour voir pourquoi ils n'ont pas apprécié leurs trajets.
3. Utilisez nos [modèles de messages et fonctionnalités de personnalisation][17] pour faire glisser l'attribut de code promo unique vers la messagerie destinée aux utilisateurs.

## Meilleures pratiques

### Meilleures pratiques générales

#### Ne pas sursegmenter votre suivi

- Être plus générique vous aidera à cibler plus d'utilisateurs et à dessiner des divisions plus utiles entre les segments d'utilisateurs
- Par exemple, plutôt que de capturer un événement séparé pour regarder chacun des 50 films différents, il serait plus efficace de capturer simplement en regardant un film comme un événement
- Si vous avez dépassé le segment de vos données d'utilisateur, vos résultats perdront toute importance statistique et ne guideront pas le développement de votre application et de vos initiatives de marketing aussi efficacement
    - Vous allez "manquer la forêt pour les arbres" lors de l'évaluation des données des tendances utilisateur
    - Les événements doivent être liés directement à vos objectifs de marketing et de conversion

> Plusieurs actions utilisateur dans une application peuvent être marquées avec la même désignation d'événement ou d'attribut personnalisé. Ceci est utile lorsque vous voulez suivre quelque chose de manière générale comme "jouer une chanson" plutôt que d'enregistrer chaque chanson dans une application de musique comme un événement distinct et distinct.

### Développer les meilleures pratiques

#### Définir les identifiants d'utilisateur pour chaque utilisateur

Les identifiants d'utilisateur doivent être définis pour chacun de vos utilisateurs. Celles-ci doivent être inchangées et accessibles lorsqu'un utilisateur ouvre l'application. Nous __recommandons fortement__ de fournir cet identifiant car il vous permettra de :

- Suivez vos utilisateurs à travers vos appareils et plates-formes, améliorant la qualité de vos données comportementales et démographiques.
- Importez des données sur vos utilisateurs en utilisant notre [API de données utilisateur][9].
- Ciblez des utilisateurs spécifiques avec notre [API de messagerie][10] pour les messages généraux et transactionnels.

Les identifiants d'utilisateur doivent être de moins de 512 caractères et doivent être privés et ne pas être facilement obtenus (par exemple, pas une simple adresse e-mail ou un nom d'utilisateur). Si un tel identifiant n'est pas disponible, Braze attribuera un identifiant unique à vos utilisateurs, mais vous ne pourrez pas utiliser les fonctionnalités ci-dessus. Vous devriez éviter de définir des identifiants d'utilisateur pour les utilisateurs pour lesquels vous n'avez pas d'identifiant unique lié à eux en tant qu'individu. Passer un identificateur d'appareil n'offre aucun avantage par rapport aux offres automatiques d'utilisateurs anonymes de Braze par défaut. Voici quelques exemples d'identifiants d'utilisateurs appropriés et inappropriés.

Bonnes options pour les identifiants d'utilisateur :

- Adresse e-mail Hashed ou nom d'utilisateur unique
- Identifiant unique de la base de données
- ID Facebook

Celles-ci ne doivent pas être utilisées comme ID d'utilisateur :

- ID de l'appareil
- Nombre aléatoire ou ID de session
- N'importe quel ID non unique

{% include sdk_auth_alert.md %}

#### Donner des noms lisibles aux événements personnalisés et aux attributs
Imaginez que vous êtes un marketeur qui commence à utiliser Braze un an ou deux après l'implémentation, lire une liste déroulante pleine de noms comme "usr_no_acct" sans contexte supplémentaire peut être intimidant. Donner des noms identifiables et lisibles à vos événements et attributs facilitera la tâche à tous les utilisateurs de votre plateforme. Considérez les meilleures pratiques suivantes :

- Ne pas commencer un événement personnalisé avec un caractère numérique. La liste déroulante est triée par ordre alphabétique et commencer par un caractère numérique rend plus difficile le segment par votre filtre de choix
- Essayez de ne pas utiliser d'abréviations obscures ou de jargon technique si possible
  - Exemple: `usr_ctry` peut être un bon nom de variable pour le pays d'un utilisateur dans un morceau de code mais l'attribut personnalisé devrait être envoyé à Braze en tant que `user_country` au moins pour apporter de la clarté à un marketeur en utilisant le tableau de bord en bas de la ligne.

#### Ne loguer que les attributs lorsqu'ils changent
Nous comptons chaque attribut passé à Braze comme un point de données, même si l'attribut passé contient la même valeur que celle enregistrée précédemment. Seule la journalisation des données lorsque celles-ci changent aide à éviter l'utilisation de points de données redondants et garantit une expérience plus fluide en évitant les appels d'API inutiles.

#### Éviter les événements générés par programme
Si vous créez constamment de nouveaux noms d'événement, il sera impossible de segmenter significativement vos utilisateurs. Vous allez rencontrer les mêmes problèmes de segmentation que ceux décrits ci-dessus. De plus, les événements programmatiques personnalisés courent le risque de contenir plus de 255 caractères, ce qui est une contrainte placée sur les événements et les attributs (voir ci-dessous). Vous devriez généralement capturer des événements génériques (« Visionné une vidéo » ou « Lisez un article ») au lieu d'événements très spécifiques tels que (« Regarder le style Gangnam » ou « Lire l’article : les 10 meilleurs repas.

### Limites et contraintes techniques
Veuillez garder à l'esprit les limitations et contraintes suivantes lors de l'implémentation d'événements personnalisés :

#### Contraintes de longueur
Tous les événements personnalisés, les noms d'attributs personnalisés (clés) et les valeurs de chaîne d'événements personnalisés de 255 caractères ou plus seront tronqués. Idéalement, ils devraient être aussi courts que possible pour améliorer les performances du réseau et de la batterie de votre application. Si possible, limitez-les à 50 caractères.

#### Contraintes de contenu
Le contenu suivant sera découpé par programme de vos attributs et événements. Veillez à ne pas utiliser les éléments suivants :

- Espaces de départ et de fin
- Newlines
- Tous les non-chiffres dans les numéros de téléphone
  - Exemple: "(732) 178-1038" sera condensé à "7321781038"
- Les caractères non-blancs doivent être convertis en espaces
- $ ne doit pas être utilisé comme préfixe pour aucun événement personnalisé
- N'importe quelle valeur d'encodage UTF-8 invalide
  -  "Mon \x80 Champ" serait condensé à "Mon Champ"

#### Clés réservées
Avant iOS SDK version 3.0 et Android SDK version 2. , les clés suivantes sont __RESERVES__ et __NE PEUT PAS__ être utilisées comme attributs personnalisés :

- `Email`
- `facebook`
- `twitter`
- `prénom`
- `nom_de famille`
- `chien`
- `id externe`
- `Pays`
- `ville_domicile`
- `bio`
- `Sexe`
- `Téléphone`
- `Inscription par e-mail`
- `Poussez vous abonner`

De plus, les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d'événement personnalisées:

- `Heure`
- `identifiant_produit`
- `Quantité`
- `nom_événement`
- `prix`
- `Devise`

#### Cfinitions de la valeur

- Les valeurs entières sont 64 bits
- Les décimales ont 15 décimales par défaut

### Analyse d'un champ de nom générique

Si seul un seul champ de nom générique existe pour un utilisateur (par exemple 'JohnDoe'), vous pouvez assigner ce titre à l'attribut prénom de votre utilisateur. De plus, vous pouvez essayer d'analyser le prénom et le nom de famille de l'utilisateur en utilisant des espaces, mais cette dernière méthode comporte le risque potentiel de dénommer certains de vos utilisateurs.
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png" [18]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png" [19]: {% image_buster /assets/img_archive/custom_event_properties_gaming.png %} "custom_event_properties_gaming.png"

[4]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#purchase-events--revenue-tracking
[9]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[10]: {{site.baseurl}}/api/endpoints/messaging/
[10]: {{site.baseurl}}/api/endpoints/messaging/
[11]: http://www.regextester.com/pregsyntax.html
[12]: #integers
[16]: #example-case
[17]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/
