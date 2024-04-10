---
nav_title: Présentation du SDK pour les marketeurs
article_title: Présentation du SDK pour les marketeurs
page_order: 3
page_type: reference
description: "Cet article de référence sur l’onboarding décrit les bases du SDK Braze."

---

# Présentation du SDK pour les marketeurs

> Le SDK Braze facilite la collecte des données de session, l’identification des utilisateurs et l’enregistrement des achats et des événements personnalisés sur votre site web ou votre application. Vous pouvez également utiliser le SDK pour interagir avec vos utilisateurs en envoyant des messages in-app et des notifications push directement depuis le tableau de bord de Braze.

Êtes-vous un développeur à la recherche d’un aperçu technique du SDK ? Consultez plutôt notre [présentation pour les développeurs][1].

Le SDK Braze en bref :
* Recueille et synchronise les données utilisateur dans un profil utilisateur consolidé
* Capture les données d’engagement marketing et les données personnalisées spécifiques à votre entreprise
* Alimente les canaux de communication de notifications push, de messages in-app et de carte de contenu

## Qu’est-ce qu’un SDK ?
Un kit de développement logiciel (SDK) est un ensemble d’outils préfabriqués&mdash;de petits blocs de code&mdash;qui peuvent être ajoutés aux applications numériques pour prendre en charge de nouvelles capacités. Le SDK Braze est utilisé pour envoyer et obtenir des informations sur et depuis votre application ou site. Il est conçu pour fournir des fonctionnalités essentielles dès le départ : création de profils utilisateur, journalisation d’événements personnalisés, déclenchement de notifications push, etc. 

Étant donné que cette fonctionnalité provient par défaut de Braze, vos développeurs sont libres de se concentrer sur votre activité principale. Sans SDK, chaque client Braze devrait créer depuis le départ toute l’infrastructure et tous les outils nécessaires au traitement des données, à la logique de segmentation, aux options de livraison, à la gestion des utilisateurs anonymes, aux analytiques des campagnes et bien plus encore. Cela prendrait beaucoup plus de temps et serait bien plus pénible que l’heure, environ, nécessaire pour intégrer notre SDK.

## Mise en œuvre

Pour intégrer un SDK dans votre application ou votre site, quelqu’un devra ajouter le code du SDK à la base de code globale qui alimente cette application. Votre équipe d’ingénierie sera donc impliquée pour, en somme, relier nos applications ensemble afin que les informations et les actions circulent entre elles. Mais bien que vos développeurs soient impliqués, le SDK est conçu pour être léger et facile à intégrer. 

Pour vous faire gagner du temps et assurer une intégration fluide, nous vous recommandons, à vous et à votre équipe d’ingénierie, de configurer vos événements personnalisés, vos attributs personnalisés et le SDK en même temps. Pour en savoir plus sur les étapes auxquelles vos équipes de marketing et d’ingénierie devront réfléchir ensemble, lisez notre [article d’implémentation][4]. 

## Agrégation des données

Le SDK Braze capture automatiquement d’immenses quantités de données au niveau de l’utilisateur, ce qui facilite la visualisation des indicateurs clés pour votre application et votre base d’utilisateurs. Vous regrouperez des applications similaires en un seul groupe d’apps sur votre tableau de bord. Par exemple, vous regrouperez les versions iOS et Android de votre application dans le même groupe d’apps, ce qui vous permettra de voir les données collectées par les utilisateurs sur les deux plateformes. Cela vous donne une vue plus complète de vos utilisateurs sur les canaux web et mobiles. Voir l’article sur la [page Overview][3] pour plus d’informations.

## Envoi de messages in-app

Le SDK facilite la composition et l’envoi de messages in-app pour interagir directement avec les utilisateurs. Vous pouvez choisir d’envoyer des messages slideup, modal ou plein écran en fonction de votre stratégie de campagne. Pour plus d’informations sur la composition d’un message in-app, consultez notre page sur [créer un message in-app][8].

![Notification push affichée sur un navigateur Web][11]{: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Notifications push

Les notifications push sont une autre excellente option pour interagir avec vos utilisateurs et sont particulièrement utiles pour gérer les appels à l’action urgents. Les notifications push mobiles apparaissent sur l’appareil de vos utilisateurs et les notifications push Web apparaissent même lorsque votre site n’est pas ouvert. Pour plus de détails sur l’utilisation des notifications push, consultez notre [article sur les notifications push][5].

Les utilisateurs de votre application ou de votre site Internet doivent s’abonner pour recevoir des notifications push. Consultez la [préparation aux notifications push][13] pour plus de détails. 

## Règles de segmentation et de livraison

Par défaut, une campagne contenant des messages in-app sera envoyée à toutes les versions de l’application dans ce groupe d’apps. Par exemple, le message sera envoyé aux utilisateurs Web et mobiles. Pour envoyer un message in-app exclusivement sur Internet ou mobile, vous devez segmenter votre campagne en conséquence, ce qui est pris en charge par défaut sur le SDK Braze. 

Vous pouvez créer un segment de vos utilisateurs Web en sélectionnant uniquement l’icône de l’application de votre site Internet dans la section **Applications utilisées** d’un segment.

![Page Détails du segment avec application Web sélectionnée][10]

Cela vous permet de cibler de façon intelligente les utilisateurs en fonction de leur comportement. Si vous souhaitez cibler des utilisateurs Web pour les encourager à télécharger votre application mobile, vous pouvez créez ce segment comme votre audience cible. Si vous souhaitez envoyer une campagne de communication qui comprend un message in-app mobile mais pas un message Web, il suffit de décocher l’icône de votre site Internet dans votre segment.

## Quelles sont les intégrations de Braze ?
Braze propose une version de notre SDK pour de nombreuses plateformes (Web, Android, iOS, Flutter, React Native, etc.), mais elles fonctionnent toutes essentiellement de la même manière. Donc, si vous voyez une référence au « SDK Web », il s’agit juste de la version du SDK Braze destinée à votre site Web.

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
Intégrations disponibles   | &nbsp;  |  &nbsp;
----------- |---------------- | --------------------
[![Android]({% image_buster /assets/img/braze_icons/android.svg %})]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) |[![iOS]({% image_buster /assets/img/braze_icons/apple.svg %})]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/){: style="max-width:20%;margin-right:15px;border:0" class="noimgborder"} [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/) |[![Web]({% image_buster /assets/img/braze_icons/globe-02.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/){: style="max-width:25%;margin-right:15px;border:0" class="noimgborder"} [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)  

Toutes les intégrations   | &nbsp;  |  &nbsp;
----------- |---------------- | --------------------
[![Cordova Android]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/android/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova Android]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/android/) | [![Cordova iOS]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/ios/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/ios/) | [![Flutter Android & iOS]({% image_buster /assets/img/flutter_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/flutter/flutter_sdk_integration/){: style="max-width:20%;margin-top:5%;border:0" class="noimgborder"}  [Flutter Android & iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/flutter/flutter_sdk_integration/)
[![React Native]({% image_buster /assets/img/reactnative_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/) | [![tvOS]({% image_buster /assets/img/tvos_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [tvOS]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/) | [![MacOS]({% image_buster /assets/img/macOS_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/macOS/initial_sdk_setup/){: style="max-width:40%;margin-top:15%;border:0" class="noimgborder"}  [MacOS]({{site.baseurl}}/developer_guide/platform_integration_guides/macOS/initial_sdk_setup/)
[![Unity Android]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/android/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/android/) | [![Unity iOS]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/) | [![Xamarin]({% image_buster /assets/img/xamarin.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/){: style="max-width:35%;margin-top:5%;border:0" class="noimgborder"}  [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/) 
[![Roku]({% image_buster /assets/img/roku.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/) | [![Unreal Engine]({% image_buster /assets/img/unreal.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unreal_engine/initial_sdk_setup/){: style="max-width:30%;margin-right:15px;border:0" class="noimgborder"}  [Unreal Engine]({{site.baseurl}}/developer_guide/platform_integration_guides/unreal_engine/initial_sdk_setup/)


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/
[3]: {{site.baseurl}}/user_guide/data_and_analytics/your_analytics_dashboards/understanding_your_app_usage_data/
[4]: {{site.baseurl}}/user_guide/onboarding_with_braze/integration/#the-technical-side-of-the-integration-process
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push/about/
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[7]: {% image_buster /assets/img_archive/app_group_list.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[10]: {% image_buster /assets/img_archive/web-users-segment.png %}
[11]: {% image_buster /assets/img_archive/web_push_macbook.png %}
[13]: {{site.baseurl}}user_guide/message_building_by_channel/push/push_primer_messages/