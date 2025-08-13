---
nav_title: Android 13 Upgrade-Anleitung
article_title: Android 13 Upgrade-Anleitung
page_order: 9
platform: 
  - Android
  - FireOS
description: "Dieser Artikel behandelt Android 13, SDK-Updates, Änderungen an der Push-Erlaubnis, SDK-Kompatibilität und mehr."
---
<br>

# Anleitung zum Upgrade für iOS 13

> Dieser Leitfaden beschreibt die für Braze relevanten Änderungen in Android 13 (2022) sowie die erforderlichen Upgrade-Schritte für Ihre Braze-Android-SDK-Integration.

Eine vollständige Anleitung zur Migration finden Sie in der [Dokumentation für Android 13 Entwickler](https://developer.android.com/about/versions/13):in.

## Android 13 Braze SDK

Um sich auf Android 13 vorzubereiten, upgraden Sie bitte Ihr Braze SDK auf die [neueste Version (v21.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300). Damit erhalten Sie Zugang zu unserem neuen ["No-Code"-Push Prime-Feature]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/).

## Änderungen in Android 13

### Push-Genehmigung {#push-permission}

Mit Android 13 [ändert sich die](https://developer.android.com/about/versions/13/changes/notification-permission) Art und Weise, wie Nutzer:innen Apps verwalten, die Push-Benachrichtigungen senden, [erheblich](https://developer.android.com/about/versions/13/changes/notification-permission). In Android 13 müssen Apps eine Genehmigung einholen, bevor Push-Benachrichtigungen angezeigt werden können. 

![Eine Android Push-Nachricht mit der Frage "Erlauben Sie Kitchenerie, Ihnen Benachrichtigungen zu senden?" mit zwei Buttons "Zulassen" und "Nicht zulassen" am unteren Rand der Nachricht.]({% image_buster /assets/img/android/android-13-push-prompt.png %}){: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

Diese neue Berechtigung folgt einem ähnlichen Muster wie bei iOS und Web-Push, wo Sie nur einen Versuch haben, die Berechtigung zu erhalten. Wenn ein Nutzer `Don't Allow` wählt oder die Aufforderung ablehnt, kann Ihre App nicht erneut um Erlaubnis bitten.

Beachten Sie, dass für Nutzer von Apps, die vor dem Update auf Android 13 Push-Benachrichtigungen aktiviert hatten, eine [Ausnahme](https://developer.android.com/about/versions/13/changes/notification-permission#eligibility) gewährt wird. Diese Nutzer können auch nach dem Update auf Android 13 [weiterhin Push-Nachrichten erhalten](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps), ohne dass sie eine Genehmigung einholen müssen.

#### Timing der Erlaubnisaufforderung {#push-permission-timing}

**Targeting Android 13**

Apps, die auf Android 13 zielen, können steuern, wann die Erlaubnis angefragt und die native Push-Aufforderung angezeigt werden soll. 

Wenn Ihr Nutzer:innen von Android 12 auf 13 upgraden, Ihre App zuvor installiert war und Sie bereits Push-Benachrichtigungen verschickt haben, gewährt das System allen in Frage kommenden Apps automatisch die neue Berechtigung für die Benachrichtigung. Mit anderen Worten: Diese Apps können weiterhin Benachrichtigungen an Nutzer:innen senden, und die Nutzer:innen sehen keine Aufforderung zur Laufzeitgenehmigung.

Weitere Einzelheiten hierzu finden Sie in der Dokumentation für Entwickler:in von Android für die [Auswirkungen von Updates auf bestehende Apps](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps).

**Targeting Android 12 oder früher**

Wenn Ihre App noch kein Targeting für Android 13 hat und ein neuer Nutzer:innen auf Android 13 Ihre App installiert, wird er automatisch eine Push-Erlaubnisaufforderung sehen, wenn Ihre App ihren ersten Benachrichtigungskanal erstellt (über `notificationManager.createNotificationChannel`). Nutzer:innen, die Ihre App bereits installiert haben und dann auf Android 13 upgraden, werden nie gefragt und erhalten automatisch die Push-Erlaubnis.

{% alert note %}
Braze SDK v23.0.0 erstellt beim Empfang einer Push-Benachrichtigung automatisch einen Standard-Benachrichtigungskanal, wenn er noch nicht vorhanden ist. Wenn Sie nicht auf Android 13 abzielen, wird die Aufforderung zur Push-Erlaubnis angezeigt, die für die Anzeige der Push-Benachrichtigung erforderlich ist.
{% endalert %}

## Vorbereitungen für Android 13 {#next-steps}

Es wird dringend empfohlen, dass Ihre App auf Android 13 abzielt, um zu kontrollieren, wann Nutzer zur Push-Erlaubnis aufgefordert werden.

Auf diese Weise können Sie Ihre [Push Opt-in-Raten](https://www.braze.com/resources/articles/android-13-developer-preview-push-opt-ins-arrive-for-android-apps) optimieren, indem Sie die Nutzer:innen zu geeigneteren Zeitpunkten um Erlaubnis für Push bitten, was zu einem besseren Nutzer:innen-Erlebnis führt.

Um unser neues ["No-Code"-Push-Primer Feature]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/) zu nutzen, upgraden Sie Ihr Android SDK auf die [neueste Version (v23.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300).

