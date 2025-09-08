---
nav_title: Présentation du SDK 
article_title: Présentation du SDK 
page_order: 9
page_type: reference
description: "Cet article de référence traite des principes fondamentaux du SDK Braze."
---

# Aperçu du SDK 

> Le SDK Braze facilite la collecte des données de session, l’identification des utilisateurs et l’enregistrement des achats et des événements personnalisés sur votre site web ou votre application. Vous pouvez également utiliser le SDK pour interagir avec vos utilisateurs en envoyant des messages in-app et des notifications push directement depuis le tableau de bord de Braze.

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

Le SDK Braze capture automatiquement d’immenses quantités de données au niveau de l’utilisateur, ce qui facilite la visualisation des indicateurs clés pour votre application et votre base d’utilisateurs. Vous regrouperez les applications similaires dans un même espace de travail sur votre tableau de bord. Par exemple, vous regrouperez les versions iOS et Android de votre appli dans le même espace de travail, ce qui vous permettra de voir les données collectées auprès des utilisateurs sur les deux plateformes. Cela vous donne une vue plus complète de vos utilisateurs sur les canaux web et mobiles. Voir l'article sur la [page d'accueil]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) pour plus d'informations.

## Envoi de messages in-app

Le SDK permet de composer et d'envoyer facilement des messages in-app pour communiquer directement avec les utilisateurs. Vous pouvez choisir d’envoyer des messages slideup, modal ou plein écran en fonction de votre stratégie de campagne. Pour plus d'informations sur la composition d'un message in-app, consultez notre page sur la [création d'un message in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/).

![Push affiché sur un web navigateur]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Notifications push

Les notifications push sont une autre excellente option pour engager le dialogue avec vos utilisateurs et sont particulièrement utiles pour gérer les appels à l'action sensibles au temps. Les notifications push mobiles apparaissent sur les appareils de vos utilisateurs, et les notifications push web apparaissent même lorsque votre site n'est pas ouvert. Pour en savoir plus sur l'utilisation des notifications push, consultez notre [article sur les notifications push.]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)

Les utilisateurs de votre application ou de votre site Internet doivent s’abonner pour recevoir des notifications push. Voir l'[amorçage de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) pour plus de détails. 

## Règles de segmentation et de livraison

Par défaut, une campagne contenant des messages in-app sera envoyée à toutes les versions de l'application dans cet espace de travail. Par exemple, le message sera envoyé aux utilisateurs Web et mobiles. Pour envoyer un message in-app exclusivement sur Internet ou mobile, vous devez segmenter votre campagne en conséquence, ce qui est pris en charge par défaut sur le SDK Braze. 

Vous pouvez créer un segment de vos internautes en définissant des **Apps et des sites web ciblés** sur les **Utilisateurs d'apps spécifiques**, puis sélectionner uniquement votre site web pour les **Apps spécifiques.**

![Page de détails du segment avec l'application web au premier plan]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

Cela vous permet de cibler de façon intelligente les utilisateurs en fonction de leur comportement. Si vous souhaitez cibler des utilisateurs Web pour les encourager à télécharger votre application mobile, vous pouvez créez ce segment comme votre audience cible. Si vous souhaitez envoyer une campagne de communication comprenant un message mobile in-app mais pas de message web, vous décochez l'icône de votre site Web dans votre segment.

## Quelles sont les intégrations de Braze ?
Braze propose une version de notre SDK pour de nombreuses plateformes (Web, Android, iOS, Flutter, React Native, etc.), mais elles fonctionnent toutes essentiellement de la même manière. Ainsi, si vous voyez une référence au « SDK Web » par exemple, il s'agit simplement de la version du SDK de Braze destinée à votre site Web.

<style>
table th:nth-child(1) {
width: 33%;
}
table th:nth-child(2) {
width: 33%;
}
table th:nth-child(3) {
width: 33%;
}
table td {
word-break: break-word;
text-align: center;
}
</style>
Intégrations disponibles   |    |   
----------- |---------------- | --------------------
[![Android]({% image_buster /assets/img/braze_icons/android.svg %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) |[![iOS]({% image_buster /assets/img/braze_icons/apple.svg %})]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift){: style="max-width:20%;margin-right:15px;border:0" class="noimgborder"} [iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) |[![Web]({% image_buster /assets/img/braze_icons/globe-02.png %})]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web){: style="max-width:25%;margin-right:15px;border:0" class="noimgborder"} [Web]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)  

Toutes les intégrations   |    |   
----------- |---------------- | --------------------
[![Cordova Android]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=android){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=android) | [![Cordova iOS]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=ios){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=ios) | [![Flutter Android et iOS]({% image_buster /assets/img/flutter_icon.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=flutter){: style="max-width:20%;margin-top:5%;border:0" class="noimgborder"}  [Flutter Android et iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=flutter)
[![React Native]({% image_buster /assets/img/reactnative_icon.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [React Native]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native) | [![tvOS]({% image_buster /assets/img/tvos_icon.png %})]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/tvos/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [tvOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/tvos/initial_sdk_setup/) | [![MacOS]({% image_buster /assets/img/macOS_icon.png %})]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/macOS/initial_sdk_setup/){: style="max-width:40%;margin-top:15%;border:0" class="noimgborder"}  [MacOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/macOS/initial_sdk_setup/)
[![Unity Android]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity) | [![Unity iOS]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity) | [![Xamarin]({% image_buster /assets/img/xamarin.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=xamarin){: style="max-width:35%;margin-top:5%;border:0" class="noimgborder"}  [Xamarin]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=xamarin) 
[![Roku]({% image_buster /assets/img/roku.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=roku){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [Roku]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=roku) | [![Unreal Engine]({% image_buster /assets/img/unreal.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unreal%20engine){: style="max-width:30%;margin-right:15px;border:0" class="noimgborder"}  [Unreal Engine]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unreal%20engine)

