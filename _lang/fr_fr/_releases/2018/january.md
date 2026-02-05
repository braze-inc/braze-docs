---
nav_title: janvier
page_order: 12
noindex: true
page_type: update
description: "Cet article contient les notes de version de janvier 2018."
---
# Janvier 2018

## Inclusion CSS

Vous pouvez maintenant activer ou désactiver [l'intégration CSS]({{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/#css-inlining) pour des messages électroniques individuels en allant dans vos **Paramètres de messagerie**.

## Nouveaux filtres pour la segmentation

Vous pouvez maintenant créer des segments en utilisant les filtres suivants :
- Étape de Canvas reçue
- Étape de Canvas ouverte/cliquée
- Dernière étape de Canvas spécifique reçue

{% alert update %}
En mars 2019, `Received Canvas Step` a été renommé `Received Message from Canvas Step`, et `Last Received Specific Canvas Step` a été renommé `Last Received Message from Specific Canvas Step`.
{% endalert %}

## Exportation des utilisateurs via l’ID d’appareil

Ce point de terminaison accepte désormais un identifiant de périphérique en tant que paramètre, ce qui vous permet [d'exporter des profils d'utilisateurs anonymes]({{site.baseurl}}/developer_guide/rest_api/export/#users-by-identifier-endpoint).

Vous pouvez utiliser l’ID d’appareil pour exporter tous les profils utilisateur présents sur un appareil.

## Mise à jour des rapports d'engagement

Des statistiques supplémentaires, comme le **taux d'ouverture des push** et le **taux de conversion**, sont désormais disponibles dans les [rapports d'engagement]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports).

## Certificats push pour Apple : Utilisation des fichiers.p8

Vous pouvez maintenant utiliser un fichier [p8]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens) lors du téléchargement d'un certificat Apple Push, garantissant que vos identifiants push iOS ne seront jamais expirés.


