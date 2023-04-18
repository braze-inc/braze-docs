---
nav_title: Pré-remplissage des données personnalisées
article_title: Pré-remplissage des données personnalisées
page_order: 1
page_type: reference
description: "Cet article de référence décrit le processus de pré-remplissage de vos campagnes et segments avec des données personnalisées."
tool:
  - Segments
  - Campagnes
  
---

# Pré-remplissage des données personnalisées

> Il peut arriver que vous souhaitiez commencer à configurer des campagnes et des segments avec des données personnalisées avant que votre équipe de développement ait intégré ces données personnalisées. Braze vous permet de pré-renseigner des événements et des attributs personnalisés sur le tableau de bord avant que ne commence le suivi de ces données, pour que ces événements et attributs soient disponibles dans les menus déroulants et durant le processus de création de campagnes.

Pour pré-renseigner les événements et attributs personnalisés, allez sur la page **Manage Settings (Gérer les paramètres)** et sélectionnez l’onglet **Custom Attributes (Attributs personnalisés)** ou **Custom Events (Événements personnalisés)**. Ajoutez ensuite un nouvel attribut/événement personnalisé.

![Accédez aux attributs personnalisés ou aux événements personnalisés][21]

Pour les attributs personnalisés, sélectionnez un [type de données][20] (par exemple, booléen ou string). Le type de données d’un attribut détermine les filtres de segmentation disponibles pour cet attribut.

![Ajouter un nouvel attribut ou événement][22]{: style="max-width:40%;" }

Les événements personnalisés et les attributs personnalisés sont sensibles à la casse. Gardez cela à l’esprit lorsque votre équipe de développement intègrera ces événements ou attributs personnalisés : elle devra les nommer exactement comme vous les avez nommés ici, sinon Braze générera un autre événement ou un attribut personnalisé.

[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[21]: {% image_buster /assets/img_archive/prepopulate_page.png %}
[22]: {% image_buster /assets/img_archive/prepopulate_add.png %}
