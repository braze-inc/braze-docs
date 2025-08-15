---
nav_title: février
page_order: 11
noindex: true
page_type: update
description: "Cet article contient les notes de version de février 2018."
---
# Février 2018

## Compteur de badges push iOS

Vous pouvez désormais [mettre à jour le nombre de badges]({{site.baseurl}}/help/best_practices/utilizing_badge_count/#utilizing-badge-count) dans le compositeur de push depuis Braze.
Pour chaque message push, vous pouvez spécifier le badge qui déclenche les déclencheurs de notification.

## Exportation des utilisateurs via API avec les adresses e-mail

Vous pouvez désormais [exporter les données du profil utilisateur via l'API]({{site.baseurl}}/developer_guide/rest_api/export/#user-export) en spécifiant les adresses e-mail.
Cette exportation inclut tous les profils associés à l’adresse e-mail en question.

## Modèles d’e-mail via API

Vous pouvez désormais créer et mettre à jour des [modèles d'e-mail via l'API]({{site.baseurl}}/developer_guide/rest_api/email_templates/#email-templates). Chaque modèle aura un identifiant **email_template_id** qui peut être référencé dans d'autres appels de l’API.

## Autorisations des clés API REST

Vous pouvez désormais créer [plusieurs clés API REST]({{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys) et configurer les autorisations d'accès pour chacune d'entre elles. Chaque clé peut être configurée pour accorder l’accès à certains endpoints.

Vous pouvez également spécifier une [liste blanche d'adresses IP]({{site.baseurl}}/developer_guide/rest_api/basics/#api-ip-whitelisting) et de sous-réseaux autorisés à effectuer des requêtes API REST pour une clé API REST donnée.

