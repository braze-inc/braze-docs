---
nav_title: Messages sur les produits
article_title: Messages sur les produits
page_order: 2
description: "Cette page explique comment utiliser les messages produits WhatsApp pour envoyer des messages WhatsApp interactifs qui présentent les produits de votre catalogue Meta."
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - Campaigns
channel:
 - WhatsApp
---

# Messages sur les produits

> Les messages produits vous permettent d'envoyer des messages WhatsApp interactifs qui présentent des produits directement à partir de votre catalogue Meta.

Lorsque vous envoyez un message WhatsApp sur un produit à un utilisateur, celui-ci suit le parcours client suivant :

1. L'utilisateur reçoit le message de votre produit ou de votre catalogue dans WhatsApp.
2. L'utilisateur ajoute des produits à son panier directement depuis WhatsApp.
3. L'utilisateur clique sur **Passer une commande** dans WhatsApp.
4. Votre site web ou votre app reçoit les données du panier de Braze et génère un lien de paiement.
5. L'utilisateur est dirigé vers votre site web ou votre application pour terminer son paiement.

Lorsque les utilisateurs ajoutent des articles à leur panier par le biais des messages du catalogue, Braze reçoit des données webhook pour les actions de suivi.

## Exigences

| Exigence | Description |
| --- | --- |
| Compte WhatsApp Business | Pour utiliser les envois de produits WhatsApp, vous devez disposer d'un compte WhatsApp Business connecté à Braze. |
| Méta catalogue | Vous devez mettre en place un Meta catalogue dans votre gestionnaire de commerce. |
| Respect de la durée | Respecter les [conditions et politiques de Meta Commerce.](https://www.facebook.com/policies_center/commerce) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Types d'envoi de messages sur les produits

{% alert note %}
Améliorez votre expérience des messages produits grâce au sélecteur de produits intégré, accessible à l'étape 4 de la [configuration des messages produits](#setting-up-product-messages).
{% endalert %}

{% tabs local %}
{% tab Catalog messages %}

Les messages du catalogue affichent l'ensemble de votre catalogue de produits dans un format interactif. Ils sont disponibles sous forme de [messages types et de messages de réponse.](#building-a-product-message)

Si vous avez activé les autorisations de catalogue pour Braze lors de la [configuration](#setting-up-product-messages), vous pouvez sélectionner la vignette visible par les utilisateurs. 

{% alert note %}
Vous n'avez pas besoin d'effectuer des sélections de produits supplémentaires dans Braze, car la connexion au catalogue est gérée par Meta et est donc héritée dans votre catalogue de produits.
{% endalert %}


{% endtab %}
{% tab Multi-product messages %}

Les messages multiproduits mettent en avant des produits spécifiques de votre catalogue, avec jusqu'à 30 articles mis en avant par message. Ils sont disponibles sous forme de [messages types et de messages de réponse.](#building-a-product-message)

Vous pouvez sélectionner les produits manuellement à l'aide d'ID ou, si vous avez activé les autorisations de catalogue lors de la [configuration](#setting-up-product-messages), utiliser le sélecteur de produits déroulant.

{% alert important %}
Il y a un problème connu d'affichage de l'en-tête avec les modèles d'envoi messages multi-produits sur Meta. Meta est conscient du problème et travaille à sa résolution.
{% endalert %}

{% endtab %}
{% tab Single product %}

Les messages portant sur un seul produit mettent en valeur un produit spécifique de votre catalogue. Ils sont disponibles sous forme d'[envois de messages.](#building-a-product-message)

Vous pouvez sélectionner les produits manuellement à l'aide d'ID ou, si vous avez activé les autorisations de catalogue lors de la [configuration](#setting-up-product-messages), utiliser le sélecteur de produits déroulant.

{% endtab %}
{% endtabs %}

## Mise en place des messages sur les produits

1. Dans le [gestionnaire Meta Commerce](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#), suivez les [instructions de Meta](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1) pour créer votre catalogue Meta. Assurez-vous de vous trouver dans le même portefeuille Meta Business où réside votre WhatsApp Business Accont connecté à Braze.
2. Suivez les instructions de Meta pour [connecter votre catalogue Meta](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715) à votre compte professionnel WhatsApp connecté à Braze en attribuant l'autorisation "Gérer le catalogue" dans Meta Business Manager. 

\![Méta page "Catalogues" avec une flèche pointant vers le bouton "Attribuer un partenaire" pour le catalogue appelé "sweeney_catalog".]({% image_buster /assets/img/whatsapp/meta_catalog.png %}){: style="max-width:90%;"}

Veillez à utiliser l'ID du gestionnaire de Braze, `332231937299182`, comme ID de l'entreprise partenaire.

\![Fenêtre de partage d'un catalogue avec un partenaire qui contient des champs permettant de saisir un ID d'entreprise partenaire et d'attribuer l'autorisation "Gérer le catalogue".]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Sélectionnez les paramètres de votre catalogue Meta. Vous devez sélectionner **Afficher l'icône du catalogue dans l'en-tête du chat** pour envoyer les messages du catalogue.

!Page des paramètres du gestionnaire WhatsApp pour le catalogue "Catalog_products".]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:90%;"}

{: start="4"}
4\. Dans Braze, suivez le processus d'[inscription intégré]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) pour fournir des autorisations. Veillez à sélectionner **tous les** catalogues pour lesquels vous souhaitez obtenir des autorisations. Cela déverrouillera le sélecteur de produits intégré à Braze.

\![La fenêtre avec cinq catalogues sélectionnés fournit des autorisations.]({% image_buster /assets/img/whatsapp/select_catalogs.png %}){: style="max-width:50%;"}

{% alert tip %}
Pour connaître les meilleures pratiques à suivre lors de la création de catalogues Meta, reportez-vous à [Conseils pour créer un catalogue de haute qualité dans Commerce Manager.](https://www.facebook.com/business/help/2086567618225367?id=725943027795860)
{% endalert %}

## Créer un message sur le produit

Vous pouvez créer un message produit en utilisant un modèle de message WhatsApp ou un message de réponse.

{% tabs local %}
{% tab WhatsApp message template %}

1. Dans votre gestionnaire Meta Business, allez dans **Modèles de messages.**
2. Sélectionnez **Catalogue** comme format, puis choisissez entre **Message catalogue** (affiche le catalogue complet) et **Message catalogue multi-produits** (met en évidence des articles spécifiques).
3. Dans Braze, créez une campagne WhatsApp ou une étape du message canvas.
4. Sélectionnez le groupe d'abonnement correspondant à l'endroit où vous avez soumis le modèle.
5. Sélectionnez **WhatsApp Template Message.**
6. Sélectionnez le modèle que vous souhaitez utiliser.
    - Si vous sélectionnez un modèle multi-produits, indiquez le titre de la section et les ID de contenu des produits à mettre en évidence. Vous pouvez soit copier l'ID du contenu directement à partir de votre gestionnaire Meta Commerce, soit, si vous avez activé les permissions pour le sélecteur de produits intégré, sélectionner les éléments.

\![Liste d'éléments avec des champs pour saisir les titres de vos sections et l'ID du contenu.]({% image_buster /assets/img/whatsapp/multi_product_template.png %}){: style="max-width:60%;"}

\![Liste d'éléments avec une liste déroulante d'éléments à sélectionner.]({% image_buster /assets/img/whatsapp/content_id_items.png %}){: style="max-width:60%;"}

{: start="7"}
7\. Continuez à créer votre message.

{% endtab %}
{% tab Response message %}

1. Dans Braze, créez une campagne WhatsApp ou une étape du message canvas.
2. Sélectionnez un groupe d'abonnement.
3. Sélectionnez **Response Message (message de réponse)**.
4. Sélectionnez **Meta Product Messages.**

\![Options permettant de sélectionner un type de message et la présentation du message de réponse, avec "Response Message" et "Meta Product Messages" en surbrillance.]({% image_buster /assets/img/whatsapp/response_message_layouts.png %}){: style="max-width:90%;"}

{: start="5"}
5\. Sélectionnez le [type de message](#product-message-types) que vous souhaitez utiliser.

!Sélection de la mise en page de "Multi-produits".]({% image_buster /assets/img/whatsapp/multi-product_message_layout.png %}){: style="max-width:90%;"}

{: start="6"}
6\. Continuez à créer votre message.

Exemple de message de produit Meta avec des informations complètes sur les produits.]({% image_buster /assets/img/whatsapp/example_response_message.png %}){: style="max-width:90%;"}

{% endtab %}
{% endtabs %}

## Gestion des produits

### Accès au gestionnaire de commerce

Dans votre Meta Business Manager, allez dans **Commerce Manager** et sélectionnez votre organisation. Ici, vous pouvez gérer les ressources de votre catalogue, telles que :
- Créer de nouveaux catalogues
- Ajouter des produits aux catalogues existants
- Mise à jour des informations sur les produits
- Supprimer les articles en fin de série

{% alert important %}
Si vous supprimez les produits référencés de votre catalogue, les messages associés ne seront pas envoyés.
{% endalert %}

## Recevoir les questions entrantes sur les produits 

Les utilisateurs peuvent répondre au message de votre produit ou de votre catalogue en posant des questions sur le produit. Ceux-ci arrivent sous forme de messages entrants, qui peuvent ensuite être triés à l'aide d'un [parcours d'action.]({{site.baseurl}}/action_paths/) 

En outre, Braze extrait l'ID du produit et l'ID du catalogue de ces questions, de sorte que si vous souhaitez automatiser les réponses ou envoyer les questions à une autre équipe (comme le support client), vous pouvez inclure ces détails. Par exemple, vous pourriez personnaliser les réponses avec les propriétés WhatsApp de `inbound_product_id` ou `inbound_catalog_id`.

\!["Fenêtre "Ajouter une personnalisation" avec un type de personnalisation "Propriétés WhatsApp" et un attribut mis en évidence de "inbound_product_id".]({% image_buster /assets/img/whatsapp/inbound_product_questions.png %}){: style="max-width:60%;"}

## Sortie de la caisse : Traitement des paniers et webhooks

Lorsque les utilisateurs interagissent avec vos messages WhatsApp sur les produits, ils peuvent parcourir les produits et ajouter des articles à leur panier. Cependant, il n'y a actuellement aucune fonctionnalité de caisse intégrée pour les informations d'expédition ou le traitement des paiements. Nous vous encourageons plutôt à créer un panier au sein de votre propre application ou site web et à diriger les utilisateurs vers ce panier à l'aide d'un lien personnalisé.

### Considérations

- **Pas de paiement in-app :** Les utilisateurs ne peuvent pas effectuer d'achats directement dans WhatsApp. Toutes les transactions doivent être redirigées vers votre site web ou votre appli.
- **Lien personnalisé requis :** Vous devez créer un lien personnalisé qui dirige les utilisateurs vers leur panier sur votre plateforme.
- **Configuration manuelle :** Le processus de configuration nécessite une configuration manuelle de votre panier et de vos flux d'envoi de messages.

{% alert note %}
Actuellement, nous ne prenons pas en charge les paiements effectués directement dans WhatsApp, et la prise en charge future sera spécifique à chaque pays (actuellement, Meta ne l'offre qu'aux entreprises basées en Inde, au Brésil et à Singapour et travaillant directement avec les utilisateurs de ces pays).
{% endalert %}

### Mise en place de déclencheurs de panier

Lorsqu'un client passe une commande dans WhatsApp, Braze le fait automatiquement :
1. Reçoit le contenu du panier de WhatsApp (ID des produits, quantités et autres données de la commande).
2. Crée un événement eCommerce `ecommerce.cart_update` avec toutes les données pertinentes, y compris `source = whats_app`.
3. Déclenche une réponse, ce qui vous permet d'implémenter des campagnes automatisées pour répondre à la commande.

L'événement `ecommerce.cart_update` eCommerce n'apparaît dans la liste de Braze qu'après l'envoi d'un événement, ce qui peut être fait en générant un message de produit test à partir de Braze et en soumettant un événement de panier.
L'événement de la charrette comprend :

- **ID du panier :** Identifiant unique du panier
- **Produits :** Liste d'articles avec ID de produit, quantités et prix
- **Valeur totale :** Somme de tous les éléments
- **Monnaie :** La devise du panier
- **Source :** Marqué comme "whats_app"
- **Métadonnées :** Données supplémentaires telles que l'ID du catalogue et le texte du message

Vous pouvez trouver des informations supplémentaires sur les événements du panier Braze dans la rubrique [Types d'événements recommandés pour le commerce électronique.]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events)

### Mise en place d'une réponse déclenchée

1. Créez un déclencheur d'événement personnalisé pour `ecommerce.cart_updated`.
2. Ajoutez un filtre de propriété pour `source = "whats_app"`.

\![Étape du canvas pour un déclencheur d'événement personnalisé `ecommerce.cart_updated` dont la propriété de base "source" est égale à `whats_app`.]({% image_buster /assets/img/whatsapp/product_message_canvas_step.png %})

{: start="3"}
3\. Configurez des actions de suivi basées sur les données du panier.

### Mise en œuvre de la vérification recommandée 

{% tabs local %}
{% tab Simple Liquid-based cart links %}

Utilisez Liquid pour créer des URL de panier directement dans votre message de réponse. La meilleure solution est de disposer d'ID de produits cohérents entre WhatsApp et votre plateforme d'e-commerce.

#### Exemple Liquid

{% raw %}
```liquid
{% assign cart_link = "http://alejandro-test-new.myshopify.com/cart/" %}
{% for product in event_properties.products %}
 {% assign variant_id = product.product_id %}
 {% assign quantity = product.quantity %}
 {% if forloop.first %}
   {% assign cart_link = cart_link | append: variant_id | append: ":" | append: quantity %}
 {% else %}
   {% assign cart_link = cart_link | append: "," | append: variant_id | append: ":" | append: quantity %}
 {% endif %}
{% endfor %}
{{ cart_link }}
```
{% endraw %}

#### Configuration

1. Créez une campagne d'envoi de messages de réponse WhatsApp avec le déclencheur d'un événement eCommerce `ecommerce.cart_update`.
2. Créez un message ultérieur avec l'URL du panier.
3. Créez l'URL de votre panier avec Liquid. Si vous utilisez Shopify, vous pouvez [créer un panier permanent](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks) avec l'exemple précédent Liquid.

Diagramme montrant le déroulement du processus de paiement pour un panier généré par Liquid : Meta envoie un message de réception de commande à Braze, qui déclenche un action déclenchement puis crée un message avec un lien de panier, qui envoie ensuite un message WhatsApp.]({% image_buster /assets/img/whatsapp/liquid_generated_cart_link_checkout.png %})

{% endtab %}
{% tab Connected Content %}

Effectuez un appel API à votre système de commerce électronique pour générer une URL de paiement personnalisée. C'est la meilleure solution si vous avez besoin de générer des URL de panier dynamiques ou d'un mappage complexe des produits.

#### Configuration

1. Créez une campagne webhook ou une étape du canvas déclenchée par l'événement eCommerce. [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated) qui enverra les données du panier à votre système de commerce électronique.
2. Créez une campagne WhatsApp ou une étape Canvas Message déclenchée par le même événement eCommerce pour envoyer un message de réponse WhatsApp avec l'URL du panier à l'utilisateur. Suivez les instructions du message de réponse suivant pour utiliser le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content).

Diagramme montrant le déroulement de l'expérience de paiement pour un appel de contenu connecté : Meta envoie un envoi de messages de commande reçue à Braze, qui a des appels en va-et-vient avec une plateforme de commerce électronique, puis envoie un message WhatsApp.]({% image_buster /assets/img/whatsapp/connected_content_checkout.png %})

{% endtab %}
{% tab Webhook and custom events %}

Utilisez des webhooks pour envoyer les données du panier à votre système, puis déclenchez des messages de suivi grâce à des événements personnalisés. C'est la meilleure solution pour les intégrations complexes nécessitant un traitement approfondi des paniers ou des flux de travail en plusieurs étapes.

#### Configuration

Créez une campagne webhook ou une étape du canvas déclenchée par l'événement `ecommerce.cart_update` eCommerce, qui enverra les données du panier à votre système eCommerce. Votre API sera alors :
1. Recevoir les données du panier
2. Créer un panier dans votre système
3. Générer l'URL de la caisse
4. Envoyez un événement `checkout_started` à Braze, déclenchant l'envoi de votre message WhatsApp avec le lien de paiement.

Diagramme montrant le déroulement de l'expérience de paiement pour les webhooks et les événements personnalisés : Meta envoie un message de réception de commande à Braze, qui a des appels en va-et-vient avec une plateforme de commerce électronique, puis envoie un message WhatsApp avec l'URL du panier.]({% image_buster /assets/img/whatsapp/webhooks_custom_events_checkout.png %})

{% endtab %}
{% endtabs %}

## Essais et validation

### Exigences relatives aux messages d'essai

La fonctionnalité du panier est transférée entre les messages de test, mais le traitement du résultat de l'envoi n'est pas transféré.

### Aperçu du message

- Les images et les détails des produits sont tirés de votre catalogue Meta.
- L'aperçu interactif affiche des marqueurs substitutifs jusqu'à ce que l'intégration soit terminée.

### Codes d'erreur 

- Si un ID de produit n'existe pas dans le catalogue, vous recevrez l'erreur `product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359`.
- Si un catalogue est déconnecté du WABA, vous recevrez l'erreur `Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings`.
