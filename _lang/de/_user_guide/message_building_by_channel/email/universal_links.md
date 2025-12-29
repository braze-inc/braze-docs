---
nav_title: Universelle Links und App-Links
article_title: Universelle Links und App-Links
page_order: 6.4
page_type: reference
description: "Dieser Hilfeartikel zeigt Ihnen, wie Sie Apple Universal Links und Android App Links einrichten."
channel: email
---

# Universelle Links und App-Links

Apple Universal Links und Android App Links sind Mechanismen, die für einen nahtlosen Übergang zwischen Webinhalten und mobilen Apps sorgen. Während universelle Links spezifisch für iOS sind, dienen Android App Links demselben Zweck für Android-Anwendungen.

## Wie Universal Links und App Links funktionieren

Universal Links (iOS) und App Links (Android) sind Standard-Web-Links (`http://mydomain.com`), die sowohl auf eine Webseite als auch auf einen Inhalt innerhalb einer App verweisen.

Wenn ein Universal Link oder App Link geöffnet wird, prüft das Betriebssystem, ob eine installierte App für diese Domain registriert ist. Wenn eine App gefunden wird, wird sie sofort gestartet, ohne die Webseite zu laden. Wenn keine App gefunden wird, wird die Internet-URL im Standard Webbrowser des Nutzers:innen geladen, der auch so konfiguriert werden kann, dass er zum App Store bzw. Google Play Store weiterleitet.

Wenn ein Nutzer:innen also auf einen Link zu einer Webseite klickt, die einem App-Bildschirm entspricht, kann die App direkt geöffnet werden (sofern die App derzeit installiert ist).

In dieser Tabelle finden Sie die wichtigsten Unterschiede zwischen universellen Links und herkömmlichen Deeplinks:

|                        | Universelle Links und App-Links                                  | Deeplinks                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| Plattform-Kompatibilität | iOS (Version 9 und höher) und Android (Version 6.0 und höher)  | Verwendet in verschiedenen mobilen Betriebssystemen    |
| Zweck                | Verknüpfen Sie nahtlos Web- und App-Inhalte auf iOS- und Android-Geräten | Link zu bestimmten Inhalten der App |
| Funktion               | Leitet kontextabhängig zu Webseiten oder App-Inhalten weiter           | Öffnet bestimmte App-Bildschirme   |
| App Installation       | Öffnet die App, wenn die App installiert ist, andernfalls werden Webinhalte geöffnet | Erfordert die Installation einer App |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Anwendungsfälle

Universal Links und App Links werden am häufigsten für Kampagnen verwendet, da E-Mails sowohl von Desktop- als auch von mobilen Geräten aus geöffnet und angeklickt werden können.

Einige Kanäle funktionieren nicht gut mit diesen Links. Zum Beispiel sollten Push-Benachrichtigungen, In-App-Nachrichten und Content-Cards schema-basierte Deeplinks (`mydomain://`) verwenden.

{% alert note %}
Android App Links erfordern eine angepasste `IBrazeDeeplinkHandler` mit Logik, um Links von ihren Domains getrennt von anderen Web-URLs zu behandeln. Es kann einfacher sein, stattdessen Deeplinks zu setzen und die Verlinkungspraktiken für andere Kanäle als E-Mail einheitlich zu halten.
{% endalert %}

## Voraussetzungen

Zur Verwendung von Universal Links und App Links:

- Ihre Website muss über HTTPS zugänglich sein
- Ihre App muss im App Store (iOS) oder im Google Play Store (Android) verfügbar sein

## Einrichten von Universal Links und App Links

Damit Apps universelle Links oder App-Links unterstützen können, benötigen sowohl iOS als auch Android eine spezielle Berechtigungsdatei, die in der Link Domain gehostet wird. Diese Datei enthält Definitionen darüber, welche Apps in der Lage sind, Links von dieser Domain zu öffnen und, für iOS, welche Pfade diese Apps öffnen dürfen:

- **iOS:** Apple App Site Association (AASA) Datei
- **Android:** Digital Asset Links Datei

Zusätzlich zu dieser Berechtigungsdatei gibt es hart kodierte Definitionen, welche Link Domains die App öffnen darf, die innerhalb der App eingerichtet werden:

- **iOS:** Als "Zugehörige Domains" in Xcode festlegen
- **Android:** Definiert in der Datei `AndroidManifest.xml` der App

Diese zweiteilige Domain-App-Verknüpfung ist erforderlich, damit ein universeller Link oder ein App-Link funktioniert und verhindert, dass eine App Links von einer bestimmten Domain entführt oder eine Domain eine bestimmte App öffnet.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

Diese Schritte sind der Dokumentation für Entwickler:in von Apple entnommen. Weitere Informationen finden Sie unter [Apps und Websites erlauben, auf Ihre Inhalte zu verlinken](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc).

### Schritt 1: Konfigurieren Sie Ihre App-Berechtigungen

{% alert note %}
[In Xcode 13 und höher](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/) kann Xcode die Bereitstellung von Berechtigungen automatisch für Sie übernehmen. Sie können wahrscheinlich zu [Schritt 1c](#step-1c) übergehen und auf diese Anleitung zurückgreifen, wenn Sie Probleme haben.
{% endalert %}

#### Schritt 1a: Registrieren Sie Ihre App {#step-1a}

1. Gehen Sie auf developer.apple.com und melden Sie sich an.
2. Klicken Sie auf **Zertifikate, Bezeichner & Profile**.
3. Klicken Sie auf **Bezeichner**.
4. Wenn Sie noch keinen registrierten App Bezeichner haben, klicken Sie auf +, um einen zu erstellen.
   a. Geben Sie einen **Namen** ein. Das kann alles sein, was Sie wollen.
   b. Geben Sie die **Bundle ID** ein. Sie können Ihre Bundle ID auf dem Tab **Allgemein** Ihres Xcode-Projekts finden, um das richtige Targeting zu finden.

#### Schritt 1b: Aktivieren Sie Assoziierte Domains in Ihrem Bezeichner für die App

1. Suchen Sie in Ihrem bestehenden oder neu erstellten App Bezeichner den Abschnitt **App Serviceleistungen; Dienste**.
2. Wählen Sie **Assoziierte Domains** aus.
3. Klicken Sie auf **Speichern**.

![]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### Schritt 1c: Aktivieren Sie Assoziierte Domains in Ihrem Xcode-Projekt {#step-1c}

Bevor Sie fortfahren, vergewissern Sie sich, dass in Ihrem Xcode-Projekt das gleiche Team ausgewählt ist, in dem Sie gerade Ihren Bezeichner für die App registriert haben. 

1. Gehen Sie in Xcode auf den Tab **Fähigkeiten** Ihrer Projektdatei.
2. Aktivieren Sie **Assoziierte Domains**.

##### Tipp für die Fehlerbehebung

Wenn Sie die Fehlermeldung "Eine App ID mit dem Bezeichner 'your-app-id' ist nicht verfügbar. Bitte geben Sie einen anderen String ein", gehen Sie folgendermaßen vor:

1. Überprüfen Sie, ob Sie das richtige Team ausgewählt haben.
2. Vergewissern Sie sich, dass die Bundle ID[(Schritt 1a](#step-1a)) Ihres Xcode-Projekts mit der ID übereinstimmt, mit der Sie den Bezeichner für die App registriert haben.

#### Schritt 1d: Fügen Sie die Domain-Berechtigung hinzu

Fügen Sie im Bereich Domains den entsprechenden Tag für die Domain hinzu. Sie müssen das Präfix `applinks:` verwenden. In diesem Fall können Sie sehen, dass wir `applinks:yourdomain.com` hinzugefügt haben.

![]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### Schritt 1e: Vergewissern Sie sich, dass die Datei mit den Berechtigungen im Build enthalten ist

Vergewissern Sie sich im Projektbrowser, dass Ihre neue Berechtigungsdatei unter **Zielmitgliedschaft** ausgewählt ist.

Xcode sollte dies automatisch erledigen.

### Schritt 2: Konfigurieren Sie Ihre Website, um die AASA-Datei zu hosten

Um Ihre Website Domain mit Ihrer nativen App auf iOS zu verknüpfen, müssen Sie die Apple App Site Association (AASA) Datei auf Ihrer Website hosten. Diese Datei dient als sicherer Weg, um den Besitz von Domains gegenüber iOS zu überprüfen. Vor iOS 9 konnten Entwickler:in jedes beliebige URI-Schema registrieren, um ihre Apps zu öffnen, ohne dass eine Überprüfung stattfand. Mit AASA ist dieser Prozess jedoch viel sicherer und zuverlässiger geworden.

Die AASA-Datei enthält ein JSON-Objekt mit einer Liste von Apps und den URL-Pfaden auf der Domain, die als universelle Links ein- oder ausgeschlossen werden sollen. Hier ist ein Beispiel für eine AASA-Datei:

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": “JHGFJHHYX.com.facebook.ios",
        "paths": [
          "*"
        ]
      }
    ]
  }
}
```

- `appID`: Erstellt durch die Kombination der **Team ID** Ihrer App (gehen Sie zu `https://developer.apple.com/account/#/membership/`, um die Team ID zu erhalten) und des **Bundle Identifiers**. Im obigen Beispiel ist "JHGFJHHYX" die ID des Teams und "com.facebook.ios" ist die ID des Pakets.
- `paths`: String-Array mit Strings, die angeben, welche Pfade von der Zuordnung ein- oder ausgeschlossen werden. Sie können `NOT` vor der Pfadangabe verwenden, um Pfade zu deaktivieren. In diesem Beispiel führen alle Links auf diesem Pfad ins Internet, anstatt die App zu öffnen. Sie können `*` als Platzhalter verwenden, um alle Pfade in einem Verzeichnis zu aktivieren, und `?`, um ein einzelnes Zeichen abzugleichen (z.B. /archives/201?/, um alle Nummern von 2010-2019 abzugleichen).

{% alert note %}
Bei diesen Strings wird die Groß- und Kleinschreibung beachtet. Abfrage-Strings und Bezeichner von Fragmenten werden ignoriert.
{% endalert %}

### Schritt 3: Hosten Sie die AASA-Datei auf Ihrer Domain

Wenn Sie mit Ihrer AASA-Datei fertig sind, können Sie sie nun auf Ihrer Domain entweder unter `https://<<yourdomain>>/apple-app-site-association` oder unter `https://<<yourdomain>>/.well-known/apple-app-site-association` hosten.

Laden Sie die Datei `apple-app-site-association` auf Ihren HTTPS-Webserver hoch. Sie können die Datei im Stammverzeichnis Ihres Servers oder im Unterverzeichnis `.well-known` ablegen. Hängen Sie nicht `.json` an den Dateinamen an.

{% alert important %}
iOS wird nur versuchen, die AASA-Datei über eine sichere Verbindung (HTTPS) abzurufen.
{% endalert %}

Achten Sie beim Hosten der AASA-Datei darauf, dass die Datei diesen Richtlinien entspricht:

- Wird über HTTPS bereitgestellt.
- Verwendet den MIME-Typ `application/json`.
- Übersteigt nicht 128 KB (Voraussetzung in iOS 9.3.1 und höher)

### Schritt 4: Bereiten Sie Ihre App auf den Umgang mit universellen Links vor

Wenn ein Nutzer:innen auf einem iOS-Gerät auf einen universellen Link tippt, startet das Gerät die App und sendet ihr ein [NSUserActivity-Objekt](https://developer.apple.com/documentation/foundation/nsuseractivity). Die App kann dann das NSUserActivity-Objekt abfragen, um festzustellen, wie sie gestartet wurde.

Um universelle Links in Ihrer App zu unterstützen, führen Sie die folgenden Schritte aus:

1. Fügen Sie eine Berechtigung hinzu, die die Domains angibt, die Ihre App unterstützt.
2. Aktualisieren Sie Ihren App-Delegaten, damit er angemessen reagiert, wenn er das NSUserActivity-Objekt erhält.

Öffnen Sie in Xcode den Abschnitt **Assoziierte Domains** auf dem Tab **Fähigkeiten** und fügen Sie für jede Domain, die Ihre App unterstützt, einen Eintrag mit dem Präfix `applinks:` hinzu. Zum Beispiel: `applinks:www.mywebsite.com`.

{% alert note %}
Apple empfiehlt, diese Liste auf nicht mehr als 20 bis 30 Domains zu beschränken.
{% endalert %}

### Schritt 5: Testen Sie Ihren Universal Link

Fügen Sie den universellen Link zu einer E-Mail hinzu und senden Sie diese an ein Gerät, das Sie testen möchten. Wenn Sie einen universellen Link direkt in das Safari-URL-Feld einfügen, wird die App nicht automatisch geöffnet. Wenn Sie dies tun, müssen Sie die Website manuell nach unten ziehen, damit oben eine Aufforderung erscheint, die entsprechende App zu öffnen.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

Diese Schritte sind der Dokumentation für Android Entwickler:in entnommen. Weitere Informationen finden Sie unter [Android App-Links hinzufügen](https://developer.android.com/training/app-links#add-app-links) und [Deeplinks zu App-Inhalten setzen](https://developer.android.com/training/app-links/deep-linking).

{% alert note %}
Android App Links erfordern eine angepasste `IBrazeDeeplinkHandler` mit Logik, um Links von ihren Domains getrennt von anderen Web-URLs zu behandeln. Es kann einfacher sein, stattdessen Deeplinks zu setzen und die Verlinkungspraktiken für andere Kanäle als E-Mail einheitlich zu halten.
{% endalert %}

### Schritt 1: Deeplinks setzen

Zunächst müssen Sie Deeplinks für Ihre Android App setzen. Dazu können Sie in Ihrer Datei `AndroidManifest.xml` [Filter für Absichten](https://developer.android.com/guide/components/intents-filters) hinzufügen. Der Filter für die Absicht sollte die Aktion `VIEW` und die Kategorie `BROWSABLE` sowie die URL Ihrer Website im Datenelement enthalten.

### Schritt 2: Verknüpfen Sie Ihre App mit Ihrer Website

Sie müssen Ihre App mit Ihrer Website verknüpfen. Dazu können Sie eine Datei mit digitalen Asset-Links erstellen. Diese Datei sollte im JSON-Format vorliegen und enthält Angaben zu den Android-Apps, die Links zu Ihrer Website öffnen können. Sie sollte in das Verzeichnis `.well-known` Ihrer Website gestellt werden.

### Schritt 3: Aktualisieren Sie Ihre App-Manifestdatei

Fügen Sie in Ihrer Datei `AndroidManifest.xml` ein Element mit Metadaten innerhalb des Anwendungselements hinzu. Das Metadaten-Element sollte ein `android:name` Attribut von "asset_statements" und ein `android:resource` Attribut haben, das auf eine Ressourcendatei mit einem String-Array verweist, das die URL Ihrer Website enthält.

### Schritt 4: Bereiten Sie Ihre App auf den Umgang mit Deeplinks vor

In Ihrer Android App müssen Sie die eingehenden Deeplinks behandeln. Sie können dies tun, indem Sie die Absicht ermitteln, mit der Ihre Aktivität begonnen hat, und die Daten daraus extrahieren.

### Schritt 5: Testen Sie Ihre Deeplinks

Schließlich können Sie Ihre Deeplinks testen. Senden Sie sich selbst einen Link über eine Messaging App oder E-Mail und klicken Sie ihn an. Wenn alles richtig eingestellt ist, sollte Ihre App geöffnet werden.

{% endtab %}
{% endtabs %}

## Universelle Links, App Links und Click-Tracking

{% alert note %}
Click-Tracking-Links werden in der Regel als Teil Ihres Onboardings für E-Mails eingerichtet. Wenn dies beim Onboarding des Kunden nicht geschehen ist, wenden Sie sich bitte an Ihren Account Manager:in, um Hilfe zu erhalten.
{% endalert %}

Unsere Partner für das Versenden von E-Mails, SendGrid und SparkPost, verwenden Domains für das Click-Tracking, um alle Links zu verpacken und URL-Parameter für das Click-Tracking in E-Mails von Braze einzubinden.

Zum Beispiel wird ein Link wie `https://www.example.com` zu einem Link wie `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`.

Damit E-Mail-Links mit Click-Tracking als universelle Links oder App-Links funktionieren können, müssen Sie einige zusätzliche Einstellungen vornehmen. Vergewissern Sie sich, dass Sie die Domain für das Tracking von Klicks (`links.email.example.com`) als Domain hinzufügen, deren Öffnung für die App zulässig ist. Außerdem sollte die Click-Tracking Domain die AASA (iOS) oder Digital Asset Links (Android) Dateien bereitstellen. So können Sie sicherstellen, dass E-Mail-Links mit Click-Tracking nahtlos funktionieren.

Wenn Sie nicht möchten, dass jeder Klick-Tracking-Link ein universeller Link oder App-Link ist, können Sie auf der Grundlage des E-Mail versendenden Partners festlegen, welche Links universelle Links sein sollen. Einzelheiten finden Sie in den folgenden Abschnitten.

### SendGrid

So behandeln Sie einen SendGrid Click-Tracking-Link wie einen universellen Link:

1. Richten Sie Ihre AASA- oder AndroidManifest pathPrefix-Werte so ein, dass nur Links mit `/uni/` im URL-Pfad als universelle Links behandelt werden.
2. Fügen Sie das Attribut `universal="true"` zum Anker-Tag Ihres Links hinzu (`<a>`). Dadurch wird der URL-Pfad des umgeschlagenen Links so geändert, dass er `/uni/` enthält.

{% alert note %}
Für AMP-E-Mails sollte dieses Attribut data-universal="true" sein.
{% endalert %}

Zum Beispiel:

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3\. Vergewissern Sie sich, dass Ihre App so eingerichtet ist, dass sie die umgeschlagenen Links richtig verarbeitet. Lesen Sie den Artikel von SendGrid über das [Auflösen von SendGrid Click Tracking Links](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) und befolgen Sie die Schritte für Ihr Betriebssystem. Dieser Artikel enthält Beispiel-Code für [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) und [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android).

Mit dieser Konfiguration funktionieren Links mit `/uni/` im URL-Pfad als universelle Links, während alle anderen Links als Weblinks funktionieren.

### SparkPost

Um einen SparkPost-Link zum Tracking von Klicks als universellen Link zu behandeln, fügen Sie das folgende Attribut in den Abschnitt Attribute des Drag-and-Drop-Editors für E-Mails ein oder bearbeiten Sie den HTML-Code des Links manuell, um das folgende Attribut in den Anker-Tag des Links einzufügen: `data-msys-sublink="custom_path"`.

Dieser angepasste Pfad ermöglicht es Ihnen, URLs mit diesem Wert selektiv als universellen Link zu behandeln.

Zum Beispiel:

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

Stellen Sie dann sicher, dass Ihre App so eingerichtet ist, dass sie den angepassten Pfad richtig verarbeiten kann. Lesen Sie den SparkPost-Artikel über die [Verwendung von SparkPost Click Tracking für Deeplinks](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links). Dieser Artikel enthält Beispiel-Code für [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) und [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost).

### Deaktivieren des Trackings von Klicks auf einer Link-zu-Link-Basis

Sie können das Tracking von Klicks für bestimmte Links deaktivieren, indem Sie Ihrer Nachricht für den HTML-Editor oder einem HTML-Block für den Drag-and-Drop-Editor einen HTML-Code hinzufügen.

#### SendGrid

Wenn Ihr E-Mail Dienstanbieter SendGrid ist, verwenden Sie den HTML Code `clicktracking=off` wie folgt:

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost 

Wenn Ihr E-Mail-Dienst SparkPost ist, verwenden Sie den HTML Code `data-msys-clicktrack="0"` wie folgt:

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

Wenn Ihr E-Mail-Dienstanbieter Amazon SES ist, verwenden Sie den HTML Code `ses:no-track` wie folgt:

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### Drag-and-Drop-Editor

Wenn Sie den Drag-and-Drop-Editor für E-Mails verwenden, geben Sie Ihren HTML-Code als angepasstes Attribut ein, wenn Ihr Link an einen Text, einen Button oder ein Bild angehängt ist.

##### Angepasstes Attribut für einen Textlink

#### SendGrid

Wählen Sie für das angepasste Attribut Folgendes aus:

- **Name:** `clicktracking`
- **Wert:** `off`

#### SparkPost

Wählen Sie für das angepasste Attribut Folgendes aus:

- **Name:** `data-msys-clicktrack`
- **Wert:** `0`

![Ein angepasstes Attribut für einen Textlink.]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### Angepasstes Attribut für einen Button oder ein Bild

#### SendGrid

Wählen Sie für das angepasste Attribut Folgendes aus:

- **Name:** `clicktracking`
- **Wert:** `off`
- **Typ:** Link

#### SparkPost

Wählen Sie für das angepasste Attribut Folgendes aus:

- **Name:** `data-msys-clicktrack`
- **Wert:** `0`
- **Typ:** Link

![Ein angepasstes Attribut für einen Button.]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### Fehlerbehebung bei universellen Links mit Click-Tracking

Wenn Ihre universellen Links in Ihren E-Mails nicht wie erwartet funktionieren, z.B. wenn der Empfänger von seiner E-Mail App zum Webbrowser navigiert, bevor er schließlich zur App weitergeleitet wird, finden Sie hier Tipps zur Fehlerbehebung bei der Einrichtung Ihrer universellen Links.

#### Überprüfen Sie den Standort der Link-Datei

Stellen Sie sicher, dass sich die AASA-Datei (iOS) bzw. die Digital Asset Links-Datei (Android) am richtigen Standort befindet:

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

Es ist wichtig, sicherzustellen, dass diese Dateien immer öffentlich zugänglich sind. Wenn Sie nicht darauf zugreifen können, haben Sie möglicherweise einen Schritt bei der Einrichtung der universellen Links für E-Mails übersehen.

#### Domain-Definitionen überprüfen

Stellen Sie sicher, dass Sie die richtigen Definitionen für die Domains haben, die Ihre App öffnen darf.

- **iOS:** Überprüfen Sie die Associated Domains, die in Xcode für Ihre App eingerichtet wurden[(Schritt 1c]({{site.baseurl}}/help/help_articles/email/universal_links/?tab=ios#step-1c)). Vergewissern Sie sich, dass die Domain für das Click Tracking in dieser Liste enthalten ist.
- **Android:** Öffnen Sie die App-Infoseite (drücken Sie lange auf das App-Symbol und klicken Sie auf ⓘ). Suchen Sie im Info-Menü der App den Eintrag **Standardmäßig öffnen** und tippen Sie darauf. Dies sollte einen Bildschirm mit allen überprüften Links anzeigen, die die App öffnen darf. Vergewissern Sie sich, dass die Domain für das Click Tracking in dieser Liste enthalten ist.

