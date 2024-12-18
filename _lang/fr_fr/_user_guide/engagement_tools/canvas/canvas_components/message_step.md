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

![][1]{: style="float:right;max-width:25%;margin-left:15px;"}

## Créer un message

Pour créer un composant de message, ajoutez d’abord une étape à votre Canvas. Glissez-déposez le composant depuis la barre latérale ou cliquez sur le bouton plus <i class="fas fa-plus-circle"></i> au bas d'une étape et sélectionnez **Message.** 

### Définir des messages

Tous les utilisateurs qui entrent dans l'étape Message passeront à l'étape suivante si l'une des conditions suivantes est remplie :
- Un message est envoyé
- Un message est limité de fréquence et n'est pas envoyé.
- Un message est interrompu
- Un utilisateur n'est pas joignable par le canal, le message n'est donc pas envoyé.

![Configurer les paramètres de messages pour une étape de message qui comprend la possibilité de sélectionner votre canal de communication et de personnaliser les paramètres de réception/distribution.][2]{: style="max-width:75%;"}

{% raw %}
Si un Canvas basé sur une action est déclenché par un message SMS entrant, vous pouvez référencer les propriétés du SMS dans la première étape (étape Message) ou dans une étape Message imbriquée sous une étape Parcours d'action. Par exemple, à l’étape Message, vous pouvez utiliser `{{sms.${inbound_message_body}}}` ou `{{sms.${inbound_media_urls}}}`.
{% endraw %}

### Modifier les paramètres de livraison

Le composant de message comprend également des paramètres pour la livraison intelligente, les remplacements d’heures calmes et la validation de livraison. Vous pouvez activer le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) avec une option de repli lorsque le profil d'un utilisateur ne dispose pas de suffisamment de données pour calculer une heure optimale. Nous vous recommandons d'activer le timing intelligent et la [limite de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) afin de vérifier les éventuels délais entre l'entrée des utilisateurs dans l'étape Message et l'envoi effectif du message.

Sélectionnez **Utiliser le timing intelligent** dans l'onglet **Paramètres de réception/distribution**. À ce niveau, vous pouvez sélectionner l’heure la plus classique ou une heure de base spécifique. Si l’option Heures calmes est activée, l’étape de message vous permet donc d’ignorer ce paramètre.

Les validations de livraison fournissent un contrôle supplémentaire pour confirmer que votre audience répond aux critères de livraison pour l’envoi de message. Ce paramètre est recommandé si les options Heures calmes, Timing Intelligent ou Limitation du taux sont activées. Vous pouvez ajouter un segment ou des filtres supplémentaires pour valider l’heure d’envoi du message. Si un utilisateur ne correspond pas aux validations de livraison définies pour une étape de message, il sortira du Canvas à cette étape.

![Onglet Paramètres de livraison pour les paramètres de lu composant de message. Les heures calmes sont activées et la case pour l’utilisation de Timing Intelligent est cochée pour envoyer le message à une heure optimale. Les validations de distribution sont activées pour confirmer l’audience lors de l’envoi du message.][4]{: style="max-width:80%;"}

### Propriétés d’entrées de Canvas

Les propriétés d’entrée dans le Canvas sont configurées dans l’étape de planification d’entrée de la création du Canvas et indiqueront le déclencheur qui fait entrer l’utilisateur dans le Canvas. Ces propriétés peuvent également accéder aux propriétés des charges utiles d’entrée dans les Canvas déclenchés par API. Notez que l’objet `canvas_entry_properties` a une taille maximale limite de 50 KB. 

{% alert note %}
Expressément pour les Canaux de communication in-app, `canvas_entry_properties` ne peut être référencé dans Canvas Flow et dans l’éditeur Canvas d’origine que si vous avez activé les propriétés d’entrées persistantes dans l’éditeur d’origine durant l’accès anticipé précédent.
{% endalert %}

#### Canvas Flow

Pour les envois de messages Canvas Flow, les propriétés d’entrée peuvent être utilisées en Liquid dans n’importe laquelle des étapes de message. Utilisez le code Liquid suivant lorsque vous faites référence à ces propriétés d'entrée : {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %}. Les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

Utilisez le code Liquid suivant lorsque vous faites référence à ces propriétés d'entrée : {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %}. Notez que les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

{% raw %}
Imaginons, par exemple, la requête suivante : `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Vous pouvez ajouter le mot « chaussures » à un message avec le code Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

Vous pouvez également exploiter les [propriétés d'entrées persistantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) dans n'importe quelle étape du message pour guider vos utilisateurs à travers des étapes personnalisées tout au long de votre flux de travail Canvas.

#### Flux de travail d’origine

Pour les Canvas créés à partir de l’éditeur d’origine, `canvas_entry_properties` ne peut être référencé que dans la première étape complète d’un Canvas.

### Propriétés de l’événement

Les propriétés de l’événement sont les propriétés que vous avez définies pour des événements personnalisés et des achats. Ces `event_properties` peuvent être utilisées dans les campagnes ayant une livraison par événement ainsi que dans les Canvas. 

#### Canvas Flow

Dans Canvas Flow, les propriétés des événements personnalisés et des événements d’achat peuvent être utilisées en Liquid dans n’importe quelle étape de message qui suit une étape de [parcours d’action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/). Pour Canvas Flow, utilisez le Liquid `` {% raw %} {{event_properties.${property_name}}} {% endraw %}`` lorsque vous référencez ces `event_properties`. Ces événements doivent être des événements personnalisés ou d’achat pour être utilisés ainsi dans le composant de message.

{% alert important %}
Les `event_properties` ne peuvent pas être utilisées indépendamment des parcours d’action pour Canvas Flow.
{% endalert %}

Dans la première étape de message suivant un parcours d’action, vous pouvez utiliser les `event_properties` liées à l’événement référencé dans le parcours d’action. Vous pouvez disposer d’autres étapes (n’étant pas un autre parcours d’action ou une étape de message) entre cette étape de parcours d’action et celle de message. Prenez en compte le fait que vous n’aurez accès aux `event_properties` que si votre étape de message peut être remontée jusqu’à un parcours n’étant pas « Tous les autres » dans l’étape du parcours d’action.

#### Flux de travail d’origine

Les `event_properties` peuvent être utilisées dans la première étape complète d’un Canvas par événement en utilisant le flux de travail d’origine, même si l’étape complète est planifiée. 

{% alert important %}
Pour l’éditeur d’origine et Canvas Flow, vous ne pouvez pas utiliser `event_properties` dans la première étape de message. Au lieu de cela, vous devez utiliser `canvas_entry_properties` ou ajouter une étape de parcours d’action avec l’événement correspondant avant l’étape de message qui comprend `event_properties`.
{% endalert %}

Pour obtenir plus d’informations ainsi que des exemples, consultez notre section [Propriété d’entrées et d’événement Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/).


## Analyse

Reportez-vous au tableau suivant pour les définitions des indicateurs du composant de message : 

| Indicateur | Description |
| --- | --- |
| Entrées | Le nombre d’accès à l’étape. Si votre Canvas est rééligible et qu’un utilisateur accède deux fois à une étape Message, les deux entrées seront enregistrées. |
| A poursuivi vers l’étape suivante | Le nombre d’entrées pour accéder à l’étape suivante dans le Canvas. |
| Envois | Le nombre total de messages envoyés par l’étape. Si votre canvas est rééligible et qu’un utilisateur accède deux fois à une étape Message, les deux entrées seront enregistrées. |
| Destinataires uniques | Le nombre d’utilisateurs ayant reçu des messages depuis cette étape. |
| Événement de conversion primaire | Le nombre de fois où un événement défini se produit après l’interaction ou la consultation d’un message reçu d’une campagne Braze. Vous définissez cet événement lors de la création de la campagne. |
| Revenue | Le revenu total en dollars de destinataires de campagne dans la fenêtre de conversion principale définie. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][3]{: style="max-width:20%;"}


[1]: {% image_buster /assets/img/canvas_components/message_step1.png %}
[2]: {% image_buster /assets/img/canvas_components/message_step2.png %}
[3]: {% image_buster /assets/img/canvas_components/message_step3.png %}
[4]: {% image_buster /assets/img/canvas_components/message_step4.png %}
