---
nav_title: Android 11 Upgrade-Anleitung
article_title: Android 11 Upgrade-Anleitung
page_order: 9
platform: 
  - Android
  - FireOS
description: "Dieser referenzierende Artikel behandelt das Android 11 SDK Update und hebt Änderungen wie Deeplinks, SDK-Kompatibilität und mehr hervor."
hidden: true
---

# Android 11 SDK upgrade Anleitung

Dieser Leitfaden beschreibt die relevanten Änderungen, die mit Android 11 (veröffentlicht am 8\. September 2020) eingeführt wurden, sowie die erforderlichen Upgrade-Schritte für Ihre Braze Android SDK-Integration.

Eine vollständige Anleitung zur Migration von Android 11 finden Sie in der [Dokumentation für Android-Entwickler](https://developer.android.com/preview/migration):in.

## Braze SDK Kompatibilität

Alle Apps, die _auf_ Android 11 (API 30) _zielen_, müssen auf [Braze Android SDK v8.1.0+](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810) upgraden, um die Messaging Features von Braze weiterhin nutzen zu können.

{% alert important %}
Aufgrund von Änderungen in den Android 11 APIs werden Apps, die auf Android 11 abzielen und nicht auf Braze Android SDK v8.1.0+ aktualisieren, Probleme mit Deeplinks von Braze UI-Komponenten haben und angepasste HTML In-App-Nachrichten nicht korrekt anzeigen.
{% endalert %}

### Deeplinks

Apps, die auf Android 11 oder höher (API Version 30+) Targeting betreiben, müssen auf [Braze Android SDK v8.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810) upgraden, um weiterhin Deeplinks innerhalb von Braze Nachrichten zu verwenden. Aufgrund einer Änderung der Android 11 APIs werden Apps, die nicht mindestens auf Android SDK v8.1.0 aktualisieren, Probleme mit Deeplinks innerhalb von Braze Nachrichten (In-App-Nachrichten oder Content-Cards) haben.

### HTML In-App-Nachrichten

Apps, die auf Android 11 oder höher (API Version 30+) zielen, müssen auf Braze Android SDK v8.1.0 upgraden, um weiterhin angepasste HTML In-App-Nachrichten verwenden zu können. Aufgrund einer Änderung in den Android 11 WebView-Einstellungen werden HTML In-App-Nachrichten auf Android 11 Targeting-Apps erst nach einem Upgrade auf [Braze Android SDK v8.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810) korrekt angezeigt. 

### Berechtigungen für Standorte

Apps, die Standort-Berechtigungen verwenden, sollten die [bewährten Praktiken](https://developer.android.com/preview/privacy/location#change-details) von Android befolgen, wenn sie den Zugriff auf Standorte anfragen. Für diese Updates der Standorte sind keine Änderungen an Ihrer Braze Integration erforderlich.

## Änderungen im Verhalten von Android 11

### Einmalige Berechtigungen zulassen

Nutzer:innen können jetzt Berechtigungen, wie z.B. die Erfassung von Standorten, einmalig erteilen (weitere Informationen finden Sie in den [Android Docs](https://developer.android.com/preview/privacy/location#one-time-access) ). Wenn eine App lange genug geschlossen oder im Hintergrund ist, wird diese Berechtigung automatisch entzogen. Die App müsste diese Erlaubnis bei Bedarf in Zukunft erneut anfragen. Apps, die bereits den empfohlenen Ablauf für die Anfrage von Standort-Berechtigungen befolgen, unterstützen einmalige Berechtigungen.

![]({% image_buster /assets/img/android/android-11-one-time-permission.svg %}){: height="230px" }

### Erlaubnis für Standorte im Hintergrund

In Android 11 müssen Apps zunächst die Erlaubnis für den Standort im Vordergrund anfragen. Wenn die App dann im Hintergrund läuft, kann sie den Nutzer:in erneut um die Erlaubnis für den Standort im Hintergrund bitten.
Kund:innen, die Geofences verwenden, sollten sicherstellen, dass ihre App den Empfehlungen von Android zur Erfassung von Berechtigungen für Standorte im Hintergrund folgt. Weitere Informationen finden Sie in den [Android Docs](https://developer.android.com/preview/privacy/location#background-location).

