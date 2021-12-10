---
nav_title: Livraison par action
article_title: Livraison par action
page_order: 1
page_type: Référence
description: "Cet article de référence décrit comment déclencher des campagnes à envoyer après qu'un utilisateur a terminé un certain événement."
tool: Campagnes
---

# Livraison basée sur l'action

Les campagnes de livraison basées sur l'action ou les campagnes déclenchées par des événements sont très efficaces pour les messages transactionnels ou axés sur les résultats. Au lieu d'envoyer votre campagne à certains jours, vous pouvez les déclencher pour les envoyer après qu'un utilisateur ait terminé un certain événement. Listé ci-dessous sont les étapes de la mise en place d'un planning basé sur des événements :

{% alert important %}
La livraison par action n'est pas disponible pour les [étapes de Canvas avec les messages dans l'application]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas). Ces étapes doivent être planifiées.
{% endalert %}

## Mise en place d'une campagne déclenchée

### Étape 1 : Sélectionnez un événement de déclenchement

Sélectionnez un événement déclencheur, qui peut être:
- Démarrage d'une session
- Achat d'un objet
- Interagir avec les cartes de flux d'actualités (voir le connecteur de campagne de [Braze][33])
- Interagir avec d'autres campagnes
- Saisie d'un emplacement
- Terminer tout événement personnalisé
- Effectuer l'événement principal de conversion de la campagne
- Exécution de l'évènement d'exception pour une autre campagne
- Ajout d'une adresse e-mail à un profil utilisateur

Vous pouvez également filtrer les événements par le biais des [propriétés d'événement personnalisées de Braze][32], permettant des propriétés d'événements personnalisables pour des événements personnalisés et des achats dans l'application. Cette fonctionnalité vous permet de personnaliser davantage les utilisateurs qui reçoivent un message en fonction des attributs spécifiques de l'événement personnalisé, permettant une plus grande personnalisation des campagnes et une collecte de données plus sophistiquée. Par exemple, dans la capture d'écran suivante, un événement personnalisé du panier abandonné est davantage ciblé par le filtre de propriété "valeur du panier". Cette campagne n'atteindra que les utilisateurs qui ont laissé entre 100 et 200 $ de marchandises dans leurs paniers.

!\[Propriétés d'événement personnalisées\]\[34\]

{% alert note %}
L'événement trigger "session de démarrage" peut être la première application de l'utilisateur ouverte si le segment de votre campagne s'applique aux nouveaux utilisateurs (par exemple, si votre segment se compose de ceux qui n'ont pas de sessions).
{% endalert %}

Gardez à l'esprit que vous pouvez toujours envoyer une campagne déclenchée à un segment spécifique d'utilisateurs de sorte que les utilisateurs qui ne font pas partie du segment ne recevront pas la campagne même s'ils complètent l'événement de déclenchement. Si vous remarquez que les utilisateurs ne reçoivent pas la campagne même s'ils se qualifient pour le segment, veuillez lire notre section sur les [raisons pour lesquelles un utilisateur n'a peut-être pas reçu une campagne déclenchée][49].

En ce qui concerne l'événement de déclenchement pour lorsqu'un utilisateur ajoute une adresse e-mail à son profil, les règles suivantes s'appliquent :

- L'événement trigger sera déclenché après la mise à jour de l'attribut profil de l'utilisateur. Cela signifie que l'évaluation des segments et des filtres de la campagne se fera après toute mise à jour d'attributs. Ceci est bénéfique car il vous permet de configurer des filtres comme "adresse e-mail correspond à gmail. om" pour créer une campagne de déclenchement qui n'envoie qu'aux utilisateurs de Gmail et se déclenche dès qu'ils ajoutent leur adresse e-mail.
- L'événement déclencheur se déclenchera lorsqu'une adresse e-mail est ajoutée à un profil utilisateur. Si vous avez plusieurs profils d'utilisateurs que vous créez avec la même adresse e-mail, la campagne peut se déclencher plusieurs fois, une fois pour chaque profil d'utilisateur.

De plus, les messages déclenchés dans l'application sont toujours conformes aux règles de livraison des messages intégrés à l'application et apparaissent au début d'une session de l'application.

!\[Select Trigger\]\[17\]

### Étape 2 : Sélectionnez la longueur du délai

Sélectionnez le temps d'attente avant d'envoyer la campagne après que les critères de déclenchement soient remplis. Si la longueur de délai choisie est plus longue que la durée d'envoi du message, aucun utilisateur ne recevra la campagne.

De plus, les utilisateurs qui terminent l'événement de déclenchement après le lancement de votre campagne seront les premiers à commencer à recevoir le message une fois le délai écoulé. Les utilisateurs qui ont terminé l'événement de déclenchement avant le lancement de la campagne ne seront pas qualifiés pour recevoir la campagne.

!\[Select Delay\]\[19\]

Vous pouvez également choisir d'envoyer la campagne soit un jour spécifique de la semaine (en choisissant "le lendemain" puis en sélectionnant un jour) soit un nombre de jours précis (en sélectionnant "dans") dans le futur. Vous pouvez également choisir d’envoyer votre message en utilisant la fonction [Intelligent Timing][8] au lieu de sélectionner manuellement un délai de livraison.

!\[Schedule Delay Intelligent Timing\]\[41\] !\[Schedule Delay\]\[50\]

### Étape 3 : Sélectionnez les événements d'exception

Sélectionnez un événement d'exception qui empêchera les utilisateurs de recevoir cette campagne. Vous ne pouvez le faire que si votre message déclenché envoie après un délai de temps. Les événements d'exception peuvent faire un achat, en commençant une session, effectuer l'un des
événements de conversion de la campagne désignés [][18], ou effectuer un événement personnalisé. Si un utilisateur termine l'événement de déclenchement mais termine ensuite votre événement d'exception avant que le message ne soit envoyé en raison du délai, ils ne recevront pas la campagne. Les utilisateurs qui ne reçoivent pas la campagne en raison de l'événement d'exception seront automatiquement éligibles pour le recevoir dans le futur, la prochaine fois qu'ils termineront l'événement de déclenchement, même si vous ne choisissez pas que les utilisateurs deviennent [ré-éligibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/).</p> 

Vous pouvez en savoir plus sur l'utilisation d'événements d'exception dans notre section sur les [cas d'utilisation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#use-cases).

!\[Schedule Delay Exception\]\[20\]



> Si vous envoyez une campagne avec l'événement de déclenchement qui correspond à l'événement d'exception, la campagne initiale sera annulée. Au lieu d'envoyer les deux campagnes, la première campagne de votre utilisateur sera annulée et Braze replanifiera automatiquement une nouvelle campagne en fonction du délai de livraison du message de l'événement.<br><br>Par exemple, si votre premier événement de déclenchement commence à 5 minutes et que l'heure de l'événement d'exception commence à 10 minutes, vous compteriez sur les 10 minutes de l'évènement d'exception comme le délai de livraison du message officiel de la campagne.

{% alert note %}

Vous ne pouvez pas faire un "démarrage de session" à la fois l'événement trigger et l'évènement d'exception pour une campagne. Cependant, vous avez toujours le choix de sélectionner tout autre événement personnalisé en dehors de cette option. 

{% endalert %}



### Étape 4 : Assigner la durée

Assignez la durée de la campagne en spécifiant une heure de début et une heure de fin facultative. Si un utilisateur termine un événement de trigger pendant la période spécifiée, mais se qualifie pour le message en dehors de la période en raison d'un délai planifié, alors ils ne recevront pas la campagne. Par conséquent, si vous définissez un délai plus long que le délai du message, aucun utilisateur ne recevra votre campagne. En outre, vous pouvez choisir d'envoyer le message dans les [fuseaux horaires locaux]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/scheduled_delivery/#local-time-zone-campaigns) des utilisateurs.

!\[Durée de la campagne\]\[21\]



### Étape 5 : Sélectionnez une période de temps

Indique si l'utilisateur recevra la campagne pendant une partie spécifique de la journée. Si vous donnez au message un laps de temps et que l'utilisateur termine soit l'évènement déclencheur en dehors de la période soit le délai de message, cela ne peut pas être le cas, puis par défaut, l'utilisateur ne recevra pas votre message.

!\[Sepcific Time Frame\]\[27\]

Dans le cas où un utilisateur termine l'événement de trigger dans le laps de temps, mais le délai de message fait que l'utilisateur tombe en dehors du laps de temps, vous pouvez cocher la case ci-dessous pour que ces utilisateurs reçoivent toujours la campagne:

!\[Triggered Next Available\]\[31\]

Si un utilisateur ne reçoit pas le message parce qu'il manque le laps de temps, alors ils seront toujours qualifiés pour le recevoir la prochaine fois qu'ils termineront l'événement de déclenchement même si vous n'avez pas choisi que les utilisateurs deviennent [rééligibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/). Si vous choisissez que les utilisateurs deviennent rééligibles, alors les utilisateurs peuvent recevoir la campagne chaque fois qu'ils terminent l'événement de déclenchement en supposant qu'ils se qualifient pendant la période spécifiée.

Si vous avez également attribué une certaine durée à la campagne, alors un utilisateur doit se qualifier à la fois dans la durée et dans la partie spécifique de la journée pour recevoir le message.



### Étape 6 : Déterminer la rééligibilité

Détermine si les utilisateurs peuvent devenir \[re-eligible\]\[24\] pour la campagne. Si vous autorisez les utilisateurs à devenir rééligibles, vous pouvez spécifier un délai avant que l'utilisateur puisse recevoir la campagne à nouveau. Cela empêchera vos campagnes déclenchées de devenir "spammy".

!\[Ré-éligibilité de la campagne\]\[28\]



## Cas d'utilisation

Les campagnes déclenchées sont très efficaces pour les messages transactionnels ou axés sur les résultats.

Les campagnes transactionnelles comprennent les messages envoyés une fois que l'utilisateur a terminé un achat ou ajouté un article à son panier. Ce dernier cas est un bel exemple de campagne qui bénéficierait d'un événement exceptionnel. Dites que votre campagne rappelle aux utilisateurs des articles de leur panier qu'ils n'ont pas achetés. L'exception, dans ce cas, serait l'achat des produits dans leur panier. Pour les campagnes axées sur les accomplissements, vous pouvez envoyer un message 5 minutes après que l'utilisateur ait terminé une conversion ou a battu un niveau de jeu.

En outre, lors de la création de campagnes de bienvenue, vous pouvez déclencher des messages à envoyer après l'enregistrement de l'utilisateur ou la création d'un compte. Des messages étourdissants à envoyer dans les différents jours suivant l’inscription vous permettront de créer un processus d’intégration approfondi.



## Pourquoi un utilisateur n'a-t-il pas reçu ma campagne déclenchée ?

Chacune de ces choses empêchera un utilisateur qui a terminé l'événement de déclenchement de recevoir la campagne :

- L'utilisateur a terminé l'évènement d'exception avant que le délai ne s'écoule complètement.
- Le délai de temps a amené l'utilisateur à se qualifier pour recevoir la campagne après la fin de la durée.
- Le délai de temps a amené l'utilisateur à se qualifier pour recevoir la campagne en dehors de la partie spécifiée de la journée.
- L'utilisateur a déjà reçu la campagne, et les utilisateurs ne sont pas rééligibles.
- Alors que les utilisateurs sont rééligibles pour recevoir la campagne, ils ne peuvent le réactiver qu'après une certaine période de temps, et cette période de temps n'est pas encore écoulée.

[Segmenter]({{site.baseurl}}/user_guide/engagement_tools/segments/) une campagne déclenchée sur des données utilisateur enregistrées lors de l'événement peut causer une [condition de course]({{site.baseurl}}/help/best_practices/race_conditions/#race-conditions). Cela se produit lorsque l'attribut utilisateur sur lequel la campagne est segmentée est modifiée, mais le changement n'a pas été traité pour l'utilisateur lors de l'envoi de la campagne. Étant donné que les campagnes vérifient la présence d'un segment à l'entrée, cela peut conduire à ce que l'utilisateur ne reçoive pas la campagne.

Par exemple, imaginez que vous voulez envoyer une campagne déclenchée par un événement aux utilisateurs masculins qui viennent de s'inscrire. Lorsque l'utilisateur s'inscrit, vous enregistrez un événement personnalisé `inscription` et définissez simultanément l'attribut `sexe` de l'utilisateur. L'événement peut déclencher la campagne avant que Braze n'ait traité le sexe de l'utilisateur, l'empêchant de recevoir la campagne.

C'est une bonne pratique de s'assurer que l'attribut sur lequel la campagne est segmentée est vidé sur les serveurs de Braze avant l'événement. Dans les cas où ce n'est pas possible, la meilleure façon de garantir la livraison est d'utiliser [les propriétés d'événement personnalisées][48] pour attacher les propriétés utilisateur pertinentes à l'événement et appliquer un filtre de propriété pour la propriété d'événement spécifique au lieu d'un filtre de segmentation. Dans l'exemple ci-dessus, vous ajouterez une propriété `sexe` à l'inscription de l'événement personnalisé `` afin que Braze soit garanti d'avoir les données dont vous avez besoin lorsque votre campagne est déclenchée.

De plus, si une campagne est basée sur l'action et a un délai, vous pouvez cocher l'option de **réévaluer l'adhésion au segment à envoi-time** pour vous assurer que les utilisateurs font toujours partie du public cible lorsque le message est envoyé.

!\[réévaluer l'adhésion au segment \]\[51\]

[17]: {% image_buster /assets/img_archive/schedule_triggered1.png %} [19]: {% image_buster /assets/img_archive/schedule_triggered22.png %} [20]: {% image_buster /assets/img_archive/schedule_triggered32. ng %} [21]: {% image_buster /assets/img_archive/schedule_triggered43.png %} [24]: {% image_buster /assets/img_archive/ReEligible.png %} [27]: {% image_buster /assets/img_archive/schedule_triggered5. ng %} [28]: {% image_buster /assets/img_archive/schedule_triggered6.png %} [31]: {% image_buster /assets/img_archive/schedule_triggered_next_available.png %} [34]: {% image_buster /assets/img_archive/customEventProperties. ng %} [41]: {% image_buster /assets/img_archive/schedule_triggered7.png %} [50]: {% image_buster /assets/img_archive/schedule_triggered8. ng %} [51]: {% image_buster /assets/img_archive/reevaluate_segment_membership.png %}

[8]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[18]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[18]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[32]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[33]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/campaign_connector/#campaign-connector
[48]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[49]: {{site.baseurl}}/help/help_articles/campaigns_and_canvas/not_triggering/
