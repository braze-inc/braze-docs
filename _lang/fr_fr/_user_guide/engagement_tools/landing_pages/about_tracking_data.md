---
nav_title: À propos des données de suivi
article_title: "À propos des données de suivi des pages d'atterrissage"
description: "Découvrez le suivi et les données anonymisées pour les pages d'atterrissage dans Braze."
page_order: 10
alias: /landing_pages/data_tracking/
---

# À propos des données de suivi des pages d'atterrissage

> Découvrez le suivi et les données anonymisées pour les pages d'atterrissage dans Braze.

## Méthodes de suivi

### Web SDK

Le SDK web de Braze n'est initialisé que lorsqu'un utilisateur soumet un formulaire sur la page de renvoi. Avant la soumission du formulaire, aucune donnée personnelle n'est collectée et le SDK ne suit pas activement les utilisateurs. Une fois l'initialisation terminée, le SDK ne stocke aucune donnée dans le navigateur (comme les cookies, le stockage local ou autres).

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

Braze ne fusionne pas automatiquement les utilisateurs en fonction d'attributs, tels que l'e-mail ou le téléphone, lorsqu'un formulaire de page d'atterrissage est soumis. Si un formulaire est soumis avec un e-mail ou un numéro de téléphone qui correspond à un profil utilisateur existant, Braze crée un profil utilisateur distinct.

Pour fusionner des profils utilisateurs en double, vous pouvez :

- Déclenchez l'[endpoint`/users/merge` ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) lorsqu'un formulaire de page d'atterrissage est soumis pour fusionner le nouveau profil avec un profil existant.
- Planifiez la [fusion en bloc]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging) pour fusionner périodiquement les profils en double sur la base des identifiants correspondants.

