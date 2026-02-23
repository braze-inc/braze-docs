---
nav_title: Android 12 Upgrade-Anleitung
article_title: Android 12 Upgrade-Anleitung
page_order: 9
permalink: "/android_12/"
layout: "dev_guide"
hidden: true
platform: 
  - Android
  - FireOS
description: "Dieser referenzierende Artikel behandelt das Android 12 SDK Update und hebt Änderungen wie Deeplinks, SDK-Kompatibilität und mehr hervor."
---

# Android 12 SDK upgrade Anleitung

Dieser Leitfaden beschreibt die relevanten Änderungen, die mit Android 12 (2021) eingeführt wurden, sowie die erforderlichen Upgrade-Schritte für Ihre Braze Android SDK-Integration.

Eine vollständige Anleitung zur Migration von Android 12 finden Sie in der [Dokumentation für Android-Entwickler](https://developer.android.com/about/versions/12):in.

## Braze SDK Kompatibilität

Wenn Sie auf Android 12 targeting, müssen Sie [Braze Android SDK v13.1.2+](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312) verwenden. Wenn Sie noch nicht auf Android 12 targeting, ist ein Upgrade dennoch empfehlenswert.

**Was passiert, wenn ich mein Braze Android SDK nicht upgraden möchte?**

* Aufgrund einer Änderung in den [Dialogen zum Schließen des Android-Systems](https://developer.android.com/about/versions/12/behavior-changes-all#close-system-dialogs) geben ältere Versionen des Braze Android SDK Warnungen aus, wenn Push-Benachrichtigungen auf Geräten mit Android 12 empfangen werden. Dieses Verhalten tritt auch dann auf, wenn Ihre App nicht auf Android 12 zielt.
* Änderungen an [Komponentenexporten](https://developer.android.com/about/versions/12/behavior-changes-12#exported), [ausstehenden Absichten](https://developer.android.com/about/versions/12/behavior-changes-12#pending-intent-mutability) und [Benachrichtigungstrampolinen](https://developer.android.com/about/versions/12/behavior-changes-12#notification-trampolines) können die Kompilierung Ihrer App beeinträchtigen oder die Initialisierung des Braze SDK verhindern. Dieses Verhalten tritt nur bei Apps auf, die auf Android 12 zielen.
* Änderungen bei [angepassten Push-Benachrichtigungen](https://developer.android.com/about/versions/12/behavior-changes-12#custom-notifications) haben das Layout für unser neues [Android Inline Image Push]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_sending-inline-images) Feature verändert. Dieses Verhalten tritt nur bei Apps auf, die auf Android 12 zielen.

