---
nav_title: Synchronisation des collections Shopify
article_title: Synchronisation des collections Shopify
permalink: "/shopify_collections_sync/"
description: "Cet article de référence explique comment configurer la synchronisation des collections Shopify, ce qui vous permet de regrouper vos produits en collections afin que les clients puissent trouver vos produits par catégorie."
hidden: true
---

# Synchronisation des collections Shopify bêta

> La synchronisation des collections Shopify vous permet de regrouper vos produits en collections afin que les clients puissent trouver vos produits par catégorie. Pour une expérience d'achat plus fluide, vous pouvez intégrer des articles dans les collections de votre boutique dans vos messages Braze.

{% alert important %}
La synchronisation des collections Shopify est actuellement en version bêta. Si vous souhaitez participer à la version bêta, contactez votre gestionnaire de compte Braze.
{% endalert %}

## Configuration de la synchronisation des collections Shopify

Pour synchroniser vos produits de votre boutique Shopify à Braze, cochez la case pour **Synchroniser les collections Shopify** dans l'étape **Synchroniser les produits** de [l'intégration de Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify#setting-up-shopify-in-braze).<br><br>![Étape 4 de la synchronisation des produits Shopify avec la case « Synchroniser les collections Shopify » cochée.][1]

Une fois que vos produits ont été synchronisés, vous pouvez voir quels produits sont associés à vos collections en consultant votre catalogue Shopify. <br><br>![Ligne de tableau de catalogue montrant un produit dans les collections de "meilleures ventes" et "page d'accueil".][2]

Depuis votre catalogue Shopify, vous pouvez consulter votre collection Shopify dans l'onglet **Selections**. <br><br>![L'onglet Sélections affichant une liste de deux collections : « best-sellers (meilleures ventes) » et « frontpage (page d'accueil) ».][3]

### Fonctionnalité bêta

- Braze prendra en charge jusqu'à 30 collections
- L'ordre de tri de votre collection n'est pas maintenu ou pris en charge pour le moment. Pour l'instant, l'ordre de tri est basé sur ce qui suit :
    - Les produits les plus récents ajoutés à votre collection.
    - L'ordre dans lequel les éléments sont mis à jour lors des synchronisations continues.
    - L'ordre que vous sélectionnez dans l'onglet Sélections pour votre collection Shopify.

## Utilisation des collections Shopify

Utilisez vos collections Shopify pour personnaliser un message pour chaque utilisateur de votre campagne, de la même manière que vous utiliseriez une [séléction Braze]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/).

{% alert warning %}
Soyez conscient du comportement suivant dans la version bêta : <br><br>Si vous mettez à jour la description de la collection Shopify ou les paramètres de filtrage, vous interromprez la synchronisation de votre collection Shopify. En conséquence, votre collection Shopify ne fonctionnera pas comme prévu.
{% endalert %}

### Étape 1 : Configurer l'ordre de tri de votre collection Shopify

1. Spécifiez l'ordre dans lequel les résultats de votre collection Shopify sont retournés en sélectionnant l'**Ordre de tri** dans l'onglet de sélection de votre collection Shopify. Ceci comprend une option permettant de rendre l’ordre du classement aléatoire.
2. Entrez le nombre maximum de résultats (jusqu'à 50) pour le **Nombre limite**.
3. Sélectionnez **Mettre à jour la sélection**.

![Page Modifier la sélection, où vous pouvez sélectionner les paramètres de filtre, le type de tri et la limite de résultats.][4]

### Étape 2 : Utilisez la collection dans une campagne

1. Créez une campagne, puis sélectionnez **\+ Personnalisation** dans le compositeur de message.
2. Sélectionnez ce qui suit :<br>- **Produits du catalogue** comme **Type de personnalisation**<br>\- Nom du catalogue<br>\- Méthode de sélection des produits<br>\- Nom de la sélection (votre nom de collection Shopify) <br>Les informations à afficher dans votre message

{: start="3"}
3\. Copiez et collez l'extrait Liquid là où vous souhaitez que l'information apparaisse dans votre message.

![La section « Ajouter une personnalisation » avec des champs pour sélectionner votre catalogue, la méthode de sélection des articles et les informations à afficher.][5]{: style="max-width:30%;"}

#### Liquide dans les résultats de sélection

L'utilisation de tout résultat dans les catalogues, tels que les attributs personnalisés et les événements personnalisés, peut entraîner des résultats différents pour chaque utilisateur de votre sélection.

[1]: {% image_buster /assets/img/Shopify/sync_products.png %}
[2]: {% image_buster /assets/img/Shopify/view_catalog.png %}
[3]: {% image_buster /assets/img/Shopify/selections_tab.png %}
[4]: {% image_buster /assets/img/Shopify/edit_selection.png %}
[5]: {% image_buster /assets/img/Shopify/add_personalization.png %}
