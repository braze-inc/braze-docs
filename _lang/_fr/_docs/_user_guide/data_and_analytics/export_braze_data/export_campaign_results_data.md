---
nav_title: Exporter les résultats de la campagne
article_title: Exporter les résultats de la campagne
page_order: 0
page_type: Référence
description: "Cet article de référence couvre la manière d'exporter les analyses de campagne."
tool:
  - Campagnes
  - Rapports
---

# Données des résultats de la campagne

Toutes les analyses de vos campagnes Braze peuvent être exportées vers un CSV. À partir de la page **Campagnes** du tableau de bord, sélectionnez la campagne que vous souhaitez afficher et faire défiler vers le bas les graphiques de performance historiques, qui peuvent être exportés.

## Campagnes multi-canaux

Pour les campagnes multi-canaux, les données qui peuvent être exportées dépendront des canaux de messagerie utilisés. Voici une liste de toutes les données qui peuvent être exportées à partir d'une campagne qui a utilisé iOS push, push Android, e-mail et messages dans l'application:

- Messages envoyés par date
    - Total des messages envoyés
    - Messages envoyés à travers les canaux de campagne (peut inclure Push, Email et Message In-Apple)
- Envoyer un message par date
    - Nombre d'E-mails envoyés
    - Nombre d'emails envoyés
    - Nombre d'e-mails ouverts
    - Nombre de clics de courriel
    - Nombre d'emails Bounces
    - Nombre d'emails signalés comme spam
- In-App Message Engagement par Date
    - Nombre de messages envoyés dans l'application
    - Impressions de message dans l'application
    - Nombre de Clics de Message In-App
- Engagement de Push iOS par date
    - Nombre de notifications envoyées pour iOS
    - Ouvertures totales
    - Ouvertures directes
    - Bounces
- Engagement Android par date
    - Nombre de notifications envoyées sur Android
    - Ouvertures totales
    - Ouvertures directes
    - Bounces
- Engagement de poussée de Windows Phone 8 par date
    - Nombre de notifications push envoyées par Windows Phone 8
    - Ouvertures totales
    - Ouvertures directes
    - Bounces

## Campagnes multivariées

Pour les campagnes multivariées, qui utilisent un seul canal de messagerie, vous serez en mesure d'exporter des données qui montrent comment chaque variante effectuée sur les analytiques du canal de messagerie spécifique au fil du temps. Vous pouvez consulter ces données regroupées par statistiques ou regroupées par variante de message.

Les résultats des campagnes push contiennent des graphiques pour les analyses suivantes :

- Messages envoyés par date pour chaque variante
- Conversions par date pour chaque variante
- Destinataires uniques par date pour chaque variante
- Ouvre par date pour chaque variante
- Ouverture directe par date pour chaque variante
- Bounces par date pour chaque variante

Les résultats de la campagne contiennent des graphiques pour les analyses suivantes :

- Nombre livré par date pour chaque variante
- Nombre envoyé par date pour chaque variante
- Ouvre par date pour chaque variante
- Clics par date pour chaque variante
- Bounces par date pour chaque variante
- Rapports de spam par date pour chaque variante

Les résultats de la campagne de messages intégrés contiennent des graphiques pour les analyses suivantes :

- Envoyé par date pour chaque variante
- Impressions par date pour chaque variante
- Clics par date pour chaque variante

## Destinataires de la campagne

Vous pouvez exporter les données utilisateur pour tous les destinataires d'une campagne en tant que fichier CSV. Pour ce faire, cliquez sur le bouton __Données utilisateur__ dans le bloc __Détails de la campagne__.

{% alert note %}
Vous ne pouvez pas voir le bouton **Données utilisateur**? Pour exporter les données utilisateur, vous avez besoin des permissions **Exporter les données utilisateur** []({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) pour ce groupe d'applications.
{% endalert %}

!\[Icône d'exportation\]\[6\]

La sortie CSV contient des données de profil utilisateur pour chaque destinataire de la campagne. Braze va générer le rapport en arrière-plan et l'envoyer par courriel à l'utilisateur qui est actuellement connecté.

Si vous avez [lié vos identifiants Amazon S3 à Braze][26], alors le CSV sera également téléchargé dans votre compartiment S3. Sinon, le lien qui vous est envoyé par e-mail expirera dans quelques heures.

Le fichier exporté inclut les mêmes champs de données utilisateur qui sont inclus lorsque vous [exportez des données utilisateur pour un segment][40]. En plus de ces champs de données, si vous choisissez "Exporter toutes les données du destinataire", alors le fichier exporté contiendra également les données suivantes pour chaque utilisateur :

- Nom de la variation de campagne reçue
- ID API de variation de la campagne reçue
- Si l'utilisateur est dans le groupe de contrôle

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}
[6]: {% image_buster /assets/img/campaign_export_example.png %}

[26]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/
[40]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data
