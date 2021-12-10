---
nav_title: Pré-remplissage des données personnalisées
article_title: Pré-remplissage des données personnalisées
page_order: 0.2
page_type: Référence
description: "Cet article de référence décrit le processus de pré-remplissage de vos campagnes et segments avec des données personnalisées."
tool:
  - Segments
  - Campagnes
---

# Pré-remplissage des données personnalisées

Il peut arriver que vous vouliez commencer à configurer des campagnes et des segments en utilisant des données personnalisées avant que ces données personnalisées aient été intégrées par votre équipe de développement. Braze vous permet de pré-remplir les événements et attributs personnalisés sur le tableau de bord avant que ces données ne commencent à suivre, afin que ces événements et attributs soient disponibles dans les listes déroulantes, et dans le cadre du processus de création de campagne.

Pour pré-remplir les événements et attributs personnalisés, accédez à la page **Gérer les paramètres** et sélectionnez l'onglet **Attributs personnalisés** ou **Événements personnalisés**. Ajoute ensuite un nouvel attribut personnalisé ou un événement personnalisé.

!\[Naviguer vers des attributs personnalisés ou des événements personnalisés\]\[21\]

Pour les attributs personnalisés, sélectionnez un [type de données][20] pour cet attribut (par exemple, booléen ou chaîne). Le type de données d'un attribut déterminera quels types de filtres de segmentation sont disponibles pour cet attribut.

!\[Ajouter un nouvel attribut ou un événement\]\[22\]{: style="max-width:60%;" }

Les événements personnalisés et les attributs personnalisés sont sensibles à la casse. Gardez cela à l'esprit lorsque votre équipe de développement intègre ces événements personnalisés ou attributs plus tard, ils doivent les nommer exactement comme vous les avez nommés ici — y compris l'utilisation de lettres majuscules ou minuscules — sinon Braze générera un événement ou un attribut personnalisé différent.
[21]: {% image_buster /assets/img_archive/prepopulate_page.png %} [22]: {% image_buster /assets/img_archive/prepopulate_add.png %}

[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
