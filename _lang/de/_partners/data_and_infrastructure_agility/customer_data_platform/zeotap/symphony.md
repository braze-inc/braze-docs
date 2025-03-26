---
nav_title: Zeotap Symphonie
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Zeotap, einer Kundendatenplattform der nächsten Generation, die Identitätsauflösung, Einblicke und Anreicherung bietet."
page_type: partner
search_tag: Partner
page_order: 2 
---

# Zoetap Symphony

Die Integration von Braze und Zoetap Symphony ermöglicht es Ihnen, Echtzeit-Orchestrationen zu erstellen und E-Mail- und Push-Benachrichtigungskampagnen durchzuführen.

- Senden Sie Vor- und Nachnamen über Zeotap, anhand derer Benutzer personalisierte E-Mails über Braze versenden können.
- Senden Sie benutzerdefinierte Ereignisse oder ein Kaufereignis in Echtzeit über Zeotap, auf deren Grundlage Benutzer Kampagnenauslöser in Braze erstellen können, um ihre Kunden anzusprechen.

{% alert note %}
Um E-Mail-Marketingkampagnen zu erstellen, übertragen Sie die Roh-E-Mails in Zeotap, indem Sie sie `Email Raw` im Zeotap-Katalog zuordnen.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Name des Kunden | Dies ist Ihr Kundenname für Ihr Braze-Konto. Sie finden sie, indem Sie zur Braze-Konsole navigieren. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze-Onboarding-Manager oder Sie finden sie auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

In diesem Abschnitt finden Sie Informationen über die beiden Methoden, die Sie mit Braze integrieren können:

### Methode 1
Bei dieser Methode müssen Sie die folgenden Aufgaben ausführen:
1. Integrieren Sie das Braze SDK in Ihre Website oder App.
2. Integrieren Sie Braze mit Zeotap über Symphony.

- `User traits` müssen den entsprechenden Braze-Feldern auf der Registerkarte **Zu sendende Daten** zugeordnet werden. Wenn Sie die Attribute `Event` und `Purchase` zuordnen, führt dies zur Duplizierung von Ereignissen innerhalb von Braze.
- Ordnen Sie `External ID` auf `User ID` zu, das bei der Einrichtung des Braze SDK konfiguriert wurde.

Wenn die Integration erfolgreich eingerichtet ist, können Sie E-Mail- und Push-Benachrichtigungskampagnen erstellen, die auf benutzerdefinierten Attributen basieren, die über Symphony an Braze gesendet werden.

### Methode 2
Bei dieser Methode können Sie Braze über Symphony mit Zeotap integrieren.

- Diese Methode unterstützt nicht die Braze UI-Funktionen wie In-App-Nachrichten, News Feed, Inhaltskarten oder Push-Benachrichtigungen.
- Zeotap empfiehlt, die im Zeotap-Katalog verfügbaren `hashed email` auf die `External ID` zu mappen.

Wenn die Integration erfolgreich eingerichtet ist, können Sie nur E-Mail-Kampagnen erstellen, die auf benutzerdefinierten Attributen basieren, die über Symphony an Braze gesendet werden.

## Datenfluss zu Braze und unterstützte Bezeichner

Die Daten fließen von Zeotap zu Braze über die API für [die Benutzerverfolgung](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/). Die folgenden Punkte fassen den Datenfluss zusammen:

1. Zeotap sendet Benutzerprofilattribute, benutzerdefinierte Attribute, benutzerdefinierte Ereignisse und Kauffelder.
2. Sie ordnen alle relevanten Zeotap-Katalogfelder den Braze-Feldern auf der Registerkarte **Zu sendende Daten** zu.
3. Die Daten werden dann auf Braze hochgeladen.

Einzelheiten zu den verschiedenen Attributen finden Sie unter dem Abschnitt [Zu sendende Daten](#data-to-send-tab).

## Ziel einrichten

Nachdem Sie in Symphony Filter angewendet oder eine Bedingung für Ihre Benutzer hinzugefügt haben, können Sie diese in Braze unter **An Ziele senden** aktivieren. Es öffnet sich ein neues Fenster, in dem Sie Ihr Ziel festlegen können. Sie können ein bestehendes Ziel aus der Liste der **verfügbaren Ziele** verwenden oder ein neues Ziel erstellen.

#### Neues Ziel hinzufügen
Führen Sie die folgenden Schritte aus, um ein neues Ziel hinzuzufügen:
1. Klicken Sie auf **Neues Ziel hinzufügen**.
2. Suchen Sie nach **Braze**.
3. Fügen Sie den **Client-Namen**, den **API-Schlüssel** und die **Instanz** hinzu und speichern Sie das Ziel.

Das Ziel wird erstellt und unter **Verfügbare Ziele** verfügbar gemacht.

#### Eingaben auf Workflow-Ebene hinzufügen
Nachdem Sie ein Ziel erstellt haben, müssen Sie als Nächstes Eingaben auf Workflow-Ebene hinzufügen, wie unten beschrieben.
1. Wählen Sie das Ziel aus der Liste der verfügbaren Ziele mit Hilfe der Suchfunktion.
2. Die Felder **Kundenname**, **API-Schlüssel** und **Instanz** werden automatisch auf der Grundlage des Wertes ausgefüllt, den Sie bei der Erstellung des Ziels eingegeben haben.
3. Geben Sie den **Audience Name** ein, den Sie für diesen Workflow-Knoten erstellen möchten. Dies wird als **benutzerdefiniertes Attribut** an Braze gesendet.
4. Vervollständigen Sie die Zuordnung von Katalog zu Ziel auf der Registerkarte **Zu sendende Daten**. Im Folgenden finden Sie Einzelheiten zur Durchführung der Zuordnung.

#### Registerkarte Zu sendende Daten
Auf der Registerkarte **Zu sendende Daten** können Sie die Zeotap-Katalogfelder den Braze-Feldern zuordnen, die an Braze gesendet werden können. Das Mapping kann auf eine der folgenden Arten erfolgen:
- **Statisches Mapping** \- Es gibt bestimmte Felder, die Zeotap automatisch den entsprechenden Braze-Feldern zuordnet, z.B. E-Mail, Telefon, Vorname, Nachname und so weiter.<br>
- **Dropdown-Auswahl** \- Ordnen Sie die in Zeotap aufgenommenen relevanten Felder den im Dropdown-Menü angebotenen Braze-Feldern zu.<br>![Verschiedene in Zeotap eingestellte Benutzermerkmale, wie Sprache, Stadt, Geburtstag und mehr.][3]{: style="max-width:70%;"}<br>
- **Benutzerdefinierte Dateneingabe** \- Fügen Sie benutzerdefinierte Daten hinzu, die dem entsprechenden Zeotap-Feld zugeordnet sind, und senden Sie sie an Braze.<br>![Auswahl von "loyalty_points" als Benutzereigenschaft in Zeotap.][4]{: style="max-width:70%;"}

## Unterstützte Attribute
In diesem Abschnitt finden Sie Details zu allen Braze-Feldern.

| Hartlötfeld | Mapping Typ | Beschreibung |
| --- | --- | --- |
| Externe ID | Dropdown-Auswahl | Dies ist die persistente `User ID`, die Sie von Braze definiert haben, um Benutzer über Geräte und Plattformen hinweg zu verfolgen. Wir empfehlen Ihnen, `User ID` auf `External ID` abzubilden; andernfalls kann Zeotap E-Mails als Benutzer-Alias versenden.<br><br>Zeotap empfiehlt Ihnen, die im Zeotap-Katalog verfügbaren `hashed email` auf die `External ID` zu übertragen.|
| E-Mail | Statisches Mapping | Im Zeotap-Katalog ist dies auf `Email Raw` abgebildet. |
| Tel. | Statisches Mapping | Im Zeotap-Katalog ist dies auf `Mobile Raw` abgebildet.<br><br>\- Braze akzeptiert Telefonnummern im Format `E.164`. Zeotap führt keine Transformation durch. Daher müssen Sie die Telefonnummern in dem vorgeschriebenen Format eingeben. Weitere Informationen finden Sie unter [Benutzertelefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/). |
| Vorname | Statisches Mapping | Im Zeotap-Katalog ist dies auf `First Name` abgebildet. |
| Nachname | Statisches Mapping | Im Zeotap-Katalog ist dies auf `Last Name` abgebildet. |
| Geschlecht | Statisches Mapping | Im Zeotap-Katalog ist dies auf `Gender` abgebildet. |
| Name des angepassten Events | Statisches Mapping | Im Zeotap-Katalog ist dies auf `Event Name` abgebildet.<br><br>Sowohl der Name des benutzerdefinierten Ereignisses als auch der Zeitstempel des benutzerdefinierten Ereignisses müssen zugewiesen werden, um benutzerdefinierte Ereignisse in Braze zu erfassen. Das benutzerdefinierte Ereignis kann nicht verarbeitet werden, wenn eines der beiden nicht zugeordnet ist. Weitere Informationen finden Sie unter [Ereignisobjekt](https://www.braze.com/docs/api/objects_filters/event_object#what-is-the-event-object). |
| Zeitstempel für benutzerdefinierte Ereignisse | Statisches Mapping | Dies ist der `Event Timestamp` im Zeotap-Katalog zugeordnet.<br><br>Sowohl der Name des benutzerdefinierten Ereignisses als auch der Zeitstempel des benutzerdefinierten Ereignisses müssen zugewiesen werden, um benutzerdefinierte Ereignisse in Braze zu erfassen. Das benutzerdefinierte Ereignis kann nicht verarbeitet werden, wenn eines der beiden nicht zugeordnet ist. Weitere Informationen finden Sie unter [Ereignisobjekt](https://www.braze.com/docs/api/objects_filters/event_object#what-is-the-event-object). |
| E-Mail abonnieren | Dropdown-Auswahl | Gehen Sie an Bord eines `Email Marketing Preference` Feldes und ordnen Sie es zu.<br><br>Zeotap sendet die folgenden drei Werte:<br>- `opted_in` - Zeigt an, dass der Benutzer sich explizit für E-Mail-Marketing-Präferenzen registriert hat<br>- `unsubscribed` - Zeigt an, dass der Benutzer sich explizit von E-Mail-Nachrichten abgemeldet hat<br>- `subscribed` - Zeigt an, dass der Benutzer sich weder an- noch abgemeldet hat. |
| Abonnieren drücken | Dropdown-Auswahl | Gehen Sie an Bord eines `Push Marketing Preference` Feldes und ordnen Sie es zu.<br><br>Zeotap sendet die folgenden drei Werte:<br>- `opted_in` - Zeigt an, dass der Benutzer sich explizit für die Push-Marketing-Präferenz registriert hat<br>- `unsubscribed` - Zeigt an, dass sich der Benutzer ausdrücklich gegen Push-Nachrichten entschieden hat.<br>- `subscribed` - Zeigt an, dass der Benutzer sich weder an- noch abgemeldet hat. |
| E-Mail-Open-Tracking aktivieren | Dropdown-Auswahl | Ordnen Sie das entsprechende Feld `Marketing Preference` zu.<br><br>Wenn diese Option auf true gesetzt ist, wird ein Tracking-Pixel zum Öffnen zu allen zukünftigen E-Mails hinzugefügt, die an diesen Benutzer gesendet werden. |
| E-Mail-Klickverfolgung Aktivieren | Dropdown-Auswahl | Ordnen Sie das entsprechende Feld `Marketing Preference` zu.<br><br>Wenn diese Option auf true gesetzt ist, können Sie alle Links in allen zukünftigen E-Mails, die an diesen Benutzer gesendet werden, verfolgen. |
| Produkt-ID | Dropdown-Auswahl | \- Kennung für eine Kaufaktion `(Product Name/Product Category)`. Weitere Einzelheiten finden Sie unter [Kaufobjekt](https://www.braze.com/docs/api/objects_filters/purchase_object/).<br>\- Nehmen Sie das entsprechende Attribut in den Zeotap-Katalog auf und ordnen Sie es zu.<br><br>`Product ID`, `Currency` und `Price` müssen zwingend zugewiesen werden, um Kaufereignisse in Braze zu erfassen. Der Kaufvorgang kann nicht durchgeführt werden, wenn eine der drei Bedingungen nicht erfüllt ist. Weitere Informationen finden Sie unter [Kaufobjekt](https://www.braze.com/docs/api/objects_filters/purchase_object/#purchase-object). |
| Währung | Dropdown-Auswahl | \- Währungsattribut für die Kaufaktion.<br>\- Das unterstützte Format ist `ISO 4217 Alphabetic Currency Code`.<br>\- Die korrekt formatierten Währungsdaten werden in den Zeotap-Katalog geladen und mit diesem verknüpft.<br><br>`Product ID`, `Currency` und `Price` müssen zwingend zugewiesen werden, um Kaufereignisse in Braze zu erfassen. Der Kaufvorgang kann nicht durchgeführt werden, wenn eine der drei Bedingungen nicht erfüllt ist. |
| Preis | Dropdown-Auswahl | \- Preisattribut für die Kaufaktion.<br>\- Nehmen Sie das entsprechende Attribut in den Zeotap-Katalog auf und ordnen Sie es zu.<br><br>`Product ID`, `Currency` und `Price` müssen zwingend zugewiesen werden, um Kaufereignisse in Braze zu erfassen. Der Kaufvorgang kann nicht durchgeführt werden, wenn eine der drei Bedingungen nicht erfüllt ist. |
| Menge | Dropdown-Auswahl | \- Mengenattribut für die Kaufaktion.<br>\- Nehmen Sie das entsprechende Attribut in den Zeotap-Katalog auf und ordnen Sie es zu. |
| Land | Dropdown-Auswahl | Ordnen Sie dem `Country` Katalogfeld zu, das Sie einbinden möchten. |
| Ort | Dropdown-Auswahl | Ordnen Sie dem `City` Katalogfeld zu, das Sie einbinden möchten. |
| Sprache | Dropdown-Auswahl | \- Das akzeptierte Format ist `ISO-639-1` standard (zum Beispiel en).<br>\- Richtig formatierte Sprache an Bord und Zuordnung zu dieser Sprache. |
| Geburtsdatum | Dropdown-Auswahl | Ordnen Sie dem Feld `Date of Birth` zu, das Sie einbinden möchten. |
| Angepasstes Attribut | Benutzerdefinierte Dateneingabe | Ordnen Sie jedes Benutzerattribut einer benutzerdefinierten Dateneingabe zu, die dann an Braze gesendet wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Anzeigen von Daten auf der Braze-Konsole

Nachdem Sie die relevanten Attribute, die gesendet und im Workflow veröffentlicht werden sollen, zugewiesen haben, werden die Ereignisse auf der Grundlage der definierten Kriterien an Braze weitergeleitet. Sie können in der Braze-Konsole nach E-Mail-ID oder externer ID suchen.

![][2]

Verschiedene Attribute sind unter verschiedenen Abschnitten des Benutzer-Dashboards in Braze zu finden.
- Die Registerkarte **Profil** enthält die Benutzerattribute.
- Die Registerkarte **Benutzerdefinierte Attribute** enthält die vom Benutzer definierten benutzerdefinierten Attribute.
- Die Registerkarte **Benutzerdefinierte Ereignisse** enthält das vom Benutzer definierte benutzerdefinierte Ereignis.
- Die Registerkarte **Einkäufe** enthält die Einkäufe, die der Benutzer über einen bestimmten Zeitraum getätigt hat.

## Erstellung von Kampagnen

Benutzer können in Braze Kampagnen erstellen und Benutzer in Echtzeit oder zu einem bestimmten Zeitpunkt aktivieren. Kampagnen können auf der Grundlage der vom Benutzer durchgeführten Aktionen (benutzerdefiniertes Ereignis, Kauf) oder Benutzerattribute ausgelöst werden.

[1]: {% image_buster /assets/img/zeotap/zeotap5.png %}
[2]: {% image_buster /assets/img/zeotap/zeotap6.jpg %}
[3]: {% image_buster /assets/img/zeotap/zeotap7.png %}
[4]: {% image_buster /assets/img/zeotap/zeotap8.png %}