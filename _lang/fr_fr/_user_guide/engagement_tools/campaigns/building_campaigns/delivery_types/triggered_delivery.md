---
nav_title: Réception par événement
article_title: Réception par événement
page_order: 1
page_type: reference
description: "Le présent article de référence décrit comment déclencher des campagnes à envoyer après qu’un utilisateur a effectué un certain événement."
tool: Campaigns

---

# Livraison par événement

> Les campagnes de livraison par événement ou les campagnes déclenchées par des événements sont très efficaces pour les messages transactionnels ou basés sur le résultat. Au lieu d’envoyer votre campagne certains jours, vous pouvez les déclencher pour qu’elles s’envoient après qu’un utilisateur a effectué un certain événement. 

## Configurer une campagne avec déclencheur

### Étape 1 : Sélectionner un événement déclencheur

Sélectionnez un événement déclencheur. Il peut comprendre l’un des éléments suivants :
- Faire un achat
- Démarrer une session
- Réalisation d'un événement personnalisé
- Effectuer l’événement de conversion principal de la campagne
- Ajouter une adresse e-mail à un profil utilisateur
- Changer une valeur d'attribut personnalisé
- Mise à jour du statut d'abonnement
- Mise à jour du statut d'un groupe d'abonnement
- Interagir avec d’autres campagnes
    - Consultent un message in-app
    - Cliquent sur un message in-app
    - Cliquez sur le bouton de message in-app
    - Cliquer sur l’e-mail
    - Cliquez sur l’alias dans l’e-mail
    - Alias cliqué dans n'importe quelle campagne ou étape de Canvas
    - Ouvrir l’e-mail
    - Ouvre l’e-mail (ouverture automatique)
    - Ouvre l’e-mail (autres ouvertures)
    - Ouvrent directement une notification push
    - Cliquez sur le bouton de notification push
    - Cliquez sur la page de push story
    - Effectuent un événement de conversion
    - Recevoir un e-mail
    - Reçoit un SMS
    - Cliquez sur le lien SMS raccourci
    - Reçoivent une notification push
    - Reçoit le webhook
    - Sont inscrits dans le groupe de contrôle
    - Voir la carte de contenu
    - Cliquez sur la carte de contenu
    - Ignorer la carte de contenu
- Saisir une localisation
- Effectuer l’événement d’exception pour une autre campagne
- Interagir avec une étape de Canvas
- Déclencher un géorepérage
- Envoyer un message SMS entrant
- Envoi d'un message entrant WhatsApp

Vous pouvez également filtrer davantage les événements déclencheurs grâce aux [propriétés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) d'événement personnalisées de Braze, ce qui permet de personnaliser les propriétés d'événement pour les événements personnalisés et les achats in-app. Cette fonction vous permet d’adapter davantage quel utilisateur va recevoir un message sur la base des attributs spécifiques de l’événement personnalisé, ce qui permet une personnalisation plus importante de la campagne et une collecte de données plus sophistiquée. 

Supposons, par exemple, que nous ayons une campagne avec un événement personnalisé d’abandon de panier qui est ciblé par le filtre de propriété « valeur du panier ». Cette campagne n’atteindra que les utilisateurs qui ont abandonné entre 100 $ et 200 $ de marchandises dans leur panier. 

![]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
L'événement déclencheur « démarrer la session » peut être la toute première ouverture de l'application par l'utilisateur si le segment de votre campagne s'applique aux nouveaux utilisateurs. (par exemple, si votre segment se compose de ceux qui n'ont pas de sessions).
{% endalert %}

N’oubliez pas que vous pouvez toujours envoyer une campagne déclenchée à un segment spécifique d’utilisateurs, afin que ceux qui ne font pas partie du segment ne reçoivent pas la campagne même s’ils effectuent l’événement déclencheur. Si vous remarquez que des utilisateurs ne reçoivent pas la campagne alors qu'ils se sont qualifiés pour le segment, consultez notre section sur les [raisons pour lesquelles un utilisateur pourrait ne pas avoir reçu une campagne déclenchée]({{site.baseurl}}/help/help_articles/campaigns_and_canvas/not_triggering/).

En ce qui concerne l’événement déclencheur défini quand un utilisateur ajoute une adresse e-mail à son profil, les règles suivantes s’appliquent :

- L’événement déclencheur sera activé après la mise à jour des attributs de profil utilisateur. Cela signifie que l’évaluation des segments et des filtres de la campagne se produira après toute mise à jour d’attribut. Ceci est bénéfique car cela vous permet de configurer des filtres tels que « l'adresse e-mail correspond à gmail.com » pour créer une campagne de déclenchement qui n'envoie qu'aux utilisateurs de Gmail et se déclenche dès qu'ils ajoutent leur adresse e-mail.
- L’événement déclencheur s’active lorsqu’une adresse e-mail est ajoutée à un profil utilisateur. Si vous avez plusieurs profils d’utilisateur que vous créez avec la même adresse e-mail, la campagne peut être déclenchée plusieurs fois, une fois pour chaque profil utilisateur.

En outre, les messages in-app déclenchés sont toujours conformes aux règles de livraison des messages in-app et apparaissent au début de la session de l’application.

![]({% image_buster /assets/img_archive/schedule_triggered1.png %})

### Étape 2 : Sélectionner la longueur du délai

Sélectionnez la durée d’attente avant d’envoyer la campagne une fois les critères de déclenchement satisfaits. Si la longueur du délai choisi est supérieure à la durée d’envoi du message, aucun utilisateur ne recevra la campagne. 

De plus, les utilisateurs qui complètent l'événement déclencheur après le lancement de votre campagne seront les premiers à commencer à recevoir le message après l'expiration du délai. Les utilisateurs qui ont terminé l’événement déclencheur avant que la campagne ne commence ne sont pas qualifiés pour recevoir la campagne.

![]({% image_buster /assets/img_archive/schedule_triggered22.png %})

Vous pouvez également choisir d’envoyer la campagne soit un jour spécifique de la semaine (en choisissant « au prochain » puis en sélectionnant un jour) ou un nombre spécifique de jours dans l’avenir (en sélectionnant « dans »). Vous pouvez également choisir d'envoyer votre message en utilisant la fonctionnalité [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) au lieu de sélectionner manuellement une heure de livraison.

![]({% image_buster /assets/img_archive/schedule_triggered7.png %})
![]({% image_buster /assets/img_archive/schedule_triggered8.png %})

### Étape 3 : Sélectionner des événements d’exception

Sélectionnez un événement d’exception qui disqualifiera les utilisateurs pour la réception de cette campagne. Vous ne pouvez le faire que si votre message déclenché est envoyé après un délai temporel. Les [événements d'exception]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#exception-events) peuvent être la réalisation d'un achat, le démarrage d'une session, l'exécution de l'un des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events) désignés par une campagne ou l'exécution d'un événement personnalisé. Si un utilisateur effectue l’événement déclencheur mais effectue ensuite votre événement d’exception avant que le message ne soit envoyé en raison du délai temporel, il ne recevra pas la campagne. Les utilisateurs qui ne reçoivent pas la campagne en raison de l'événement d'exception seront automatiquement éligibles pour la recevoir à l'avenir, la prochaine fois qu'ils complètent l'événement déclencheur, même si vous ne choisissez pas que les utilisateurs deviennent [à nouveau éligibles]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/).

![]({% image_buster /assets/img_archive/schedule_triggered32.png %})

Vous pouvez en savoir plus sur la façon d'utiliser les événements d'exception dans notre section sur les [cas d'utilisation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#use-cases).

> Si vous envoyez une campagne avec un événement déclencheur qui correspond à l'événement d'exception, Braze annulera la campagne et reprogrammera automatiquement une nouvelle campagne en fonction de l'heure de livraison du message de l'événement d'exception. Par exemple, si votre premier événement déclencheur commence à cinq minutes et que l'événement d'exception commence à 10 minutes, vous vous fieriez aux 10 minutes de l'événement d'exception comme heure officielle de livraison du message de la campagne.

{% alert note %}
Vous ne pouvez pas faire que l’événement « démarrer la session » soit à la fois l’événement déclencheur et l’événement d’exception d’une campagne. Cependant, vous avez toujours la possibilité de sélectionner tout autre événement personnalisé en dehors de cette option.
{% endalert %}

### Étape 4 : Attribuer une durée

Attribuez la durée de la campagne en spécifiant une heure de début et une heure de fin facultative.

![]({% image_buster /assets/img_archive/schedule_triggered43.png %})

Si un utilisateur effectue un événement déclencheur pendant la période spécifiée, mais qu’il est éligible pour le message en dehors du délai imparti en raison d’un délai planifié, il ne recevra pas la campagne. Par conséquent, si vous définissez un délai plus long que la durée du message, aucun utilisateur ne recevra votre campagne. De plus, vous pouvez choisir d'envoyer le message dans les [fuseaux horaires locaux des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/#local-time-zone-campaigns).

### Étape 5 : Sélectionner la fenêtre temporelle

Indiquez si l’utilisateur recevra la campagne pendant à un moment spécifique de la journée. Si vous donnez au message une fenêtre de réception et que l’utilisateur effectue l’événement déclencheur en dehors de cette fenêtre ou que le délai du message entraîne le fait qu’il la rate, alors, par défaut, l’utilisateur ne recevra pas votre message.

![]({% image_buster /assets/img_archive/schedule_triggered5.png %})

Dans le cas où un utilisateur effectue l’événement déclencheur dans la fenêtre temporelle, mais que le délai de message le fait sortir de cette fenêtre, vous pouvez cocher la case suivante pour que ces utilisateurs reçoivent toujours la campagne.

![]({% image_buster /assets/img_archive/schedule_triggered_next_available.png %})

Si un utilisateur ne reçoit pas le message parce qu’il manque la fenêtre temporelle, il sera toujours éligible pour la recevoir la prochaine fois qu’il effectuera l’événement déclencheur, même si vous ne choisissez pas de rendre les utilisateurs [rééligibles]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/). Si vous choisissez d’autoriser les utilisateurs à devenir rééligibles, ils peuvent recevoir la campagne chaque fois qu’ils effectuent l’événement déclencheur, en supposant qu’ils sont admissibles pendant la période spécifiée.

Si vous avez également attribué une certaine durée à la campagne, un utilisateur doit être admissible à la fois à la durée et au moment spécifique de la journée pour recevoir le message.

### Étape 6 : Déterminer la rééligibilité

Déterminez si les utilisateurs peuvent devenir [rééligibles]({% image_buster /assets/img_archive/ReEligible.png %}) pour la campagne. Si vous autorisez les utilisateurs à devenir rééligibles, vous pouvez spécifier un délai avant que l’utilisateur puisse recevoir à nouveau la campagne. Cela empêchera les campagnes déclenchées de devenir « indésirables ».

![]({% image_buster /assets/img_archive/schedule_triggered6.png %})

## Cas d’utilisation

Les campagnes déclenchées sont très efficaces pour les messages transactionnels ou basés sur le résultat.

Les campagnes transactionnelles comprennent les messages envoyés après que l’utilisateur effectue un achat ou ajoute un article à son panier. Ce dernier cas est un excellent exemple d’une campagne qui pourrait bénéficier d’un événement d’exception. Imaginez que votre campagne rappelle aux utilisateurs la présence d’articles dans leur panier qu’ils n’ont pas acheté. Dans ce cas, l’utilisateur achetant les produits dans son panier deviendrait l’événement d’exception. Pour les campagnes basées sur les résultats, vous pouvez envoyer un message 5 minutes après que l’utilisateur a achevé une conversion ou battu un niveau de jeu.

De plus, lors de la création de campagnes de bienvenue, vous pouvez déclencher des messages à envoyer après que l’utilisateur s’enregistre ou configure un compte. Répartir des messages à envoyer différents jours suivant l’inscription vous permettra de créer un processus d’onboarding complet.

## Pourquoi un utilisateur n’a-t-il pas reçu ma campagne déclenchée ?

L’un des éléments suivants empêchera un utilisateur qui a effectué l’événement déclencheur de recevoir la campagne :

- L’utilisateur a effectué l’événement d’exception avant que le délai ne soit complètement écoulé.
- La [logique Liquid `abort_message`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) a été utilisée et le message a été annulé selon les règles ou la logique `abort_message`.
- Le délai a poussé l’utilisateur à devenir admissible à recevoir la campagne après que sa durée est terminée.
- Le délai a poussé l’utilisateur à devenir admissible à recevoir la campagne en dehors du moment de la journée spécifié.
- L’utilisateur a déjà reçu la campagne et les utilisateurs ne sont pas rééligibles.
- Bien que les utilisateurs soient rééligibles pour recevoir la campagne, ils ne peuvent la déclencher à nouveau qu’après une certaine période temporelle et elle n’est pas encore écoulée.

[Segmenter]({{site.baseurl}}/user_guide/engagement_tools/segments/) une campagne déclenchée sur les données utilisateur enregistrées au moment de l'événement peut provoquer une [condition de course]({{site.baseurl}}/help/best_practices/race_conditions/#race-conditions). Cela se produit lorsque l’attribut utilisateur sur lequel la campagne est segmentée est modifié, mais que le changement n’a pas été traité pour l’utilisateur lorsque la campagne est envoyée. Étant donné que les campagnes vérifient l’appartenance au segment à l’entrée, cela peut entraîner des utilisateurs ne recevant pas la campagne.

Imaginez par exemple que vous souhaitiez envoyer une campagne déclenchée par un événement aux utilisateurs masculins qui viennent juste de s’enregistrer. Lorsque l’utilisateur s’enregistre, vous notez un événement personnalisé `registration` et définissez simultanément un attribut `gender`. L’événement peut déclencher la campagne avant que Braze ne traite le genre de l’utilisateur, ce qui empêche qu’il ne reçoive la campagne.

En tant que bonne pratique, assurez-vous que l’attribut sur lequel la campagne est segmentée est envoyé vers les serveurs de Braze avant l’événement. Si ce n'est pas possible, la meilleure façon de garantir la réception/distribution est d'utiliser des [propriétés d'événement personnalisées]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) pour attacher les propriétés utilisateur pertinentes à l'événement et d'appliquer un filtre de propriété pour la propriété d'événement spécifique au lieu d'un filtre de segmentation. Dans notre exemple, vous ajouteriez une propriété `gender` à l’événement personnalisé `registration` afin que Braze dispose forcément des données dont vous avez besoin lorsque votre campagne est déclenchée.

De plus, si une campagne est basée sur l'action et a un délai, vous pouvez cocher l'option **Réévaluer l'appartenance au segment au moment de l'envoi** pour vous assurer que les utilisateurs font toujours partie du public cible lorsque le message est envoyé.

Si votre campagne est déclenchée par un événement personnalisé spécifique et que vous sélectionnez un segment comme audience, les utilisateurs doivent effectuer le même événement personnalisé pour être inclus dans le segment. Cela signifie que les utilisateurs doivent faire partie du public avant qu'une campagne basée sur des actions puisse être déclenchée. Le flux de travail général pour une campagne déclenchée est le suivant :

1. **Rejoindre l’audience :** Lorsqu'un utilisateur effectue l'événement personnalisé, il est ajouté au public cible de la campagne.
2. **Déclencher l'e-mail :** Un utilisateur doit effectuer à nouveau l'événement personnalisé pour déclencher l'e-mail, car il doit faire partie du public avant que l'e-mail puisse être envoyé.

Nous recommandons soit de changer le public cible pour inclure tous les utilisateurs, soit de vérifier que les utilisateurs censés effectuer l'événement font déjà partie du public de la campagne pour que le message soit déclenché.

![]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

### Résolution des problèmes des événements personnalisés

Tout d'abord, confirmez que l'événement personnalisé est transmis à Braze. Accédez à **Analyse/analytique** > **Rapport sur les événements personnalisés**, puis sélectionnez l'événement personnalisé et la plage de dates correspondants. Si l'événement ne s'affiche pas, vérifiez qu'il est correctement configuré et que l'utilisateur a effectué la bonne action.

Si l'événement personnalisé s'affiche, poursuivez la résolution des problèmes en procédant comme suit :

- Vérifiez le téléchargement du profil utilisateur pour confirmer qu'il a déclenché l'événement et quand il l'a fait. Si l'événement a été déclenché, comparez l'horodatage du déclenchement de l'événement à la durée en ligne/en production/instantanée de la campagne. L'événement peut avoir été déclenché avant que la campagne ne soit en ligne/en production/instantanée.
- Examinez les journaux des modifications pour la campagne et tous les segments utilisés dans le ciblage afin de déterminer si l'utilisateur se trouvait dans le segment lorsque son événement personnalisé a été déclenché. S'ils ne faisaient pas partie de la segmentation, ils n'auraient pas reçu la campagne.
- Vérifiez si l'utilisateur a été intégré dans un groupe de contrôle par le biais de la segmentation et, par conséquent, s'il n'a pas pu recevoir la campagne.
- En cas de retard planifié, vérifiez si l'événement personnalisé de l'utilisateur a été déclenché avant le retard. Si l'événement avait été déclenché avant le délai, ils n'auraient pas reçu la campagne.

{% alert note %}
Les messages in-app ne peuvent être déclenchés que par des événements envoyés via le SDK, et non via l'API REST.
{% endalert %}

