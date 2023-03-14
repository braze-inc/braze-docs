---
nav_title: Capturer les utilisateurs inactifs
article_title: Capturer les utilisateurs inactifs
page_order: 1
page_type: tutorial
description: "Le présent article pratique aborde le problème des utilisateurs inactifs et comment utiliser efficacement les campagnes Braze pour ré-engager ces utilisateurs."
tool:
  - Segments
  - Campagnes

---

# Capturer les utilisateurs inactifs

> Le présent article pratique aborde le problème des utilisateurs inactifs et comment utiliser efficacement les campagnes Braze pour ré-engager ces utilisateurs.

Si votre audience s’érode, il est crucial d’essayer de la courtiser. En reconnaissant cette nécessité, Braze facilite la mise en place de campagnes de ré-engagement récurrentes automatisées pour capturer les utilisateurs inactifs. Vous pouvez choisir le délai de ré-engagement et la récurrence qui conviennent le mieux à votre application, mais pour les besoins de la démonstration, nous allons commencer avec un plan de ré-engagement de 14 jours.

Pour en savoir plus sur le ciblage des utilisateurs, consultez notre [Cours d’apprentissage Braze](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sur la configuration de campagne !

## Étape 1 : Segmentation

Nous allons d’abord créer un segment pour cibler les utilisateurs qui n’ont pas utilisé l’application au cours des deux dernières semaines, en utilisant les filtres suivants :

- Dernière utilisation de l’application il y a plus de 2 semaines
- Dernière utilisation de l’application il y a moins de 3 semaines

![][1]

N’oubliez pas de nommer le segment de manière simple et dont vous vous souviendrez, comme « Utilisateurs inactifs – 2 semaines ». Étant donné que nous définirons la campagne pour qu’elle se répète chaque semaine, nous voulons nous assurer qu’au moins une semaine d’utilisateurs soit capturée dans le segment. C’est pourquoi nous avons sélectionné des utilisateurs qui ont utilisé l’application il y a deux à trois semaines.

## Étape 2 : Création de la campagne

Ensuite, cliquez sur **Create Campaign** (Créer une campagne) et choisissez le type de campagne que nous enverrons à ce segment. Dans cet exemple, nous allons créer une [campagne de notification push][6].

![][5]

Nous nommerons la campagne **Message aux utilisateurs inactifs - 2 semaines** et sélectionnerons le segment. Ensuite, nous allons créer le contenu de notre message. Dans cet exemple, nous ciblerons uniquement les utilisateurs iOS, mais vous pouvez utiliser Braze pour les notifications push Android et iOS. Plus la dernière fois où l’utilisateur était dans l’application est proche, plus il est important d’être thématique et pertinent. Quand vous envoyez un message à un utilisateur après deux semaines sans utilisation de l’application, il est important de mettre en évidence le contenu pertinent et les avantages à utiliser l’application.

![][2]

Ensuite, nous allons créer un calendrier récurrent pour envoyer notre message hebdomadaire le jeudi à 17 h 45 en utilisant la [livraison selon le fuseau horaire local][4] dans les **Options de planification basée sur le temps**. Nous vous recommandons de consulter le graphique de vos sessions pour cibler les utilisateurs juste avant les périodes d’utilisation élevée. Cela garantit que vous essayez de ré-engager les personnes lorsqu’elles sont les plus susceptibles d’utiliser l’application. Vous pouvez le modifier plus tard et tester votre hypothèse initiale.

![][3]

Maintenant, vous êtes prêt à envoyer la campagne. Confirmez les paramètres sur la dernière page de l’assistant et cliquez sur **Lancer la campagne** !

[1]: {% image_buster /assets/img_archive/2weeklapse1.png %}
[2]: {% image_buster /assets/img_archive/2weeklapse3.png %}
[3]: {% image_buster /assets/img_archive/2weeklapse4.png %}
[4]: {{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer
[5]: {% image_buster /assets/img_archive/2weeklapse2.png %}
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message