---
nav_title: Message 
article_title: Message 
alias: "/message_step/"
page_order: 5
page_type: reference
description: "Cet article de référence aborde la façon de créer un message indépendant à l’aide de l’étape de communication de Canvas."
tool: Canvas

---

# Message 

Les étapes Message vous permettent d’ajouter un message indépendant où vous voulez dans votre flux Canvas.

![][1]{: style="float:right;max-width:25%;margin-left:15px;"}

## Créer un composant de message

Pour créer un composant de message, ajoutez d’abord une étape à votre Canvas. Glissez-déplacez le composant depuis la barre latérale ou cliquez le bouton plus <i class="fas fa-plus-circle"></i> en bas d’une étape et sélectionnez **Message**. 

### Définir des messages

Avec un composant de message, tous les utilisateurs ayant franchi l’étape progressent vers l’étape suivante lorsque l’une des conditions suivantes est remplie :
- Un message est envoyé
- Un message n’est pas envoyé, car l’utilisateur n’est pas joignable par un canal
- Un message n’est pas envoyé, car il est en limite de fréquence
- Un message n’est pas envoyé, car il est annulé

![Configurez des paramètres de messages pour un composant de message Canvas, incluant l’option permettant de sélectionner votre canal de communication et de personnaliser des paramètres de livraison.][2]{: style="max-width:75%;"}

{% raw %}
Si un Canvas par événement est déclenché par un SMS entrant, vous pouvez référencer les propriétés du SMS dans la première étape de message du Canvas. Par exemple, à l’étape Message, vous pouvez utiliser `{{sms.${inbound_message_body}}}` ou `{{sms.${inbound_media_urls}}}`.
{% endraw %}

### Modifier les paramètres de livraison

Le composant de message comprend également des paramètres pour la livraison intelligente, les remplacements d’heures calmes et la validation de livraison. Vous pouvez activer le [Timing Intelligent]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) avec une option de secours lorsqu’un profil utilisateur n’a pas suffisamment de données pour calculer une heure optimale. Nous conseillons d’activer le Timing Intelligent et les [Limites de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) comme contrôle supplémentaire de tout délai entre le moment où les utilisateurs accèdent à l’étape Message et l’envoi réel du message.

Sélectionnez **Using Intelligent Timing (Utilisation de Timing Intelligent)** dans l’onglet **Delivery Settings (Paramètres de livraison)**. À ce niveau, vous pouvez sélectionner l’heure la plus classique ou une heure de base spécifique. Si l’option Heures calmes est activée, l’étape de message vous permet donc d’ignorer ce paramètre.

Les validations de livraison fournissent un contrôle supplémentaire pour confirmer que votre audience répond aux critères de livraison pour l’envoi de message. Ce paramètre est recommandé si les options Heures calmes, Timing Intelligent ou Limitation du taux sont activées. Vous pouvez ajouter un segment ou des filtres supplémentaires pour valider l’heure d’envoi du message. Si un utilisateur ne correspond pas aux validations de livraison définies pour une étape de message, il sortira du Canvas à cette étape.

![Onglet Paramètres de livraison pour les paramètres de lu composant de message. Les heures calmes sont activées et la case pour l’utilisation de Timing Intelligent est cochée pour envoyer le message à une heure optimale. Les validations de livraison sont activées pour valider l’audience lors de l’envoi du message.][4]{: style="max-width:80%;"}

### Propriétés d’entrées de Canvas

Les propriétés d’entrée dans le Canvas sont configurées dans l’étape de planification d’entrée de la création du Canvas et indiqueront le déclencheur qui fait entrer l’utilisateur dans le Canvas. Ces propriétés peuvent également accéder aux propriétés des charges utiles d’entrée dans les Canvas déclenchés par API. Notez que l’objet `canvas_entry_properties` a une taille maximale limite de 50 KB. 

{% alert note %}
Expressément pour les Canaux de communication in-app, `canvas_entry_properties` ne peut être référencé dans Canvas Flow et dans l’éditeur Canvas d’origine que si vous avez activé les propriétés d’entrées persistantes dans l’éditeur d’origine durant l’accès anticipé précédent.
{% endalert %}

#### Flux de travail d’origine

Pour les Canvas construits à partir de l’éditeur d’origine, `canvas_entry_properties` ne peut être référencé que dans la première étape complète d’un Canvas.

#### Canvas Flow

Pour les envois de messages Canvas Flow, les propriétés d’entrée peuvent être utilisées en Liquid dans n’importe laquelle des étapes de message. Utilisez le Liquid suivant lorsque vous référencez ces propriétés d’entrée : {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %}. Les événements doivent être des événements personnalisés ou d’achat pour être utilisés ainsi.

Utilisez le Liquid suivant lorsque vous référencez ces propriétés d’entrée : {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %}. Prenez note du fait que les événements doivent être des événements personnalisés ou d’achat pour être utilisés ainsi.

{% raw %}
Vous pouvez, par exemple, considérer la demande suivante : `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Vous pouvez ajouter le mot « chaussures » à un message avec le Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

Vous pouvez également tirer parti des [propriétés d’entrée persistantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) dans chaque étape de message pour guider vos utilisateurs à travers des étapes personnalisées dans tout votre flux de travail Canvas.

### Propriétés de l’événement

Les propriétés de l’événement sont les propriétés que vous avez définies pour des événements personnalisés et des achats. Ces `event_properties` peuvent être utilisées dans les campagnes ayant une livraison par événement ainsi que dans les Canvas. 

#### Flux de travail d’origine

Les `event_properties` peuvent être utilisées dans la première étape complète d’un Canvas par événement en utilisant le flux de travail d’origine, même si l’étape complète est planifiée. 

#### Canvas Flow

Dans Canvas Flow, les événements personnalisés et les propriétés de l’événement d’achat peuvent être utilisées en Liquid dans n’importe quelle étape de message suivant une étape de [parcours d’action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/). Pour le Canvas Flow, utilisez ce Liquid `` {% raw %} {{event_properties.${property_name}}} {% endraw %}`` lorsque vous référencez ces `event_properties`. Ces événements doivent être des événements personnalisés ou d’achat pour être utilisés ainsi dans le composant de message.

{% alert important %}
Les `event_properties` ne peuvent pas être utilisées indépendamment des parcours d’action pour Canvas Flow.
{% endalert %}

Dans la première étape de message suivant un parcours d’action, vous pouvez utiliser les `event_properties` liées à l’événement référencé dans le parcours d’action. Vous pouvez disposer d’autres étapes (n’étant pas un autre parcours d’action ou une étape de message) entre cette étape de parcours d’action et celle de message. Prenez en compte le fait que vous n’aurez accès aux `event_properties` que si votre étape de message peut être remontée jusqu’à un parcours n’étant pas « Tous les autres » dans l’étape du parcours d’action.

{% alert important %}
Pour l’éditeur Canvas d’origine et Canvas Flow, vous ne pouvez pas utiliser `event_properties` au cours de l’étape du premier message. Au lieu de cela, vous devez utiliser `canvas_entry_properties` ou ajouter une étape de parcours d’action avec l’événement correspondant avant l’étape de message qui comprend `event_properties`.
{% endalert %}

Pour obtenir plus d’informations ainsi que des exemples, consultez notre section [Propriété d’entrées et d’événement Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/).

## Analytique

Reportez-vous au tableau suivant pour les définitions des indicateurs du composant de message : 

| Indicateur | Description |
| --- | --- |
| Entrées | Le nombre d’entrées dans le composant. Si votre Canvas est rééligible et qu’un utilisateur accède deux fois à un composant de message, les deux entrées seront enregistrées. |
| Poursuivre vers l’étape suivante | Le nombre d’entrées pour accéder à l’étape suivante dans le Canvas. |
| Envois | Le nombre total de messages envoyés par le composant. Si votre Canvas est rééligible et qu’un utilisateur accède deux fois à un composant de message, les deux entrées seront enregistrées. |
| Destinataires uniques | Le nombre d’utilisateurs ayant reçu des messages depuis ce composant. |
| Événement de conversion primaire | Le nombre de fois où un événement défini se produit après l’interaction ou la consultation d’un message reçu d’une campagne Braze. Vous définissez cet événement lors de la création de la campagne. |
| Revenue | Le revenu total en dollars de destinataires de campagne dans la fenêtre de conversion principale définie. |
{: .reset-td-br-1 .reset-td-br-2}

![][3]{: style="max-width:20%;"}


[1]: {% image_buster /assets/img/canvas_components/message_step1.png %}
[2]: {% image_buster /assets/img/canvas_components/message_step2.png %}
[3]: {% image_buster /assets/img/canvas_components/message_step3.png %}
[4]: {% image_buster /assets/img/canvas_components/message_step4.png %}
