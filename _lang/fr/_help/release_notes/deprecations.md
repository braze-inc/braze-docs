---
nav_title: Obsolescences
article_title: Obsolescences
page_order: 9
layout: dev_guide

guide_top_header: "Obsolescences"
guide_top_text: "La technologie évolue constamment, chez Braze et en dehors ! Et nous faisons de notre mieux pour tenir la cadence. Ici, vous en apprendrez plus sur les origines de Braze et sa technologie - ce que nous faisions « avant », avant maintenant... <br> <br> Vous êtes peut-être arrivé ici en faisant une recherche sur une intégration ou fonctionnalité qui n’existe plus. C’est notre manière de vous tenir informé de nos progrès et des mouvements au sein de l’industrie technologique. <br> <br> Vous pouvez trouver une liste de fonctions désactivées et non prises en charge et lire les articles associés en visitant les liens suivants."

page_type: landing
description: "Cette page d’accueil comprend des références aux articles obsolètes et fournit une liste de fonctions obsolètes qui ne sont plus prises en charge."

guide_featured_title: "Articles obsolètes"
guide_featured_list:
  - name: Partenariat Apptimize
    link: /docs/help/release_notes/deprecations/apptimize/
    image: /assets/img/braze_icons/beaker-02.svg
  - name: Récepteur de diffusion personnalisée de notifications push pour Android
    link: /docs/help/release_notes/deprecations/custom_broadcast_receiver/
    image: /assets/img/braze_icons/phone-01.svg
  - name: Configuration du SDK Eclipse
    link: /docs/help/release_notes/deprecations/eclipse_setup_deprecated/
    image: /assets/img/braze_icons/x.svg
  - name: "Désactivation de TLS 1.0 et 1.1"
    link: /docs/help/release_notes/deprecations/tls_deprecation/
    image: /assets/img/braze_icons/lock-01.svg
  - name: Intégration du Webhook Twilio
    link: /docs/help/release_notes/deprecations/twilio/
    image: /assets/img/braze_icons/annotation.svg
  - name: Partenariat avec Grouparoo
    link: /docs/help/release_notes/deprecations/grouparoo
    image: /assets/img/braze_icons/users-01.svg
    
---

# Journal des Obsolescences

## Récepteur de diffusion personnalisée de notifications push pour Android

**Fin du support** : Octobre 2022

La prise en charge de Grouparo a été arrêtée en avril 2022.

L’utilisation d’un `BroadcastReceiver` personnalisé pour les notifications push est obsolète. Utilisez [` subscribeToPushNotificationEvents()`](/docs/developer_guide/platform_integration_guides/android/push_notifications/android/customization/custom_event_callback/) à la place.

## Partenariat avec Grouparoo

**Fin du support** : Avril 2022

La prise en charge de Grouparo a été arrêtée en avril 2022.

## SDK Windows Braze

**24 mars 2022 :** Le SDK Windows de Braze est obsolète et aucune nouvelle application Windows ne peut être créée dans le tableau de bord de Braze.<br>
**15 septembre 2022 :** Aucun nouveau message ne peut être envoyé aux applications Windows. Les messages existants et la collecte de données ne sont pas affectés.<br>
**15 janvier 2023 :** Braze ne sert plus de messages ni ne collecte de données à partir des applications Windows.

## Intégration des push Baidu

**24 mars 2022 :** L’intégration entre les push Baidu et Braze est obsolète et aucune nouvelle application Baidu ne peut être créée dans le tableau de bord de Braze. <br>
**15 septembre 2022 :** Aucun nouveau message push Baidu ne peut être créé. Les messages existants et la collecte de données ne sont pas affectés.<br>
**15 janvier 2023 :** Braze ne sert plus de messages ni ne recueille des données à partir des applications Baidu.

## Partenariat Amazon Moments

**Fin du support** : Juin 2020

Le support pour Amazon Moments a été arrêté en juin 2020. Amazon Moments est fusionné dans Amazon Advertising et a déconseillé leurs API et notre intégration.

## Partenariat Factual

**Fin du support** : Juin 2020

Le support pour Factual a été arrêté en juin 2020. Factual a récemment été acquis par Foursquare et ne s’intègre plus à la Plateforme Braze.

## Intégration du webhook Twilio

**Fin du support** : Janvier 2020

Le support pour l’[Intégration du webhook Twilio]({{site.baseurl}}/partners/twilio/) a été arrêté le 31 janvier 2020. Si vous souhaitez toujours accéder aux services SMS avec Braze, consultez notre [Documentation SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/).

## Partenariat Apptimize

**Fin du support** : Août 2019

Si vous utilisez actuellement [Apptimize avec Braze]({{site.baseurl}}/help/release_notes/deprecations/apptimize), vous ne subirez pas d’interruption de service. Vous pouvez toujours définir des attributs personnalisés Apptimize sur les profils utilisateur Braze. Cependant, aucune escalade de support formelle avec le partenaire ne sera fournie.

## Messages in-app originaux

**Fin du support** : Février 2019<br>
**Remplacé par** : [Messagerie In-App]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creating_an_in-app_message)

Braze a amélioré le look and feel des messages in-app pour se conformer aux meilleures pratiques en termes d’UX et d’IU, et Braze ne prend plus en charge les messages in-app originaux.

Braze est passé à une nouvelle forme de messages in-app avec les publications de SDK suivantes :
- iOS : `2.19.0`
- Android : `1.13.0`
- Web : `1.3.0`

Avant ces versions, Braze prenait en charge les « messages in-app originaux ». Auparavant, la prise en charge des messages in-app originaux était fournie à tout client qui effectuait une campagne in-app avant toute nouvelle version. Toutes les statistiques de campagne n’ont pas été affectées par ce changement, et ceux qui avaient envoyé des messages in-app originaux ont eu la possibilité d’en envoyer d’autres via le bouton **Create Campaign** (Créer une campagne) sur la page **Campaign** (Campagne).

## Widget « Commentaires »

**Fin du support** : 1er juillet 2019.

Le SDK Braze fournissait un widget de commentaires qui pouvait être ajouté à votre application pour permettre aux utilisateurs de laisser un feed-back en utilisant la méthode `submitfeedback` et en la transmettant à Desk.com ou Zendesk. Il était géré depuis le tableau de bord.

## Google Cloud Messaging (GCM)

**Fin du support** : Fin de prise en charge par Braze : Juillet 2018, fin de prise en charge par Google : 29 mai 2019<br>
**Remplacé par** : [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)

Google a [cessé de prendre GCM en charge](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html) depuis le 29 mai 2019. Braze a cessé le support GCM pour les SDK Android en juillet 2018, ce qui a été noté dans notre [Journal de modifications du SDK Android](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md). Cela signifie que les jetons GCM existants continueront de fonctionner, et vous pourrez envoyer des messages à vos utilisateurs existants. Mais vous ne pourrez pas envoyer de messages à des nouveaux utilisateurs.

Les clients qui n’ont pas encore migré vers [Messagerie cloud Firebase (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) peuvent être affecté par ce changement.

Si vous n’avez pas migré vers FCM, tous les enregistrements de jetons push GCM échoueront. Si vos applications prennent actuellement en charge GCM, vous devez travailler avec vos équipes de développement pour [passer de GCM à Firebase Cloud Messaging (FCM)](https://developers.google.com/cloud-messaging/android/android-migrate-fcm).

## Eclipse

**Fin du support** : 2014-2015<br>
**Remplacé par** : [Android Studio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)

Braze a arrêté sa prise en charge de l’IDE Eclipse, car Google [arrête sa prise en charge](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html) du plug-in Eclipse Android Developer Tools (ADT).  

Si vous avez besoin d’aide pour votre intégration Eclipse avant la migration, contactez notre [Service d’assistance]({{site.baseurl}}/support_contact/) pour obtenir de l’aide.

## Raw Event Stream (RES)

**Fin du support** : Juillet 2018<br>
**Remplacé par** : [Currents]({{site.baseurl}}/partners/braze_currents/about/)

Raw Event Stream était le prédécesseur de [Currents]({{site.baseurl}}/partners/braze_currents/about/), il a été arrêté pour laisser la place à Currents, l’avenir des données dans Braze.

## Delay while idle - Fonctionnalité GCM

**Fin du support** : Novembre 2016

Le paramètre « Delay While Idle » faisait autrefois partie des [Options de push GCM](https://developers.google.com/cloud-messaging/http-server-ref). Google a cessé de prendre en charge cette option le 15 novembre 2016. Auparavant, quand elle était configurée sur **true**, cela indiquait que le message ne devait pas être envoyé tant que l’appareil était inactif.

## Endpoints personnalisés

**Fin du support** : Décembre 2019

Suppression des Endpoints personnalisés. Si vous avez un endpoint personnalisé, vous pouvez continuer à l’utiliser, mais Braze n’en crée plus de nouveaux.


[15]: {% image_buster /assets/img_archive/in-app-choices.png %}
