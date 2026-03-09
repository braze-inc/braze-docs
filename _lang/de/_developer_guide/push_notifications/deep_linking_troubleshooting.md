---
nav_title: Fehlerbehebung bei Deeplinking
article_title: Fehlerbehebung bei Deeplinking
description: "Häufige Probleme mit Deeplinking unter iOS und deren Diagnose, einschließlich benutzerdefinierter Schema-Links, Universal Links, E-Mail-Links und Drittanbietern wie Branch."
page_order: 1.2
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Fehlerbehebung bei Deeplinking

> Diese Seite behandelt häufige Probleme mit Deeplinking unter iOS und deren Diagnose. Für Unterstützung bei der Auswahl des geeigneten Linktyps konsultieren Sie bitte [den Leitfaden für iOS-Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). Für Details zur Implementierung, siehe [Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift).

## Der Deeplink des benutzerdefinierten Schemas öffnet nicht die korrekte Ansicht.

Wenn ein benutzerdefinierter Deeplink (z. B. `myapp://products/123`) Ihre App öffnet, jedoch nicht zum gewünschten Bildschirm navigiert:

1. **Bitte überprüfen Sie, ob das Programm registriert ist.** Bitte überprüfen Sie in Xcode, ob Ihr Schema unter`CFBundleURLTypes` aufgeführt`Info.plist` ist.
2. **Bitte überprüfen Sie Ihren Handler.** Setzen Sie einen Haltepunkt in, um`application(_:open:options:)` zu bestätigen, dass es aufgerufen wird, und überprüfen Sie den`url`Parameter.
3. **Bitte überprüfen Sie den Link unabhängig.** Führen Sie den folgenden Befehl im Terminal aus, um den Deeplink außerhalb von Braze zu testen:
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   Sollte der Link hier nicht funktionieren, liegt das Problem in der URL-Verarbeitung Ihrer App und nicht bei Braze.
4. **Bitte überprüfen Sie das URL-Format.** Bitte überprüfen Sie, ob die URL in Ihrer Kampagne mit den Erwartungen Ihres Handlers übereinstimmt. Häufige Fehler sind fehlende Pfadkomponenten oder falsche Groß-/Kleinschreibung.

## Die Öffnung des Universal-Links erfolgt in Safari statt in der App.

Wenn die Öffnung eines universellen Links (z. B. `https://myapp.com/products/123`) in Safari statt in Ihrer App erfolgt:

### Bitte überprüfen Sie die Berechtigung für die zugehörigen Domains.

Öffnen Sie in Xcode Ihr App-Ziel > **Signing&Capabilities** und überprüfen Sie, ob unter **Associated **`applinks:yourdomain.com`**Domains** aufgeführt ist.

### Bitte überprüfen Sie die AASA-Datei.

Ihre Apple App Site Association (AASA)-Datei muss an einem der folgenden Standorte gehostet werden:

- `https://yourdomain.com/.well-known/apple-app-site-association`
- `https://yourdomain.com/apple-app-site-association`

Bitte überprüfen Sie Folgendes:

- Die Datei wird über HTTPS mit einem gültigen Zertifikat bereitgestellt.
- Das`Content-Type`ist `application/json`.
- Die Dateigröße beträgt weniger als 128 KB.
- Die`appID`  entspricht Ihrer Team-ID und Bundle-ID (zum Beispiel `ABCDE12345.com.example.myapp`).
- Das `paths``components`Array enthält die von Ihnen erwarteten URL-Muster.

Sie können Ihre AASA mit [dem Suchvalidierungstool von Apple](https://search.developer.apple.com/appsearch-validation-tool/) oder durch Ausführen des folgenden Befehls validieren:

```bash
swcutil dl -d yourdomain.com
```

### Bitte überprüfen Sie die `AppDelegate`

Bitte überprüfen Sie, ob in Ihrem `application(_:continue:restorationHandler:)``AppDelegate`implementiert ist und das`NSUserActivity`korrekt verarbeitet:

```swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
    return false
  }
  // Handle the URL
  return true
}
```

### Bitte überprüfen Sie die Konfiguration des Braze SDK.

Wenn Sie Universal Links aus Push-Benachrichtigungen, In-App-Nachrichten oder Content-Cards von Braze verwenden, vergewissern Sie sich bitte, dass`forwardUniversalLinks`die Option aktiviert ist:

```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
```

{% alert note %}
Die universelle Linkweiterleitung erfordert den Zugriff auf die Anwendungsberechtigungen. Bei der Ausführung in einem Simulator sind diese Berechtigungen nicht direkt verfügbar. Um in einem Simulator zu testen, fügen Sie die`.entitlements`Datei zur Build-Phase **„Copy Bundle Resources“** hinzu.
{% endalert %}

### Bitte überprüfen Sie das Problem mit dem langen Drücken.

Wenn Sie einen Universal-Link lange gedrückt halten und **die Öffnung** auswählen, kann iOS die Universal-Link-Zuordnung für diese Domain unterbrechen. Dies ist ein bekanntes Verhalten von iOS. Um ihn zurückzusetzen, drücken Sie bitte erneut lange auf den Link und wählen Sie **„Öffnung in [App-Name]**“.

## Der Deeplink aus der E-Mail öffnet die App nicht.

E-Mail-Links werden durch das Klick-Tracking-System Ihres ESP geleitet, das Links in eine Tracking-Domain einbindet (zum Beispiel )`https://click.yourdomain.com/...`. Damit Universal Links aus E-Mails funktionieren, müssen Sie die AASA-Datei auf Ihrer Klick-Tracking-Domain konfigurieren – nicht nur auf Ihrer primären Domain.

### Bitte überprüfen Sie die Klick-Tracking-Domain AASA.

1. Identifizieren Sie Ihre Klick-Tracking-Domain in Ihren ESP-Einstellungen (SendGrid, SparkPost oder Amazon SES).
2. Bitte hosten Sie die AASA-Datei unter `https://your-click-tracking-domain/.well-known/apple-app-site-association`.
3. Bitte stellen Sie sicher, dass die AASA-Datei auf der Klick-Tracking-Domain dieselben `appID`gültigen Pfadmuster enthält.

Für spezifische Einrichtungsanweisungen für ESP, sehen Sie [bitte unter „Universelle Links und App-Links“]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/) nach.

### Bitte überprüfen Sie die Weiterleitungskette.

Einige ESPs führen eine Weiterleitung von der URL des Klick-Tracking-Tools zu Ihrer endgültigen URL durch. Universelle Links funktionieren nur, wenn iOS die *ursprüngliche* Domain (die Domain für Tracking) als mit Ihrer App verbunden erkennt. Wenn die Weiterleitung die AASA-Prüfung umgeht, erfolgt die Öffnung des Links in Safari.

Zum Testen:

1. Bitte senden Sie sich selbst eine Test-E-Mail.
2. Halten Sie den Link gedrückt und überprüfen Sie die URL – dies ist die Tracking-URL für Klicks.
3. Bitte überprüfen Sie, ob diese Domain über eine gültige AASA-Datei verfügt.

## Deeplinks setzen über Push-Benachrichtigungen, jedoch nicht über In-App-Nachrichten (oder umgekehrt).

### Bitte überprüfen Sie den BrazeDelegate.

Wenn Sie implementieren`BrazeDelegate.braze(_:shouldOpenURL:)`, überprüfen Sie bitte, ob es Links kanalübergreifend konsistent verarbeitet. Der`context`Parameter umfasst den Quellkanal. Bitte überprüfen Sie die bedingte Logik, die möglicherweise versehentlich Links aus bestimmten Kanälen herausfiltert.

### Ausführliche Protokollierung einschalten

[Bitte aktivieren Sie die ausführliche Protokollierung]({{site.baseurl}}/developer_guide/verbose_logging) und reproduzieren Sie das Problem. Bitte suchen Sie nach dem `Opening`Protokolleintrag:

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

Bitte vergleichen Sie die Protokollausgabe für den funktionierenden Kanal mit der des nicht funktionierenden Kanals. Unterschiede in`useWebView`  oder`isUniversalLink`  zeigen an, wie das SDK den Link unterschiedlich interpretiert.

### Überprüfen Sie auf angepasste Anzeigedelegaten.

Wenn Sie einen angepassten In-App-Nachrichten-Anzeige-Delegaten oder einen Content-Card-Klick-Handler verwenden, überprüfen Sie bitte, dass dieser Link-Ereignisse korrekt an das Braze SDK zur Verarbeitung weiterleitet.

## „Web-URL in App öffnen“ zeigt eine leere oder fehlerhafte Seite an

Wenn die Auswahl **von „Web-URL in App öffnen“** zu einer leeren oder fehlerhaften Webansicht führt:

1. **Bitte überprüfen Sie, ob die URL HTTPS verwendet.** Die WebView des SDK erfordert ATS-konforme URLs. HTTP-Links funktionieren nicht, ohne dass dies angezeigt wird.
2. **Bitte überprüfen Sie die Content Security Policy-Header.** Wenn die Zielwebseite  oder eine `X-Frame-Options: DENY`restriktive  `Content-Security-Policy`festlegt, wird die Darstellung in einer WebView blockiert.
3. **Bitte überprüfen Sie, ob Weiterleitungen zu angepassten Schemata vorhanden sind.** Wenn die Webseite zu einem angepassten Schema weiterleitet (z. B. `myapp://`), kann WebView dies nicht verarbeiten.
4. **Bitte überprüfen Sie die URL in Safari.** Sollte die Seite in Safari auf dem Gerät nicht geladen werden, wird sie auch nicht in WebView geladen.

## Fehlerbehebung mit Braze für Branch {#branch}

Wenn Sie [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) als Ihren Linking-Anbieter verwenden:

### Bitte überprüfen Sie die BrazeDelegate-Routen zu Branch.

Sie`BrazeDelegate`müssen Branch-Links abfangen und an das Branch SDK weiterleiten. Bitte überprüfen Sie Folgendes:

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host, host.contains("app.link") {
    // Route to Branch SDK
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle other links
  return true
}
```

Wenn`shouldOpenURL`Rückgaben`true`für Branch-Links vorliegen, verarbeitet Braze diese direkt, anstatt sie an Branch weiterzuleiten.

### Bitte überprüfen Sie die Domain des Branch-Links.

Bitte überprüfen Sie, ob die Branch-Domain in Ihren Einstellungen`BrazeDelegate`mit Ihrer tatsächlichen Branch-Link-Domain übereinstimmt. Branch verwendet mehrere Domain-Formate:

- `yourapp.app.link` (Standard)
- `yourapp-alternate.app.link` (alternativ)
- Angepasste Domains (sofern im Branch-Dashboard konfiguriert)

### Aktivieren Sie die Protokollierung beider SDKs.

Um festzustellen, wo die Verbindung in der Kette unterbrochen ist:

1. Aktivieren Sie [die ausführliche Protokollierung von Braze]({{site.baseurl}}/developer_guide/verbose_logging) – suchen Sie nach`Opening '<URL>':`Einträgen, um zu überprüfen, ob das SDK den Link erhalten hat.
2. Aktivieren Sie [den Branch-Testmodus](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking) – überprüfen Sie das Branch-Dashboard auf Link-Klick-Ereignisse.
1. Bitte aktivieren Sie [die ausführliche Protokollierung von Braze]({{site.baseurl}}/developer_guide/verbose_logging). Bitte überprüfen Sie`Opening '<URL>':`die Einträge, um sicherzustellen, dass das SDK den Link erhalten hat.
2. Bitte aktivieren Sie [den Branch-Testmodus](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking). Bitte überprüfen Sie das Branch-Dashboard auf Link-Klick-Ereignisse.
3. Wenn Braze den Link protokolliert, Branch jedoch keinen Klick erkennt, liegt das Problem wahrscheinlich an der`BrazeDelegate`Weiterleitungslogik.

### Bitte überprüfen Sie die Konfiguration des Dashboards der Branch.

Bitte überprüfen Sie im Branch-Dashboard Folgendes:

- **Die Bundle-ID** und **die Team-ID** Ihrer App stimmen mit Ihrem Xcode-Projekt überein.
- Ihre **zugehörigen Domains** umfassen die Branch-Link-Domain.
- Ihre Branch-AASA-Datei ist gültig (Branch hostet diese automatisch auf`app.link`Domains).

### Branch-Links unabhängig voneinander

Bitte überprüfen Sie den Branch-Link außerhalb von Braze, um das Problem einzugrenzen:

1. Öffnen Sie den Link „Branch“ in Safari auf Ihrem Gerät. Sollte die Öffnung der App nicht erfolgen, liegt das Problem in Ihrer Branch- oder AASA-Konfiguration und nicht bei Braze.
2. Bitte fügen Sie den Branch-Link in die Notizen-App ein und tippen Sie darauf. Universelle Links funktionieren in Notes zuverlässiger als in der Adressleiste von Safari.

## Allgemeine Tipps zur Fehlerbehebung

### Verwendung ausführlicher Protokollierung

[Aktivieren Sie die ausführliche Protokollierung,]({{site.baseurl}}/developer_guide/verbose_logging) um genau zu sehen, wie das SDK Links verarbeitet. Wichtige Einträge, auf die Sie achten sollten:

| Protokolleintrag | Was es bedeutet |
|---|---|
| `Opening '<URL>': - channel: notification` | Das SDK verarbeitet einen Link aus einer Push-Benachrichtigung. |
| `Opening '<URL>': - channel: inAppMessage` | Das SDK verarbeitet einen Link aus einer In-App-Nachricht. |
| `Opening '<URL>': - channel: contentCard` | Das SDK verarbeitet einen Link aus einer Content-Card. |
| `useWebView: true` | Das SDK führt die Öffnung der URL im In-App-WebView durch. |
| `isUniversalLink: true` | Das SDK hat die URL als Universal Link als Bezeichner identifiziert. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Informationen zum Lesen dieser Protokolle finden Sie unter [Lesen von ausführlichen Protokollen]({{site.baseurl}}/developer_guide/verbose_logging).

### Testen Sie Links isoliert.

Bevor Sie den Test über Braze durchführen, überprüfen Sie bitte, ob Ihr Deeplink oder Universal Link eigenständig funktioniert:

- **Angepasstes Schema**: Bitte führen Sie das Programm`xcrun simctl openurl booted "myapp://path"`im Terminal aus.
- **Universeller Link**: Fügen Sie die URL in die Notizen-App auf einem physischen Gerät ein und tippen Sie darauf. Bitte führen Sie keine Tests über die Adressleiste von Safari durch, da iOS eingegebene URLs anders behandelt als angeklickte Links.
- **Branch-Link**: Öffnen Sie den Branch-Link über die Notes-App auf einem Gerät.

### Testen Sie auf einem physischen Gerät

Universelle Links werden im iOS-Simulator nur eingeschränkt unterstützt. Bitte führen Sie Tests stets auf einem physischen Gerät durch, um genaue Ergebnisse zu erzielen. Falls Sie in einem Simulator testen müssen, fügen Sie die`.entitlements`Datei zur Build-Phase **„Copy Bundle Resources“** hinzu.