---
nav_title: Google Tag Manager
article_title: Google Tag Manager für Web
platform: Web
page_order: 20
description: "Dieser Artikel beschreibt, wie Sie Google Tag Manager verwenden, um Braze auf Ihrer Website bereitzustellen."

---

# Google Tag Manager

> Dieser Artikel enthält eine schrittweise Anleitung, wie Sie das Braze Web SDK mit dem Google Tag Manager (GTM) zu Ihrer Website hinzufügen. Mit [dem Google Tag Manager](https://support.google.com/tagmanager/answer/6103696) können Sie per Fernzugriff Tags auf Ihrer Website hinzufügen, entfernen und bearbeiten, ohne dass eine Produktionscode-Freigabe oder technische Ressourcen erforderlich sind.

Es gibt zwei von Braze erstellte Google Tag Manager-Vorlagen, den [Initialisierungs-Tag](#initialization-tag) und den [Aktions-Tag](#actions-tag).

Beide Tags können Sie Ihrem Arbeitsbereich über die [Community-Galerie von Google](https://tagmanager.google.com/gallery/#/?filter=braze) hinzufügen oder indem Sie beim Hinzufügen eines neuen Tags über die Community-Vorlagen nach Braze suchen.

![Bild der Galeriesuche]({% image_buster /assets/img/web-gtm/gtm-community-gallery-search.png %})

## Aktualisierte Google-Richtlinie zur Zustimmung von Nutzern in der EU

{% alert important %}
Google aktualisiert seine [EU-Zustimmungsrichtlinie](https://www.google.com/about/company/user-consent-policy/) als Reaktion auf die Änderungen des [Digital Markets Act (DMA](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)), der ab dem 6\. März 2024 in Kraft tritt. Diese neue Änderung verlangt von den Werbetreibenden, dass sie ihren Endnutzern aus dem EWR und dem Vereinigten Königreich bestimmte Informationen offenlegen und die erforderlichen Einwilligungen von ihnen einholen. Weitere Informationen finden Sie in der folgenden Dokumentation.
{% endalert %}

Im Rahmen der EU-Zustimmungsrichtlinie von Google müssen die folgenden booleschen benutzerdefinierten Attribute in Nutzerprofilen protokolliert werden:

- `$google_ad_user_data`
- `$google_ad_personalization`

Wenn Sie diese über die GTM-Integration einstellen, müssen Sie für benutzerdefinierte Attribute ein benutzerdefiniertes HTML-Tag erstellen. Im Folgenden finden Sie ein Beispiel dafür, wie Sie diese Daten als boolesche Datentypen (nicht als Strings) protokollieren:

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Weitere Informationen finden Sie unter [Zielgruppen-Synchronisierung mit Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/).

## Template für Initialisierungs-Tag {#initialization-tag}

Verwenden Sie das Initialisierungs-Tag, um das Braze Web SDK zu Ihrer Website hinzuzufügen.

### Schritt 1: Push-Einrichtung (optional)

Wenn Sie die Möglichkeit haben möchten, Push-Nachrichten über den Google Tag Manager zu senden, befolgen Sie zunächst die Richtlinien zur [Push-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/):
1. Konfigurieren Sie die Service Worker-Datei Ihrer Website und speichern Sie sie im Stammverzeichnis Ihrer Website.
2. Browserregistrierung einrichten - Nachdem der Service Worker konfiguriert ist, müssen Sie die Methode `braze.requestPushPermission()` entweder nativ in ihrer App oder über ein benutzerdefiniertes HTML-Tag (über das GTM-Dashboard) einrichten. Außerdem müssen Sie sicherstellen, dass das Tag nach der Initialisierung des SDK ausgelöst wird.

### Schritt 2: Initialisierungs-Tag auswählen

Suchen Sie in der Template-Galerie der Community nach Braze und wählen Sie das **Braze Initialisierungs-Tag** aus.

![Dialogfeld mit den Konfigurationseinstellungen des Braze Initialisierungs-Tags. Zu den Einstellungen gehören "Tag-Typ", "API-Schlüssel", "API-Endpunkt", "SDK-Version", "Externe Nutzer-ID" und "Safari Web-Push-ID".]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

### Schritt 3: Einstellungen konfigurieren

Geben Sie Ihren Braze-API-App-Identifizierungsschlüssel und den SDK-Endpunkt ein, die Sie auf der Seite **Einstellungen verwalten** in Ihrem Dashboard finden. Geben Sie die neueste Version des Web SDK im Format `major.minor` ein. Wenn die neueste Version beispielsweise `4.1.2` ist, geben Sie `4.1` ein. Sie können eine Liste der SDK-Versionen in unserem [Changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) einsehen.

### Schritt 4: Wählen Sie Initialisierungsoptionen

Wählen Sie aus den optionalen zusätzlichen Initialisierungsoptionen, die im Leitfaden [Ersteinrichtung]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze) ) beschrieben sind, die gewünschten Optionen aus.

### Schritt 5: Überprüfen und QA durchführen

Nachdem Sie das Tag bereitgestellt haben, gibt es zwei Möglichkeiten, um die ordnungsgemäße Integration zu überprüfen:

1. Wenn Sie das [Debugging-Tool](https://support.google.com/tagmanager/answer/6107056?hl=en) von Google Tag Manager verwenden, sollten Sie sehen, dass das Braze Initialization Tag auf Ihren konfigurierten Seiten oder Ereignissen ausgelöst wurde.
2. Sie sollten sehen, dass Netzwerkanforderungen an Braze gestellt werden, und die globale Bibliothek `window.braze` sollte jetzt auf Ihrer Webseite definiert sein.

## Template für Aktions-Tag {#actions-tag}

Mit dem Braze-Template für Aktions-Tags können Sie angepasste Events triggern, Käufe verfolgen, Nutzer-IDs ändern und das Tracking aus Datenschutzgründen beenden oder fortsetzen.

![]({% image_buster /assets/img/web-gtm/gtm-actions-tag.png %})

### Ändern der externen Nutzer-ID {#external-id}

Der Tag-Typ **Nutzer ändern** ruft die [Methode `changeUser` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) auf. 

Verwenden Sie dieses Tag immer dann, wenn sich ein Benutzer anmeldet oder anderweitig mit seiner eindeutigen `external_id` Kennung identifiziert wird.

Achten Sie darauf, die eindeutige ID des aktuellen Benutzers in das Feld **Externe Benutzer-ID** einzugeben, die in der Regel mit einer von Ihrer Website gesendeten Datenschichtvariablen gefüllt wird.

![Ein Dialogfeld mit den Konfigurationseinstellungen für Braze Action Tags. Zu den Einstellungen gehören "Tag-Typ" und "Externe Nutzer-ID".]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})

### Angepasste Events protokollieren {#custom-events}

Der Tag-Typ **Angepasstes Event** ruft die [Methode `logCustomEvent` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) auf.

Verwenden Sie dieses Tag, um angepasste Events an Braze zu senden, und schließen Sie optional angepasste Event-Eigenschaften ein.

Geben Sie den **Event-Namen** an, indem Sie entweder eine Variable verwenden oder einen Namen eingeben.

Verwenden Sie den Button **Zeile hinzufügen**, um Event-Eigenschaften hinzuzufügen.

![Ein Dialogfeld mit den Konfigurationseinstellungen für Braze Action Tags. Zu den Einstellungen gehören "Tag-Typ" (Angepasstes Event), "Event-Name" (Button-Klick) und "Event-Eigenschaften".]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})

### E-Commerce-Events {#ecommerce}

Wenn Ihre Website Käufe mithilfe des standardmäßigen Daten-Layer-Elements [E-Commerce-Event](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) im Google Tag Manager protokolliert, können Sie den Tag-Typ **E-Commerce-Kauf** verwenden. Dieser Aktionstyp protokolliert in Braze einen separaten "Kauf" für jeden Artikel in der Liste `items`.

Sie können auch weitere Eigenschaftsnamen angeben, die Sie als Kauf-Eigenschaften einbeziehen möchten, indem Sie deren Schlüssel in der Liste der Kauf-Eigenschaften angeben. Beachten Sie, dass Braze in einem individuellen `item`, der protokolliert wird, nach Kauf-Eigenschaften sucht, die Sie der Liste hinzufügen.

Angenommen, Ihre E-Commerce Payload enthält folgende `items`:

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

Wenn Sie nur `item_brand` und `item_name` als Kaufeigenschaften übergeben möchten, fügen Sie einfach diese beiden Felder zur Tabelle der Kaufeigenschaften hinzu. Wenn Sie keine Eigenschaften angeben, werden auch keine Kauf-Eigenschaften im Aufruf [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) an Braze gesendet.

### Kauf-Tracking {#purchases}

Der Tag-Typ **Kauf** ruft die [Methode `logPurchase` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) auf.

Verwenden Sie dieses Tag, um Käufe zu tracken, und schließen Sie optional Kauf-Eigenschaften ein.

Die Felder **Produkt-ID** und **Preis** sind erforderlich.

Verwenden Sie den Button **Zeile hinzufügen**, um Kauf-Eigenschaften hinzuzufügen.

![Ein Dialogfeld mit den Konfigurationseinstellungen für Braze Action Tags. Zu den Einstellungen gehören "Tag-Typ", "Externe ID", "Preis", "Währungscode", "Menge" und "Kauf-Eigenschaften".]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})

### Tracking anhalten und fortsetzen {#stop-tracking}

Mitunter kann es erforderlich sein, das Braze-Tracking auf Ihrer Website zu deaktivieren oder wieder zu aktivieren, z. B. nachdem ein Nutzer das Web-Tracking aus Datenschutzgründen abgelehnt hat.

Verwenden Sie den Tag-Typ **Tracking deaktivieren** oder **Tracking fortsetzen**, um das Web Tracking zu deaktivieren bzw. wieder zu aktivieren. Diese beiden Optionen rufen [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) und [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).

### Benutzerdefinierte Attribute {#custom-attributes}

Benutzerdefinierte Benutzerattribute sind aufgrund einer Einschränkung in der Skriptsprache von Google Tag Manager nicht verfügbar. Um angepasste Attribute zu protokollieren, erstellen Sie ein angepasstes HTML-Tag mit folgendem Inhalt:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
Die GTM-Vorlage unterstützt keine verschachtelten Eigenschaften für Ereignisse oder Käufe. Mit dem vorstehenden HTML-Code können Sie alle Events oder Käufe protokollieren, die verschachtelte Eigenschaften erfordern.
{% endalert %}

### Standard-Nutzerattribute {#standard-attributes}

Standard-Nutzerattribute wie z. B. der Vorname eines Nutzers, sollten auf die gleiche Weise protokolliert werden wie angepasste Nutzerattribute. Stellen Sie sicher, dass die Werte, die Sie für Standardattribute übergeben, dem erwarteten Format entsprechen, das in der Dokumentation [Nutzerklasse](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) angegeben ist.

Das Attribut "gender" kann zum Beispiel folgende Werte annehmen: `"m" | "f" | "o" | "u" | "n" | "p"`. Um also das Geschlecht eines Nutzers als weiblich festzulegen, erstellen Sie ein angepasstes HTML-Tag mit folgendem Inhalt:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```

## Integration von Content-Cards

Es gibt ein paar zusätzliche Schritte, um den [Content Cards-Nachrichtenkanal]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) mit Google Tag Manager zu integrieren. Google Tag Manager funktioniert, indem das [Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (eine Version unseres Web-SDK) direkt in den Code Ihrer Website injiziert wird. Das bedeutet, dass alle SDK-Methoden genauso verfügbar sind, als hätten Sie das SDK ohne Google Tag Manager integriert, außer bei der Implementierung von Content Cards.

### Option 1: Integration mit GTM

Für eine Standardintegration des Content Card Feeds können Sie ein **benutzerdefiniertes HTML-Tag** im Google Tag Manager verwenden. Fügen Sie Ihrem angepassten HTML-Tag Folgendes hinzu, um den standardmäßigen Content-Card-Feed zu aktivieren:

```html
<script>
   window.braze.showContentCards();
</script>
```

![Tag-Konfiguration eines angepassten HTML-Tags, das den Content-Card-Feed anzeigt, im Google Tag Manager.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})

### Option 2: Direkte Integration auf Ihrer Website

Um das Erscheinungsbild von Content-Cards und ihres Feeds stärker anpassen zu können, können Sie Content-Cards direkt in Ihre native Website integrieren. Hierfür gibt es zwei Möglichkeiten: Sie können die Standard-Feed-Benutzeroberfläche verwenden oder eine benutzerdefinierte Feed-Benutzeroberfläche erstellen.

#### Standard-Feed

Bei der Implementierung der [Standard-Feed-UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui) müssen die Methoden von Braze mit `window.` beginnen. `braze.showContentCards` sollte dann beispielsweise `window.braze.showContentCards` lauten.

#### Benutzerdefinierte Feed UI

Für den Stil des [angepassten Feeds]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_styling) sind die gleichen Schritte durchzuführen wie bei der Integration des SDK ohne GTM. Wenn Sie zum Beispiel die Breite des Content-Card-Feeds anpassen möchten, können Sie Folgendes in Ihre CSS-Datei einfügen:

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}

## Upgraden und Updaten von Templates {#upgrading}

Um ein Upgrade auf die neueste Version des Braze Web SDK durchzuführen, führen Sie die folgenden drei Schritte im Google Tag Manager-Dashboard aus:

1. **Tag-Template aktualisieren**<br>Rufen Sie die Seite **Vorlagen** in Ihrem Arbeitsbereich auf. Hier sollten Sie ein Symbol sehen, das anzeigt, dass ein Update verfügbar ist.<br><br>![Die Seite mit den Vorlagen zeigt an, dass ein Update verfügbar ist]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Klicken Sie auf dieses Symbol und klicken Sie nach Überprüfung der Änderung auf **Update akzeptieren**.<br><br>![Bildschirm, auf dem ein Vergleich zwischen altem und neuem Tag-Template mit dem Button "Update zustimmen" zu sehen ist]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Versionsnummer aktualisieren**<br>Nachdem Sie das Tag-Template aktualisiert haben, bearbeiten Sie das Braze Initialisierungs-Tag und aktualisieren die SDK-Version auf die neueste Version im Format `major.minor`. Wenn die neueste Version beispielsweise `4.1.2` ist, geben Sie `4.1` ein. Sie können eine Liste der SDK-Versionen in unserem [Changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) einsehen.<br><br>![Braze-Template für Initialisierungs-Tags mit einem Eingabefeld zum Ändern der SDK Version]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **QA und Veröffentlichung**<br>Vergewissern Sie sich, dass die neue SDK-Version funktioniert, indem Sie das [Debugging-Tool](https://support.google.com/tagmanager/answer/6107056?hl=en) von Google Tag Manager verwenden, bevor Sie ein Update für Ihren Tag-Container veröffentlichen.

## Schritte zur Fehlerbehebung {#troubleshooting}

### Tag-Debugging aktivieren {#debugging}

Jede Braze-Tag-Vorlage verfügt über ein optionales Kontrollkästchen **GTM Tag Debugging**, mit dem Sie Debug-Meldungen in der JavaScript-Konsole Ihrer Webseite protokollieren können.

![Das Debug-Tool von Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

### Debugging-Modus aufrufen

Eine weitere Möglichkeit, Ihre Google Tag Manager-Integration zu debuggen, ist die Verwendung der Google-Funktion [Vorschaumodus](https://support.google.com/tagmanager/answer/6107056).

Auf diese Weise können Sie feststellen, welche Werte von der Datenebene Ihrer Webseite an die einzelnen ausgelösten Braze-Tags gesendet werden, und Sie erfahren, welche Tags ausgelöst wurden und welche nicht.

![Seite mit der Zusammenfassung des Braze Initialisierungs-Tags, auf der Sie eine Übersicht über das Tag zusammen mit Informationen zu den getriggerten Tags finden.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

### Ausführliche Protokollierung einschalten

Damit der technische Support von Braze während der Tests auf die Protokolle zugreifen kann, können Sie die ausführliche Protokollierung in Ihrer Google Tag Manager-Integration aktivieren. Diese Protokolle erscheinen auf der Registerkarte **Konsole** der [Entwicklertools](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) Ihres Browsers.

Navigieren Sie in der Google Tag Manager-Integration zu Ihrem Braze Initialisierungs-Tag und wählen Sie **Web SDK-Protokollierung aktivieren**.

![Seite mit der Zusammenfassung des Braze Initialisierungs-Tags und der aktivierten Option "Web SDK-Protokollierung aktivieren".]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
