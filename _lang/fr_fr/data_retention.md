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

*Dernière révision le 1er avril 2024*

> Cet article couvre les informations générales sur la conservation des données de Braze.<br><br>Les données enregistrées dans Braze sont conservées et peuvent être utilisées pour la segmentation, la personnalisation et le ciblage pour la durée de vie du compte du client. Ceci signifie que les données telles que les attributs du profil utilisateur, les attributs personnalisés, les événements personnalisés et les achats sont enregistrés indéfiniment pour les utilisateurs actifs pendant la durée du contrat sauf si elles sont supprimées par le client.<br><br>Braze dispose de fonctionnalités, de processus et d’API pour implémenter automatiquement de bonnes pratiques d’hygiène des données à des fins de conformité avec le RGPD et d’autres recommandations. Ceux-ci sont décrits ci-dessous.

## Conservation des données gérée par les clients via le tableau de bord ou l’API de Braze

Braze permet à ses clients de supprimer eux-mêmes des profils utilisateurs entiers et des données d'attribut à partir de leur espace de travail.

Cela signifie que vous pouvez : 
- Supprimez des profils utilisateurs à l'aide de l'[endpoint API Delete user de]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) Braze [.]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) 
- Supprimer (null) ou modifier des attributs sur des profils utilisateurs en utilisant l'[endpoint de l'API]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Braze [Track user.]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)

Les événements comportementaux ne peuvent pas être supprimés d’un profil d’utilisateur (événements personnalisés, sessions, campagnes, achats). Pour supprimer ces événements, vous devez supprimer l’ensemble du profil utilisateur.

Pour des raisons de respect de la vie privée, vous pouvez être amené à supprimer toutes les données personnelles relatives à un utilisateur à la demande de ce dernier. Vous trouverez des instructions sur notre page d'[assistance technique relative à la protection des données]({{site.baseurl}}/help/dp-technical-assistance/#the-right-to-erasure).

{% alert note %}
Un utilisateur peut avoir plusieurs profils, et vous devrez peut-être supprimer plusieurs profils pour supprimer toutes les données relatives à un seul utilisateur. Suivez les instructions de la page d’assistance technique sur la protection des données pour supprimer complètement toutes les données concernant un utilisateur.
{% endalert %}

## Conservation des données gérée par Braze pour des fonctionnalités spécifiques des Services Braze

#### Base de données Braze : Archivage/suppression automatique des utilisateurs inactifs

Chaque semaine, Braze exécute un processus visant à supprimer les utilisateurs inactifs et dormants des services Braze. En général, il s'agit d'utilisateurs qui ne sont pas joignables (par exemple, qui n'ont pas d'adresse e-mail, pas de numéro de téléphone, pas de jeton push, qui n'utilisent pas vos apps ou ne visitent pas vos sites web), qui n'ont eu aucune activité enregistrée sur leur profil utilisateur et qui n'ont pas reçu de message ou n'ont pas été engagés avec l'utilisation de Braze. Ceci est mis en place pour respecter les principes et recommandations du RGPD. Vous pouvez en savoir plus sur ce processus en consultant notre page consacrée [aux définitions de l'archivage utilisateur]({{site.baseurl}}/user_archival/).

{% alert note %}
Les clients ont un contrôle total sur le statut inactif ou dormant des utilisateurs et peuvent empêcher l’archivage des profils utilisateurs en enregistrant un point de donnée à intervalle régulier. Braze Canvas offre la possibilité de le faire automatiquement, ce qui vous permet de désactiver efficacement cette fonctionnalité pour certains ou pour tous vos utilisateurs inactifs ou dormants. 
{% endalert %}

#### Données sur les interactions de campagne et de Canvas 

Les données d'interaction des messages se réfèrent à la manière dont un utilisateur interagit avec une campagne ou une variante du canvas qu'il a reçu (par exemple, lorsqu'un utilisateur ouvre la campagne A ou qu'un utilisateur reçoit la variante A). Ces données sont utilisées à des fins de reciblage. Pour en savoir plus sur la disponibilité des données d’interaction de messagerie, consultez [À propos de la disponibilité des données d’interaction de messagerie]({{site.baseurl}}/messaging_interaction_data/).

## Conservation des données gérée par Braze

Les politiques de conservation ci-dessous concernent la conformité de Braze avec les réglementations RGPD et relatives à la confidentialité et concernent le stockage des données transitoires au fur et à mesure qu’elles passent dans nos systèmes internes. Ces politiques de conservation n’ont pas d’impact sur les Services de Braze et sont des informations destinées à vos équipes juridiques et de protection de la vie privée.

#### Serveurs Braze : Conservation à court terme à des fins de recouvrement

Les données envoyées par Braze à certains sous-processeurs peuvent se maintenir dans les systèmes internes de Braze pendant un maximum de 90 jours.

#### Conservation des données du Data Lake de Braze

Les données disponibles pour les clients dans le tableau de bord de Braze sont principalement agrégées. Les journaux détaillés sont conservés dans une base de données distincte créée par Braze (le " lac de données "). Les données du Data Lake sont utilisées pour l’agrégation de rapports et d’autres fonctionnalités avancées. Braze supprime les informations personnellement identifiables des données d'événements stockées dans le lac de données au bout de deux ans (voir plus d'informations dans notre page sur la [conservation des données de Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention#snowflake-data-retention/) ).

Si vous utilisez nos API pour supprimer des profils utilisateurs ou pour supprimer ou modifier des attributs de profils utilisateurs, la suppression de ces données du Data Lake de Braze peut prendre jusqu'à trois semaines. Supprimer des données dans le Data Lake n’aura pas d’effet sur la segmentation ou la personnalisation mais garantit que les données sont supprimées de tous les systèmes de Braze.

#### Serveurs de sauvegarde Braze

Lorsque les données sont supprimées de votre instance de production, elles restent dans les serveurs de sauvegarde de Braze pendant six mois, puis sont supprimées conformément à nos processus internes.
