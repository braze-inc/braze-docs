---
nav_title: Conservation des données
article_title: Conservation des données
alias: /data_retention/
description: "Cet article de référence couvre les informations générales sur la conservation des données de Braze."
page_type: reference
page_order: 2.5

---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Informations sur la conservation des données de Braze

*Dernière révision le 20 janvier 2023*

> Cet article couvre les informations générales sur la conservation des données de Braze.<br><br>Les données enregistrées dans Braze sont conservées et peuvent être utilisées pour la segmentation, la personnalisation et le ciblage pour la durée de vie du compte du client. Ceci signifie que les données telles que les attributs du profil utilisateur, les attributs personnalisés, les événements personnalisés et les achats sont enregistrés indéfiniment pour les utilisateurs actifs pendant la durée du contrat sauf s’ils sont supprimés par le client.<br><br>Braze dispose de fonctionnalités, de processus et d’API pour implémenter automatiquement de bonnes pratiques d’hygiène des données à des fins de conformité avec le RGPD et d’autres recommandations. Ceux-ci sont décrits ci-dessous.

## Conservation des données gérée par les clients via le tableau de bord ou l’API de Braze

Braze permet à ses clients de supprimer eux-mêmes des profils d’utilisateurs et des données d’attributs entiers de leur groupe d’apps.

Cela signifie que vous pouvez : 
- Supprimer les profils utilisateur en utilisant l’[Endpoint de l'API de suppression d'utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) de Braze 
-Supprimer (null) ou modifier les attributs sur les profils utilisateur en utilisant l’[Endpoint de l'API de suivi des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze

Les événements comportementaux ne peuvent pas être supprimés d’un profil d’utilisateur (événements personnalisés, sessions, campagnes, achats). Pour supprimer ces événements, vous devez supprimer l’ensemble du profil utilisateur.

Pour des raisons de respect de la vie privée, vous pouvez être amené à supprimer toutes les données personnelles relatives à un utilisateur à la demande de ce dernier. Vous pouvez trouver des instructions sur notre [page d’assistance technique en matière de protection des données]({{site.baseurl}}/help/dp-technical-assistance/#the-right-to-erasure).

{% alert note %}
Un utilisateur peut avoir plusieurs profils et vous devrez peut-être supprimer plusieurs profils pour supprimer toutes les données relatives à un seul utilisateur. Suivez les instructions de la page d’assistance technique sur la protection des données pour supprimer complètement toutes les données concernant un utilisateur.
{% endalert %}

## Conservation des données gérée par Braze pour des fonctionnalités spécifiques des Services Braze

#### Base de données Braze : Archivage/suppression automatique des utilisateurs inactifs

Chaque semaine, Braze exécute un processus visant à supprimer les utilisateurs inactifs et dormants des services Braze. En général, il s’agit d’utilisateurs qui ne peuvent pas être contactés (par ex., qui n’ont pas d’adresse e-mail, de numéro de téléphone, de jetons de notification push, qui n’utilisent pas vos applications et ne se rendent pas sur vos sites Internet), n’ont pas eu d’activité enregistrée sur leur profil utilisateur et n’ont pas reçu de message ni n’ont été contactés pour utiliser Braze. Ceci est mis en place pour respecter les principes et recommandations du RGPD. Vous pouvez en savoir plus sur ce processus sur notre page [Définitions de l’archivage utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/).

{% alert note %} 
Les clients ont un contrôle total sur le statut inactif ou dormant des utilisateurs et peuvent empêcher l’archivage des profils utilisateurs en enregistrant un point de donnée à intervalle régulier. Braze Canvas offre la possibilité de le faire automatiquement, ce qui vous permet de désactiver efficacement cette fonctionnalité pour certains ou pour tous vos utilisateurs inactifs ou dormants. 
{% endalert %}

#### Données sur les interactions de la campagne 
 
**Qu’est-ce que c’est ? ** Les interactions de la campagne sont des données relatives aux interactions des utilisateurs finaux avec une campagne. Elles sont utilisées pour les filtres de reciblage et pour déterminer la rééligibilité des campagnes.
 
**Quand sont-elles supprimées ? ** Braze supprime automatiquement des groupes d’applications du client les interactions de campagne pour les campagnes qui n’ont pas envoyé de messages depuis 25 mois civils et qui ne sont pas utilisées pour le reciblage dans des campagnes, des Canvas ou des cartes de contenu dans un statut actif.
 
**Que se passe-t-il après la suppression ? **
 Les campagnes sans interactions de campagne ne peuvent pas être utilisées dans les filtres de reciblage pour les campagnes, les Canvas et les segments.
 Toute campagne active qui n’a pas envoyé de messages depuis 25 mois, et qui n’est pas utilisée pour le reciblage dans des campagnes, des Canvas ou des cartes actives, sera arrêtée car l’éligibilité des campagnes est remise à zéro. Vous pouvez relancer la campagne après avoir vérifié le paramètre de rééligibilité.
 
**Comment remettre l’horloge à zéro pour éviter la suppression ? ** Pour conserver les interactions de la campagne pour une campagne particulière, vous pouvez envoyer un message utilisant cette campagne au moins une fois dans les 25 mois qui suivent le dernier message envoyé ou utiliser cette campagne dans un filtre de reciblage dans toute campagne, Canvas ou carte active. Vous pouvez demander une conservation des données plus courte que 25 mois via votre gestionnaire du succès des clients de Braze.
 
#### Données des interactions Canvas 

**Qu’est-ce que c’est ? ** Les interactions Canvas sont des données liées aux interactions de l’utilisateur final avec un Canvas ou un Canvas Step. Elles sont utilisées pour les filtres de reciblage et pour déterminer la rééligibilité des Canvas.

**Quand sont-elles supprimées ? ** Braze supprime automatiquement des groupes d’applications du client les interactions de Canvas pour les Canvas qui n’ont pas envoyé de messages depuis 25 mois civils et qui ne sont pas utilisées pour le reciblage dans des campagnes ou des Canvas actifs.

**Que se passe-t-il après la suppression ? **

- Les Canvas sans interactions de Canvas ne peuvent pas être utilisées dans les filtres de reciblage pour les campagnes, les Canvas et les segments.
- Tout Canvas actif qui n’a pas envoyé de messages depuis 25 mois et qui n’est pas utilisé pour le reciblage dans des campagnes, des Canvas ou des cartes actives, sera arrêté car l’éligibilité des Canvas est remise à zéro. Vous pouvez relancer le Canvas après avoir vérifié le paramètre de rééligibilité.
- Vous ne pourrez pas référencer ces interactions Canvas au sein de fonctionnalités de reciblage telles que des filtres et vous ne pourrez pas extraire les données supprimées de l’API `/users/export`.

**Comment remettre l’horloge à zéro pour éviter la suppression ? ** Pour conserver les interactions du Canvas pour un Canvas particulier, vous pouvez envoyer un message utilisant ce Canvas au moins une fois dans les 25 mois qui suivent le dernier message envoyé ou utiliser ce Canvas dans un filtre de reciblage dans toute campagne, Canvas ou carte active. Vous pouvez demander une conservation des données plus courte que 25 mois via votre gestionnaire du succès des clients de Braze.

## Conservation des données gérée par Braze

Les politiques de conservation ci-dessous concernent la conformité de Braze avec les réglementations RGPD et relatives à la confidentialité et concernent le stockage des données transitoires au fur et à mesure qu’elles passent dans nos systèmes internes. Ces politiques de conservation n’ont pas d’impact sur les Services de Braze et sont des informations destinées à vos équipes juridiques et de protection de la vie privée.

#### Serveurs Braze : Conservation à court terme à des fins de recouvrement

Les données envoyées par Braze à certains sous-processeurs peuvent se maintenir dans les systèmes internes de Braze pendant un maximum de 90 jours.

#### Conservation des données du Data Lake de Braze

Les données disponibles pour les clients dans le tableau de bord de Braze sont principalement agrégées. Les journaux détaillés sont conservés dans une base de données distincte créée par Braze (le « Data Lake », anciennement appelé « BI Database »). Les données du Data Lake sont utilisées pour l’agrégation de rapports et d’autres fonctionnalités avancées.

Si vous utilisez nos API pour supprimer des profils utilisateurs ou bien supprimer ou modifier des attributs des profils utilisateurs, les données peuvent prendre jusqu’à deux semaines pour être supprimées du Data Lake de Braze. Supprimer des données dans le Data Lake n’aura pas d’effet sur la segmentation ou la personnalisation mais garantit que les données sont supprimées de tous les systèmes de Braze.

#### Serveurs de sauvegarde Braze

Lorsque les données sont supprimées de votre instance de production, elles restent dans les serveurs de sauvegarde de Braze pendant six mois, puis sont supprimées conformément à nos processus internes.
