---
nav_title: Shopify Standard-Integration einrichten
article_title: "Shopify Standard-Integration einrichten"
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie die Standard Shopify Integration einrichten."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# Shopify Standard-Integration einrichten

> Auf dieser Seite erfahren Sie, wie Sie Braze mithilfe unserer Standardintegration für Nutzer:innen mit einem Shopify-Onlineshop in Shopify integrieren können. Wenn Sie eine Shopify-Website ohne Kopfzeile verwenden oder weitere angepasste Lösungen implementieren möchten, lesen Sie bitte den Abschnitt [Einrichtung der angepassten Integration in Shopify]({{site.baseurl}}/shopify_custom_integration/).

## Schritt 1: Verbinden Sie Ihren Shopify Shop

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und suchen Sie dann nach "Shopify".

{% alert note %}
Wenn Sie die ältere Navigation verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

{: start="2"}
2\. Wählen Sie auf der Shopify Partnerseite **Einrichtung beginnen**, um die Integration zu starten.<br><br>![Shopify Integrationsseite mit Button, um mit der Einrichtung zu beginnen.]({% image_buster /assets/img/Shopify/begin_setup.png %})<br><br> 
3\. Installieren Sie im Shopify App-Store die Anwendung Braze.<br><br>![Die Braze App Shop Seite mit einem Button zur Installation der Anwendung.]({% image_buster /assets/img/Shopify/shopify_log_in.png %}){: style="max-width:70%;"}

{% alert note %}
Wenn Ihr Shopify-Konto mit mehr als einem Shop verbunden ist, können Sie den Shop, bei dem Sie angemeldet sind, ändern, indem Sie das Shop-Symbol oben rechts auf der Seite auswählen und **Shop wechseln** wählen.
{% endalert %}

{: start="4"}
4\. Nach der Installation der Braze App werden Sie zu Braze weitergeleitet, um den Workspace zu bestätigen, den Sie mit Shopify verbinden möchten. Ein Shopify Shop kann sich nur mit einem Workspace verbinden. Wenn Sie wechseln müssen, wählen Sie den richtigen Workspace aus.<br><br>![Ein Fenster, das Sie auffordert zu bestätigen, dass Sie sich im richtigen Workspace befinden.]({% image_buster /assets/img/Shopify/confirm_workspace1.png %}){: style="max-width:70%;"}

{: start="5"}
5\. Wählen Sie **Einrichtung beginnen**.<br><br>!["Integrationseinstellungen" mit einem Feld zur Eingabe der Domain und einem Button zum Starten der Einrichtung.]({% image_buster /assets/img/Shopify/choose_account.png %})

## Schritt 2: Enablement von Braze Internet SDKs

Für Shopify Online-Shops können Sie das Standard-Setup auswählen, um das Braze Internet SDK und das JavaScript SDK automatisch zu implementieren.

![Schritt "Internet SDK aktivieren" mit Optionen zur Implementierung über eine Standardeinrichtung oder eine angepasste Einrichtung.]({% image_buster /assets/img/Shopify/sdk_setup.png %})

Nachdem Sie den Standardpfad für das Onboarding ausgewählt haben, müssen Sie aus einer der folgenden Optionen auswählen, wann Braze initialisiert und die SDKs geladen werden sollen: 
- Beim Besuch vor Ort, z.B. zu Beginn der Sitzung
    - Tracking von identifizierten und anonymen Nutzer:innen
- Bei der Anmeldung eines Kontos, z.B. bei der Anmeldung eines Kontos
    - Nur identifizierte Nutzer:innen verfolgen
    - Startet das Tracking von Daten, wenn sich Besucher der Website registrieren oder bei ihren Konten anmelden.

## Schritt 3: Konfigurieren Sie Ihre Shopify Daten

### Standard Daten einrichten

Jetzt wählen Sie die Shopify Daten aus, die Sie tracken möchten.

![Abschnitt "Tracking von Shopify-Daten" mit einem Kontrollkästchen zum Tracking von Verhaltensdaten und Nutzer:innen-Attributen.]({% image_buster /assets/img/Shopify/tracking_shopify_data.png %})

Die folgenden Ereignisse werden in der Standard Integration standardmäßig aktiviert.

| Braze empfohlene Veranstaltungen | Shopify angepasste Events | Angepasste Shopify-Attribute |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Angesehenes Produkt</li><li>Warenkorb aktualisiert</li><li>Checkout gestartet</li><li>Bestellung aufgegeben</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_bezahlte_bestellung</li><li>shopify_bestellung_storniert</li><li>shopify_bestellung_erstattet</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_provinz</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

Weitere Informationen zu den Daten, die durch die Integration getrackt werden, finden Sie unter [Shopify Data Features]({{site.baseurl}}/shopify_data_features/).

### Historischer Aufbau der Verfüllung

Bei der Standardeinrichtung haben Sie die Möglichkeit, eine erste Ladung Ihrer Shopify Kunden und Bestellungen aus den letzten 90 Tagen vor der Anbindung an die Shopify Integration durchzuführen. Wählen Sie dazu das Kontrollkästchen aus, um das anfängliche Laden der Daten als Teil Ihrer Integration einzuschließen. 

![Historische Daten umschalten.]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

Diese Tabelle enthält die Daten, die anfänglich über das Backfill geladen werden sollen.

| Braze empfohlene Veranstaltungen | Shopify angepasste Events | Braze Standard Attribute | Braze Abo-Status |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Bestellung aufgegeben</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_provinz</li></ul>{:/} | {::nomarkdown}<ul><li>E-Mail</li><li>Vorname</li><li>Nachname</li><li>Telefon</li><li>Ort</li><li>Land</li></ul>{:/} | {::nomarkdown}<ul><li>E-Mail Marketing Abos, die mit diesem Shopify Shop verbunden sind</li><li>SMS-Marketing Abos, die mit diesem Shopify Shop verbunden sind</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

Wenn Ihre Shopify Kund:in-Datensätze in Braze geladen werden, wird die Shopify Kund:in-ID als externe ID von Braze verwendet. 

{% alert note %}
Wenn Sie ein bestehender Braze-Kunde mit aktiven Kampagnen oder Canvase sind, lesen Sie die [Shopify Daten Features]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill) für weitere Details.
{% endalert %}

### (Fortgeschrittene) Einrichtung des angepassten Daten Trackings

Mit den Braze SDKs können Sie angepasste Events oder angepasste Attribute verfolgen, die über die Standard-Events für diese Integration hinausgehen. Angepasste Events erfassen eindeutige Interaktionen in Ihrem Shop, wie zum Beispiel:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="width: 50%;">Angepasste Events</th>
      <th style="width: 50%;">Angepasste Attribute</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Einen angepassten Rabattcode verwenden</li>
          <li>Mit personalisierter Produktempfehlung interagiert</li>
          <li>Der Bestellung eine Geschenkbotschaft beifügen</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Bevorzugte Marken oder Produkte</li>
          <li>Bevorzugte Einkaufskategorien</li>
          <li>Zugehörigkeit oder Treuestatus</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

Durch das Tracking angepasster Daten erhalten Sie tiefere Insights in das Nutzerverhalten und können die Erfahrungen der Nutzer:innen noch besser personalisieren. Um angepasste Events zu implementieren, müssen Sie [den Code Ihres Schaufensterdesigns](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) in der Datei `theme.liquid` bearbeiten. Vielleicht brauchen Sie die Hilfe Ihrer Entwickler:in.

Das folgende JavaScript-Snippet verfolgt zum Beispiel, ob der:die aktuelle Nutzer:in einen Newsletter abonniert hat, und protokolliert dies als angepasstes Event im individuellen Nutzerprofil in Braze:

```json
braze.logCustomEvent(
  “subscribed_to_newsletter”,
  {
    newsletterName: ‘News and Offers’,
    customerEmail: ‘customer_1@gmail.com’,
    sendOffers: true
  }
);

```

Das SDK muss auf dem Gerät eines Nutzers initialisiert werden (auf Aktivitäten warten), um Events oder angepasste Attribute zu protokollieren. Um mehr über die Protokollierung angepasster Daten zu erfahren, lesen Sie [User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) und [logCustomEvent object](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

## Schritt 4: Konfigurieren Sie, wie Sie Nutzer:innen verwalten

Wählen Sie Ihren `external_id` Typ aus der Dropdown-Liste aus. 

![Abschnitt "Abonnent:innen sammeln".]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
Die Verwendung einer E-Mail-Adresse oder einer gehashten E-Mail-Adresse als externe ID von Braze kann die Identitätsverwaltung über Ihre Datenquellen hinweg vereinfachen. Es ist jedoch wichtig, die potenziellen Risiken für den Datenschutz und die Datensicherheit der Nutzer:innen zu berücksichtigen.<br><br>

- **Erratbare Informationen:** E-Mail-Adressen sind leicht zu erraten, was sie anfällig für Angriffe macht.
- **Risiko der Ausbeutung:** Wenn ein böswilliger Nutzer:innen seinen Webbrowser so verändert, dass er die E-Mail-Adresse einer anderen Person als externe ID verwendet, kann er möglicherweise auf sensible Nachrichten oder Kontoinformationen zugreifen.
{% endalert %}

Wenn Sie einen angepassten externen ID-Typ ausgewählt haben, fahren Sie mit den Schritten 4.1 und 4.2 fort. Andernfalls fahren Sie mit Schritt 4.3 fort.

### Schritt 4.1: Erstellen Sie eine angepasste `external_id`

Gehen Sie zunächst zu Shopify und erstellen Sie das Metafeld `braze.external_id`. Wir empfehlen Ihnen, die Schritte unter [Anpassen von Metafeldbeschreibungen](https://help.shopify.com/en/manual/custom-data/metafields/metafield-definitions/creating-custom-metafield-definitions) zu befolgen. Geben Sie für **Namensraum und Schlüssel** `braze.external_id` ein. Für **Typ** empfehlen wir Ihnen, einen ID-Typ zu wählen.

Nachdem Sie das Metafelder erstellt haben, hören Sie auf [`customer/create` Webhooks](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks), damit Sie das Metafelder schreiben können, wenn eine neue Kund:in erstellt wird. Verwenden Sie dann die [Admin API](https://shopify.dev/docs/api/admin-graphql) oder die [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer), um alle Ihre zuvor erstellten Kund:in mit diesem Metafeld zu versehen.

### Schritt 4.2: Einen Endpunkt erstellen

Sie benötigen einen öffentlichen GET-Endpunkt, um Ihre externe ID abzurufen. Wenn Shopify das Metafeld nicht bereitstellen kann, ruft Braze diesen Endpunkt auf, um die externe ID abzurufen.

Ein Beispiel für einen Endpunkt ist: `https://mystore.com/custom_id?shopify_customer_id=1234&email_address=raghav.narain@braze.com&shopify_storefront=dev-store.myshopify.com`

#### Antwort

Braze erwartet einen `200` Status Code. Jeder andere Code wird als Fehler des Endpunkts betrachtet. Die Antwort sollte lauten:

{% raw %}
```json
{ "external_id": "my_external_id" }
```
{% endraw %}

Passen Sie die `shopify_customer_id` und die E-Mail Adresse mit Hilfe der Admin API oder der Customer API an, um sicherzustellen, dass die Parameterwerte mit den Kunden:in in Shopify übereinstimmen. Nach der Validierung können Sie auch die APIs verwenden, um das Metafeld `braze.external_id` abzurufen und den Wert der externen ID zurückzugeben.

### Schritt 4.3: Sammeln Sie Ihre E-Mail- oder SMS-Opt-ins von Shopify (optional)

Sie haben die Möglichkeit, Ihre Opt-ins für E-Mail- oder SMS-Marketing in Shopify zu sammeln. 

Wenn Sie die Kanäle E-Mail oder SMS nutzen, können Sie Ihre Opt-in-Status für E-Mail- und SMS-Marketing mit Braze synchronisieren. Wenn Sie Opt-ins für das E-Mail Marketing von Shopify synchronisieren, erstellt Braze automatisch eine Abo-Gruppe für alle Nutzer:innen, die mit diesem Shop verbunden sind. Sie müssen einen eindeutigen Namen für diese Abo-Gruppe erstellen.

![Abschnitt "Abonnent:innen sammeln" mit der Option, Opt-ins für E-Mail- oder SMS-Marketing zu sammeln.]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
Wie in der [Übersicht von Shopify]({{site.baseurl}}/shopify_overview/) erwähnt, müssen Ihre Entwickler:in den Code für das Braze SDK integrieren, wenn Sie ein Erfassungsformular eines Drittanbieters verwenden möchten. Auf diese Weise können Sie die E-Mail Adresse und den Status des globalen E-Mail Abos von Formularen erfassen. Genauer gesagt, müssen Sie diese Methoden in Ihre `theme.liquid` Datei implementieren und testen:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Legt die E-Mail Adresse im Nutzerprofil fest
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Aktualisiert den Status des globalen E-Mail-Abos
{% endalert %}

## Schritt 5: Produkte synchronisieren (optional)

Sie können alle Produkte aus Ihrem Shopify Shop mit einem Braze Katalog synchronisieren, um die Personalisierung von Nachrichten zu vertiefen. Automatische Updates erfolgen nahezu in Realtime, so dass Ihr Katalog immer die neuesten Produktdaten enthält. Wenn Sie mehr darüber erfahren möchten, lesen Sie [Shopify Produkt-Synchronisation]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/).

![Schritt 4 der Einrichtung mit "Shopify Variant ID" als "Bezeichner für das Produkt im Katalog".]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:80%;"}

## Schritt 6: Kanäle aktivieren (optional)

Sie können In-App-Nachrichten auch ohne einen Entwickler:in aktivieren, indem Sie sie in Ihrem Setup konfigurieren.

![Einrichtungsschritt zur Aktivierung von Kanälen, wobei die verfügbare Option In-Browser Messaging ist.]({% image_buster /assets/img/Shopify/activate_channels_standard.png %})

{% alert note %}
Braze sammelt über In-Browser-Nachrichten Informationen über Besucher, wie z.B. E-Mail-Adressen und Telefonnummern. Diese Informationen werden dann an Shopify gesendet. Diese Daten helfen Händlern, die Besucher ihres Shops zu erkennen und ein personalisiertes Einkaufserlebnis zu schaffen. Weitere Einzelheiten finden Sie unter [Besucher-API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

### Unterstützung für zusätzliche SDK Kanäle

Die SDKs von Braze ermöglichen verschiedene Messaging-Kanäle, einschließlich Content-Cards.

#### Content-Cards und Feature-Flags

Um Content-Cards oder Feature-Flags hinzuzufügen, müssen Sie mit Ihren Entwickler:in zusammenarbeiten, um den erforderlichen SDK Code direkt in Ihre `theme.liquid` Datei einzufügen. Eine ausführliche Anleitung finden Sie unter [Integration des Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/). 

#### Web-Push-Benachrichtigungen

Web-Push wird derzeit für die Shopify-Integration nicht unterstützt. Wenn Sie möchten, dass dies in Zukunft unterstützt wird, reichen Sie eine Anfrage für ein Produkt über das [Braze Produktportal]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) ein.

Wenn Sie möchten, dass dies in Zukunft unterstützt wird, stellen Sie eine Anfrage für ein Produkt über das Braze [Produktportal]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

## Schritt 7: Einrichtung abschließen

1. Nachdem Sie Ihre Einrichtung konfiguriert haben, wählen Sie **Einrichtung beenden**.
2. Aktivieren Sie die Einbettung der Braze App in Ihren Shopify Themeneinstellungen. Wählen Sie **Shopify öffnen**, um zu Ihrem Shopify-Konto weitergeleitet zu werden, um die Einbettung der App in den Themeneinstellungen Ihres Shops zu aktivieren. 

![Ein Banner, das darauf hinweist, dass Sie die Einbettung der Braze App in Shopify aktivieren müssen und einen Button zum Öffnen von Shopify enthält.]({% image_buster /assets/img/Shopify/open_shopify.png %})

{: start="3"}
3\. Nachdem Sie die Einbettung der App aktiviert haben, ist Ihre Einrichtung abgeschlossen!
Bestätigen Sie, dass Sie Ihre Integrationseinstellungen, den Status der ersten Datensynchronisation und Ihre aktiven Shopify-Ereignisse einsehen können. <br><br>![Shopify Partnerseite mit den Einstellungen für die Integration.]({% image_buster /assets/img/Shopify/install_complete.png %})