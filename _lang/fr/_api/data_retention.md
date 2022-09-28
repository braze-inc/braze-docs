---
nav_title: Conservation des données
article_title: Conservation des données
alias: /data_retention/
description: "Cet article de référence couvre les informations générales sur la conservation des données de Braze. "
page_type: reference
page_order: 2.5

---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Informations sur la conservation des données de Braze

* Dernière révision le 2 mars 2022*

> Cet article couvre les informations générales sur la conservation des données de Braze.

## Conservation des données gérée par les clients via le tableau de bord ou l’API de Braze

Braze permet à ses clients de supprimer eux-mêmes des profils d’utilisateurs et des données d’attributs entiers de leur groupe d’apps.

Cela signifie que vous pouvez : 
- Supprimer les profils d’utilisateur à l’aide du [endpoint de l’API de suppression d’utilisateur de Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/). 
- Supprimer (annuler) ou modifier les attributs des profils d’utilisateurs à l’aide du [endpoint de l’API de suivi des utilisateurs de Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

Les événements comportementaux ne peuvent pas être supprimés d’un profil d’utilisateur (événements personnalisés, sessions, campagnes, achats). Pour supprimer ces événements, vous devez supprimer l’ensemble du profil utilisateur.

Pour des raisons de respect de la vie privée, vous pouvez être amené à supprimer toutes les données personnelles relatives à un utilisateur à la demande de ce dernier. Vous pouvez trouver des instructions sur notre [page d’assistance technique en matière de protection des données]({{site.baseurl}}/help/dp-technical-assistance/#the-right-to-erasure).

{% alert note %}
Un utilisateur peut avoir plusieurs profils, et vous devrez peut-être supprimer plusieurs profils pour supprimer toutes les données relatives à un seul utilisateur. Suivez les instructions de la page d’assistance technique sur la protection des données pour supprimer complètement toutes les données concernant un utilisateur.
{% endalert %}

## Conservation des données gérée par Braze

Dans certains cas, nous ne conservons certaines données que pendant une période prédéterminée avant de les supprimer automatiquement en fonction de certains critères. Pour chaque type de données, nous fixons les délais de conservation suivants :

{% alert important %} Les délais indiqués dans cette section ne sont pas personnalisables. {% endalert %}

#### Base de données Braze : Archivage/suppression automatique des utilisateurs inactifs

Chaque semaine, Braze exécute un processus visant à supprimer les utilisateurs inactifs et dormants des services Braze. Vous pouvez en savoir plus sur ce processus sur notre page [Définitions de l’archivage utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/).

{% alert note %} Bien que l’archivage des profils d’utilisateurs inactifs ou dormants soit automatisé et que la conservation des données ne soit pas personnalisable, vous pouvez exécuter un point de données sur ces profils à intervalles réguliers pour empêcher l’archivage et ainsi les garder actifs. {% endalert %}

#### Résolution des problèmes Braze

Braze peut supprimer des données lorsque cela s’avère nécessaire dans le cadre de la résolution d’un problème ou d’un incident technique, par exemple pour dédupliquer des données.

#### Conservation des données du Data Lake de Braze

Les données disponibles pour les clients dans le tableau de bord de Braze sont principalement agrégées. Les journaux détaillés sont conservés dans une base de données distincte créée par Braze (le « Data Lake », anciennement appelé « BI Database »).

Braze a mis en place des processus pour assurer la suppression régulière des Informations personnellement identifiables du « Data Lake » au niveau d’un groupe d’apps ou d’un événement. Si vous utilisez nos API pour supprimer des profils d’utilisateurs ou pour supprimer ou modifier des attributs de profils d’utilisateurs, dans un délai de deux semaines, ce processus de suppression automatique s’appliquera à :

- Événements
- Achats
- Événements d’engagement de la campagne (par exemple, envois, ouvertures, clics)
- Données des sessions

La suppression de données dans le Data Lake n’affectera pas votre segmentation.

#### Serveurs Braze : Conservation à court terme à des fins de recouvrement

Les données envoyées par les Services Braze au Data Lake de Braze via les serveurs Braze sont conservées jusqu’à 90 jours à des fins de récupération.

#### Serveurs de sauvegarde Braze

Lorsque les données sont supprimées de votre instance de production, elles restent dans les serveurs de sauvegarde de Braze pendant six mois, puis sont supprimées conformément à nos processus internes.

## Conservation des données gérée par Braze pour des fonctionnalités spécifiques des Services Braze
 
#### Données sur les interactions de la campagne 
 
<br>
**Qu’est-ce que c’est ? ** Les interactions de la campagne sont des données relatives aux interactions des utilisateurs finaux avec une campagne. Elles sont utilisées pour les filtres de reciblage et pour déterminer la rééligibilité des campagnes.
 
**Quand sont-elles supprimées ? ** Braze supprime automatiquement des groupes d’applications du client les interactions de campagne pour les campagnes qui n’ont pas envoyé de messages depuis 25 mois civils et qui ne sont pas utilisées pour le reciblage dans des campagnes, des Canvas ou des cartes de contenu dans un statut actif.
 
**Que se passe-t-il après la suppression ? **
 - Les campagnes sans interactions de campagne ne peuvent pas être utilisées dans les filtres de reciblage pour les campagnes, les Canvas et les segments.
 - Toute campagne active qui n’a pas envoyé de messages depuis 25 mois, et qui n’est pas utilisée pour le reciblage dans des campagnes, des Canvas ou des cartes actives, sera arrêtée car l’éligibilité des campagnes est remise à zéro. Vous pouvez relancer la campagne après avoir vérifié le paramètre de rééligibilité.
 
**Comment remettre l’horloge à zéro pour éviter la suppression ? ** Pour conserver les interactions de la campagne pour une campagne particulière, vous pouvez envoyer un message utilisant cette campagne au moins une fois dans les 25 mois qui suivent le dernier message envoyé ou utiliser cette campagne dans un filtre de reciblage dans toute campagne, Canvas ou carte active.
 
Vous pouvez demander une conservation des données plus courte que 25 mois via votre CSM.