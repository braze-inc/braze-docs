---
nav_title: Obsolescences
article_title: Obsolescences
page_order: 9
page_type: reference
description: "Cette page comprend des références à des articles obsolètes et fournit une liste de fonctionnalités obsolètes et non prises en charge."
---

# Obsolescences

La technologie est toujours en mouvement, à l'intérieur comme à l'extérieur de Braze ! Et nous faisons de notre mieux pour tenir la cadence. Vous y trouverez les origines de Braze et de sa technologie - comment nous avons aidé les gens dans le passé - avant aujourd'hui, en tout cas...

Vous êtes peut-être arrivé ici en faisant une recherche sur une intégration ou fonctionnalité qui n’existe plus. C’est notre manière de vous tenir informé de nos progrès et des mouvements au sein de l’industrie technologique. Vous pouvez trouver une liste de fonctions désactivées et non prises en charge et lire les articles associés en visitant les liens suivants.

## Articles obsolètes

- [Récepteur de diffusion personnalisée de notifications push pour Android]({{site.baseurl}}/help/release_notes/deprecations/custom_broadcast_receiver/)
- [Configuration du SDK Eclipse]({{site.baseurl}}/help/release_notes/deprecations/eclipse_setup_deprecated/)
- [TLS 1.0 et 1.1 deprecation)]({{site.baseurl}}/help/release_notes/deprecations/tls_deprecation/)
- [Intégration du webhook Twilio]({{site.baseurl}}/help/release_notes/deprecations/twilio/)
- [Partenariat Apptimize]({{site.baseurl}}/help/release_notes/deprecations/apptimize/)
- [Partenariat avec Grouparoo]({{site.baseurl}}/help/release_notes/deprecations/grouparoo)
- [Shopify `checkout.liquid` deprecation]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout/)

## Journal des Obsolescences

### Shopify `checkout.liquid`

**Soutien retiré**: Août 2024 (phase 1), août 2025 (phase 2)

La prise en charge de Shopify `checkout.liquid` commencera à être obsolète en août 2024 et se terminera en août 2025. Shopify va passer à [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions), qui est plus sûr, plus performant et plus personnalisable.

### Récepteur de diffusion personnalisée de notifications push pour Android

**Soutien retiré**: Octobre 2022

L’utilisation d’un `BroadcastReceiver` personnalisé pour les notifications push est obsolète. Utilisez plutôt [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events) à la place.

### Partenariat avec Grouparoo

**Soutien retiré**: Avril 2022

La prise en charge de Grouparo a été arrêtée en avril 2022.

### SDK Windows Braze

**Le 24 mars 2022**: Le SDK Windows de Braze est obsolète et aucune nouvelle application Windows ne peut être créée dans le tableau de bord de Braze.<br>
**Le 15 septembre 2022**: Aucun nouveau message ne peut être envoyé aux applications Windows. Les messages existants et la collecte de données ne sont pas affectés.<br>
**Le 11 janvier 2024**: Braze ne sert plus de messages ni ne collecte de données à partir des applications Windows.

### Intégration des push Baidu

**Le 24 mars 2022**: L’intégration entre les push Baidu et Braze est obsolète et aucune nouvelle application Baidu ne peut être créée dans le tableau de bord de Braze. <br>
**Le 15 septembre 2022**: Aucun nouveau message push Baidu ne peut être créé. Les messages existants et la collecte de données ne sont pas affectés.<br>
**Le 11 janvier 2024**: Braze ne sert plus de messages ni ne recueille des données à partir des applications Baidu.

### Variable globale appboyBridge

**Soutien retiré**: Mai 2021<br>
**Remplacé par**: `brazeBridge`

La variable globale `appboyBridge` est obsolète et remplacée par `brazeBridge`. `appboyBridge` continuera à fonctionner pour les clients existants, mais nous vous recommandons de migrer vers `brazeBridge` si vous utilisez `appboyBridge`.

### Partenariat Amazon Moments

**Soutien retiré**: Juin 2020

Le support pour Amazon Moments a été arrêté en juin 2020. Amazon Moments est fusionné dans Amazon Advertising et a déconseillé leurs API et notre intégration.

### Partenariat Factual

**Soutien retiré**: Juin 2020

Le support pour Factual a été arrêté en juin 2020. Factual a récemment été acquis par Foursquare et ne s’intègre plus à la Plateforme Braze.

### Intégration du webhook Twilio

**Soutien retiré**: Janvier 2020

La prise en charge de l'[intégration du webhook Twilio]({{site.baseurl}}/partners/twilio/) n'est plus assurée depuis le 31 janvier 2020. Si vous souhaitez continuer à accéder aux services SMS avec Braze, consultez notre [documentation sur les SMS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms/)

### Partenariat Apptimize

**Soutien retiré**: Août 2019

Si vous utilisez actuellement [Apptimize avec Braze]({{site.baseurl}}/help/release_notes/deprecations/apptimize), vous ne subirez pas d'interruption de service. Vous pouvez toujours définir des attributs personnalisés Apptimize sur les profils utilisateur Braze. Cependant, aucune escalade de support formelle avec le partenaire ne sera fournie.

### Messages in-app originaux

**Soutien retiré :** Février 2019<br>
**Remplacé par**: [in-app Messaging]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/)

Braze a amélioré le look and feel des messages in-app pour se conformer aux meilleures pratiques en termes d’UX et d’IU, et Braze ne prend plus en charge les messages in-app originaux.

Braze est passé à une nouvelle forme de messages in-app avec les publications de SDK suivantes :
- iOS : `2.19.0`
- Android : `1.13.0`
- Web : `1.3.0`

Avant ces versions, Braze prenait en charge les « messages in-app originaux ». Auparavant, la prise en charge des messages in-app originaux était fournie à tout client qui effectuait une campagne in-app avant toute nouvelle version. Toutes les statistiques de la campagne n'ont pas été affectées par ce changement, et ceux qui avaient envoyé des messages in-app originaux ont eu la possibilité d'en envoyer d'autres via le bouton **Créer une campagne de** la page **Campagne.** 

### Widget « Commentaires »

**Soutien retiré**: 1er juillet 2019.

Le SDK de Braze fournit un widget de feedback qui peut être ajouté à votre application pour permettre aux utilisateurs de laisser un feedback à l'aide de la méthode `submitfeedback` et de le transmettre à Desk.com ou Zendesk et qui est géré sur le tableau de bord.

### Google Cloud Messaging (GCM)

**Soutien retiré**: Fin de prise en charge par Braze : Juillet 2018, fin de prise en charge par Google : 29 mai 2019<br>
**Remplacé par**: [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)

Google a [supprimé la prise en charge de GCM](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html) à compter du 29 mai 2019. Braze a cessé de prendre en charge le GCM à partir des SDK Android en juillet 2018, ce qui a été noté au sein de nos [journaux des modifications des SDK Android](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md). Cela signifie que les jetons GCM existants continueront de fonctionner, et vous pourrez envoyer des messages à vos utilisateurs existants. Mais vous ne pourrez pas envoyer de messages à des nouveaux utilisateurs.

Les clients qui n'ont pas encore migré vers [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) peuvent être concernés par ce changement.

Si vous n’avez pas migré vers FCM, tous les enregistrements de jetons push GCM échoueront. Si vos apps prennent actuellement en charge GCM, vous devrez travailler avec vos équipes de développement sur la [transition de GCM vers Firebase Cloud Messaging (FCM).](https://developers.google.com/cloud-messaging/android/android-migrate-fcm)

### Eclipse

**Soutien retiré**: 2014-2015<br>
**Remplacé par**: [Android Studio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)

Braze a cessé de prendre en charge l'IDE Eclipse en raison de l’[abandon](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html) par Google de la prise en charge du plugin Eclipse Android Developer Tools (ADT). 

Si vous avez besoin d'aide pour l'intégration d'Eclipse avant la migration, contactez le [service d'assistance.]({{site.baseurl}}/support_contact/) 

### Raw Event Stream (RES)

**Soutien retiré**: Juillet 2018<br>
**Remplacé par**: [Currents]({{site.baseurl}}/user_guide/data/braze_currents/)

Le flux d'événements bruts était le prédécesseur de [Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/) et a été supprimé pour faire place à l'avenir des données à Braze.

### Delay while idle - Fonctionnalité GCM

**Soutien retiré**: Novembre 2016

Le paramètre Délai au repos faisait auparavant partie des [options de poussée du GCM.](https://developers.google.com/cloud-messaging/http-server-ref) Google a cessé de prendre en charge cette option le 15 novembre 2016. Auparavant, lorsque cette valeur était fixée à **true**, elle indiquait que le message ne devait pas être envoyé tant que l'appareil n'était pas actif.

### Endpoints personnalisés

**Soutien retiré**: Décembre 2019

Suppression des Endpoints personnalisés. Si vous avez un endpoint personnalisé, vous pouvez continuer à l’utiliser, mais Braze n’en crée plus de nouveaux.


