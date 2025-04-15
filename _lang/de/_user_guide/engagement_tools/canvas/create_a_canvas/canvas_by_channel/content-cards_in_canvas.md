---
nav_title: Content-Cards
article_title: Inhaltskarten in Canvas
page_order: 1
page_type: reference
description: "Dieser Referenzartikel beschreibt die Besonderheiten und Nuancen der Verwendung von Content-Cards als Messaging-Kanal innerhalb von Canvas."
tool: Canvas
channel: content cards

---

# Inhaltskarten in Canvas

> Content Cards können als Teil der Canvas-Reise an Ihre Kunden geschickt werden. Dieser Artikel beschreibt die Besonderheiten und Feinheiten der Verwendung von Content Cards als Nachrichtenkanal in Canvas.

Wie bei anderen Canvas-Messaging-Kanälen werden Content Cards an das Gerät eines Nutzers gesendet, wenn dieser die für die jeweilige Stufe festgelegten Zielgruppen- und Targeting-Kriterien erfüllt. Nachdem die Content Card versendet wurde, ist sie im Feed jedes berechtigten Nutzers verfügbar, wenn dessen Karten-Feed das nächste Mal aktualisiert wird.

![][1]

Zwei Optionen, die die Interaktion des Content-Card-Schritts mit Canvas verändern, beziehen sich auf [Ablauf](#content-card-expiration) und [Fortschrittsverhalten](#advancement-behavior-options).

## Content-Card-Ablauf {#content-card-expiration}

Wenn Sie eine neue Content-Card erstellen, können Sie anhand der Sendezeit festlegen, wann diese aus dem Feed des Nutzers oder der Nutzerin ablaufen soll. Der Countdown für den Ablauf einer Content-Card beginnt, wenn der oder die Nutzer:in den Nachrichtenschritt im Canvas erreicht, in dem die Karte gesendet wird. Die Karte ist ab diesem Zeitpunkt im Feed des Nutzers der Nutzerin aktiv, bis sie abläuft. Eine Karte kann bis zu 30 Tage lang im Feed eines Benutzers vorhanden sein. 

### Relative versus absolute Verfallsdaten

Sie haben zwei Möglichkeiten festzulegen, wann eine Karte aus dem Feed eines Benutzers verschwinden soll: ein relatives Datum oder ein absolutes Datum. So funktionieren sie:

#### Relative Daten

Wenn Sie ein relatives Datum auswählen, wie z. B. „Gesendete Karten nach 5 Tagen aus dem Feed eines Nutzers oder einer Nutzerin entfernen“, können Sie ein Ablaufdatum von maximal 30 Tagen festlegen.

#### Absolute Daten

Wenn Sie ein absolutes Datum wählen, wie z.B. "Gesendete Karten am 1\. Dezember 2023 um 16 Uhr entfernen", gibt es einige Nuancen.

Obwohl Sie eine Ablaufdauer von mehr als 30 Tagen angeben können, bleibt die Content-Card maximal 30 Tage lang im Feed eines Nutzers oder einer Nutzerin. Wenn Sie eine Dauer von mehr als 30 Tagen angeben, können Sie eventuelle Verzögerungen vor dem Triggern des Schritts Nachricht berücksichtigen, aber die maximale Lebensdauer der Karte im Feed des Nutzers oder Nutzers wird dadurch nicht verlängert.

Seien Sie vorsichtig, wenn Sie ein Ablaufdatum festlegen, das mehr als 30 Tage nach dem Start des Canvas liegt. Erreicht ein:e Nutzer:in den Nachrichtenschritt mehr als 30 Tage vor dem angegebenen Ablaufdatum erreicht, wird die Karte nicht gesendet.

### Ablaufverhalten

Die Content-Card bleibt bis zu ihrem Ablaufdatum im Feed des Nutzers oder der Nutzerin verfügbar, auch wenn der oder die Nutzer:in zu weiteren Schritten in der Canvas-Journey fortschreitet. Wenn Sie nicht möchten, dass die Content-Card live ist, wenn die nächsten Schritte im Canvas zugestellt werden, stellen Sie sicher, dass die Ablaufzeit kürzer ist als die Verzögerung bei den nachfolgenden Schritten.

Nachdem eine Content Card abgelaufen ist, wird sie bei der nächsten Aktualisierung automatisch aus dem Feed des Benutzers entfernt, auch wenn dieser sie noch nicht angesehen hat.

## Fortschrittsverhalten-Optionen {#advancement-behavior-options}

{% alert important %}
Ab dem 28\. Februar 2023 können Sie keine Canvase mehr mit dem Original-Editor erstellen oder duplizieren. Dieser Abschnitt dient zum Nachschlagen, wenn Sie verstehen möchten, wie das Fortschrittsverhalten bei Schritten mit Inhaltskarten funktioniert.
{% endalert %}

{% alert note %}
In Canvas Flow bringen die Nachrichtenkomponenten automatisch alle Nutzer:innen voran, die den Schritt aufrufen. Es ist nicht erforderlich, das Verhalten des Nachrichtenfortschritts anzugeben, wodurch die Konfiguration des Gesamtschritts vereinfacht wird. Wenn Sie die Option **Weiterleiten, wenn Nachricht gesendet wurde** implementieren möchten, fügen Sie einen separaten [Zielgruppenpfad]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) hinzu, um Benutzer zu filtern, die den vorherigen Schritt nicht erhalten haben.
{% endalert %}

Mit der Option „Fortschrittsverhalten“ können Sie festlegen, wann ein:e Nutzer:in den nächsten Schritt übergehen soll. Schritte, die [nur Content-Cards](#steps-with-in-content-cards-only) versenden, haben andere Möglichkeiten des Fortschritts als [Schritte mit mehreren Content-Typen](#steps-with-multiple-message-channels) (Push, E-Mail usw.). Bei Content-Cards in einem Canvas-Flow-Workflow ist diese Option so eingestellt, dass die Zielgruppe immer sofort fortschreitet.

### Schritte nur mit Inhaltskarten {#steps-with-in-content-cards-only}

Wenn ein Schritt nur Content-Cards (und keinen anderen Messaging-Kanal) enthält, können Sie das Fortschrittsverhalten mit den folgenden Optionen steuern:

| Option | Beschreibung |
|---|---|
| Voranbringen, wenn Nachricht gesendet wird | Nutzer:innen gelangen zu den nächsten Schritten des Canvas, wenn die Content-Card erfolgreich gesendet wurde. Verwenden Sie diese Option, wenn Sie möchten, dass die Benutzer nur dann weiterkommen, wenn die Karte gesendet und nicht abgebrochen wird. |
| Zielgruppe sofort voranbringen | Nutzer:innen gelangen zu den nächsten Schritten des Canvas, wenn versucht wird, die Content-Card zu senden. Wenn die Karte abgebrochen und nicht gesendet wird, gelangen die Nutzer:innen trotzdem zum nächsten Schritt. Verwenden Sie diese Option, wenn Nutzer:innen unabhängig davon, ob die Content-Card erfolgreich gesendet oder abgebrochen wurde, weitergeleitet werden sollen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][2]

### Komponenten mit mehreren Kanälen {#steps-with-multiple-message-channels}

Canvas-Komponenten mit einer Content-Card und einem anderen Messaging-Kanal haben die folgenden Fortschrittsoptionen:

| Option | Beschreibung |
|---|---|
| Voranbringen, wenn Nachricht gesendet wird | Nutzer:innen gelangen zu den nächsten Schritten des Canvas, wenn mindestens einer der Content-Typen in diesem Schritt erfolgreich gesendet wurde.|
| Zielgruppe sofort voranbringen | Wenn diese Option ausgewählt ist, wird jeder in der Zielgruppe der Komponente nach Ablauf der Verzögerung zu den nächsten Schritten geleitet, unabhängig davon, ob er oder sie die notierte Nachricht gesehen hat oder nicht.  <br> <br> _Nutzer:innen müssen die Segmentierungs- und Filterkriterien der Komponente erfüllen, um mit den nächsten Schritten fortfahren zu können._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][3]

## Berichte und Analysen

Nachdem Sie einen Content-Cards-Schritt in Canvas gestartet haben, können Sie damit beginnen, verschiedene Metriken für diesen Schritt zu analysieren. Zu diesen Metriken gehören die Anzahl der versendeten Nachrichten, eindeutige Empfänger, Konversionsraten, Gesamtumsatz und mehr.

![][4]

Weitere Informationen zu den verfügbaren Metriken und ihren Definitionen finden Sie in unserem [Report Metrics Glossary][6]].

## Anwendungsfälle

#### Werbeangebote

Fügen Sie dem Feed eines Nutzers oder einer Nutzerin Karten hinzu, wenn er oder sie sich für bestimmte Aktionen und Anzeigen qualifiziert. Wenn ein Benutzer beispielsweise nach einer Aktion oder einem Kauf für ein neues Angebot in Frage kommt, können Sie ihm mit Canvas zusätzlich zu anderen Nachrichtenkanälen eine Content Card senden, so dass das Angebot beim nächsten Öffnen der App für ihn verfügbar ist.

#### Posteingang für Push-Benachrichtigungen

Es kann vorkommen, dass ein Nutzer eine Push-Benachrichtigung ablehnt oder eine E-Mail löscht, aber Sie möchten ihn daran erinnern oder für das Angebot werben, falls er seine Meinung ändert.

Mit Canvas können Sie eine Komponente hinzufügen, die sowohl eine Inhaltskarte als auch eine Push-Benachrichtigung sendet, um den Benutzern einen dauerhaften "Posteingang" mit Karten zu bieten, die mit den per Push gesendeten Werbebotschaften übereinstimmen. 

#### Mehrere Feeds basierend auf Kategorien

Sie können Ihre Content Cards in mehrere Feeds unterteilen, die auf Kategorien basieren, wie z.B. verschiedene Themen, die Benutzer durchsuchen können, oder Transaktions- und Marketing-Feeds. Weitere Informationen zur Erstellung mehrerer Feeds mithilfe von Schlüssel-Wert-Paaren finden Sie in unserem Leitfaden [Content-Anpassen von Card-Feeds][7].


[1]: {% image_buster /assets/img_archive/content-cards-in-canvas.png %}
[2]: {% image_buster /assets/img_archive/content-cards-in-canvas-single-channel.png %}
[3]: {% image_buster /assets/img_archive/content-cards-in-canvas-multiple-channels.png %}
[4]: {% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %}
[6]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
[7]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds