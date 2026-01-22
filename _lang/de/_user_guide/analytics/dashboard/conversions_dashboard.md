---
nav_title: Konversions-Dashboard
article_title: Konversions-Dashboard
alias: "/conversions_dashboard_v2/"
description: "Mit dem Dashboard für Konversionen können Sie Konversionen über Kampagnen, Canvase und Kanäle hinweg analysieren und dabei verschiedene Attributionsmethoden verwenden."
page_order: 3
page_type: reference
tool: 
  - Reports
---

# Dashboard für Konversionen

> Das Konversions-Dashboard analysiert Konversionen über Kampagnen, Canvase und Kanäle hinweg, indem es verschiedene [Attributionsmethoden](#attribution-methods) verwendet. Wenn Sie Ihre Konversionen messen, können Sie den Zeitrahmen, das Konversions-Event und das Konversionsfenster festlegen.

## Einrichten Ihres Berichts

So richten Sie Ihren Konversions Dashboard-Bericht ein:

1. Gehen Sie zu **Analytics** > Conversions.
2. Wählen Sie einen **Datumsbereich** für Ihren Bericht aus, bis zu einem Zeitfenster von 90 Tagen.
3. Wählen Sie die zu analysierenden Kampagnen oder Canvase (oder beides) aus. 
   - (optional) Filtern Sie Kampagnen und Canvase, indem Sie einen Tag auswählen.  
4. Wählen Sie **den/die Kanal/Kanäle** aus, den/die Sie für Ihre Nachrichten analysieren möchten.
5. Wählen Sie eine **Aufschlüsselung nach** Ebene aus, um verschiedene Dimensionen von Daten anzuzeigen, z. B. nach Variante, Canvas-Schritt, Land oder Sprache.
6. (Optional) Wenn Sie Konversionen eines Ereignisses berechnen möchten, das nicht als Konversions-Event in der Kampagne oder im Canvas eingerichtet wurde, aktivieren Sie [Angepasste Events verwenden](#using-custom-events).
7. Wählen Sie eine [Attribution-Methode](#attribution-methods) aus, mit der die ausgewählten Nachrichten analysiert werden sollen.

{% alert note %}
Wenn Sie Konversionen für mehrere Kanäle analysieren, wird Ihre **Attribution-Methode** standardmäßig auf **Last-Touch-Attribution** eingestellt.
{% endalert %}

{:start="8"}
8\. Wählen Sie **Erstellen**, um den Bericht auszuführen.

Nachdem die Seite geladen wurde, wählen Sie ein **Konversions-Event**, um den Bericht nach Konversionsdaten zu filtern. Die verfügbare Auswahl umfasst die Events, die auf den Canvase und Kampagnen vorkonfiguriert wurden. Wenn Sie beim Einrichten Ihres Berichts (Schritt 6) ein angepasstes Ereignis ausgewählt haben, ist diese Option nicht verfügbar.

### Angepasste Events verwenden

Damit die Metriken für angepasste Events auf dem Dashboard für Konversionen angezeigt werden, müssen ein Konversions-Event und ein Canvas-Eingang-Event in dem auf der Seite angegebenen Datumsbereich liegen. 

Um die Konversionen eines Events zu berechnen, das nicht als Konversion-Event in der Kampagne oder im Canvas eingerichtet wurde, wählen Sie ein bestimmtes angepasstes Event aus, das als Konversion-Event verwendet werden soll. 

1. Wenn Sie Ihren Bericht einrichten, aktivieren Sie die Option **Angepasste Events verwenden**.
2. Wählen Sie ein angepasstes Event aus, das als Konversion-Event verwendet werden soll.
3. Wählen Sie das Konversionsfenster aus, in dem das Event stattgefunden haben sollte, um als Konversion gezählt zu werden.

{% alert note %}
Wenn Sie ein angepasstes Event auswählen, wird das Dropdown-Menü **Konversions-Event** auf der Seite nicht angezeigt und Sie müssen den Bericht erneut ausführen, um die Konversionen für verschiedene angepasste Events anzuzeigen.
{% endalert %}

## Grundlegendes zu Ihrem Bericht

Ihr Bericht ist in drei Abschnitte unterteilt:

- [Konversionsdetails](#conversion-details)
- [Konversions-Funnel](#conversion-funnel)
- [Konversionen im Zeitverlauf](#conversions-over-time)

### Konversionsdetails

Die Tabelle mit den Konversionsdetails zeigt immer eine Spalte für *Empfänger:innen* und eine weitere für *Konversionen* (Rate und Summe). Die beiden verbleibenden Tabellenspalten, die angezeigt werden, hängen von den Optionen ab, die Sie beim Einrichten Ihres Berichts ausgewählt haben. 

![Tabelle mit Konversionsdetails, die Berührungen als Attributionsmethode für die Spalten drei und vier anzeigt.]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="border:none"}

Die folgende Tabelle beschreibt mögliche Metriken.

| Angezeigte Metrik | Beschreibung |
| --- | --- |
| Empfänger:innen | Die Anzahl der Nutzer:innen, die eine Nachricht über den ausgewählten Kanal innerhalb des Datumsbereichs des Berichts erhalten haben |
| Konversionsrate (Empfänger:innen) | Berechnet als: (Anzahl der Konversionen) / (Anzahl der Empfänger:innen) |
| Attributionsmethode | Definiert durch die [Attribution-Methode](#attribution-methods), die Sie beim Einrichten des Berichts ausgewählt haben. Bei der Last Touch Attribution oder wenn mehrere Kanäle ausgewählt sind, erscheint dies als [Berührungen](#terms-to-know). |
| Konversionsrate (Attributionsmethode) | Definiert durch die [Attribution-Methode](#attribution-methods), die Sie beim Einrichten des Berichts ausgewählt haben. Wenn Sie mehrere Kanäle ausgewählt haben, wird standardmäßig die Letztkontakt-Attribution verwendet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Wenn Sie beim [Einrichten Ihres Berichts](#setting-up-your-report) (Schritt 5) Details auf der Aufschlüsselungsebene für Kampagnen oder Canvase ausgewählt haben, können Sie auf <i class="fas fa-angle-down"></i> klicken, um die Tabelle zu erweitern.

### Konversions-Funnel

Dieses Balkendiagramm zeigt die absoluten Zahlen für jedes [Engagement-Ereignis]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) auf der Grundlage des ausgewählten Kanals. Die Anzahl der Konversionen wird entsprechend der ausgewählten Attribution-Methode definiert.

Standardmäßig werden alle ausgewählten Kampagnen und Canvase angezeigt. Um die Auswahl einer Kampagne oder eines Canvas aufzuheben, wählen Sie den Namen der Kampagne oder des Canvas aus, den Sie ausschließen möchten. Für weitere Details zum Engagement-Ereignis können Sie mit dem Mauszeiger über die einzelnen Balken fahren.

Wählen Sie eine Download-Option aus, um die Zeitreihendaten herunterzuladen: PNG, JPEG, PDF, SVG oder CSV.

{% alert note %}
Dieses Diagramm zeigt jeweils nur Daten für einen einzelnen Kanal an. Verwenden Sie das Dropdown-Menü **Kanal** auf dem Chart, um einen einzelnen Kanal auszuwählen.
{% endalert %}

![Funnel-Balkendiagramm für Konversionen für zwei Kampagnen, die ähnliche Ergebnisse für zugestellte E-Mails, geöffnete E-Mails, angeklickte E-Mails und Konversionen zeigen.]({% image_buster /assets/img_archive/conversions2_funnel.png %})

### Konversionen im Zeitverlauf

Dieses Zeitreihendiagramm enthält eine Darstellung der Konversionen pro Kampagne oder Canvas im Laufe der Zeit. Standardmäßig werden alle ausgewählten Kampagnen und Canvase angezeigt. Um die Auswahl einer Kampagne oder eines Canvas aufzuheben, klicken Sie auf den Namen der Kampagne oder des Canvas, die Sie ausschließen möchten.

Um die Zeitreihendaten herunterzuladen, wählen Sie <i class="fas fa-bars"></i> und dann die gewünschte Download-Option aus. Die verfügbaren Optionen sind PNG, JPEG, PDF, SVG oder CSV.

![Zeitreihengrafik der Konversionen für zwei E-Mail Kampagnen, die die Konversionen nach Tagen anzeigt.]({% image_buster /assets/img_archive/conversions2_over_time.png %})

### Attributionsmethoden

| Attributionsmethode | Definition | Berechnung der Rate | Kanalspezifische Optionen |
| --- | --- | --- | --- |
| Nach Empfang | Gesamtzahl der Konversionen, die nach Erhalt der Nachricht stattgefunden haben | Berechnet als (eindeutige empfangene Konversionen) / (eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Nach E-Mail-Zustellung</li><li>Nach SMS-Zustellung</li></ul>{:/} |
| Nach Sendung | Gesamtzahl der Konversionen, die nach dem Senden der Nachricht stattgefunden haben | Berechnet als (Eindeutige Sendekonversionen) / (Eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Nach Push-Sendung</li><li>Nach Content-Card-Sendung</li><li>Nach SMS-Sendung</li></ul>{:/} |
| Nach Öffnung | Gesamtzahl der Konversionen, die nach dem Öffnen der Nachricht stattgefunden haben | Berechnet als (Eindeutige Öffnungen Konversionen) / (Eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Nach E-Mail-Öffnung</li><li>Nach Push-Öffnung</li></ul>{:/} |
| Nach Klick | Gesamtzahl der Konversionen, die aufgetreten sind Nachricht Klick | Berechnet als (Eindeutige Klick-Konversionen) / (Eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Nach E-Mail-Klick</li><li>Nach Content-Card-Klick</li><li>Nach IAM-Klick</li></ul>{:/} |
| Nach Impression | Gesamtzahl der Konversionen, die nach einer Impression stattgefunden haben | Berechnet als (Eindeutige Impressionen Konversionen) / (Eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Nach IAM-Impression</li><li>Nach Content-Card-Impression</li></ul>{:/} |
| Nach Letztkontakt | Konversionen, bei denen die zuletzt angeklickte oder berührte Nachricht während des Konversionsfensters berücksichtigt wird. | Berechnet als (Anzahl der Berührungen) / (Eindeutige Empfänger:innen) | Die Letztkontakt-Attribution wird automatisch ausgewählt, wenn dem Bericht mehrere Kanäle hinzugefügt werden.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Begriffe, die Sie kennen sollten

| Begriff | Definition |
| --- | --- |
| Berühren | Eine physische Interaktion oder ein Touchpoint mit einer Nachricht.<br><br>Zu den Berührungen können gehören:<br>{::nomarkdown}<ul><li>E-Mail-Klick</li><li>Push-Öffnung</li><li>Contend-Card-Klick</li><li>In-App-Nachricht-Klick</li><li>SMS Klick</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
