---
page_order: 0.5
nav_title: Page de test vidéo
layout: featured_video
video_id: XY5uXoKIvFY
video_source: YouTube
noindex: true
---

# Collecte de données utilisateur

Avant de terminer votre implémentation de Braze, assurez-vous que vos équipes marketing et développement soient bien sur la même longueur d’onde concernant vos objectifs marketing. Lorsque vous décidez de ce que vous voulez suivre et de la façon dont vous voulez le suivre avec Braze, il est utile d’envisager ces objectifs d’abord et de travailler à rebours ensuite en partant des objectifs. Consultez notre cas d’une [Application Taxi/Partage de trajet][16] à la fin de ce Guide pour un exemple de ce processus.

Ce guide sur les bonnes pratiques vous aidera à comprendre exactement la différence entre un événement personnalisé et un attribut personnalisé pour Braze.

## Données collectées automatiquement

Les événements et attributs suivants sont collectés et mis à jour automatiquement par le SDK Braze dans le cadre des points de données de `Session Start` et de `Session End`, ou par le back-end Braze. Vous n’avez pas besoin de les enregistrer séparément en tant qu’événements personnalisés ou attributs personnalisés.

#### Informations sur l’utilisation
- Première application utilisée (date)
- Dernière application utilisée (date)
- Nombre total de sessions (entier)
- Nombre d’objets de feedback (entier)
- Nombre de sessions au cours des derniers Y jours (entier et date)
- E-mail disponible (booléen)
- Nombre de vues du fil d’actualité (entier)

#### Reciblage d’une campagne
- Dernier message reçu (date)
- Dernière campagne par e-mail reçue (date)
- Dernière campagne de notification push reçue (date)
- Dernier fil d’actualité vu (date)
- Carte cliquée (entier)
- Message reçu de la campagne
  - Ce filtre vous permet de cibler les utilisateurs selon qu’ils ont reçu (ou pas) une campagne précédente.
- Message reçu à partir d’une campagne avec tag
  - Ce filtre vous permet de cibler les utilisateurs selon qu’ils ont reçu (ou pas) une campagne précédente qui a actuellement un tag.
- Recibler la campagne
  - Ce filtre vous permet de cibler les utilisateurs selon s’ils ont ou non ouvert ou cliqué sur un e-mail spécifique, une notification push ou un slideup dans le passé

#### Informations sur l’appareil
- Emplacement disponible (booléen)
- Location la plus récente (si l’autorisation de location est accordée à votre application)
- Push activé (booléen)
- Emplacement du périphérique
- Langue (prise à partir de l’emplacement du périphérique)
- Pays (d’abord extrait de l’adresse IP. Si cette option n’est pas disponible, il est pris depuis l’emplacement du périphérique)
- Version la plus récente de l’application
- Modèle du périphérique
- Version du système d’exploitation
- Résolution du périphérique
- Dispositif Transporteur sans fil
- Fuseau horaire du périphérique
- Identifiant du dispositif
- Désinstallé (date et booléen)

## Événements personnalisés

Les événements personnalisés sont des actions effectuées par vos utilisateurs ; ils conviennent mieux pour le suivi des interactions utilisateur de grande valeur avec votre application. L’enregistrement d’un événement personnalisé peut déclencher un nombre quelconque de campagnes de suivi avec des délais configurables et permet aux filtres de segmentation suivants de filtrer la fréquence et la dernière occurrence de cet événement :

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifie si l’événement personnalisé s’est produit **plus de X fois** | **SUPERIEUR A ** | **ENTIER** |
| Vérifie si l’événement personnalisé s’est produit **moins de X fois** | **INFERIEUR A** | **ENTIER** |
| Vérifie si l’événement personnalisé s’est produit **exactement X fois** | **EXACTEMENT** | **ENTIER** |
| Vérifie si l’événement personnalisé s’est produit pour la dernière fois **après la date X** | **APRÈS** | **DATE** |
| Vérifie si l’événement personnalisé s’est produit pour la dernière fois **avant la date X** | **AVANT** | **DATE** |
| Vérifie si l’événement personnalisé s’est produit pour la dernière fois **il y a plus de X jours** | **PLUS DE** | **IL Y A X JOURS** (entier positif) |
| Vérifie si l’événement personnalisé a eu lieu **il y a moins de X jours** | **MOINS QUE** | **IL Y A X JOURS** (entier positif) |
| Vérifie si l’événement personnalisé s’est produit **plus de X (Max = 50)  fois** | **PLUS DE ** | dans les **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifie si l’événement personnalisé s’est produit **moins de X (Max = 50) fois** | **MOINS DE** | dans les **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifie si l’événement personnalisé s’est produit **exactement X (Max = 50)  fois** | **EXACTEMENT** | dans les **Y derniers jours  (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Braze indique le nombre de fois où ces événements ont eu lieu ainsi que la dernière fois qu’ils ont été exécutés par chaque utilisateur pour la segmentation. La page d’analyses des événements personnalisés vous permet de voir la fréquence à laquelle chaque événement personnalisé se produit, ainsi que par segment dans le temps pour une analyse plus détaillée. Ceci est particulièrement utile pour voir comment vos campagnes ont affecté les événements personnalisés,  en regardant les lignes grises placées par Braze sur la série temporelle pour indiquer la dernière fois qu’une campagne a été envoyée.

![custom_event_analytics_example.png][8]

>  Comme pour un événement personnalisé, [des attributs personnalisés incrémentaux][10] peuvent être utilisés pour mettre un compteur sur une action de l’utilisateur. Cependant, vous ne pourrez pas afficher les données d’attribut personnalisées dans une série temporelle. Les actions utilisateur qui ne doivent pas être analysées dans les séries temporelles doivent être enregistrées à l’aide de cette méthode.

### Stockage d’événements personnalisés

Toutes les données de profil utilisateur (événements personnalisés, attributs personnalisés, données personnalisées) sont stockées tant que ces profils sont actifs. Les propriétés de l’événement sont stockées pour la segmentation pendant soixante (60) jours.

### Propriétés de l'événement personnalisé

Avec des propriétés de l’événement personnalisé, Braze vous permet de définir des propriétés sur des événements personnalisés et des achats. Ces propriétés peuvent ensuite être utilisées pour ajouter des conditions de déclenchement supplémentaires, améliorer le niveau de personnalisation des envois de messages et générer des analyses plus sophistiquées via l’exportation des données brutes. Les valeurs des propriétés peuvent être des chaînes de caractères, des nombres, des valeurs booléennes ou des objets de date. Cependant, les valeurs de propriété ne peuvent pas être des objets de type tableau.

Par exemple, si une application d’e-commerce souhaite envoyer un message à un utilisateur lorsqu’il abandonne son panier, elle pourrait en outre améliorer son public cible et permettre une personnalisation accrue de la campagne en ajoutant une propriété d’événement personnalisé « Valeur du panier » sur les paniers des utilisateurs.

![customEventProperties.png][18]

Les propriétés de l'événement personnalisées peuvent également être utilisées pour la personnalisation du modèle de messagerie. Toute campagne utilisant [Action-Based Delivery][19] (Livraison par événement) avec un événement déclencheur peut utiliser des propriétés de l’événement personnalisées de cet événement pour la personnaliser les messages. Si un jeu souhaite envoyer un message aux utilisateurs qui ont terminé un niveau, il pourrait personnaliser le message avec une propriété pour le temps qu’il a fallu à l’utilisateur pour terminer le niveau. Dans cet exemple, le message est personnalisé pour trois segments différents en utilisant la [logique conditionnelle][18].  La propriété d’événement personnalisée appelée ``time_spent`` peut être incluse dans le message en appelant ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Félicitations pour avoir battu ce niveau aussi rapidement ! Consultez notre portail en ligne pour pouvoir jouer contre les meilleurs joueurs du monde entier !
{% elsif {{event_properties.${time_spent}}} < 1800 %}
N’oubliez pas de visiter le magasin de ville entre les niveaux pour actualiser vos outils.
{% else %}
Parlez aux villageois pour obtenir des conseils sur la façon de battre les niveaux !
{% endif %}
```
{% endraw %}

Les propriétés d’événement personnalisé sont conçues pour vous aider à personnaliser vos envois de messages ou à élaborer des campagnes de livraison par événement précises. Si vous souhaitez créer des segments en fonction de la fréquence et de la dernière occurrence des propriétés de l’événement, veuillez contacter votre gestionnaire du succès des clients car cela pourrait entraîner des coûts de données supplémentaires.

## Attributs personnalisés
Les attributs personnalisés sont les plus appropriés pour stocker des attributs sur vos utilisateurs, ou des informations sur les actions à faible valeur dans votre application. Gardez à l’esprit que nous ne stockons pas d’informations sur les séries temporelles pour les attributs personnalisés. Vous ne pourrez donc pas voir de graphiques basés sur ces attributs, comme dans l’exemple précédent pour les événements personnalisés.

### Stockage des attributs personnalisé

Toutes les données de profil utilisateur (événements personnalisés, attributs personnalisés, données personnalisées) sont stockées tant que ces profils sont actifs. Les propriétés de l’événement sont stockées pour la segmentation pendant soixante (60) jours.

### Types de données des attributs personnalisés
Les attributs personnalisés sont des outils extraordinairement flexibles qui permettent un ciblage exceptionnel. Les types de données suivants peuvent être stockés en tant qu’attributs personnalisés :

#### Chaînes de caractères (caractères alphanumériques)
Les attributs au format string sont utiles pour stocker les entrées utilisateur, comme une marque préférée, un numéro de téléphone ou la dernière recherche dans votre application. La longueur maximale des attributs de chaîne de caractères est de 256 caractères.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifie si l’attribut de chaîne de caractères est **exactement identique** à une chaîne de caractères| **ÉGAL A** | **STRING** |
| Vérifie si l’attribut de chaîne de caractères **correspond partiellement** à une chaîne de caractères **OU** une expression régulière | **CORRESPOND À L’EXPRESSION RÉGULIÈRE** | **STRING**[`Retrait en magasin`]**OU**[`Retrait en magasin`]**EXPRESSION RÉGULIÈRE**[`Retrait en magasin`]|
| Vérifie si l’attribut de chaîne de caractères **ne correspond pas partiellement** à une chaîne de caractères **OU** une expression régulière saisie. | **NE CORRESPOND PAS À L’EXPRESSION RÉGULIÈRE *** | **STRING**[`Retrait en magasin`]**OU**[`Retrait en magasin`]**EXPRESSION RÉGULIÈRE**[`Retrait en magasin`]|
| Vérifie si l’attribut de chaîne **ne correspond pas** à une chaîne de caractères saisie| **N’EST PAS ÉGAL À ** | **STRING** |
| Vérifie si l’attribut de chaîne **existe** sur le profil d’un utilisateur | **N’EST PAS VIDE** | **S.O.** |
| Vérifie si l’attribut de chaîne de caractères **n’existe pas** sur le profil d’un utilisateur | **EST VIDE** | **‬S.O.‭** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
&#42;Lors de la segmentation à l’aide du filtre **NE CORRESPOND PAS À L’EXPRESSION RÉGULIÈRE** vous devez déjà avoir un attribut personnalisé avec une valeur attribuée dans ce profil utilisateur. Braze suggère d’utiliser la logique « OR » (OU) pour vérifier si un attribut personnalisé est vide pour s’assurer que les utilisateurs sont correctement ciblés.
{% endalert %}

{% alert tip %}
Pour en savoir plus sur la façon d’utiliser notre filtre d’expressions régulières, consultez la documentation sur les [expressions régulières compatibles Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
Plus de ressources sur les expressions régulières :
- [Braze et les expressions régulières]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Débogueur et testeur d’expression régulière](https://regex101.com/)
- [Didacticiel d’expression régulière](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

#### Tableaux
Les attributs de tableau sont appropriés pour stocker les listes d’informations associées à vos utilisateurs. Par exemple, le stockage en tableau des 100 derniers morceaux de contenu qu’un utilisateur a regardé permettrait une segmentation spécifique basée sur les intérêts.

Les tableaux d’attribut personnalisé sont des ensembles unidimensionnels ; les tableaux multidimensionnels ne sont pas pris en charge. **L’ajout d’un élément à un tableau d’attribut personnalisé ajoute l’élément à la fin du tableau, à moins qu’il ne soit déjà présent, auquel cas il passe de sa position actuelle à la fin du tableau.** Par exemple, si un tableau indiquant ['hotdog','hotdog','hotdog','pizza'] est importé, les attributs du tableau seront ['hotdog', 'pizza'], car nous ne prenons en charge que les valeurs uniques.

Si le tableau contient son nombre maximum d’éléments, le premier élément sera supprimé et le nouvel élément ajouté à la fin. Voici quelques exemples de code illustrant le comportement du tableau dans le SDK Web :

```
var abUser = appboy.getUser();
// initialise l'array pour cet utilisateur, en supposant une longueur maximale de favorite_foods est défini sur 4.
abUser.setCustomUserAttribute('favorite_foods', ['pizza', 'wings', 'pasta']); // => ['pizza', 'ailes', 'pâtes']
abUser.addToCustomAttributeArray('favorite_foods', 'fries'); // => ['pizza', 'ailes', 'pâtes', 'frites']
abUser.addToCustomAttributeArray('favorite_foods', 'pizza'); // => ['ailes', 'pâtes', 'frites', 'pizza']
abUser.addToCustomAttributeArray('favorite_foods', 'ice cream'); // => ['pâtes', 'frites', 'pizza', 'glace']

```

Le nombre maximum d’éléments dans les tableaux d’attributs personnalisés est par défaut de 25. Le maximum pour les tableaux individuels peut être augmenté jusqu’à 100. Si vous souhaitez que cette limite soit augmentée, contactez votre gestionnaire de services clients. Les tableaux dépassant le nombre maximum d’éléments seront tronqués pour contenir le nombre maximum d’éléments.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifie si l’attribut du tableau **inclut une valeur qui correspond exactement à** une valeur entrée| **INCLUT LA VALEUR** | **STRING** |
| Vérifie si l’attribut du tableau **n’inclut pas une valeur qui correspond exactement à** une valeur entrée | **N’INCLUT PAS LA VALEUR** | **STRING** |
| Vérifie si l’attribut du tableau **contient une valeur qui correspond partiellement à** une valeur entrée **OU** une Expression régulière | **CORRESPOND À L’EXPRESSION RÉGULIÈRE** | **STRING**[`Retrait en magasin`]**OU**[`Retrait en magasin`]**EXPRESSION RÉGULIÈRE**[`Retrait en magasin`]|
| Vérifie si l’attribut du tableau **a une valeur quelconque** | **A UNE VALEUR** | **S.O.** |
| Vérifie si l’attribut du tableau **est vide** | **EST VIDE** | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

>  Nous utilisons des [expressions régulières compatibles avec Perl (PCRE)][11].

#### Dates
Les attributs de date sont utiles pour enregistrer la dernière fois qu’une action spécifique a été effectuée, car ils vous permettent d’envoyer des contenus de ré-engagement à vos utilisateurs.

>  La dernière date à laquelle un événement personnalisé ou événement d’achat s’est produit est automatiquement enregistrée et ne doit pas être enregistrée en double avec un attribut de date personnalisé.

Les filtres temporels basés sur des dates relatives (p. ex., il y a plus d’un jour, il y a moins de 2 jours) mesurent 1 journée en tant que 24 heures. Toute campagne que vous exécutez à l’aide de ces filtres inclura tous les utilisateurs par incréments de 24 heures. Par exemple, l’option Dernière utilisation de l’application il y a plus d’un jour capturera tous les utilisateurs qui ont « utilisé l’application plus de 24 heures » à partir du lancement exact de la campagne. Il en va de même pour les campagnes définies avec des plages de dates plus longues. Ainsi, cinq jours après l’activation signifie les 120 heures précédentes.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifiez si l’attribut de date **est avant** une **date sélectionnée**| **AVANT** | **SÉLECTEUR DE DATE** |
| Vérifiez si l’attribut de date **est après** une **date sélectionnée**| **APRÈS** | **SÉLECTEUR DE DATE** |
| Vérifiez si l’attribut de date est postérieur à **il y a plus de X ****jours** | **PLUS DE ** | **IL Y A NOMBRE DE JOURS** |
| Vérifiez si l’attribut de date est antérieur à **il y a moins de X ****jours**| **MOINS DE** | **IL Y A NOMBRE DE JOURS** |
| Vérifiez si l’attribut de date est dans **plus de X ****jours dans le futur** | **DANS PLUS DE** | ** JOURS À L’AVENIR** |
| Vérifiez si l’attribut de date est dans **moins de X ****jours dans le futur** | **DANS MOINS DE** | ** JOURS À L’AVENIR**  |
| Vérifiez si l’attribut de date **existe** sur le profil d’un utilisateur | **EXISTE** | **S.O.** |
| Vérifiez si l’attribut de date **n’existe pas** sur le profil d’un utilisateur | **N’EXISTE PAS** | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Nombres entiers (standards ou incrémentaux) et décimaux (floats/doubles) {#integers}
Les attributs numériques incluent une grande variété de cas d’utilisation. Les attributs personnalisés basés sur un nombre entier incrémental sont utiles pour stocker le nombre de fois qu’une action ou un événement donné s’est produit. Les nombres entiers standards et les nombres décimaux ont de nombreuses utilisations, par exemple : (Enregistrer la pointure, le tour de taille, le nombre de fois qu’un utilisateur a regardé une certaine caractéristique ou catégorie de produit).
>  L’argent dépensé dans l’application ne doit pas être enregistré via cette méthode. Il vaut mieux l’enregistrer via nos [méthodes d’achat][4].

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifiez si l’attribut numérique **est supérieur à** un **nombre entier ou à une valeur décimale**| **PLUS DE ** | **NOMBRES ENTIERS** ou **DÉCIMAUX** |
| Vérifiez si l’attribut numérique **est inférieur à** un **nombre entier ou à une valeur décimale**| **MOINS DE** | **NOMBRES ENTIERS** ou **DÉCIMAUX** |
| Vérifiez si l’attribut numérique **est égal à** un **nombre entier ou à une valeur décimale**| **EXACTEMENT** | **NOMBRES ENTIERS** ou **DÉCIMAUX** |
| Vérifiez si l’attribut numérique **n’est pas égal à** un **nombre entier ou à une valeur décimale**| **N’EST PAS ÉGAL À** | **NOMBRES ENTIERS** ou **DÉCIMAUX** |
| Vérifier si l’attribut numérique **existe** sur le profil d’un utilisateur | **EXISTS** | **S.O.** |
| Vérifier si l’attribut numérique **n’existe pas** sur le profil d’un utilisateur | **DOES NOT EXIST** | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Booléen (Vrai/Faux)
Les attributs booléens sont utiles pour stocker des données binaires simples sur vos utilisateurs, comme le statut d’abonnement. Les options de saisie que nous proposons vous permettent de trouver des utilisateurs qui ont explicitement une variable définie sur Vrai ou Faux, en plus des personnes qui n’ont pas encore d’enregistrement pour cet attribut.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifier si la valeur booléenne **est** | **EST**  | **VRAI**, **FAUX**, **VRAI OU NON DÉFINI**, ou **FAUX OU NON DÉFINI** |
| Vérifie si la valeur booléenne **existe** sur le profil d’un utilisateur | **EXISTE**  | **S.O.** |
| Vérifie si la valeur booléenne **n’existe pas** sur le profil d’un utilisateur | **N’EXISTE PAS**  | **S.O.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Événements d’achat / suivi des revenus

L’utilisation de nos méthodes d’achat pour enregistrer les achats dans l’application établit la Valeur à vie (LTV) pour chaque profil utilisateur individuel. Ces données sont consultables sur notre page de revenus dans les séries temporelles.

| Options de segmentation | Filtre déroulant | Options d’entrée |
| ---------------------| --------------- | ------------- |
| Vérifiez si le total de dollars dépensé **est supérieur à **un **nombre entier ou une valeur décimale**| **SUPÉRIEUR À** | **NOMBRES ENTIERS** ou **DÉCIMAUX** |
| Vérifiez si le total de dollars dépensé **est inférieur à **un **nombre entier ou une valeur décimale**| **MOINS DE** | **NOMBRES ENTIERS** ou **DÉCIMAUX** |
| Vérifiez si le total de dollars dépensé **est égal à **un **nombre entier ou une valeur décimale**| **EXACTEMENT** | **NOMBRES ENTIERS** ou **DÉCIMAUX** |
| Vérifie si l’achat a été effectué **après la date X** | **APRÈS** | **DATE** |
| Vérifiez si l’achat a été effectué **avant la date X** | **AVANT** | **DATE** |
| Vérifiez si l’achat a été effectué **il y a plus de X jours** | **PLUS DE ** | **DATE** |
| Vérifie si l’achat a été effectué **il y a moins de X jours** | **MOINS DE** | **DATE** |
| Vérifie si l’achat a eu lieu **plus de X (Max = 50) fois** | **PLUS DE ** | dans les **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifie si l’achat a eu lieu **moins de X (Max = 50) fois** | **MOINS DE** | dans les **Y derniers jours (Y = 1,3,7,14,21,30)** |
| Vérifie si l’achat a eu lieu **exactement X (Max = 50) fois** | **EXACTEMENT** | dans les **Y derniers jours  (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

>  Si vous souhaitez segmenter sur le nombre de fois où un achat spécifique s’est produit, vous devez également enregistrer l’achat individuel en tant qu’[attribut personnalisé incrémental][12].

## Cas d’utilisation : application de taxi/partage de trajets {#example-case}
Dans cet exemple, prenons une application de taxi/partage de trajets (comme Hailo, Lyft, etc.) qui décide quelles données utilisateur collecter. Le brainstorming et les questions suivantes sont un excellent modèle à suivre pour les équipes de marketing et de développement. À la fin de cet exercice, les deux équipes doivent avoir une solide compréhension des événements et attributs personnalisés qu’elles devraient collecter pour essayer d’atteindre leur objectif.

**Question n° 1 : Quel est l’objectif ?**

Leur objectif est simple : ils veulent que les utilisateurs fassent des trajets en taxi via leur application.

**Question n° 2 : Quelles sont les étapes intermédiaires sur la voie de l’installation de l’application ?**

1. Il faut que les utilisateurs commencent le processus d’inscription et donnent leurs informations personnelles.
2. Il faut que les utilisateurs confirment leur inscription en entrant un code reçu via SMS dans l’application.
3. Ils doivent essayer de commander un taxi.
4. Pour commander un taxi, il faut des taxis disponibles au moment de leur recherche.

Ces actions peuvent ensuite être des tags pour les événements personnalisés suivants :

- Inscription commencée
- Inscription terminée
- Appels de taxis réussis
- Appels de taxis échoués

Une fois que les événements ont été définis, vous pouvez maintenant exécuter les campagnes suivantes :

1. Envoyer des messages aux utilisateurs qui ont commencé l’enregistrement, sans le terminer dans un certain délai.
2. Envoyer des messages de félicitations aux utilisateurs qui se sont abonnés.
3. Envoyer des excuses et des remises aux utilisateurs qui n’ont pas réussi à avoir un taxi pour un trajet.
4. Envoyer des remises aux utilisateurs qui ont pris de nombreux taxis pour les remercier leur fidélité.
5. Et beaucoup, beaucoup d’autres.

**Question n° 3 : Quelles autres informations pourrions-nous connaître sur nos utilisateurs qui informeront notre communication ?**

- Ont-ils ou non un crédit promotionnel ?
- La note moyenne qu’ils donnent à leurs chauffeurs ?
- Codes promotionnels uniques pour l’utilisateur ?

Ces caractéristiques peuvent ensuite être des tags pour les attributs personnalisés suivants :

- Solde de crédit promotionnel (type décimal)
- Note moyenne du chauffeur (Type Entier)
- Code promotionnel unique (Type String)

L’ajout de ces attributs vous permettrait d’envoyer des campagnes aux utilisateurs pour :

1. Rappeler aux utilisateurs qui n’ont pas utilisé l’application depuis 7 jours que leur compte est éligible pour une remise et qu’ils devraient revenir sur l’appli pour en profiter !
2. Envoyer des messages aux utilisateurs qui donnent de mauvaises notes aux conducteurs pour obtenir un retour direct des clients et savoir pourquoi ils n’ont pas apprécié leur trajet.
3. Utilisez nos [fonctionnalités de personnalisation et de templating][17] pour faire glisser l’attribut de Promotion Code unique dans la communication envoyée aux utilisateurs.

## Meilleures pratiques 

### Bonnes pratiques générales

#### Utiliser les propriétés de l’événement

- Donner à un événement personnalisé un nom qui décrit une action effectuée par un utilisateur
- Faire un usage optimal des propriétés d’événements personnalisés pour représenter des données importantes sur un événement
- Par exemple, plutôt que de capturer un événement personnalisé distinct pour regarder chacun des 50 films différents, il serait plus efficace de capturer simplement un film en tant qu’événement et d’avoir une propriété d’événement qui inclut le nom du film

### Bonnes pratiques de développement

#### Définir les ID utilisateur pour chaque utilisateur

Les ID utilisateur doivent être définis pour chacun de vos utilisateurs. Ils doivent être inchangés et accessibles lorsqu’un utilisateur ouvre l’application. Nous **vous recommandons** également vivement de fournir cet identifiant, car vous pourrez ainsi :

- Suivre vos utilisateurs sur les appareils et plateformes, améliorant la qualité de vos données comportementales et démographiques.
- Importer des données sur vos utilisateurs en utilisant notre [API de données utilisateur][9].
- Cibler des utilisateurs spécifiques avec notre [API de messagerie][10] pour les messages généraux et transactionnels.

Les identifiants d’utilisateur doivent comporter moins de 512 caractères ; ils doivent être privés et ne sont pas faciles à obtenir (p. ex., ils ne peuvent pas être une adresse e-mail ou un nom d’utilisateur simple). Si un tel identifiant n’est pas disponible, Braze attribue un identifiant unique à vos utilisateurs, mais il vous manquera les capacités énumérées pour les ID utilisateur. Vous devez éviter de définir des ID utilisateur pour les utilisateurs pour lesquels vous n’avez pas d’identifiant unique qui leur soit lié en tant qu’individus. La transmission d’un identifiant d’appareil n’offre aucun avantage par rapport au suivi automatique d’utilisateur anonyme que Braze propose par défaut. Voici quelques exemples d’identifiants utilisateur appropriés et inappropriés.

Bonnes options pour les ID utilisateur :

- Adresse e-mail hachée ou nom d’utilisateur unique
- Identifiant de base de données unique
- Identifiant Facebook

Ne pas utiliser comme ID utilisateur :

- ID du dispositif
- Numéro aléatoire ou ID de session
- N’importe quel ID non unique

#### Donnez des noms et des noms lisibles des événements personnalisés
Imaginez que vous êtes un marketeur qui commence à utiliser Braze un an ou deux après la mise en œuvre, lire une liste déroulante remplie de noms comme « usr_no_acct » sans contexte supplémentaire peut être déconcertant. Donner des noms identifiables et lisibles à votre événement et à vos attributs facilitera les choses pour tous les utilisateurs de votre plateforme. Tenez compte des meilleures pratiques suivantes :

- Ne commencez pas un événement personnalisé avec un caractère numérique. La liste déroulante est triée par ordre alphabétique et commence par un caractère numérique, ce qui rend le segment plus difficile à segmenter par votre filtre de choix
- Essayez, dans la mesure du possible, de ne pas utiliser les abréviations obscures ou le jargon technique
  - Example: `usr_ctry` peut être un nom de variable pour le pays d’un utilisateur dans une partie de code, mais l’attribut personnalisé doit être envoyé à Braze en tant que `user_country`, au moins pour apporter des précisions aux marketeurs qui utiliseront le tableau de bord par la suite.

#### Enregistrez les attributs uniquement lorsqu’ils sont modifiés
Nous comptons chaque attribut transmis à Braze comme point de données, même si l’attribut transféré contient la même valeur que celle enregistrée précédemment. Le fait de ne consigner les données que lorsqu’elles changent permet d’éviter une utilisation redondante des points de données et de garantir une expérience plus fluide en évitant les appels API inutiles.

#### Évitez les noms d’événements générés par programmation
Si vous créez constamment de nouveaux noms d’événements, il sera impossible de segmenter de façon significative vos utilisateurs. Vous devez généralement capturer des événements génériques (« A regardé une vidéo » ou « A lu un article ») plutôt que des événements très spécifiques tels que (« A regardé le style Gangnam » ou « A lu l’article : Les 10 meilleurs endroits pour déjeuner à Midtown Manhattan »). Les données spécifiques à propos de l’événement doivent être incluses comme propriété de l’événement, et non pas dans le cadre du nom de l’événement.

### Limitations et contraintes techniques
Soyez attentif aux limitations et contraintes suivantes lors de la mise en œuvre d’événements personnalisés :

#### Contraintes de longueur
Tous les événements personnalisés, les noms d’attributs personnalisés (clés) et les valeurs de chaîne d’événements personnalisées de 255 caractères ou plus seront tronqués. Idéalement, ils doivent être aussi courts que possible pour améliorer les performances réseau et de batterie de votre application. Si possible, limitez-les à 50 caractères.

#### Contraintes de contenu
Le contenu suivant sera découpé de manière programmatique à partir de vos attributs et événements. Veillez à ne pas utiliser ce qui suit :

- Espace blanc avant et arrière
- Retours à la ligne
- Tous les éléments qui ne sont pas des chiffres dans les numéros de téléphone
  - Example: « (732) 178-1038 » sera abrégé comme suit « 7321781038 »
- Les caractères non blancs doivent être convertis en espaces
- Le symbole $ ne doit pas être utilisé comme préfixe pour les événements personnalisés
- Toute valeur d’encodage UTF-8 non valide
  -  « Mon champ \x80 » sera abrégé comme suit « Mon champ »"

#### Clés réservées
Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés de l’événement personnalisées :

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

#### Définitions de valeur

- Les valeurs entières comportent 64 bits
- Les décimales comportent 15 chiffres par défaut.

### Analyse d’un champ de nom générique

Si seul un champ générique existe pour un utilisateur (p. ex., « JohnDoe »), vous pouvez attribuer ce titre entier à l’attribut Prénom de votre utilisateur. De plus, vous pouvez essayer d’analyser à la fois le prénom et le nom de l’utilisateur en utilisant des espaces, mais cette dernière méthode comporte le risque potentiel de mal nommer certains de vos utilisateurs.

[4]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#purchase-events--revenue-tracking
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[9]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[10]: {{site.baseurl}}/developer_guide/rest_api/messaging/
[11]: http://www.regextester.com/pregsyntax.html
[12]: #integers
[16]: #example-case
[17]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[18]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
