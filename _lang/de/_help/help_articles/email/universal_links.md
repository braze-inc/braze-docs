---
nav_title: Universelle Links und App-Links
article_title: Universelle Links und App-Links
page_order: 1
page_type: solution
description: "Dieser Hilfeartikel zeigt Ihnen, wie Sie Apple Universal Links und Android App Links einrichten."
channel: email
---

# Universelle Links und App-Links

Apple Universal Links und Android App Links sind Mechanismen, die für einen nahtlosen Übergang zwischen Webinhalten und mobilen Apps sorgen. Während universelle Links spezifisch für iOS sind, dienen Android App Links demselben Zweck für Android-Anwendungen.

## Wie Universal Links und App Links funktionieren

Universal Links (iOS) und App Links (Android) sind Standard-Web-Links (`http://mydomain.com`), die sowohl auf eine Webseite als auch auf einen Inhalt innerhalb einer App verweisen.

Wenn ein Universal Link oder App Link geöffnet wird, prüft das Betriebssystem, ob eine installierte App für diese Domain registriert ist. Wenn eine App gefunden wird, wird sie sofort gestartet, ohne die Webseite zu laden. Wenn keine App gefunden wird, wird die Web-URL im Standard-Webbrowser des Benutzers geladen, der auch so konfiguriert werden kann, dass er zum App Store bzw. Google Play Store weiterleitet.

Wenn also ein Benutzer auf einen Link zu einer Webseite klickt, die einem App-Bildschirm entspricht, kann die App direkt geöffnet werden (wenn die App derzeit installiert ist).

In dieser Tabelle finden Sie die wichtigsten Unterschiede zwischen universellen Links und herkömmlichen Deep Links:

|                        | Universelle Links und App-Links                                  | Tiefe Links                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| Plattform-Kompatibilität | iOS (Version 9 und höher) und Android (Version 6.0 und höher)  | Verwendet in verschiedenen mobilen Betriebssystemen    |
| Zweck                | Verknüpfen Sie nahtlos Web- und App-Inhalte auf iOS- und Android-Geräten | Link zu bestimmten App-Inhalten |
| Funktion               | Leitet kontextabhängig zu Webseiten oder App-Inhalten weiter           | Öffnet bestimmte App-Bildschirme   |
| App-Installation       | Öffnet die App, wenn die App installiert ist, andernfalls werden Webinhalte geöffnet | Erfordert die Installation einer App |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Anwendungsfälle

Universal Links und App Links werden am häufigsten für E-Mail-Kampagnen verwendet, da E-Mails sowohl von Desktop- als auch von Mobilgeräten aus geöffnet und angeklickt werden können.

Einige Kanäle funktionieren nicht gut mit diesen Links. Zum Beispiel sollten Push-Benachrichtigungen, In-App-Nachrichten und Content Cards schema-basierte Deep Links verwenden (`mydomain://`).

{% alert note %}
Android-App-Links erfordern eine benutzerdefinierte `IBrazeDeeplinkHandler` mit einer Logik, die Links von ihren Domains getrennt von anderen Web-URLs behandelt. Es kann einfacher sein, stattdessen Deep Links zu verwenden und die Verlinkungspraktiken für andere Kanäle als E-Mail einheitlich zu halten.
{% endalert %}

## Voraussetzungen

Zur Verwendung von Universal Links und App Links:

- Ihre Website muss über HTTPS zugänglich sein
- Ihre App muss im App Store (iOS) oder Google Play Store (Android) verfügbar sein.

## Universelle Links und App-Links einrichten

Damit Apps universelle Links oder App-Links unterstützen, benötigen sowohl iOS als auch Android eine spezielle Berechtigungsdatei, die auf der Link-Domain gehostet wird. Diese Datei enthält Definitionen darüber, welche Apps Links von dieser Domain öffnen können und, für iOS, welche Pfade diese Apps öffnen dürfen:

- **iOS:** Apple App Site Association (AASA) Datei
- **Android:** Digital Asset Links Datei

Zusätzlich zu dieser Berechtigungsdatei gibt es fest kodierte Definitionen der Link-Domänen, die die App öffnen darf, die innerhalb der App eingerichtet sind:

- **iOS:** Als "Zugehörige Domänen" in Xcode festlegen
- **Android:** Definiert in der `AndroidManifest.xml` Datei der App

Diese zweiteilige Domain-App-Verknüpfung ist erforderlich, damit ein universeller Link oder App-Link funktioniert und verhindert, dass eine App Links von einer bestimmten Domain entführt oder eine bestimmte App von einer beliebigen Domain geöffnet wird.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

Diese Schritte sind der Apple-Entwicklerdokumentation entnommen. Weitere Informationen finden Sie unter [Erlauben von Apps und Websites, auf Ihre Inhalte zu verlinken](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc).

### Schritt 1 Konfigurieren Sie Ihre App-Berechtigungen

{% alert note %}
[In Xcode 13 und höher](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/) kann Xcode die Bereitstellung von Berechtigungen automatisch für Sie übernehmen. Sie können wahrscheinlich zu [Schritt 1c](#step-1c) übergehen und auf diese Anleitung zurückgreifen, wenn Sie Probleme haben.
{% endalert %}

#### Schritt 1a: Registrieren Sie Ihre App {#step-1a}

1. Gehen Sie auf developer.apple.com und melden Sie sich an.
2. Klicken Sie auf **Zertifikate, Identifikatoren & Profile**.
3. Klicken Sie auf **Identifikatoren**.
4. Wenn Sie noch keine registrierte App-Kennung haben, klicken Sie auf +, um eine zu erstellen.
   a. Geben Sie einen **Namen** ein. Das kann alles sein, was Sie wollen.
   b. Geben Sie die **Bundle-ID** ein. Sie können Ihre Bundle-ID auf der Registerkarte **Allgemein** Ihres Xcode-Projekts finden, um das richtige Build-Ziel zu finden.

#### Schritt 1b: Aktivieren Sie Assoziierte Domains in der Kennung Ihrer Anwendung

1. Suchen Sie in Ihrer bestehenden oder neu erstellten App-Kennung den Abschnitt **App-Dienste**.
2. Wählen Sie **Assoziierte Domains**.
3. Klicken Sie auf **Speichern**.

![]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### Schritt 1c: Aktivieren Sie Assoziierte Domänen in Ihrem Xcode-Projekt {#step-1c}

Bevor Sie fortfahren, vergewissern Sie sich, dass in Ihrem Xcode-Projekt das gleiche Team ausgewählt ist, in dem Sie gerade Ihre App-Kennung registriert haben. 

1. Gehen Sie in Xcode auf die Registerkarte **Fähigkeiten** Ihrer Projektdatei.
2. Aktivieren Sie **Assoziierte Domains**.

##### Tipp zur Fehlersuche

Wenn Sie die Fehlermeldung "Eine App ID mit dem Identifikator 'your-app-id' ist nicht verfügbar. Bitte geben Sie eine andere Zeichenfolge ein", gehen Sie folgendermaßen vor:

1. Überprüfen Sie, ob Sie die richtige Mannschaft ausgewählt haben.
2. Vergewissern Sie sich, dass die Bundle-ID[(Schritt 1a](#step-1a)) Ihres Xcode-Projekts mit derjenigen übereinstimmt, die Sie für die Registrierung des App Identifiers verwendet haben.

#### Schritt 1d: Fügen Sie die Domänenberechtigung hinzu

Fügen Sie im Abschnitt Domains das entsprechende Domain-Tag hinzu. Sie müssen das Präfix `applinks:` verwenden. In diesem Fall können Sie sehen, dass wir `applinks:yourdomain.com` hinzugefügt haben.

![]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### Schritt 1e: Vergewissern Sie sich, dass die Datei mit den Berechtigungen im Build enthalten ist

Stellen Sie im Projektbrowser sicher, dass Ihre neue Berechtigungsdatei unter **Zielmitgliedschaft** ausgewählt ist.

Xcode sollte dies automatisch erledigen.

### Schritt 2 Konfigurieren Sie Ihre Website, um die AASA-Datei zu hosten

Um Ihre Website-Domain mit Ihrer nativen App auf iOS zu verknüpfen, müssen Sie die Apple App Site Association (AASA) Datei auf Ihrer Website hosten. Diese Datei dient als sicherer Weg, um den Besitz der Domain gegenüber iOS zu verifizieren. Vor iOS 9 konnten Entwickler jedes beliebige URI-Schema registrieren, um ihre Apps zu öffnen, ohne jegliche Überprüfung. Mit AASA ist dieser Prozess jedoch viel sicherer und zuverlässiger geworden.

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

- `appID`: Erstellt durch die Kombination der **Team-ID** Ihrer App (gehen Sie zu `https://developer.apple.com/account/#/membership/`, um die Team-ID zu erhalten) und dem **Bundle Identifier**. Im obigen Beispiel ist "JHGFJHHYX" die Team-ID und "com.facebook.ios" ist die Bundle-ID.
- `paths`: Array von Zeichenketten, die angeben, welche Pfade von der Zuordnung ein- oder ausgeschlossen werden. Sie können `NOT` vor der Pfadangabe verwenden, um Pfade zu deaktivieren. In diesem Beispiel führen alle Links auf diesem Pfad ins Internet, anstatt die App zu öffnen. Sie können `*` als Platzhalter verwenden, um alle Pfade in einem Verzeichnis zu aktivieren, und `?`, um ein einzelnes Zeichen abzugleichen (z. B. /archives/201?/, um alle Nummern von 2010-2019 abzugleichen).

{% alert note %}
Bei diesen Zeichenfolgen wird zwischen Groß- und Kleinschreibung unterschieden und Abfragezeichenfolgen und Fragmentbezeichner werden ignoriert.
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

Wenn ein Benutzer auf einem iOS-Gerät auf einen universellen Link tippt, startet das Gerät die App und sendet ihr ein [NSUserActivity-Objekt](https://developer.apple.com/documentation/foundation/nsuseractivity). Die App kann dann das NSUserActivity-Objekt abfragen, um festzustellen, wie sie gestartet wurde.

Um universelle Links in Ihrer App zu unterstützen, führen Sie die folgenden Schritte aus:

1. Fügen Sie eine Berechtigung hinzu, die die von Ihrer App unterstützten Domänen angibt.
2. Aktualisieren Sie Ihren App-Delegaten, damit er angemessen reagiert, wenn er das NSUserActivity-Objekt erhält.

Öffnen Sie in Xcode den Abschnitt **Assoziierte Domänen** auf der Registerkarte **Fähigkeiten** und fügen Sie für jede von Ihrer App unterstützte Domäne einen Eintrag mit dem Präfix `applinks:` hinzu. Zum Beispiel: `applinks:www.mywebsite.com`.

{% alert note %}
Apple empfiehlt, diese Liste auf nicht mehr als 20 bis 30 Domains zu beschränken.
{% endalert %}

### Schritt 5: Testen Sie Ihren Universal Link

Fügen Sie den universellen Link zu einer E-Mail hinzu und senden Sie sie an ein Testgerät. Wenn Sie einen universellen Link direkt in das URL-Feld von Safari einfügen, wird die App nicht automatisch geöffnet. In diesem Fall müssen Sie die Website manuell nach unten ziehen, so dass oben eine Aufforderung erscheint, die entsprechende App zu öffnen.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

Diese Schritte sind der Android-Entwicklerdokumentation entnommen. Weitere Informationen finden Sie unter [Hinzufügen von Android App-Links](https://developer.android.com/training/app-links#add-app-links) und [Erstellen von Deep Links zu App-Inhalten](https://developer.android.com/training/app-links/deep-linking).

{% alert note %}
Android-App-Links erfordern eine benutzerdefinierte `IBrazeDeeplinkHandler` mit einer Logik, die Links von ihren Domains getrennt von anderen Web-URLs behandelt. Es kann einfacher sein, stattdessen Deep Links zu verwenden und die Verlinkungspraktiken für andere Kanäle als E-Mail einheitlich zu halten.
{% endalert %}

### Schritt 1 Deep Links erstellen

Zunächst müssen Sie Deep Links für Ihre Android-App erstellen. Dies kann durch Hinzufügen von [Absichtsfiltern](https://developer.android.com/guide/components/intents-filters) in Ihrer `AndroidManifest.xml` Datei geschehen. Der Absichtsfilter sollte die Aktion `VIEW` und die Kategorie `BROWSABLE` zusammen mit der URL Ihrer Website im Datenelement enthalten.

### Schritt 2 Verknüpfen Sie Ihre App mit Ihrer Website

Sie müssen Ihre App mit Ihrer Website verknüpfen. Dazu können Sie eine Datei mit digitalen Asset-Links erstellen. Diese Datei sollte im JSON-Format vorliegen und enthält Angaben zu den Android-Apps, die Links zu Ihrer Website öffnen können. Sie sollte im Verzeichnis `.well-known` Ihrer Website abgelegt werden.

### Schritt 3: Aktualisieren Sie Ihre App-Manifestdatei

Fügen Sie in Ihrer Datei `AndroidManifest.xml` ein Metadaten-Element innerhalb des Anwendungselements hinzu. Das Meta-Daten-Element sollte ein `android:name` -Attribut von "asset_statements" und ein `android:resource` -Attribut haben, das auf eine Ressourcendatei mit einem String-Array verweist, das die URL Ihrer Website enthält.

### Schritt 4: Bereiten Sie Ihre Anwendung auf den Umgang mit Deep Links vor

In Ihrer Android-App müssen Sie die eingehenden Deep Links behandeln. Sie können dies tun, indem Sie die Absicht abrufen, mit der Ihre Aktivität gestartet wurde, und die Daten daraus extrahieren.

### Schritt 5: Testen Sie Ihre Deep Links

Schließlich können Sie Ihre Deep Links testen. Senden Sie sich selbst einen Link über eine Messaging-App oder eine E-Mail und klicken Sie ihn an. Wenn alles richtig eingestellt ist, sollte sich Ihre App öffnen.

{% endtab %}
{% endtabs %}

## Universelle Links, App-Links und Klick-Tracking

{% alert note %}
Links zur Nachverfolgung von Klicks werden in der Regel als Teil Ihres Onboardings für E-Mails eingerichtet. Wenn dies nicht während der Kundenanmeldung ausgefüllt wurde, wenden Sie sich an Ihren Kundenbetreuer, um Hilfe zu erhalten.
{% endalert %}

Unsere Partner für den E-Mail-Versand, SendGrid und SparkPost, verwenden Click-Tracking-Domains, um alle Links zu verpacken und URL-Parameter für das Click-Tracking in Braze-E-Mails aufzunehmen.

Zum Beispiel wird ein Link wie `https://www.example.com` zu einem Link wie `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`.

Damit E-Mail-Links mit Click-Tracking als universelle Links oder App-Links funktionieren, müssen Sie einige zusätzliche Einstellungen vornehmen. Stellen Sie sicher, dass Sie die Click-Tracking-Domain (`links.email.example.com`) als Domain hinzufügen, die die App öffnen darf. Außerdem sollte die Click-Tracking-Domain die AASA (iOS) oder Digital Asset Links (Android) Dateien bereitstellen. So können Sie sicherstellen, dass E-Mail-Links mit Click-Tracking reibungslos funktionieren.

Wenn Sie nicht möchten, dass jeder Click-Tracking-Link ein universeller Link oder ein App-Link ist, können Sie auf der Grundlage des E-Mail-Versandpartners festlegen, welche Links universelle Links sein sollen. Einzelheiten finden Sie in den folgenden Abschnitten.

### SendGrid

So behandeln Sie einen SendGrid-Click-Tracking-Link wie einen universellen Link:

1. Richten Sie Ihre AASA- oder AndroidManifest pathPrefix-Werte so ein, dass nur Links mit `/uni/` im URL-Pfad als universelle Links behandelt werden.
2. Fügen Sie dem Anker-Tag Ihres Links das Attribut `universal="true"` hinzu (`<a>`). Dadurch wird der URL-Pfad des umgeschlagenen Links so geändert, dass er `/uni/` enthält.

{% alert note %}
Für AMP-E-Mails sollte dieses Attribut data-universal="true" sein.
{% endalert %}

Zum Beispiel:

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3\. Vergewissern Sie sich, dass Ihre App so eingerichtet ist, dass sie die umbrochenen Links richtig verarbeitet. Lesen Sie den Artikel von SendGrid über das [Auflösen von SendGrid Click Tracking Links](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) und befolgen Sie die Schritte für Ihr Betriebssystem. Dieser Artikel enthält Beispielcode für [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) und [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android).

Mit dieser Konfiguration funktionieren Links mit `/uni/` im URL-Pfad als universelle Links, während alle anderen Links als Weblinks funktionieren.

### SparkPost

Um einen SparkPost-Click-Tracking-Link als universellen Link zu behandeln, fügen Sie das folgende Attribut in den Abschnitt Attribute des Drag-and-Drop-Editors für E-Mails ein oder bearbeiten Sie den Link-HTML-Code manuell, um das folgende Attribut in den Anker-Tag Ihres Links einzufügen: `data-msys-sublink="custom_path"`.

Dieser benutzerdefinierte Pfad ermöglicht es Ihnen, URLs mit diesem Wert selektiv als universellen Link zu behandeln.

Zum Beispiel:

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

Stellen Sie dann sicher, dass Ihre Anwendung den benutzerdefinierten Pfad richtig verarbeitet. Lesen Sie den SparkPost-Artikel über die [Verwendung von SparkPost-Klick-Tracking für Deep Links](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links). Dieser Artikel enthält Beispielcode für [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) und [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost).

### Fehlersuche bei universellen Links mit Click-Tracking

Wenn Ihre universellen Links in Ihren E-Mails nicht wie erwartet funktionieren, z. B. wenn der Empfänger von seiner E-Mail-App zum Webbrowser navigiert wird, bevor er schließlich zur App weitergeleitet wird, beachten Sie diese Tipps zur Fehlerbehebung bei der Einrichtung Ihrer universellen Links.

#### Überprüfen Sie den Speicherort der Link-Datei

Vergewissern Sie sich, dass sich die AASA-Datei (iOS) oder die Digital Asset Links-Datei (Android) an der richtigen Stelle befindet:

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

Es ist wichtig, sicherzustellen, dass diese Dateien immer öffentlich zugänglich sind. Wenn Sie nicht darauf zugreifen können, haben Sie möglicherweise einen Schritt bei der Einrichtung der universellen Links für E-Mails vergessen.

#### Überprüfen Sie die Domänendefinitionen

Stellen Sie sicher, dass Sie die richtigen Definitionen für die Domänen haben, die Ihre App öffnen darf.

- **iOS:** Überprüfen Sie die verknüpften Domänen, die in Xcode für Ihre App eingerichtet wurden[(Schritt 1c]({{site.baseurl}}/help/help_articles/email/universal_links/?tab=ios#step-1c)). Überprüfen Sie, ob die Click-Tracking-Domain in dieser Liste enthalten ist.
- **Android:** Öffnen Sie die App-Infoseite (drücken Sie lange auf das App-Symbol und klicken Sie auf ⓘ). Suchen Sie im App-Infomenü nach **Standardmäßig öffnen** und tippen Sie darauf. Dies sollte einen Bildschirm mit allen verifizierten Links anzeigen, die die App öffnen darf. Überprüfen Sie, ob die Click-Tracking-Domain in dieser Liste enthalten ist.
