---
nav_title: Analyse
article_title: "À propos de l'analyse pour le SDK de Braze"
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
  - .NET MAUI
---

# Analyse

> Découvrez les analyses du SDK Braze, afin de mieux comprendre quelles données Braze collecte, la différence entre les événements personnalisés et les attributs personnalisés, et les meilleures pratiques de gestion des analyses.

{% alert tip %}
Lors de la mise en œuvre de Braze, n'oubliez pas de discuter des objectifs marketing avec votre équipe, afin de décider au mieux des données que vous souhaitez suivre et de la manière dont vous souhaitez les suivre avec Braze. Pour un exemple, consultez notre étude de cas sur l'[application Taxi/covoiturage](#example-case) à la fin de ce guide.
{% endalert %}

## Données collectées automatiquement

Certaines données utilisateur sont collectées automatiquement par notre SDK, par exemple : Première application utilisée, Dernière application utilisée, Nombre total de sessions, Système d'exploitation de l'appareil, etc. Si vous suivez nos guides d'intégration pour mettre en œuvre nos SDK, vous pourrez profiter de cette [collecte de données par défaut]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/). Vérifier cette liste peut vous aider à éviter de stocker plusieurs fois les mêmes informations sur les utilisateurs. À l'exception du début et de la fin de session, toutes les autres données suivies automatiquement ne sont pas comptabilisées dans votre consommation de points de donnée.

Consultez notre article [Présentation du SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/) pour établir une liste d'autorisation des processus qui bloquent la collecte par défaut de certains éléments de données.

## Événements personnalisés

Les événements personnalisés sont des actions effectuées par vos utilisateurs ; ils sont particulièrement adaptés au suivi des interactions à forte valeur ajoutée avec votre application. L'enregistrement d'un événement personnalisé peut déclencher un nombre quelconque de campagnes de suivi avec des délais configurables, et permet les filtres de segmentation suivants autour de la récence et de la fréquence de cet événement :

| Options de segmentation | Filtre déroulant | Options d'entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si l'événement personnalisé s'est produit **plus de X fois** | **PLUS DE** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit **moins de X fois** | **MOINS DE** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit **exactement X fois** | **EXACTEMENT** | **NOMBRE** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **après la date X** | **APRÈS** | **DATE** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **avant la date X** | **AVANT** | **DATE** |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **il y a plus de X jours** | **PLUS DE** | **NOMBRE DE JOURS ÉCOULÉS** (Nombre positif) |
| Vérifier si l'événement personnalisé s'est produit pour la dernière fois **il y a moins de X jours** | **MOINS DE** | **NOMBRE DE JOURS ÉCOULÉS** (Nombre positif) |
| Vérifier si l'événement personnalisé s'est produit **plus de X (max = 50) fois** | **PLUS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l'événement personnalisé s'est produit **moins de X (max = 50) fois** | **MOINS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l'événement personnalisé s'est produit **exactement X (max = 50) fois** | **EXACTEMENT** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze enregistre le nombre de fois où ces événements se sont produits ainsi que la dernière fois qu'ils ont été effectués par chaque utilisateur, à des fins de segmentation. Sur la page d'analyse des **Événements personnalisés**, vous pouvez visualiser la fréquence globale de chaque événement personnalisé, ainsi que par segment au fil du temps pour une analyse plus détaillée. C'est particulièrement utile pour observer l'impact de vos campagnes sur l'activité des événements personnalisés, grâce aux lignes grises que Braze superpose sur la série temporelle pour indiquer la dernière fois qu'une campagne a été envoyée.

![Graphique d'analyse d'événements personnalisés affichant des statistiques sur les utilisateurs qui ont ajouté une carte de crédit et effectué une recherche sur une période de trente jours.]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

{% alert note %}
L'[incrémentation des attributs personnalisés]({{site.baseurl}}/api/endpoints/messaging/) peut être utilisée pour maintenir un compteur sur une action utilisateur, de manière similaire à un événement personnalisé. Cependant, vous ne pourrez pas visualiser les données d'attribut personnalisé sous forme de série temporelle. Les actions utilisateur qui n'ont pas besoin d'être analysées en série temporelle doivent être enregistrées via cette méthode.
{% endalert %}

### Stockage des événements personnalisés

Toutes les données de profil utilisateur (événements personnalisés, attributs personnalisés, données personnalisées) sont stockées tant que ces profils sont actifs.

### Propriétés d'événement personnalisé

Avec les propriétés d'événement personnalisé, Braze vous permet de définir des propriétés sur des événements personnalisés et des achats. Ces propriétés peuvent ensuite être utilisées pour affiner les conditions de déclenchement, améliorer la personnalisation des messages et générer des analyses plus sophistiquées via l'exportation des données brutes. Les valeurs des propriétés peuvent être des chaînes de caractères, des nombres, des valeurs booléennes ou des objets temporels. En revanche, les valeurs de propriété ne peuvent pas être des objets de type tableau.

Par exemple, si une application de commerce électronique souhaitait envoyer un message à un utilisateur lorsqu'il abandonne son panier, elle pourrait également améliorer son audience cible et renforcer la personnalisation de la campagne en ajoutant une propriété d'événement personnalisé `cart_value` correspondant à la valeur du panier de l'utilisateur.

![Exemple d'événement personnalisé qui enverra une campagne à un utilisateur ayant abandonné son panier et laissé la valeur du panier à plus de 100 et moins de 200.]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

Les propriétés d'événement personnalisé peuvent également être utilisées pour la personnalisation dans le modèle de message. Toute campagne utilisant la [livraison par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) avec un événement déclencheur peut exploiter les propriétés d'événement personnalisé de cet événement pour personnaliser les messages. Si une application de jeu souhaitait envoyer un message aux utilisateurs ayant terminé un niveau, elle pourrait personnaliser davantage le message avec une propriété indiquant le temps qu'il a fallu aux utilisateurs pour terminer ce niveau. Dans cet exemple, le message est personnalisé pour trois segments différents à l'aide de la [logique conditionnelle]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/). La propriété d'événement personnalisé appelée ``time_spent`` peut être incluse dans le message en appelant ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Congratulations on beating that level so fast! Check out our online portal where you can play against top players from around the world!
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Talk to villagers for essential tips on how to beat levels!
{% endif %}
```
{% endraw %}

Les propriétés d'événement personnalisé sont conçues pour vous aider à personnaliser vos messages ou à élaborer des campagnes granulaires de livraison par événement. Si vous souhaitez créer des segments basés sur la récence et la fréquence des propriétés d'événement, contactez votre Customer Success Manager ou notre équipe d'assistance.

## Attributs personnalisés

Les attributs personnalisés sont des outils extrêmement flexibles qui vous permettent de cibler les utilisateurs avec une plus grande précision qu'avec les attributs standard. Ils sont parfaits pour stocker des informations spécifiques à votre marque concernant vos utilisateurs. Gardez à l'esprit que nous ne stockons pas d'informations de séries temporelles pour les attributs personnalisés. Vous ne pourrez donc pas obtenir de graphiques basés sur ces attributs, contrairement à l'exemple précédent pour les événements personnalisés.

### Stockage des attributs personnalisés

Toutes les données de profil utilisateur (événements personnalisés, attributs personnalisés, données personnalisées) sont stockées tant que ces profils sont actifs.

### Types de données des attributs personnalisés

Les types de données suivants peuvent être stockés en tant qu'attributs personnalisés :

#### Chaînes de caractères (caractères alphanumériques)

Les attributs au format chaîne de caractères sont utiles pour stocker les entrées utilisateur, comme une marque préférée, un numéro de téléphone ou la dernière recherche effectuée dans votre application. Les attributs de chaîne de caractères sont soumis aux [contraintes de longueur](#length-constraints) applicables aux données personnalisées (479 octets, soit environ 479 caractères à un octet ou environ 160 caractères pour les scripts multioctets tels que le japonais).

Le tableau suivant décrit les options de segmentation disponibles pour les attributs de chaîne de caractères.

| Options de segmentation | Filtre déroulant | Options d'entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si l'attribut chaîne de caractères **correspond exactement à** une chaîne de caractères saisie| **ÉGAL À** | **CHAÎNE DE CARACTÈRES** |
| Vérifier si l'attribut chaîne de caractères **correspond partiellement à** une chaîne saisie **OU** à une expression régulière | **CORRESPOND À L'EXPRESSION RÉGULIÈRE** | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE** |
| Vérifier si l'attribut chaîne de caractères **ne correspond pas partiellement** à une chaîne de caractères **OU** à une expression régulière saisie | **NE CORRESPOND PAS À L'EXPRESSION RÉGULIÈRE** | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE** |
| Vérifier si l'attribut chaîne de caractères **ne correspond pas à** une chaîne de caractères saisie| **N'EST PAS ÉGAL À** | **CHAÎNE DE CARACTÈRES** |
| Vérifier si l'attribut chaîne de caractères **existe** dans le profil d'un utilisateur | **EST VIDE** | **S.O.** |
| Vérifier si l'attribut chaîne de caractères **n'existe pas** dans le profil d'un utilisateur | **N'EST PAS VIDE** | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Lors de la segmentation à l'aide du filtre **NE CORRESPOND PAS À L'EXPRESSION RÉGULIÈRE**, il est nécessaire qu'un attribut personnalisé avec une valeur attribuée existe déjà dans le profil utilisateur concerné. Braze recommande d'utiliser la logique « OU » pour vérifier si un attribut personnalisé est vide afin de cibler correctement les utilisateurs.
{% endalert %}

{% alert tip %}
Pour en savoir plus sur l'utilisation de notre filtre d'expressions régulières, consultez cette documentation sur les [expressions régulières compatibles avec Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
Plus de ressources sur les expressions régulières :
- [Braze et les expressions régulières]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Débogueur et testeur d'expressions régulières](https://regex101.com/)
- [Tutoriel sur les expressions régulières](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

#### Tableaux

Les attributs de tableau sont adaptés au stockage de listes d'informations associées à vos utilisateurs. Par exemple, stocker dans un tableau les 100 derniers contenus consultés par un utilisateur permettrait une segmentation spécifique basée sur les centres d'intérêt.

Les tableaux d'attributs personnalisés sont des ensembles unidimensionnels ; les tableaux multidimensionnels ne sont pas pris en charge. **L'ajout d'un élément à un tableau d'attribut personnalisé place l'élément à la fin du tableau, sauf s'il est déjà présent, auquel cas il est déplacé de sa position actuelle vers la fin du tableau.** Par exemple, si un tableau `['hotdog','hotdog','hotdog','pizza']` est importé, il apparaîtra dans l'attribut de tableau comme `['hotdog', 'pizza']`, car seules les valeurs uniques sont prises en charge.

Si le tableau contient son nombre maximum d'éléments, le premier élément sera supprimé et le nouvel élément ajouté à la fin. Voici quelques exemples de code illustrant le comportement du tableau dans le SDK Web :

```js
var abUser = appboy.getUser();
// initialize array for this user, assuming max length of favorite_foods is set to 4.
abUser.setCustomUserAttribute('favorite_foods', ['pizza', 'wings', 'pasta']); // => ['pizza', 'wings', 'pasta']
abUser.addToCustomAttributeArray('favorite_foods', 'fries'); // => ['pizza', 'wings', 'pasta', 'fries']
abUser.addToCustomAttributeArray('favorite_foods', 'pizza'); // => ['wings', 'pasta', 'fries', 'pizza']
abUser.addToCustomAttributeArray('favorite_foods', 'ice cream'); // => ['pasta', 'fries', 'pizza', 'ice cream']
```

Le nombre par défaut et maximum d'éléments dans un tableau est de 500. Vous pouvez modifier le nombre maximum d'éléments dans le tableau de bord de Braze, sous **Paramètres des données** > **Attributs personnalisés**. Les tableaux dépassant le nombre maximum d'éléments sont tronqués pour ne contenir que le nombre maximum d'éléments.

Le tableau suivant décrit les options de segmentation disponibles pour les attributs de tableau.

| Options de segmentation | Filtre déroulant | Options d'entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si l'attribut du tableau **inclut une valeur qui correspond exactement** à une valeur saisie| **INCLUT LA VALEUR** | **CHAÎNE DE CARACTÈRES** |
| Vérifier si l'attribut du tableau **n'inclut pas une valeur qui correspond exactement** à une valeur saisie| **N'INCLUT PAS LA VALEUR** | **CHAÎNE DE CARACTÈRES** |
| Vérifier si l'attribut du tableau **contient une valeur qui correspond partiellement** à une valeur saisie **OU** à une expression régulière | **CORRESPOND À L'EXPRESSION RÉGULIÈRE** | **CHAÎNE DE CARACTÈRES** **OU** **EXPRESSION RÉGULIÈRE** |
| Vérifier si l'attribut du tableau **a une valeur** | **A UNE VALEUR** | **S.O.** |
| Vérifier si l'attribut du tableau **est vide** | **EST VIDE** | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Nous utilisons des [expressions régulières compatibles avec Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
{% endalert %}

#### Dates

Les attributs de temps sont utiles pour stocker la dernière fois qu'une action spécifique a été effectuée, ce qui vous permet d'envoyer des messages de réengagement ciblés à vos utilisateurs.

{% alert note %}
La dernière date à laquelle un événement personnalisé ou un événement d'achat s'est produit est automatiquement enregistrée et ne doit pas être enregistrée en double via un attribut de temps personnalisé.
{% endalert %}

Les filtres de date utilisant des dates relatives (par exemple, il y a plus d'un jour, il y a moins de deux jours) comptent 1 jour comme 24 heures. Toute campagne utilisant ces filtres inclura tous les utilisateurs par incréments de 24 heures. Par exemple, l'option « Dernière utilisation de l'application il y a plus d'un jour » capturera tous les utilisateurs qui ont « utilisé l'application il y a plus de 24 heures » à partir du moment exact où la campagne est lancée. Il en va de même pour les campagnes définies avec des plages de dates plus longues — ainsi, cinq jours après l'activation correspond aux 120 heures précédentes.

Le tableau suivant décrit les options de segmentation disponibles pour les attributs de temps.

| Options de segmentation | Filtre déroulant | Options d'entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si l'attribut de temps **est antérieur à** une **date sélectionnée**| **AVANT** | **SÉLECTEUR DE DATE DU CALENDRIER** |
| Vérifier si l'attribut de temps **est postérieur à** une **date sélectionnée**| **APRÈS** | **SÉLECTEUR DE DATE DU CALENDRIER** |
| Vérifier si l'attribut de temps **date de plus de X jours** | **PLUS DE** | **NOMBRE DE JOURS ÉCOULÉS** |
| Vérifier si l'attribut de temps **date de moins de X jours**| **MOINS DE** | **NOMBRE DE JOURS ÉCOULÉS** |
| Vérifier si l'attribut de temps se situe **dans plus de X jours dans le futur** | **DANS PLUS DE** | **NOMBRE DE JOURS À VENIR** |
| Vérifier si l'attribut de temps se situe **dans moins de X jours dans le futur** | **DANS MOINS DE** | **NOMBRE DE JOURS À VENIR**  |
| Vérifier si l'attribut de temps **existe** dans le profil d'un utilisateur | **VIDE** | **S.O.** |
| Vérifier si l'attribut de temps **n'existe pas** dans le profil d'un utilisateur | **N'EST PAS VIDE** | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Nombres {#integers}

Les attributs numériques couvrent une grande variété de cas d'utilisation. Les attributs personnalisés de type nombre incrémental sont utiles pour stocker le nombre de fois qu'une action ou un événement donné s'est produit. Les nombres standards servent à toutes sortes d'usages, par exemple : enregistrer la pointure de chaussures, le tour de taille, ou le nombre de fois qu'un utilisateur a consulté une certaine fonctionnalité ou catégorie de produit.

{% alert note %}
L'argent dépensé ne doit pas être enregistré via cette méthode. Il convient plutôt de l'enregistrer via nos [méthodes d'achat]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#purchase-events--revenue-tracking).
{% endalert %}

Le tableau suivant décrit les options de segmentation disponibles pour les attributs numériques.

| Options de segmentation | Filtre déroulant | Options d'entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si l'attribut numérique **est supérieur à** un **nombre**| **PLUS DE** | **NOMBRE** |
| Vérifier si l'attribut numérique **est inférieur à** un **nombre**| **MOINS DE** | **NOMBRE** |
| Vérifier si l'attribut numérique **est exactement** un **nombre**| **EXACTEMENT** | **NOMBRE** |
| Vérifier si l'attribut numérique **n'est pas égal à** un **nombre**| **N'EST PAS ÉGAL À** | **NOMBRE** |
| Vérifier si l'attribut numérique **existe** dans le profil d'un utilisateur | **EXISTE** | **S.O.** |
| Vérifier si l'attribut numérique **n'existe pas** dans le profil d'un utilisateur | **N'EXISTE PAS** | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Valeurs booléennes (vrai/faux)

Les attributs booléens sont utiles pour stocker des données binaires simples sur vos utilisateurs, comme le statut d'abonnement. Les options de saisie proposées vous permettent de trouver des utilisateurs dont une variable est explicitement définie sur une valeur booléenne, ainsi que ceux pour lesquels cet attribut n'a pas encore été enregistré.

Le tableau suivant décrit les options de segmentation disponibles pour les attributs booléens.

| Options de segmentation | Filtre déroulant | Options d'entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si la valeur booléenne **est** | **EST**  | **VRAI**, **FAUX**, **VRAI OU NON ENREGISTRÉ**, ou **FAUX OU NON ENREGISTRÉ** |
| Vérifier si la valeur booléenne **existe** dans le profil d'un utilisateur | **EXISTE**  | **S.O.** |
| Vérifier si la valeur booléenne **n'existe pas** dans le profil d'un utilisateur | **N'EXISTE PAS**  | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Événements d'achat / suivi du chiffre d'affaires

L'utilisation de nos méthodes d'achat pour enregistrer les achats in-app établit la valeur à vie (LTV) pour chaque profil utilisateur individuel. Ces données sont consultables sur notre page de chiffre d'affaires sous forme de graphiques de séries temporelles.

Le tableau suivant décrit les options de segmentation disponibles pour les événements d'achat.

| Options de segmentation | Filtre déroulant | Options d'entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si le montant total dépensé en dollars **est supérieur à** un **nombre**| **SUPÉRIEUR À** | **NOMBRE** |
| Vérifier si le montant total dépensé en dollars **est inférieur à** un **nombre**| **MOINS DE** | **NOMBRE** |
| Vérifier si le montant total dépensé en dollars **est exactement** un **nombre**| **EXACTEMENT** | **NOMBRE** |
| Vérifier si le dernier achat a eu lieu **après la date X** | **APRÈS** | **DATE** |
| Vérifier si le dernier achat a eu lieu **avant la date X** | **AVANT** | **DATE** |
| Vérifier si le dernier achat a eu lieu **il y a plus de X jours** | **PLUS DE** | **DATE** |
| Vérifier si le dernier achat a eu lieu **il y a moins de X jours** | **MOINS DE** | **DATE** |
| Vérifier si l'achat a eu lieu **plus de X (max = 50) fois** | **PLUS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l'achat a eu lieu **moins de X (max = 50) fois** | **MOINS DE** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifier si l'achat a eu lieu **exactement X (max = 50) fois** | **EXACTEMENT** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Si vous souhaitez segmenter sur le nombre de fois qu'un achat spécifique a été effectué, vous devez également enregistrer cet achat individuellement en tant qu'[attribut personnalisé incrémental](#integers).
{% endalert %}

## Cas d'utilisation : application de taxi/covoiturage {#example-case}

Dans cet exemple, prenons une application de covoiturage qui souhaite déterminer quelles données utilisateur collecter. Les questions et le brainstorming suivants constituent un excellent modèle à suivre pour les équipes marketing et de développement. À la fin de cet exercice, les deux équipes devraient avoir une compréhension claire des événements et attributs personnalisés qu'il est pertinent de collecter pour atteindre leur objectif.

**Question n° 1 : Quel est l'objectif ?**

Leur objectif est simple : ils veulent que les utilisateurs commandent des trajets en taxi via leur application.

**Question n° 2 : Quelles sont les étapes intermédiaires entre l'installation de l'application et cet objectif ?**

1. Il faut que les utilisateurs commencent le processus d'inscription et renseignent leurs informations personnelles.
2. Il faut que les utilisateurs confirment leur inscription en entrant un code reçu par SMS dans l'application.
3. Ils doivent essayer de commander un taxi.
4. Pour commander un taxi, il faut que des taxis soient disponibles au moment de leur recherche.

Ces actions peuvent ensuite être associées aux événements personnalisés suivants :

- Inscription commencée
- Inscription terminée
- Appels de taxi réussis
- Appels de taxi échoués

Une fois les événements définis, vous pouvez lancer les campagnes suivantes :

1. Envoyer des messages aux utilisateurs qui ont commencé l'inscription sans la terminer dans un certain délai.
2. Envoyer des messages de félicitations aux utilisateurs qui ont terminé leur inscription.
3. Envoyer des excuses et un crédit promotionnel aux utilisateurs dont les appels de taxi ont échoué et qui n'ont pas été suivis d'un appel réussi dans un certain délai.
4. Envoyer des promotions aux utilisateurs les plus actifs ayant de nombreux appels de taxi réussis pour les remercier de leur fidélité.

Et bien plus encore !

**Question n° 3 : Quelles autres informations pourrions-nous connaître sur nos utilisateurs pour enrichir nos messages ?**

- Ont-ils un crédit promotionnel ?
- Quelle note moyenne donnent-ils à leurs chauffeurs ?
- Des codes promotionnels uniques pour l'utilisateur ?

Ces caractéristiques peuvent ensuite être associées aux attributs personnalisés suivants :

- Solde de crédit promotionnel (type décimal)
- Note moyenne du chauffeur (type nombre)
- Code promotionnel unique (type chaîne de caractères)

L'ajout de ces attributs vous permettrait d'envoyer des campagnes aux utilisateurs, par exemple :

1. Rappeler aux utilisateurs qui ne se sont pas connectés depuis 7 jours mais qui disposent d'un crédit promotionnel que ce crédit existe et qu'ils devraient revenir sur l'application pour l'utiliser !
2. Envoyer des messages aux utilisateurs qui donnent de mauvaises notes aux chauffeurs pour obtenir un retour direct et comprendre pourquoi ils n'ont pas apprécié leur trajet.
3. Utiliser nos [fonctionnalités de modélisation et de personnalisation des messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) pour intégrer l'attribut de code promotionnel unique dans les messages adressés aux utilisateurs.

## Bonnes pratiques

### Bonnes pratiques générales

#### Utiliser les propriétés d'événement

- Donnez à un événement personnalisé un nom qui décrit une action effectuée par un utilisateur.
- Faites un usage généreux des propriétés d'événement personnalisé pour représenter des données importantes sur un événement.
- Par exemple, plutôt que de capturer un événement personnalisé distinct pour chacun des 50 films visionnés, il serait plus efficace de capturer simplement le visionnage d'un film comme événement et d'inclure le nom du film en tant que propriété d'événement.

### Bonnes pratiques de développement

#### Définir les ID utilisateur pour chaque utilisateur

Les ID utilisateur doivent être définis pour chacun de vos utilisateurs. Ils doivent être immuables et accessibles lorsqu'un utilisateur ouvre l'application. Nous vous **recommandons vivement** de fournir cet identifiant, car il vous permettra de :

- Suivre vos utilisateurs sur les appareils et plateformes, améliorant la qualité de vos données comportementales et démographiques.
- Importer des données sur vos utilisateurs à l'aide de notre [API de données utilisateur]({{site.baseurl}}/api/endpoints/user_data/).
- Cibler des utilisateurs spécifiques avec notre [API d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging/) pour les messages généraux et transactionnels.

Les ID utilisateur doivent comporter moins de 512 caractères et doivent être privés et difficiles à obtenir (par exemple, pas une simple adresse e-mail ou un nom d'utilisateur). Si un tel identifiant n'est pas disponible, Braze attribuera un identifiant unique à vos utilisateurs, mais vous ne bénéficierez pas des fonctionnalités mentionnées ci-dessus. Évitez de définir des ID utilisateur pour les utilisateurs pour lesquels vous ne disposez pas d'un identifiant unique qui leur soit propre. La transmission d'un identifiant d'appareil n'offre aucun avantage par rapport au suivi automatique des utilisateurs anonymes que Braze propose par défaut. Voici quelques exemples d'identifiants utilisateur appropriés et inappropriés.

Bonnes options pour les ID utilisateur :

- Adresse e-mail hachée ou nom d'utilisateur unique
- Identifiant de base de données unique

Ne pas utiliser comme ID utilisateur :

- ID de l'appareil
- Numéro aléatoire ou ID de session
- N'importe quel ID non unique
- Adresse e-mail
- Un ID utilisateur d'un autre fournisseur tiers

{% multi_lang_include alerts/important_alerts.md alert='SDK auth' %}

#### Donnez des noms lisibles aux événements personnalisés et aux attributs

Imaginez que vous soyez un marketeur qui commence à utiliser Braze un an ou deux après sa mise en œuvre. Parcourir une liste déroulante remplie de noms comme « usr_no_acct » sans contexte supplémentaire peut être décourageant. Donner des noms identifiables et lisibles à vos événements et attributs facilitera les choses pour tous les utilisateurs de votre plateforme. Voici quelques bonnes pratiques à suivre :

- Ne commencez pas un événement personnalisé par un caractère numérique. La liste déroulante est triée par ordre alphabétique et commencer par un chiffre rend plus difficile la segmentation par le filtre de votre choix.
- Essayez, dans la mesure du possible, de ne pas utiliser d'abréviations obscures ou de jargon technique.
  - Exemple : `usr_ctry` peut convenir comme nom de variable pour le pays d'un utilisateur dans du code, mais l'attribut personnalisé devrait être envoyé à Braze sous la forme `user_country` pour apporter de la clarté à un marketeur utilisant le tableau de bord par la suite.

#### Enregistrez les attributs uniquement lorsqu'ils changent

Nous comptabilisons chaque attribut transmis à Braze comme un point de donnée, même si l'attribut transmis contient la même valeur que celle déjà enregistrée. N'enregistrer les données que lorsqu'elles changent permet d'éviter une consommation redondante de points de donnée et favorise une expérience plus fluide en évitant les appels d'API inutiles.

#### Évitez de générer des noms d'événements par programmation

Si vous créez constamment de nouveaux noms d'événements, il sera impossible de segmenter vos utilisateurs de manière pertinente. Privilégiez les événements génériques (« A regardé une vidéo » ou « A lu un article ») plutôt que des événements très spécifiques comme « A regardé Gangnam Style » ou « A lu l'article : Les 10 meilleurs restaurants du centre-ville ». Les données spécifiques à l'événement doivent être incluses comme propriété d'événement, et non dans le nom de l'événement.

### Limitations et contraintes techniques

Soyez attentif aux limitations et contraintes suivantes lors de la mise en œuvre d'événements personnalisés :

#### Contraintes de longueur

Braze impose une limite de longueur en octets (479 octets) pour les noms d'événements personnalisés, les noms d'attributs personnalisés (clés) et les valeurs de chaîne de caractères des événements personnalisés. Les valeurs qui dépassent cette limite sont tronquées. En termes de caractères, cela correspond à environ 479 caractères à un octet (par exemple, ASCII), ou environ 160 caractères pour les scripts multioctets tels que le japonais (en supposant environ 3 octets par caractère en UTF-8). Idéalement, gardez les noms et les valeurs aussi courts que possible afin d'améliorer les performances réseau et batterie de votre application — si possible, limitez-les à 50 caractères.

#### Contraintes de contenu
Le contenu suivant sera supprimé automatiquement de vos attributs et événements. Veillez à ne pas utiliser ce qui suit :

- Espaces en début et en fin de chaîne
- Retours à la ligne
- Tous les éléments qui ne sont pas des chiffres dans les numéros de téléphone
  - Exemple : « (732) 178-1038 » sera condensé en « 7321781038 »
- Les caractères non blancs doivent être convertis en espaces
- Le symbole $ ne doit pas être utilisé comme préfixe pour les événements personnalisés
- Toute valeur d'encodage UTF-8 non valide
  -  « Mon \x80 champ » serait condensé en « Mon champ »

#### Clés réservées

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d'événement personnalisé :

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

#### Définitions de valeur

- Les valeurs entières comportent 64 bits
- Les décimales comportent 15 chiffres par défaut

### Analyse d'un champ de nom générique

S'il n'existe qu'un seul champ de nom générique pour un utilisateur (par exemple, « JohnDoe »), vous pouvez attribuer ce titre entier à l'attribut Prénom de votre utilisateur. Vous pouvez également essayer d'analyser le prénom et le nom de l'utilisateur en utilisant les espaces, mais cette méthode comporte le risque de mal nommer certains de vos utilisateurs.