---
nav_title: Intelligence Suite
article_title: Intelligence Suite
page_order: 10
layout: dev_guide
search_rank: 12
guide_top_header: "Intelligence Suite"
guide_top_text: "Intelligence Suite de Braze vous permet d’automatiser la prise de décision avec des informations basées sur les données. De l’heure de livraison au test multivarié, les marques peuvent utiliser ces outils et fonctionnalités pour créer des expériences dynamiques et cross-canal, afin d’optimiser l’ensemble. <br> <br> La suite d'outils Intelligence Suite est composée de trois fonctionnalités principales : Timing Intelligent, Canal intelligent et Sélection intelligente."
description: "Intelligence Suite de Braze vous permet d’automatiser la prise de décision avec des informations basées sur les données. De l’heure de livraison au test multivarié, les marques peuvent utiliser ces outils et fonctionnalités pour créer des expériences dynamiques et cross-canal, afin d’optimiser l’ensemble."

Tool:
  - Dashboard

guide_featured_title: "Outils et fonctionnalités"
guide_featured_list:
- name: Timing intelligent
  link: /docs/user_guide/brazeai/intelligence/intelligent_timing/
  image: /assets/img/braze_icons/clock.svg
- name: Canal intelligent
  link: /docs/user_guide/brazeai/intelligence/intelligent_channel/
  image: /assets/img/braze_icons/mail-04.svg
- name: Sélection intelligente
  link: /docs/user_guide/brazeai/intelligence/intelligent_selection/
  image: /assets/img/braze_icons/hearts.svg

guide_menu_title: "Additional resources"
guide_menu_list:
- name: FAQ Intelligence
  link: /docs/user_guide/brazeai/intelligence/faqs/
  image: /assets/img/braze_icons/annotation-question.svg


---

## Cas d’utilisation

La suite Intelligence offre des fonctionnalités puissantes pour analyser l'historique des utilisateurs et les performances des campagnes et des Canvas, puis procéder à des ajustements automatiques pour augmenter l'engagement, l'audience et les conversions. Pour quelques exemples de la manière dont ces fonctionnalités peuvent bénéficier à différents secteurs, consultez les cas d'utilisation ci-dessous.

### eCommerce

- **Ventes flash :** Utilisez le [filtre Canal intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) pour étudier l'historique des utilisateurs afin d'identifier ceux qui sont plus réactifs aux notifications push qu'aux e-mails, puis envoyez des notifications push et des e-mails aux utilisateurs concernés. En option, sélectionnez un canal spécifique pour les utilisateurs qui ne disposent pas de suffisamment de données pour déterminer leur canal préféré.
- **Bannières promotionnelles :** Utilisez la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) pour analyser les performances de différentes bannières promotionnelles dans une campagne récurrente, puis sélectionnez et envoyez automatiquement la bannière qui génère les taux de clics les plus élevés.

### Voyage

- **Offres de forfaits :** Utilisez la sélection intelligente pour tester différentes offres de forfaits de voyage dans un Canvas récurrent et déplacez progressivement le trafic du Canvas vers la variante la plus performante afin d'obtenir des taux de réservation plus élevés.
- **Offres de voyages :** Utilisez le filtre de canal intelligent pour envoyer des offres de voyage personnalisées via le canal le plus actif d'un utilisateur, tel que l'e-mail ou le SMS, maximisant ainsi la probabilité qu'il s'engage dans votre envoi de messages.

### Divertissement

- **Promotion de nouveau contenu :** Utilisez le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) pour envoyer des notifications sur les nouveaux films, émissions, musiques et autres types de contenu lorsque les utilisateurs sont le plus susceptibles d'ouvrir votre envoi de messages.
- **Achats dans le jeu :** Utilisez la sélection intelligente pour tester différents messages promotionnels pour les achats dans le jeu et sélectionnez automatiquement celui qui génère les taux de conversion les plus élevés.

### Restaurant à service rapide

Imaginons que nous travaillons au SandwichEmperor, un restaurant rapide qui propose un nouveau plat à durée limitée : le Royal Roast. Nous utiliserons deux fonctionnalités de la suite Intelligence pour envoyer des promotions personnalisées dans un Canvas.

#### Utilisez le timing intelligent pour savoir quand envoyer des notifications

Nous utiliserons le timing intelligent pour analyser les interactions passées de nos utilisateurs avec notre appli et chaque canal d'envoi de messages, puis nous sélectionnerons automatiquement le meilleur moment pour promouvoir le Royal Roast auprès de chaque utilisateur. Certains utilisateurs peuvent recevoir la promotion dans l'après-midi, d'autres dans la soirée. 

Pour les utilisateurs qui n'ont pas suffisamment d'interactions passées à analyser, nous prévoyons un moment de repli : le moment le plus populaire de l'utilisation de l'application parmi tous les utilisateurs.

![Paramètres de livraison du timing intelligent pour une étape Message.][1]

#### Utilisez la sélection intelligente pour sélectionner la promotion

Pour les messages promotionnels proprement dits, nous utiliserons la sélection intelligente afin de tester trois messages différents (notification push, e-mail et SMS) pour le Royal Roast. La sélection intelligente analysera la performance de tous nos messages promotionnels deux fois par jour, puis enverra progressivement davantage les messages les plus performants et moins les autres.

Une fois que la sélection intelligente a recueilli suffisamment de données pour déterminer le message le plus performant, elle utilisera ce message dans 100 % des envois futurs.

![Section de test A/B d'un canvas avec sélection intelligente activée.][3]

#### Lancer le canvas

Grâce au timing intelligent et à la sélection intelligente, nous avons mis en place nos promotions Royal Roast afin d'optimiser le timing et l'envoi des messages. Nous pouvons lancer notre canvas et observer l’adaptation de nos envois en fonction des préférences des utilisateurs.

[1]: {% image_buster /assets/img/intelligence_suite1.png %}
[3]: {% image_buster /assets/img/intelligent_selection_canvas.png %}
