---
nav_title: Benutzerdefinierte Sounds
article_title: Benutzerdefinierte Push-Benachrichtigungstöne für iOS
platform: Swift
page_order: 3
description: "Dieser Artikel behandelt die Implementierung benutzerdefinierter iOS-Sounds im Swift SDK."
channel:
  - push

---

# Benutzerdefinierte Klänge

## Schritt 1: Hosting des Sounds in der App

Benutzerdefinierte Push-Benachrichtigungstöne müssen lokal innerhalb des Haupt-Bundles Ihrer App gehostet werden. Die folgenden Audiodatenformate werden akzeptiert:

- Lineare PCM
- MA4
- µLaw
- aLaw

Sie können die Audiodaten in eine AIFF-, WAV- oder CAF-Datei packen. In Xcode fügen Sie die Sounddatei als nicht lokalisierte Ressource des Anwendungsbundles zu Ihrem Projekt hinzu.

{% alert note %}
Benutzerdefinierte Sounds müssen beim Abspielen unter 30 Sekunden bleiben. Wenn ein angepasster Sound dieses Limit überschreitet, wird stattdessen der standardmäßige Systemton abgespielt.
{% endalert %}

### Konvertieren von Tondateien

Sie können das Tool afconvert verwenden, um Töne zu konvertieren. Um zum Beispiel den linearen 16-Bit-PCM-Systemton Submarine.aiff in IMA4-Audio in einer CAF-Datei zu konvertieren, verwenden Sie den folgenden Befehl im Terminal:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
Sie können einen Sound untersuchen, um sein Datenformat zu bestimmen, indem Sie ihn im QuickTime Player öffnen und im Menü **Film** die Option **Filminspektor anzeigen** wählen.
{% endalert %}

## Schritt 2: Bereitstellung einer Protokoll-URL für den Sound

Sie müssen eine Protokoll-URL angeben, die auf den Speicherort der Sounddatei in Ihrer App verweist. Hierzu gibt es gibt zwei Methoden:

* Verwenden Sie den Parameter `sound` des [Apple Push-Objekts]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object), um die URL an Braze zu übergeben.
* Geben Sie die URL im Dashboard an. Wählen Sie im [Push Composer]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android) **Einstellungen** und geben Sie die Protokoll-URL in das Feld **Sound** ein. 

![Push Composer im Braze-Dashboard]({% image_buster /assets/img_archive/sound_push_ios.png %})

Wenn die angegebene Sounddatei nicht existiert oder das Schlüsselwort "default" eingegeben wird, verwendet Braze den standardmäßigen Alarmton des Geräts. Abgesehen von unserem Dashboard kann der Ton auch über unsere [Messaging API][12]] konfiguriert werden.

Weitere Informationen finden Sie in der Apple-Entwicklerdokumentation zur [Vorbereitung von benutzerdefinierten Warntönen](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html).

