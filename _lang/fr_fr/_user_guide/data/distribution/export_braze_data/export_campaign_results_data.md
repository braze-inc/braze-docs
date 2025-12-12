---
nav_title: Exporter les données de la campagne
article_title: Exporter les données de la campagne
page_order: 0
page_type: reference
description: "Cet article de référence explique comment exporter les données de résultats de campagnes uniques, multicanales ou multivariées. L'article indique également comment exporter les données des destinataires."
tool: 
  - Campaigns
  - Reports
  
---

# Exporter les données de la campagne

> Dans la page **Campagnes** du tableau de bord, sélectionnez la campagne que vous souhaitez consulter et faites défiler vers le bas jusqu'aux graphiques de performances historiques, qui peuvent être exportés.<br><br>Cette page explique comment exporter les données de résultats de campagnes uniques, multicanales et multivariées, et comment exporter les données des utilisateurs des destinataires.

## Campagnes multicanal

Pour les campagnes multicanales, les données qui peuvent être exportées dépendent des canaux d'envoi de messages que vous avez utilisés. Voici une liste de toutes les données qui peuvent être exportées d'une campagne qui a utilisé le push iOS, le push Android, l'e-mail et les messages in-app :

- Messages envoyés par date
    - Total des messages envoyés
    - Messages envoyés à travers les canaux de la campagne (peut inclure les messages push, les e-mails et les messages in-app).
- Engagement des messages e-mail par date
    - Nombre d'e-mails délivrés
    - Nombre d'e-mails envoyés
    - Nombre d'e-mails ouverts
    - Nombre de clics sur l'e-mail
    - Nombre d'e-mails rejetés
    - Nombre d'e-mails signalement de courrier indésirable
- Engagement des messages in-app par date
    - Nombre de messages in-app envoyés
    - Impressions des messages in-app
    - Nombre de clics sur les messages in-app
- Engagement de Push iOS par date
    - Nombre de notifications push iOS envoyées
    - Total des ouvertures
    - Ouvertures directes
    - Rebonds
- Engagement Push Android par date
    - Nombre de notifications push Android envoyées
    - Total des ouvertures
    - Ouvertures directes
    - Rebonds

## Campagnes multivariées

Pour les campagnes multivariées, qui n'utilisent qu'un seul canal de messages, vous pouvez exporter des données qui montrent les performances de chaque variante sur les analyses du canal de messages spécifique au fil du temps. Vous pouvez consulter ces données regroupées par statistiques ou par variante de message.

Les résultats de la campagne Push contiennent des graphiques pour les analyses/analytiques suivantes :

- Messages envoyés par date pour chaque variante
- Conversions par date pour chaque variante
- Destinataires uniques par date pour chaque variante
- Ouvertures par date pour chaque variante
- Ouvertures directes par date pour chaque variante
- Rebonds par date pour chaque variante

Les résultats des campagnes d'e-mail contiennent des graphiques pour les analyses/analytiques suivantes :

- Nombre de livraisons par date pour chaque variante
- Nombre d'envois par date pour chaque variante
- Ouvertures par date pour chaque variante
- Clics par date pour chaque variante
- Rebonds par date pour chaque variante
- Signalement de courrier indésirable par date pour chaque variante

Les résultats des campagnes de messages in-app contiennent des graphiques pour les analyses/analytiques suivantes :

- Envoi par date pour chaque variante
- Impressions par date pour chaque variante
- Clics par date pour chaque variante

## Destinataires de la campagne

Vous pouvez exporter les données des utilisateurs pour tous les destinataires d'une campagne sous la forme d'un fichier CSV. Pour ce faire, sélectionnez le bouton **Données utilisateur** dans la section **Détails de la campagne.** 

{% alert note %}
Vous ne voyez pas le bouton **Données de l'utilisateur**? Pour exporter des données utilisateur, vous devez disposer des [autorisations d']({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) **exportation de données utilisateur** pour cet espace de travail.
{% endalert %}

!liste déroulante Données de l'utilisateur sur la page Détails de la campagne]({% image_buster /assets/img/campaign_export_example.png %})

Le fichier CSV contient les données relatives au profil utilisateur de chaque destinataire de la campagne. Braze génère le rapport en arrière-plan et l'envoie par e-mail à l'utilisateur actuellement connecté.

Si vous avez lié vos [identifiants Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) à Braze, le CSV sera également téléchargé dans votre compartiment S3. Dans le cas contraire, le lien qui vous a été envoyé par e-mail expirera dans quelques heures.

Le fichier exporté comprend les mêmes champs de données utilisateur que ceux qui sont inclus lorsque vous [exportez les données utilisateur d'un segment.]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data) En plus de ces champs de données, si vous choisissez "Exporter toutes les données des destinataires", le fichier exporté contiendra également les données suivantes pour chaque utilisateur :

- Nom de la campagne Variation reçue
- ID API de la variation de campagne reçue
- Si l'utilisateur fait partie du groupe de contrôle

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez la [résolution des problèmes d'exportation.]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)
{% endalert %}

