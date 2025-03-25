---
nav_title: Analyse du fil d’actualité
article_title: Analyse du fil d’actualité et données de reciblage
page_order: 10
page_type: reference
description: "Cet article de référence aborde l’analyse du fil d’actualité et plusieurs filtres qui y sont associés."
tool: 
- Reports
channel: news feed
hidden: true

---

# Analyse du fil d’actualité

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Comme pour les campagnes programmées, l’outil Fil d’actualité inclut un tableau de bord analytique qui vous permet de surveiller les impressions, les clics et les taux de clics. Vous pouvez consulter de nombreuses analyses visuelles en cliquant sur un message de fil d’actualité dans votre tableau de bord. 

En haut de la page, vous pouvez sélectionner une période pour vos données et consulter un bref visuel de vos indicateurs les plus importantes. Vous y trouverez également les informations de ce message de fil d’actualité, par exemple le moment auquel il a été envoyé et à qui il a été envoyé.

![Informations et analyses du fil d’actualité.][19]

Faites défiler la page vers le bas pour voir une répartition plus détaillée de vos clics et impressions quotidiens. Le total des clics/impressions peut être facilement comparé aux clics et impressions uniques dans des graphiques en courbes, tandis que le taux de clics est présenté sous la forme d’un graphique en barres interactif.

![Graphique de répartition des performances.][20]

## Données de reciblage

Vous pouvez exploiter les données Braze sur les utilisateurs qui interagissent avec votre fil d'actualité via des filtres de segmentation qui vous permettent de recibler des comportements spécifiques.

### Filtre des impressions du fil d’actualité

Braze suit automatiquement le moment où les utilisateurs voient votre fil d’actualité et combien de fois ils l’ont vu. Deux filtres sont disponibles :

- Dernier fil d’actualité vu
- News Feed View Count (Nombre de vues du fil d’actualité)

L’option **Dernier fil d’actualité vu** est un moyen efficace d'utiliser d'autres canaux pour attirer à nouveau les utilisateurs dans le fil d'actualité. Cela peut se faire facilement en utilisant des notifications push et des messages dans l’application. Braze a observé plus de 100 % d’augmentation du nombre d’impressions des fils d’actualité grâce à un ciblage efficace. Ces avantages se maintiennent à mesure que la notoriété de votre fil d’actualité augmente.

Le **nombre de vues du fil d'actualité** peut être utilisé pour cibler les utilisateurs qui n'ont jamais consulté le fil d'actualité ou qui le consultent rarement, afin d'encourager un plus grand nombre d'impressions de vos cartes.

Pensez à utiliser ces filtres avec d’autres pour créer un appel à l’action encore plus ciblé.

### Filtre Carte cliquée

Vous pouvez créer des segments en fonction de la manière dont les utilisateurs ont interagi avec certaines cartes de vote fil d’actualité. Le filtre Clicked Card (Carte cliquée) se trouve dans la section Retargeting (Reciblage) de la liste des filtres.

### Filtre Has clicked card

- Le filtre Has clicked card (A cliqué sur la carte) fonctionne bien pour recibler les utilisateurs qui ont cliqué sur une carte, mais qui n’ont pas suivis votre appel à l’action.
- Il est également utile de recibler les utilisateurs en leur envoyant des contenus associés susceptibles de les intéresser.
- Vous pouvez également utiliser ce filtre pour cibler les utilisateurs qui n’ont pas cliqué sur une carte. Ce filtre peut être appliqué à des cartes spécifiques afin qu’elles disparaissent du fil d’un utilisateur après qu’il ait cliqué dessus.
  - Pour ce faire, après avoir créé une carte, revenez en arrière et modifiez le segmentation cible pour y inclure les **Has non cliqués.**
  - Lorsqu’un utilisateur clique sur la carte, la carte sera automatiquement retirée du fil au début de la prochaine session de l’utilisateur.
  - Évitez de surutiliser ce type de ciblage, car votre utilisateur pourrait se retrouver avec un fil d’actualité complètement vide. Une bonne pratique à suivre consiste à combiner du contenu statique et du contenu supprimé de manière automatique.
- Cela fonctionne bien pour recibler les utilisateurs qui ne cliquent pas sur une carte en leur envoyant un autre appel à l’action.

![Exemple d’un filtre de segment montrant les utilisateurs qui n’ont pas cliqué sur la carte « Santé ! Les choses à faire et à ne pas faire pour porter un toast ».][14]


[19]: {% image_buster /assets/img_archive/braze_newsfeedanalytics.png %}
[20]: {% image_buster /assets/img_archive/braze_newsfeedanalytics2.png %}
[14]: {% image_buster /assets/img_archive/braze_newsfeedsegment.png %}
