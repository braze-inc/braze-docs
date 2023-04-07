---
nav_title: Livraison par événement
article_title: Livraison par événement
page_order: 1
page_type: reference
description: "Le présent article de référence décrit comment déclencher des campagnes à envoyer après qu’un utilisateur a effectué un certain événement."
tool: Campaigns

---

# Livraison par événement

Les campagnes de livraison par événement ou les campagnes déclenchées par des événements sont très efficaces pour les messages transactionnels ou basés sur le résultat. Au lieu d’envoyer votre campagne certains jours, vous pouvez les déclencher pour qu’elles s’envoient après qu’un utilisateur a effectué un certain événement. Les étapes suivantes décrivent la configuration d’une planification basée sur les événements :

{% alert important %}
La livraison par événement n’est pas disponible pour des [composants Canvas avec des messages in-app]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas). Ces étapes doivent être planifiées.
{% endalert %}

## Configurer une campagne avec déclencheur

### Étape 1 : Sélectionner un événement déclencheur

Sélectionnez un événement déclencheur. Il peut comprendre l’un des éléments suivants :
- Démarrer une session
- Acheter un article
- Interagir avec les cartes de fil d’actualité (voir [Connecteur de campagne Braze][33])
- Interagir avec d’autres campagnes
- Saisir un emplacement
- Terminer tout événement personnalisé
- Effectuer l’événement de conversion primaire de la campagne
- Effectuer l’événement d’exception pour une autre campagne
- Ajouter une adresse e-mail à un profil utilisateur
- Mise à jour du statut du groupe d’abonnement
- Message WhatsApp ou SMS entrant

Vous pouvez filtrer de manière plus approfondie les événements déclencheurs à l’aide des [propriétés d’événements personnalisés][32] de Braze qui permettent des propriétés de l’événement personnalisables pour les événements personnalisés et les achats in-app. Cette fonction vous permet d’adapter davantage quel utilisateur va recevoir un message sur la base des attributs spécifiques de l’événement personnalisé, ce qui permet une personnalisation plus importante de la campagne et une collecte de données plus sophistiquée. 

Supposons, par exemple, que nous ayons une campagne avec un événement personnalisé d’abandon de panier qui est ciblé par le filtre de propriété « valeur du panier ». Cette campagne n’atteindra que les utilisateurs qui ont abandonné entre 100 $ et 200 $ de marchandises dans leur panier. 

![][34]

{% alert note %}
L’événement déclencheur « démarrer la session » peut être la première ouverture de l’application par l’utilisateur si le segment de votre campagne s’applique aux nouveaux utilisateurs (par ex., si votre segment est composé de ceux n’ayant pas de sessions).
{% endalert %}

N’oubliez pas que vous pouvez toujours envoyer une campagne déclenchée à un segment spécifique d’utilisateurs, afin que ceux qui ne font pas partie du segment ne reçoivent pas la campagne même s’ils effectuent l’événement déclencheur. Si vous remarquez que les utilisateurs ne reçoivent pas la campagne même s’ils sont qualifiés pour le segment, consultez notre section [pourquoi un utilisateur peut ne pas avoir reçu une campagne déclenchée][49].

En ce qui concerne l’événement déclencheur défini quand un utilisateur ajoute une adresse e-mail à son profil, les règles suivantes s’appliquent :

- L’événement déclencheur sera activé après la mise à jour des attributs de profil utilisateur. Cela signifie que l’évaluation des segments et des filtres de la campagne se produira après toute mise à jour d’attribut. C’est une bonne chose parce qu’elle vous permet de configurer des filtres comme « adresse e-mail contient gmail.com » pour créer une campagne déclenchée qui n’est envoyée qu’aux utilisateurs Gmail et s’active dès qu’ils ajoutent leur adresse e-mail.
- L’événement déclencheur s’active lorsqu’une adresse e-mail est ajoutée à un profil utilisateur. Si vous avez plusieurs profils d’utilisateur que vous créez avec la même adresse e-mail, la campagne peut être déclenchée plusieurs fois, une fois pour chaque profil utilisateur.

En outre, les messages in-app déclenchés sont toujours conformes aux règles de livraison des messages in-app et apparaissent au début de la session de l’application.

![][17]

### Étape 2 : Sélectionner la longueur du délai

Sélectionnez la durée d’attente avant d’envoyer la campagne une fois les critères de déclenchement satisfaits. Si la longueur du délai choisi est supérieure à la durée d’envoi du message, aucun utilisateur ne recevra la campagne. 

De plus, les utilisateurs qui terminent l’événement déclencheur après le lancement de votre campagne seront les premiers à commencer à recevoir le message une fois que le délai a été dépassé. Les utilisateurs qui ont terminé l’événement déclencheur avant que la campagne ne commence ne sont pas qualifiés pour recevoir la campagne.

![][19]

Vous pouvez également choisir d’envoyer la campagne soit un jour spécifique de la semaine (en choisissant « au prochain » puis en sélectionnant un jour) ou un nombre spécifique de jours dans l’avenir (en sélectionnant « dans »). Vous pouvez également choisir d’envoyer votre message à l’aide de la fonctionnalité [Timing Intelligent][8] au lieu de sélectionner manuellement une heure de livraison.

![][41]
![][50]

### Étape 3 : Sélectionner des événements d’exception

Sélectionnez un événement d’exception qui disqualifiera les utilisateurs pour la réception de cette campagne. Vous ne pouvez le faire que si votre message déclenché est envoyé après un délai temporel. Les événements d’exception peuvent être la réalisation d’un achat, démarrer une session, exécuter l’un des [événements de conversion][18] de la campagne ou effectuer un événement personnalisé. Si un utilisateur effectue l’événement déclencheur mais effectue ensuite votre événement d’exception avant que le message ne soit envoyé en raison du délai temporel, il ne recevra pas la campagne. Les utilisateurs qui ne reçoivent pas la campagne en raison de l’événement d’exception seront automatiquement éligibles à la recevoir à l’avenir, la prochaine fois qu’ils effectueront l’événement déclencheur, même si vous ne choisissez pas de rendre les utilisateurs [rééligibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/).

![][20]

Vous pouvez en apprendre plus sur la manière d’utiliser des événements d’exception dans notre section sur les [cas d’utilisation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#use-cases).

> Si vous envoyez une campagne avec l’événement déclencheur correspondant à l’événement d’exception, la campagne initiale sera annulée. Au lieu d’envoyer les deux campagnes, la première campagne de votre utilisateur sera annulée et Braze planifiera à nouveau automatiquement une nouvelle campagne en fonction de l’heure de livraison du message d’événement d’exception.<br><br>Par exemple, si votre premier événement déclencheur commence à 5 minutes et que le moment de l’événement d’exception commence à 10 minutes, vous vous baseriez sur les 10 minutes de l’événement d’exception comme heure de livraison officielle du message de la campagne.

{% alert note %}
Vous ne pouvez pas faire que l’événement « démarrer la session » soit à la fois l’événement déclencheur et l’événement d’exception d’une campagne. Cependant, vous avez toujours la possibilité de sélectionner tout autre événement personnalisé en dehors de cette option.
{% endalert %}

### Étape 4 : Attribuer une durée

Attribuez la durée de la campagne en spécifiant une heure de début et une heure de fin facultative.

![][21]

Si un utilisateur effectue un événement déclencheur pendant la période spécifiée, mais qu’il est éligible pour le message en dehors du délai imparti en raison d’un délai planifié, il ne recevra pas la campagne. Par conséquent, si vous définissez un délai plus long que la durée du message, aucun utilisateur ne recevra votre campagne. De plus, vous pouvez choisir d’envoyer le message selon les [fuseaux horaires locaux]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/scheduled_delivery/#local-time-zone-campaigns) de l’utilisateur.

### Étape 5 : Sélectionner la fenêtre temporelle

Indiquez si l’utilisateur recevra la campagne pendant à un moment spécifique de la journée. Si vous donnez au message une fenêtre de réception et que l’utilisateur effectue l’événement déclencheur en dehors de cette fenêtre ou que le délai du message entraîne le fait qu’il la rate, alors, par défaut, l’utilisateur ne recevra pas votre message.

![][27]

Dans le cas où un utilisateur effectue l’événement déclencheur dans la fenêtre temporelle, mais que le délai de message le fait sortir de cette fenêtre, vous pouvez cocher la case suivante pour que ces utilisateurs reçoivent toujours la campagne.

![][31]

Si un utilisateur ne reçoit pas le message parce qu’il manque la fenêtre temporelle, il sera toujours éligible à la recevoir la prochaine fois qu’il effectuera l’événement déclencheur, même si vous ne choisissez pas de rendre les utilisateurs [rééligibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/). Si vous choisissez d’autoriser les utilisateurs à devenir rééligibles, ils peuvent recevoir la campagne chaque fois qu’ils effectuent l’événement déclencheur, en supposant qu’ils sont admissibles pendant la période spécifiée.

Si vous avez également attribué une certaine durée à la campagne, un utilisateur doit être admissible à la fois à la durée et au moment spécifique de la journée pour recevoir le message.

### Étape 6 : Déterminer la rééligibilité

Déterminez si les utilisateurs peuvent devenir [rééligibles][24] à la campagne. Si vous autorisez les utilisateurs à devenir rééligibles, vous pouvez spécifier un délai avant que l’utilisateur puisse recevoir à nouveau la campagne. Cela empêchera les campagnes déclenchées de devenir « indésirables ».

![][28]

## Cas d’utilisation

Les campagnes déclenchées sont très efficaces pour les messages transactionnels ou basés sur le résultat.

Les campagnes transactionnelles comprennent les messages envoyés après que l’utilisateur effectue un achat ou ajoute un article à son panier. Ce dernier cas est un excellent exemple d’une campagne qui pourrait bénéficier d’un événement d’exception. Imaginez que votre campagne rappelle aux utilisateurs la présence d’articles dans leur panier qu’ils n’ont pas acheté. Dans ce cas, l’utilisateur achetant les produits dans son panier deviendrait l’événement d’exception. Pour les campagnes basées sur les résultats, vous pouvez envoyer un message 5 minutes après que l’utilisateur a achevé une conversion ou battu un niveau de jeu.

De plus, lors de la création de campagnes de bienvenue, vous pouvez déclencher des messages à envoyer après que l’utilisateur s’enregistre ou configure un compte. Répartir des messages à envoyer différents jours suivant l’inscription vous permettra de créer un processus d’onboarding complet.

## Pourquoi un utilisateur n’a-t-il pas reçu ma campagne déclenchée ?

L’un des éléments suivants empêchera un utilisateur qui a effectué l’événement déclencheur de recevoir la campagne :

- L’utilisateur a effectué l’événement d’exception avant que le délai ne soit complètement écoulé.
- Le délai a poussé l’utilisateur à devenir admissible à recevoir la campagne après que sa durée est terminée.
- Le délai a poussé l’utilisateur à devenir admissible à recevoir la campagne en dehors du moment de la journée spécifié.
- L’utilisateur a déjà reçu la campagne et les utilisateurs ne sont pas rééligibles.
- Bien que les utilisateurs soient rééligibles pour recevoir la campagne, ils ne peuvent la déclencher à nouveau qu’après une certaine période temporelle et elle n’est pas encore écoulée.

[Segmenter]({{site.baseurl}}/user_guide/engagement_tools/segments/) une campagne déclenchée sur la base des données utilisateur enregistrées au moment de l’événement peut entraîner une [condition de course]({{site.baseurl}}/help/best_practices/race_conditions/#race-conditions). Cela se produit lorsque l’attribut utilisateur sur lequel la campagne est segmentée est modifié, mais que le changement n’a pas été traité pour l’utilisateur lorsque la campagne est envoyée. Étant donné que les campagnes vérifient l’appartenance au segment à l’entrée, cela peut entraîner des utilisateurs ne recevant pas la campagne.

Imaginez par exemple que vous souhaitiez envoyer une campagne déclenchée par un événement aux utilisateurs masculins qui viennent juste de s’enregistrer. Lorsque l’utilisateur s’enregistre, vous notez un événement personnalisé `registration` et définissez simultanément un attribut `gender`. L’événement peut déclencher la campagne avant que Braze ne traite le genre de l’utilisateur, ce qui empêche qu’il ne reçoive la campagne.

En tant que bonne pratique, assurez-vous que l’attribut sur lequel la campagne est segmentée est envoyé vers les serveurs de Braze avant l’événement. Si cela n’est pas possible, la meilleure manière de garantir la livraison est d’utiliser des [propriétés de l’événement personnalisées][48] pour joindre les propriétés utilisateur pertinentes à l’événement et appliquer un filtre de propriété pour la propriété de l’événement spécifique au lieu d’un filtre de segmentation. Dans notre exemple, vous ajouteriez une propriété `gender` à l’événement personnalisé `registration` afin que Braze dispose forcément des données dont vous avez besoin lorsque votre campagne est déclenchée.

De plus, si une campagne est basée sur des actions et dispose d’un délai, vous pouvez cocher l’option **Réévaluer l’appartenance au segment au moment de l’envoi** pour vous assurer que les utilisateurs font toujours partie de l’audience cible lorsque le message est envoyé.

![][51]

[5]: #local-time-zone-campaigns
[8]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[17]: {% image_buster /assets/img_archive/schedule_triggered1.png %}
[18]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[19]: {% image_buster /assets/img_archive/schedule_triggered22.png %}
[20]: {% image_buster /assets/img_archive/schedule_triggered32.png %}
[21]: {% image_buster /assets/img_archive/schedule_triggered43.png %}
[22]: #use-cases-2
[24]: {% image_buster /assets/img_archive/ReEligible.png %}
[27]: {% image_buster /assets/img_archive/schedule_triggered5.png %}
[28]: {% image_buster /assets/img_archive/schedule_triggered6.png %}
[29]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/in-app_message_behavior/#in-app-message-delivery-rules
[30]: {{site.baseurl}}/help/best_practices/user_onboarding/#user-onboarding
[31]: {% image_buster /assets/img_archive/schedule_triggered_next_available.png %}
[32]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[33]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/campaign_connector/#campaign-connector
[34]: {% image_buster /assets/img_archive/customEventProperties.png %}
[41]: {% image_buster /assets/img_archive/schedule_triggered7.png %}
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign
[48]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[49]: {{site.baseurl}}/help/help_articles/campaigns_and_canvas/not_triggering/
[50]: {% image_buster /assets/img_archive/schedule_triggered8.png %}
[51]: {% image_buster /assets/img_archive/reevaluate_segment_membership.png %}
