---
nav_title: Aperçu du SDK
article_title: Aperçu du SDK 
page_order: 9
page_type: reference
description: "Cet article de référence couvre les bases du SDK de Braze."
---

# Aperçu du SDK 

> Le SDK de Braze facilite la collecte des données de session, l'identification des utilisateurs et l'enregistrement des achats et des événements personnalisés via votre site web ou votre appli. Vous pouvez également utiliser le SDK pour dialoguer avec vos utilisateurs en envoyant des messages in-app et des notifications push directement depuis le tableau de bord de Braze.

En bref, le SDK de Braze :
* Collecte et synchronise les données de l'utilisateur dans un profil utilisateur consolidé.
* Capture des données d'engagement marketing et des données personnalisées propres à votre entreprise.
* Permet de gérer les notifications push, les messages in-app et les canaux d'envoi de messages des cartes de contenu.

## Qu'est-ce qu'un SDK ?
Un kit de développement logiciel (SDK) est un ensemble d'outils préfabriqués - de petits blocs de code - qui peuvent être ajoutés aux applications numériques pour prendre en charge de nouvelles fonctionnalités. Le SDK de Braze est utilisé pour envoyer et recevoir des informations depuis et vers votre app ou votre site. Il est conçu pour fournir des fonctionnalités essentielles dès le départ : création de profils utilisateurs, enregistrement d'événements personnalisés, déclenchement de notifications push, etc. 

Cette fonctionnalité étant fournie par défaut par Braze, vos développeurs sont libérés et peuvent se concentrer sur votre cœur de métier. Sans SDK, chaque client de Braze devrait créer de toutes pièces l'infrastructure et les outils nécessaires au traitement des données, à la logique de segmentation, aux options de réception/distribution, à la gestion des utilisateurs anonymes, à l'analyse des campagnes et à bien d'autres choses encore. Cela prendrait beaucoup plus de temps et serait beaucoup plus pénible que l'heure environ nécessaire à l'intégration de notre SDK.

## Mise en œuvre

Pour intégrer un SDK dans votre application ou votre site, il faut ajouter le code du SDK à la base de code globale de l'application. Cela signifie que votre équipe d'ingénierie sera impliquée, essentiellement pour lier nos apps ensemble afin que les informations et les actions circulent entre elles. Bien que vos développeurs soient impliqués, le SDK est conçu pour être léger et facile à intégrer. 

Pour vous faire gagner du temps et garantir une intégration en douceur, nous vous recommandons, ainsi qu'à votre équipe d'ingénieurs, de configurer vos événements personnalisés, vos attributs personnalisés et le SDK en même temps. Découvrez les étapes auxquelles vos équipes de marketing et d'ingénierie devront réfléchir ensemble en lisant notre [article sur la mise en œuvre]({{site.baseurl}}/user_guide/getting_started/integration/). 

## Agrégation des données

Le SDK de Braze capture automatiquement d'immenses quantités de données au niveau de l'utilisateur, ce qui permet de voir facilement les indicateurs clés de votre application et de votre base d'utilisateurs. Vous regrouperez les applications similaires dans un même espace de travail sur votre tableau de bord. Par exemple, vous regrouperez les versions iOS et Android de votre appli dans le même espace de travail, ce qui vous permettra de voir les données collectées auprès des utilisateurs sur les deux plateformes. Vous disposez ainsi d'une vue plus complète de vos utilisateurs sur l'ensemble des canaux web et mobiles. Voir l'article sur la [page d'accueil]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) pour plus d'informations.

## Message in-app

Le SDK permet de composer et d'envoyer facilement des messages in-app pour dialoguer directement avec les utilisateurs. Vous pouvez choisir d'envoyer des messages en mode contextuel, modal ou plein écran en fonction de votre stratégie de communication. Pour plus d'informations sur la composition d'un message in-app, consultez notre page sur la [création d'un message in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/).

!Push affiché sur un navigateur web]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Notifications push

Les notifications push sont une autre excellente option pour engager le dialogue avec vos utilisateurs et sont particulièrement utiles pour gérer les appels à l'action sensibles au temps. Les notifications push mobiles apparaissent sur les appareils de vos utilisateurs, et les notifications push web apparaissent même lorsque votre site n'est pas ouvert. Pour en savoir plus sur l'utilisation des notifications push, consultez notre [article sur les notifications push.]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)

Les utilisateurs de votre site web ou de votre appli doivent s'abonner pour recevoir des notifications push. Voir l'[amorçage de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) pour plus de détails. 

## Règles de segmentation/distribution

Par défaut, une campagne contenant des messages in-app sera envoyée à toutes les versions de l'application dans cet espace de travail. Par exemple, le message sera envoyé à la fois aux utilisateurs web et aux utilisateurs mobiles. Pour envoyer un message in-app exclusivement sur le web ou le mobile, vous devrez segmenter votre campagne en conséquence, ce qui est pris en charge par défaut via le SDK de Braze. 

Vous pouvez créer un segment de vos internautes en définissant des **Apps et des sites web ciblés** sur les **Utilisateurs d'apps spécifiques**, puis sélectionner uniquement votre site web pour les **Apps spécifiques.**

[Page de détails du segment avec l'application web en point de mire]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

Vous pourrez ainsi cibler les utilisateurs en fonction de leur comportement de manière intelligente. Si vous vouliez cibler les internautes pour les inciter à télécharger votre application mobile, vous créeriez ce segment en tant qu'audience cible. Si vous souhaitez envoyer une campagne de communication comprenant un message mobile in-app mais pas de message web, vous décochez l'icône de votre site web dans votre segment.

## Plates-formes prises en charge

Braze fournit des SDK pour plusieurs plateformes, comme le Web, Android et Swift. Pour obtenir la liste complète, consultez le [guide du développeur de Braze]({{site.baseurl}}/developer_guide/home).
