---
nav_title: Création d'une campagne SMS
article_title: Création d'une campagne SMS
page_order: 5
description: "Cet article de référence couvre les étapes de l'élaboration et de la création d'une campagne SMS."
page_type: Référence
tool:
  - Campagnes
channel:
  - SMS
---

# Créer une campagne SMS

> Les campagnes SMS sont idéales pour atteindre directement et discuter avec vos clients de façon programmatique. Vous pouvez utiliser Liquid et d'autres contenus dynamiques pour créer une expérience personnelle avec vos utilisateurs et créer un environnement qui favorise et améliore une expérience utilisateur discrète avec votre marque.

## Étape 1 : Choisissez où construire votre message

Les SMS sont disponibles dans les deux campagnes et dans Canvas.

{% tabs local %}
  {% tab Campaigns %}
  Cliquez sur **Créer une campagne** pour ouvrir un nouvel assistant de messagerie pour les campagnes de messages dans l'application. Ensuite, suivez le flux de l'assistant de messagerie pour créer et lancer rapidement votre campagne SMS.

  ![Créer une campagne SMS]({% image_buster /assets/img/sms_campaign_setup.gif %})

1. Nommez votre campagne quelque chose de clair et significatif.
2. Ajouter des équipes et des tags, si nécessaire.
3. Ajoutez et nommez autant de variantes que vous avez besoin pour cette campagne.
  - Vous pouvez choisir différentes plateformes, types de messages et mises en page pour chacune de vos variantes ajoutées.
4. Sélectionnez le groupe d'abonnement pour vous assurer que vous envoyez votre message aux utilisateurs appropriés. Lors de la sélection d'un groupe d'abonnement, Braze ajoutera automatiquement un filtre de segmentation, en s'assurant que seuls les utilisateurs inscrits recevront la campagne. Seuls les codes longs et les codes courts qui appartiennent à ce groupe d'abonnement seront utilisés pour envoyer des SMS aux utilisateurs cibles.

  {% alert tip %}
Si tous les messages de votre campagne vont être similaires ou ont le même contenu, composez votre message avant d'ajouter des variantes supplémentaires - vous serez en mesure de choisir **Copier de la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

 {% endtab %}
 {% tab Canvas %}
 After you have [created and set up your Canvas using the Canvas wizard]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/),

1. Nommez votre étape quelque chose de clair et de significatif.
2. Ajouter un délai, si nécessaire.
3. Filtrer votre public, si nécessaire.
4. Choisissez vos options d'avancement, si nécessaire.
5. Choisissez tous les autres canaux de messagerie que vous souhaitez associer à votre message.

{% alert important %}
Vous ne pouvez pas avoir plusieurs variantes de messages dans l'application en une seule étape.
{% endalert %}

{% endtab %}
{% endtabs %}

## Étape 2 : Écrire votre SMS

Écrire un SMS est facile ! Il vous suffit d'écrire votre message en utilisant les langues et la personnalisation (Liquid, Connected Content, et Emojis) au besoin. Assurez-vous de respecter les limites de copie de notre message afin de réduire vos risques de surâge.

{% alert important %}
Avant de continuer, lisez [les limites de copie des messages SMS et les directives de segment de message]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/). Les segments de messages SMS sont les caractères utilisés par les opérateurs téléphoniques pour mesurer les messages textuels. Les messages sont facturés par segment de message, de sorte que les clients qui utilisent les SMS profitent grandement de la compréhension des nuances de la façon dont les messages seront partagés.
{% endalert %}

![Écrire un SMS]({% image_buster /assets/img/sms_campaign_compose.gif %})

{% alert tip %}
{% raw %}
Si vous prévoyez d'utiliser Liquid, assurez-vous d'inclure une valeur par défaut pour la personnalisation de votre choix ainsi, dans le cas où votre profil utilisateur du destinataire est incomplet, il ne recevra pas de marqueur vide `Bonjour, !`, au lieu de leur nom ou d'une phrase cohérente.
{% endraw %}
{% endalert %}

## Étape 3 : Prévisualiser et tester votre message

Braze recommande toujours de prévisualiser et de tester votre message avant l'envoi.

![Tester les SMS]({% image_buster /assets/img/sms_campaign_test.gif %})

{% alert tip %}
Si vous souhaitez tester combien de segments de SMS peuvent être divisés, testez la longueur de votre copie [ici]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#sms-segment-calculator).
{% endalert %}

## Étape 4 : Configurer l'envoi du message

Décidez comment, quand et pourquoi votre message sera envoyé. Vous pouvez soit programmer votre message pour une heure spécifique, soit le déclencher à partir de l'action d'un utilisateur. Vous pouvez également le déclencher via l'API pour les [campagnes]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) et [Canvas]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/).

![Envoi de SMS]({% image_buster /assets/img/sms_campaign_delivery.gif %})

## Étape 5 : les utilisateurs ciblés et sélectionnez le segment

Dans cette étape, vous choisissez quels utilisateurs reçoivent votre message. Vous devriez déjà avoir choisi le Groupe d'Abonnement, qui rétrécit les utilisateurs par le niveau ou la catégorie de communication qu'ils souhaitent avoir avec vous. Dans cette étape, vous sélectionnerez le plus grand public de vos Segments, et vous réduirez ce segment plus loin avec nos Filtres, si vous le souhaitez.

![Ciblage de SMS]({% image_buster /assets/img/sms_campaign_targeting.gif %})

{% alert tip %}
Intéressant au repositionnement par SMS? Visitez notre [article de redistribution SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) pour en savoir plus.
{% endalert %}

## Étape 6 : Choisissez les événements de conversion

Les événements de conversion vous aident à mesurer le succès de votre campagne:
- Si vous utilisez le géociblage pour déclencher un message SMS qui a un objectif final que l'utilisateur effectue un achat, réglez l'événement de conversion sur un « Achat ».
- Si vous tentez de conduire l'utilisateur vers votre application, définissez l'événement de conversion à "Démarre la session".

Vous pouvez également définir des événements de conversion personnalisés en fonction de votre cas d'utilisation spécifique. Soyez créatif et pensez à la façon dont vous voulez vraiment mesurer le succès de cette campagne.

![Événements de conversion SMS]({% image_buster /assets/img/sms_campaign_conversion.gif %})

## Étape 7 : Confirmez les détails et lancez !

Si vous utilisez des campagnes, vous aurez la possibilité de confirmer ses détails. Si vous utilisez Canvas, assurez-vous de confirmer les détails de chacune des pièces.

![Confirmation par SMS]({% image_buster /assets/img/sms_campaign_confirm.gif %})
