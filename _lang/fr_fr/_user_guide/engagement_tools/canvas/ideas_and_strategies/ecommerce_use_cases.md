---
nav_title: "Cas d'utilisation du commerce électronique"
article_title: "Cas d'utilisation du commerce électronique"
alias: /ecommerce_use_cases/
page_order: 4
description: "Cet article de référence traite de plusieurs modèles de Braze préconstruits et adaptés spécifiquement aux marketeurs du commerce électronique, facilitant ainsi la mise en œuvre de stratégies essentielles."
toc_headers: h2
---

# Comment utiliser les événements recommandés pour le commerce électronique

> Cette page explique comment et où vous pouvez utiliser les événements recommandés par eCommerce sur la plateforme, notamment comment utiliser les modèles eCommerce Canvas de Braze.

{% alert important %}
Les [événements recommandés pour le commerce électronique]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) sont actuellement en accès anticipé. Contactez votre gestionnaire satisfaction client Braze si vous souhaitez participer à cet accès anticipé. <br><br>Si vous utilisez le nouveau connecteur Shopify, les événements recommandés pour le commerce électronique seront automatiquement disponibles via l'intégration.
{% endalert %}

## Utilisation d'un modèle Canvas

Pour utiliser un modèle Canvas :
1. Allez dans **Messagerie** > **Canvas.**
2. Sélectionnez **Créer un canvas** > **Utiliser un modèle de canvas**.
3. Recherchez dans l'onglet **Modèles de Braze** le modèle que vous souhaitez utiliser. Vous pouvez prévisualiser un modèle en sélectionnant son nom.
4. Sélectionnez **Appliquer** le modèle pour le modèle que vous souhaitez utiliser.<br><br>![La page "Canvas templates" s'ouvre sur l'onglet "Braze templates" et affiche une liste des modèles récemment utilisés et des modèles de Braze sélectionnables.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## Modèles de canevas pour le commerce électronique

Braze propose quatre modèles de canvas pour le commerce électronique.

{% multi_lang_include canvas/ecommerce_templates.md %}

## Personnalisation des messages

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) est un puissant langage de templating utilisé par Braze qui vous permet de créer un contenu dynamique et personnalisé pour vos clients. En utilisant les étiquettes Liquid, vous pouvez personnaliser les messages en fonction des données des clients, des informations sur les produits et d'autres variables, ce qui améliore l'expérience d'achat et favorise l'engagement.

### Principales fonctionnalités de Liquid

- **Contenu dynamique :** Insérez dans vos messages des informations spécifiques au client, telles que son nom, les détails de sa commande et ses préférences.
- **Logique conditionnelle :** Utilisez les instructions if/else pour afficher un contenu différent en fonction d'emplacements spécifiques (tels que l'emplacement/localisation du client et l'historique des achats).
- **Boucles :** Iteratez sur des collections de produits ou de données personnalisées pour afficher des listes ou des grilles d'éléments.

### Démarrer avec Liquid

Pour commencer à personnaliser vos messages à l'aide des étiquettes Liquid, vous pouvez consulter les ressources suivantes :

- Référence de [données Shopify]({{site.baseurl}}/shopify_features/#shopify-data) avec des étiquettes Liquid prédéfinies.
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## Segmentation

Utilisez les segments de Braze pour créer des segments de clients ciblés en fonction d'attributs et de comportements spécifiques, et diffusez des messages et des campagnes personnalisés. Grâce à cette fonctionnalité puissante, vous pouvez engager efficacement vos clients en atteignant la bonne audience avec le bon message au bon moment.

Pour plus d'informations sur l'utilisation des segments, consultez la rubrique [À propos des segments de Braze]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments).

### Événements recommandés

Les événements liés au commerce électronique sont basés sur les [événements recommandés]({{site.baseurl}}/recommended_events/).
Parce que les événements recommandés sont des événements personnalisés plus proches de l'opinion, vous pouvez rechercher les noms d'événements eCommerce recommandés en sélectionnant n'importe quel [filtre d'événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters).

### Filtres pour le commerce électronique

Segmentez vos utilisateurs avec des filtres de commerce électronique, comme la **source de commerce électronique** et le **chiffre d'affaires total**, en allant à la section **Commerce électronique** dans le segmenteur. 

Pour obtenir la liste des filtres eCommerce et leur définition, reportez-vous à la section [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) et sélectionnez la catégorie de recherche "eCommerce".

![Segmentation de la liste déroulante des filtres avec des filtres "Ecommerce".]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## Propriétés d'événement imbriquées

Pour segmenter par propriétés d'événement imbriquées, vous pouvez utiliser les [extensions segments.]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions) Par exemple, vous pouvez utiliser les extensions de segments pour savoir qui a acheté le produit "SKU-123" au cours des 90 derniers jours.

## Analyse

### Rapport sur les événements personnalisés

Vous pouvez suivre le volume des événements recommandés pour le commerce électronique dans le [rapport sur les événements personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/#analytics). Filtrez par **Perform Custom Event**, puis indiquez le [nom de l'événement personnalisé eCommerce]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events) pour afficher ses performances dans le temps.

![Graphique des événements personnalisés affichant les résultats de six événements sélectionnés.]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### Rapport sur les conversions 

### Rapport sur les événements personnalisés

Pour créer un [rapport sur les événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) en fonction des personnes qui ont effectué un événement pris en charge par l'intégration, vous pouvez spécifier le [nom de l'événement]({{site.baseurl}}/shopify_data_features/) spécifique.

### Tableaux de bord

#### Tableau de bord de conversions

Pour obtenir des informations sur les tendances liées aux commandes passées à partir de vos Canevas lancés, configurez un [tableau de bord des conversions]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard) et spécifiez vos Canevas.

#### Tableau de bord des chiffres affaires du commerce électronique

Pour obtenir des informations sur les revenus attribués à la dernière campagne ou Canvas avec lequel un utilisateur a interagi avant de passer une commande, utilisez le [tableau de bord des revenus du commerce électronique]({{site.baseurl}}/ecommerce_revenue_dashboard/) et sélectionnez une fenêtre de conversion.

### Générateur de requêtes

### Chiffre d'affaires 

Pour analyser les données de ces nouveaux événements, accédez au [générateur de tableaux de bord]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) et affichez le [tableau de bord**eCommerce Revenue - Last Touch Attribution**]({{site.baseurl}}/ecommerce_revenue_dashboard/).
