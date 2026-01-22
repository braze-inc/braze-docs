---
nav_title: „Zum Kalender hinzufügen“-Links
article_title: Links zum Kalender hinzufügen
page_order: 1
page_type: tutorial
description: "Dieser Artikel beschreibt, wie Sie einen Link zum Hinzufügen zum Kalender in Ihre E-Mail-Kampagnen einfügen."
channel: email

---

# „Zum Kalender hinzufügen“-Links

> Wenn Sie für ein Event, einen Verkauf oder einen Termin werben, können Sie den Nutzer:innen helfen, das Event ganz einfach in ihrem Kalender zu speichern, indem Sie einen „Zum Kalender hinzufügen“-Link zu Ihren E-Mails hinzufügen.

Entwerfen Sie dazu Ihre E-Mail und legen Sie fest, wo Sie Ihre Links platzieren möchten. Fügen Sie dann zwei Optionen hinzu: eine für Google Kalender und eine für andere Kalender (wie iCal oder Outlook). Zum Beispiel "Zum Google Kalender hinzufügen" und "Zu iCal oder Outlook hinzufügen".

![Link-Dialog beim Hinzufügen eines Links im Dashboard. Die Registerkarte „Link-Info“ ist ausgewählt und der Text ist auf „Zum Google-Kalender hinzufügen“ eingestellt.]({% image_buster /assets/img_archive/calendar_1.png %}){: style="max-width:50%"}

## URL-Format

Fügen Sie die folgende URL zu Ihren Links hinzu und ersetzen Sie die Platzhalter. Der einzige Unterschied zwischen diesen beiden URLs ist, dass Google Kalender einen zusätzlichen Parameter benötigt: `&format=gcal`.

{% tabs %}
{% tab Google Calendar %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal or Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

Ersetzen Sie Folgendes:

- `EVENT_SUBJECT`: Titel des Events
- `EVENT_LOCATION`: Ort des Events
- `START_TIME`: Die Startzeit des Events im ISO 8601-Format (JJJJ-MM-TTTHH:MM:SSZ) als UTC
- `END_TIME`: Die Endzeit des Events im ISO 8601-Format (JJJJ-MM-TTTHH:MM:SSZ) als UTC
- `EVENT_DESCRIPTION`: Beschreibung des Events

Ersetzen Sie alle Leerzeichen durch den HTML-Escape-Code `%20`. Zum Beispiel wäre ein Betreff von „Meet Braze“ „Meet%20Braze“.

Hier ist ein Beispiel für eine "Zum Google Kalender hinzufügen"-URL:

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### Zusätzliche Parameter

Die folgenden Parameter sind optional und können verwendet werden, um zusätzliche Aspekte eines Events zu definieren.

- **Organisatorname:** `&organizer=name`
- **Fügen Sie die URL für das Event an:** `&attach=http://www.example.com/`
- **Dauer:** `duration=30M` Als Alternative zur Endzeit des Events (dtend) können Sie eine Dauer wie 1 Stunde oder 30 Minuten angeben.
- **Erinnerungsalarmzeit, in Minuten:** `&reminder=15`
- **Ganztägiges Event:** `&allday=1`
- **UID:** optionaler Parameter, um den eindeutigen Bezeichner für das Ereignis fest zu kodieren, sodass einige Kalenderanwendungen das Event nach und nach aktualisieren können. Die Zeichenfolge @ics.agical.io wird automatisch an den Wert angehängt.

Sie können auch zusätzliche Parameter für wiederkehrende Events hinzufügen:
- **Wöchentliche Events:** `&recur=weekly`
- **Monatliche Events:** `&recur=monthly`
- **Ende der Wiederholung:** `&recuruntil=END_DATE`, wobei `END_DATE` das Datum und die Uhrzeit des Endes der Wiederholung im ISO 8601-Format (JJJJ-MM-TTTHH:MM:SSZ) als UTC ist

## Link Verhalten

Wenn ein Benutzer auf den Link klickt, wandeln die Kalender die UTC-Zeitstempel in den URLs automatisch so um, dass sie die Zeitzone des Benutzers widerspiegeln, die in seinem Kalender eingestellt ist.

Wenn Sie beispielsweise den Link „Zum Google Kalender hinzufügen“ öffnen und Ihr Kalender auf CST eingestellt ist, wird die Uhrzeit des Events automatisch entsprechend der 15-Uhr-UTC-Zeit in CST (10 Uhr) ausgefüllt.

### Google Kalender

Wenn Sie darauf klicken, öffnet sich der Google-Kalender in einer neuen Registerkarte oder einem neuen Fenster mit den Details des Termins, die in der Einladung bereits ausgefüllt sind und die der Nutzer speichern kann. Dies geschieht sowohl auf dem Handy als auch auf dem Desktop.

![Google Kalender-Dialog zum Hinzufügen eines Termins mit den hinzugefügten und speicherbereiten Details.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal oder Outlook

Wenn Sie auf den Desktop klicken, wird eine ICS-Datei heruntergeladen. Der Benutzer muss dann die ICS-Datei öffnen, wodurch iCal oder Outlook geöffnet wird und der Benutzer aufgefordert wird, das Ereignis zu seinem Kalender hinzuzufügen.

![iCal-Kalender mit einem Dialog zum Hinzufügen eines neuen Termins, der den Nutzer:innen auffordert, einen Kalender auszuwählen und zu bestätigen.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![iCal-Kalender mit dem hinzugefügten Ereignis.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

Auf dem Handy müssen Sie den Link gedrückt halten und werden dann aufgefordert, ihn zu Ihrem Kalender hinzuzufügen.

![iOS-Popup-Fenster, wenn Sie auf einen Kalender-Link drücken und ihn gedrückt halten, das einen Button "Zum Kalender hinzufügen" enthält.]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

Weitere Informationen finden Sie unter:
* [Events für Google Kalender erstellen](https://developers.google.com/calendar/api/guides/create-events)
* [Erstellen Sie einen Link Zum Kalender hinzufügen in einer E-Mail-Nachricht](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)


