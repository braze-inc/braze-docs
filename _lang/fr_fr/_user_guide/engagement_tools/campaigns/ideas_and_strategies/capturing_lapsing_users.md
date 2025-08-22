---
nav_title: Capturer les utilisateurs inactifs
article_title: Capturer les utilisateurs inactifs
page_order: 1
page_type: tutorial
description: "Le présent article pratique aborde le problème des utilisateurs inactifs et comment utiliser efficacement les campagnes Braze pour ré-engager ces utilisateurs."
tool:
  - Segments
  - Campaigns

---

# Capturer les utilisateurs inactifs

> Si votre audience s’érode, il est crucial d’essayer de la courtiser. Avec Braze, vous pouvez créer des campagnes de réengagement récurrentes et automatisées pour capturer les utilisateurs inactifs. Vous pouvez choisir le délai de ré-engagement et la récurrence qui conviennent le mieux à votre application, mais pour les besoins de la démonstration, nous allons commencer avec un plan de ré-engagement de 14 jours.

Pour en savoir plus sur le ciblage des utilisateurs, consultez notre [cours d'apprentissage Braze](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sur la configuration des campagnes !

## Étape 1 : Segmentation des utilisateurs

Tout d'abord, nous allons créer un segment pour cibler les utilisateurs qui n'ont pas utilisé votre application au cours des deux dernières semaines, en utilisant les filtres suivants :

- **Dernière utilisation de l’application** il y a plus de 2 semaines
- **Dernière utilisation de l’application** il y a moins de 3 semaines

![]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Nommez le segment de manière à ce qu'il soit facile à mémoriser, par exemple "Utilisateurs abandonnés - 2 semaines". Étant donné que nous créons la campagne pour qu’elle se répète chaque semaine, nous voulons nous assurer qu’au moins une semaine d’utilisateurs sera capturée dans le segment. C’est pourquoi nous avons sélectionné des utilisateurs qui ont utilisé l’application il y a deux à trois semaines.

## Étape 2 : Créer une campagne

Ensuite, cliquez sur **Créer une campagne** et choisissez le type de campagne que nous allons envoyer à ce segment. Dans cet exemple, nous allons créer une nouvelle [campagne push.]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message)

![]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Nous nommerons la campagne « Message aux utilisateurs inactifs - 2 semaines », puis nous créerons le contenu de notre message. Dans cet exemple, nous ciblerons uniquement les utilisateurs iOS, mais vous pouvez utiliser Braze pour les notifications push Android et iOS. 

Plus la dernière fois où l’utilisateur était dans l’application est proche, plus il est important d’être thématique et pertinent. Lorsque vous envoyez un message à un utilisateur après deux semaines sans utilisation de l’application, il est important de mettre en évidence le contenu pertinent et les avantages à utiliser l’application.

![]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

Ensuite, nous allons créer une planification récurrente pour envoyer notre message hebdomadaire le jeudi à 17 h 45 en utilisant la [réception/distribution selon l'heure locale]({{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer) dans les **options de planification basée sur l'heure**. Nous vous recommandons de consulter le graphique de vos sessions pour cibler les utilisateurs juste avant les périodes d’utilisation élevée. Cela garantit que vous essayez de ré-engager les personnes lorsqu’elles sont les plus susceptibles d’utiliser l’application. Vous pouvez le modifier plus tard et tester votre hypothèse initiale.

![]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## Étape 3 : Lancer la campagne

Maintenant, vous êtes prêt à envoyer la campagne. Vérifiez les paramètres sur la dernière page de l’outil de création et cliquez sur **Lancer la campagne** !

