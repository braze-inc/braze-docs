---
nav_title: Recurly
article_title: Recurly
description: "Recurly ist die führende Plattform für das Abo-Management und die Rechnungsstellung für Marken im Direktvertrieb an Verbraucher:in, die ihre Abos und wiederkehrenden Einnahmen steigern möchten."
alias: /partners/recurly/
page_type: partner
search_tag: partner
---

# Recurly

> [Recurly](https://recurly.com/) ist eine Plattform für das Abo-Management und die Rechnungsstellung. Die integrierte Plattform von Recurly vereinfacht die Automatisierung des Abo-Lebenszyklus in großem Umfang, indem sie Teams in die Lage versetzt, das Abo-Erlebnis zu verwalten und zu optimieren - vom Testen neuer Pläne, Angebote und Aktionen bis hin zur Verwaltung von Zahlungsarten, Integrationen und Insights.

_Diese Integration wird von Recurly gepflegt._

## Über die Integration

Die Integration zwischen Recurly und Braze vereinfacht den Austausch von Abo-Daten mit Braze und ermöglicht so eine gezielte Kommunikation mit den Kund:innen.

- Nutzen Sie die Recurly-Lebenszyklusereignisse (z. B. Abonnementverlängerungen, Pausen oder Kündigungen) in Braze, um personalisierte Kampagnen und Mitteilungen zu triggern.
- Nutzen Sie Recurly-Abonnementdaten (z.B. Abo-Pläne, Add-Ons oder Status), um Braze Nutzer:innen, Segmente und Canvase zu erstellen und zu verwalten, um kohortenspezifische Kampagnen und Mitteilungen durchzuführen.
- Senden Sie Recurly-Daten direkt an Braze, um zusätzliche Messaging-Anwendungsfälle zu ermöglichen und die Entwicklungskosten zu senken.

Weitere Einzelheiten zur Verwendung von Recurly mit Braze finden Sie in den [Recurly Docs](https://docs.recurly.com/docs/braze-integration).

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Recurly-Konto | Sie benötigen ein Elite [Recurly](https://recurly.com/) Abo mit aktiviertem Braze Feature-Flag, um die Vorteile dieser Partnerschaft zu nutzen. Die Aktivierung von Kreditrechnungen in Ihrer Recurly-Plattform ist ebenfalls erforderlich.|
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. Da Recurly nur den Endpunkt `users.track` verwendet, empfehlen wir, einen Recurly-spezifischen Schlüssel nur mit dieser Berechtigung zu versehen. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |

## Integration

Bevor Sie beginnen, vergewissern Sie sich, dass Sie sowohl bei Braze als auch bei Recurly ein aktives Konto haben.

### Verbinden Sie Recurly mit Braze

1. Gehen Sie in Recurly zu **Integrationen** > **Braze**. Wenn Sie zum ersten Mal zur Konfigurationsseite für die Integration von Braze in Recurly navigieren, werden Sie von der Schnittstelle aufgefordert, die beiden Systeme miteinander zu verbinden.

2. Geben Sie die folgenden Zugangsdaten an:

- **Instanz-URL:** Der Braze REST-Endpunkt der Instanz, für die Sie bereitgestellt werden.
- **API-Schlüssel (Bezeichner):** Der REST API-Schlüssel von Braze, den Recurly beim Senden von Anfragen an Braze verwenden soll.

Denken Sie daran, die URL Ihrer Braze-Instanz zu kopieren. Ihre URL könnte zum Beispiel so aussehen: 

```
<https://dashboard-03.braze.com/dashboard/app_usage?locale=en>
```

{:start="3"}
3\. Nachdem Sie Ihre Zugangsdaten eingegeben haben, klicken Sie auf **Verbinden**.

## Verwendung dieser Integration

### Unterstützte Bezeichner

Recurly verwendet die `account_code` eines Kontos als `external_id` in Braze. Aus diesem Grund sollte die `account_code` Ihrer Recurly-Konten mit der `external_id` Ihrer Braze-Nutzer:innen übereinstimmen.

### Angepasste Events

Für ein effektives Customer-Engagement müssen Sie in Braze [angepasste Events konfigurieren]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/), um von Recurly getriggerte Events zu empfangen. Stellen Sie sicher, dass Sie jedes Ereignis aus Recurly für eine gründliche Datenintegration einbeziehen. Diese Ereignisse können auch in [Braze Analytics]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics) getrackt werden. Einmal konfiguriert, können diese angepassten Events zur Segmentierung von Nutzer:innen oder zur Personalisierung von Nachrichten verwendet werden. 

| Braze Angepasstes Event| Wiederkehrendes Ereignis |
| ----------- | ----------- |
| Recurly Neues Abo              | Ausgelöst, wenn ein Abo erstellt wird                            |
| Recurly Verlängertes Abo          | Ausgelöst, wenn ein Abo verlängert wird                                |
| Recurly Update Abo          | Wird ausgelöst, wenn sich die Attribute eines Abos ändern (Planänderung, Preisänderung oder Mengenänderung) |
| Recurly Abo gekündigt         | Ausgelöst, wenn ein Abo gekündigt wird                           |
| Recurly Reaktiviertes Abo      | Wird ausgelöst, wenn ein gekündigtes Abo reaktiviert wird               |
| Recurly Pausiertes Abo           | Wird ausgelöst, wenn ein Abo pausiert werden soll                   |
| Recurly hat das Abo wieder aufgenommen          | Wird ausgelöst, wenn ein Abo nicht mehr pausiert                              |
| Recurly Abo Abgelaufen          | Ausgelöst, wenn ein Abo ausläuft                               |
| Recurly-Rechnung erstellt               | Ausgelöst, wenn eine Rechnung erstellt wird                                |
| Wiederkehrende erfolgreiche Zahlung            | Wird ausgelöst, wenn eine Rechnung erfolgreich eingezogen wurde                 |
| Wiederkehrende Erstattung ausgestellt                 | Ausgelöst, wenn eine Erstattung ausgegeben wird                                   |
| Recurly Fehlgeschlagene wiederkehrende Zahlung      | Wird ausgelöst, wenn eine Rechnung für eine Abo-Verlängerung fehlschlägt          |

### Batching und Rate-Limiting

Da Recurly den Endpunkt Braze `/users/track` verwendet, unterliegt die Integration den standardmäßigen Rate-Limits von Braze von 50.000 Anfragen pro Minute.

Recurly bündelt bestimmte Abo-Lebenszyklusereignisse als einzelne API-Aufrufe an Braze, um die Anzahl der Aufrufe zu reduzieren.

- Die Erstellung mehrerer Abos zur gleichen Zeit wird gebündelt und in einer einzigen Anfrage an Braze gesendet.
- Wenn für ein Konto mehrere Abos gleichzeitig verlängert werden, wird jede dieser Verlängerungen in einer einzigen Anfrage zusammengefasst.
- Lebenszyklusereignisse des gleichen Modells werden in einer einzigen Anfrage gesendet. Ein Beispiel: Eine neu erstellte Rechnung mit einer Zahlung würde eine einzige API-Anfrage mit den beiden angepassten Events `Recurly Invoice Created` und `Recurly Successful Payment` senden.

Stapel werden in Gruppen von bis zu 75 Ereignissen auf einmal an Braze gesendet. Wenn zum Beispiel 100 Abos auf einmal erstellt werden, würde Recurly zwei API-Anfragen an Braze stellen. Weitere Informationen finden Sie unter [Stapeln von Nutzer:innen Tracking-Anfragen]({{site.baseurl}}/api/api_limits/#batch-user-track).


