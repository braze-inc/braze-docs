---
nav_title: Conditions de concurrence
article_title: Conditions de concurrence
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Cet article aborde les meilleures pratiques à suivre pour éviter les conditions de concurrence qui affectent vos campagnes de communication."

---

# Conditions de concurrence

Une condition de concurrence est un concept à travers lequel un résultat dépend de la séquence ou du timing d’autres événements. Par exemple, si la séquence d’événements souhaitée est « événement A », puis « événement B », mais que « événement B » arrive parfois en premier, cette situation est connue sous le nom de condition de concurrence.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

## Cibler de nouveaux utilisateurs

Dans Braze, l’une des conditions de concurrence les plus courantes se produit avec des messages qui ciblent de nouveaux utilisateurs. Dans ce cas, l’ordre attendu des événements est le suivant : 

1. Un utilisateur est créé ; 
2. Le même utilisateur est immédiatement ciblé par un message. 

Cependant, dans certains cas, le deuxième événement se déclenchera d’abord. Cela signifie qu’un message tente d’être envoyé à un utilisateur qui n’a pas encore été créé, et par conséquent, l’utilisateur ne recevra jamais le message en question.

## Utiliser plusieurs endpoints API

Si vous utilisez des endpoints API distincts pour créer des utilisateurs et déclencher des campagnes ou Canvas, cela peut également entraîner une condition de concurrence. Lorsque des informations utilisateur sont envoyées à Braze via l’endpoint `users/track`, le traitement de ces informations peut parfois prendre quelques secondes. Par conséquent, lorsque des requêtes sont envoyées aux endpoints `users/track` et [de messagerie][4] en même temps, il n’est pas garanti que les informations utilisateur seront mises à jour avant qu’un message ne soit envoyé. Si ces requêtes sont effectuées dans le même appel d’API, il ne devrait y avoir aucun problème. Notez que si vous envoyez un appel d’API pour un message planifié, ces requêtes doivent être séparées et un utilisateur doit être créé avant d’envoyer l’appel d’API programmé.

{% alert note %}
Si les attributs utilisateur sont envoyés via le SDK ou dans le même appel « user/track » que l’événement, alors Braze traitera automatiquement ces attributs avant d’essayer d’envoyer un message.
{% endalert %}

Un moyen d’éviter cette condition de concurrence est d’ajouter un délai (d’environ une minute) entre la création d’un utilisateur et le ciblage de cet utilisateur par votre Canvas ou votre campagne. 

De même, vous pouvez utiliser l’objet [`Attributes`][1] pour ajouter, créer ou mettre à jour un utilisateur, puis le cibler en utilisant l’endpoint [`canvas/trigger/send`][2] ou [`campaign/trigger/send`][3]. Cet appel d’API traitera les `Attributes` avant de cibler les utilisateurs.

Les attributs inclus dans cet objet seront traités avant que Braze ne commence à envoyer la campagne. Si l’indicateur `send_to_existing_only` est défini sur faux, et qu’il n’existe aucun `external_user_id` dans la base de données de Braze, Braze créera un profil utilisateur pour l’`external_user_id` et traitera les attributs associés au profil utilisateur avant de commencer à envoyer la campagne. Notez également que si l’indicateur `send_to_existing_only` est défini sur faux, l’objet Attributs doit être inclus pour pouvoir créer l’utilisateur. L’indicateur `send_to_existing_only` ne peut pas être utilisé avec les alias utilisateur.

## Associer des déclencheurs par événement et des filtres d’audience

Une autre condition de concurrence courante peut se produire lorsque vous configurez une campagne ou un Canvas par événement avec le même déclencheur que le filtre d’audience (c’est-à-dire un attribut modifié ou un événement personnalisé effectué). Il se peut que l’utilisateur ne figure pas dans l’audience au moment de l’événement déclencheur, ce qui signifie qu’il ne recevra pas la campagne ou ne pourra pas accéder au Canvas. Dans ce cas, Braze recommande de ne pas configurer le déclencheur pour qu’il corresponde au filtre d’audience.


[1]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[2]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[3]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[4]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
