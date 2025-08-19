---
nav_title: "Tutoriel : Restaurant à service rapide"
article_title: "Tutoriel sur l'Intelligence Suite"
page_order: 10
search_rank: 12
description: "Vous êtes nouveau dans la suite intelligence de Braze ? Commencez par ce tutoriel."
tool:
  - Dashboard
---

# Tutoriel sur l'Intelligence Suite

> Nouveau dans la Braze Intelligence Suite ? Commencez par ce tutoriel ! Pour plus d'informations générales, voir [Intelligence Suite.]({{site.baseurl}}/user_guide/brazeai/intelligence/)

## Tutoriel : Restaurant à service rapide

Imaginons que nous travaillons au SandwichEmperor, un restaurant rapide qui propose un nouveau plat à durée limitée : le Royal Roast. Nous utiliserons deux fonctionnalités de la suite Intelligence pour envoyer des promotions personnalisées dans un Canvas.

### Étape 1 : Utilisez le timing intelligent pour savoir quand envoyer des notifications

Nous utiliserons le timing intelligent pour analyser les interactions passées de nos utilisateurs avec notre appli et chaque canal d'envoi de messages, puis nous sélectionnerons automatiquement le meilleur moment pour promouvoir le Royal Roast auprès de chaque utilisateur. Certains utilisateurs peuvent recevoir la promotion dans l'après-midi, d'autres dans la soirée. 

Pour les utilisateurs qui n'ont pas suffisamment d'interactions passées à analyser, nous prévoyons un moment de repli : le moment le plus populaire de l'utilisation de l'application parmi tous les utilisateurs.

![Paramètres de réception/distribution intelligente pour une étape du message.]({% image_buster /assets/img/intelligence_suite1.png %})

### Étape 2 : Utilisez la sélection intelligente pour sélectionner la promotion

Pour les messages promotionnels proprement dits, nous utiliserons la sélection intelligente afin de tester trois messages différents (notification push, e-mail et SMS) pour le Royal Roast. La sélection intelligente analysera la performance de tous nos messages promotionnels deux fois par jour, puis enverra progressivement davantage les messages les plus performants et moins les autres.

Une fois que la sélection intelligente a recueilli suffisamment de données pour déterminer le message le plus performant, elle utilisera ce message dans 100 % des envois futurs.

![Section de test A/B d'un canvas avec sélection intelligente activée.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

### Étape 3 : Lancer le canvas

Grâce au timing intelligent et à la sélection intelligente, nous avons mis en place nos promotions Royal Roast afin d'optimiser le timing et l'envoi des messages. Nous pouvons lancer notre canvas et observer l’adaptation de nos envois en fonction des préférences des utilisateurs.
