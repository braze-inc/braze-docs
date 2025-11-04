---
nav_title: "Cas d'utilisation du commerce électronique"
article_title: "Cas d'utilisation du commerce électronique"
alias: /ecommerce_use_cases/
page_order: 4
description: "Cet article de référence traite de plusieurs modèles de Braze préconstruits et adaptés spécifiquement aux marketeurs du commerce électronique, facilitant ainsi la mise en œuvre de stratégies essentielles."
toc_headers: h2
---

# Cas d'utilisation du commerce électronique

> Braze Canvas propose plusieurs modèles préconstruits spécialement conçus pour les marketeurs de l'e-commerce, ce qui facilite la mise en œuvre de stratégies essentielles. Cette page propose quelques modèles clés que vous pouvez utiliser pour améliorer vos parcours clients.

{% alert important %}
Les [événements recommandés pour le commerce électronique]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) sont actuellement en accès anticipé. Contactez votre gestionnaire satisfaction client Braze si vous souhaitez participer à cet accès anticipé. <br><br>Si vous utilisez le nouveau connecteur Shopify, les événements recommandés pour le commerce électronique seront automatiquement disponibles via l'intégration.
{% endalert %}

## Utilisation d'un modèle Canvas

Pour utiliser un modèle Canvas :
1. Allez dans **Messagerie** > **Canvas**.
2. Sélectionnez **Créer un canvas** > **Utiliser un modèle de canvas**.
3. Recherchez dans l'onglet **Modèles de Braze** le modèle que vous souhaitez utiliser. Vous pouvez prévisualiser un modèle en sélectionnant son nom.
4. Sélectionnez **Appliquer** le modèle pour le modèle que vous souhaitez utiliser.<br><br>La page "Canvas templates" s'ouvre sur l'onglet "Braze templates" et affiche une liste des modèles récemment utilisés et des modèles de Braze sélectionnables.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## Modèles eCommerce

- [Parcourir Abandonné](#abandoned-browse)
- [Abandon de panier](#abandoned-cart)
- [Caisse abandonnée](#abandoned-checkout)
- [Confirmation de la commande et enquête de satisfaction](#order-confirmation--feedback-survey)

## Parcourir Abandonné

Utilisez le modèle **Abandon** de **navigation** pour engager les utilisateurs qui ont parcouru des produits mais ne les ont pas ajoutés à leur panier ou n'ont pas passé de commande.

Un modèle de canvas "Abandoned Browse" appliqué avec des "règles d'entrée" étendues.]({% image_buster /assets/img_archive/abandoned_browse.png %})

### Configuration

Sur la page Canvas, sélectionnez **Utiliser un modèle de canvas** > **Modèles de Braze**, puis appliquez le modèle de **navigation Abandonné**. 

#### Paramètres par défaut

Les paramètres suivants sont préconfigurés dans votre Canvas :
- Principes de base 
    - Nom de la toile : **Parcourir Abandonné**
    - Événement de conversion : `ecommerce.order placed`
        - Date limite de conversion : 3 jours 
- Planification de l'entrée 
    - Basé sur l'action lorsqu'un utilisateur effectue l'événement `ecommerce.product_viewed` 
    - L'heure de début est l'heure à laquelle vous créez le modèle Canvas.<br><br>\!["Options basées sur l'action" pour le Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br> 
- L'audience ciblée 
    - Audience d'entrée 
        - L'e-mail **n'est pas vide**
        - Vous pouvez également modifier les critères de l'audience d'entrée pour répondre aux besoins de votre entreprise
    - Contrôles d'entrée
        - Les utilisateurs sont autorisés à se réinscrire à ce Canvas une fois que la durée totale de celui-ci est terminée
    - Critères de sortie 
        - Effectue les opérations suivantes : `ecommerce.cart_updated`, `ecommerce.checkout_started`, ou `ecommerce.order_placed`<br><br>Contrôles d'entrée et critères de sortie de la toile.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br> 
- Paramètres d'envoi 
    - Utilisateurs abonnés ou opt-in 
- Pas de retard
    - Délai de 1 heure
- Étape du message 
    - Examinez le modèle d'e-mail et le bloc HTML avec un exemple de modèle liquide pour ajouter des produits à votre message dans le modèle préconstruit. Si vous utilisez votre propre modèle d'e-mail, vous pouvez également faire référence aux [variables Liquid](#message-personalization), comme le montre la section suivante.

### Personnalisation des produits abandonnés dans les e-mails 

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

#### URL du produit

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

## Abandon de panier

Utilisez le modèle de **panier abandonné** pour couvrir les ventes potentielles perdues par les clients qui ont ajouté des produits à leur panier mais n'ont pas continué à passer à la caisse ou n'ont pas passé de commande. 

Un modèle de canvas "panier abandonné" appliqué avec des "règles d'entrée" étendues.]({% image_buster /assets/img_archive/abandoned_cart.png %})

### Configuration

Sur la page Canvas, sélectionnez **Utiliser un modèle de canvas** > **Modèles de Braze**, puis appliquez le modèle **Panier abandonné**. 

#### Paramètres par défaut

Les paramètres suivants sont préconfigurés dans votre Canvas :
- Principes de base 
    - Nom de la toile : **Abandon de panier**
    - Événement de conversion : `ecommerce.order_placed`
        - Date limite de conversion : 3 jours 
- Planification de l'entrée 
    - Déclencheur basé sur une action lorsqu'un utilisateur déclenche l'**événement Perform Cart Updated** (situé dans la liste déroulante).
    - L'heure de début est l'heure à laquelle vous créez le modèle Canvas.<br><br>\!["Options basées sur l'action" pour le Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br> 
- L'audience ciblée 
    - Audience d'entrée 
        - A utilisé ces applications **plus de 0** fois 
        - L'e-mail **n'est pas vide**
    - Contrôles d'entrée
        - Les utilisateurs sont immédiatement rééligibles pour la participation à Canvas.
    - Critères de sortie 
        - Effectue les opérations suivantes : `ecommerce.cart_updated`, `ecommerce.checkout_started`, ou `ecommerce.order_placed`<br><br>Contrôles d'entrée et critères de sortie de la toile.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br> 
- Paramètres d'envoi 
    - Utilisateurs abonnés ou opt-in 
- Pas de retard
     - Délai de 4 heures
- Étape du message 
    - Examinez le modèle d'e-mail et le bloc HTML avec un exemple de modèle liquide pour ajouter des produits à votre message dans le modèle préconstruit. Si vous utilisez votre propre modèle d'e-mail, vous pouvez également faire référence aux [variables Liquid](#message-personalization), comme le montre la section suivante.

### Personnalisation des produits du panier abandonné pour les e-mails {#abandoned-cart-checkout}

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

#### URL du panier en HTML

Si vous souhaitez renvoyer les utilisateurs à leur panier, vous pouvez ajouter une propriété d'événement imbriqué sous l'objet medata, comme par exemple :

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

## Caisse abandonnée

Utilisez le modèle **Abandoned checkout** pour cibler les clients qui ont commencé le processus de paiement mais qui sont partis avant de passer leur commande. 

Un modèle de canvas "Abandoned Checkout" appliqué avec des "règles d'entrée" étendues.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

### Configuration

Sur la page Canvas, sélectionnez **Utiliser un modèle de canevas** > **Modèles de Braze**, puis appliquez le modèle de **caisse abandonnée**. 

#### Paramètres par défaut

Les paramètres suivants sont préconfigurés dans votre Canvas :

- Principes de base 
    - Nom de la toile : **Caisse abandonnée**
    - Événement de conversion : `ecommerce.order_placed`
        - Date limite de conversion : 3 jours 
- Planification de l'entrée 
    - Déclencheur basé sur une action lorsqu'un utilisateur effectue l'événement `ecommerce.checkout_started` 
    - L'heure de début est l'heure à laquelle vous créez le modèle Canvas.<br><br>\!["Options basées sur l'action" pour le Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- L'audience ciblée 
    - Audience d'entrée 
        - A utilisé ces applications **plus de 0** fois 
        - L'e-mail **n'est pas vide**
    - Contrôles d'entrée
        - Les utilisateurs sont immédiatement rééligibles pour la participation à Canvas.
        - Critères de sortie 
            - Effectue les événements `ecommerce.order_placed` <br><br>Contrôles d'entrée et critères de sortie de la toile.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- Paramètres d'envoi 
    - Utilisateurs abonnés ou opt-in 
- Pas de retard
    - Délai de 4 heures
- Étape du message 
    - Examinez le modèle d'e-mail et le bloc HTML avec un exemple de modèle liquide pour ajouter des produits à votre message dans le modèle préconstruit. Si vous utilisez votre propre modèle d'e-mail, vous pouvez également faire référence aux [variables Liquid](#message-personalization), comme le montre la section suivante.

### Personnalisation des e-mails en cas d'abandon d'achat

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

#### URL de la caisse

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

## Confirmation de la commande et enquête de satisfaction

Utilisez le modèle d'**enquête de confirmation de commande & ** pour confirmer les commandes réussies et améliorer la satisfaction des clients.

Un modèle de canvas de "confirmation de commande" appliqué avec des "règles d'entrée" étendues.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

### Configuration

Sur la page Canvas, sélectionnez **Utiliser un modèle Canvas** > **Modèles de Braze**, puis appliquez le modèle d'**enquête de confirmation de commande & feedback.**  

#### Paramètres par défaut

Les paramètres suivants sont préconfigurés dans votre Canvas :

- Principes de base 
    - Nom de la toile : **Confirmation de commande avec enquête de satisfaction**
    - Événement de conversion : `ecommerce.session_start`
        - Date limite de conversion : 10 jours 
- Planification de l'entrée 
    - Déclencheur basé sur une action lorsqu'un utilisateur effectue l'événement `ecommerce.cart_updated` 
    - L'heure de début est l'heure à laquelle vous créez le modèle Canvas.<br><br>\!["Options basées sur l'action" pour le Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- L'audience ciblée 
    - Audience d'entrée 
        - A utilisé ces applications **plus de 0** fois 
        - L'e-mail **n'est pas vide**
    - Contrôles d'entrée
        - Les utilisateurs sont immédiatement rééligibles pour la participation à Canvas.
    - Critères de sortie 
        - Non applicable<br><br>\![Filtres et contrôles d'entrée supplémentaires pour le Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- Paramètres d'envoi 
    - Utilisateurs abonnés ou opt-in 
- Étape du message 
    - Examinez le modèle d'e-mail et le bloc HTML avec un exemple de modèle liquide pour ajouter des produits à votre message dans le modèle préconstruit. Si vous utilisez votre propre modèle d'e-mail, vous pouvez également faire référence aux [variables Liquid](#message-personalization), comme le montre la section suivante.

### Personnalisation des e-mails de confirmation de commande

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

#### URL du statut de la commande

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

## Personnalisation des messages

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) est un puissant langage de templating utilisé par Braze qui vous permet de créer un contenu dynamique et personnalisé pour vos clients. En utilisant les étiquettes Liquid, vous pouvez personnaliser les messages en fonction des données des clients, des informations sur les produits et d'autres variables, ce qui améliore l'expérience d'achat et favorise l'engagement.

### Principales fonctionnalités du Liquid

- **Contenu dynamique :** Insérez dans vos messages des informations spécifiques au client, telles que son nom, les détails de sa commande et ses préférences.
- **Logique conditionnelle :** Utilisez les instructions if/else pour afficher un contenu différent en fonction d'emplacements spécifiques (tels que l'emplacement/localisation du client et l'historique des achats).
- **Boucles :** Iteratez sur des collections de produits ou de données personnalisées pour afficher des listes ou des grilles d'éléments.

### Démarrer avec Liquid

Pour commencer à personnaliser vos messages à l'aide des étiquettes Liquid, vous pouvez consulter les ressources suivantes :

- Référence de [données Shopify]({{site.baseurl}}/shopify_features/#shopify-data) avec des étiquettes Liquid prédéfinies.
- [Liquide]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## Segmentation

Utilisez les segments de Braze pour créer des segments de clients ciblés en fonction d'attributs et de comportements spécifiques, et diffusez des messages et des campagnes personnalisés. Grâce à cette fonctionnalité puissante, vous pouvez engager efficacement vos clients en atteignant la bonne audience avec le bon message au bon moment.

Pour plus d'informations sur l'utilisation des segments, consultez la rubrique [À propos des segments de Braze]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments).

### Événements recommandés

Les événements liés au commerce électronique sont basés sur les [événements recommandés]({{site.baseurl}}/recommended_events/).
Parce que les événements recommandés sont des événements personnalisés plus proches de l'opinion, vous pouvez rechercher les noms d'événements eCommerce recommandés en sélectionnant n'importe quel [filtre d'événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters).

### Filtres pour le commerce électronique

Segmentez vos utilisateurs avec des filtres de commerce électronique, comme la **source de commerce électronique** et le **chiffre d'affaires total**, en allant à la section **Commerce électronique** dans le segmenteur.

!Segmenter la liste déroulante des filtres avec les filtres "Ecommerce".]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:80%"}

{% alert important %}
L'événement d'achat sera finalement abandonné et remplacé par des [événements recommandés par le commerce électronique.]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/) Dans ce cas, les filtres de segmentation ne s'afficheront plus sous le comportement d'achat. Pour obtenir une liste complète des événements d'achat, reportez-vous à la section [Enregistrement des événements d'achat]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

## Propriétés d'événement imbriquées

Pour segmenter par propriétés d'événement imbriquées, vous pouvez utiliser les [extensions segments.]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions) Par exemple, vous pouvez utiliser les extensions de segments pour savoir qui a acheté le produit "SKU-123" au cours des 90 derniers jours.

## Analyse/analytique (si utilisé comme adjectif)

{% alert note %}
Pour l'instant, l'intégration de Shopify ne permet pas de renseigner l'[événement d'achat de]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events) Braze. Par conséquent, les filtres d'achat, les étiquettes Liquid, les déclenchements basés sur l'action et les analyses doivent utiliser l'événement ecommerce.order_placed.
{% endalert %}

Pour créer un [rapport sur les événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) en fonction des personnes qui ont effectué un événement pris en charge par l'intégration, vous pouvez spécifier le [nom de]({{site.baseurl}}/shopify_data_features/) l'[événement]({{site.baseurl}}/shopify_data_features/) spécifique.

Pour obtenir des informations sur les tendances liées aux commandes passées à partir de vos Canevas lancés, vous devrez configurer un [tableau de bord des conversions]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard) et spécifier vos Canevas.

Pour des cas d'utilisation plus avancés, vous pouvez utiliser le [générateur de rapports de]({{site.baseurl}}/user_guide/analytics/query_builder/) Braze pour générer des rapports personnalisés. 

