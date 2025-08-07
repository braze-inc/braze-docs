---
nav_title: Benutzerdefinierte Sounds
article_title: Benutzerdefinierte Push-Benachrichtigungstöne für iOS
platform: iOS
page_order: 3
description: "Dieser referenzierte Artikel behandelt die Implementierung angepasster Sounds in Ihren iOS Push-Benachrichtigungen."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Benutzerdefinierte Klänge

## Schritt 1: Hosting des Sounds in der App

Angepasste Push-Benachrichtigungstöne müssen lokal innerhalb des Hauptbündels der Client-Anwendung gehostet werden. Die folgenden Audiodatenformate werden akzeptiert:

- Lineare PCM
- MA4
- µLaw
- aLaw

Sie können die Audiodaten in eine AIFF-, WAV- oder CAF-Datei packen. In Xcode fügen Sie die Sounddatei als nicht lokalisierte Ressource des Anwendungsbundles zu Ihrem Projekt hinzu.

Sie können das Tool afconvert verwenden, um Töne zu konvertieren. Um zum Beispiel den linearen 16-Bit-PCM-Systemton Submarine.aiff in IMA4-Audio in einer CAF-Datei zu konvertieren, verwenden Sie den folgenden Befehl im Terminal:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

Sie können einen Sound untersuchen, um sein Datenformat zu bestimmen, indem Sie ihn im QuickTime Player öffnen und im Menü **Film** die Option **Filminspektor anzeigen** wählen.

Benutzerdefinierte Sounds müssen beim Abspielen unter 30 Sekunden bleiben. Wenn ein angepasster Sound dieses Limit überschreitet, wird stattdessen der standardmäßige Systemton abgespielt.

## Schritt 2: Das Dashboard mit einer Protokoll-URL für den Ton versorgen

Ihr Sound muss lokal in der App gehostet werden. Sie müssen im Feld **Sound** des Push Composers eine Protokoll-URL angeben, die auf den Standort der Sounddatei in der App verweist. Wenn Sie in diesem Feld "default" angeben, wird der standardmäßige Benachrichtigungston auf dem Gerät abgespielt. Dies kann über unsere [Messaging API]({{site.baseurl}}/api/endpoints/messaging/) oder unser Dashboard unter **Einstellungen** im Push Composer festgelegt werden, wie im folgenden Screenshot zu sehen ist:

![]({% image_buster /assets/img_archive/sound_push_ios.png %})

Wenn die angegebene Sounddatei nicht existiert oder das Schlüsselwort "default" eingegeben wird, verwendet Braze den standardmäßigen Alarmton des Geräts. Abgesehen von unserem Dashboard kann der Ton auch über unsere [Messaging API]({{site.baseurl}}/api/endpoints/messaging/) konfiguriert werden. Weitere Informationen finden Sie in der Apple-Entwicklerdokumentation zur [Vorbereitung von benutzerdefinierten Warntönen](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html).

