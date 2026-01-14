---
nav_title: Zustellung und Eingangstypen
article_title: Zustellung und Eingangstypen
page_order: 5
page_type: reference
description: "Dieser referenzierte Artikel beschreibt die Zustellungsarten für Kampagnen, Eingangsarten für Canvase und die zeitbasierten Features beim Einrichten einer Kampagne oder eines Canvas."
tool:
    - Campaigns
    - Canvas
---

# Zeitplan für Ihre Nachricht

> In Braze können Sie Ihre Nachrichten auf drei verschiedene Arten planen: geplant, aktionsbasiert und API-getriggert. Die Entscheidung, wie und wann Ihre Nachricht zugestellt wird, ist entscheidend für die Entwicklung einer wirksamen Nachricht. 

## Zustellung und Eingangstypen

Bei Kampagnen bestimmt die Art der Zustellung, wann Ihre Nutzer:innen Ihre Kampagne betreten und wann sie versendet wird. Da ein Canvas als eine fortlaufende Nutzer:innen-Reise aufgebaut ist, wird das Messaging-Konzept einer Zeitplanung als Eingangstyp bezeichnet.

| Zustellung<nobr> und Eingangstypen | Beschreibung                                                                                                                                                                                                                                                                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Geplant**       | Diese Art von Zeitplan ist für einmalige Nachrichten gedacht, die Sie sofort versenden möchten, wie z.B. Kampagnen zu einem aktuellen Ereignis. <br><br>Wenn Sie Testnachrichten senden, die nur an Sie selbst oder Ihr Team gerichtet sind, können Sie sie mit dieser Option sofort zustellen.                                                                                   |
| **Aktionsbasiert**    | Aktionsbasierte Zustellungen oder ereignisgesteuerte Kampagnen und Canvase sind sehr effektiv für transaktions- oder leistungsbezogene Nachrichten. Sie können sie so triggern, dass sie gesendet werden, nachdem ein Nutzer:innen ein bestimmtes Ereignis abgeschlossen hat, anstatt Ihre Nachricht an bestimmten Tagen zu senden.                                                                                           |
| **API-getriggert**   | Mit API-getriggerten Nachrichten können Sie im Braze-Dashboard Nachrichtenkopien, multivariate Tests und Wiederzulassungsregeln verwalten und gleichzeitig die Zustellung dieser Inhalte von Ihren eigenen Servern und Systemen triggern. <br><br>Die API-Anfrage zum Triggern der Nachricht kann auch zusätzliche Daten enthalten, die in Echtzeit in die Nachricht eingefügt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Zeitbasierte Optionen

{% tabs %}
{% tab campaign %}
Bei der geplanten Zustellung haben Sie die Wahl zwischen den folgenden Optionen:

- Senden, sobald die Kampagne gestartet ist
- Zu bestimmter Zeit senden
- [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
{% endtab %}

{% tab canvas %}
Bei der zeitgesteuerten Zustellung geben die Nutzer:innen einen Zeitplan ein, ähnlich wie Sie eine Kampagne planen würden. Sie können Nutzer:innen in ein Canvas einschreiben, sobald es gestartet wird oder zu einem bestimmten Zeitpunkt.

#### Bezeichnete Zeiten

Sie können wählen, ob Sie Ihr Canvas mit einer bestimmten Häufigkeit des Eingangs versenden möchten, z. B. nur einmal, täglich, wöchentlich oder monatlich. Für Canvase mit wiederkehrender Zustellung nach Zeitplan können Sie die Wiederholung so einstellen, dass Nutzer:innen das Canvas bis zu 30 Mal betreten können.
{% endtab %}
{% endtabs %}

### Aktionsbasierte Optionen

{% tabs %}
{% tab campaign %}
Bei der aktionsbasierten Zustellung werden Kampagnen an Nutzer:innen gesendet, die eine bestimmte Aktion ausführen. Nachdem diese Aktion erfolgt ist, können Sie entscheiden, wann die Kampagne gesendet werden soll: sofort, nach einer bestimmten Zeit, zu einem bestimmten Zeitpunkt oder zu einem Zeitpunkt in der Zukunft.
{% endtab %}

{% tab canvas %}
Die aktionsbasierten Optionen legen fest, welche Aktionen (oder Trigger) ein Nutzer:innen ausführen muss, um ein Canvas zu betreten, und zu welchem Zeitpunkt er mit dem Betreten beginnen darf. Sie könnten Ihre Nutzer:innen zum Beispiel durch die folgenden Aktionen bewerten:

- Öffnen Ihrer App
- Hinzufügen einer E-Mail-Adresse
- Einen Standort eingeben

#### Eingang Fenster

Das Eingangsfenster Ihres Canvas bestimmt, welche Nutzer:innen das Canvas zur festgelegten Startzeit (und optionalen Endzeit) betreten können. Ähnlich wie bei aktionsbasierten Kampagnen können Sie die Nutzer:innen in ihrer Ortszeit erfassen.
{% endtab %}
{% endtabs %}

### API triggern Optionen

{% tabs %}
{% tab campaign %}
Wenn Sie API-getriggert als Option für die Zustellung auswählen, erhalten Sie eine Kampagnen ID, um die Kampagne zu identifizieren, die mit dem [Endpunkt`/campaigns/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#prerequisites) gesendet werden soll.
{% endtab %}

{% tab canvas %}
Wenn Sie als Eingangstyp "API-getriggert" auswählen, erhalten Sie eine Canvas ID, mit der Sie die Kampagne identifizieren können, die Sie mit dem [Endpunkt`/canvas/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) einsenden möchten.
{% endtab %}
{% endtabs %}
