---
nav_title: Livraison/distribution par événement
article_title: Livraison/distribution par événement
page_order: 1
page_type: reference
description: "Cet article de référence décrit comment déclencher l'envoi de campagnes après qu'un utilisateur a accompli un certain événement."
tool: Campaigns

---

# Livraison/distribution par événement

> Les campagnes de réception/distribution basées sur l'action ou les campagnes déclenchées par un événement sont très efficaces pour les messages transactionnels ou basés sur l'accomplissement. Au lieu d'envoyer votre campagne certains jours, vous pouvez déclencher leur envoi après qu'un utilisateur ait accompli un certain événement. 

## Implémenter une campagne déclenchée

### Étape 1 : Sélectionnez un événement déclencheur

Sélectionnez un événement déclencheur. Il peut s'agir de l'un des éléments suivants :
- Effectuer un achat
- Démarrer une session
- Exécution d'un événement personnalisé
- Réalisation de l'événement de conversion principal de la campagne
- Ajout d'une adresse e-mail à un profil utilisateur
- Modification de la valeur d'un attribut personnalisé
- Mise à jour de l'état d'un abonnement
- Mise à jour du statut du groupe d'abonnement
- Interagir avec d'autres campagnes
    - Voir le message in-app
    - Cliquez sur le message in-app.
    - Cliquez sur les boutons d'envoi de messages in-app.
    - Cliquez sur e-mail
    - Cliquez sur l'alias dans l'e-mail
    - Alias cliqué dans une campagne ou une étape du canvas
    - Ouvrir l'e-mail
    - Ouvrir un e-mail (machine ouverte)
    - Ouvrir un e-mail (autres ouvertures)
    - Ouvrir directement la notification push
    - Cliquez sur le bouton de notification push
    - Cliquez sur la page du contenu push
    - Effectuer un événement de conversion
    - Recevoir un e-mail
    - Recevoir des SMS
    - Cliquez sur le lien SMS abrégé
    - Recevoir une notification push
    - Recevoir un webhook
    - Sont inscrits dans le groupe de contrôle
    - Voir la carte de contenu
    - Cliquez sur la carte de contenu
    - Fermeture de la carte de contenu
- Saisir un emplacement/localisation
- Exécution de l'événement d'exception pour une autre campagne
- Interagir avec une étape du canvas
- Déclencher un géorepérage
- Envoi d'un message SMS entrant
- Envoi d'un message WhatsApp entrant

Vous pouvez également filtrer davantage les événements déclencheurs grâce aux [propriétés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) d'événement personnalisées de Braze, ce qui permet de personnaliser les propriétés d'événement pour les événements personnalisés et les achats in-app. Cette fonctionnalité vous permet d'adapter davantage les utilisateurs qui reçoivent un message en fonction des attributs personnalisés de l'événement, ce qui permet une plus grande personnalisation de la campagne et une collecte de données plus sophistiquée. 

Par exemple, disons que nous avons une campagne avec un événement personnalisé d'abandon de panier qui est davantage ciblé par le filtre de la propriété "valeur du panier". Cette campagne ne touchera que les utilisateurs qui ont laissé entre 100 et 200 dollars de marchandises dans leur panier. 

\![]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
L'événement déclencheur "début de session" peut correspondre à la toute première ouverture de l'application par l'utilisateur si la segmentation de votre campagne s'applique aux nouveaux utilisateurs. (par exemple, si votre segmentation est constituée de ceux qui n'ont pas encore ouvert de session).
{% endalert %}

Gardez à l'esprit que vous pouvez toujours envoyer une campagne déclenchée à un segment spécifique d'utilisateurs, de sorte que les utilisateurs qui ne font pas partie du segment ne recevront pas la campagne même s'ils accomplissent l'événement déclencheur. Si vous remarquez que des utilisateurs ne reçoivent pas la campagne alors qu'ils se sont qualifiés pour le segment, consultez notre section sur les [raisons pour lesquelles un utilisateur pourrait ne pas avoir reçu une campagne déclenchée]({{site.baseurl}}/help/help_articles/campaigns_and_canvas/not_triggering/).

En ce qui concerne l'événement déclencheur lorsqu'un utilisateur ajoute une adresse e-mail à son profil, les règles suivantes s'appliquent :

- L'événement déclencheur sera déclenché après la mise à jour de l'attribut du profil utilisateur. Cela signifie que l'évaluation des segments et des filtres de la campagne se fera après toute mise à jour des attributs. Cette fonction est utile car elle vous permet d'implémenter des filtres tels que "l'adresse e-mail correspond à gmail.com" pour créer une campagne de déclencheurs qui n'envoie des messages qu'aux utilisateurs de Gmail et qui se déclenche dès qu'ils ajoutent leur adresse e-mail.
- L'événement déclencheur se déclenche lorsqu'une adresse e-mail est ajoutée à un profil utilisateur. Si vous avez plusieurs profils utilisateurs créés avec la même adresse e-mail, la campagne peut être déclenchée plusieurs fois, une fois pour chaque profil utilisateur.

En outre, les messages in-app déclenchés respectent toujours les règles de réception/distribution des messages in-app et apparaissent au début d'une session d'application.

\![]({% image_buster /assets/img_archive/schedule_triggered1.png %})

### Étape 2 : Sélectionner la durée du délai

Sélectionnez le délai d'attente avant l'envoi de la campagne lorsque les critères de déclenchement sont remplis. Si le délai choisi est plus long que la durée d'envoi du message, aucun utilisateur ne recevra la campagne. 

En outre, les utilisateurs qui accomplissent l'événement déclencheur après le lancement de votre campagne seront les premiers à commencer à recevoir le message une fois le délai écoulé. Les utilisateurs qui ont terminé l'événement déclencheur avant le lancement de la campagne ne pourront pas recevoir la campagne.

\![]({% image_buster /assets/img_archive/schedule_triggered22.png %})

Vous pouvez également choisir d'envoyer la campagne un jour précis de la semaine (en choisissant "le jour suivant" puis en sélectionnant un jour) ou un nombre précis de jours (en sélectionnant "dans") à l'avenir. Vous pouvez également choisir d'envoyer votre message à l'aide de la fonctionnalité de [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) au lieu de sélectionner manuellement une heure de réception/distribution.

\![]({% image_buster /assets/img_archive/schedule_triggered7.png %})
\![]({% image_buster /assets/img_archive/schedule_triggered8.png %})

### Étape 3 : Sélectionner les événements d'exception

Sélectionnez un événement d'exception qui empêchera les utilisateurs de recevoir cette campagne. Vous ne pouvez le faire que si votre message déclenché est envoyé après un certain délai. Les [événements d'exception]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#exception-events) peuvent être la réalisation d'un achat, le démarrage d'une session, l'exécution de l'un des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events) désignés par une campagne ou l'exécution d'un événement personnalisé. Si un utilisateur réalise l'événement déclencheur mais réalise ensuite votre événement d'exception avant l'envoi du message en raison du délai, il ne recevra pas la campagne. Les utilisateurs qui ne reçoivent pas la campagne en raison de l'événement d'exception seront automatiquement éligibles pour la recevoir à l'avenir, la prochaine fois qu'ils accompliront l'événement déclencheur, même si vous ne choisissez pas que les utilisateurs deviennent [à nouveau éligibles]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/).

\![]({% image_buster /assets/img_archive/schedule_triggered32.png %})

Pour en savoir plus sur l'utilisation des événements d'exception, consultez notre section sur les [cas d'utilisation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#use-cases).

> Si vous envoyez une campagne avec un événement déclencheur qui correspond à l'événement d'exception, Braze annule la campagne et planifie automatiquement une nouvelle campagne en fonction de l'heure de réception/distribution du message de l'événement d'exception. Par exemple, si votre premier événement déclencheur commence à cinq minutes et que l'événement d'exception commence à 10 minutes, vous vous baserez sur les 10 minutes de l'événement d'exception comme délai de réception/distribution du message de la campagne officielle.

{% alert note %}
Vous ne pouvez pas faire du "début de session" à la fois l'événement déclencheur et l'événement d'exception d'une campagne. Toutefois, vous avez toujours la possibilité de sélectionner tout autre événement personnalisé en dehors de cette option.
{% endalert %}

### Étape 4 : Attribuer une durée

Attribuez la durée de la campagne en spécifiant une heure de début et une heure de fin facultative.

\![]({% image_buster /assets/img_archive/schedule_triggered43.png %})

Si un utilisateur réalise un événement déclencheur pendant la période spécifiée, mais se qualifie pour le message en dehors de cette période en raison d'un délai planifié, il ne recevra pas la campagne. Par conséquent, si vous fixez un délai plus long que celui du message, aucun utilisateur ne recevra votre campagne. En outre, vous pouvez choisir d'envoyer le message dans le [fuseau horaire local]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/#local-time-zone-campaigns) des utilisateurs.

### Étape 5 : Sélectionnez une période

Indiquez si l'utilisateur recevra la campagne pendant une partie spécifique de la journée. Si vous donnez un délai au message et que l'utilisateur effectue l'événement déclencheur en dehors de ce délai ou que le délai du message lui fait manquer le délai, l'utilisateur ne recevra pas votre message par défaut.

\![]({% image_buster /assets/img_archive/schedule_triggered5.png %})

Dans le cas où un utilisateur réalise l'événement déclencheur dans le délai imparti, mais que le retard du message fait sortir l'utilisateur du délai imparti, vous pouvez cocher la case suivante pour que ces utilisateurs reçoivent tout de même la campagne.

\![]({% image_buster /assets/img_archive/schedule_triggered_next_available.png %})

Si un utilisateur ne reçoit pas le message parce qu'il n'a pas respecté le délai, il sera toujours qualifié pour le recevoir la prochaine fois qu'il accomplira l'événement déclenchcheur, même si vous n'avez pas choisi que les utilisateurs soient [rééligibles]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/). Si vous choisissez de rendre les utilisateurs rééligibles, les utilisateurs peuvent recevoir la campagne chaque fois qu'ils accomplissent l'événement déclencheur, à condition qu'ils se qualifient pendant la période spécifiée.

Si vous avez également attribué une certaine durée à la campagne, l'utilisateur doit se qualifier à la fois pour la durée et pour la partie spécifique de la journée pour recevoir le message.

### Étape 6 : Déterminer la rééligibilité

Déterminez si les utilisateurs peuvent devenir [rééligibles]]({% image_buster /assets/img_archive/ReEligible.png %}) pour la campagne. Si vous autorisez les utilisateurs à redevenir éligibles, vous pouvez spécifier un délai avant que l'utilisateur ne puisse recevoir à nouveau la campagne. Vous éviterez ainsi que vos campagnes déclenchées ne deviennent "spammy".

\![]({% image_buster /assets/img_archive/schedule_triggered6.png %})

## Cas d'utilisation

Les campagnes déclenchées sont très efficaces pour les messages transactionnels ou axés sur la réussite.

Les campagnes transactionnelles comprennent les messages envoyés après que l'utilisateur a effectué un achat ou ajouté un article à son panier. Ce dernier cas est un excellent exemple de campagne qui bénéficierait d'un événement d'exception. Imaginons que votre campagne rappelle aux utilisateurs les articles de leur panier qu'ils n'ont pas achetés. L'événement d'exception, dans ce cas, serait l'achat par l'utilisateur des produits contenus dans son panier. Pour les campagnes basées sur les réalisations, vous pouvez envoyer un message 5 minutes après que l'utilisateur a effectué une conversion ou qu'il a atteint un niveau de jeu.

En outre, lorsque vous créez des campagnes de bienvenue, vous pouvez déclencher des messages à envoyer après que l'utilisateur s'est enregistré ou a créé un compte. L'échelonnement des messages à envoyer les différents jours suivant l'inscription vous permettra de créer un processus d'onboarding approfondi.

## Pourquoi un utilisateur n'a-t-il pas reçu ma campagne déclenchée ?

L'un ou l'autre de ces éléments empêchera un utilisateur qui a terminé l'événement déclencheur de recevoir la campagne :

- L'utilisateur a terminé l'événement d'exception avant la fin du délai.
- La [logique de]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) Liquid [`abort_message` a été utilisée et le message a été interrompu sur la base de la logique ou des règles de]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) `abort_message`.
- Le délai a permis à l'utilisateur de se qualifier pour recevoir la campagne après la fin de la durée.
- En raison de ce retard, l'utilisateur s'est qualifié pour recevoir la campagne en dehors de la période spécifiée de la journée.
- L'utilisateur a déjà reçu la campagne et les utilisateurs ne sont pas rééligibles.
- Si les utilisateurs peuvent à nouveau bénéficier de la campagne, ils ne peuvent la déclencher à nouveau qu'après un certain délai, et ce délai n'est pas encore écoulé.

[La segmentation d']({{site.baseurl}}/user_guide/engagement_tools/segments/) une campagne déclenchée sur les données utilisateur enregistrées au moment de l'événement peut provoquer une [condition de concurrence]({{site.baseurl}}/help/best_practices/race_conditions/#race-conditions). Cela se produit lorsque l'attribut de l'utilisateur sur lequel la campagne est segmentée est modifié, mais que le changement n'a pas été traité pour l'utilisateur au moment de l'envoi de la campagne. Étant donné que les campagnes vérifient l'appartenance à un segment à l'entrée, l'utilisateur risque de ne pas recevoir la campagne.

Par exemple, imaginez que vous souhaitiez envoyer une campagne déclenchée par un événement aux utilisateurs masculins qui viennent de s'inscrire. Lorsque l'utilisateur s'enregistre, vous enregistrez un événement personnalisé `registration` et définissez simultanément l'attribut `gender` de l'utilisateur. L'événement peut déclencher la campagne avant que Braze n'ait traité le sexe de l'utilisateur, l'empêchant ainsi de recevoir la campagne.

En tant que meilleure pratique, assurez-vous que l'attribut sur lequel la campagne est segmentée est envoyé sur les serveurs de Braze avant l'événement. Si ce n'est pas possible, la meilleure façon de garantir la réception/distribution est d'utiliser des [propriétés d'événement personnalisées]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) pour attacher les propriétés utilisateur pertinentes à l'événement et d'appliquer un filtre de propriété pour la propriété d'événement spécifique au lieu d'un filtre de segmentation. Dans notre exemple, vous ajouterez une propriété `gender` à l'événement personnalisé `registration` afin que Braze soit assuré de disposer des données dont vous avez besoin lorsque votre campagne est déclenchée.

En outre, si une campagne est basée sur des actions et comporte un délai, vous pouvez cocher l'option **Réévaluer l'appartenance à un segment au moment de l'envoi** afin de vous assurer que les utilisateurs font toujours partie de l'audience cible au moment de l'envoi du message.

Si votre campagne est déclenchée par un événement personnalisé spécifique et que vous sélectionnez un segment comme audience, les utilisateurs doivent effectuer le même événement personnalisé pour être inclus dans le segment. Cela signifie que les utilisateurs doivent faire partie de l'audience avant qu'une campagne basée sur l'action puisse être déclenchée. Le déroulement général d'une campagne déclenchée est le suivant :

1. **Rejoignez l'audience :** Lorsqu'un utilisateur réalise l'événement personnalisé, il est ajouté à l'audience cible de la campagne.
2. **Déclenchez l'e-mail :** Un utilisateur doit à nouveau effectuer l'événement personnalisé pour déclencher l'e-mail, car il doit faire partie de l'audience pour que l'e-mail puisse être envoyé.

Nous vous recommandons soit de modifier l'audience cible pour y inclure tous les utilisateurs, soit de vérifier que les utilisateurs censés effectuer l'événement font déjà partie de l'audience de la campagne pour que le message soit déclenché.

\![]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

### Résolution des problèmes des événements personnalisés

Tout d'abord, confirmez que l'événement personnalisé est transmis à Braze. Accédez à **Analyse/analytique** > **Rapport sur les événements personnalisés**, puis sélectionnez l'événement personnalisé et la plage de dates correspondants. Si l'événement ne s'affiche pas, vérifiez qu'il est correctement configuré et que l'utilisateur a effectué la bonne action.

Si l'événement personnalisé s'affiche, poursuivez la résolution des problèmes en procédant comme suit :

- Vérifiez le téléchargement du profil utilisateur pour confirmer qu'il a déclenché l'événement et quand il l'a fait. Si l'événement a été déclenché, comparez l'horodatage du déclenchement de l'événement à la durée en ligne/en production/instantanée de la campagne. L'événement peut avoir été déclenché avant que la campagne ne soit en ligne/en production/instantanée.
- Examinez les journaux des modifications pour la campagne et tous les segments utilisés dans le ciblage afin de déterminer si l'utilisateur se trouvait dans le segment lorsque son événement personnalisé a été déclenché. S'ils ne faisaient pas partie du segment, ils n'auraient pas reçu la campagne.
- Vérifiez si l'utilisateur a été intégré dans un groupe de contrôle par le biais de la segmentation et, par conséquent, s'il n'a pas pu recevoir la campagne.
- En cas de retard planifié, vérifiez si l'événement personnalisé de l'utilisateur a été déclenché avant le retard. Si l'événement avait été déclenché avant le délai, ils n'auraient pas reçu la campagne.

{% alert note %}
Les messages in-app ne peuvent être déclenchés que par des événements envoyés via le SDK, et non via l'API REST.
{% endalert %}

