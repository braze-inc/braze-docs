---
nav_title: Rétention des données
article_title: Rétention des données
alias: /fr_FR/fr_FR/
description: "Cet article de référence couvre les informations générales de rétention des données de Braze."
page_type: Référence
page_order: 2.5
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Informations sur la conservation des données de Braze

*Dernière révision en octobre 2021*

> Cet article couvre les informations générales sur la rétention des données de Braze.

## La conservation des données est gérée par les clients à travers le tableau de bord ou l'API de Braze

Braze permet à ses clients de supprimer eux-mêmes des profils d'utilisateurs et des données d'attributs de leur groupe d'applications.

Cela signifie que vous pouvez:
- Supprimez les profils d'utilisateurs en utilisant le point d'extrémité de l'API [Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)
- Supprimer (null) ou modifier les attributs sur les profils des utilisateurs en utilisant le [point de terminaison de l'API de suivi utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)

Les événements comportementaux ne peuvent pas être supprimés d'un profil utilisateur (événements personnalisés, sessions, campagnes, achats). Pour supprimer ces événements, vous devez supprimer l'intégralité du profil d'utilisateur.

Pour respecter la vie privée, il se peut que vous deviez supprimer toutes les données personnelles relatives à un Utilisateur à la demande de l’Utilisateur. Vous pouvez trouver des instructions sur notre page [assistance technique]({{site.baseurl}}/help/dp-technical-assistance/#the-right-to-erasure) en matière de protection des données.

{% alert note %}
Un utilisateur peut avoir plusieurs profils, et vous devrez peut-être supprimer plusieurs profils pour supprimer toutes les données relatives à un seul utilisateur. Suivez les instructions sur la page d'assistance technique en matière de protection des données pour savoir comment supprimer complètement toutes les données concernant un Utilisateur.
{% endalert %}

## Rétention des données gérée par Braze

Dans certains cas, nous stockons certaines données uniquement pour une période prédéterminée avant qu'elles ne soient automatiquement supprimées en fonction de certains critères. Pour chaque type de données, nous définissons les délais de rétention décrits ci-dessous.

{% alert important %} Les échéanciers décrits dans cette section ne sont pas personnalisables. {% endalert %}

#### Base de données Braze : Archivage automatique/Suppression des utilisateurs autorisés

Chaque semaine, Braze exécute un processus pour supprimer les utilisateurs inactifs et les utilisateurs dormants des services de Braze. Vous pouvez en savoir plus sur ce processus sur notre page [définitions d'archives]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/) des utilisateurs.

{% alert note %} Alors que l'archivage des profils d'utilisateurs inactifs ou dormants est automatisé et que la rétention des données n'est pas personnalisable, vous pouvez exécuter un point de données sur de tels profils à intervalles réguliers pour éviter l'archivage et ainsi les garder actifs. {% endalert %}

#### Serveurs Braze : Rétention à court terme à des fins de récupération

Les données envoyées par les services de Braze à Braze's Snowflake Data Lake via les serveurs de Braze sont conservées dans ces serveurs pendant 90 jours à des fins de récupération.

#### Conservation des données de Braze Data Lake

Les données disponibles pour les clients dans le tableau de bord de Braze sont pour la plupart agrégées. Les journaux détaillés sont conservés dans une base de données séparée créée par Braze (le « lac des données », anciennement connu sous le nom de « base de données BI »).

Braze a mis en place des processus pour assurer des suppressions régulières de PII du “Lac des données” au niveau d'un groupe d'applications ou d'un événement. Si vous utilisez nos APIs pour supprimer les profils d'utilisateur, ou supprimer ou modifier les attributs des profils d'utilisateurs, dans les deux semaines, ce processus de suppression automatique s'appliquera à:

- Évènements
- Achats
- Événements d'engagement de la campagne (par exemple, envois, ouverts, clics)
- Données des sessions

La suppression de données dans le lac des données n'affectera pas votre segmentation.

#### Serveurs de sauvegarde Braze

Lorsque des données sont supprimées de votre instance de production, les données restent dans les serveurs de sauvegarde de Braze pendant 6 mois et sont ensuite supprimées selon nos processus internes.

## Rétention des données gérée par Braze pour des fonctionnalités spécifiques des services de Braze

#### Données d'interactions de la campagne

<br>**Qu'est-ce que c'est ?** Les interactions de la campagne sont des données liées aux interactions des utilisateurs finaux avec une campagne. Ils sont utilisés pour les filtres de redistribution et pour déterminer la rééligibilité de la campagne.

**Quand est-elle supprimée?** Braze supprime automatiquement des groupes d'applications du client les Interactions de campagne pour des campagnes qui n'ont pas envoyé de messages dans 25 mois civils et ne sont pas utilisés pour le repositionnement dans aucune campagne, Canvases, ou Cartes de Contenu dans un état actif.

**Que se passe-t-il après la suppression?**
 - Les campagnes sans Interactions de campagne ne peuvent pas être utilisées dans des filtres de redistribution pour les campagnes, les canevas et les segments.
 - Toute campagne active qui n'a pas envoyé de messages en 25 mois et qui n'est utilisée pour le repositionnement dans aucune campagne active, Les vases, ou cartes, seront arrêtées parce que l'éligibilité de la campagne sera réinitialisée. Vous pouvez relancer la campagne après avoir examiné le cadre de réadmissibilité.

**Comment réinitialiser l'horloge pour éviter la suppression ?** Conserver les Interactions de Campagne pour une campagne particulière, vous pouvez envoyer un message en utilisant cette campagne au moins une fois dans les 25 mois qui ont suivi l'envoi du dernier message ou l'utilisation de cette campagne dans un filtre de redistribution dans n'importe quelle campagne active, Toile ou carte.

Vous pouvez demander une conservation de données plus courte que 25 mois via votre MCS.