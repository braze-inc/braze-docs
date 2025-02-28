---
nav_title: Recurly
article_title: Recurly
description: "Recurly ist die führende Plattform für die Verwaltung und Abrechnung von Abonnements für Direktvertriebsmarken, die ihre Abonnements und wiederkehrenden Einnahmen steigern möchten."
alias: /partners/recurly/
page_type: partner
search_tag: partner
---

# Recurly

> [Recurly](https://recurly.com/) ist eine Plattform zur Verwaltung und Abrechnung von Abonnements. Die integrierte Plattform von Recurly vereinfacht die Automatisierung des Abonnement-Lebenszyklus in großem Umfang, indem sie Teams in die Lage versetzt, das Abonnentenerlebnis zu verwalten und zu optimieren - vom Testen neuer Pläne, Angebote und Werbeaktionen bis hin zur Verwaltung von Zahlungsmethoden, Integrationen und Einblicken.

Die Integration zwischen Recurly und Braze vereinfacht den Austausch von Abonnementdaten mit Braze und ermöglicht eine gezielte Kommunikation mit Kunden.

- Nutzen Sie Recurly-Abonnement-Lebenszyklusereignisse (z.B. Abonnementverlängerungen, Pausen oder Kündigungen) in Braze, um personalisierte Kampagnen und Mitteilungen auszulösen.
- Nutzen Sie Recurly-Abonnementdaten (z. B. Abonnementpläne, Add-Ons oder Status), um Braze-Benutzer, -Segmente und -Canvases zu erstellen und zu verwalten, um kohortenspezifische Kampagnen und Mitteilungen durchzuführen.
- Senden Sie Recurly-Daten direkt an Braze, um zusätzliche Messaging-Anwendungen zu ermöglichen und die Entwicklungskosten zu senken.

Weitere Details zur Verwendung von Recurly mit Braze finden Sie in den [Recurly Docs](https://docs.recurly.com/docs/braze-integration).

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Recurly-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie einen Elite [Recurly-Abonnementplan](https://recurly.com/) mit aktiviertem Braze-Funktionsflag. Die Aktivierung von Kreditrechnungen in Ihrer Recurly-Plattform ist ebenfalls erforderlich.|
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. Da Recurly nur den Endpunkt `users.track` verwendet, empfehlen wir, einen Recurly-spezifischen Schlüssel nur mit dieser Berechtigung zu versehen. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |

## Integration

Bevor Sie beginnen, vergewissern Sie sich, dass Sie sowohl bei Braze als auch bei Recurly aktive Konten haben.

### Verbinden Sie Recurly mit Braze

1. Gehen Sie in Recurly zu **Integrationen** > **Braze**. Wenn Sie zum ersten Mal die Konfigurationsseite für die Braze-Integration in Recurly aufrufen, werden Sie aufgefordert, die beiden Systeme zu verbinden.

2. Legen Sie die folgenden Nachweise vor:

- **Instanz-URL:** Der Braze REST-Endpunkt der Instanz, für die Sie provisioniert werden.
- **API-Schlüssel (Bezeichner):** Der REST-API-Schlüssel von Braze, den Recurly beim Senden von Anfragen an Braze verwenden soll.

Denken Sie daran, die URL Ihrer Braze-Instanz zu kopieren. Ihre URL könnte zum Beispiel so aussehen: 

```
<https://dashboard-03.braze.com/dashboard/app_usage?locale=en>
```

{:start="3"}
3\. Nachdem Sie Ihre Anmeldedaten eingegeben haben, klicken Sie auf **Verbinden**.

## Mit dieser Integration

### Unterstützte Identifikatoren

Recurly verwendet die `account_code` eines Kontos als `external_id` in Braze. Aus diesem Grund sollte die `account_code` Ihrer Recurly-Konten mit der `external_id` Ihres Braze-Benutzers übereinstimmen.

### Angepasste Events

Für ein effektives Kundenengagement müssen Sie in Braze [benutzerdefinierte Ereignisse konfigurieren][2], um von Recurly ausgelöste Ereignisse zu empfangen. Stellen Sie sicher, dass Sie jedes Ereignis aus Recurly für eine vollständige Datenintegration einbeziehen. Diese Ereignisse können auch in [Braze Analytics][3] nachverfolgt werden. Einmal konfiguriert, können diese benutzerdefinierten Ereignisse verwendet werden, um Benutzer zu segmentieren oder Nachrichten zu personalisieren. 

| Braze Custom Event| Wiederkehrendes Ereignis |
| ----------- | ----------- |
| Recurly Neues Abonnement              | Wird ausgelöst, wenn ein Abonnement erstellt wird                            |
| Recurly Verlängertes Abonnement          | Wird ausgelöst, wenn ein Abonnement verlängert wird                                |
| Recurly Aktualisiertes Abonnement          | Ausgelöst, wenn sich die Attribute eines Abonnements ändern (Planänderung, Preisänderung oder Mengenänderung) |
| Recurly Abonnement gekündigt         | Ausgelöst, wenn ein Abonnement gekündigt wird                           |
| Recurly Reaktiviertes Abonnement      | Wird ausgelöst, wenn ein gekündigtes Abonnement reaktiviert wird               |
| Recurly Pausiertes Abonnement           | Wird ausgelöst, wenn ein Abonnement pausiert werden soll                   |
| Recurly Wiederaufnahme des Abonnements          | Wird ausgelöst, wenn ein Abonnement pausiert wird                              |
| Recurly Abonnement Abgelaufen          | Ausgelöst, wenn ein Abonnement abläuft                               |
| Recurly-Rechnung erstellt               | Ausgelöst, wenn eine Rechnung erstellt wird                                |
| Wiederkehrende erfolgreiche Zahlung            | Wird ausgelöst, wenn eine Rechnung erfolgreich eingezogen wurde                 |
| Wiederkehrende Erstattung ausgestellt                 | Ausgelöst, wenn eine Erstattung ausgegeben wird                                   |
| Recurly Fehlgeschlagene wiederkehrende Zahlung      | Ausgelöst, wenn eine Rechnung für eine Abonnementverlängerung fehlschlägt          |

### Batching und Ratenbegrenzung

Da Recurly den Endpunkt Braze `/users/track` verwendet, unterliegt die Integration den standardmäßigen Braze-Ratenbeschränkungen von 50.000 Anfragen pro Minute.

Recurly bündelt bestimmte Ereignisse im Lebenszyklus von Abonnements als einzelne API-Aufrufe an Braze, um die Anzahl der Aufrufe zu reduzieren.

- Die Erstellung mehrerer Abonnements zur gleichen Zeit wird gebündelt und als eine einzige Anfrage an Braze gesendet.
- Wenn mehrere Abonnements für ein Konto gleichzeitig verlängert werden, wird jede dieser Verlängerungen in einer einzigen Anfrage zusammengefasst.
- Lebenszyklusereignisse des gleichen Modells werden als eine einzige Anfrage gesendet. Ein Beispiel: Eine neu erstellte Rechnung mit einer Zahlung würde eine einzige API-Anfrage mit den beiden benutzerdefinierten Ereignissen `Recurly Invoice Created` und `Recurly Successful Payment` senden.

Stapel werden in Gruppen von bis zu 75 Ereignissen auf einmal an Braze gesendet. Wenn zum Beispiel 100 Abonnements auf einmal erstellt werden, würde Recurly zwei API-Anfragen an Braze stellen. Weitere Informationen finden Sie unter [Stapeln von User Track-Anfragen][4].

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[3]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics
[4]: {{site.baseurl}}/api/api_limits/#batch-user-track
