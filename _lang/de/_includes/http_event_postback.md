Alle Transaktions-E-Mails werden durch Ereignisstatus-Postbacks ergänzt, die als HTTP-Anfrage an die von Ihnen angegebene URL zurückgeschickt werden. So können Sie den Status der Nachricht in Realtime auswerten und Maßnahmen ergreifen, um den Nutzer:innen auf einem anderen Kanal zu erreichen, wenn die Nachricht nicht zugestellt wurde, oder auf ein internes System zurückgreifen, wenn Braze eine Latenzzeit hat.

Sie können diese Updates über eindeutige Bezeichner mit einzelnen Nachrichten verknüpfen:

- `dispatch_id`: Eine eindeutige ID, die Braze automatisch für jede Nachricht generiert.
- `external_send_id`: Ein angepasster Bezeichner, den Sie angeben, z.B. eine Bestellnummer, um Updates mit Ihren internen Systemen abzugleichen.

Wenn Sie zum Beispiel `external_send_id einschließen: 1234` in der Anfrage beim Versenden einer E-Mail zur Auftragsbestätigung enthalten, werden alle nachfolgenden Event-Postbacks für diese E-Mail - wie `Sent` oder `Delivered -` `external\_send\_id enthalten: 1234`. Damit können Sie bestätigen, ob der Kund:in für die Bestellung #1234 seine E-Mail zur Bestellbestätigung erhalten hat.

### Einrichten von Postbacks

In Ihrem Braze-Dashboard:

1. Gehen Sie zu **Einstellungen** > **E-Mail-Voreinstellungen**.
2. Geben Sie unter **Transaktionsereignis-Status-Postback** die URL ein, an die Braze Status-Updates für Ihre Transaktions-E-Mails senden soll.
3. Testen Sie das Postback.

\![\]({% image\_buster /assets/img/transactional\_webhook\_url.png %})

### Körper der Rückmeldung

```json { "dispatch_id": (String, eine zufällig erzeugte eindeutige ID der Instanz dieses Sendens), "status": (String, Aktueller Status der Nachricht aus der folgenden Nachrichtenstatustabelle, "metadata" : (Objekt, zusätzliche Informationen zur Ausführung eines Ereignisses) { "external_send_id" : (String, Wenn zum Zeitpunkt der Anfrage angegeben, übergibt Braze Ihren internen Bezeichner für diese Sendung für alle Postbacks), "campaign_api_id" : (String, API-Bezeichner dieser transaktionalen Kampagne), "received_at": (ISO 8601 DateTime String, Zeitstempel des Eingangs der Anfrage bei Braze, nur bei Ereignissen mit dem Status "gesendet" enthalten), "enqueued\_at": (ISO 8601 DateTime String, Zeitstempel des Zeitpunkts, zu dem die Anfrage von Braze in die Warteschlange gestellt wurde, nur für Ereignisse mit dem Status "gesendet"), "executed\_at": (ISO 8601 DateTime String, Zeitstempel des Zeitpunkts, zu dem die Anfrage von Braze verarbeitet wurde, nur bei Ereignissen mit dem Status "gesendet" enthalten), "sent\_at": (ISO 8601 DateTime String, Zeitstempel des Zeitpunkts, zu dem die Anfrage von Braze an den ESP gesendet wurde, nur für Ereignisse mit dem Status "gesendet" enthalten), "processed\_at" : (ISO 8601 DateTime String, Zeitstempel, zu dem das Ereignis vom ESP verarbeitet wurde, nur für Ereignisse mit dem Status "verarbeitet"), "delivered\_at" : (ISO 8601 DateTime String, Zeitstempel, zu dem das Ereignis dem Posteingang des Nutzers zugestellt wurde, nur bei Ereignissen mit dem Status "verarbeitet" enthalten), "bounced\_at" : (ISO 8601 DateTime String, Zeitstempel, an dem das Ereignis vom Posteingang des Nutzers:innen abgelehnt wurde, nur bei Ereignissen mit dem Status "abgelehnt" enthalten), "aborted\_at" : (ISO 8601 DateTime String, Zeitstempel, an dem das Ereignis von Braze abgebrochen wurde, nur bei Ereignissen mit dem Status "abgebrochen" enthalten), "reason" : (String, Der Grund, warum Braze oder der Posteingang-Anbieter diese Nachricht an den Nutzer:in nicht verarbeiten konnte, nur bei Ereignissen mit dem Status "abgebrochen" oder "geprellt" enthalten), } } ```

#### Status der Nachrichten

| Status | Beschreibung | | ------------ | ----------- | | `gesendet` | Nachricht erfolgreich an einen Partner für den E-Mail-Versand von Braze gesendet | | `verarbeitet` | Der Partner für den E-Mail-Versand hat die Nachricht erfolgreich empfangen und für den Versand an den Posteingang des Nutzers vorbereitet | | `abgebrochen` | Braze konnte die Nachricht nicht erfolgreich versenden, da der Nutzer:innen keine E-Mail-Adresse hat oder die Liquid-Abbruchlogik im Nachrichtentext aufgerufen wurde. Alle abgebrochenen Ereignisse enthalten ein `Grundfeld` im Metadatenobjekt, das angibt, warum die Nachricht abgebrochen wurde | `|delivered|` Nachricht wurde vom Anbieter des E-Mail Posteingangs des Nutzers zugestellt | `|bounced|` Nachricht wurde vom Anbieter des E-Mail Posteingangs des Nutzers abgelehnt. Alle Bounce-Ereignisse enthalten im Metadaten-Objekt ein `Grundfeld`, das den vom Posteingang-Anbieter bereitgestellten Fehlercode widerspiegelt | {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Beispiel Postback
\`\`\`json

// Gesendetes Ereignis { "dispatch\_id": "acf471119f7449d579e8089032003ded", "status": "sent", "metadata": { "received\_at": "2020-08-31T18:58:41.000+00:00", "enqueued\_at": "2020-08-31T18:58:41.000+00:00", "executed\_at": "2020-08-31T18:58:41.000+00:00", "sent\_at": "2020-08-31T18:58:42.000+00:00", "campaign\_api\_id": "417220e4-5a2a-b634-7f7d-9ec891532368", "external\_send\_id" : "34a2ceb3cf6184132f3d816e9984269a" } }

// Verarbeitetes Ereignis { "dispatch\_id": "acf471119f7449d579e8089032003ded", "status": "processed", "metadata": { "processed\_at": "2020-08-31T18:58:42.000+00:00", "campaign\_api\_id": "417220e4-5a2a-b634-7f7d-9ec891532368", "external\_send\_id" : "34a2ceb3cf6184132f3d816e9984269a" } }

// Abgebrochen { "dispatch\_id": "acf471119f7449d579e8089032003ded", "status": "aborted", "metadata": { "Grund": "Nutzer:innen nicht per E-Mail erreichbar", "aborted\_at": "2020-08-31T19:04:51.000+00:00", "campaign\_api\_id": "417220e4-5a2a-b634-7f7d-9ec891532368", "external\_send\_id" : "34a2ceb3cf6184132f3d816e9984269a" } }

// Zugestelltes Ereignis { "dispatch\_id": "acf471119f7449d579e8089032003ded", "status": "delivered", "metadata": { "delivered\_at": "2020-08-31T18:27:32.000+00:00", "campaign\_api\_id": "417220e4-5a2a-b634-7f7d-9ec891532368", "external\_send\_id" : "34a2ceb3cf6184132f3d816e9984269a" } }

// Geprelltes Ereignis { "dispatch\_id": "acf471119f7449d579e8089032003ded", "status": "geprellt", "metadata": { "bounced\_at": "2020-08-31T18:58:43.000+00:00", "reason": "550 5.1.1 Das E-Mail-Konto, das Sie zu erreichen versucht haben, existiert nicht", "campaign\_api\_id": "417220e4-5a2a-b634-7f7d-9ec891532368", "external\_send\_id" : "34a2ceb3cf6184132f3d816e9984269a" } }

\`\`\`

