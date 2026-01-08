---
nav_title: "Données de l'utilisateur"
article_title: Données des utilisateurs de Braze
page_order: 3.5
layout: dev_guide
guide_top_header: "Données des utilisateurs de Braze"
guide_top_text: "Avant d'achever la mise en œuvre de Braze, veillez à ce que votre équipe de marketing et votre équipe de développement aient une conversation sur vos objectifs de marketing. Il est utile de tenir compte de ces objectifs et de travailler à rebours à partir d'eux lorsque vous décidez des données à suivre et de la manière de les suivre avec Braze."

page_type: landing
description: "Cette page d'atterrissage contient des articles sur la collecte de données sur les utilisateurs. Vous y trouverez des ressources sur les définitions d'archivage, l'importation d'utilisateurs, le cycle de vie du profil utilisateur, les cas d'utilisation, les meilleures pratiques, etc."

guide_featured_title: "Articles de section"
guide_featured_list:
  - name: Collecte de données SDK
    link: /docs/user_guide/data/unification/user_data_collection/sdk_data_collection/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Meilleures pratiques en matière de collecte de données
    link: /docs/user_guide/data/unification/user_data_collection/best_practices/
    image: /assets/img/braze_icons/thumbs-up.svg
  - name: "Exemple de cas d'utilisation pour la collecte de données"
    link: /docs/user_guide/data/unification/user_data_collection/collection_use_case/
    image: /assets/img/braze_icons/data.svg
  - name: Cycle de vie du profil utilisateur
    link: /docs/user_guide/data/unification/user_data_collection/user_profile_lifecycle/
    image: /assets/img/braze_icons/refresh-ccw-05.svg
  - name: "Importation d'utilisateurs"
    link: /docs/user_guide/data/unification/user_data_collection/user_import/
    image: /assets/img/braze_icons/users-01.svg
  - name: "Suppression d'utilisateurs"
    link: /docs/user_guide/data/unification/user_data/delete_users/
    image: /assets/img/braze_icons/users-01.svg
  - name: Utilisateurs anonymes
    link: /docs/user_guide/data/unification/user_data_collection/user_profile_lifecycle/anonymous_users/
    image: /assets/img/braze_icons/user-circle.svg
  - name: "Codes de la langue de l'utilisateur"
    link: /docs/user_guide/data/unification/user_data_collection/language_codes/
    image: /assets/img/braze_icons/globe-04.svg
---

<br>

{% alert important %}
Braze bannira ou bloquera les utilisateurs ("utilisateurs fictifs") ayant plus de 5 millions de sessions et n'ingérera plus leurs événements SDK parce qu'ils sont généralement le résultat d'une mauvaise intégration. Si vous constatez que cela s'est produit pour un utilisateur légitime, contactez votre gestionnaire de compte Braze.
{% endalert %}

<br>
