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

> Les étapes du message vous permettent d'ajouter un message autonome à l'endroit de votre choix dans votre Canvas.

!Une étape de message nommée "Lunch promo" utilisant le canal de communication.]({% image_buster /assets/img/canvas_components/message_step1.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

## Création d'un message

Pour créer un composant Message, ajoutez d'abord une étape à votre Canvas. Glissez-déposez le composant à partir de la barre latérale ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus au bas d'une étape et sélectionnez **Message.** 

### Étape 1 : Sélectionnez votre canal d'envoi de messages

Vous pouvez choisir parmi les canaux de communication suivants : 
- Cartes de contenu
- e-mail
- LIGNE
- Notifications push
- SMS/MMS/RCS
- Messages in-app 
- webhook
- WhatsApp

\![Liste des canaux de communication disponibles à sélectionner pour l'étape Message.]({% image_buster /assets/img/canvas_components/message_step2.png %})

### Étape 2 : Modifier les paramètres de réception/distribution

Ensuite, vous pouvez modifier les paramètres de la réception/distribution intelligente, des heures calmes et de la validation de la réception/distribution.

#### Le timing intelligent

Vous pouvez activer le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) avec une option de repli lorsque le profil d'un utilisateur ne dispose pas de suffisamment de données pour calculer une heure optimale. Nous vous recommandons d'activer le timing intelligent et la [limite de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) afin de vérifier les éventuels délais entre l'entrée des utilisateurs dans l'étape Message et l'envoi effectif du message.

Sélectionnez **Utiliser le timing intelligent** dans l'onglet **Paramètres de réception/distribution**. Ici, vous pouvez sélectionner soit l'heure la plus populaire, soit une heure de repli spécifique. Si les heures calmes sont activées, l'étape Message vous permet également de remplacer ce paramètre.

#### Validations de réception/distribution

Les validations de réception/distribution permettent de vérifier une nouvelle fois que votre audience répond aux critères de livraison lors de l'envoi du message. Ce réglage est recommandé si les heures calmes, le timing intelligent ou la limite de débit sont activés. Vous pouvez ajouter un segment ou des filtres supplémentaires pour valider au moment de l'envoi du message. Si un utilisateur ne remplit pas les conditions de réception/distribution pour une étape du message, il quittera le canevas à cette étape.

!L'onglet Paramètres de réception/distribution pour les paramètres du composant Message. Les heures calmes sont activées et la case Utiliser le timing intelligent est cochée afin d'envoyer le message à un moment optimal. Les validations de réception/distribution sont activées pour valider l'audience lors de l'envoi du message.]({% image_buster /assets/img/canvas_components/message_step4.png %}){: style="max-width:90%;"}

## L'avancement des utilisateurs

Tous les utilisateurs qui entrent dans l'étape Message passeront à l'étape suivante si l'une des conditions suivantes est remplie :

- Tout message est envoyé
- Un message est limité de fréquence et n'est pas envoyé.
- Un message est interrompu
- Un utilisateur n'est pas joignable par le canal, le message n'est donc pas envoyé.

{% raw %}
Si un Canvas basé sur une action est déclenché par un message SMS entrant, vous pouvez référencer les propriétés du SMS dans la première étape (étape Message) ou dans une étape Message imbriquée sous une étape Parcours d'action. Par exemple, à l'étape du message, vous pouvez utiliser `{{sms.${inbound_message_body}}}` ou `{{sms.${inbound_media_urls}}}`.
{% endraw %}

## Référencement des propriétés d'entrée du canvas

Les propriétés d'entrée dans le canevas sont configurées à l'étape de la **planification de l'entrée** lors de la création d'un canevas et indiquent le déclencheur qui permet à un utilisateur d'entrer dans un canevas. Ces propriétés peuvent également accéder aux propriétés des charges utiles d'entrée dans les canevas déclenchés par l'API. Notez que la taille maximale de l'objet `canvas_entry_properties` est de 50 KB. 

Les propriétés d'entrée peuvent être utilisées dans Liquid dans n'importe quelle étape du message. Utilisez le Liquid suivant lorsque vous faites référence à ces propriétés d'entrée : {% raw %}``canvas_entry_properties${property_name}``{% endraw %}. Les événements doivent être des événements personnalisés ou des événements d'achat pour pouvoir être utilisés de cette manière.

{% alert note %}
Pour les canaux de communication in-app en particulier, `canvas_entry_properties` ne peut être référencé que dans Canvas.
{% endalert %}

Utilisez le Liquid suivant lorsque vous faites référence à ces propriétés d'entrée : {% raw %}``canvas_entry_properties${property_name}``{% endraw %}. Notez que les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

{% raw %}
Par exemple, considérez la demande suivante : `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Vous pouvez ajouter le mot "chaussures" à un message avec le liquide `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

Vous pouvez également exploiter les [propriétés d'entrées persistantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) dans n'importe quelle étape du message pour guider vos utilisateurs à travers des étapes personnalisées tout au long de votre flux de travail Canvas.

### Propriétés d'événement

Les propriétés d'événement font référence aux propriétés que vous définissez pour les événements personnalisés et les événements d'achat. Ces propriétés d'événement peuvent être utilisées dans les campagnes avec livraison/distribution par événement ainsi que dans les canevas. 

Dans Canvas, les propriétés d'événement personnalisé et d'achat peuvent être utilisées dans Liquid dans toute étape de message qui suit une étape de [parcours d'action.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)  Par exemple, lorsque vous faites référence à `event_properties`, utilisez l'extrait de code suivant : Liquid : {% raw %}``{{event_properties.${property_name}}}``{% endraw %} 

{% alert important %}
`event_properties` ne peuvent pas être utilisées indépendamment des étapes des parcours d'action.
{% endalert %}

Dans la première étape du message suivant un parcours d'action, vous pouvez utiliser `event_properties` en rapport avec l'événement référencé dans ce parcours d'action. Vous pouvez avoir d'autres étapes (qui ne sont pas d'autres parcours d'action ou d'autres envois de messages) entre cette étape de parcours d'action et l'étape d'envoi de messages. Notez que vous n'aurez accès à `event_properties` que si votre étape Message peut être retracée jusqu'à un chemin autre que Tout le monde ailleurs dans une étape Chemin d'action.

{% alert important %}
Vous ne pouvez pas utiliser `event_properties` à l'étape du message principal. Au lieu de cela, vous devez utiliser `canvas_entry_properties` ou ajouter une étape de parcours d'action avec l'événement correspondant avant l'étape de message qui inclut `event_properties`.
{% endalert %}

{% details Expand for original Canvas editor %}

Vous ne pouvez plus créer ou dupliquer des toiles à l'aide de l'éditeur original. Cette section n'est disponible qu'à titre de référence.

- `event_properties` ne peut pas être utilisé dans des étapes complètes planifiées. Toutefois, vous pouvez utiliser `event_properties` dans la première étape complète d'un canvas basé sur l'action, même si l'étape complète est planifiée.
- `canvas_entry_properties` ne peut être référencée que dans la première étape complète d'un canvas.
- Pour les canaux de messages in-app en particulier, `canvas_entry_properties` peut être référencé dans l'éditeur Canvas original si vous avez activé les propriétés d'entrées persistantes dans le cadre de l'accès anticipé précédent.

{% enddetails %}

## Analyse/analytique (si utilisé comme adjectif)

Reportez-vous au tableau suivant pour connaître les définitions des indicateurs des composantes du message : 

| Indicateurs | Description |
| --- | --- |
| _Entrées_ | Le nombre de fois que l'étape a été saisie. Si votre Canvas est rééligible et qu'un utilisateur entre deux fois dans une étape du message, deux entrées seront enregistrées. |
| _Passage à l'étape suivante_ | Le nombre d'entrées qui sont passées à l'étape suivante du canvas. |
| _Envoie_ | Nombre total de messages envoyés par l'étape. Si votre Canvas est rééligible et qu'un utilisateur entre deux fois dans une étape du message, deux entrées seront enregistrées. |
| _Destinataires uniques_ | Le nombre d'utilisateurs qui ont reçu des messages de cette étape. |
| _Événement de conversion principal_ | Le nombre de fois qu'un événement défini s'est produit après avoir interagi avec ou visualisé un message reçu d'une campagne Braze. Vous définissez cet événement lorsque vous créez la campagne. |
| _Chiffre d'affaires_ | Le chiffre d'affaires total en dollars des destinataires de la campagne dans la fenêtre de conversion primaire définie. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


