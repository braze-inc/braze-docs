---
nav_title: Analyses du flux d'actualités
article_title: Flux d'actualités Analytics et données de redistribution
page_order: 10
page_type: Référence
description: "Cet article de référence couvre les analyses de News Feed et divers filtres connexes."
tool:
  - Rapports
channel: fil d'actualité
---

# Analyses

Similaire aux campagnes planifiées, l'outil Flux d'actualités est fourni avec un tableau de bord d'analyse pour surveiller les impressions, les clics et les taux de clics. En cliquant sur un message spécifique de News Feed dans votre tableau de bord, une foule d'analyses visuelles peuvent être triées. En haut de la page, vous pouvez sélectionner votre plage de données et voir une visualisation rapide de vos indicateurs les plus importants. De plus, vous pouvez voir des détails sur ce message de flux de nouvelles, comme quand il a été envoyé et à qui il a été envoyé.

!\[Top Analytiques du fil d'actualités\]\[19\]

En faisant défiler la page, vous pouvez voir une plus grande répartition de vos clics et des impressions jour après jour. Les clics/impressions totaux sont facilement comparés à des clics/impressions uniques à travers des diagrammes de ligne, tandis que le taux de clics est présenté sous la forme d'un diagramme à barres interactif.

![InfoFeed Analytics en bas[20]

## Reciblage des données

Vous pouvez tirer parti des données de Braze sur lesquelles les utilisateurs interagissent avec votre fil d'actualité via des filtres de segment qui vous permettent de recibler des comportements spécifiques.

### Filtre d'impressions de flux

Braze automatiquement les traces lorsque les utilisateurs consultent le flux et combien de fois ils l'ont vu. Il y a deux filtres disponibles :

- Dernier fil d'actualité consulté
- Nombre de nouvelles vues de flux

'Dernier fil d'actualité consulté' est un moyen efficace d'utiliser d'autres canaux pour attirer les utilisateurs dans le flux. Cela peut être facilement fait avec les notifications push et in-app. Braze a vu plus de 100 % d'augmentation dans les impressions de News Feed avec un ciblage efficace. Au fur et à mesure que la prise de conscience des aliments augmente, ces bénéfices sont maintenus.

Le 'Nombre de Fil d'Actualités' peut être utilisé pour cibler les utilisateurs qui n'ont jamais vu le flux ou qui n'ont jamais vu le flux pour encourager plus d'impressions de vos cartes.

Considérez l'utilisation de ces filtres en tandem ou avec d'autres filtres pour créer un appel à l'action encore plus ciblé.

### Filtre de carte cliqué

Vous pouvez créer des segments en fonction de la façon dont les utilisateurs ont interagi avec des cartes spécifiques dans le flux. Le filtre se trouve dans la section Retargeting de la liste de filtres et appelé Clicked Card.

### A cliqué sur le filtre de carte

- Fonctionne bien pour les utilisateurs de retarget qui ont cliqué sur une carte, mais pas suivi lors de votre appel à l'action.
- Il est également utile de recibler les utilisateurs avec un contenu connexe qui pourrait les intéresser.
- Vous pouvez également utiliser ce filtre pour cibler les utilisateurs qui n'ont pas cliqué sur une carte. Ce filtre peut être appliqué à des cartes spécifiques pour qu'elles disparaissent du flux d'un utilisateur après avoir cliqué dessus.
  - Pour configurer cela, après avoir créé une carte, retournez en arrière et éditez le segment cible pour inclure "N'a pas cliqué VOTRE NOUVELLE CARTE".
  - Après avoir cliqué sur la carte, la carte quittera automatiquement le flux au début de la prochaine session de l'utilisateur.
  - Évitez de trop utiliser ce ciblage car l'utilisateur peut se retrouver avec des flux vides. La meilleure pratique consiste à utiliser une combinaison de contenu statique et automatiquement retiré.
- Il fonctionne aussi bien pour retarger les utilisateurs qui ne cliquent pas sur une carte pour suivre un autre appel à l'action.

!\[N'a pas cliqué sur l'exemple de carte\]\[14\]
[19]: {% image_buster /assets/img_archive/braze_newsfeedanalytics.png %} [20]: {% image_buster /assets/img_archive/braze_newsfeedanalytics2.png %} [14]: {% image_buster /assets/img_archive/braze_newsfeedsegment.png %}
