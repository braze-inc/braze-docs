---
nav_title: Janvier
page_order: 12
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour janvier 2018."
---

# Janvier 2018

## CSS inlining

Vous pouvez maintenant activer/désactiver [CSS Inlining][84] pour les messages électroniques individuels - faites-le depuis [votre page des paramètres de messagerie][83].

## Nouveaux filtres de segment

Vous pouvez maintenant créer des segments en utilisant les filtres suivants :
- Étape de la toile reçue
- Étape de la toile ouverte/cliquée
- Dernière étape de Canvas Spécifique Reçu

{% alert update %}
As of March 2019, `Received Canvas Step` has been renamed to `Received Message from Canvas Step`, and `Last Received Specific Canvas Step` has been renamed to `Last Received Message from Specific Canvas Step`.
{% endalert %}

## Exportation des utilisateurs en utilisant l'ID de l'appareil

Ce point de terminaison accepte maintenant un identifiant de périphérique en tant que paramètre, ce qui vous permet de [exporter des profils d'utilisateurs anonymes][82].

Vous pouvez utiliser l'ID de l'appareil pour exporter tous les profils d'utilisateurs sur ce périphérique.

## Mise à jour des rapports d'engagement

Des statistiques supplémentaires, comme **le taux d'ouverture push** et **le taux de conversion**, sont [maintenant disponibles dans les rapports][81].

## Certificats push Apple : utilisation de fichiers .p8

Vous pouvez maintenant utiliser un fichier [.p8][80] lorsque vous téléchargez un certificat Push Apple. Assurez-vous que vos identifiants de push iOS n'expireront jamais.


[80]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens
[81]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports
[82]: {{site.baseurl}}/developer_guide/rest_api/export/#users-by-identifier-endpoint
[83]: https://dashboard-01.braze.com/app_settings/app_settings/email/
[84]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/#css-inlining
