---
nav_title: Offene Loyalität
article_title: Offene Loyalität
description: "Die Integration von Braze und Open Loyalty erlaubt es Ihnen, Loyalitätsdaten wie Punktestand, Tier-Änderungen und Ablaufwarnungen in Echtzeit direkt mit Braze zu synchronisieren."
alias: /partners/openloyalty/
page_type: partner
search_tag: Partner
---

# Offene Loyalität

> [Open Loyalty](https://www.openloyalty.io/) ist eine cloudbasierte Plattform für Kundenbindungsprogramme, mit der Sie Kundenbindungs- und Rewards-Programme erstellen und verwalten können. Die Integration von Braze und Open Loyalty synchronisiert Loyalitätsdaten wie Punktestand, Tier-Änderungen und Ablaufwarnungen direkt mit Braze in Realtime. Damit können Sie personalisierte Nachrichten (E-Mail, Push, SMS) triggern, wenn sich der Treuestatus eines Nutzers:innen ändert.

_Diese Integration wird von Open Loyalty gepflegt_

## Über die Integration

Diese Integration verwendet Braze Data Transformations, um Webhooks von Open Loyalty zu erfassen und sie auf Nutzerprofile von Braze abzubilden.

* **Updates in Echtzeit**: Pushen Sie Loyalitätsereignisse (verdiente Punkte, Tier Upgrades) auf Braze.
* **Personalisierung**: Verwenden Sie in Ihren Braze Templates Attribute zur Loyalität (aktueller Saldo, Name der nächsten Stufe).
* **Bi-direktional**: Aktualisieren Sie die angepassten Attribute von Open Loyalty Kund:in auf der Grundlage von Braze Engagement-Daten.

## Anwendungsfälle

Diese Integration umfasst die folgenden Datenflüsse:

1. **Synchronisierung von Ereignissen mit Braze (eingehend)**: Verfolgen Sie Punktänderungen, Upgrades oder Einlösungen von Prämien, indem Sie Daten von Open Loyalty an Braze senden. Die Datentransformation wandelt diese Daten in ein Nutzer:innen-Ereignis um.
2. **Ändern von geöffneten Treue-Mitgliedern (ausgehend)**: Aktualisieren Sie automatisch Nutzerdaten in Open Loyalty auf der Grundlage des Kundenverhaltens in Braze, z.B. durch Hinzufügen von "VIP"-Etiketten oder Aktualisieren angepasster Attribute.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Anforderung | Beschreibung |
| :--- | :--- |
| Loyalty-Konto öffnen | Sie benötigen ein Admin-Konto auf einem Open Loyalty Tenant, um von dieser Partnerschaft zu profitieren. |
| Öffnen Sie Loyalty REST API-Schlüssel | Ein Open Loyalty REST API-Schlüssel (für Integrationen, die Daten von Braze an Open Loyalty senden). <br><br> Erstellen Sie diesen unter **Einstellungen > Admins > API-Schlüssel**. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Erstellen Sie diesen Schlüssel im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. |
| Braze Data Transformation | Sie benötigen Zugriff auf den Tab "Dateneinstellungen" in Braze, um Webhook-Listener zu konfigurieren. |
| Übereinstimmende IDs | Die `external_id` des Nutzers:in in Braze muss mit seiner `loyaltyCardNumber` (oder einem anderen Standard Bezeichner) in Open Loyalty übereinstimmen. |
| Mandanten-ID | Ihre Open Loyalty Tenant ID (erforderlich für ausgehende Updates). |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Integration

Die primäre Integration synchronisiert Open Loyalty-Webhook-Ereignisse mit Braze über Datentransformation.

### Schritt 1: Generieren Sie die Webhook-URL in Braze

Erstellen Sie zunächst eine Datentransformation in Braze, um eine eindeutige URL für den Empfang von Daten zu generieren.

1.  Öffnen Sie in Braze **Dateneinstellungen > Datentransformation.**
2.  Klicken Sie auf **Transformation erstellen**.
3.  Füllen Sie die folgenden Felder aus:
     * **Name der Transformation**: Geben Sie einen beschreibenden Namen ein (z.B. "Öffnen Sie Treuepunkte Update Events").
     * **Wählen Sie ein Ziel aus**: Wählen Sie **POST: Nutzer:innen tracken**.
4.  Klicken Sie auf **Transformation erstellen**.
5.  Suchen Sie die **Webhook-URL** auf der rechten Seite und klicken Sie auf **Kopieren**.

{% alert important %}
Bewahren Sie diese URL sicher auf; Sie benötigen sie für den nächsten Schritt.
{% endalert %}

### Schritt 2: Erstellen Sie das Webhook-Abonnement in Open Loyalty

Weisen Sie Open Loyalty an, bestimmte Ereignisse an die URL zu senden, die Sie gerade erstellt haben.

1.  Melden Sie sich in Ihrem Open Loyalty Admin Panel an.
2.  Navigieren Sie zu **Allgemein > Webhooks**.
3.  Klicken Sie auf **Neuen Webhook hinzufügen** und konfigurieren Sie das Abo:
    * **EreignisName**: Wählen Sie das Ereignis aus, das Sie tracken möchten (z.B. `AvailablePointsAmountChanged`, `CustomerLevelChanged`, oder `CampaignEffectWasApplied`).
    * **url**: Fügen Sie die Braze-Webhook-URL aus Schritt 1 ein.
    * Fügen Sie die folgenden Kopfzeilen hinzu:
      * `Content-Type: application/json`
      * `User-Agent: partner-OpenLoyalty`
4.  Speichern Sie das Webhook Abo.

### Schritt 3: Konfigurieren Sie die Datentransformation

Schreiben Sie die JavaScript-Logik in Braze, um die eingehenden Open Loyalty-Payloads den Eigenschaften von Braze zuzuordnen.

1.  Öffnen Sie in Braze die Datentransformation, die Sie in Schritt 1 erstellt haben.
2.  Triggern Sie das Ereignis in Open Loyalty (z.B. ändern Sie die Punkte eines Mitglieds oder weisen Sie eine Stufe zu), um eine Beispiel-Nutzlast in der **Webhook-Detailansicht** zu erzeugen.
3.  Schreiben Sie im **Code-Editor** für **die Transformation** ein Skript für die Abbildung der eingehenden Daten. Verwenden Sie das folgende Beispiel als Anhaltspunkt:

```javascript
// 1. Parse the incoming Open Loyalty payload
const data = payload.data;

// 2. Construct the Braze API body
let brazecall = {
  "events": [
    {
      // CRITICAL: Map the identifier (e.g., loyaltyCardNumber -> external_id)
      "external_id": data.customer.loyaltyCardNumber,
     
      // Define the Event Name (what you see in Braze)
      "name": "Loyalty Event Triggered",
     
      // timestamp
      "time": new Date().toISOString(),
     
      // Map specific properties you want to use in emails/segments
      "properties": {
        "event_type": payload.type, // for example, 'AvailablePointsAmountChanged'
        "new_balance": data.amount,
        "change_amount": data.amountChange,
        "tier_name": data.tier ? data.tier.name : null
      }
    }
  ]
};

return brazecall;
```

{: start="4"}
4\. Klicken Sie auf **Validieren**, um sicherzustellen, dass der Code mit Ihrer Beispiel-Nutzlast funktioniert, und klicken Sie dann auf **Aktivieren**.


## Verwendung von Open Loyalty mit Braze

Nachdem Sie die eingehende Integration abgeschlossen haben, konfigurieren Sie **ausgehende Updates**, um offene Loyalitätsmitglieder auf der Grundlage des Verhaltens von Braze zu ändern.

### Schritt 1: Konfigurieren Sie die Braze-to-Braze-Webhook-Kampagne

Dieser Prozess verwendet Braze-Webhooks, um eine `PATCH` Anfrage an die Open Loyalty Member API zu senden (zum Beispiel, um ein "VIP"-Label hinzuzufügen).

1.  Erstellen Sie in Braze eine neue **Webhook-Kampagne** (oder verwenden Sie einen Webhook innerhalb eines Canvas).
2.  Klicken Sie auf **Webhook zusammenstellen**.
3.  **Webhook URL**: Konstruieren Sie die URL unter Verwendung Ihrer Open Loyalty Instanz, der Tenant ID und der Braze Liquid Variable für die Nutzer:in.
    * Format:
      {% raw %}
      `https://<YOUR_OL_INSTANCE>/api/<TENANT_ID>/member/loyaltyCardNumber={{${user_id}}}`
      {% endraw %}
4. Füllen Sie die folgenden Felder aus:   
    * **Anfrage Methode**: `PATCH`
    * **Anfrage-Header**:
      * `Content-Type`: `application/json`
      * `X-AUTH-TOKEN`: `<YOUR_PERMANENT_TOKEN>`
      * `User-Agent: Braze`
5.  **Anfrage Körper**: Wählen Sie `Raw text` und fügen Sie die Nutzlast ein:

```json
{
  "customer": {
    "labels": [
      {
        "key": "braze_vip_segment",
        "value": "optedIn"
      }
    ]
  }
}
```

### Schritt 2: Konfigurieren Sie den Trigger

1.  Navigieren Sie zum Tab **Zustellung** oder **Zeitplan des Eingangs**.
2.  Füllen Sie die folgenden Felder aus:
    * **Methode der Zustellung**: Handlungsorientiert.
    * **Triggern Sie**: Definieren Sie den entsprechenden Trigger (z.B. ein Nutzer:in gibt ein bestimmtes Segment in Braze ein).
    * **Start**: Aktivieren Sie die Kampagne.

## Fehlersuche

### Eingehende Ereignisse überprüfen
Wenn die Datentransformation aktiv ist, erscheinen die Daten in Braze als angepasstes Event. Überprüfen Sie dies, indem Sie eine Kampagne mit einem **Perform Custom Event** Trigger erstellen und überprüfen, ob das von Ihnen definierte Ereignis (z.B. `Loyalty Event Triggered`) verfügbar ist.

### Ausgehende Webhooks überprüfen
Überprüfen Sie das Protokoll der Nachrichtenaktivität in Braze, um sicherzustellen, dass der Webhook den Status `200 OK` zurückgegeben hat.
* **401 Fehler**: Überprüfen Sie Ihr Open Loyalty API Token.
* **404 Fehler**: Die Nutzer:innen ID in Braze existiert nicht in Open Loyalty.