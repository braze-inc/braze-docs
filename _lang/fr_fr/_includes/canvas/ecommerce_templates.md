{% tabs %}
{% tab Abandoned browse %}

### Parcourir Abandonné

Utilisez le modèle **Abandon de navigation** pour engager les utilisateurs qui ont parcouru des produits mais ne les ont pas ajoutés à leur panier ou n'ont pas passé de commande.

![Un modèle de canvas "Abandoned Browse" appliqué avec des "règles d'entrée" élargies.]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### Configuration

Sur la page Canvas, sélectionnez **Utiliser un modèle de canvas** > **Modèles de Braze**, puis appliquez le modèle de **navigation Abandonné**. 

##### Paramètres par défaut

Les paramètres suivants sont préconfigurés dans votre Canvas :
- Bases 
    - Nom de la toile : **Parcourir Abandonné**
    - Événement de conversion : `ecommerce.order placed`
        - Date limite de conversion : 3 jours 
- Planification d’entrée 
    - Basé sur l'action lorsqu'un utilisateur effectue l'événement `ecommerce.product_viewed` 
    - L'heure de début est l'heure à laquelle vous créez le modèle Canvas.<br><br>!["Options basées sur l'action" pour la toile.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br> 
- Audience cible 
    - Audience entrant 
        - L'e-mail **n'est pas vide**
        - Vous pouvez également modifier les critères de l'audience d'entrée pour répondre aux besoins de votre entreprise
    - Contrôles d'entrée
        - Les utilisateurs sont autorisés à se réinscrire à ce Canvas une fois que la durée totale de ce dernier est terminée
    - Critère de sortie 
        - Effectue les opérations suivantes : `ecommerce.cart_updated`, `ecommerce.checkout_started`, ou `ecommerce.order_placed`<br><br>![Contrôles d'entrée et critères de sortie de la toile.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br> 
- Paramètres d'envoi 
    - Utilisateurs abonnés ou opt-in 
- Pas de retard
    - Délai de 1 heure
- Étape du message 
    - Examinez le modèle d'e-mail et le bloc HTML avec un exemple de modèle liquide pour ajouter des produits à votre message dans le modèle préconstruit. Si vous utilisez votre propre modèle d'e-mail, vous pouvez également faire référence aux [variables Liquid](#message-personalization), comme le montre la section suivante.

#### Personnalisation des produits abandonnés dans les e-mails 

Voici un exemple de la manière dont vous pouvez ajouter un bloc de produit HTML pour votre e-mail de recherche abandonnée. 

{% raw %}
```java
<table style="width:100%">
  <tr>
    <th><img src="{{context.${image_url}}}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{context.${product_name}}}</li>
        <li>Price: ${{context.${price}}}</li>
      </ul>
    </th>
  </tr>
</table>
```
{% endraw %}

##### URL du produit

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

{% endtab %}
{% tab Abandoned cart %}

### Panier abandonné

Utilisez le modèle de **panier abandonné** pour couvrir les ventes potentielles perdues par les clients qui ont ajouté des produits à leur panier mais n'ont pas continué à passer à la caisse ou n'ont pas passé de commande. 

![Un modèle de canvas "panier abandonné" appliqué avec des "règles d'entrée" étendues.]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### Configuration

Sur la page Canvas, sélectionnez **Utiliser un modèle de canvas** > **Modèles de Braze**, puis appliquez le modèle **Panier abandonné**. 

##### Paramètres par défaut

Les paramètres suivants sont préconfigurés dans votre Canvas :
- Bases 
    - Nom de la toile : **Panier abandonné**
    - Événement de conversion : `ecommerce.order_placed`
        - Date limite de conversion : 3 jours 
- Planification d’entrée 
    - Déclencheur basé sur une action lorsqu'un utilisateur déclenche l'**événement Perform Cart Updated** (situé dans la liste déroulante).
    - L'heure de début est l'heure à laquelle vous créez le modèle Canvas.<br><br>!["Options basées sur l'action" pour la toile.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br> 
- Audience cible 
    - Audience entrant 
        - A utilisé ces applications **plus de 0** fois 
        - L'e-mail **n'est pas vide**
    - Contrôles d'entrée
        - Les utilisateurs sont immédiatement rééligibles pour la participation à Canvas.
    - Critère de sortie 
        - Effectue les opérations suivantes : `ecommerce.cart_updated`, `ecommerce.checkout_started`, ou `ecommerce.order_placed`<br><br>![Contrôles d'entrée et critères de sortie de la toile.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br> 
- Paramètres d'envoi 
    - Utilisateurs abonnés ou opt-in 
- Pas de retard
     - Délai de 4 heures
- Étape du message 
    - Examinez le modèle d'e-mail et le bloc HTML avec un exemple de modèle liquide pour ajouter des produits à votre message dans le modèle préconstruit. Si vous utilisez votre propre modèle d'e-mail, vous pouvez également faire référence aux [variables Liquid](#message-personalization), comme le montre la section suivante.

#### Comment fonctionne la logique de réintroduction des paniers abandonnés ?

Lorsqu'un utilisateur entame le processus de paiement, son panier est marqué comme étant `checkout_started`. À partir de ce moment, toute nouvelle mise à jour du panier avec le même ID ne permettra pas à l'utilisateur de revenir dans le parcours de l'utilisateur du panier abandonné.

1. Lorsqu'un utilisateur ajoute un article à son panier, il entre dans le Canvas.
2. Chaque fois qu'ils ajoutent ou modifient des articles, ils réintègrent le canvas, ce qui permet d'actualiser les données de leur panier et l'envoi de leurs messages.
3. Lorsque l'utilisateur entame la procédure de paiement, son panier est étiqueté `checkout_started` et il quitte le canvas.
4. Toute mise à jour ultérieure du panier à l'aide du même ID ne déclenchera pas de nouvelle saisie, car le panier est déjà passé à l'étape du paiement.

Lorsque les utilisateurs passent au parcours d'achat, ils sont ciblés par le [Canvas d'achat abandonné](#abandoned-checkout), qui est conçu pour les utilisateurs plus avancés dans le parcours d'achat.

#### Personnalisation des produits du panier abandonné pour les e-mails {#abandoned-cart-checkout}

Les parcours des utilisateurs de paniers abandonnés nécessitent une étiquette Liquid spéciale `shopping_cart` pour la personnalisation du produit. 

Voici un exemple de la façon dont vous ajouteriez un bloc HTML avec votre étiquette Liquid `shopping_cart` pour ajouter des produits dans votre e-mail. 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

{% alert note %}
Si vous utilisez Shopify, ajoutez le nom de votre catalogue pour obtenir l'URL de l'image variante.
{% endalert %}

##### URL du panier en HTML

Si vous souhaitez renvoyer les utilisateurs à leur panier, vous pouvez ajouter une propriété d'événement imbriqué sous l'objet de métadonnées, comme par exemple :

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Si vous utilisez Shopify, créez l'URL de votre panier en utilisant ce modèle Liquid :

{% raw %}
```liquid
{{context.${source}}}/checkouts/cn/{{context.${cart_id}}} 
```
{% endraw %}

{% endtab %}
{% tab Abandoned checkout %}

### Paiement abandonné

Utilisez le modèle **Abandoned checkout** pour cibler les clients qui ont commencé le processus de paiement mais qui sont partis avant de passer leur commande. 

![Un modèle de canvas "Abandoned Checkout" appliqué avec des "règles d'entrée" étendues.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### Configuration

Sur la page Canvas, sélectionnez **Utiliser un modèle de canevas** > **Modèles de Braze**, puis appliquez le modèle de **caisse abandonnée**. 

##### Paramètres par défaut

Les paramètres suivants sont préconfigurés dans votre Canvas :

- Bases 
    - Nom de la toile : **Paiement abandonné**
    - Événement de conversion : `ecommerce.order_placed`
        - Date limite de conversion : 3 jours 
- Planification d’entrée 
    - Déclencheur basé sur une action lorsqu'un utilisateur effectue l'événement `ecommerce.checkout_started` 
    - L'heure de début est l'heure à laquelle vous créez le modèle Canvas.<br><br>!["Options basées sur l'action" pour la toile.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- Audience cible 
    - Audience entrant 
        - A utilisé ces applications **plus de 0** fois 
        - L'e-mail **n'est pas vide**
    - Contrôles d'entrée
        - Les utilisateurs sont immédiatement rééligibles pour la participation à Canvas.
        - Critère de sortie 
            - Effectue les événements `ecommerce.order_placed` <br><br>![Contrôles d'entrée et critères de sortie de la toile.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- Paramètres d'envoi 
    - Utilisateurs abonnés ou opt-in 
- Pas de retard
    - Délai de 4 heures
- Étape du message 
    - Examinez le modèle d'e-mail et le bloc HTML avec un exemple de modèle liquide pour ajouter des produits à votre message dans le modèle préconstruit. Si vous utilisez votre propre modèle d'e-mail, vous pouvez également faire référence aux [variables Liquid](#message-personalization), comme le montre la section suivante.

#### Personnalisation des e-mails en cas d'abandon d'achat

Les parcours des utilisateurs ayant abandonné leur commande nécessitent une étiquette Liquid `shopping_cart` spéciale pour la personnalisation du produit. 

Voici un exemple de la façon dont vous ajouteriez un bloc HTML avec votre étiquette Liquid `shopping_cart` pour ajouter des produits dans votre e-mail. 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
    {% endfor %}
</table>
```
{% endraw %}

##### URL de la caisse

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### Confirmation de la commande et enquête de satisfaction

Utilisez le modèle d'**enquête de confirmation de commande & ** pour confirmer les commandes réussies et améliorer la satisfaction des clients.

![Un modèle de canvas de "confirmation de commande" appliqué avec des "règles d'entrée" étendues.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### Configuration

Sur la page Canvas, sélectionnez **Utiliser un modèle Canvas** > **Modèles de Braze**, puis appliquez le modèle d'**enquête de confirmation de commande & feedback.**  

##### Paramètres par défaut

Les paramètres suivants sont préconfigurés dans votre Canvas :

- Bases 
    - Nom de la toile : **Confirmation de commande avec enquête de satisfaction**
    - Événement de conversion : `ecommerce.session_start`
        - Date limite de conversion : 10 jours 
- Planification d’entrée 
    - Déclencheur basé sur une action lorsqu'un utilisateur effectue l'événement `ecommerce.cart_updated` 
    - L'heure de début est l'heure à laquelle vous créez le modèle Canvas.<br><br>!["Options basées sur l'action" pour la toile.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- Audience cible 
    - Audience entrant 
        - A utilisé ces applications **plus de 0** fois 
        - L'e-mail **n'est pas vide**
    - Contrôles d'entrée
        - Les utilisateurs sont immédiatement rééligibles pour la participation à Canvas.
    - Critère de sortie 
        - Sans objet<br><br>![Filtres et contrôles d'entrée supplémentaires pour le Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- Paramètres d'envoi 
    - Utilisateurs abonnés ou opt-in 
- Étape du message 
    - Examinez le modèle d'e-mail et le bloc HTML avec un exemple de modèle liquide pour ajouter des produits à votre message dans le modèle préconstruit. Si vous utilisez votre propre modèle d'e-mail, vous pouvez également faire référence aux [variables Liquid](#message-personalization), comme le montre la section suivante.

#### Personnalisation des e-mails de confirmation de commande

Voici un exemple de la manière dont vous pouvez ajouter un bloc HTML de produit à votre confirmation de commande après qu'une commande a été passée.

{% raw %}
```json
<table style="width:100%">
  {% for item in {{context.${products}}} %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200" /></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{item.product_name}}</li>
        <li>Price: {{item.price}}</li>
        <li>Quantity: {{item.quantity}}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

##### URL du statut de la commande

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}