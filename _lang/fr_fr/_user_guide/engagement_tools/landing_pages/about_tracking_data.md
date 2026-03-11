---
nav_title: À propos du suivi des données
article_title: "À propos des données de suivi des pages d'atterrissage"
description: "Découvrez le suivi et les données anonymisées pour les pages d'atterrissage dans Braze."
page_order: 10
alias: /landing_pages/data_tracking/
---

# À propos des données de suivi des pages d'atterrissage

> Découvrez le suivi et les données anonymisées pour les pages d'atterrissage dans Braze.

## Méthodes de suivi

### Web SDK

Le SDK Web Braze est initialisé lorsqu'un utilisateur soumet un formulaire sur une page d'accueil. Avant la soumission du formulaire, aucune donnée personnelle n'est collectée et le SDK ne suit pas activement les utilisateurs. Une fois l'initialisation terminée, le SDK ne stocke aucune donnée dans le navigateur (comme les cookies, le stockage local ou autres). 

Le SDK Web Braze est initialisé immédiatement lorsqu'un utilisateur accède à la page de destination via un lien généré par une étiquette{% raw %}`{% landing_page_url %}`{% endraw %} Liquid dans un message Braze.

Lorsqu'un formulaire est soumis, le SDK recueille les données suivantes :

- Événement de soumission du formulaire (nom de l'événement et heure de soumission)
- Données spécifiées par votre équipe dans le formulaire (telles que le nom, l'e-mail et le numéro de téléphone).
- Heure de début de la session
- ID de l'appareil (un ID unique généré, mais non stocké, pour l'appareil)
- Pays déterminé par l'adresse IP

### Données anonymes

Avant qu'un utilisateur ne soumette un formulaire, les données suivies sur une page de renvoi sont uniquement constituées d'informations anonymes et non identifiables. Il s'agit d'indicateurs globaux standard pour les sites web, comme le nombre de pages vues (impressions) et de clics qu'une page de renvoi reçoit.

Ces données n'étant pas liées à des utilisateurs identifiables, elles ne peuvent pas être utilisées pour recibler ou suivre le comportement d'utilisateurs individuels.

## Fusion de profils utilisateurs dupliqués

Braze ne fusionne pas automatiquement les utilisateurs en fonction d'attributs tels que l'e-mail ou le numéro de téléphone lorsqu'un formulaire de page de destination est soumis. Si un formulaire est soumis avec une adresse e-mail ou un numéro de téléphone correspondant à un profil utilisateur existant, Braze crée un profil utilisateur distinct.

Pour fusionner des profils utilisateurs en double, vous pouvez :

- Veuillez utiliser le déclencheur de[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)[l'endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) lorsqu'un formulaire de page de destination est soumis afin de fusionner le nouveau profil avec un profil existant.
- Effectuez la planification [de la fusion groupée]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging) afin de fusionner périodiquement les profils en double en fonction des identifiants correspondants.

