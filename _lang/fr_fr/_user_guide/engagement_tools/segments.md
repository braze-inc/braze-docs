---
nav_title: Segmentations
article_title: Segmentations
page_order: 1
layout: dev_guide
guide_top_header: "Segmentations"
guide_top_text: "La segmentation de l'audience est un élément clé du marketing stratégique. Elle vous permet d'éviter de trop cibler, d'ennuyer ou de passer à côté d'un lien potentiel avec un client. Consultez les articles suivants pour apprendre comment segmenter et filtrer votre audience pour votre plus grand bénéfice (et le leur)."
descriptions: "La segmentation de l'audience est un élément clé du marketing stratégique. Elle vous permet d'éviter de trop cibler, d'ennuyer ou de passer à côté d'un lien potentiel avec un client. Consultez cette page d'atterrissage pour apprendre comment segmenter et filtrer votre audience pour votre plus grand bénéfice (et le leur)."
search_rank: 4
tool: Segments
page_type: landing
description: "Cette page d'atterrissage couvre les articles sur la segmentation dans les campagnes de tableau de bord. Vous y trouverez des informations sur la manière de configurer un segment, des filtres, des entonnoirs, des insights, des extensions, etc."

guide_featured_title: "Articles populaires"
guide_featured_list:
  - name: "Création d'une segmentation"
    link: /docs/user_guide/engagement_tools/segments/creating_a_segment/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Gestion des segments
    link: /docs/user_guide/engagement_tools/segments/managing_segments/
    image: /assets/img/braze_icons/edit-05.svg
  - name: Filtres de segmentation
    link: /docs/user_guide/engagement_tools/segments/segmentation_filters/
    image: /assets/img/braze_icons/flag-02.svg
  - name: Données de segmentation
    link: /docs/viewing_and_understanding_segment_data/
    image: /assets/img/braze_icons/pie-chart-01.svg

guide_menu_title: "More articles"
guide_menu_list:
  - name: Statistiques des segments
    link: /docs/user_guide/engagement_tools/segments/segment_insights/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Extension de segments
    link: /docs/user_guide/engagement_tools/segments/segment_extension/
    image: /assets/img/braze_icons/users-01.svg
  - name: Segments SQL
    link: /docs/sql_segments/
    image: /assets/img/braze_icons/users-01.svg
  - name: Segments du catalogue
    link: /docs/catalog_segments/
    image: /assets/img/braze_icons/users-01.svg
  - name: Profils utilisateurs
    link: /docs/user_guide/engagement_tools/segments/user_profiles/
    image: /assets/img/braze_icons/users-01.svg
  - name: Ciblage des emplacements
    link: /docs/user_guide/engagement_tools/segments/location_targeting/
    image: /assets/img/braze_icons/marker-pin-06.svg
  - name: Expressions régulières
    link: /docs/user_guide/engagement_tools/segments/regex/
    image: /assets/img/braze_icons/search-sm.svg
  - name: Listes de suppression
    link: /docs/user_guide/engagement_tools/segments/suppression_lists/
    image: /assets/img/braze_icons/list.svg 
  - name: Mesure de la taille des segments
    link: /docs/user_guide/engagement_tools/segments/measuring_segment_size/
    image: /assets/img/braze_icons/pie-chart-02.svg
  - name: Résolution des problèmes
    link: /docs/user_guide/engagement_tools/segments/troubleshooting/
    image: /assets/img/braze_icons/annotation-question.svg

guide_menu_title2: "Other"
guide_menu_list2:
  - name: Attributs personnalisés
    link: /docs/user_guide/data/custom_data/custom_attributes/
    image: /assets/img/braze_icons/table.svg

---

## À propos des segments de Braze

Dans Braze, les segments sont des groupes dynamiques d'utilisateurs qui répondent à des critères personnalisés que vous définissez, tels que les attributs et le comportement des clients, ainsi que les événements personnalisés. Vous pouvez affiner les critères en imbriquant des segments dans d'autres segments et en appliquant des fonctionnalités supplémentaires, ce qui permet de réduire la portée de votre audience afin d'envoyer un contenu hautement personnalisé et attrayant aux bons utilisateurs.

Vous pouvez créer autant de segmentations que vous le souhaitez pour cibler les utilisateurs. Explorez différentes combinaisons de fonctionnalités et de filtres de segmentation pour découvrir des façons créatives d'utiliser vos données utilisateur, et débloquer de nouvelles façons d'envoyer des messages pertinents aux utilisateurs et d'augmenter l'engagement.

Consultez les cas d'utilisation ci-dessous pour avoir un petit aperçu de la façon dont les segments de Braze peuvent vous aider à cibler vos utilisateurs.

### Cas d'utilisation

- **Messages de bienvenue :** Segmentez les nouveaux utilisateurs afin de pouvoir leur envoyer des e-mails d'onboarding ou des messages in-app qui leur présentent votre appli.
- **Récompenses de fidélité :** Segmentez les utilisateurs en fonction de la fréquence de leurs achats, de l'anniversaire de leur adhésion ou d'autres jalons, et envoyez des offres exclusives ou des récompenses à vos utilisateurs les plus fidèles.
- **Déclencheurs comportementaux :** Segmentez les utilisateurs en fonction de leurs actions, comme l'abandon d'un panier à la caisse, pour déclencher des messages in-app ou des notifications push.
- **Recommandations de l'article :** Segmentez les utilisateurs qui ont acheté des produits spécifiques et envoyez-leur des recommandations pour des produits complémentaires ou de niveau supérieur.
- **Test A/B :** Segmentez les utilisateurs pour effectuer des tests A/B sur différents messages, lignes d'objet ou contenus afin de déterminer ce qui résonne le mieux auprès d'utilisateurs d'âges, de sexes et d'autres attributs spécifiques.

#### Cas d'utilisation de l'extension de segments

Vous pouvez affiner vos segments en utilisant les [extensions de segments]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) pour cibler les utilisateurs en fonction d'un événement personnalisé ou d'un comportement d'achat stocké pendant toute la durée de vie de leur profil utilisateur.

- **Achats historiques :** Segmentez les utilisateurs selon qu'ils ont acheté une couleur spécifique d'un produit spécifique au moins deux fois au cours des deux dernières années.
- **Événements et interactions des messages :** Segmentez les utilisateurs selon qu'ils ont effectué un achat au cours des trente derniers jours et qu'ils ont également interagi avec un message in-app spécifique.
- **Données de la requête :** 
  - **Demande à Snowflake :** Segmentez les utilisateurs avec des données combinées provenant de Braze et de sources externes, telles qu'un CRM ou un entrepôt de données, en utilisant [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) pour interroger Snowflake.
  - **Synchronisation à partir de l'entrepôt de données :** Segmentez les utilisateurs dont les données sont directement synchronisées depuis votre entrepôt de données ou votre système de stockage de fichiers vers Braze en utilisant les [extensions de segmentation CDI.]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/)

