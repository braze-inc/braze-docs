---
nav_title: "Cas d'utilisation du commerce électronique"
article_title: "Cas d'utilisation du commerce électronique"
alias: /ecommerce_use_cases/
page_order: 4
description: "Cet article de référence traite de plusieurs modèles de Braze préconstruits et adaptés spécifiquement aux marketeurs du commerce électronique, facilitant ainsi la mise en œuvre de stratégies essentielles."
toc_headers: h2
---

# Comment utiliser les événements recommandés pour le commerce électronique

> Cette page explique comment et où vous pouvez utiliser les événements recommandés pour le commerce électronique sur la plateforme, y compris comment utiliser les modèles Braze eCommerce Canvas.

{% alert important %}
Les [événements recommandés pour le commerce électronique]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) sont actuellement en accès anticipé. Contactez votre gestionnaire satisfaction client Braze si vous souhaitez participer à cet accès anticipé. <br><br>Si vous utilisez le nouveau connecteur Shopify, les événements recommandés pour le commerce électronique seront automatiquement disponibles via l'intégration.
{% endalert %}

## Utilisation d'un modèle Canvas

Pour utiliser un modèle Canvas :
1. Allez dans **Messagerie** > **Canvas.**
2. Sélectionnez **Créer un canvas** > **Utiliser un modèle de canvas**.
3. Recherchez dans l'onglet **Modèles de Braze** le modèle que vous souhaitez utiliser. Vous pouvez prévisualiser un modèle en sélectionnant son nom.
4. Sélectionnez **Appliquer** le modèle pour le modèle que vous souhaitez utiliser.<br><br>![La page « Modèles canvas » s'ouvre sur l'onglet « Modèles Braze » et affiche une liste des modèles récemment utilisés et des modèles Braze disponibles.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## Modèles de canevas pour le commerce électronique

Braze propose quatre modèles canvas pour le commerce électronique.

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

Pour obtenir la liste des filtres e-commerce et leurs définitions, veuillez vous référer aux [filtres de segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) et sélectionner la catégorie de recherche « e-commerce ».

![Menu déroulant des filtres de segment avec les filtres « E-commerce ».]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## Propriétés d'événement imbriquées

Pour segmenter par propriétés d'événement imbriquées, vous pouvez utiliser les [extensions segments.]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions) Par exemple, vous pouvez utiliser les extensions de segments pour savoir qui a acheté le produit "SKU-123" au cours des 90 derniers jours.

## Analyse

### Rapport sur les événements personnalisés

Vous pouvez suivre le volume d'événements recommandés pour le commerce électronique dans le [rapport Custom events]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/#analytics). Veuillez filtrer par **« Effectuer un événement personnalisé** », puis spécifiez le [nom de l'événement recommandé par eCommerce]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events) afin d'observer ses performances au fil du temps.

![Graphique des custom events affichant les résultats pour six événements sélectionnés.]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### Tableaux de bord

#### Tableau de bord de conversions

Après avoir lancé une campagne ou un canvas à l'aide de l'événement de conversion « Commander », vous pouvez créer un [rapport de conversion]({{site.baseurl}}/user_guide/analytics/dashboard/conversions_dashboard/#setting-up-your-report) correspondant afin de suivre les performances.

![Tableau détaillé des conversions avec les campagnes et les canevas, ainsi que les statistiques de conversion associées.]({% image_buster /assets/img_archive/conversion_details_table.png %})

#### Tableau de bord du chiffre d'affaires du commerce électronique

Pour obtenir des informations sur le chiffre d'affaires attribué à la dernière campagne ou au dernier canvas avec lequel un utilisateur a interagi avant de passer une commande, veuillez utiliser le [tableau de bord du chiffre d'affaires e-commerce]({{site.baseurl}}/ecommerce_revenue_dashboard/) et sélectionner une fenêtre de conversion.

### Rapport sur le chiffre d'affaires 

Pour analyser les données issues de ces nouveaux événements, veuillez vous rendre dans le [générateur de tableaux de bord]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) et consulter le [tableau de bord **« Chiffre d'affaires e-commerce - Attribution au dernier point de contact**]({{site.baseurl}}/ecommerce_revenue_dashboard/) ».
