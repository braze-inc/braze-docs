---
nav_title: Janvier
page_order: 12
noindex: true
page_type: update
description: "Cet article contient les notes de version de janvier 2018."
---
# Janvier 2018

## Inlining CSS

Vous pouvez maintenant basculer l’[insertion CSS][84] pour des messages individuels en allant dans la section **Email Settings (Paramètres des e-mails)**.

## Nouveaux filtres pour la segmentation

Vous pouvez maintenant créer des segments en utilisant les filtres suivants :
- Canvas Step eçue
- Canvas Step ouverte/cliquée
- Dernière Canvas Step spécifique reçue

{% alert update %}
En mars 2019, `Received Canvas Step` a été renommé `Received Message from Canvas Step`, et `Last Received Specific Canvas Step` a été renommé `Last Received Message from Specific Canvas Step`.
{% endalert %}

## Exportation des utilisateurs via l’ID d’appareil

Cet endpoint accepte désormais un identifiant d’appareil en tant que paramètre, ce qui vous permet d’[exporter des profils utilisateur anonymes][82].

Vous pouvez utiliser l’ID d’appareil pour exporter tous les profils utilisateur présents sur un appareil.

## Mise à jour des Engagement Reports

Des statistiques supplémentaires, telles que **le taux d’ouverture des notification push** et le **taux de conversion** sont maintenant disponibles dans les [Engagement Reports.][81] (Rapports d’engagement).

## Certificats push pour Apple : Utilisation des fichiers.p8

Vous pouvez désormais utiliser un [fichier p8][80] lors du chargement d’un certificat Apple Push, vous assurant que vos identifiants de notification push iOS n’expireront jamais.


[80]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens
[81]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports
[82]: {{site.baseurl}}/developer_guide/rest_api/export/#users-by-identifier-endpoint
[84]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/#css-inlining
