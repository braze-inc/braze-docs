---
nav_title: Dépréciations
article_title: Dépréciations
page_order: 9
layout: en vedette
guide_top_header: "Dépréciations"
guide_top_text: "La technologie est toujours en mouvement - à l'intérieur de Braze et à l'extérieur! Et nous faisons de notre mieux pour nous y tenir. Ici, vous trouverez les origines de Braze et de sa technologie - comment nous avons soutenu les gens dans le \"temps avant\" - avant maintenant, de toute façon... <br> <br> Vous avez peut-être obtenu ici en recherchant un terme pour une intégration ou une fonctionnalité qui n'existe plus. C'est notre tentative de vous tenir au courant de notre évolution et de notre évolution dans l'industrie technologique. <br> <br> Vous pouvez trouver une liste de fonctionnalités obsolètes et non prises en charge ci-dessous. Vous pouvez également lire les articles obsolètes en cliquant sur les boutons ci-dessous."
page_type: atterrissage
description: "Cette page d'accueil contient des références à des articles obsolètes et fournit une liste de fonctionnalités obsolètes et non supportées."
guide_featured_title: "Articles obsolètes"
guide_featured_list:
  - 
    name: Apptimize le partenariat
    link: /fr/docs/help/release_notes/deprecations/apptimize/
    fa_icon: fas fa-vials
  - 
    name: Configuration du SDK Eclipse
    link: /docs/help/release_notes/deprecations/eclipse_setup_deprecated/
    fa_icon: fas fa-circle
  - 
    name: "Dépréciation TLS 1.0 & 1.1"
    link: /fr/docs/help/release_notes/deprecations/tls_deprecation/
    fa_icon: fas fa-lock
---


## Apptimize

_partenariat de braze_

_Soutien retiré : Août 2019_

Si vous utilisez actuellement [Apptimize avec Braze]({{site.baseurl}}/help/release_notes/deprecations/apptimize), vous ne rencontrerez pas de perturbation du service. Vous pouvez toujours définir des attributs personnalisés Apptimize pour les profils d'utilisateurs de Braze. Cependant, aucun soutien officiel d'escalade avec le partenaire ne sera fourni.


## Messages originaux dans l'application

_Remplacé par : [Messagerie In-App]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creating_an_in-app_message)_

_Fonctionnalité de Braze_

_Soutien complètement retiré : février 2019_

Braze a amélioré l'apparence et la sensation des messages In-App pour adhérer aux dernières pratiques UX et UI et ne prend plus en charge les messages originaux dans l'application.

Braze s'est déplacé vers une nouvelle forme de messages dans l'application avec les versions SDK suivantes :

- iOS : `2.19.0`
- Android: `1.13.0`
- Web: `1.3.0`

Avant ces versions, Braze supportait les « messages originaux dans l'application. » Auparavant, la prise en charge des messages originaux dans l'application était fournie à tout client qui a lancé une campagne dans l'application avant la nouvelle version. Toutes les statistiques de la campagne n'ont pas été affectées par le changement, et ceux qui ont envoyé des messages originaux dans l'application ont eu la possibilité d'envoyer d'autres messages via le bouton **Créer une campagne** sur la page **Campagne**.

!\[Choices\]\[15\]


## Vos commentaires

_fonction de brise_

_L'aide doit être retirée complètement le 1er juillet 2019._

Le SDK de Braze a fourni un widget de rétroaction qui pourrait être ajouté à votre application pour permettre aux utilisateurs de laisser leurs commentaires en utilisant la méthode submitFeedback et de le passer dans l'un ou l'autre des bureaux. om ou Zendesk et a été géré sur le tableau de bord.

## Messagerie Google Cloud (GCM)

_Remplacé par : [Messagerie Firebase Cloud (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)_

_Intégration_

_Soutien retiré: Juillet 2018 (Braze removal of support) et 29 Mai 2019 (retrait de la prise en charge de Google)._

[Google a supprimé la prise en charge de GCM](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html) depuis le 29 mai 2019. Braze a supprimé la prise en charge de GCM des SDKs Android en juillet 2018, ce qui a été noté dans [nos changelogs Android SDK](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md). Cela signifie que les jetons GCM existants continueront de fonctionner et que vous pourrez envoyer des messages à vos utilisateurs existants. Cependant, vous ne pourrez pas envoyer de message aux nouveaux utilisateurs.

Les clients qui n'ont pas déjà migré vers [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) peuvent être affectés par cette modification.

Si vous n'avez pas passé à FCM, tous les enregistrements de jetons push GCM échoueront. Si vos applications prennent actuellement en charge GCM, vous devrez travailler avec vos équipes de développement sur [la transition de GCM à Firebase Cloud Messaging (FCM)](https://developers.google.com/cloud-messaging/android/android-migrate-fcm).

## Eclipse

_remplacé par : [android studio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)_

_Intégration_

_Soutien retiré: 2014-2015_

Braze a supprimé la prise en charge de l'IDE Eclipse en raison de la prise en charge de [Google sunsetting pour le plugin Eclipse Android Developer Tools](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html). Si vous avez besoin d'aide pour votre intégration à Eclipse avant la migration, veuillez [envoyer un e-mail à Support]({{site.baseurl}}/support_contact/) pour obtenir de l'aide.

## Le flux d'événements bruts (RES)

_Remplacé par : [courants]({{site.baseurl}}/partners/braze_currents/about/)_

_Fonctionnalité de Braze_

_Soutien retiré: Juillet 2018_

Le flux d'événements bruts était le prédécesseur de [courants]({{site.baseurl}}/partners/braze_currents/about/) et était obsolète pour faire de la place pour l'avenir des données de Braze.

## Délai d'inactivité

_Remplacé par: n/a_

_Fonctionnalité GCM_

_Soutien retiré: Novembre 2016_

Le paramètre Delay While Idle faisait précédemment partie des [options push GCM](https://developers.google.com/cloud-messaging/http-server-ref). Google a retiré le support de cette option le 15 novembre 2016. Auparavant, lorsque réglé sur **true**, il a indiqué que le message ne devrait pas être envoyé jusqu'à ce que le périphérique devienne actif.

## Points de terminaison personnalisés

_Remplacé par: n/a_

_Fonctionnalité de Braze_

_Soutien retiré: décembre 2019_

Suppression des points de terminaison personnalisés. Si vous avez un point de terminaison personnalisé, vous pouvez continuer à l'utiliser, mais Braze ne les distribue plus.
[15]: {% image_buster /assets/img_archive/in-app-choices.png %}
