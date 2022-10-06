---
nav_title: Février
page_order: 11
noindex: true
page_type: update
description: "Cet article contient les notes de version de février 2018."
---
# Février 2018

## Compteur de badges push iOS

Vous pouvez maintenant [mettre à jour le nombre de badges][89] dans le compositeur de Push de Braze.
Pour chaque message push, vous pouvez spécifier le badge qui déclenche les déclencheurs de notification.

## Exportation des utilisateurs via API avec les adresses e-mail

Vous pouvez maintenant [exporter des données de profil utilisateur via API][88] en spécifiant les adresses e-mail.
Cette exportation inclut tous les profils associés à l’adresse e-mail en question.

## Modèles d’e-mail via API

Vous pouvez maintenant créer et mettre à jour les [modèles de courrier électronique via l’API][87]. Chaque modèle aura un **email_template_id** qui peut être référencé dans d’autres appels API.

## Autorisations des clés API REST

Vous pouvez maintenant créer des [clés API REST][86] multiples et configurer les autorisations d’accès pour chacune d’elles. Chaque clé peut être configurée pour accorder l’accès à certains endpoints.

Vous pouvez spécifier une [liste d’adresses IP et de sous-réseaux autorisés][85] à faire des requêtes API REST pour une clé API REST spécifique.

[85]: {{site.baseurl}}/developer_guide/rest_api/basics/#api-ip-whitelisting
[86]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[87]: {{site.baseurl}}/developer_guide/rest_api/email_templates/#email-templates
[88]: {{site.baseurl}}/developer_guide/rest_api/export/#user-export
[89]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#utilizing-badge-count
