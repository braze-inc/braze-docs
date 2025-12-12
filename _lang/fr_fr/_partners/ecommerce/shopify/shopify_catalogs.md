---
nav_title: Synchronisation des produits Shopify
article_title: Synchronisation des produits Shopify
alias: /shopify_catalogs/
page_order: 4
description: "Cet article de référence explique comment importer vos produits Shopify dans les catalogues Braze."
---

# Synchronisation des produits Shopify 

> Vous pouvez synchroniser tous les produits de votre boutique Shopify avec un [catalogue]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) Braze pour une personnalisation plus poussée des messages. 

Les catalogues Shopify seront mis à jour en quasi-temps réel à mesure que vous apportez des modifications et des changements aux produits de votre boutique Shopify. Vous pouvez enrichir votre panier abandonné, votre confirmation de commande et plus encore avec les détails et informations sur le produit les plus à jour.

## Configuration de la synchronisation de votre produit Shopify {#setting-up}

Si vous avez déjà installé votre boutique Shopify, vous pouvez toujours synchroniser vos produits en suivant les instructions ci-dessous. 

### Étape 1 : Activer la synchronisation

Vous pouvez synchroniser vos produits avec un catalogue Braze via le flux d'installation Shopify ou sur la page partenaire Shopify. 

![Étape 3 du processus de configuration avec "Shopify Variant ID" comme "Catalog product identifier".]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:70%;"}

Les produits synchronisés avec un catalogue Braze contribueront à votre [limite de catalogue]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits).

### Étape 2 : Sélectionnez votre identifiant de produit

Sélectionnez quel identifiant de produit utiliser comme ID de catalogue :
- ID de variante Shopify
- UNITÉ DE GESTION DES STOCKS

Les valeurs d'ID et d'en-tête pour l'identifiant du produit que vous choisissez ne peuvent inclure que des lettres, des chiffres, des tirets et des underscores. Si l'identifiant du produit ne suit pas ce format, Braze le filtrera de votre synchronisation de catalogue.

Il s'agira de l'identifiant principal que vous utiliserez pour référencer les informations du catalogue Braze. 

{% alert note %}
Si vous sélectionnez l'unité de gestion des stocks comme ID de votre catalogue, assurez-vous que tous vos produits et variantes dans votre magasin ont une unité de gestion des stocks définie et qu'ils sont uniques. 
- Si un article a une unité de gestion des stocks manquante, Braze ne peut pas synchroniser ce produit dans le catalogue. 
- Si plusieurs produits possèdent la même unité de gestion des stocks, cela peut entraîner un comportement inattendu ou entraîner l'écrasement involontaire des informations du produit par l'unité de gestion des stocks en double.
{% endalert %}

### Étape 3 : Synchronisation en cours

Vous recevrez une notification de tableau de bord, et votre statut s'affichera comme « En cours » pour indiquer que la synchronisation initiale commence. Notez que le temps nécessaire pour terminer la synchronisation dépendra du nombre de produits et de variantes que Braze devra synchroniser depuis Shopify. Pendant ce temps, vous pouvez quitter cette page et attendre une notification de tableau de bord ou un e-mail pour vous informer lorsque cela est terminé.

Notez que si votre synchronisation initiale dépasse votre [limite de catalogue]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits), Braze arrêtera de synchroniser d'autres produits. Si vous dépassez la limite après la synchronisation réussie en raison de nouveaux produits ajoutés au fil du temps, la synchronisation ne sera plus active. Dans les deux cas, les mises à jour de produit de Shopify ne seront plus reflétées dans Braze. Contactez votre gestionnaire de compte pour envisager de mettre à niveau votre niveau d’abonnement. 

### Étape 4 : Synchronisation terminée

Vous recevrez une notification de tableau de bord et un e-mail après la synchronisation réussie. La page partenaire Shopify mettra également à jour l’état des catalogues Shopify en « Synchronisation ». Vous pouvez voir vos produits en cliquant sur le nom du catalogue dans la page partenaire Shopify.

Reportez-vous aux [cas d'utilisation supplémentaires des catalogues]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases) pour en savoir plus sur la façon de tirer parti des données de catalogue pour personnaliser votre message.

#### Données de catalogue Shopify prises en charge

- `id`
- `store_name`
- `shopify_product_id`
- `shopify_variant_id`
- `product_title`
- `variant_title`
- `status`
- `product_image_url`
- `variant_image_url`
- `vendor`
- `product_type`
- `product_url`
- `product_handle`
- `published_scope`
- `price`
- `compare_at_price`
- `inventory_quantity`
- `options`
- `option_values`
- `sku`

{% alert warning %}
La modification du catalogue Shopify de quelque manière que ce soit peut interférer involontairement avec les synchronisations de produits en temps réel. N’apportez pas de modifications au catalogue Shopify, car elles pourraient être écrasées par Shopify. Au lieu de cela, effectuez les mises à jour nécessaires du produit dans votre instance Shopify.<br><br>Pour supprimer votre catalogue Shopify, accédez à la page Shopify et désactivez la synchronisation. Ne supprimez pas directement le catalogue Shopify sur la page des catalogues.
{% endalert %}

##### En utilisant `product_handle` ou `product_url`

Pour accéder à `product_handle` et `product_url` et les utiliser, déconnectez et reconnectez votre catalogue Shopify en procédant comme suit.

1. Accédez à la page d'intégration de Shopify et sélectionnez **Modifier la configuration**.

![Page d'intégration de Shopify.]({% image_buster /assets/img/Shopify/edit_config.png %})

{: start="2"}
2\. Dans l'étape **Synchroniser le** catalogue, basculez le catalogue puis mettez à jour les paramètres.
3\. Basculez sur le catalogue et mettez à jour les paramètres.

![Shopify "Sync catalog" step with catalog toggle.]({% image_buster /assets/img/Shopify/catalog_toggle.png %})

## Cas d'utilisation de retour en stock et de baisse de prix

Pour configurer les notifications de retour en stock, suivez les étapes [ici]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications#back-in-stock-notifications).

Pour configurer les notifications de baisse de prix, suivez les étapes [ici]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications/).

Notez qu'avec l'intégration Shopify, vous devrez créer un événement personnalisé qui capture le statut d'abonnement d'un utilisateur dans votre catalogue pour chaque cas d'utilisation. L'événement personnalisé nécessitera une propriété d'événement qui correspond soit à l'[unité de gestion des stocks ou à l'ID de variante Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs#step-2-select-your-product-identifier) que vous avez sélectionnée dans le cadre de la synchronisation de votre produit Shopify. 

## Changement de l'ID du catalogue

Pour changer l'identifiant du produit pour votre catalogue Shopify, vous devez désactiver la synchronisation. Confirmez que vous avez cessé d'envoyer tout message utilisant ces données de catalogue Shopify en premier lieu. Relancez la synchronisation initiale du catalogue Shopify et sélectionnez votre identifiant de produit souhaité en suivant les étapes de [synchronisation des produits](#setting-up).

## Désactivation de la synchronisation de votre produit {#deactivate}

La désactivation de la fonctionnalité de synchronisation des produits Shopify supprimera l'intégralité de votre catalogue et de vos produits. Cela peut également avoir un impact sur les messages qui utilisent activement les données produit de ce catalogue. Confirmez que vous avez mis à jour ou mis en pause ces campagnes ou Canvas avant la désactivation, car cela pourrait entraîner l'envoi de messages sans détails sur les produits. Ne supprimez pas directement le catalogue Shopify sur la page des catalogues.

## Résolution des problèmes
Si la synchronisation de votre produit Shopify rencontre une erreur, cela pourrait être dû aux erreurs suivantes. Suivez les instructions sur la façon de corriger le problème et de résoudre la synchronisation :

| Erreur | Raison | Solution |
| --- | --- | --- |
| Erreur du serveur | Cela se produit s'il y a une erreur de serveur du côté de Shopify lorsque nous essayons de synchroniser vos produits. | [Désactivez la synchronisation](#deactivate) et resynchronisez à nouveau l'ensemble de votre inventaire de produits. |
| Unité de gestion des stocks en double | Cela se produit si vous utilisez une unité de gestion des stocks comme ID d'article de catalogue et avez des produits avec la même unité de gestion des stocks. Puisque l'ID de l'article du catalogue doit être unique, tous vos produits doivent avoir des unités de gestion des stocks uniques. | Vérifiez votre liste complète de produits et de variantes dans Shopify pour vous assurer qu'il n'y a pas d’unités de gestion des stocks en double. S'il y a des unités de gestion des stocks en double, mettez-les à jour pour qu'elles soient uniques dans votre compte de boutique Shopify. Après cela, [désactivez la synchronisation](#deactivate) et resynchronisez à nouveau l'ensemble de votre inventaire de produits. |
| Limite du catalogue dépassée | Cela se produit si vous dépassez votre limite de catalogue. Braze ne pourra pas terminer la synchronisation ou maintenir la synchronisation active en raison de l'absence de disponibilité de stockage. | Il existe deux solutions à ce problème :<br><br>1\. Contactez votre gestionnaire de compte pour mettre à niveau votre abonnement afin d'augmenter votre limite de catalogue. <br><br>2\. Libérez de l'espace de stockage en supprimant l'un des éléments suivants :<br>Cataloguer des articles d'autres catalogues<br>\- Autres catalogues<br>Sélections créées<br><br> Après avoir utilisé l'une ou l'autre des solutions, la synchronisation doit être désactivée puis resynchronisée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

