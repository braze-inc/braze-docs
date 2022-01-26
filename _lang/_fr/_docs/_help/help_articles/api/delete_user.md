---
nav_title: Suppression des utilisateurs via l'API
article_title: Suppression des utilisateurs via l'API
page_order: 0
page_type: Référence
description: "Cet article décrit les implications de la suppression d'un profil utilisateur via l'API REST de Braze."
tool: Tableau de bord
platform: API
---

# Suppression des utilisateurs via l'API

Lorsque vous [supprimez un utilisateur via l'API REST de Braze]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint), cela se produit :

- Le nombre d'utilisateurs à vie (c'est-à-dire "Utilisateurs") sera mis à jour pour tenir compte des utilisateurs nouvellement supprimés.
- L'ensemble du profil de l'utilisateur sera supprimé.
- L'utilisateur supprimé sera toujours compté dans le pourcentage de conversion agrégé.

Le nombre d’événements personnalisés et le nombre d’achats ne seront pas mis à jour pour les utilisateurs supprimés.

_Dernière mise à jour le 8 octobre 2019_