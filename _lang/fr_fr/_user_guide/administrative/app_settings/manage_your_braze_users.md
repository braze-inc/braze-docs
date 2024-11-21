---
nav_title: Utilisateurs de l’entreprise
article_title: Utilisateurs de l’entreprise
page_order: 23
layout: dev_guide
guide_top_header: "Utilisateurs de l’entreprise"
guide_top_text: "En tant qu’administrateur de compte Braze de votre entreprise, vous pouvez juger nécessaire de gérer les utilisateurs sur une base plus granulaire ou cas par cas. Braze peut vous y aider en créant des Teams et en gérant les autorisations des utilisateurs et les paramètres à l'échelle de l'entreprise."

page_type: landing
description: "Cette page d’accueil répertorie des articles sur la gestion des utilisateurs de Braze, tels que l’ajout et la suppression d’utilisateurs, la définition des autorisations utilisateur, la création d’équipes et la gestion des paramètres de l’entreprise."

guide_featured_title: "Section Articles"
guide_featured_list:
- name: Gestion des utilisateurs de Braze
  link: /docs/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/
  image: /assets/img/braze_icons/user-plus-01.svg
- name: Définition des autorisations utilisateur
  link: /docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/
  image: /assets/img/braze_icons/user-square.svg
- name: Équipes
  link: /docs/user_guide/administrative/app_settings/manage_your_braze_users/teams/
  image: /assets/img/braze_icons/users-01.svg
---

## Quelles sont les différences entre les équipes, les jeux de permissions et les rôles ? 

Vous pouvez utiliser l'équipe, les jeux de permissions et les rôles d'utilisateur pour gérer l'accès et les responsabilités des utilisateurs du tableau de bord au sein de Braze. Chaque fonctionnalité englobe un ensemble différent d'autorisations et de contrôles d'accès.

### Différences clés

De manière générale, chaque fonctionnalité a une portée différente :
- Les jeux de permissions contrôlent ce que les utilisateurs du tableau de bord peuvent faire dans tous les espaces de travail.
- Les rôles contrôlent ce que les utilisateurs du tableau de bord peuvent faire dans des espaces de travail spécifiques.
- Les Teams contrôlent les audiences auxquelles les utilisateurs du tableau de bord peuvent envoyer des messages.

| Fonctionnalité | Ce que vous pouvez faire
| - | - |
| [Ensembles d’autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) | Regroupez les autorisations liées à des domaines ou à des actions spécifiques (comme pour les « développeurs  et les « marketeurs »), puis appliquez-les aux utilisateurs du tableau de bord qui ont besoin des mêmes autorisations dans différents espaces de travail. |
| [Rôles]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) | Regroupez les autorisations personnalisées individuelles et les contrôles d'accès à l'espace de travail dans des rôles prédéfinis (tels que "Marketeur - Marques de mode" et "Marketeur - Marques de soins"), puis attribuez un rôle aux utilisateurs du tableau de bord afin de leur accorder directement l'accès à l'espace de travail et les autorisations correspondantes. |
| [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) | Limiter l'accès des utilisateurs du tableau de bord aux ressources en fonction de l'audience (comme l'emplacement/localisation de la base de clients, la langue et les attributs personnalisés). |
{: .reset-td-br-1 .reset-td-br-2 }