---
nav_title: Février
page_order: 11
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour février 2018."
---

# Février 2018

## Nombre de badges de push iOS

Vous pouvez maintenant [mettre à jour le nombre de badges][89] dans le compositeur push de Braze. Pour chaque message push, vous pouvez spécifier quel nombre de badges ces déclencheurs de notification.

## Exportation des utilisateurs via API en utilisant des adresses e-mail

Vous pouvez maintenant [exporter les données du profil utilisateur via l'API][88] en spécifiant les adresses e-mail. Cet export inclut tous les profils associés à cette adresse e-mail.

## API du modèle d'e-mail

Vous pouvez maintenant créer et mettre à jour des modèles d'e-mail [via l'API][87]. Chaque modèle aura un **email_template_id** qui peut être référencé dans d'autres appels API.

## Autorisations des clés API REST

Vous pouvez maintenant créer [plusieurs clés API REST][86] et configurer les autorisations d'accès pour chacune. Chaque clé peut être configurée pour donner accès à certains terminaux.

Vous pouvez également spécifier une liste [blanche d'adresses IP][85] et de sous-réseaux autorisés à faire des requêtes d'API REST pour une clé d'API REST donnée.

[85]: {{site.baseurl}}/developer_guide/rest_api/basics/#api-ip-whitelisting
[86]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[87]: {{site.baseurl}}/developer_guide/rest_api/email_templates/#email-templates
[88]: {{site.baseurl}}/developer_guide/rest_api/export/#user-export
[89]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#utilizing-badge-count
