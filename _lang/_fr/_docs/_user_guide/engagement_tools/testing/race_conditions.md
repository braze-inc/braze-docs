---
nav_title: Conditions de la course
article_title: Conditions de la course
alias: /fr/race_conditions/
page_order: 9
page_type: Référence
description: "Cet article couvre les meilleures pratiques pour éviter que les conditions de course n'affectent vos campagnes de messagerie."
---

# Conditions de la course

Une **condition de course** est un concept où un résultat dépend de la séquence ou du calendrier d'autres événements. Par exemple, si la séquence désirée d'événements est "Événement A" puis "Événement B", mais parfois "Evénement A" vient en premier et d'autres fois "Evénement B" vient en premier, ce qui est connu comme une condition de course.

{% include video.html id="LyJaxDoMtMs" align="right" %}

## Cibler les nouveaux utilisateurs

Sur la plateforme de Braze, une des conditions de course les plus courantes se produit avec des messages ciblant les nouveaux utilisateurs. Ici, l'ordre des événements attendu est :

1. Un utilisateur est créé;
2. Le même utilisateur est immédiatement ciblé pour un message.

Cependant, dans certains cas, le deuxième événement se déclenchera en premier. Cela signifie qu'un message tente d'être envoyé à un utilisateur qui n'a pas encore été créé. et en conséquence, l'utilisateur ne le reçoit jamais.

## Utilisation de plusieurs terminaux API

Si vous utilisez des points de terminaison API distincts pour créer des utilisateurs et déclencher des campagnes Canvas/s, cela peut également entraîner cette condition de course. Lorsque les informations de l'utilisateur sont envoyées à Braze via le point de terminaison `utilisateurs/piste,` il peut parfois prendre quelques secondes à traiter. En conséquence, lorsque des requêtes sont faites aux `utilisateurs/pistes` et [terminaux de messagerie][4] en même temps, il n'y a aucune garantie que les informations de l'utilisateur seront mises à jour avant l'envoi d'un message. Si ces requêtes sont effectuées dans le même appel API, il ne devrait pas y avoir de problème. Veuillez noter que si vous envoyez un appel API de message planifié, ces requêtes __doivent__ être séparées, et un utilisateur doit être créé avant d'envoyer un appel API échappé.

{% alert note %}
Si les attributs de l'utilisateur sont envoyés via le SDK ou dans le même utilisateur/appel de suivi que l'événement, alors Braze traitera automatiquement ceux avant de tenter d'envoyer un message.
{% endalert %}

Une façon d'éviter cette condition de course est d'ajouter un retard, environ une minute, entre la création d'un utilisateur, et le ciblage de cet utilisateur par votre Canvas ou campagne.

De même, vous pouvez utiliser l'objet [`Attributs`][1] pour ajouter/créer/mettre à jour un utilisateur, puis les cibler en utilisant soit le [`canvas/trigger/send`][2] ou [`campagne/trigger/send`][3] endpoint. Cet appel API traitera l'objet `Attributs` avant de cibler les utilisateurs.

Les attributs qui sont inclus dans cet objet seront traités avant que Braze ne commence à envoyer la campagne. Si le drapeau `send_to_existing_only` est défini à false, et qu'un `external_user_id` n'existe pas dans la base de données de Braze, Braze va créer un profil utilisateur pour le `external_user_id` et traiter les attributs associés au profil utilisateur avant que Braze ne commence à envoyer la campagne. Notez également que si le flag `send_to_existing_only` est défini à false, alors l'objet attributs doit être inclus afin de créer l'utilisateur.

## Les déclencheurs d'actions correspondants et les filtres d'audience

Une autre condition de course courante peut se produire si vous configurez une campagne basée sur l'action ou Canvas avec le même déclencheur que le filtre d'audience (i. ., un attribut modifié ou effectué un événement personnalisé). L'utilisateur ne peut pas être dans le public au moment où il effectue l'événement de déclenchement ce qui signifie qu'ils ne recevront pas la campagne ou n'entreront pas dans le Canvas. Dans ce cas, Braze vous recommande d'éviter de configurer votre déclencheur pour qu'il corresponde à votre filtre d'audience.


[1]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[2]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[3]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[4]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
