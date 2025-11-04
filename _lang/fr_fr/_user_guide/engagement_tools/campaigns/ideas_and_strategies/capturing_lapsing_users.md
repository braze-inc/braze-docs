---
nav_title: Capturer les utilisateurs en déchéance
article_title: Capturer les utilisateurs absents
page_order: 1
page_type: tutorial
description: "Cet article pratique aborde la question des utilisateurs perdus et la manière d'utiliser efficacement les campagnes de Braze pour réengager ces utilisateurs."
tool:
  - Segments
  - Campaigns

---

# Capturer les utilisateurs en déchéance

> Si votre audience diminue, il est essentiel de tenter de la reconquérir. Avec Braze, vous pouvez implémenter des campagnes de réengagement récurrentes et automatisées pour capter les utilisateurs défaillants. Vous pouvez choisir le délai de réengagement et la récurrence qui conviennent le mieux à votre application, mais pour démontrer, nous allons commencer avec un plan de réengagement de 14 jours.

Pour en savoir plus sur le ciblage des utilisateurs, consultez notre [cours d'apprentissage Braze](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sur la configuration des campagnes !

## Étape 1 : Segmentation des utilisateurs

Tout d'abord, nous allons créer un segment pour cibler les utilisateurs qui n'ont pas utilisé votre application au cours des deux dernières semaines, en utilisant les filtres suivants :

- **Dernière utilisation App** il y a plus de 2 semaines
- **Dernière utilisation App** il y a moins de 3 semaines

\![]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Nommez le segment de manière à ce qu'il soit facile à mémoriser, par exemple "Utilisateurs abandonnés - 2 semaines". Comme nous implémentons la campagne sur une base hebdomadaire, nous voulons nous assurer qu'il y a au moins une semaine d'utilisateurs capturés dans la segmentation. C'est pourquoi nous avons sélectionné des utilisateurs qui ont utilisé l'application pour la dernière fois il y a deux à trois semaines.

## Étape 2 : Créer une campagne

Ensuite, cliquez sur **Créer une campagne** et choisissez le type de campagne que nous allons envoyer à ce segment. Dans cet exemple, nous allons créer une nouvelle [campagne push.]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message)

\![]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Nous nommerons la campagne "Message aux utilisateurs abandonnés - 2 semaines", puis nous créerons le contenu de notre message. Dans cet exemple, nous ne ciblerons que les utilisateurs iOS, mais vous pouvez utiliser Braze pour les notifications push Android et iOS. 

Plus l'importation d'utilisateurs dans l'appli est proche de la dernière fois, plus il est important d'être d'actualité et pertinent. Lorsque vous envoyez un message à un utilisateur après deux semaines de non-utilisation de l'application, il est important de faire remonter à la surface du contenu pertinent et de mettre en avant les avantages de l'utilisation de l'application.

\![]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

Ensuite, nous allons créer une planification récurrente pour envoyer notre message hebdomadaire le jeudi à 17 h 45 en utilisant la [réception/distribution]({{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer) selon l' [heure locale]({{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer) dans les **options de planification basée sur l'heure**. Nous vous recommandons d'examiner votre graphique de sessions pour cibler les utilisateurs juste avant les périodes de forte utilisation. Ainsi, vous vous assurez de tenter de réengager les gens au moment où ils sont le plus susceptibles d'utiliser l'appli. Vous pouvez modifier ce point ultérieurement et tester votre hypothèse initiale.

\![]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## Étape 3 : Lancer la campagne

Vous êtes maintenant prêt à envoyer la campagne. Confirmez les paramètres sur la dernière page du compositeur et cliquez sur **Lancer la campagne**!

