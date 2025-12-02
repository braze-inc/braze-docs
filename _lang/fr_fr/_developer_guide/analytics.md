---
nav_title: Analyse
article_title: "A propos de l'analyse/analytique pour le SDK de Braze (si utilisé comme adjectif)"
page_order: 2.6
description: "Découvrez les analyses du SDK Braze, afin de mieux comprendre quelles données Braze collecte, la différence entre les événements personnalisés et les attributs personnalisés, et les meilleures pratiques de gestion des analyses."
platform: 
  - Android
  - Swift
  - Web
  - Cordova
  - FireOS
  - Flutter
  - React Native
  - Roku
  - Unity
  - Unreal Engine
  - Xamarin
---

# Analyse

> Découvrez les analyses du SDK Braze, afin de mieux comprendre quelles données Braze collecte, la différence entre les événements personnalisés et les attributs personnalisés, et les meilleures pratiques de gestion des analyses.

{% alert tip %}
Lors de la mise en œuvre de Braze, n'oubliez pas de discuter des objectifs marketing avec votre équipe, afin de décider au mieux des données que vous souhaitez suivre et de la manière dont vous souhaitez les suivre avec Braze. Pour un exemple, consultez notre étude de cas sur l ['application Taxi/Ride-Sharing](#example-case) à la fin de ce guide.
{% endalert %}

## Données collectées automatiquement

Certaines données utilisateur sont collectées automatiquement par notre SDK, par exemple, Première application utilisée, Dernière application utilisée, Nombre total de sessions, Système d’exploitation de l’appareil, etc. Si vous suivez nos guides d'intégration pour mettre en œuvre nos SDK, vous pourrez profiter de cette [collecte de données par défaut]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/). Vérifier cette liste pour éviter de stocker plusieurs fois les mêmes informations sur les utilisateurs. À l’exception du début et de la fin de session, toutes les autres données automatiquement suivies ne sont pas prises en compte dans votre compte de points de données.

Consultez notre article sur [l’amorce SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/) pour établir une liste des processus qui bloquent la collecte par défaut de certains éléments de données.

## Événements personnalisés

Les événements personnalisés sont des actions effectuées par vos utilisateurs ; ils conviennent mieux pour le suivi des interactions utilisateur de grande valeur avec votre application. L’enregistrement d’un événement personnalisé peut déclencher un nombre quelconque de campagnes de suivi avec des délais configurables et permet aux filtres de segmentation suivants de filtrer la fréquence et la dernière occurrence de cet événement :

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si l'événement personnalisé s'est produit **plus de X fois.** | **PLUS DE** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit **moins de X fois.** | **MOINS DE** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit **exactement X fois.** | **EXACTEMENT** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **après la date X** | **APRÈS** | **DATE** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **avant la date X** | **AVANT** | **DATE** |
| Vérifier si l’événement personnalisé s’est produit pour la dernière fois **il y a plus de X jours** | **PLUS DE** | **Nombre de jours écoulés** (positif) Nombre) |
| Vérifier si l’événement personnalisé s’est produit pour la dernière fois **il y a moins de X jours** | **MOINS DE** | **Nombre de jours écoulés** (positif) Nombre) |
| Vérifier si l’événement personnalisé s’est produit **plus de X (max = 50) fois** | **PLUS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l’événement personnalisé s’est produit **moins de X (max = 50) fois** | **MOINS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l'événement personnalisé s'est produit **exactement X (Max = 50) fois.** | **EXACTEMENT** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze indique le nombre de fois où ces événements ont eu lieu ainsi que la dernière fois qu’ils ont été exécutés par chaque utilisateur pour la segmentation. Sur la page d'analyse/analytique des **événements personnalisés**, vous pouvez visualiser la fréquence de chaque événement personnalisé de manière globale, ainsi que par segment au fil du temps pour une analyse plus détaillée. Ceci est particulièrement utile pour voir comment vos campagnes ont affecté les événements personnalisés, en regardant les lignes grises placées par Braze sur la série temporelle pour indiquer la dernière fois qu’une campagne a été envoyée.

![Un graphique d'analyse des événements personnalisés montrant des statistiques sur les utilisateurs qui ont ajouté une carte de crédit et effectué une recherche sur une période de trente jours.]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

{% alert note %}
L'[incrémentation des attributs personnalisés]({{site.baseurl}}/api/endpoints/messaging/) peut être utilisée pour conserver un compteur sur une action de l'utilisateur similaire à un événement personnalisé. Cependant, vous ne pourrez pas afficher les données d’attribut personnalisées dans une série temporelle. Les actions de l’utilisateur qui ne doivent pas être analysées dans les séries temporelles doivent être enregistrées à l’aide de cette méthode.
{% endalert %}

### Stockage d’événements personnalisés

Toutes les données de profil utilisateur (événements personnalisés, attribut personnalisé, données personnalisées) sont stockées tant que ces profils sont actifs.

### Propriétés de l'événement  personnalisé

Avec des propriétés d’événement personnalisé, Braze vous permet de définir des propriétés sur des événements personnalisés et des achats. Ces propriétés peuvent ensuite être utilisées pour ajouter des conditions de déclenchement supplémentaires, améliorer le niveau de personnalisation des envois de messages et générer des analyses plus sophistiquées via l’exportation des données brutes. Les valeurs des propriétés peuvent être des chaînes de caractères, des nombres, des booléens ou des objets temporels. Cependant, les valeurs de propriété ne peuvent pas être des objets de type tableau.

Par exemple, si une application de commerce électronique souhaitait envoyer un message à un utilisateur lorsqu'il abandonne son panier, elle pourrait en outre améliorer son audience cible et permettre une personnalisation accrue de la campagne en ajoutant une propriété d'événement personnalisé de l'adresse `cart_value` des paniers des utilisateurs.

![Un exemple d'événement personnalisé qui enverra une campagne à un utilisateur qui a abandonné son panier et dont la valeur du panier est supérieure à 100 et inférieure à 200.]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

Les propriétés d'événement personnalisé peuvent également être utilisées pour personnaliser les messages. Toute campagne utilisant la [livraison par action]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) avec un événement déclencheur peut utiliser les propriétés d'événement personnalisées de cet événement pour la personnalisation des messages. Si un jeu souhaite envoyer un message aux utilisateurs qui ont terminé un niveau, il pourrait personnaliser le message avec une propriété pour le temps qu’il a fallu à l’utilisateur pour terminer le niveau. Dans cet exemple, le message est personnalisé pour trois segments différents à l'aide de la [logique conditionnelle]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/). La propriété d’événement personnalisée appelée ``time_spent`` peut être incluse dans le message en appelant ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Congratulations on beating that level so fast! Check out our online portal where you can play against top players fromm around the world!
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Talk to villagers for essential tips on how to beat levels!
{% endif %}
```
{% endraw %}

Les propriétés d’événement personnalisé sont conçues pour vous aider à personnaliser vos messages ou à élaborer des campagnes de diffusion granulaires à livraison par événement. Si vous souhaitez créer des segments basés sur la récence et la fréquence des propriétés d'événement, contactez votre gestionnaire de satisfaction client ou notre équipe d'assistance.

## Attributs personnalisés

Les attributs personnalisés sont des outils extraordinairement flexibles qui vous permettent de cibler les utilisateurs avec une plus grande spécificité que vous ne l’auriez avec les attributs standard. Les attributs personnalisés sont parfaits pour stocker des informations spécifiques à la marque à propos de vos utilisateurs. Gardez à l’esprit que nous ne stockons pas d’informations sur les séries temporelles pour les attributs personnalisés. Vous ne pourrez donc pas voir de graphiques basés sur ces attributs, comme dans l’exemple précédent pour les événements personnalisés.

### Stockage des attributs personnalisé

Toutes les données de profil utilisateur (événements personnalisés, attribut personnalisé, données personnalisées) sont stockées tant que ces profils sont actifs.

### Types de données des attributs personnalisés

Les types de données suivants peuvent être stockés en tant qu’attributs personnalisés :

#### Chaînes de caractères (caractères alphanumériques)

Les attributs au format string sont utiles pour stocker les entrées utilisateur, comme une marque préférée, un numéro de téléphone ou la dernière recherche dans votre application. Les attributs au format string peuvent avoir jusqu’à 255 caractères.

Le tableau suivant décrit les options de segmentation disponibles pour les attributs de chaîne de caractères.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si l'attribut string **correspond exactement à** une chaîne de caractères saisie| **ÉGAL À** | **CHAÎNE DE CARACTÈRES** |
| Vérifier si l'attribut chaîne de caractères **correspond partiellement à** une chaîne saisie **OU à** une expression régulière | **CORRESPOND À L’EXPRESSION RÉGULIÈRE** | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE** |
| Vérifier si l’attribut de chaîne de caractères **ne correspond pas partiellement** à une chaîne de caractères **OU** à une expression régulière saisie. | **NE CORRESPOND PAS À L'EXPRESSION RÉGULIÈRE** | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE** |
| Vérifier si l'attribut string **ne correspond pas à** une chaîne de caractères saisie| **N'EST PAS ÉGAL À** | **CHAÎNE DE CARACTÈRES** |
| Vérifier si l'attribut chaîne de caractères **existe** dans le profil d'un utilisateur | **EST BLANC** | **S.O.** |
| Vérifier si l'attribut chaîne de caractères **n'existe pas** dans le profil d'un utilisateur | **N'EST PAS VIDE** | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Lors de la segmentation à l'aide du filtre **DOES NOT MATCH REGEX**, il est nécessaire qu'il existe déjà un attribut personnalisé avec une valeur attribuée dans ce profil utilisateur. Braze suggère d'utiliser la logique "OU" pour vérifier si un attribut personnalisé est vide afin de cibler correctement les utilisateurs.
{% endalert %}

{% alert tip %}
Pour en savoir plus sur l'utilisation de notre filtre d'expressions régulières, consultez cette documentation sur les [expressions régulières compatibles avec Perl (PCRE).](http://www.regextester.com/pregsyntax.html)
<br>
Plus de ressources sur les expressions régulières :
- [Braze et les expressions régulières]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Débogueur et testeur d'expressions régulières](https://regex101.com/)
- [Tutoriel sur les expressions régulières](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

#### Tableaux

Les attributs de tableau sont appropriés pour stocker les listes d’informations associées à vos utilisateurs. Par exemple, le stockage en tableau des 100 derniers morceaux de contenu qu’un utilisateur a regardé permettrait une segmentation spécifique basée sur les intérêts.

Les tableaux d’attributs personnalisés sont des ensembles unidimensionnels ; les tableaux multidimensionnels ne sont pas pris en charge. **L’ajout d’un élément à un tableau d’attribut personnalisé ajoute l’élément à la fin du tableau, à moins qu’il ne soit déjà présent, auquel cas il passe de sa position actuelle à la fin du tableau.** Par exemple, si un tableau `['hotdog','hotdog','hotdog','pizza']` a été importé, il apparaîtra dans l’attribut de tableau comme `['hotdog', 'pizza']`, car seules des valeurs uniques sont prises en charge.

Si le tableau contient son nombre maximum d’éléments, le premier élément sera supprimé et le nouvel élément ajouté à la fin. Voici quelques exemples de code illustrant le comportement du tableau dans le SDK Web :

```js
var abUser = appboy.getUser();
// initialize array for this user, assuming max length of favorite_foods is set to 4.
abUser.setCustomUserAttribute('favorite_foods', ['pizza', 'wings', 'pasta']); // => ['pizza', 'wings', 'pasta']
abUser.addToCustomAttributeArray('favorite_foods', 'fries'); // => ['pizza', 'wings', 'pasta', 'fries']
abUser.addToCustomAttributeArray('favorite_foods', 'pizza'); // => ['wings', 'pasta', 'fries', 'pizza']
abUser.addToCustomAttributeArray('favorite_foods', 'ice cream'); // => ['pasta', 'fries', 'pizza', 'ice cream']
```

Le nombre maximum d’éléments dans les tableaux d’attributs personnalisés est par défaut de 25. Le maximum pour les tableaux individuels peut être augmenté jusqu’à 100 dans le tableau de bord de Braze, sous **Paramètres des données** > **Attributs personnalisés**. Si vous souhaitez que cette limite soit augmentée, contactez votre gestionnaire de services clients. Les tableaux dépassant le nombre maximum d’éléments seront tronqués pour contenir le nombre maximum d’éléments.

Le tableau suivant décrit les options de segmentation disponibles pour les attributs de tableau.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si l’attribut du tableau **inclut une valeur qui correspond exactement** à une valeur saisie| **INCLUT LA VALEUR** | **CHAÎNE DE CARACTÈRES** |
| Vérifier si l’attribut du tableau **n’inclut pas une valeur qui correspond exactement** à une valeur saisie| **NE COMPREND PAS DE VALEUR** | **CHAÎNE DE CARACTÈRES** |
| Vérifier si l'attribut du tableau **contient une valeur qui correspond partiellement** à une valeur saisie **OU** à une expression régulière | **CORRESPOND À L’EXPRESSION RÉGULIÈRE** | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE** |
| Vérifier si l'attribut du tableau **a une valeur** | **A UNE VALEUR** | **S.O.** |
| Vérifier si l'attribut du tableau **est vide** | **EST VIDE** | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Nous utilisons des [expressions régulières compatibles avec Perl (PCRE](http://www.regextester.com/pregsyntax.html)).
{% endalert %}

#### Dates

Les attributs de temps sont utiles pour stocker la dernière fois qu’une action spécifique a été prise, car ils vous permettent d’envoyer des contenus spécifiques  de ré-engagement dans vos envois de messages client.

{% alert note %}
La dernière date à laquelle un événement personnalisé ou événement d’achat s’est produit est automatiquement enregistrée et ne doit pas être enregistrée en double avec un attribut de temps personnalisé.
{% endalert %}

Les filtres de date utilisant des dates relatives (par exemple, il y a plus d'un jour, il y a moins de deux jours) mesurent 1 jour comme 24 heures. Toute campagne que vous exécutez à l’aide de ces filtres inclura tous les utilisateurs par incréments de 24 heures. Par exemple, l’option Dernière utilisation de l’application il y a plus d’un jour capturera tous les utilisateurs qui ont « utilisé l’application plus de 24 heures » à partir du lancement exact de la campagne. Il en va de même pour les campagnes définies avec des plages de dates plus longues. Ainsi, cinq jours après l’activation signifie les 120 heures précédentes.

Le tableau suivant décrit les options de segmentation disponibles pour les attributs de temps.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si l'attribut time **est antérieur à** une **date sélectionnée**| **AVANT** | **SÉLECTEUR DE DATE DU CALENDRIER** |
| Vérifier si l'attribut time **est postérieur à** une **date sélectionnée**| **APRÈS** | **SÉLECTEUR DE DATE DU CALENDRIER** |
| Vérifier si l'attribut time **date de plus** de **X jours** | **PLUS DE** | **NOMBRE DE JOURS ÉCOULÉS** |
| Vérifier si l’attribut de temps est **antérieur** à **il y a moins de X jours**| **MOINS DE** | **NOMBRE DE JOURS ÉCOULÉS** |
| Vérifier si l'attribut temporel se situe dans **plus de X jours** **dans le futur** | **DANS PLUS DE** | **NOMBRE DE JOURS À VENIR** |
| Vérifier si l'attribut temporel est **inférieur à un nombre X de** **jours dans le futur** | **EN MOINS DE** | **NOMBRE DE JOURS À VENIR**  |
| Vérifier si l'attribut time **existe** dans le profil d'un utilisateur | **VIDE** | **S.O.** |
| Vérifier si l'attribut time **n'existe pas** dans le profil d'un utilisateur | **N'EST PAS VIDE** | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Nombre {#integers}

Les attributs numériques incluent une grande variété de cas d’utilisation. Les attributs personnalisés basés sur un nombre incrémental sont utiles pour stocker le nombre de fois qu’une action ou un événement donné s’est produit. Les numéros standards sont destinés à toutes sortes d’usages, par exemple : enregistrer la taille des chaussures, le tour de taille, ou le nombre de fois qu’un utilisateur a consulté une certaine caractéristique ou catégorie de produit.

{% alert note %}
L’argent dépensé ne doit pas être enregistré via cette méthode. Il vaut mieux l’enregistrer via nos [méthodes d’achat]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#purchase-events--revenue-tracking).
{% endalert %}

Le tableau suivant décrit les options de segmentation disponibles pour les attributs numériques.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si l'attribut numérique **est plus qu'** un **nombre**| **PLUS DE** | **NOMBRE** |
| Vérifier si l'attribut numérique **est inférieur à** un **nombre**| **MOINS DE** | **NOMBRE** |
| Vérifier si l'attribut numérique **est exactement** un **nombre**| **EXACTEMENT** | **NOMBRE** |
| Vérifier si l'attribut numérique **n'est pas égal à** un **nombre**| **N'EST PAS ÉGAL À** | **NOMBRE** |
| Vérifier si l'attribut numérique **existe** dans le profil d'un utilisateur | **EXISTE** | **S.O.** |
| Vérifier si l'attribut numérique **n'existe pas** dans le profil d'un utilisateur | **N'EXISTE PAS** | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Booléen (vrai/faux)

Les attributs booléens sont utiles pour stocker des données binaires simples sur vos utilisateurs, comme le statut d’abonnement. Les options de saisie que nous proposons vous permettent de trouver des utilisateurs qui ont explicitement une variable définie sur booléen, en plus des personnes qui n’ont pas encore d’enregistrement pour cet attribut.

Le tableau suivant décrit les options de segmentation disponibles pour les attributs booléens.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si la valeur booléenne **est** | **EST**  | **VRAI**, **FAUX**, **VRAI OU NON ENREGISTRÉ**, ou **FAUX OU NON ENREGISTRÉ** |
| Vérifier si la valeur booléenne **existe** dans le profil d'un utilisateur. | **EXISTE**  | **S.O.** |
| Vérifier si la valeur booléenne **n'existe pas** dans le profil d'un utilisateur. | **N'EXISTE PAS**  | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Acheter des événements / suivi des revenus

L’utilisation de nos méthodes d’achat pour enregistrer les achats dans l’application établit la Valeur à vie (LTV) pour chaque profil utilisateur individuel. Ces données sont consultables sur notre page de revenus dans les graphiques de séries temporelles.

Le tableau suivant décrit les options de segmentation disponibles pour les événements d’achat.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si le nombre total de dollars dépensés **est supérieur à** **un nombre**| **SUPÉRIEUR À** | **NOMBRE** |
| Vérifier si le nombre total de dollars dépensés **est inférieur à** **un nombre**| **MOINS DE** | **NOMBRE** |
| Vérifier si le nombre total de dollars dépensés **est exactement** un **nombre**| **EXACTEMENT** | **NOMBRE** |
| Vérifiez si le dernier achat a eu lieu **après la date X** | **APRÈS** | **DATE** |
| Vérifiez si le dernier achat a eu lieu **avant la date X** | **AVANT** | **DATE** |
| Vérifier si l’achat a été effectué pour la dernière fois **il y a plus de X jours** | **PLUS DE** | **DATE** |
| Vérifier si l’achat a été effectué pour la dernière fois **il y a moins de X jours** | **MOINS DE** | **DATE** |
| Vérifiez si l'achat a eu lieu **plus de X (Max = 50) fois.** | **PLUS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifiez si l'achat a eu lieu **moins de X (Max = 50) fois.** | **MOINS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifiez si l'achat a eu lieu **exactement X (Max = 50) fois.** | **EXACTEMENT** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Si vous souhaitez segmenter le nombre de fois qu'un achat spécifique a été effectué, vous devez également enregistrer cet achat individuellement en tant qu'[attribut personnalisé incrémentiel.](#integers)
{% endalert %}

## Cas d’utilisation : application de taxi/covoiturage {#example-case}

Dans cet exemple, prenons une application de taxi/partage de trajets  qui décide quelles données utilisateur collecter. Le brainstorming et les questions suivantes sont un excellent modèle à suivre pour les équipes de marketing et de développement. À la fin de cet exercice, les deux équipes doivent avoir une solide compréhension des événements et attributs personnalisés qu’elles devraient collecter pour essayer d’atteindre leur objectif.

**Question n° 1 : Quel est l’objectif ?**

Leur objectif est simple : ils veulent que les utilisateurs fassent des trajets en taxi via leur application.

**Question n° 2 : Quelles sont les étapes intermédiaires sur la voie de l’installation de l’application ?**

1. Il faut que les utilisateurs commencent le processus d’inscription et donnent leurs informations personnelles.
2. Il faut que les utilisateurs confirment leur inscription en entrant un code reçu via SMS dans l’application.
3. Ils doivent essayer de commander un taxi.
4. Pour commander un taxi, il faut des taxis disponibles au moment de leur recherche.

Ces actions peuvent ensuite être des balises pour les événements personnalisés suivants :

- Inscription commencée
- Inscription terminée
- Appels de taxis réussis
- Appels de taxis échoués

Une fois que les événements ont été définis, vous pouvez maintenant exécuter les campagnes suivantes :

1. Envoyer des messages aux utilisateurs qui ont commencé l’enregistrement, sans le terminer dans un certain délai.
2. Envoyer des messages de félicitations aux utilisateurs qui se sont abonnés.
3. Envoyer des excuses et des remises aux utilisateurs qui n’ont pas réussi à avoir un taxi pour un trajet qui ne sont pas parvenus à avoir un taxi dans un certain délai.
4. Envoyer des remises aux utilisateurs qui ont pris de nombreux taxis pour les remercier leur fidélité.

Et bien plus encore !

**Question n° 3 : Quelles autres informations pourrions-nous connaître sur nos utilisateurs qui renseigneront nos envois de messages ?**

- Ont-ils ou non un crédit promotionnel ?
- La note moyenne qu’ils donnent à leurs chauffeurs ?
- Codes promotionnels uniques pour l’utilisateur ?

Ces caractéristiques peuvent ensuite être des balises  pour les attributs personnalisés suivants :

- Solde de crédit promotionnel (type décimal)
- Note moyenne du chauffeur (Type Entier)
- Code promotionnel unique (Type String)

L’ajout de ces attributs vous permettrait d’envoyer des campagnes aux utilisateurs, par exemple  :

1. Rappeler aux utilisateurs qui ne se sont pas connectés depuis 7 jours mais ayant un crédit promotionnel que leur crédit existe et qu’ils devraient réutiliser l’application !
2. Envoyer des messages aux utilisateurs qui donnent de mauvaises notes aux conducteurs pour obtenir un retour direct des clients et savoir pourquoi ils n’ont pas apprécié leur trajet.
3. Utilisez nos [fonctionnalités de modélisation et de personnalisation des messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) pour intégrer l'attribut unique du code de promotion dans les messages adressés aux utilisateurs.

## Bonnes pratiques

### Bonnes pratiques générales

#### Utiliser les propriétés de l’événement

- Donner à un événement personnalisé un nom qui décrit une action effectuée par un utilisateur.
- Faire un usage optimal des propriétés d’événement personnalisé pour représenter des données importantes sur un événement.
- Par exemple, plutôt que de capturer un événement personnalisé distinct pour regarder chacun des 50 films différents, il serait plus efficace de capturer simplement un film en tant qu’événement et d’avoir une propriété de l’événement qui inclut le nom du film.

### Bonnes pratiques de développement

#### Définir les ID utilisateur pour chaque utilisateur

Les ID utilisateur doivent être définis pour chacun de vos utilisateurs. Ils doivent être inchangés et accessibles lorsqu’un utilisateur ouvre l’application. Nous vous **recommandons vivement** de fournir cet identifiant, car vous pourrez ainsi :

- Suivre vos utilisateurs sur les appareils et plateformes, améliorant la qualité de vos données comportementales et démographiques.
- Importez des données sur vos utilisateurs à l'aide de notre [API de données d'utilisateurs]({{site.baseurl}}/api/endpoints/user_data/).
- Ciblez des utilisateurs spécifiques avec notre [API d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging/) pour les messages généraux et transactionnels.

Les ID doivent comporter moins de 512 caractères et doivent être privés et difficiles à obtenir (par exemple, pas une simple adresse e-mail ou un nom d'utilisateur). Si un tel identifiant n’est pas disponible, Braze attribue un identifiant unique à vos utilisateurs, mais il vous manquera les capacités énumérées pour les ID utilisateur. Vous devez éviter de définir des ID utilisateur pour les utilisateurs pour lesquels vous n’avez pas d’identifiant unique qui leur soit lié en tant qu’individus. La transmission d’un identifiant d’appareil n’offre aucun avantage par rapport au suivi automatique d’utilisateur anonyme que Braze propose par défaut. Voici quelques exemples d’identifiants utilisateur appropriés et inappropriés.

Bonnes options pour les ID utilisateur :

- Adresse e-mail hachée ou nom d’utilisateur unique
- Identifiant de base de données unique

Ne pas utiliser comme ID utilisateur :

- ID de l’appareil
- Numéro aléatoire ou ID de session
- N’importe quel ID non unique
- Adresse e-mail
- Un autre ID de fournisseur tiers

{% multi_lang_include sdk_auth_alert.md %}

#### Donnez des noms et des noms lisibles des événements personnalisés

Imaginez que vous êtes un marketeur qui commence à utiliser Braze un an ou deux après la mise en œuvre. Une liste déroulante remplie de noms comme « usrnoncpte » sans contexte supplémentaire peut être déconcertante. Donner des noms identifiables et lisibles à votre événement et à vos attributs facilitera les choses pour tous les utilisateurs de votre plateforme. Tenez compte des bonnes pratiques suivantes :

- Ne commencez pas un événement personnalisé avec un caractère numérique. La liste déroulante est triée par ordre alphabétique et le fait de commencer par un caractère numérique rend plus difficile la segmentation par le filtre de votre choix
- Essayez, dans la mesure du possible, de ne pas utiliser les abréviations obscures ou du jargon technique
  - Exemple : `usr_ctry` peut convenir comme nom de variable pour le pays d’un utilisateur dans un morceau de code, mais l’attribut personnalisé doit être envoyé à Braze comme `user_country` au moins pour donner un peu de clarté à un spécialiste du marketing utilisant le tableau de bord par la suite.

#### Enregistrez les attributs uniquement lorsqu’ils sont modifiés

Nous comptons chaque attribut transmis à Braze comme point de données, même si l’attribut transféré contient la même valeur que celle enregistrée précédemment. L'enregistrement des données uniquement lorsqu'elles changent permet d'éviter l'utilisation redondante de points de données et favorise une expérience plus fluide en évitant les appels d'API inutiles.

#### Évitez les noms d’événements générés par programmation

Si vous créez constamment de nouveaux noms d’événements, il sera impossible de segmenter de façon significative vos utilisateurs. Vous devriez généralement capturer des événements génériques ("Regarder une vidéo" ou "Lire un article") plutôt que des événements très spécifiques tels que ("Regarder Gangnam Style" ou "Lire un article") : Best 10 Lunch Spots in Midtown Manhattan"). Les données spécifiques à propos de l’événement doivent être incluses comme propriété de l’événement, et non pas dans le cadre du nom de l’événement.

### Limitations et contraintes techniques

Soyez attentif aux limitations et contraintes suivantes lors de la mise en œuvre d’événements personnalisés :

#### Contraintes de longueur

Tous les événements personnalisés, les noms d’attributs personnalisés (clés) et les valeurs de chaîne d’événements personnalisées de 255 caractères ou plus seront tronqués. Idéalement, ils doivent être aussi courts que possible pour améliorer les performances réseau et de batterie de votre application. Si possible, limitez-les à 50 caractères.

#### Contraintes de contenu
Le contenu suivant sera découpé de manière programmatique à partir de vos attributs et événements. Veillez à ne pas utiliser ce qui suit :

- Espace blanc avant et arrière
- Retours à la ligne
- Tous les éléments qui ne sont pas des chiffres dans les numéros de téléphone
  - Exemple : "(732) 178-1038" sera condensé en "7321781038"
- Les caractères non blancs doivent être convertis en espaces
- Le symbole $ ne doit pas être utilisé comme préfixe pour les événements personnalisés
- Toute valeur d’encodage UTF-8 non valide
  -  "Mon domaine \\x80" serait condensé en "Mon domaine"

#### Clés réservées

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d’événement personnalisé :

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

#### Définitions de valeur

- Les valeurs entières comportent 64 bits
- Les décimales comportent 15 chiffres par défaut

### Analyse d’un champ de nom générique

S'il n'existe qu'un seul champ de nom générique pour un utilisateur (par exemple, "JohnDoe"), vous pouvez attribuer ce titre entier à l'attribut First Name (prénom) de votre utilisateur. De plus, vous pouvez essayer d’analyser à la fois le prénom et le nom de l’utilisateur en utilisant des espaces, mais cette dernière méthode comporte le risque potentiel de mal nommer certains de vos utilisateurs.
