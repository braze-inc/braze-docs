---
nav_title: Message 
article_title: Message 
alias: "/message_step/"
page_order: 5
page_type: reference
description: "Cet article de référence explique comment créer un message autonome à l'aide de l'étape Message."
tool: Canvas

---

# Message 

> Les étapes du message vous permettent d'ajouter un message autonome à l'endroit de votre choix dans votre flux Canvas.

![Une étape de message nommée "Lunch promo" utilisant le canal de communication.]({% image_buster /assets/img/canvas_components/message_step1.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

## Création d'un message

Pour créer un composant de message, ajoutez d’abord une étape à votre Canvas. Glissez-déposez le composant depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus au bas d'une étape et sélectionnez **Message.** 

### Étape 1 : Sélectionnez votre canal d'envoi de messages

Vous pouvez choisir parmi les canaux de communication suivants : 
- Cartes de contenu
- E-mail
- LINE
- Notifications push
- SMS/MMS/RCS
- in-app Messages 
- Webhook
- WhatsApp

![Liste des canaux de communication disponibles à sélectionner pour l'étape Message.]({% image_buster /assets/img/canvas_components/message_step2.png %})

### Étape 2 : Modifier les paramètres de livraison

Ensuite, vous pouvez modifier les paramètres de la réception/distribution intelligente, des heures calmes et de la validation de la réception/distribution.

#### Timing intelligent

Vous pouvez activer le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) avec une option de repli lorsque le profil d'un utilisateur ne dispose pas de suffisamment de données pour calculer une heure optimale. Nous vous recommandons d'activer le timing intelligent et la [limite de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) afin de vérifier les éventuels délais entre l'entrée des utilisateurs dans l'étape Message et l'envoi effectif du message.

Sélectionnez **Utiliser le timing intelligent** dans l'onglet **Paramètres de réception/distribution**. À ce niveau, vous pouvez sélectionner l’heure la plus classique ou une heure de base spécifique. Si l’option Heures calmes est activée, l’étape de message vous permet donc d’ignorer ce paramètre.

#### Validation des distributions

Les validations de livraison fournissent un contrôle supplémentaire pour confirmer que votre audience répond aux critères de livraison pour l’envoi de message. Ce paramètre est recommandé si les options Heures calmes, Timing Intelligent ou Limitation du taux sont activées. Vous pouvez ajouter un segment ou des filtres supplémentaires pour valider l’heure d’envoi du message. Si un utilisateur ne correspond pas aux validations de livraison définies pour une étape de message, il sortira du Canvas à cette étape.

![Onglet Paramètres de livraison pour les paramètres de lu composant de message. Les heures calmes sont activées et la case pour l’utilisation de Timing Intelligent est cochée pour envoyer le message à une heure optimale. Les validations de réception/distribution sont activées pour valider l'audience lors de l'envoi du message.]({% image_buster /assets/img/canvas_components/message_step4.png %}){: style="max-width:90%;"}

## L'avancement des utilisateurs

Tous les utilisateurs qui entrent dans l'étape Message passeront à l'étape suivante si l'une des conditions suivantes est remplie :

- Un message est envoyé
- Un message est limité de fréquence et n'est pas envoyé.
- Un message est interrompu
- Un utilisateur n'est pas joignable par le canal, le message n'est donc pas envoyé.

{% raw %}
Si un Canvas basé sur une action est déclenché par un message SMS entrant, vous pouvez référencer les propriétés du SMS dans la première étape (étape Message) ou dans une étape Message imbriquée sous une étape Parcours d'action. Par exemple, à l’étape Message, vous pouvez utiliser `{{sms.${inbound_message_body}}}` ou `{{sms.${inbound_media_urls}}}`.
{% endraw %}

## Référencement des propriétés d'entrée du canvas

Les propriétés d'entrée dans le canevas sont configurées à l'étape de la **planification de l'entrée** lors de la création d'un canevas et indiquent le déclencheur qui permet à un utilisateur d'entrer dans un canevas. Ces propriétés peuvent également accéder aux propriétés des charges utiles d’entrée dans les Canvas déclenchés par API. Notez que l’objet `canvas_entry_properties` a une taille maximale limite de 50 KB. 

Les propriétés d'entrée peuvent être utilisées dans Liquid dans n'importe quelle étape du message. Utilisez le Liquid suivant lorsque vous faites référence à ces propriétés d'entrée : {% raw %}``canvas_entry_properties${property_name}``{% endraw %}. Les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

{% alert note %}
Pour les canaux de communication in-app en particulier, `canvas_entry_properties` ne peut être référencé que dans Canvas.
{% endalert %}

Utilisez le Liquid suivant lorsque vous faites référence à ces propriétés d'entrée : {% raw %}``canvas_entry_properties${property_name}``{% endraw %}. Notez que les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

{% raw %}
Imaginons, par exemple, la requête suivante : `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Vous pouvez ajouter le mot « chaussures » à un message avec le code Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

Vous pouvez également exploiter les [propriétés d'entrées persistantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) dans n'importe quelle étape du message pour guider vos utilisateurs à travers des étapes personnalisées tout au long de votre flux de travail Canvas.

### Propriétés de l’événement

Les propriétés d'événement font référence aux propriétés que vous définissez pour les événements personnalisés et les événements d'achat. Ces propriétés d'événement peuvent être utilisées dans les campagnes avec livraison/distribution par événement ainsi que dans les canevas. 

Dans Canvas, les propriétés d'événement personnalisé et d'achat peuvent être utilisées dans Liquid dans toute étape de message qui suit une étape de [parcours d'action.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)  Par exemple, lorsque vous faites référence à `event_properties`, utilisez l'extrait de code suivant : Liquid : {% raw %}``{{event_properties.${property_name}}}``{% endraw %} 

{% alert important %}
`event_properties` ne peuvent pas être utilisées indépendamment des étapes des parcours d'action.
{% endalert %}

Dans la première étape de message suivant un parcours d’action, vous pouvez utiliser les `event_properties` liées à l’événement référencé dans le parcours d’action. Vous pouvez disposer d’autres étapes (n’étant pas un autre parcours d’action ou une étape de message) entre cette étape de parcours d’action et celle de message. Prenez en compte le fait que vous n’aurez accès aux `event_properties` que si votre étape de message peut être remontée jusqu’à un parcours n’étant pas « Tous les autres » dans l’étape du parcours d’action.

{% alert important %}
Vous ne pouvez pas utiliser les `event_properties` dans la première étape de message. Au lieu de cela, vous devez utiliser `canvas_entry_properties` ou ajouter une étape de parcours d’action avec l’événement correspondant avant l’étape de message qui comprend `event_properties`.
{% endalert %}

{% details Élargir pour l'éditeur original de Canvas %}

Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’éditeur Canvas d’origine. Cette section n'est disponible qu'à titre de référence.

- `event_properties` ne peut pas être utilisé dans des étapes complètes planifiées. Cependant, vous pouvez utiliser les `event_properties` dans la première étape complète d’un Canvas par événement, même si l’étape complète est planifiée.
- `canvas_entry_properties` ne peut être référencée que dans la première étape complète d'un canvas.
- Pour les canaux de messages in-app en particulier, `canvas_entry_properties` peut être référencé dans l'éditeur Canvas original si vous avez activé les propriétés d'entrées persistantes dans le cadre de l'accès anticipé précédent.

{% enddetails %}

## Analyse

Reportez-vous au tableau suivant pour les définitions des indicateurs du composant de message : 

| Indicateur | Description |
| --- | --- |
| _Entrées_ | Le nombre d’accès à l’étape. Si votre Canvas est rééligible et qu’un utilisateur accède deux fois à une étape Message, les deux entrées seront enregistrées. |
| _A poursuivi vers l’étape suivante_ | Le nombre d’entrées pour accéder à l’étape suivante dans le Canvas. |
| _Envois_ | Le nombre total de messages envoyés par l’étape. Si votre canvas est rééligible et qu’un utilisateur accède deux fois à une étape Message, les deux entrées seront enregistrées. |
| _Destinataires uniques_ | Le nombre d’utilisateurs ayant reçu des messages depuis cette étape. |
| _Événement de conversion primaire_ | Le nombre de fois où un événement défini se produit après l’interaction ou la consultation d’un message reçu d’une campagne Braze. Vous définissez cet événement lors de la création de la campagne. |
| _Revenue_ | Le revenu total en dollars de destinataires de campagne dans la fenêtre de conversion principale définie. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


