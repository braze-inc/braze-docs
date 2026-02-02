---
nav_title: Aperçu du SDK
article_title: Présentation du SDK 
page_order: 9
page_type: reference
description: "Cet article de référence traite des principes fondamentaux du SDK Braze."
---

# Aperçu du SDK 

> Le SDK de Braze recueille des données de session, identifie les utilisateurs et enregistre les achats et les événements personnalisés par le biais de votre site web ou de votre appli. Vous pouvez également utiliser le SDK pour engager les utilisateurs en envoyant des messages in-app et des notifications push directement depuis le tableau de bord de Braze.

Le SDK Braze en bref :
* Collecte et synchronise les données de l'utilisateur dans un profil utilisateur consolidé.
* Capture les données d’engagement marketing et les données personnalisées spécifiques à votre entreprise
* Alimente les canaux de communication de notifications push, de messages in-app et de carte de contenu

## Qu’est-ce qu’un SDK ?
Un kit de développement logiciel (SDK) est un ensemble d'outils préfabriqués ( de petits blocs de code) qui peuvent être ajoutés aux applications numériques pour prendre en charge de nouvelles fonctionnalités. Le SDK Braze est utilisé pour envoyer et obtenir des informations sur et depuis votre application ou site. Il est conçu pour fournir des fonctionnalités essentielles dès le départ : création de profils utilisateur, journalisation d’événements personnalisés, déclenchement de notifications push, etc. 

Étant donné que cette fonctionnalité provient par défaut de Braze, vos développeurs sont libres de se concentrer sur votre activité principale. Sans SDK, chaque client Braze devrait créer depuis le départ toute l’infrastructure et tous les outils nécessaires au traitement des données, à la logique de segmentation, aux options de livraison, à la gestion des utilisateurs anonymes, aux analyses des campagnes et bien plus encore. Cela prendrait beaucoup plus de temps et serait bien plus pénible que l’heure, environ, nécessaire pour intégrer notre SDK.

## Mise en œuvre

Pour intégrer un SDK dans votre application ou votre site, quelqu’un devra ajouter le code du SDK à la base de code globale qui alimente cette application. Votre équipe d’ingénierie sera donc impliquée pour, en somme, relier nos applications ensemble afin que les informations et les actions circulent entre elles. Mais bien que vos développeurs soient impliqués, le SDK est conçu pour être léger et facile à intégrer. 

Pour vous faire gagner du temps et assurer une intégration fluide, nous vous recommandons, à vous et à votre équipe d’ingénierie, de configurer vos événements personnalisés, vos attributs personnalisés et le SDK en même temps. Découvrez les étapes auxquelles vos équipes de marketing et d'ingénierie devront réfléchir ensemble en lisant notre [article sur la mise en œuvre]({{site.baseurl}}/user_guide/getting_started/integration/). 

## Agrégation des données

Le SDK de Braze capture automatiquement les données au niveau de l'utilisateur, vous donnant des indicateurs clés pour votre application et votre base d'utilisateurs. Regroupez les applications similaires dans un seul espace de travail (par exemple, les versions iOS et Android ensemble) pour consulter les données collectées sur toutes les plateformes et créer une image complète de l'activité des utilisateurs. Voir l'article sur la [page d'accueil]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) pour plus d'informations.

## Envoi de messages in-app

Utilisez le SDK pour composer et envoyer des messages in-app directement. Vous pouvez choisir des messages en mode contextuel, modal ou plein écran en fonction de votre stratégie de communication. Pour plus de détails sur la composition, reportez-vous à la section [Créer un message in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/).

![Push affiché sur un navigateur web]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Notifications push

Les notifications push sont une autre excellente option pour engager le dialogue avec vos utilisateurs et sont particulièrement utiles pour gérer les appels à l'action sensibles au temps. Les notifications push mobiles apparaissent sur les appareils de vos utilisateurs, et les notifications push web apparaissent même lorsque votre site n'est pas ouvert. Pour en savoir plus sur l'utilisation des notifications push, consultez notre [article sur les notifications push.]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)

Les utilisateurs de votre application ou de votre site Internet doivent s’abonner pour recevoir des notifications push. Voir l'[amorçage de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) pour plus de détails. 

## Règles de segmentation et de livraison

Par défaut, une campagne contenant des messages in-app sera envoyée à toutes les versions de l'application dans cet espace de travail. Par exemple, le message sera envoyé aux utilisateurs Web et mobiles. Pour envoyer un message in-app exclusivement sur Internet ou mobile, vous devez segmenter votre campagne en conséquence, ce qui est pris en charge par défaut sur le SDK Braze. 

Vous pouvez créer un segment de vos internautes en définissant des **Apps et des sites web ciblés** sur les **Utilisateurs d'apps spécifiques**, puis sélectionner uniquement votre site web pour les **Apps spécifiques.**

![Page de détails du segment avec l'application web en point de mire]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

Cela vous permet de cibler de façon intelligente les utilisateurs en fonction de leur comportement. Si vous souhaitez cibler des utilisateurs Web pour les encourager à télécharger votre application mobile, vous pouvez créez ce segment comme votre audience cible. Si vous souhaitez envoyer une campagne de communication comprenant un message mobile in-app mais pas de message web, vous décochez l'icône de votre site Web dans votre segment.

## Plates-formes prises en charge

Braze fournit des SDK pour plusieurs plateformes, comme le Web, Android et Swift. Pour obtenir la liste complète, consultez le [guide du développeur de Braze]({{site.baseurl}}/developer_guide/home).
