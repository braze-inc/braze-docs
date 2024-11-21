---
nav_title: Conditions de concurrence
article_title: Conditions de concurrence
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Cet article aborde les meilleures pratiques à suivre pour éviter les conditions de concurrence qui affectent vos campagnes de communication."

---

# Conditions de concurrence

> Une condition de concurrence est un concept à travers lequel un résultat dépend de la séquence ou du timing d’autres événements. 

Par exemple, si la séquence d’événements souhaitée est « événement A », puis « événement B », mais que « événement B » arrive parfois en premier, cette situation est connue sous le nom de condition de concurrence.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

## Cibler de nouveaux utilisateurs

Dans Braze, l’une des conditions de concurrence les plus courantes se produit avec des messages qui ciblent de nouveaux utilisateurs. Dans ce cas, l’ordre attendu des événements est le suivant :

1. Un utilisateur est créé ;
2. Le même utilisateur est immédiatement ciblé par un message, effectue un événement personnalisé ou enregistre un attribut personnalisé.

Cependant, dans certains cas, le deuxième événement se déclenchera d’abord. Cela signifie qu’un message tente d’être envoyé à un utilisateur qui n’a pas encore été créé, et par conséquent, l’utilisateur ne recevra jamais le message en question. Il en va de même pour les événements ou les attributs, lorsque l'événement ou l'attribut tente d'être enregistré dans un profil utilisateur qui n'existe pas encore.

## Utiliser plusieurs endpoints API

Il existe quelques scénarios dans lesquels plusieurs endpoints d'API peuvent également entraîner cette condition de concurrence, par exemple :

- Utiliser des endpoints API distincts pour créer des utilisateurs et déclencher des Canvases ou des campagnes.
- Effectuer plusieurs appels distincts à l'endpoint `/users/track` pour mettre à jour des attributs personnalisés, des événements ou des achats.

Lorsque des informations utilisateur sont envoyées à Braze via l’endpoint `/users/track`, le traitement de ces informations peut parfois prendre quelques secondes. Par conséquent, lorsque des demandes sont adressées simultanément aux endpoints `/users/track` et [Messaging][4], rien ne garantit actuellement que les informations relatives à l'utilisateur seront mises à jour avant l'envoi d'un message.

Pour les deux scénarios précédents, si ces demandes sont effectuées dans la même requête API, il n'y aura pas de problème.

{% alert note %}
Si les attributs de l'utilisateur et les événements sont envoyés dans la même demande (à partir de `/users/track` ou du SDK), Braze traitera les attributs avant les événements ou la tentative d'envoi d'un message.
{% endalert %}

Notez que si vous envoyez une requête API pour un message planifié, ces requêtes doivent être séparées et un utilisateur doit être créé avant d’envoyer la requête API programmée.

### Éviter la condition de concurrence

Un moyen d'éviter cette condition de concurrence consiste à ajouter un délai - d'environ une minute - entre la création d'un utilisateur et le ciblage de cet utilisateur par votre Canvas ou votre campagne, ou la tentative d'enregistrement d'un attribut ou d'un événement dans le profil de cet utilisateur.

De même, vous pouvez utiliser l'objet [`Attributes`][1] pour ajouter, créer ou mettre à jour un utilisateur, puis le cibler à l'aide de l’[endpoint `/canvas/trigger/send`][2] ou de l’[endpoint `/campaign/trigger/send`.][3] Cette requête API traitera l’objet `attributes` avant de cibler les utilisateurs.

Les attributs inclus dans cet objet seront traités avant que Braze ne commence à envoyer la campagne. Si l'indicateur `send_to_existing_only` est défini sur false et qu'un `external_user_id` n'existe pas dans la base de données de Braze, nous créerons un profil utilisateur pour le `external_user_id` et traiterons les attributs associés au profil utilisateur avant que Braze ne commence à envoyer la campagne. Notez également que si l’indicateur `send_to_existing_only` est défini sur faux, l’objet Attributs doit être inclus pour pouvoir créer l’utilisateur. L’indicateur `send_to_existing_only` ne peut pas être utilisé avec les alias utilisateur.

## Associer des déclencheurs par événement et des filtres d’audience

Une autre condition de concurrence courante peut se produire si vous configurez une campagne basée sur une action ou un Canvas avec le même déclencheur que le filtre d'audience (tel qu'un attribut modifié ou l'exécution d'un événement personnalisé). Il se peut que l’utilisateur ne figure pas dans l’audience au moment de l’événement déclencheur, ce qui signifie qu’il ne recevra pas la campagne ou ne pourra pas accéder au Canvas. Dans ce cas, Braze recommande de ne pas configurer le déclencheur pour qu’il corresponde au filtre d’audience. 

### Éviter la condition de concurrence

Une façon d'éviter cette condition de concurrence peut être d'ajouter un délai de plus d'une minute pour laisser aux utilisateurs suffisamment de temps pour entrer dans le Canvas.

[1]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[2]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[3]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[4]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
