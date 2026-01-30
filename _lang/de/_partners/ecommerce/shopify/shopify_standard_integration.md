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
| {::nomarkdown}<ul><li>Angesehenes Produkt</li><li>Warenkorb aktualisiert</li><li>Checkout gestartet</li><li>Bestellung aufgegeben</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

Weitere Informationen zu den Daten, die durch die Integration getrackt werden, finden Sie unter [Shopify Data Features]({{site.baseurl}}/shopify_data_features/).

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

### Historischer Aufbau der Verfüllung

Bei der Standardeinrichtung haben Sie die Möglichkeit, eine erste Ladung Ihrer Shopify Kunden und Bestellungen aus den letzten 90 Tagen vor der Anbindung an die Shopify Integration durchzuführen. Wählen Sie dazu das Kontrollkästchen aus, um das anfängliche Laden der Daten als Teil Ihrer Integration einzuschließen. 

![Historische Daten umschalten.]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

Diese Tabelle enthält die Daten, die anfänglich über das Backfill geladen werden sollen.

| Braze empfohlene Veranstaltungen | Shopify angepasste Events | Braze Standard Attribute | Braze Abo-Status |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Bestellung aufgegeben</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>E-Mail</li><li>Vorname</li><li>Nachname</li><li>Telefon</li><li>Ort</li><li>Land</li></ul>{:/} | {::nomarkdown}<ul><li>E-Mail Marketing Abos, die mit diesem Shopify Shop verbunden sind</li><li>SMS-Marketing Abos, die mit diesem Shopify Shop verbunden sind</li></ul>{:/} |
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

Das Tracking angepasster Daten bietet tiefere Insights in das Nutzerverhalten und unterstützt eine zusätzliche Personalisierung. Um angepasste Events zu implementieren, müssen Sie [den Code Ihres Schaufensterdesigns](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) in der Datei `theme.liquid` bearbeiten. Vielleicht brauchen Sie die Hilfe Ihrer Entwickler:in.

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

## Schritt 4: Konfigurieren Sie, wie Sie Nutzer:innen verwalten {#step-4}

Wählen Sie Ihren `external_id` Typ aus der Dropdown-Liste aus. 

![Abschnitt "Abonnent:innen sammeln".]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
Die Verwendung einer E-Mail-Adresse oder einer gehashten E-Mail-Adresse als externe ID von Braze kann die Identitätsverwaltung über Ihre Datenquellen hinweg vereinfachen. Es ist jedoch wichtig, die potenziellen Risiken für den Datenschutz und die Datensicherheit der Nutzer:innen zu berücksichtigen.<br><br>

- **Erratbare Informationen:** E-Mail-Adressen sind leicht zu erraten, was sie anfällig für Angriffe macht.
- **Risiko der Ausbeutung:** Wenn ein böswilliger Nutzer:innen seinen Webbrowser so verändert, dass er die E-Mail-Adresse einer anderen Person als externe ID verwendet, kann er möglicherweise auf sensible Nachrichten oder Kontoinformationen zugreifen.
{% endalert %}

Standardmäßig wandelt Braze E-Mails von Shopify automatisch in Kleinbuchstaben um, bevor es sie als externe ID verwendet. Wenn Sie E-Mail oder gehashte E-Mail als externe ID verwenden, vergewissern Sie sich, dass Ihre E-Mail-Adressen auch in Kleinbuchstaben umgewandelt werden, bevor Sie sie als externe ID zuweisen oder bevor Sie sie aus anderen Datenquellen hashen. Dies hilft, Diskrepanzen bei externen IDs zu vermeiden und die Erstellung doppelter Nutzerprofile in Braze zu verhindern.

{% alert note %}
Die nächsten Schritte hängen davon ab, welche externe ID Sie ausgewählt haben:<br><br>
- **Wenn Sie einen angepassten externen ID-Typ ausgewählt haben:** Führen Sie die Schritte 4.1-4.3 aus, um Ihre angepasste externe ID-Konfiguration einzurichten.
- **Wenn Sie die ID, E-Mail oder Hash-E-Mail von Shopify ausgewählt haben:** Überspringen Sie die Schritte 4.1-4.3 und fahren Sie direkt mit Schritt 4.4 fort.
{% endalert %}

### Schritt 4.1: Erstellen Sie das Metafeld `braze.external_id` 

1. Gehen Sie in Ihrem Shopify Admin Panel zu **Einstellungen** > **Metafelder und Metaobjekte**.
2. Wählen Sie **Kunden** > **Definition hinzufügen**.
3. Geben Sie für **Name** `braze.external_id` ein. 
4. Wählen Sie den automatisch generierten Namensraum und Schlüssel (`custom.braze_external_id`) aus, um ihn zu bearbeiten und in `braze.external_id` zu ändern.
5. Wählen Sie unter **Typ** den **ID-Typ** aus.

Nachdem das Metafeld erstellt wurde, füllen Sie es für Ihre Kund:in aus. Wir empfehlen die folgenden Ansätze:

- **Hören Sie sich die Webhooks zur Erstellung von Kund:in an:** Richten Sie einen Webhook ein, um auf die [Ereignisse von`customer/create` ](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks) zu warten. Damit können Sie das Metafeld schreiben, wenn eine neue Kund:in angelegt wird.
- **Füllen Sie bestehende Kund:in nach:** Verwenden Sie die [Admin API](https://shopify.dev/docs/api/admin-graphql) oder die [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer), um das Metafeld für zuvor erstellte Kund:innen zu füllen.

### Schritt 4.2: Erstellen Sie einen Endpunkt zum Abrufen Ihrer externen ID

Sie müssen einen öffentlichen Endpunkt erstellen, den Braze zum Abrufen der externen ID aufrufen kann. Dadurch kann Braze die ID in Szenarien abrufen, in denen Shopify das Metafeld `braze.external_id` nicht direkt bereitstellen kann.

#### Endpunkt-Spezifikationen

**Methode:** GET

Braze sendet die folgenden Parameter an Ihren Endpunkt:

| Parameter            | Erforderlich | Datentyp | Beschreibung                                                      |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id  | Ja      | String    | Die Shopify ID des Kunden.                                         |
| shopify_storefront   | Ja      | String    | Der Schaufenstername für die Anfrage. Ex: `<storefront_name>.myshopify.com` |
| email_address        | Kein:e       | String    | Die E-Mail Adresse des angemeldeten Nutzers:in. <br><br>Dieses Feld kann in bestimmten Webhook-Szenarien fehlen. Ihre Endpunkt-Logik sollte hier Nullwerte berücksichtigen (z.B. holen Sie die E-Mail über shopify_customer_id, wenn Ihre interne Logik dies erfordert). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### Beispiel Endpunkt

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@braze.com&shopify_storefront=dev-store.myshopify.com
```

#### Erwartete Antwort
Braze erwartet einen `200` Status Code, der die externe ID JSON zurückgibt:
```json
{
  "external_id": "my_external_id"
}
```

#### Validierung
Es ist wichtig, dass Sie überprüfen, ob `shopify_customer_id` und `email_address` (falls vorhanden) mit den Werten der Kund:in in Shopify übereinstimmen. Sie können die [Shopify Admin API](https://shopify.dev/docs/api/admin-graphql) oder die [Kund:in API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) verwenden, um diese Parameter zu validieren und das richtige `braze.external_id` Metafeld abzurufen.

#### Versagensverhalten und Zusammenführung
Jeder andere Status Code als `200` wird als Fehlschlag betrachtet.

- **Auswirkungen der Verschmelzung:** Wenn der Endpunkt fehlschlägt (nicht`200` oder Timeout), kann Braze die externe ID nicht abrufen. Folglich wird die Zusammenführung zwischen dem Shopify Nutzer:in und dem Braze Nutzerprofil zu diesem Zeitpunkt nicht stattfinden.
- **Wiederholungslogik:** Braze kann standardmäßig sofortige Wiederholungsversuche im Netzwerk unternehmen, aber wenn der Fehler weiterhin besteht, wird die Zusammenführung bis zum nächsten qualifizierenden Ereignis aufgeschoben (z.B. wenn der Nutzer:innen sein Profil aktualisiert oder einen Checkout abschließt).
- **Unterstützbarkeit:** Um die rechtzeitige Zusammenführung von Nutzer:innen zu unterstützen, stellen Sie sicher, dass Ihr Endpunkt hochverfügbar ist und das optionale Feld `email_address` zuverlässig verarbeitet.

### Schritt 4.3: Geben Sie Ihre externe ID ein

Wiederholen Sie [Schritt 4](#step-4) und geben Sie Ihre Endpunkt-URL ein, nachdem Sie die angepasste externe ID als Ihren externen ID-Typ von Braze ausgewählt haben.

#### Überlegungen

- Wenn Ihre externe ID nicht generiert wird, wenn Braze eine Anfrage an Ihren Endpunkt sendet, verwendet die Integration standardmäßig die Shopify Kund:innen-ID, wenn die Funktion `changeUser` aufgerufen wird. Dieser Schritt ist entscheidend für die Zusammenführung des anonymen Nutzerprofils mit dem identifizierten Nutzerprofil. Daher kann es vorübergehend vorkommen, dass in Ihrem Workspace verschiedene Arten von externen IDs existieren.
- Wenn die externe ID im Metafeld `braze.external_id` verfügbar ist, wird die Integration diese externe ID priorisieren und zuweisen. 
    - Wenn die Shopify Kund:in ID zuvor als externe ID von Braze eingestellt war, wird sie durch den Wert des Metafelds `braze.external_id` ersetzt. 

### Schritt 4.4: Sammeln Sie Ihre E-Mail- oder SMS-Opt-ins von Shopify (optional)

Sie haben die Möglichkeit, Ihre Opt-ins für E-Mail- oder SMS-Marketing in Shopify zu sammeln. 

Wenn Sie die Kanäle E-Mail oder SMS nutzen, können Sie Ihre Opt-in-Status für E-Mail- und SMS-Marketing mit Braze synchronisieren. Wenn Sie Opt-ins für das E-Mail Marketing von Shopify synchronisieren, erstellt Braze automatisch eine Abo-Gruppe für alle Nutzer:innen, die mit diesem Shop verbunden sind. Sie müssen einen eindeutigen Namen für diese Abo-Gruppe erstellen.

![Abschnitt "Abonnent:innen sammeln" mit der Option, Opt-ins für E-Mail- oder SMS-Marketing zu sammeln.]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
Wie in der [Übersicht von Shopify]({{site.baseurl}}/shopify_overview/) erwähnt, müssen Ihre Entwickler:in den Code für das Braze SDK integrieren, wenn Sie ein Erfassungsformular eines Drittanbieters verwenden möchten. Auf diese Weise können Sie die E-Mail Adresse und den Status des globalen E-Mail Abos von Formularen erfassen. Genauer gesagt, müssen Sie diese Methoden in Ihre `theme.liquid` Datei implementieren und testen:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Legt die E-Mail Adresse im Nutzerprofil fest
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Aktualisiert den Status des globalen E-Mail-Abos
{% endalert %}

## Schritt 5: Produkte synchronisieren (optional)

Sie können alle Produkte aus Ihrem Shopify Shop mit einem Braze Katalog synchronisieren, um die Personalisierung von Nachrichten zu vertiefen. Automatische Updates erfolgen nahezu in Realtime, so dass Ihr Katalog stets aktuelle Produktdaten enthält. Wenn Sie mehr darüber erfahren möchten, lesen Sie [Shopify Produkt-Synchronisation]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/).

![Schritt 4 der Einrichtung mit "Shopify Variant ID" als "Bezeichner für das Produkt im Katalog".]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:80%;"}

## Schritt 6: Kanäle aktivieren (optional)

Sie können In-App-Nachrichten auch ohne einen Entwickler:in aktivieren, indem Sie sie in Ihrem Setup konfigurieren.

![Einrichtungsschritt zur Aktivierung von Kanälen, wobei die verfügbare Option In-Browser Messaging ist.]({% image_buster /assets/img/Shopify/activate_channels_standard.png %})

{% alert note %}
Braze sammelt über In-Browser-Nachrichten Informationen über Besucher, wie z.B. E-Mail-Adressen und Telefonnummern. Diese Informationen werden an Shopify gesendet. Diese Daten ermöglichen es Händlern, Besucher ihres Shops zu erkennen und ein personalisiertes Einkaufserlebnis zu schaffen. Weitere Einzelheiten finden Sie unter [Besucher-API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

### Unterstützung für zusätzliche SDK Kanäle

Die SDKs von Braze ermöglichen verschiedene Messaging-Kanäle, einschließlich Content-Cards.

#### Content-Cards und Feature-Flags

Um Content-Cards oder Feature-Flags hinzuzufügen, müssen Sie mit Ihren Entwickler:in zusammenarbeiten, um den erforderlichen SDK Code direkt in Ihre `theme.liquid` Datei einzufügen. Eine ausführliche Anleitung finden Sie unter [Integration des Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/). 

#### Web-Push-Benachrichtigungen

Internet-Push wird für die Shopify-Integration derzeit nicht unterstützt. Um Support anzufordern, stellen Sie eine Anfrage für ein Produkt über das [Braze-Produktportal]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

## Schritt 7: Einrichtung abschließen

1. Nachdem Sie Ihre Einrichtung konfiguriert haben, wählen Sie **Einrichtung beenden**.
2. Aktivieren Sie die Einbettung der Braze App in Ihren Shopify Themeneinstellungen. Wählen Sie **Shopify öffnen**, um zu Ihrem Shopify-Konto weitergeleitet zu werden, um die Einbettung der App in den Themeneinstellungen Ihres Shops zu aktivieren. 

![Ein Banner, das darauf hinweist, dass Sie die Einbettung der Braze App in Shopify aktivieren müssen und einen Button zum Öffnen von Shopify enthält.]({% image_buster /assets/img/Shopify/open_shopify.png %})

{: start="3"}
3\. Nachdem Sie die Einbettung der App aktiviert haben, ist Ihre Einrichtung abgeschlossen!
Bestätigen Sie, dass Sie Ihre Integrationseinstellungen, den Status der ersten Datensynchronisation und Ihre aktiven Shopify-Ereignisse einsehen können. <br><br>![Shopify Partnerseite mit den Einstellungen für die Integration.]({% image_buster /assets/img/Shopify/install_complete.png %})