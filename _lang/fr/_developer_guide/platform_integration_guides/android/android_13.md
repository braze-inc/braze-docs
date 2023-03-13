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

# Guide de mise à niveau du SDK pour Android 13

Ce guide décrit les modifications pertinentes introduites dans Android 13 (2022) et les étapes de mise à niveau requises pour l’intégration SDK Braze pour Android.

Pour un guide de migration complet, consultez la [documentation du développeur pour Android 13][2].

## SDK Braze pour Android 13

Pour vous préparer à Android 13, veuillez mettre à niveau votre SDK Braze vers la [dernière version (v21.0.0+)][1]. Vous obtiendrez l’accès à notre nouvelle [fonctionnalité de base de notification push « sans code »][7].

## Modifications dans Android 13

### Autorisation de notification push {#push-permission}

Android 13 introduit une [modification majeure][3] dans la manière dont les utilisateurs gèrent les applications qui envoient des notifications push. Dans Android 13, les applications doivent obtenir une autorisation avant que les notifications push ne puissent être affichées. 

![Un message de notification push Android demandant « Autoriser Kitchenerie à vous envoyer des notifications ? » avec les deux boutons « Autoriser » et « Ne pas autoriser » au bas du message.]({% image_buster /assets/img/android/android-13-push-prompt.png %}){: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

Ce nouveau système d’autorisation suit un modèle similaire aux notifications push iOS et Web pour lesquelles une seule tentative d’obtenir l’autorisation est faite. Si un utilisateur choisit `Don't Allow` ou rejette la demande, votre application ne peut plus demander d’autorisation.

Notez que les applications obtiennent une [dérogation][4] temporaire destinée aux utilisateurs qui avaient préalablement reçu des notifications push de la part de cette application avant la mise à niveau vers Android 13. Ces utilisateurs [resteront éligibles][8] à la réception de notification push lorsqu’ils feront la mise à jour d’Android 13 sans devoir demander une autorisation.

#### Délai de la demande d’autorisation {#push-permission-timing}

**Ciblage Android 13**

Les applications ayant un ciblage Android 13 peuvent contrôler quand elles demandent l’autorisation et afficher la demande de notification push native. 

Si votre utilisateur passe d’Android 12 à 13, que votre application était installée et que vous envoyiez des notification push, le système pré-accorde automatiquement la nouvelle autorisation de notification à toutes les applications éligibles. En d’autres termes, ces applications peuvent continuer à envoyer des notifications aux utilisateurs et ces derniers ne visualisent pas d’invite d’autorisation de délai d’exécution.

Pour des précisions à ce sujet, consultez la Documentation du développeur Android [ pour connaître les effets sur les mises à jour des applications existantes][8].

**Ciblage Android 12 ou d’une version antérieure**

Si votre application a un ciblage pas encore Android 13, le nouvel utilisateur sur Android 13, il verra automatiquement une invite d’autorisation de notification push lorsque votre application créera son premier canal de notification (via `notificationManager.createNotificationChannel`). Les utilisateurs qui ont déjà installé votre application et passent ensuite à Android 13 ne reçoivent pas d’invite et reçoivent automatiquement l’autorisation de notification push.

{% alert note %}
Braze SDK v23.0.0 crée automatiquement un canal de notification par défaut s’il n’en existe pas déjà lorsqu’une notification push est reçue. Si vous ne ciblez pas Android 13, la demande d’autorisation de notification push s’affichera, ce qui est nécessaire pour afficher la notification.
{% endalert %}

## Se préparer à Android 13 {#next-steps}

Il est fortement recommandé de faire en sorte que votre application cible Android 13 afin de contrôler quand les utilisateurs recevront une demande d’autorisation de notification push.

Vous pourrez ainsi optimiser votre [taux d’abonnement aux notifications push ][6] en invitant les utilisateurs à des moments plus appropriés, ce qui entraînera une meilleure expérience utilisateur en ce qui concerne le lieu et la manière des demandes d’autorisation de notification push.

Pour commencer à utiliser notre nouvelle [fonctionnalité de base de notification push][7], « sans code »[, mettez à niveau votre SDK Android vers la dernière version (v23.0.0+)][1].

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300
[2]: https://developer.android.com/about/versions/13
[3]: https://developer.android.com/about/versions/13/changes/notification-permission
[4]: https://developer.android.com/about/versions/13/changes/notification-permission#eligibility
[5]: https://developer.android.com/about/versions/13/overview#platform_stability
[6]: https://www.braze.com/resources/articles/android-13-developer-preview-push-opt-ins-arrive-for-android-apps
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/
[8]: https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps
