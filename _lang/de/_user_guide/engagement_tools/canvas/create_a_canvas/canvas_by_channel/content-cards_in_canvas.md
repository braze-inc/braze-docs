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

![Content-Cards als Messaging-Kanal für einen Nachrichten-Schritt ausgewählt.]({% image_buster /assets/img_archive/content-cards-in-canvas.png %})

Zwei Optionen, die die Interaktion des Content-Card-Schrittes mit Canvas verändern, sind sein [Ablauf](#content-card-expiration) und seine [Entfernung](#removal).

## Content-Card-Ablauf {#content-card-expiration}

Wenn Sie eine neue Content-Card erstellen, können Sie anhand der Sendezeit festlegen, wann diese aus dem Feed des Nutzers oder der Nutzerin ablaufen soll. Der Countdown für den Ablauf einer Content-Card beginnt, wenn der oder die Nutzer:in den Nachrichtenschritt im Canvas erreicht, in dem die Karte gesendet wird. Die Karte ist ab diesem Zeitpunkt im Feed des Nutzers der Nutzerin aktiv, bis sie abläuft. Eine Karte kann bis zu 30 Tage lang im Feed eines Benutzers vorhanden sein. 

![Ablaufeinstellungen für eine Content-Card für einen Nachrichtenschritt, die nach drei Stunden im Feed eines Nutzers:innen entfernt wird.]({% image_buster /assets/img_archive/content-cards-in-canvas-expiration.png %})

### Arten des Verfalls

Sie haben zwei Möglichkeiten festzulegen, wann eine Karte aus dem Feed eines Benutzers verschwinden soll: ein relatives Datum oder ein absolutes Datum.

#### Relative Daten

Wenn Sie ein relatives Datum wählen, wie z.B. "Gesendete Karten nach 5 Tagen im Feed eines Nutzers:innen entfernen", können Sie ein Verfallsdatum von bis zu 30 Tagen festlegen.

#### Absolute Daten

Wenn Sie ein absolutes Datum wählen, wie z.B. "Gesendete Karten am 1\. Dezember 2023 um 16 Uhr entfernen", gibt es einige Nuancen.

Obwohl Sie eine Ablaufdauer von mehr als 30 Tagen angeben können, bleibt die Content-Card maximal 30 Tage lang im Feed eines Nutzers oder einer Nutzerin. Wenn Sie eine Dauer von mehr als 30 Tagen angeben, können Sie eventuelle Verzögerungen vor dem Triggern des Schritts Nachricht berücksichtigen, aber die maximale Lebensdauer der Karte im Feed des Nutzers oder Nutzers wird dadurch nicht verlängert.

Seien Sie vorsichtig, wenn Sie ein Ablaufdatum festlegen, das mehr als 30 Tage nach dem Start des Canvas liegt. Erreicht ein:e Nutzer:in den Nachrichtenschritt mehr als 30 Tage vor dem angegebenen Ablaufdatum erreicht, wird die Karte nicht gesendet.

### Ablaufverhalten

Die Content-Card bleibt bis zu ihrem Ablaufdatum im Feed des Nutzers oder der Nutzerin verfügbar, auch wenn der oder die Nutzer:in zu weiteren Schritten in der Canvas-Journey fortschreitet. Wenn Sie nicht möchten, dass die Content-Card live ist, wenn die nächsten Schritte im Canvas zugestellt werden, stellen Sie sicher, dass die Ablaufzeit kürzer ist als die Verzögerung bei den nachfolgenden Schritten.

Nachdem eine Content Card abgelaufen ist, wird sie bei der nächsten Aktualisierung automatisch aus dem Feed des Benutzers entfernt, auch wenn dieser sie noch nicht angesehen hat.

## Content-Card entfernen {#removal}

Content-Cards können entfernt werden, wenn Nutzer:innen einen Kauf abschließen oder ein angepasstes Event durchführen. Sie können eines der folgenden Ereignisse als Entfernungsereignis auswählen: **Passen Sie ein angepasstes Event an** und **tätigen Sie einen Kauf**. Wählen Sie dann **Ereignis hinzufügen**.

!["Karten entfernen, wenn Nutzer:innen einen Kauf abschließen oder ein angepasstes Event durchführen." ausgewählt mit dem Trigger, um Karten für Nutzer:innen zu entfernen, die einen bestimmten Kauf für "Armband" tätigen.]({% image_buster /assets/img_archive/content-cards-in-canvas-removal-event.png %})

## Berichte und Analysen

Nachdem Sie einen Content-Cards-Schritt in Canvas gestartet haben, können Sie damit beginnen, verschiedene Metriken für diesen Schritt zu analysieren. Zu diesen Metriken gehören die Anzahl der versendeten Nachrichten, eindeutige Empfänger, Konversionsraten, Gesamtumsatz und mehr.

![Analytics für einen Nachrichtenschritt mit der Content-Card Nachricht Performance.]({% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %})

Weitere Informationen über die verfügbaren Metriken und ihre Definitionen finden Sie in unserem [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/).

## Anwendungsfälle

#### Werbeangebote

Fügen Sie dem Feed eines Nutzers oder einer Nutzerin Karten hinzu, wenn er oder sie sich für bestimmte Aktionen und Anzeigen qualifiziert. Wenn ein Benutzer beispielsweise nach einer Aktion oder einem Kauf für ein neues Angebot in Frage kommt, können Sie ihm mit Canvas zusätzlich zu anderen Nachrichtenkanälen eine Content Card senden, so dass das Angebot beim nächsten Öffnen der App für ihn verfügbar ist.

#### Posteingang für Push-Benachrichtigungen

Es kann vorkommen, dass ein Nutzer eine Push-Benachrichtigung ablehnt oder eine E-Mail löscht, aber Sie möchten ihn daran erinnern oder für das Angebot werben, falls er seine Meinung ändert.

Mit Canvas können Sie eine Komponente hinzufügen, die sowohl eine Inhaltskarte als auch eine Push-Benachrichtigung sendet, um den Benutzern einen dauerhaften "Posteingang" mit Karten zu bieten, die mit den per Push gesendeten Werbebotschaften übereinstimmen. 

#### Mehrere Feeds basierend auf Kategorien

Sie können Ihre Content Cards in mehrere Feeds unterteilen, die auf Kategorien basieren, wie z.B. verschiedene Themen, die Benutzer durchsuchen können, oder Transaktions- und Marketing-Feeds. Weitere Informationen zur Erstellung mehrerer Feeds mithilfe von Schlüssel-Wert-Paaren finden Sie in unserem Leitfaden zur [Anpassung von Content-Card-Feeds]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).


