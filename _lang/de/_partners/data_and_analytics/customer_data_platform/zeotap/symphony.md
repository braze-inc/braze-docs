---
nav_title: Zeotap Symphonie
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Zeotap, einer Kundendaten-Plattform der nächsten Generation, die Identitätsauflösung, Insights und Anreicherung bietet."
page_type: partner
search_tag: Partner
page_order: 2 
---

# Zeotap Symphonie

Die Integration von Braze und Zoetap Symphony erlaubt es Ihnen, Orchestrierungen in Realtime zu erstellen und Kampagnen per E-Mail und Push-Benachrichtigung durchzuführen.

- Senden Sie Vor- und Nachnamen über Zeotap, auf deren Grundlage Nutzer:innen personalisierte E-Mails über Braze versenden können.
- Senden Sie angepasste Events oder ein Kauf-Event in Realtime über Zeotap, auf deren Grundlage Nutzer:innen innerhalb von Braze Kampagnen-Trigger erstellen können, um ihre Kund:innen zu targetieren.

{% alert note %}
Um E-Mail Marketing Kampagnen zu erstellen, onboarding Sie die rohen E-Mails in Zeotap, indem Sie sie `Email Raw` im Zeotap-Katalog zuordnen.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Client Name | Dies ist Ihr Client-Name für Ihr Braze-Konto. Sie finden sie, indem Sie zur Braze-Konsole navigieren. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze Onboarding Manager oder auf der [Übersichtsseite über die APIs]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

In diesem Abschnitt finden Sie Informationen zu den beiden Methoden, die Sie für die Integration mit Braze verwenden können:

### Methode 1
Bei dieser Methode müssen Sie die folgenden Aufgaben ausführen:
1. Integrieren Sie das Braze SDK auf Ihrer Website oder in Ihrer App.
2. Integrieren Sie Braze mit Zeotap über Symphony.

- `User traits` müssen den entsprechenden Braze-Feldern auf dem Tab **Zu sendende Daten** zugeordnet werden. Wenn Sie die Attribute `Event` und `Purchase` abbilden, führt dies zu einer Duplizierung von Ereignissen innerhalb von Braze.
- Abbildung `External ID` auf `User ID`, die beim Einrichten des Braze SDK konfiguriert wurde.

Wenn die Integration erfolgreich eingerichtet ist, können Sie Kampagnen für E-Mails und Push-Benachrichtigungen erstellen, die auf angepassten Attributen basieren, die über Symphony an Braze gesendet werden.

### Methode 2
Bei dieser Methode können Sie Braze über Symphony in Zeotap integrieren.

- Diese Methode unterstützt nicht die UI-Features von Braze wie In-App-Nachrichten, Content-Cards oder Push-Benachrichtigungen.
- Zeotap empfiehlt die Abbildung der im Zeotap-Katalog verfügbaren `hashed email` auf die `External ID`.

Wenn die Integration erfolgreich eingestellt ist, können Sie nur noch E-Mail Kampagnen erstellen, die auf angepassten Attributen basieren, die über Symphony an Braze gesendet werden.

## Datenfluss zu Braze und unterstützte Bezeichner

Die Daten fließen von Zeotap zu Braze über den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Die folgenden Datenpunkte fassen den Datenfluss zusammen:

1. Zeotap sendet Nutzerprofil-Attribute, angepasste Attribute, angepasste Events und Kauf-Events.
2. Sie bilden alle relevanten Zeotap-Katalogfelder in den Braze-Feldern unter dem Tab **Zu sendende Daten** ab.
3. Die Daten werden dann auf Braze hochgeladen.

Einzelheiten zu den verschiedenen Attributen finden Sie unter dem Abschnitt [Zu sendende Daten](#data-to-send-tab).

## Ziel einrichten

Nachdem Sie in Symphony Filter angewendet oder eine Bedingung für Ihre Nutzer:innen hinzugefügt haben, können Sie diese in Braze unter **An Ziele senden** aktivieren. Es öffnet sich ein neues Fenster, in dem Sie Ihr Ziel festlegen können. Sie können ein vorhandenes Ziel aus der Liste der **verfügbaren Ziele** verwenden oder ein neues Ziel erstellen.

#### Neues Ziel hinzufügen
Führen Sie die folgenden Schritte aus, um ein neues Ziel hinzuzufügen:
1. Wählen Sie **Neues Ziel hinzufügen**.
2. Suchen Sie nach **Braze**.
3. Fügen Sie den **Client-Namen**, **API-Schlüssel** und die **Instanz** hinzu und speichern Sie das Ziel.

Das Ziel wird erstellt und unter **Verfügbare Ziele** verfügbar gemacht.

#### Eingaben auf Workflow-Ebene hinzufügen
Nachdem Sie ein Ziel erstellt haben, müssen Sie als Nächstes Eingaben auf Workflow-Ebene hinzufügen, wie unten beschrieben.
1. Wählen Sie das Ziel aus der Liste der verfügbaren Ziele mit Hilfe des Features Suche.
2. Die Felder **Client-Name**, **API-Schlüssel** und **Instanz** werden automatisch auf der Grundlage des Wertes ausgefüllt, den Sie bei der Erstellung des Ziels eingegeben haben.
3. Geben Sie den **Namen der Zielgruppe** ein, die Sie für diesen Workflow-Knoten erstellen möchten. Dies wird als **angepasstes Attribut** an Braze gesendet.
4. Vervollständigen Sie die Abbildung des Katalogs auf das Ziel auf dem Tab **Zu sendende Daten**. Details zur Durchführung der Abbildung finden Sie unten.

#### Tab "Zu sendende Daten
Auf dem Tab **Zu sendende Daten** können Sie die Zeotap-Katalogfelder den Braze-Feldern zuordnen, die an Braze gesendet werden können. Die Abbildung kann auf eine der folgenden Arten erfolgen:
- **Statische Abbildung** \- Es gibt bestimmte Felder, die Zeotap automatisch den entsprechenden Feldern von Braze zuordnet, z.B. E-Mail, Telefon, Vorname, Nachname und so weiter.<br>
- **Dropdown-Auswahl** \- Ordnen Sie die relevanten, in Zeotap aufgenommenen Felder den im Dropdown-Menü bereitgestellten Braze-Feldern zu.<br>![Verschiedene Nutzer:innen, die in Zeotap eingestellt sind, wie Sprache, Ort, Geburtstag und mehr.]({% image_buster /assets/img/zeotap/zeotap7.png %}){: style="max-width:70%;"}<br>
- **Eingabe angepasster Daten** \- Fügen Sie angepasste Daten hinzu, die dem entsprechenden Zeotap-Feld zugeordnet sind, und senden Sie diese an Braze.<br>![Auswählen von "loyalty_points" als Nutzer:innen-Eigenschaft in Zeotap.]({% image_buster /assets/img/zeotap/zeotap8.png %}){: style="max-width:70%;"}

## Unterstützte Attribute
In diesem Abschnitt finden Sie Details zu allen Braze-Feldern.

| Braze Feld | Abbildung Typ | Beschreibung |
| --- | --- | --- |
| Externe ID | Dropdown-Auswahl | Dies ist die persistente `User ID`, die Sie von Braze definiert haben, um Nutzer:innen geräte- und plattformübergreifend zu tracken. Wir empfehlen Ihnen, `User ID` auf `External ID` abzubilden; andernfalls kann Zeotap E-Mails als Nutzer:in versenden.<br><br>Zeotap empfiehlt die Abbildung der im Zeotap-Katalog verfügbaren `hashed email` auf die `External ID`.|
| E-Mail | Statische Abbildung | Diese Abbildung ist im Zeotap-Katalog unter `Email Raw` zu finden. |
| Telefon | Statische Abbildung | Diese Abbildung ist im Zeotap-Katalog unter `Mobile Raw` zu finden.<br><br>\- Braze akzeptiert Rufnummern im Format `E.164`. Zeotap führt keine Transformation durch. Daher müssen Sie die Telefonnummern in dem vorgeschriebenen Format eingeben. Weitere Informationen finden Sie unter [Benutzertelefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/). |
| Vorname | Statische Abbildung | Diese Abbildung ist im Zeotap-Katalog unter `First Name` zu finden. |
| Nachname | Statische Abbildung | Diese Abbildung ist im Zeotap-Katalog unter `Last Name` zu finden. |
| Geschlecht | Statische Abbildung | Diese Abbildung ist im Zeotap-Katalog unter `Gender` zu finden. |
| Name des angepassten Events | Statische Abbildung | Diese Abbildung ist im Zeotap-Katalog unter `Event Name` zu finden.<br><br>Sowohl der Name des angepassten Events als auch der Zeitstempel des angepassten Events müssen abgebildet werden, um angepasste Events in Braze zu erfassen. Das angepasste Event kann nicht verarbeitet werden, wenn eines der beiden nicht abgebildet ist. Weitere Informationen finden Sie unter [Ereignisobjekt]({{site.baseurl}}/api/objects_filters/event_object#what-is-the-event-object). |
| Angepasster Event Zeitstempel | Statische Abbildung | Diese Abbildung ist der `Event Timestamp` im Zeotap-Katalog zugeordnet.<br><br>Sowohl der Name des angepassten Events als auch der Zeitstempel des angepassten Events müssen abgebildet werden, um angepasste Events in Braze zu erfassen. Das angepasste Event kann nicht verarbeitet werden, wenn eines der beiden nicht abgebildet ist. Weitere Informationen finden Sie unter [Ereignisobjekt]({{site.baseurl}}/api/objects_filters/event_object#what-is-the-event-object). |
| E-Mail Abonnent:innen | Dropdown-Auswahl | Onboarding eines `Email Marketing Preference` Feldes und Abbildung auf dieses Feld.<br><br>Zeotap sendet die folgenden drei Werte:<br>- `opted_in` - Zeigt an, dass sich die Nutzer:innen explizit für das Marketing per E-Mail registriert haben.<br>- `unsubscribed` - Zeigt an, dass der Nutzer:innen sich explizit gegen Nachrichten per E-Mail entschieden hat.<br>- `subscribed` - Zeigt an, dass der Nutzer:in weder ein Opt-in noch ein Opt-out gemacht hat. |
| Push Abonnieren | Dropdown-Auswahl | Onboarding eines `Push Marketing Preference` Feldes und Abbildung auf dieses Feld.<br><br>Zeotap sendet die folgenden drei Werte:<br>- `opted_in` - Zeigt an, dass sich der Nutzer:innen ausdrücklich für Push Marketing registriert hat.<br>- `unsubscribed` - Zeigt an, dass der Nutzer:innen sich ausdrücklich gegen Push Nachrichten entschieden hat.<br>- `subscribed` - Zeigt an, dass der Nutzer:in weder Opt-in noch Opt-out gewählt hat |
| E-Mail Öffnung Tracking Enablement | Dropdown-Auswahl | Bilden Sie das entsprechende Feld `Marketing Preference` ab.<br><br>Wenn es auf true gesetzt ist, wird ein Tracking-Pixel für die Öffnung zu allen zukünftigen E-Mails hinzugefügt, die an diesen Nutzer:innen gesendet werden. |
| E-Mail Click Tracking Enablement | Dropdown-Auswahl | Bilden Sie das entsprechende Feld `Marketing Preference` ab.<br><br>Wenn diese Option auf true gesetzt ist, wird das Tracking von Klicks für alle Links in allen zukünftigen E-Mails, die an diesen Nutzer:innen gesendet werden, aktiviert. |
| Produkt ID | Dropdown-Auswahl | \- Bezeichner für eine Kaufaktion `(Product Name/Product Category)`. Weitere Einzelheiten finden Sie unter [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/).<br>\- Onboarding des entsprechenden Attributs in den Zeotap-Katalog und Abbildung auf dieses Attribut.<br><br>`Product ID`, `Currency`, und `Price` müssen zwingend abgebildet werden, um Kauf-Events in Braze zu erfassen. Das Kauf-Event kann nicht durchgeführt werden, wenn eine der drei Bedingungen nicht erfüllt ist. Weitere Informationen finden Sie unter [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-object). |
| Währung | Dropdown-Auswahl | \- Währungsattribut für die Kaufaktion.<br>\- Das unterstützte Format ist `ISO 4217 Alphabetic Currency Code`.<br>\- Onboarding von korrekt formatierten Währungsdaten in den Zeotap-Katalog und Abbildungen dazu.<br><br>`Product ID`, `Currency`, und `Price` müssen zwingend abgebildet werden, um Kauf-Events in Braze zu erfassen. Das Kauf-Event kann nicht durchgeführt werden, wenn eine der drei Bedingungen nicht erfüllt ist. |
| Preis | Dropdown-Auswahl | \- Preisattribut für die Kaufaktion.<br>\- Onboarding des entsprechenden Attributs in den Zeotap-Katalog und Abbildung auf dieses Attribut.<br><br>`Product ID`, `Currency`, und `Price` müssen zwingend abgebildet werden, um Kauf-Events in Braze zu erfassen. Das Kauf-Event kann nicht durchgeführt werden, wenn eine der drei Bedingungen nicht erfüllt ist. |
| Menge | Dropdown-Auswahl | \- Attribut "Menge" für die Kaufaktion.<br>\- Onboarding des entsprechenden Attributs in den Zeotap-Katalog und Abbildung auf dieses Attribut. |
| Land | Dropdown-Auswahl | Abbildung auf das `Country` Katalogfeld, das Sie onboarding. |
| Ort | Dropdown-Auswahl | Abbildung auf das `City` Katalogfeld, das Sie onboarding. |
| Sprache | Dropdown-Auswahl | \- Das akzeptierte Format ist `ISO-639-1` standard (zum Beispiel en).<br>\- Onboarding der korrekt formatierten Sprache und Abbildung auf diese. |
| Geburtsdatum | Dropdown-Auswahl | Abbildung auf das `Date of Birth` Feld, das Sie onboarding. |
| Angepasstes Attribut | Angepasste Dateneingabe | Passen Sie jedes Nutzerdaten-Attribut an eine angepasste Dateneingabe an, die dann an Braze gesendet wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Daten auf der Braze-Konsole anzeigen

Nachdem Sie die relevanten Attribute, die gesendet und im Workflow veröffentlicht werden sollen, abgebildet haben, werden die Ereignisse auf der Grundlage der definierten Kriterien an Braze weitergeleitet. Sie können in der Braze-Konsole nach E-Mail ID oder externer ID suchen.

![]({% image_buster /assets/img/zeotap/zeotap6.jpg %})

Verschiedene Attribute sind in verschiedenen Abschnitten des Nutzer:innen-Dashboards in Braze zu finden.
- Der Tab **Profil** enthält die Attribute der Nutzer:innen.
- Der Tab **Angepasste Attribute** enthält die angepassten Attribute, die der Nutzer:innen definiert hat.
- Der Tab **Angepasste Events** enthält das vom Nutzer:in definierte angepasste Event.
- Der Tab **Einkäufe** enthält die Einkäufe, die der Nutzer:innen über einen bestimmten Zeitraum getätigt hat.

## Erstellung von Kampagnen

Benutzer können in Braze Kampagnen erstellen und Nutzer:innen in Realtime oder nach Zeitplan aktivieren. Kampagnen können auf der Grundlage der vom Nutzer:in durchgeführten Aktionen (angepasstes Event, Kauf) oder der Attribute des Nutzers ausgelöst werden.

