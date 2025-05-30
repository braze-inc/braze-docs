Alle Transaktions-E-Mails werden durch Ereignisstatus-Postbacks ergänzt, die als HTTP-Anfrage an die von Ihnen angegebene URL zurückgeschickt werden. So können Sie den Status der Nachricht in Realtime auswerten und Maßnahmen ergreifen, um den Nutzer:innen auf einem anderen Kanal zu erreichen, wenn die Nachricht nicht zugestellt wurde, oder auf ein internes System zurückgreifen, wenn Braze eine Latenzzeit hat.

Sie können diese Updates über eindeutige Bezeichner mit einzelnen Nachrichten verknüpfen:

- `dispatch_id`: Eine eindeutige ID, die Braze automatisch für jede Nachricht generiert.
- `external_send_id`: Ein angepasster Bezeichner, den Sie angeben, z.B. eine Bestellnummer, um Updates mit Ihren internen Systemen abzugleichen.

Wenn Sie beispielsweise `external_send_id: 1234` in die Anfrage beim Versenden einer E-Mail zur Auftragsbestätigung aufnehmen, werden alle nachfolgenden Ereignis-Postbacks für diese E-Mail - wie `Sent` oder `Delivered`- `external_send_id: 1234` enthalten. Damit können Sie bestätigen, ob der Kund:in für die Bestellung #1234 seine E-Mail zur Bestellbestätigung erhalten hat.

### Einrichten von Postbacks

In Ihrem Braze-Dashboard:

1. Gehen Sie zu **Einstellungen** > **E-Mail-Voreinstellungen**.
2. Geben Sie unter **Transaktionsereignis-Status-Postback** die URL ein, an die Braze Status-Updates für Ihre Transaktions-E-Mails senden soll.
3. Testen Sie das Postback.

![]({% image_buster /assets/img/transactional_webhook_url.png %})

### Körper der Rückmeldung

```json
{
  "dispatch_id": (string, a randomly-generated unique ID of the instance of this send),
  "status": (string, Current status of message from the following message status table,
  "metadata" : (object, additional information relating to the execution of an event)
   {
     "external_send_id" : (string, If provided at the time of the request, Braze will pass your internal identifier for this send for all postbacks),
     "campaign_api_id" : (string, API identifier of this transactional campaign),
     "received_at": (ISO 8601 DateTime string, Timestamp of when the request was received by Braze, only included for events with "sent" status),
     "enqueued_at": (ISO 8601 DateTime string, Timestamp of when the request was enqueued by Braze, only included for events with "sent" status),
     "executed_at": (ISO 8601 DateTime string, Timestamp of when the request was processed by Braze, only included for events with "sent" status),
     "sent_at": (ISO 8601 DateTime string, Timestamp of when the request was sent to the ESP by Braze, only included for events with "sent" status),
     "processed_at" : (ISO 8601 DateTime string, Timestamp the event was processed by the ESP, only included for events with "processed" status),
     "delivered_at" : (ISO 8601 DateTime string, Timestamp the event was delivered to the user's inbox provider, only included for events with "processed" status),
     "bounced_at" : (ISO 8601 DateTime string, Timestamp the event was bounced by the user's inbox provider, only included for events with "bounced" status),
     "aborted_at" : (ISO 8601 DateTime string, Timestamp the event was Aborted by Braze, only included for events with "aborted" status),
     "reason" : (string, The reason Braze or the Inbox provider was unable to process this message to the user, only included for events with "aborted" or "bounced" status),
   }
}
```

#### Status der Nachrichten

|  Status | Beschreibung |
| ------------ | ----------- |
| `sent` | Nachricht erfolgreich an einen Braze E-Mail sendenden Partner versendet |
| `processed` | Der Partner für das Versenden von E-Mails hat die Nachricht erfolgreich empfangen und für den Versand an den Posteingang des Nutzers:innen vorbereitet. |
| `aborted` | Braze konnte die Nachricht nicht erfolgreich versenden, da der Nutzer:innen keine E-Mail Adresse hat oder die Liquid Abbruchlogik im Nachrichtentext aufgerufen wurde. Alle abgebrochenen Ereignisse enthalten ein `reason` Feld innerhalb des Metadatenobjekts, das angibt, warum die Nachricht abgebrochen wurde. |
|`delivered`| Nachricht wurde vom Anbieter des Posteingangs des Nutzers akzeptiert |
|`bounced`| Nachricht wurde vom Anbieter des Posteingangs des Nutzers abgelehnt. Alle Bounce-Ereignisse enthalten ein Feld `reason` im Metadaten-Objekt, das den vom Posteingang-Anbieter bereitgestellten Fehlercode wiedergibt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Beispiel Postback
```json

// Sent Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "sent",
    "metadata": {
      "received_at": "2020-08-31T18:58:41.000+00:00",
      "enqueued_at": "2020-08-31T18:58:41.000+00:00",
      "executed_at": "2020-08-31T18:58:41.000+00:00",
      "sent_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Processed Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "processed",
    "metadata": {
      "processed_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Aborted
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "aborted",
    "metadata": {
      "reason": "User not emailable",
      "aborted_at": "2020-08-31T19:04:51.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Delivered Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "delivered",
    "metadata": {
      "delivered_at": "2020-08-31T18:27:32.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Bounced Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "bounced",
    "metadata": {
      "bounced_at": "2020-08-31T18:58:43.000+00:00",
      "reason": "550 5.1.1 The email account that you tried to reach does not exist",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

```

