---
nav_title: Gestion des utilisateurs
article_title: LINE Gestion des utilisateurs
page_order: 0
description: "Cet article traite de l'ID utilisateur LINE et de la manière de le définir."
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# LINE gestion des utilisateurs

> L'ID de l'utilisateur LINE est stocké dans l'attribut du profil utilisateur appelé `native_line_id`, qui est utilisé pour envoyer des messages à un utilisateur sur le canal de communication LINE. Cet article explique comment définir et rechercher l'attribut `native_line_id`.

Les données utilisateur du client sont conseillées dans un [profil utilisateur Braze]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/). Un profil utilisateur stocke des informations et des attributs sur les utilisateurs d'une entreprise, tels que les prénoms et les adresses e-mail. 

Lorsque vous envoyez des messages LINE par l'intermédiaire de Braze, Braze utilise l'attribut `native_line_id` pour identifier les utilisateurs auxquels envoyer le message. Lorsque LINE envoie des événements webhook Braze, par exemple lorsqu'un utilisateur suit un canal ou répond à un message, le site `native_line_id` est utilisé pour rechercher le profil utilisateur correspondant.

{% alert note %}
Les ID des utilisateurs de LINE sont distincts selon le fournisseur de LINE. Un utilisateur spécifique aura des ID d'utilisateur LINE différents pour chaque fournisseur qu'il suit. Il est peu probable que les utilisateurs connaissent leur ID LINE (contrairement à leur e-mail ou à leur numéro de téléphone), car ils changent pour chaque marque qu'ils suivent.
{% endalert %}

## Définition de l'attibute `native_line_id` 

Il existe un certain nombre de scénarios dans lesquels `native_line_id` est défini sur le profil utilisateur, qui sont décrits ci-dessous.

| Scénario | S'il existe un profil utilisateur avec `native_line_id` | Résultats |
| --- | --- | --- |
|Un utilisateur suit un canal LINE | Non| Un profil utilisateur anonyme est créé (une fusion sera nécessaire) :<br> - `native_line_id` est réglé sur l'ID de ligne de l'utilisateur <br>- `line_id` l'alias d'utilisateur est défini sur l'ID de ligne de l'utilisateur<br>\- L'utilisateur est abonné au groupe d'abonnement Braze de la chaîne. |
|Un utilisateur suit un canal LINE| Oui | Tous les profils utilisateurs avec l'adresse `native_line_id`:<br>\- Sont abonnés au groupe d'abonnement Braze de la chaîne.|
|L'entreprise utilise le téléchargement CSV de l'utilisateur avec une colonne`ative_line_id` | Non| Si aucun profil utilisateur n'existe pour l'adresse `external_id` ou l'alias d'utilisateur spécifié :<br>- `native_line_id` est réglé sur la valeur spécifiée<br> \- Tous les autres attributs spécifiés dans le CSV sont définis dans le profil utilisateur.|
|L'entreprise utilise le téléchargement CSV de l'utilisateur avec une colonne `native_line_id`  | Oui | S'il existe un profil utilisateur pour l'adresse `external_id` ou l'alias d'utilisateur spécifié :<br>- `native_line_id` est réglé sur la valeur spécifiée<br>\- Tous les autres attributs spécifiés dans le CSV sont définis dans le profil utilisateur.<br>\- Plusieurs profils ont le même `native_line_id` |
| L'entreprise utilise l'endpoint `/users/track` et spécifie l'attribut `native_line_id`  | Non | S'il n'existe pas de profil utilisateur pour l'utilisateur spécifié[(spécifié par `external_id`, `user_alias`, `braze_id` ou `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)) :<br>- `native_line_id` est réglé sur la valeur spécifiée<br>\- Tous les autres attributs spécifiés dans la demande sont définis dans le profil utilisateur. |
| L'entreprise utilise l'endpoint `/users/track` et spécifie l'attribut `native_line_id`  | Oui | S'il existe un profil utilisateur pour l'utilisateur spécifié[(spécifié par `external_id`, `user_alias`, `braze_id` ou `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)) :<br>- `native_line_id` est réglé sur la valeur spécifiée<br>\- Tous les autres attributs spécifiés dans la demande sont définis dans le profil utilisateur.<br>\- Plusieurs profils ont le même `native_line_id` |
| L'entreprise demande à Braze de gérer la synchronisation de l'état des abonnements | Non | Si LINE renvoie un ID d'utilisateur qui n'a pas de profil utilisateur correspondant dans Braze, un profil utilisateur anonyme est créé :<br>- `native_line_id` est réglé sur l'ID de ligne de l'utilisateur<br>- `line_id` l'alias d'utilisateur est défini sur l'ID de ligne de l'utilisateur<br>\- L'utilisateur est abonné au groupe d'abonnement Braze de la chaîne.<br><br>Notez que si un utilisateur ayant le même ID LINE est créé ultérieurement, il y aura des utilisateurs en double, mais tous deux auront le statut d'abonnement LINE correct. Dans ce cas, la fusion d'utilisateurs permet d'assainir votre base d'utilisateurs. |
| L'entreprise demande à Braze de gérer la synchronisation de l'état des abonnements | Oui | Si un ID d'utilisateur est renvoyé par LINE et qu'il existe un profil utilisateur correspondant dans Braze :<br>\- L'utilisateur est abonné au groupe d'abonnement Braze de la chaîne. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

## Trouver le `native_line_id`

Lorsque vous consultez un profil utilisateur dans le tableau de bord de Braze, vous pouvez voir si l'attribut `native_line_id` y est défini en vous rendant dans l'onglet **Engagement** > section **Paramètres de contact** > section **LINE.** 

Si l'adresse `native_line_id` a été définie, elle sera affichée sous **LINE User ID.** Sinon, il n'apparaîtra pas.

\![Ligne Paramètres de contact dans l'onglet Engagement.]({% image_buster /assets/img/line/line_contact_settings.png %}){: style="max-width:50%;"}

