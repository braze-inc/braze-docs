---
nav_title: Deaktivieren des SDK-Trackings
article_title: Deaktivieren der Datenerfassung für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 8
description: "Dieser Artikel zeigt, wie Sie die Datenerfassung für Ihre Android- oder FireOS-Anwendung deaktivieren können."

---

# Deaktivieren des SDK-Trackings

> Dieser Artikel zeigt, wie Sie die Datenerfassung für Ihre Android- oder FireOS-Anwendung deaktivieren können.

Zur Einhaltung von Datenschutzvorschriften kann das Tracking von Daten im Android SDK mit der Methode [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html) gänzlich unterbunden werden. Diese Methode bewirkt, dass alle Netzwerkverbindungen abgebrochen werden und das Braze SDK keine Daten an die Braze-Server übergibt. Wenn Sie die Datenerfassung zu einem späteren Zeitpunkt wieder aufnehmen möchten, können Sie dies mit der Methode [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html) tun.

Außerdem können Sie die Methode [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) verwenden, um alle auf dem Gerät gespeicherten clientseitigen Daten vollständig zu löschen.

