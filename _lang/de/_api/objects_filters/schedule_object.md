---
nav_title: "Zeitplan Objekt"
article_title: API Zeitplan Objekt
page_order: 12
page_type: reference
description: "In diesem referenzierten Artikel werden die verschiedenen Zeitpläne, die bei Braze verwendet werden, aufgelistet und erklärt."

---

# Objekt Zeitplan

> Die Parameter für die Endpunkte zur Erstellung von Kampagnen und Canvas-Zeitplänen spiegeln die des Sende-Endpunkts wider und fügen den Parameter `schedule` hinzu, mit dem Sie angeben können, wann die Nutzer:innen Ihrer Zielgruppe Ihre Nachricht erhalten sollen. Wenn Sie nur den Parameter `time` in das `schedule` Objekt aufnehmen, werden alle Nutzer:innen zu diesem Zeitpunkt mit Nachrichten versorgt.

Wenn Sie `in_local_time` auf `true` einstellen, erhalten Sie eine Fehlerantwort, wenn der Zeitparameter in allen Zeitzonen überschritten wurde. Wenn Sie `at_optimal_time` auf true setzen, erhalten Ihre Nutzer:innen die Nachricht an dem angegebenen Datum zur optimalen Zeit (unabhängig von der von Ihnen angegebenen Uhrzeit). Wenn Sie die Ortszeit oder die optimale Zeit senden, geben Sie im Wert des Zeitparameters keine Zeitzonenkennungen an (verwenden Sie z.B. `"2015-02-20T13:14:47"` anstelle von `"2015-02-20T13:14:47-05:00"`).

In der Antwort finden Sie eine `schedule_id`, die Sie speichern sollten, falls Sie die von Ihnen geplante Nachricht später stornieren oder aktualisieren müssen:

## Objektkörper

Fügen Sie dieses Objekt nach Bedarf ein, um Ihre Nachrichten zu planen.

```json
"schedule": {
  "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
  "in_local_time": (optional, bool),
  "at_optimal_time": (optional, bool),
}
```

## Zeitplan ID Antwort

Sie erhalten eine `schedule_id` für die geplante Nachricht, die Sie erstellt haben.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "schedule_id" : (required, string) identifier for the scheduled message that was created
}
```

Wenn Sie die API für Server-zu-Server-Aufrufe verwenden, müssen Sie möglicherweise die entsprechende API-URL zulassen, wenn sich diese hinter einer Firewall befinden.

Die Antworten des Endpunkts für die Nachrichtenplanung enthalten die `dispatch_id` der Nachricht, um auf den Versand der Nachricht zurück zu referenzieren. Die `dispatch_id` ist die ID des Nachrichtenversands (eindeutige ID für jede von Braze gesendete 'Übertragung').

