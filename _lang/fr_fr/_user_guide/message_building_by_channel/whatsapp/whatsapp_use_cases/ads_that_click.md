---
nav_title: "Les publicités qui cliquent sur WhatsApp"
article_title: Les publicités qui cliquent sur WhatsApp
page_order: 1
description: "Cet article de référence fournit un guide étape par étape pour la configuration et l'utilisation des publicités qui cliquent sur WhatsApp."
page_type: reference
alias: /whatsapp_use_cases/
channel:
  - WhatsApp
---

# Les publicités qui cliquent sur WhatsApp

> Cette page fournit un guide étape par étape pour la configuration et l'utilisation de Teams That Click sur WhatsApp, afin que vous et votre équipe puissiez élever votre programme WhatsApp.

Les publicités qui cliquent sur WhatsApp sont un moyen efficace d'apporter des clients nouveaux et existants à partir des publicités Meta sur Facebook, Instagram ou d'autres plateformes. Utilisez ces annonces pour promouvoir vos produits et services tout en sensibilisant les utilisateurs à votre présence sur WhatsApp.

Une publicité Facebook de Calorie Rocket annonçant la réception/distribution gratuite, et la conversation WhatsApp correspondante qui se produit lorsqu'un utilisateur sélectionne le bouton de la publicité.]({% image_buster /assets/img/whatsapp/ads_that_click_whatsapp.png %}){: style="max-width:70%;"}

## Configurer des publicités qui cliquent sur WhatsApp

1. Dans le gestionnaire de publicités Meta, créez une publicité sur Facebook, Instagram ou d'autres plateformes en suivant le guide étape par étape [Comment créer des publicités qui cliquent sur WhatsApp](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp). **Ne** configurez **pas** de réponses automatisées ; vous le ferez dans Braze.

\![Gestionnaire d'annonces avec un compositeur pour créer une annonce d'engagement.]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

Lors de la configuration du message prérempli, qui sera envoyé par l'utilisateur à votre compte WhatsApp Business, incluez un mot ou une phrase spécifique que vous utiliserez pour déclencher une réponse propre à l'annonce en question. Dans cet exemple, une application de livraison de nourriture utilise "réception/distribution gratuite" parce que cela est promu dans leur publicité. 

!compositeur de modèles du gestionnaire d'annonces avec un message pré-rempli "Je veux une réception/distribution gratuite".]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
Indiquez clairement dans la description de l'annonce que le fait de cliquer sur l'annonce permettra de démarrer une conversation avec votre marque en utilisant des phrases telles que "Chat now on WhatsApp".
{% endalert %}

{: start="2"}
2\. Dans Braze, configurez un Canvas basé sur l'action où l'option basée sur l'action est **Envoyer un message entrant WhatsApp** et le corps du message est “YOUR_TRIGGER_WORD”. Dans cet exemple, une appli de livraison/distribution de nourriture utilise " réception/distribution gratuite ".

Planification d'entrée pour un Braze Canvas basé sur l'action, avec l'événement déclencheur "Envoyer un message entrant WhatsApp" et un corps de message qui correspond à l'expression régulière "réception/distribution gratuite".]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3\. Configurez un message de réponse dans le canvas qui s'envoie immédiatement après que le client est entré dans le canvas (par exemple, sans délai). Bien que le fait de cliquer sur l'annonce constitue techniquement un abonnement, nous vous recommandons de configurer votre message de réponse de manière à demander à l'utilisateur s'il souhaite recevoir à l'avenir des messages marketing de votre part sur WhatsApp. 

{% alert tip %}
Configurez votre message de réponse avec des réponses rapides (telles que "Oui" ou "Non merci") afin que les utilisateurs puissent rapidement indiquer s'ils souhaitent s'abonner.
{% endalert %}

N'oubliez pas d'indiquer également tout code de réduction, offre ou autre information promise dans l'annonce !

\![Compositeur de messages WhatsApp avec les boutons de réponse "Oui" et "Non merci".]({% image_buster /assets/img/whatsapp/quick_replies.png %})

!étape du canvas avec un groupe "Opting in" avec un événement déclencheur de "Sent inbound WhatsApp to subscription groups" et un mot déclencheur de "YES".]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4\. Les utilisateurs qui s'abonnent peuvent le faire en mettant à jour le statut d'abonnement de leur profil utilisateur à l'aide de l'une des méthodes de mise à jour suivantes :
    \- Créez un webhook Braze à Braze qui met à jour le statut de l'abonnement via l'API REST.  
    \- Utilisez l'éditeur JSON avancé pour mettre à jour le profil utilisateur avec le modèle de [mise à jour du statut d'abonnement d'un utilisateur à un WhatsApp Canvas]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#whatsapp-opt-in-and-opt-out-process).

!étape du canvas de mise à jour de l'utilisateur qui utilise l'éditeur JSON avancé pour mettre à jour le profil utilisateur.]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

Canevas montrant le flux de travail pour envoyer des publicités qui cliquent à WhatsApp, y compris trois parcours d'action : L'abonnement, l'exclusion et tous les autres.]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## Considérations

Les conversions qui démarrent à partir d'une publicité qui clique sur WhatsApp sont gratuites si les conditions suivantes sont remplies :

- Si un utilisateur vous envoie un message par l'intermédiaire d'un [point d'entrée gratuit](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations), tel qu'une publicité qui clique sur WhatsApp, une [fenêtre de service client de](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) 24 heures s'ouvre, dans laquelle vous pouvez envoyer à cet utilisateur n'importe quel type de message.
- Si vous répondez dans la fenêtre du service clientèle (dans les 24 heures), un point d'entrée gratuit s'ouvre pour 72 heures, et tous les messages dans la fenêtre de 72 heures seront gratuits.
- L'envoi de messages est gratuit.