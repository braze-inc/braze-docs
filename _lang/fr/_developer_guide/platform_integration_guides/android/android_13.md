---
nav_title: Guide de mise à niveau vers Android 13
article_title: Guide de mise à niveau vers Android 13
page_order: 9
platform: 
  - Android
  - FireOS
description: "Cet article concerne Android 13, les mises à niveau SDK, les modifications apportées aux autorisations des notifications push, la compatibilité SDK, etc."
---
<br>

{% alert important %}
Android 13 a atteint son [jalon de stabilité de la plateforme](https://developer.android.com/about/versions/13/overview#platform_stability) le 8 juin 2022. Toutes les modifications ont donc été finalisées et les utilisateurs d’applications pourront bientôt mettre à niveau leurs périphériques.
{% endalert %}

# Guide de mise à niveau du SDK pour Android 13

Ce guide décrit les modifications pertinentes introduites dans Android 13 (2022) et les étapes de mise à niveau requises pour l’intégration SDK Braze pour Android.

![Un graphique montrant le calendrier de lancement anticipé pour Android 13, la version finale se situant après juillet 2022.]({% image_buster /assets/img/android/android_13_timeline.png %}){: style="max-width:70%;border:0"}

Pour un guide de migration complet, consultez la [documentation du développeur pour Android 13][2].

## SDK Braze pour Android 13

Pour vous préparer à Android 13, veuillez mettre à niveau votre SDK Braze vers la [dernière version (v21.0.0 et ultérieures)][1]. Vous obtiendrez l’accès à notre nouvelle [fonctionnalité de base de notification push « sans code »][7].

## Modifications dans Android 13

### Autorisation de notification push {#push-permission}

Android 13 introduit une [modification majeure][3] dans la manière dont les utilisateurs gèrent les applications qui envoient des notifications push. Dans Android 13, les applications devront obtenir une autorisation avant que les notifications push ne puissent être affichées. 

![Un message de notification push Android demandant « Autoriser Kitchenerie à vous envoyer des notifications ? » avec deux boutons « Autoriser » et « Ne pas autoriser » au bas du message.]({% image_buster /assets/img/android/android-13-push-prompt.png %}){: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

Ce nouveau système d’autorisation suit un modèle similaire aux notifications push iOS et Web pour lesquelles une seule tentative d’obtenir l’autorisation est faite. Si un utilisateur choisit `Don't Allow` ou rejette la demande, votre application ne peut plus demander d’autorisation.

Notez que les applications obtiennent une [dérogation temporaire][4] destinée aux utilisateurs qui avaient préalablement reçu des notifications push de la part de cette application avant la mise à niveau vers Android 13. Ces utilisateurs resteront éligibles à la réception de notification push de la part de l’application jusqu’à ce que (A) ils refusent explicitement la demande d’autorisation lorsqu’elle s’affiche (ou dans les paramètres système), ou (B) l’application est ouverte pour la première fois après la mise à niveau vers Android 13 par l’utilisateur.

#### Délai de la demande d’autorisation {#push-permission-timing}

**Ciblage Android 13**

Les applications ayant un ciblage Android 13 peuvent contrôler quand elles demandent l’autorisation et afficher la demande de notification push native. 

Si votre utilisateur met Android 12 à niveau vers Android 13, que votre application était déjà installée et que vous envoyiez déjà des notifications push, vous obtiendrez une [autorisation temporaire][4] pour les afficher jusqu’à ce que l’utilisateur ouvre à nouveau votre application après la mise à niveau du périphérique.

Une fois votre application ouverte, les notifications push ne seront pas affichées à ces utilisateurs ayant réalisé la mise à niveau tant qu’ils n’auront pas donné leur consentement explicite à l’aide de la nouvelle demande d’autorisation de notification.

**Ciblage Android 12 ou d’une version antérieure**

Si votre application a in ciblage pas encore Android 13 alors, une fois qu’un utilisateur aura effectué la mise à niveau vers Android 13, il recevra automatiquement une demande d’autorisation de notification push lorsque votre application créera son premier canal de notification (via `notificationManager.createNotificationChannel`). 

{% alert note %}
Braze crée automatiquement un canal de notification par défaut s’il n’en existe pas déjà lorsqu’une notification push est reçue. Si vous ne ciblez pas Android 13, la demande d’autorisation de notification push s’affichera, ce qui est nécessaire pour afficher la notification.
{% endalert %}

## Se préparer à Android 13 {#next-steps}

Il est fortement recommandé de faire en sorte que votre application cible Android 13 afin de contrôler quand les utilisateurs recevront une demande d’autorisation de notification push.

Vous pourrez ainsi optimiser votre [taux d’abonnement aux notifications push][6] en invitant les utilisateurs à des moments plus appropriés, ce qui entraînera une meilleure expérience utilisateur en ce qui concerne le lieu et la manière des demandes d’autorisation de notification push.

Pour commencer à utiliser notre nouvelle [fonctionnalité de base de notification push « sans code »][7], mettez à niveau votre SDK Android vers la [dernière version (v21.0.0 et ultérieures)][1].

[1]: https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2100
[2]: https://developer.android.com/about/versions/13
[3]: https://developer.android.com/about/versions/13/changes/notification-permission
[4]: https://developer.android.com/about/versions/13/changes/notification-permission#eligibility
[5]: https://developer.android.com/about/versions/13/overview#platform_stability
[6]: https://www.braze.com/resources/articles/android-13-developer-preview-push-opt-ins-arrive-for-android-apps
[7]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/push_primer_messages/
