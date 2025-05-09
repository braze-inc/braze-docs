# Mise à jour vers Android 13

> Ce guide décrit les modifications pertinentes introduites dans Android 13 (2022) et les étapes de mise à niveau requises pour l’intégration SDK Braze pour Android.

Reportez-vous à la [documentation destinée aux développeurs d'Android 13](https://developer.android.com/about/versions/13) pour obtenir un guide de migration complet.

## SDK Braze pour Android 13

Pour vous préparer à Android 13, veuillez mettre à jour votre SDK Braze vers la [dernière version (v21.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300). Vous aurez ainsi accès à notre nouvelle [fonctionnalité d'amorçage de notifications push « sans code »]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Modifications dans Android 13

### Autorisation des notifications push {#push-permission}

Android 13 introduit un [changement majeur](https://developer.android.com/about/versions/13/changes/notification-permission) dans la manière dont les gestionnaires gèrent les applications qui envoient des notifications push. Dans Android 13, les applications doivent obtenir une autorisation avant que les notifications push ne puissent être affichées. 

![Message d’autorisation des notifications push sous Android demandant « Autoriser Kitchenerie à vous envoyer des notifications ? » avec deux boutons, « Autoriser » et « Ne pas autoriser » au bas du message.]({% image_buster /assets/img/android/android-13-push-prompt.png %}){: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

Ce nouveau système d’autorisation suit un modèle similaire aux notifications push iOS et Web pour lesquelles une seule tentative d’obtenir l’autorisation est faite. Si un utilisateur choisit `Don't Allow` ou rejette la demande, votre application ne peut plus demander d’autorisation.

Notez que les apps bénéficient d'une [dérogation](https://developer.android.com/about/versions/13/changes/notification-permission#eligibility) pour les utilisateurs qui avaient déjà activé les notifications push avant la mise à jour vers Android 13. Ces utilisateurs pourront [continuer à](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps) recevoir des messages push lorsqu'ils passeront à Android 13, sans avoir à en demander l'autorisation.

#### Délai de demande d’autorisation {#push-permission-timing}

**Ciblage d'Android 13**

Les applications ayant un ciblage Android 13 peuvent contrôler quand elles demandent l’autorisation et afficher la demande de notification push native. 

Si votre utilisateur passe d’Android 12 à 13, que votre application était installée et que vous envoyiez des notification push, le système pré-accorde automatiquement la nouvelle autorisation de notification à toutes les applications éligibles. En d’autres termes, ces applications peuvent continuer à envoyer des notifications aux utilisateurs et ces derniers ne visualisent pas d’invite d’autorisation de délai d’exécution.

Pour plus de détails, consultez la documentation du développeur d'Android pour connaître les [effets des mises à jour sur les applications existantes](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps).

**Ciblage d'Android 12 ou d’une version antérieure**

Si votre application a un ciblage pas encore Android 13, le nouvel utilisateur sur Android 13, il verra automatiquement une invite d’autorisation de notification push lorsque votre application créera son premier canal de notification (via `notificationManager.createNotificationChannel`). Les utilisateurs qui ont déjà installé votre application et passent ensuite à Android 13 ne reçoivent pas d’invite et reçoivent automatiquement l’autorisation de notification push.

{% alert note %}
Braze SDK v23.0.0 crée automatiquement un canal de notification par défaut s’il n’en existe pas déjà lorsqu’une notification push est reçue. Si vous ne ciblez pas Android 13, la demande d’autorisation de notification push s’affichera, ce qui est nécessaire pour afficher la notification.
{% endalert %}

## Préparation pour Android 13 {#next-steps}

Il est fortement recommandé de faire en sorte que votre application cible Android 13 afin de contrôler quand les utilisateurs recevront une demande d’autorisation de notification push.

Vous pourrez ainsi optimiser votre [taux d’abonnement aux notifications push](https://www.braze.com/resources/articles/android-13-developer-preview-push-opt-ins-arrive-for-android-apps) en invitant les utilisateurs à des moments plus appropriés, ce qui entraînera une meilleure expérience utilisateur en ce qui concerne le lieu et la manière des demandes d’autorisation de notifications push.

Pour commencer à utiliser notre nouvelle [fonctionnalité d’amorçage des notifications push « sans code »]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/), mettez à niveau votre SDK Android vers la [dernière version (v23.0.0 et ultérieures)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300).

