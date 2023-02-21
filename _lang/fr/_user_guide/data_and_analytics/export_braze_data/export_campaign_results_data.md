---
nav_title: Exporter les données de campagne
article_title: Exporter les données de campagne
page_order: 0
page_type: reference
description: "Cet article de référence explique comment exporter une analyse de campagne."
tool: 
  - Campagnes
  - Rapports
  
---

# Données de résultats de la campagne

Toutes les analyses de vos campagnes Braze peuvent être exportées vers un fichier CSV. Sur la page **Campagnes** du tableau de bord, sélectionnez la campagne que vous souhaitez afficher et faites défiler jusqu’aux graphiques de performance historiques, qui peuvent être exportés.

## Campagnes multicanaux

Pour les campagnes multicanaux, les données qui peuvent être exportées dépendront des canaux de communication utilisés. Voici une liste de toutes les données pouvant être exportées à partir d’une campagne qui a utilisé la notification push iOS, notification push Android, l’E-mail et les messages in-app.

- Messages envoyés par date
    - Total des messages envoyés
    - Messages envoyés sur les canaux de campagne (peut inclure des messages de notification push, e-mail et messages in-app)
- Engagement par message e-mail par date
    - Nombre d’e-mails livrés
    - Nombre d’e-mails envoyés
    - Nombre d’e-mails ouverts
    - Nombre d’e-mails cliqués
    - Nombre d’e-mails en échec (bounces)
    - Nombre d’e-mails signalés comme spam
- Engagement sur les messages in-app par date
    - Nombre de messages In-App envoyés
    - Impressions de messages In-App
    - Nombre de clics sur les messages in-app 
- Engagement de notification push iOS par date
    - Nombre de notifications Push iOS envoyées
    - Total des ouvertures
    - Ouvertures directes
    - Bounces
- Engagement sur les Push Android par date
    - Nombre de notifications Push Android envoyées
    - Total des ouvertures
    - Ouvertures directes
    - Bounces

## Campagnes multivariées

Pour les campagnes multivariées qui utilisent un seul canal, vous pourrez exporter des données qui montrent la performance dans le temps de chaque variante dans les analyses d’un canal spécifique. Vous pouvez afficher ces données groupées par statistique ou groupées par variante de message.

Les résultats de campagne Push contiennent des graphiques pour les analyses suivantes :

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
- Signalements spam par date pour chaque variante

Les résultats de campagne de messages in-app contiennent des graphiques pour les analyses suivantes :

- Envoyé par date pour chaque variante
- Impressions par date pour chaque variante
- Clics par date pour chaque variante

## Destinataires de la campagne

Vous pouvez exporter des données utilisateur pour tous les destinataires d’une campagne dans un fichier CSV. Pour ce faire, cliquez sur le bouton **Données utilisateur** dans le bloc **Détails de la campagne**.

{% alert note %}
Vous ne voyez pas le bouton **Données utilisateur** ? Pour exporter les données utilisateur, vous devez avoir la [permission]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) d’**Exporter les données utilisateur** pour ce groupe d’apps.
{% endalert %}

![Menu déroulant Données utilisateur sur la page Détails de la campagne][6]

La sortie CSV contient des données de profil utilisateur pour chaque destinataire de la campagne. Braze génère le rapport en arrière-plan et l’envoie par e-mail à l’utilisateur actuellement connecté.

Si vous avez indiqué vos [informations d’identification Amazon S3][26] dans Braze, le CSV sera également chargé dans votre compartiment S3. Sinon, le lien envoyé par e-mail expirera au bout de quelques heures.

Le fichier exporté inclut les mêmes champs de données utilisateur que ceux qui sont inclus quand vous [exportez les données utilisateur d’un segment][40]. En plus des champs de données, si vous choisissez « Exporter toutes les données du destinataire », le fichier exporté contiendra également les données suivantes pour chaque utilisateur :

- Nom de la variation de campagne reçue
- ID API de la variation de campagne reçue
- Si l’utilisateur est dans le groupe de contrôle

{% alert tip %}
Pour obtenir de l’aide sur les exportations de CSV et l’API, consultez notre article [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

[6]: {% image_buster /assets/img/campaign_export_example.png %}
[26]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/
[40]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data
