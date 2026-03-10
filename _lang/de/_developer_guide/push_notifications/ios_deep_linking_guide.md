---
page_order: 1.1
nav_title: Leitfaden für Deeplinking unter iOS
article_title: Leitfaden für Deeplinking unter iOS
description: "Erfahren Sie, welche Art von Deeplink Sie für Ihre iOS-App verwenden sollten, wann Sie eine AASA-Datei benötigen und welche App-Delegate-Methoden Sie implementieren müssen."
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Leitfaden für Deeplinking unter iOS

> Dieser Leitfaden unterstützt Sie bei der Auswahl der geeigneten Deeplinking-Strategie für Ihre iOS-App, abhängig davon, welche Messaging-Kanäle Sie verwenden und ob Sie einen Drittanbieter für Links wie Branch nutzen.

Für Details zur Implementierung, siehe [Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift). Informationen zur Fehlerbehebung finden Sie unter [Fehlerbehebung bei Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

## Auswahl eines Link-Typs

Es gibt drei Möglichkeiten, Links aus Braze-Nachrichten in Ihrer iOS-App zu verarbeiten. Jedes funktioniert anders und eignet sich für unterschiedliche Kanäle und Anwendungsfälle.

| Verbindungstyp | Beispiel | Am besten für | Öffnung ohne installierte App? |
|---|---|---|---|
| **Angepasstes Schema** | `myapp://products/123` | Push-Benachrichtigungen, In-App-Nachrichten, Content-Cards | Nein – Link funktioniert nicht |
| **Universeller Link** | `https://myapp.com/products/123` | E-Mail, SMS, Kanäle mit Klick-Tracking | Ja – weicht auf das Internet aus |
| **Web-URL in App öffnen** | Jede`https://`URL | Anzeige von Internet-Inhalten in einem Modal-WebView | Nicht zutreffend – wird in WebView angezeigt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Angepasste Deeplinks für das Schema

Benutzerdefinierte Deeplinks (zum Beispiel )`myapp://products/123` öffnen Ihre App direkt auf einem bestimmten Bildschirm. Sie stellen die einfachste Option für Kanäle dar, bei denen Links nicht von Dritten geändert werden.

**Verwenden Sie benutzerdefinierte Deeplinks, wenn:**
- Versenden von Push-Benachrichtigungen, In-App-Nachrichten oder Content-Cards
- Der Link ist nicht erforderlich, wenn die App nicht installiert ist.
- Sie benötigen kein Tracking (E-Mail-ESP-Link-Wrapping).

**Verwenden Sie keine benutzerdefinierten Deeplinks, wenn:**
- Versenden von E-Mails – ESPs verpacken Links für das Tracking der Klicks, wodurch benutzerdefinierte Schemata unterbrochen werden.
- Sie benötigen den Link, um auf eine Webseite zurückzugreifen, falls die App nicht installiert ist.

### Universelle Links

Universelle Links (zum Beispiel ) sind `https://myapp.com/products/123`Standard-HTTPS-URLs, die iOS an Ihre App weiterleiten kann, anstatt eine Öffnung in einem Browser durchzuführen. Sie erfordern eine serverseitige Konfiguration (eine AASA-Datei) und eine appseitige Einrichtung (Berechtigung für zugehörige Domains).

**Verwenden Sie universelle Links, wenn:**
- Versenden von E-Mails. Ihr ESP verpackt Links für das Klick-Tracking, daher müssen die Links HTTPS-Links sein.
- Versenden von SMS oder über andere Kanäle, bei denen Links umgebrochen oder gekürzt werden.
- Sie benötigen den Link, um auf eine Webseite zurückzugreifen, wenn die App nicht installiert ist.
- Sie nutzen einen Drittanbieter für Verlinkungen wie Branch oder Appsflyer.

**Bitte verwenden Sie keine Universal-Links, wenn:**
- Sie benötigen lediglich Deeplinks aus Push-Benachrichtigungen, In-App-Nachrichten oder Content-Cards. Angepasste Schemata sind einfacher.

### „Web-URL innerhalb der App öffnen“

Diese Option führt zur Öffnung einer Webseite in einem Modal-WebView innerhalb Ihrer App. Dies wird vollständig vom Braze SDK mithilfe von  `Braze.WebViewController`abgewickelt – Sie müssen keinen Code für die URL-Verarbeitung schreiben.

**Verwenden Sie „Öffnung der Internet-URL innerhalb der App“, wenn:**
- Sie möchten eine Webseite (z. B. eine Aktion oder einen Artikel) anzeigen, ohne Ihre App zu verlassen.
- Die URL ist eine Standard-HTTPS-Webseite und kein Deeplink zu einem bestimmten App-Bildschirm.

**Bitte verwenden Sie die Option „Öffnung der Internet-URL innerhalb der App“ nicht, wenn:**
- Sie müssen zu einer bestimmten Ansicht in Ihrer App navigieren. Bitte verwenden Sie stattdessen ein angepasstes Schema oder einen universellen Link.
- Die Webseite erfordert eine Authentifizierung oder verfügt über Content Security Policy-Header, die die Einbettung verhindern.

## Was Sie für jeden Link-Typ benötigen

### Angepasste Deeplinks für das Schema

| Anforderung | Details |
|---|---|
| AASA-Datei | Nicht erforderlich |
| `Info.plist` | Bitte registrieren Sie Ihr Programm unter`CFBundleURLTypes`und fügen Sie es hinzu. `LSApplicationQueriesSchemes` |
| App-Delegate-Methode | Implementieren`application(_:open:options:)`Sie die Analyse der URL und die Navigation. |
| Konfiguration des Braze SDK | Keine – das SDK öffnet standardmäßig benutzerdefinierte Schema-URLs. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Universelle Links

| Anforderung | Details |
|---|---|
| AASA-Datei | Erforderlich — Gastgeber bei `https://yourdomain.com/.well-known/apple-app-site-association` |
| Zugehörige Domains | Fügen Sie`applinks:yourdomain.com`in Xcode unter **„Signing&Capabilities“** hinzu: |
| App-Delegate-Methode | Implementieren, `application(_:continue:restorationHandler:)`um zu verarbeiten `NSUserActivity` |
| Konfiguration des Braze SDK | Set `configuration.forwardUniversalLinks = true` |
| BrazeDelegate (optional) | Implementierung`braze(_:shouldOpenURL:)`für angepasstes Routing (z. B. Branch) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Wenn Sie E-Mails über Braze versenden, verpackt Ihr ESP (SendGrid, SparkPost oder Amazon SES) Links in eine Domain für Klick-Tracking. Bitte beachten Sie, dass Sie die AASA-Datei nicht nur auf Ihrer primären Domain, sondern auch auf Ihrer Domain für Klick-Tracking hosten müssen. Für die vollständige Einrichtung, sehen Sie [bitte unter „Universelle Links“ und „App-Links“]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/) nach.
{% endalert %}

### „Web-URL innerhalb der App öffnen“

| Anforderung | Details |
|---|---|
| AASA-Datei | Nicht erforderlich |
| App-Delegate-Methode | Nicht erforderlich – das SDK übernimmt dies automatisch. |
| Konfiguration des Braze SDK | Keine – wählen Sie **„Web-URL innerhalb der App auswählen“** im Editor der Kampagne. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Wenn Sie eine AASA-Datei benötigen {#when-aasa}

Eine Apple App Site Association (AASA)-Datei ist nur erforderlich, wenn Sie **Universal Links** verwenden. Es teilt iOS mit, welche URLs Ihre App verarbeiten kann.

Sie benötigen eine AASA-Datei, wenn:

- Sie setzen Deeplinks in E-Mail-Kampagnen ein (da ESPs Links in HTTPS-Klick-Tracking-URLs einbinden).
- Sie setzen Deeplinks in SMS-Kampagnen ein (da Links möglicherweise zu HTTPS-URLs verkürzt werden).
- Sie verwenden Branch, Appsflyer oder einen anderen Linking-Anbieter (da diese ihre eigenen HTTPS-Domains verwenden).
- Sie können universelle Links aus Push-Benachrichtigungen, In-App-Nachrichten oder Content-Cards verwenden (weniger verbreitet, jedoch möglich mit `forwardUniversalLinks = true`).

Sie benötigen keine AASA-Datei, wenn:

- Bitte setzen Sie benutzerdefinierte Deeplinks (z. B. `myapp://`) ausschließlich in Push-Benachrichtigungen, In-App-Nachrichten oder Content-Cards ein.
- Bitte verwenden Sie die Option **„Öffnung der Internet-URL innerhalb der App**“.

Anweisungen zur Einrichtung von AASA finden Sie unter [„Universelle Links“ und „App-Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#setting-up-universal-links-and-app-links)“.

## Wenn Sie App-Code zur Verarbeitung von Links benötigen {#when-app-code}

Welche Delegate-Methode Sie implementieren, hängt von der Art der verwendeten Verknüpfung ab:

| Delegierte Methode | Griffe | Wann sollte die Implementierung erfolgen? |
|---|---|---|
| `application(_:open:options:)` | Angepasste Deeplinks (`myapp://`) | Sie können benutzerdefinierte Deeplinks von jedem Kanal verwenden. |
| `application(_:continue:restorationHandler:)` | Universelle Links (`https://`) | Sie verwenden universelle Links aus E-Mails, SMS oder mit `forwardUniversalLinks = true` |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | Alle URLs, die vom SDK geöffnet werden | Sie benötigen eine angepasste Routing-Logik (z. B. Branch, bedingte Verarbeitung, Analytics). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Wenn Sie einen Drittanbieter für Verknüpfungen wie Branch verwenden, implementieren Sie bitte die`BrazeDelegate.braze(_:shouldOpenURL:)` Funktion, um URLs abzufangen und an das SDK des Anbieters weiterzuleiten. Ein vollständiges Beispiel finden Sie unter [„Branch für Deeplinking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/)“.
{% endalert %}

## Verwendung von Branch mit Braze {#branch}

Wenn Sie [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) als Ihren Linking-Anbieter verwenden, sind für Ihre Einrichtung einige zusätzliche Schritte erforderlich, die über die Standardkonfiguration für Universal Links hinausgehen:

1. **Branch SDK**: Integrieren Sie das Branch SDK gemäß [der Dokumentation von Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview).
2. **Verbundene Domains**: Fügen Sie Ihre Branch-Domain (z. B. `applinks:yourapp.app.link`) in Xcode unter **„Signing&Capabilities“** hinzu.
3. **BrazeDelegate**: Implementieren Sie`braze(_:shouldOpenURL:)`die Weiterleitung von Branch-Links an das Branch SDK, anstatt sie direkt von Braze verarbeiten zu lassen.
4. **Universelle Links weiterleiten**: Bitte stellen Sie dies`configuration.forwardUniversalLinks = true` in Ihrer Braze SDK-Konfiguration ein.

Implementierungsdetails und Anleitungen zur Fehlerbehebung finden Sie unter [„Branch für Deeplinking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/)“.