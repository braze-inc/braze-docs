---
nav_title: Blocs de produits
article_title: Blocs de produits à glisser-déposer
page_order: 7
description: "Cet article de référence traite des blocs de produits à glisser-déposer, qui permettent aux utilisateurs d'ajouter et de configurer rapidement des vitrines dynamiques ou statiques d'articles de catalogue."
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# Glisser-déposer des blocs de produits 

> L'éditeur par glisser-déposer vous permet d'ajouter et de configurer rapidement des blocs de produits à vos messages pour une mise en valeur transparente des produits, sans qu'il soit nécessaire de créer un code Liquid personnalisé. 

{% alert important %}
La fonctionnalité de glisser-déposer des blocs de produits est en accès anticipé et n'est pour l'instant disponible que pour les e-mails. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions 

| Exigence | Description |
| --- | --- |
| Événements recommandés pour le commerce électronique | Les [événements recommandés pour le commerce électronique]({{site.baseurl}}/ecommerce_events/) fournissent des schémas de données normalisés pour les événements comportementaux clés qui se produisent avant et après la passation d'une commande. Ces événements remplaceront à terme l'ancien événement d'achat de Braze et deviendront la norme pour le suivi des comportements liés au commerce. <br><br> Les événements recommandés par eCommerce sont nécessaires pour les blocs de produits dynamiques.<br><br> Les événements recommandés pour le commerce électronique sont actuellement en accès anticipé. Contactez votre gestionnaire satisfaction client Braze si vous souhaitez participer à cet accès anticipé. |
| Modèles de canevas pour le commerce électronique | Les événements recommandés pour le commerce électronique prennent en charge des modèles préconstruits, notamment des modèles eCommerce Canvas conçus pour des cas d'utilisation essentiels tels que la navigation abandonnée, les paniers abandonnés et les confirmations de commande. <br><br>Si vous envisagez de mettre en œuvre l'un de ces cas d'utilisation essentiels du commerce électronique à l'aide des [modèles eCommerce Canvas]({{site.baseurl}}/ecommerce_use_cases/), vous devez utiliser ou suivre le modèle Canvas fourni. |
| Catalogue Braze | Vous devez créer un catalogue Braze comprenant les champs suivants, qui seront utilisés dans la configuration de votre bloc produit :{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

## Types de blocs de produits glisser-déposer

| Bloc de produits | Objectif | Cas d’utilisation | Disponibilité |
| --- | --- | --- | --- |
| Dynamique | Personnalisez vos messages avec une vitrine de produits basée sur les interactions avec les clients en utilisant des [événements et des catalogues recommandés pour le commerce électronique]({{site.baseurl}}/ecommerce_events/) dans nos [modèles eCommerce Canvas]({{site.baseurl}}/ecommerce_use_cases/). | {::nomarkdown}<ul><li>Parcourir Abandonné</li><li>Panier abandonné</li><li>Paiement abandonné</li><li>Les confirmations de commande</li></ul>{:/} | Disponible uniquement en canvas. |
| Statique | Personnalisez les produits en utilisant uniquement les données stockées dans un catalogue ou une [sélection de catalogue de]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) Braze. | Parfait pour présenter le lancement de nouveaux produits ou des offres spécifiques à une catégorie.| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role=”presentation” }

## Configuration du bloc de contenu du produit

Chaque type de bloc a des configurations de contenu différentes. 

### Champs du produit

Dans la section **Champs de produits**, sélectionnez votre type de bloc de produits, puis basculez sur les champs que vous souhaitez inclure pour chaque produit. Chaque champ est tiré de différentes sources en fonction du type de bloc de produits que vous sélectionnez.

#### Bloc de produits dynamiques

| Champ du produit | Source |
| --- | --- | 
| Image de variante | Catalogues | 
| Titre du produit | Catalogues | 
| Bouton pour l'URL du produit | Catalogues |
| Prix | eCommerce Propriétés d'événement recommandées|
| Quantité | eCommerce Propriétés d'événement recommandées| 
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

![Champs de produit pour un bloc de produit dynamique, qui sont divisés en données de catalogue et en données d'événement]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### Bloc de produits statiques

| Champ du produit | Source |
| --- | --- | --- |
| Image de variante | Catalogues |
| Titre du produit | Catalogues |
| Bouton pour l'URL du produit | Catalogues |
| Prix | Catalogues |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role=“presentation” }

![Champs de produit pour un bloc de produit statique, qui sont tous classés comme données de catalogue.]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### Options de mise en page

Utilisez les options de mise en page pour personnaliser l'affichage de vos produits dans votre bloc de produits.

| Option | Description |
| --- | --- |
| Orientation des produits | Choisissez l'orientation des champs d'image et de produit dans le bloc. |
| Alignement | Ajustez l'alignement des champs de texte et du bouton à l'intérieur du bloc. |
| Nombre maximum de produits par ligne | Affichez jusqu'à trois produits par ligne, jusqu'à 12 produits au total pour les blocs de produits statiques et jusqu'à 24 produits au total pour les blocs de produits dynamiques. |
| Espacement des produits | Définissez l'espacement entre les produits. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

![Options de mise en page pour l'orientation des produits, l'alignement, le nombre maximum de produits par ligne et l'espacement des produits.]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### Paramètres globaux du style d'e-mail 

Les [paramètres globaux de style d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings) vous permettent d'appliquer un style cohérent à vos e-mails dans Braze. Cela signifie que vous pouvez définir des styles spécifiques, tels que des polices, des couleurs et des boutons, qui s'appliqueront automatiquement à tous vos e-mails.

#### Comment les paramètres globaux de style d'e-mail fonctionnent-ils avec les blocs de produits ?

Les styles existants pour les paragraphes et les boutons s'appliqueront automatiquement aux éléments de texte et de bouton dans le bloc produit. Cela signifie que tout formatage que vous avez défini pour les paragraphes et les boutons sera utilisé de manière cohérente dans votre bloc de produits, ce qui permet de conserver un aspect homogène dans l'ensemble de votre e-mail.

## Mise en place de blocs de produits

### Configuration du catalogue 

{% alert important %}
Si vous utilisez l'intégration entre Braze et Shopify pour la [synchronisation des produits]({{site.baseurl}}/shopify_catalogs/), vous n'avez pas besoin de prendre des mesures supplémentaires pour utiliser les blocs de produits à glisser-déposer.<br><br> Si vous ne disposez pas d'informations sur la variante du produit, vous devez dupliquer les informations sur le produit de premier niveau dans les champs du produit et de la variante du produit dans les charges utiles et les catalogues d'événements. Cela signifie que vous devez fournir les mêmes détails sur le produit pour les deux identifiants afin de maintenir la cohérence pour que le bloc produit fonctionne correctement.
{% endalert %}

Pour utiliser les blocs de produits glisser-déposer, vous devez configurer un catalogue Braze qui inclut des valeurs de champs spécifiques. Ces champs seront utilisés dans la configuration de votre bloc produit. Assurez-vous que votre catalogue comprend les champs suivants :

| Champ | Description |
| --- | --- |
|`product_title` | Le titre du produit.|
|`product_url` | L'URL où les clients peuvent voir ou acheter le produit. |
|`variant_image_url` | L'URL de l'image variante. |

Commencez par travailler à partir de cet [exemple de catalogue de produits]({{site.baseurl}}/assets/download_file/ecommerce_product_catalog_sample.csv), qui comprend les champs obligatoires. 

![Un exemple de fichier CSV avec les champs obligatoires et d'autres.]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

## Création de blocs de produits

Ce guide vous guidera à travers les étapes pour créer, tester et assurer la fonctionnalité d'un bloc produit dynamique ou statique en utilisant notre éditeur glisser-déposer par e-mail.

### Étape 1 : Créer une campagne d'e-mail ou une étape du canvas d'e-mail

#### Bloc de produits dynamiques

{% alert note %}
Les blocs de produits dynamiques nécessitent des [événements recommandés par eCommerce]({{site.baseurl}}/ecommerce_events/) et ne peuvent être utilisés qu'au sein de [Canvases]({{site.baseurl}}/ecommerce_use_cases). Pour les utilisateurs de Braze Shopify, ces événements sont automatiquement inclus dans le cadre de l'intégration. Pour les utilisateurs non-Shopify, vous devez travailler avec vos développeurs pour passer ces événements dans Braze et vous assurer que l'identifiant principal du produit au sein des événements est ajouté en tant qu'ID de l'article du catalogue.
{% endalert %}

Créez un nouveau Canvas qui utilise l'un des modèles de Braze disponibles pour votre cas d'utilisation spécifique :
- Abandon de la navigation
- Panier abandonné
- Paiement abandonné
- Confirmations de commande

Pour des instructions détaillées sur la création de vos toiles de commerce électronique, reportez-vous aux [cas d'utilisation pour le commerce électronique.]({{site.baseurl}}/ecommerce_use_cases/)

#### Bloc de produits statiques

Créez une campagne e-mail par glisser-déposer, un Canvas basé sur l'action ou un modèle qui comporte une étape e-mail Message par glisser-déposer.

### Étape 2 : Ajouter un bloc produit

{% tabs %}
{% tab Bloc de produits dynamiques %}

Dans l'étape message, créez un e-mail ou modifiez le modèle existant à l'aide du compositeur d'e-mails par glisser-déposer.
Faites glisser un bloc produit dans votre message e-mail.
Confirmez que le type de bloc dynamique est sélectionné.
Sélectionnez le catalogue de produits que vous souhaitez utiliser pour la personnalisation. Assurez-vous qu'il s'aligne sur les produits des événements entrants que vous ciblez.

{% endtab %}
{% tab Bloc de produits statiques %}

Faites glisser un bloc produit dans votre message e-mail et sélectionnez le type de bloc statique.
Sélectionnez le catalogue que vous souhaitez utiliser pour votre bloc produit. Si votre catalogue comporte une sélection, vous devez la sélectionner pour restreindre davantage les produits qui s'affichent dans votre bloc de produits.

{% endtab %}
{% endtabs %}

![L'onglet "Contenu" contient des blocs éditeurs, tels que des blocs produits.]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### Étape 3 : Configurer les champs du produit

Sélectionnez les [champs du produit](#product-fields) qui doivent être affichés dans le bloc produit. Sélectionnez **Appliquer les paramètres** après chaque modification pour voir les mises à jour dans l'éditeur. 

Vous pouvez également personnaliser le texte précédant vos étiquettes Liquid. Par exemple, vous pouvez ajouter un signe de dollar ($) pour le prix d'un article ou mettre à jour le terme de la quantité en le remplaçant par "montant" ou un autre libellé préféré.

![Bloc de produits dont le prix est précédé d'un dollar.]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### Étape 4 : Configurer les paramètres de mise en page

Modifiez les [options de mise en page](#layout-options) pour actualiser la façon dont les produits s'affichent dans votre bloc de produits, et veillez à sélectionner **Appliquer les paramètres** après chaque modification.

### Étape 5 : Prévisualiser et tester votre message

{% tabs %}
{% tab Bloc de produits dynamiques %}

1. Dans la section **Prévisualisation et test**, prévisualisez le message en tant qu'utilisateur personnalisé.
2. Indiquez le nombre d'éléments que vous souhaitez afficher dans l'aperçu.
3. Confirmez que le nombre correct d'éléments apparaît et que vos options de mise en page sont appliquées correctement. Notez que les éléments qui apparaissent sont sélectionnés de manière aléatoire.

![Onglet "Aperçu en tant qu'utilisateur" avec une section déroulante "Bloc de produits dynamiques" qui spécifie l'affichage de 4 éléments.]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab Bloc de produits statiques %}

Un aperçu sera généré dans le compositeur par glisser-déposer lorsque vous appliquerez des modifications à votre bloc produit. 

![Compositeur d'e-mail par glisser-déposer montrant un bloc de produit généré avec différentes tuiles d'articles.]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

Une fois que vous avez créé votre message et que vous avez confirmé qu'il ressemble à ce qui était prévu, vous êtes prêt à l'envoyer !