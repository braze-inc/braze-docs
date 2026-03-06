---
nav_title: "Tutoriel : Restaurant rapide"
article_title: Tutoriel Intelligence Suite
page_order: 10
search_rank: 12
description: "Vous débutez avec la Braze Intelligence Suite ? Commencez par ce tutoriel."
tool:
  - Dashboard
---

# Tutoriel Intelligence Suite

> Vous débutez avec la Braze Intelligence Suite ? Commencez par ce tutoriel ! Pour des informations plus générales, consultez la [Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/).

## Tutoriel : Restaurant rapide

Imaginons que nous travaillons chez SandwichEmperor, un restaurant rapide qui propose un nouvel article au menu en temps limité : le Royal Roast. Nous allons utiliser deux fonctionnalités de la Intelligence Suite pour envoyer des promotions personnalisées dans un Canvas.

### Étape 1 : Utiliser le timing intelligent pour le moment d'envoi des notifications

Nous utilisons le timing intelligent pour analyser les interactions passées de nos utilisateurs avec notre application et chaque canal de messagerie, puis sélectionner automatiquement le meilleur moment pour promouvoir le Royal Roast auprès de chaque utilisateur. Certains utilisateurs pourraient recevoir la promotion l'après-midi, d'autres le soir.

Nous fournissons une heure de repli pour les utilisateurs qui n'ont pas assez d'interactions passées à analyser : l'heure la plus populaire d'utilisation de l'application parmi tous les utilisateurs.

![Paramètres de diffusion du timing intelligent pour une étape Message.]({% image_buster /assets/img/intelligence_suite1.png %})

### Étape 2 : Utiliser la sélection intelligente pour choisir la promotion

Pour les messages promotionnels proprement dits, nous utilisons la sélection intelligente pour tester trois messages différents (notification push, e-mail et SMS) pour le Royal Roast. La sélection intelligente analyse les performances de tous nos messages promotionnels deux fois par jour, puis envoie progressivement davantage des meilleurs messages et moins des autres.

Une fois que la sélection intelligente a rassemblé suffisamment de données pour déterminer le meilleur message, elle utilisera ce message pour 100 % des envois futurs.

![Section test A/B d'un Canvas avec la sélection intelligente activée.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

### Étape 3 : Lancer le Canvas

Avec le timing intelligent et la sélection intelligente, nous avons configuré nos promotions Royal Roast pour qu'elles soient optimisées en termes de moment et de message. Nous pouvons lancer notre Canvas et observer comment les envois s'adaptent aux préférences des utilisateurs.
