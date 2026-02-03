Vous pouvez utiliser les propriétés d'entrée et les propriétés d'événement de Canvas dans vos parcours utilisateurs Canvas.

{% tabs local %}
{% tab Canvas Entry Properties %}

Les [propriétés d'entrée de Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) correspondent aux propriétés que vous mappez pour les canvas basés sur des actions ou déclenchés par API. Notez que l’objet `canvas_entry_properties` a une taille maximale limite de 50 KB.

{% alert note %}
Pour les canaux de communication in-app en particulier, `canvas_entry_properties` ne peut être référencé que dans Canvas.
{% endalert %}

Vous pouvez faire référence à `canvas_entry_properties` dans n'importe quelle étape du message en utilisant le format Liquid : ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Notez que les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

#### Cas d’utilisation

{% raw %}
Supposons qu'un magasin de détail, RetailApp, ait la demande suivante : `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. 

RetailApp peut récupérer le nom du produit (chaussures) dans un message avec ce Liquid : `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

RetailApp peut également déclencher l'envoi de messages spécifiques pour différentes propriétés d' `product_name` dans un canvas qui cible les utilisateurs après qu'ils aient déclenché un événement d'achat. Par exemple, ils peuvent envoyer des messages différents aux utilisateurs qui ont acheté des chaussures et à ceux qui ont acheté autre chose en ajoutant le liquide suivant dans une étape Message.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Expand for original Canvas editor %}

Vous ne pouvez plus créer ou dupliquer des toiles à l'aide de l'éditeur original. Cette section n'est disponible qu'à titre de référence. Pour les canvas créés avec l'éditeur original, les propriétés d'entrée du canvas ne peuvent être référencées que dans la première étape complète d'un canvas.

{% enddetails %}
{% endtab %}

{% tab Event Properties %}

Les propriétés d'événement font référence aux propriétés que vous définissez pour les événements personnalisés et les achats. Ces `event_properties` peuvent être utilisés dans des campagnes avec livraison/distribution par événement et Canvases.

{% alert important %}
Vous ne pouvez pas utiliser `event_properties` dans la première étape du message de votre Canvas. Au lieu de cela, vous devez utiliser `canvas_entry_properties` ou ajouter une étape de parcours d'action avec l'événement correspondant **avant** l’étape Message qui inclut `event_properties`.
{% endalert %}

Dans Canvas, les propriétés d'événement personnalisé et d'achat peuvent être utilisées dans Liquid dans toute étape de message qui suit une étape de parcours d'action. Veillez à utiliser {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} si vous faites référence à ces propriétés d'événement. Ces événements doivent être des événements personnalisés ou d’achat pour être utilisés ainsi dans le composant de message.

Dans la première étape du message suivant un parcours d'action, vous pouvez utiliser les propriétés d'événement liées à l'événement référencé dans ce parcours d'action. Toutefois, ces propriétés d'événement ne peuvent être utilisées que si l'utilisateur a réellement effectué l'action (et n'a pas été trié dans le groupe Tous les autres). Vous pouvez disposer d’autres étapes (n’étant pas un autre parcours d’action ou une étape de message) entre ce parcours d’action et l’étape de message.

{% details Expand for original Canvas editor %}

Vous ne pouvez plus créer ou dupliquer des toiles à l'aide de l'éditeur original. Cette section n'est disponible qu'à titre de référence. Pour l'éditeur Canvas original, les propriétés d'événement ne peuvent pas être utilisées dans les étapes complètes de planification. Toutefois, vous pouvez utiliser les propriétés d'événement dans la première étape complète d'un Canvas basé sur des actions, même si l'étape complète est planifiée.

{% enddetails %}

{% endtab %}
{% endtabs %}

Reportez-vous aux [propriétés d'entrée dans le canvas et aux propriétés d'événement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) pour plus d'informations et d'exemples.