---
nav_title: Campagnes et toiles
article_title: "Pour commencer : Campagnes et toiles"
page_order: 3
page_type: reference
description: "Cet article donne un aperçu des différentes façons dont vous pouvez envoyer des messages avec Braze."

---

# Pour commencer : Campagnes et toiles

Dans Braze, vous pouvez envoyer des messages par le biais d'une [campagne](#campaigns) ou d'un [canvas](#canvas).

- Pour envoyer un message unique et ciblé à un groupe d'utilisateurs, choisissez une campagne. Une campagne est une étape de message unique pour entrer en contact avec vos utilisateurs sur différents canaux d'envoi de messages.
- Pour envoyer une série de messages continus dans le cadre d'un parcours client global, choisissez Canvas, notre outil d'orchestration de parcours. Alors que les campagnes permettent d'envoyer des messages simples et personnalisés, les toiles sont l'occasion de faire passer vos relations avec les clients au niveau supérieur.

## Campagnes

Bien que les campagnes puissent être créées de manière unique en fonction du canal, il existe quatre types principaux de campagnes dans Braze que vous devez connaître :

| Type de campagne        | Description                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Régulière              | Il s'agit du type de campagne le plus courant. Vous pouvez cibler un ou plusieurs canaux en fonction de vos objectifs d'envoi de messages, et concevoir, personnaliser et tester votre contenu directement dans Braze grâce à nos éditeurs visuels. Apprenez à [créer une campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign). |
| Test A/B          | Pour les campagnes ciblant un seul canal, vous pouvez envoyer plusieurs versions de la même campagne et voir laquelle arrive en tête. Vous pouvez tester le texte, la personnalisation et bien d'autres choses encore pour un maximum de huit versions différentes dans le cadre d'une [campagne multivariée]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/). |
| API                  | Les [campagnes API]({{site.baseurl}}/api/api_campaigns/) vous permettent d'envoyer des messages opportuns le plus rapidement possible. Contrairement aux autres types de campagne, vous ne spécifiez pas le message, les destinataires ou la planification dans le tableau de bord de Braze. Au lieu de cela, vous transmettez ces identifiants dans vos appels à l'API. Ils sont généralement utilisés pour les messages transactionnels en temps réel ou les nouvelles de dernière minute.  |
| E-mails transactionnels | Les [e-mails transactionnels de]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/) Braze sont créés pour envoyer des messages e-mail automatisés et non promotionnels afin de faciliter une transaction convenue entre vous et vos clients. Ils envoient des notifications critiques à un seul utilisateur, où la rapidité est de la plus haute importance. *Disponible pour certains forfaits.* |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Les campagnes régulières et les campagnes de test A/B peuvent être planifiées (par exemple, informer une liste d'utilisateurs d'un événement à venir) ou automatisées pour être envoyées en réponse à l'action d'un utilisateur (par exemple, envoyer un e-mail lorsqu'une personne s'abonne à votre lettre d'information). En savoir plus sur la [planification des campagnes.]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types)
{% endalert %}

Quel que soit le type de campagne que vous créez, vos campagnes peuvent être à l'écoute des besoins de vos utilisateurs et leur apporter une réponse réfléchie et personnalisée. Après avoir envoyé votre campagne, utilisez nos [outils d'analyse/analytique intégrés]({{site.baseurl}}/user_guide/analytics/reporting/) pour voir comment elle s'est comportée et combien d'utilisateurs se sont convertis en fonction de vos [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).

Consultez ces ressources supplémentaires pour en savoir plus sur les campagnes chez Braze :

- Braze Learning : [Configuration de la campagne](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [Créer une campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign)
- [Idées et stratégies]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies)

## Canevas

Plutôt que d'envoyer des messages sporadiques au cours de plusieurs campagnes, Canvases crée une conversation fluide et continue avec les utilisateurs. En effet, le parcours d'un utilisateur dans un Canvas peut se scinder en différents parcours en fonction de ses actions (ou inactions) avec votre marque, ce qui vous permet de faire avancer automatiquement les utilisateurs dans un flux spécifique en temps réel.

\![]({% image_buster /assets/img/getting_started/canvas_flow.png %})

De cette façon, les Canvas sont parfaits pour jeter un filet afin de capturer les utilisateurs qui tombent sur le chemin de la conversion et les placer dans les initiatives de sensibilisation les plus efficaces.

Lorsque vous créez un Canvas, vous suivez en grande partie les mêmes étapes que pour la mise en place d'une campagne : spécification d'une audience globale, des conditions de participation et des paramètres d'envoi. Votre Canvas démarre lorsque quelqu'un correspond à votre condition de déclenchement. Ils empruntent ensuite un chemin dans la toile jusqu'à ce qu'ils remplissent vos conditions de sortie.

Votre Canvas peut comporter n'importe quelle combinaison de [messages]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), de [délais]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), d'[expériences]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/), etc. Vous pouvez envoyer sur n'importe quel canal de communication pris en charge, et même [intégrer des plateformes sociales et publicitaires]({{site.baseurl}}/partners/canvas_audience_sync/overview/) telles que Facebook, Google ou TikTok.

Consultez ces ressources supplémentaires pour en savoir plus sur Canvas :

- Braze Learning : [Orchestration du parcours avec Canvas Flow](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [Créer un canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- [Les contours de la toile]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_outlines/)

## Canaux d'envoi de messages

Les canaux d'envoi de messages sont les différents canaux de communication par lesquels vous pouvez vous engager avec vos clients et diffuser des messages ciblés. 

\![]({% image_buster /assets/img/getting_started/channels.png %})

Le tableau suivant présente les canaux que nous soutenons.

| Chaîne                                                                                              | Description                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)                        | Envoyez des e-mails personnalisés dans la boîte de réception de vos utilisateurs.                                                                                                       |
| [Poussée mobile]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)                   | Envoyez des messages directement sur les appareils mobiles des utilisateurs sous forme de notifications.                                                                                   |
| [Poussée sur le web]({{site.baseurl}}/user_guide/message_building_by_channel/push/web)                         | Envoyez des notifications aux navigateurs web des utilisateurs, même lorsqu'ils ne sont pas activement sur votre site web.                                                         |
| [Messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)    | Affichez des messages au sein de votre application mobile pendant que les utilisateurs l'utilisent activement.                                                                             |
| [SMS, MMS et RCS\*.]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/)                   | Envoyer des messages texte aux téléphones portables des utilisateurs.                                                                                                            |
| [WhatsApp*]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)              | Envoyez des messages via la populaire plateforme d'envoi de messages, WhatsApp, pour atteindre et engager vos utilisateurs.                                                   |
| [Bannières*]({{site.baseurl}}/user_guide/message_building_by_channel/banners/)       | Intégrez des messages directement dans votre application ou votre site web. |
| [Cartes de contenu*]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)       | Proposez une boîte de réception au sein de votre application ou site web où les utilisateurs peuvent recevoir des messages et interagir avec eux, ou affichez les messages dans un carrousel, sous forme de bannière, et plus encore. |
| [Télévision connectée]({{site.baseurl}}/developer_guide/platforms/tv_and_ott/)                           | Dialoguez avec les utilisateurs sur les plates-formes de télévision connectées.                                                                                                   |
| [Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | Permettez la communication et l'intégration en temps réel avec des systèmes externes grâce à des rappels HTTP personnalisés.                                                    |
| [LIGNE]({{site.baseurl}}/user_guide/message_building_by_channel/line/) | Engagez-vous avec les utilisateurs sur LINE, l'envoi de messages le plus populaire au Japon.                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>\*\*Disponible en tant que fonctionnalité supplémentaire.</sup>

{% alert tip %}
Pour les messages courts et urgents qui peuvent être communiqués par la plupart des canaux (e-mail, SMS, push), profitez du filtre de [canal intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) pour envoyer automatiquement le message par le meilleur canal pour chaque utilisateur.
{% endalert %}

