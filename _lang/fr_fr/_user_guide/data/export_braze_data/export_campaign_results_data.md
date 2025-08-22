---
nav_title: Exporter les données de campagne
article_title: Exporter les données de campagne
page_order: 0
page_type: reference
description: "Cet article de référence explique comment exporter les données de résultats de la campagne à partir de campagnes uniques, multicanales ou multivariées. L’article indique également comment exporter les données utilisateur des destinataires."
tool: 
  - Campaigns
  - Reports
  
---

# Exporter les données de campagne

> Depuis la page **Campagnes** du tableau de bord, sélectionnez la campagne que vous souhaitez consulter et faites défiler vers le bas jusqu'aux graphiques de performances historiques, qui peuvent être exportés.<br><br>Cette page explique comment exporter les données de résultats de campagnes uniques, multicanales et multivariées, et comment exporter les données des utilisateurs des destinataires.

## Campagnes multicanales

Pour les campagnes multicanales, les données qui peuvent être exportées dépendent des canaux d'envoi de messages que vous avez utilisés. Voici une liste de toutes les données pouvant être exportées à partir d’une campagne qui a utilisé la notification push iOS, notification push Android, l’E-mail et les messages in-app :

- Messages envoyés par date
    - Total des messages envoyés
    - Messages envoyés à travers les canaux de la campagne (peut inclure les messages push, les e-mails et les messages in-app).
- Engagement par message e-mail par date
    - Nombre d’e-mails livrés
    - Nombre d’e-mails envoyés
    - Nombre d’e-mails ouverts
    - Nombre d’e-mails cliqués
    - Nombre de rebonds (bounce) d’e-mail
    - Nombre d’e-mails signalés comme spam
- Engagement sur les messages in-app par date
    - Nombre de messages in-app envoyés
    - Impressions du in-app Message
    - Nombre de clics sur les messages in-app
- Engagement de notification push iOS par date
    - Nombre de notifications Push iOS envoyées
    - Nombre total d’ouvertures
    - Ouvertures directes
    - Rebonds
- Engagement sur les notifications push Android par date
    - Nombre de notifications Push Android envoyées
    - Nombre total d’ouvertures
    - Ouvertures directes
    - Rebonds

## Campagnes multivariées

Pour les campagnes multivariées, qui n'utilisent qu'un seul canal de messages, vous pouvez exporter des données qui montrent les performances de chaque variante sur les analyses du canal de messages spécifique au fil du temps. Vous pouvez afficher ces données groupées par statistique ou groupées par variante de message.

Les résultats de campagne de notification push contiennent des graphiques pour les analyses suivantes :

- Messages envoyés par date pour chaque variante
- Conversions par date pour chaque variante
- Destinataires uniques par date pour chaque variante
- Ouvertures par date pour chaque variante
- Ouvertures directes par date pour chaque variante
- Bounces par date pour chaque variante

Les résultats de campagne d’e-mail contiennent des graphiques pour les analyses suivantes :

- Quantité livrée par date pour chaque variante
- Quantité envoyée par date pour chaque variante
- Ouvertures par date pour chaque variante
- Clics par date pour chaque variante
- Bounces par date pour chaque variante
- Signalements de courrier indésirable par date pour chaque variante

Les résultats de campagne de messages in-app contiennent des graphiques pour les analyses suivantes :

- Envoyé par date pour chaque variante
- Impressions par date pour chaque variante
- Clics par date pour chaque variante

## Destinataires de la campagne

Vous pouvez exporter des données utilisateur pour tous les destinataires d’une campagne dans un fichier CSV. Pour ce faire, sélectionnez le bouton **Données utilisateur** dans la section **Détails de la campagne**.

{% alert note %}
Le bouton **Données utilisateur** n’apparaît pas ? Pour exporter les données utilisateur, vous avez besoin des [autorisations]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) **Exporter les données utilisateur** pour cet espace de travail.
{% endalert %}

![Liste déroulante des données de l'utilisateur sur la page des détails de la campagne]({% image_buster /assets/img/campaign_export_example.png %})

La sortie CSV contient des données de profil utilisateur pour chaque destinataire de la campagne. Braze génère le rapport en arrière-plan et l’envoie par e-mail à l’utilisateur actuellement connecté.

Si vous avez lié vos [identifiants Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) à Braze, le fichier CSV sera également téléchargé dans votre compartiment S3. Sinon, le lien envoyé par e-mail expirera au bout de quelques heures.

Le fichier exporté comprend les mêmes champs de données utilisateur que ceux inclus lorsque vous [exportez les données utilisateur d'un segment.]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data) En plus des champs de données, si vous choisissez « Exporter toutes les données du destinataire », le fichier exporté contiendra également les données suivantes pour chaque utilisateur :

- Nom de la variation de campagne reçue
- ID API de la variation de campagne reçue
- Si l’utilisateur est dans le groupe de contrôle

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez la [résolution des problèmes d'exportation.]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)
{% endalert %}

