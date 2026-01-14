---
nav_title: In-App-Nachrichten
article_title: In-App-Nachrichten in Canvas
alias: "/canvas_in-app_messages/"
page_order: 2
page_type: reference
description: "Dieser referenzierte Artikel beschreibt Features und Nuancen, die speziell für In-App-Nachrichten gelten und die Sie Ihrem Canvas hinzufügen können, um Rich Messaging anzuzeigen."
tool: Canvas
channel: in-app messages

---

# In-App-Nachrichten in Canvas

> Sie können In-App-Nachrichten als Teil Ihrer Canvas Journey hinzufügen, um reichhaltiges Messaging zu zeigen, wenn Ihr Kunde sich mit Ihrer App engagiert.

## Funktionsweise

Bevor Sie In-App-Nachrichten in Ihrem Canvas verwenden können, müssen Sie einen [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) mit Verzögerungs- und Zielgruppenoptionen einrichten.

Fügen Sie im Canvas-Builder einen [Nachrichten-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) hinzu und wählen Sie **In-App-Nachricht** als Ihren **Messaging-Kanal**. Sie können selbst bestimmen, [wann Ihre Nachricht abläuft](#in-app-message-expiration) und welches [Verhalten](#advancement-behavior) sie haben wird.

## Hinzufügen einer In-App-Nachricht zu Ihrer Nutzer:innen-Reise

Um eine In-App-Nachricht zu Ihrem Canvas hinzuzufügen, gehen Sie wie folgt vor:

1. Fügen Sie Ihrer Nutzer:innen-Reise einen Schritt für [Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) hinzu.
2. Wählen Sie **In-App-Nachricht** für Ihren **Messaging-Kanal**. 
3. Legen Sie fest, [wann Ihre Nachricht abläuft](#in-app-message-expiration) und welches [Vorbringungsverhalten](#advancement-behavior-options) sie haben wird.

## Getriggerte In-App-Nachrichten

Sie können einen Auslöser für Ihre In-App-Nachrichten auswählen, der bei Sitzungsbeginn oder durch angepasste Events und Käufe getriggert wird.

Nachdem alle Verzögerungen verstrichen sind und die Optionen für die Zielgruppe aktiviert wurden, werden In-App-Nachrichten aktiviert, sobald ein Nutzer:innen den Schritt Nachricht erreicht. Wenn ein Nutzer eine Sitzung startet und das Trigger-Ereignis für die In-App-Nachricht ausführt, sieht der Nutzer:in die In-App-Nachricht. 

Bei Canvas-Schritten mit einem durch eine Aktion getriggerter Entry können Nutzer:innen den Canvas mitten in der Sitzung betreten. In-App-Nachrichten werden erst dann aktiv, wenn eine Sitzung beginnt. Befindet sich ein Nutzer:innen also mitten in einer Sitzung, wenn er den Schritt Nachricht erreicht, erhält er die In-App-Nachricht erst, wenn er eine weitere Sitzung beginnt und den entsprechenden Trigger ausführt.

## Ablauf von In-App-Nachrichten

Sie können wählen, wann die In-App-Nachricht abläuft. Während dieser Zeit bleibt die In-App-Nachricht stehen und wartet darauf, angesehen zu werden, bis sie das Ablaufdatum erreicht hat. Nachdem die In-App-Nachricht gesendet wurde, kann sie einmalig angesehen werden.

![Der Abschnitt Message Controls eines Nachrichtenschritts für eine In-App-Nachricht. Die In-App-Nachricht läuft drei Tage nach der Verfügbarkeit des Schritts ab.]({% image_buster /assets/img_archive/canvas_expiration2.png %}){: style="max-width:90%"}

| Option | Beschreibung | Beispiel |
|---|---|---|
| **Es ist eine Zeitspanne nach dem Schritt verfügbar.** | Legt fest, dass die In-App-Nachricht relativ zu dem Zeitpunkt abläuft, an dem der Schritt für den Nutzer:innen verfügbar wird. | Eine In-App-Nachricht, die zwei Tage lang gültig ist, wird verfügbar, wenn der Nutzer:in den Schritt Nachricht geht und die Zielgruppenoptionen aktiviert sind. Alle Verzögerungen, die vor diesem Schritt auftreten, stammen von den vorangegangenen Verzögerungsschritten in Ihrem Canvas. Die In-App-Nachricht würde dann für 2 Tage (48 Stunden) ab dem Zeitpunkt, an dem der Nutzer den Schritt betritt, zur Verfügung stehen. Während dieser zwei Tage können die Nutzer:innen die In-App-Nachricht sehen, wenn sie die App öffnen. |
| **Zu bestimmten Datum und bestimmter Uhrzeit** | Wählen Sie ein bestimmtes Datum und eine Uhrzeit aus, zu der die In-App-Nachricht nicht mehr verfügbar sein wird. | Wenn Sie einen Verkauf haben, der am 30\. November 2024 endet, wählen Sie diese Option aus, damit Nutzer:innen die zugehörige In-App-Nachricht nicht mehr sehen, wenn der Verkauf endet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Anwendungsfälle

Braze empfiehlt, dass Sie dieses Feature in Ihren Canvase für Aktionen und Onboarding verwenden.

{% tabs %}
  {% tab Promotional %}

Aktionen, Gutscheine und Verkäufe haben oft ein festes Verfallsdatum. Die folgende Leinwand soll Ihre Nutzer zu den günstigsten Zeitpunkten auf eine Werbeaktion aufmerksam machen, die sie nutzen und vielleicht zu einem Kauf führen kann. Diese Aktion läuft am 28\. Februar 2019 um 11:15 Uhr in der Zeitzone Ihres Unternehmens ab.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Canvas-Schritt</th>
    <th>Delay</th>
    <th>Zielgruppe</th>
    <th>Kanal</th>
    <th>Ablauf</th>
    <th>Fortschritt</th>
    <th>Details</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Tag 1 50 % Rabatt</td>
    <td>Keine</td>
    <td>Alle von Eintrag</td>
    <td>Push</td>
    <td>--</td>
    <td>Zielgruppe nach Delay voranbringen</td>
    <td>Ein erster Push, der Ihre Nutzer:innen auf die Aktion aufmerksam macht. Dies soll die Nutzer dazu bringen, Ihre App aufzurufen, um von der Werbeaktion zu profitieren.</td>
  </tr>
  <tr>
    <td>In-App: 50 % Rabatt</td>
    <td>Keine</td>
    <td>Alle von Eintrag</td>
    <td>In-App-Nachricht</td>
    <td><b>Läuft ab:</b> 28.02.2019 11:15 Uhr Ortszeit des Unternehmens</td>
    <td>In-App-Nachricht angesehen</td>
    <td>Der Benutzer hat nun die App geöffnet und wird diese Nachricht erhalten, unabhängig davon, ob er zuvor die Push-Nachricht erhalten hat oder nicht.</td>
  </tr>
  <tr>
    <td>50 % Rabatt beim nächsten Einkauf</td>
    <td>1 Tag nachdem der Benutzer den vorherigen Schritt erhalten hat</td>
    <td>Alle von Eintrag <br><br><b>Filter:</b> Der letzte Kauf liegt mehr als eine Woche zurück</td>
    <td>In-App-Nachricht</td>
    <td><b>Läuft ab:</b> 28.02.2019 11:15 Uhr Ortszeit des Unternehmens</td>
    <td>Keine (letzte Nachricht in Canvas)</td>
    <td>Der Benutzer hat die In-App-Nachricht im vorherigen Schritt erhalten, aber keinen Kauf getätigt, obwohl er in der App ist. <br><br>Diese Nachricht soll den Benutzer noch mehr dazu verleiten, einen Kauf im Rahmen der Werbeaktion zu tätigen.</td>
  </tr>
</tbody>
</table>

Die In-App-Nachrichten verfallen, wenn die Aktion abläuft, um Diskrepanzen zwischen dem Messaging und dem Kundenerlebnis zu vermeiden.

  {% endtab %}
  {% tab User Onboarding %}

Der erste Eindruck, den Sie bei einem Benutzer hinterlassen, ist vielleicht der wichtigste. Das kann über zukünftige Besuche in Ihrer App entscheiden. Ihre anfängliche Kommunikation mit dem Nutzer sollte zu einem vernünftigen Zeitpunkt erfolgen und zu häufigen Besuchen Ihrer App anregen, um die Nutzung zu fördern.

<table class="tg">
<thead>
  <tr>
    <th>Canvas-Schritt</th>
    <th>Delay</th>
    <th>Zielgruppe</th>
    <th>Kanal</th>
    <th>Ablauf</th>
    <th>Fortschritt</th>
    <th>Details</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Willkommens-E-Mail</td>
    <td>Keine</td>
    <td>Alle von Eintrag</td>
    <td>E-Mail</td>
    <td>--</td>
    <td>Zielgruppe nach Delay voranbringen</td>
    <td>Die erste E-Mail, die Ihre Benutzer bei einem Projekt, einer Mitgliedschaft oder einem anderen Onboarding-Programm willkommen heißt. <br><br>Dies soll Nutzer:innen dazu bringen, Ihre App zu verwenden, um mit dem Onboarding zu beginnen.</td>
  </tr>
  <tr>
    <td>Tag 3-6 In-App-Nachricht</td>
    <td>3 Tage, nachdem der oder die Nutzer:in den vorherigen Schritt erhalten hat</td>
    <td>Alle von Eintrag</td>
    <td>In-App-Nachricht</td>
    <td><b>Läuft ab:</b> 3 Tage, nachdem der Schritt verfügbar ist</td>
    <td>In-App-Nachricht – Live</td>
    <td>Wenn der Benutzer auf die E-Mail reagiert hat und zur App weitergeleitet wurde, erhält er die gewünschte In-App-Nachricht, um mit dem Onboarding fortzufahren oder ihn an die damit verbundenen Anforderungen zu erinnern.</td>
  </tr>
  <tr>
    <td>Tag 5 Push </td>
    <td>2 Tage, nachdem der oder die Nutzer:in den vorherigen Schritt erhalten hat</td>
    <td>Alle von Eintrag</td>
    <td>Push</td>
    <td>--</td>
    <td>Nachricht gesendet</td>
    <td>Nachdem Nutzer:innen ihre In-App-Nachricht erhalten haben, bekommen sie einen weiteren Push, um ihr Onboarding fortzusetzen.</td>
  </tr>
</tbody>
</table>

Diese Push-Nachrichten sind um eine In-App-Nachricht herum angeordnet, um sicherzustellen, dass der Nutzer:innen die App besucht und sein Onboarding begonnen hat. Auf diese Weise vermeiden Sie Spam oder unpassende Nachrichten, die Nutzer:innen davon abhalten könnten, Ihre App zu besuchen, und schaffen stattdessen eine fließende, sinnvolle Reihenfolge für ihre ersten Erfahrungen mit Ihrer App.

  {% endtab %}
{% endtabs %}


## Priorisierung von In-App-Nachrichten

Ein Nutzer:innen kann in Ihrem Canvas zwei In-App-Nachrichten gleichzeitig triggern. In diesem Fall hält sich Braze an die folgende Prioritätsreihenfolge, um zu bestimmen, welche In-App-Nachricht angezeigt wird. 

Wählen Sie **Exakte Priorität festlegen** und ziehen Sie verschiedene Canvas-Schritte, um ihre Priorität für den Canvas neu zu ordnen. Standardmäßig werden frühere Schritte in einer Canvas-Variante vor späteren Schritten angezeigt. Nachdem Ihre Schritte in der von Ihnen gewünschten Reihenfolge angeordnet sind, wählen Sie **Sortierung anwenden**.

![Der Prioritätssortierer mit zwei Schritten "Willkommen IAM" und "Followup IAM".]({% image_buster /assets/img_archive/canvas_priority2.png %}){: style="max-width:85%"}

### Änderungen an Entwürfen von aktiven Canvase vornehmen

Wenn Sie in den **Sendeeinstellungen** eines Entwurfs eines aktiven Canvas Änderungen an der Priorität der In-App-Nachrichten vornehmen, werden diese Änderungen direkt auf das aktive Canvas angewendet, wenn die Prioritätssortierung geschlossen wird. In einem Nachrichten-Schritt wird der Prioritätssortierer jedoch aktualisiert, wenn der Entwurf gestartet wird, da die Einstellungen des Canvas-Schritts auf Schrittebene gelten. 

## Verhalten bei Fortschritt

Nachrichten-Schritte bringen automatisch alle Nutzer:innen voran, die den Schritt betreten. Beachten Sie, dass es nicht darauf wartet, dass die In-App-Nachricht ausgelöst oder angezeigt wird. Es ist nicht erforderlich, das Verhalten des Nachrichtenfortschritts anzugeben, wodurch die Konfiguration des Gesamtschritts vereinfacht wird.

Wenn ein Nutzer:in eine In-App-Nachricht eintritt, bringt er sie sofort voran, anstatt das Ablauffenster abzuwarten. In diesem Fall kann ein Verzögerungsschritt in Ihrer Nutzer:in hilfreich sein.

Um die Option **Vorbringen, wenn Nachricht gesendet wurde** zu verwenden, fügen Sie einen separaten [Zielgruppen-Pfad]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) hinzu, um Nutzer:innen zu filtern, die den vorherigen Schritt nicht erhalten haben.

{% details Original Canvas editor %}

Sie können Canvase nicht mehr mit dem Original-Editor erstellen oder duplizieren. In diesem Abschnitt können Sie referenzieren, wie das Fortschrittsverhalten bei Schritten mit In-App-Nachrichten funktioniert.

Für Canvase, die im Original-Editor erstellt wurden, müssen Sie ein Fortschrittsverhalten festlegen – die Kriterien für den Fortschritt durch Ihre Canvas-Komponente. Für [Schritte, die nur In-App-Nachrichten enthalten](#steps-iam-only), gibt es andere Möglichkeiten des Fortschritts als für [Schritte mit mehreren Arten von Nachrichten](#steps-multiple-channels) (wie Push oder E-Mail). Für In-App-Nachrichten im aktuellen Canvas-Workflow ist diese Option so eingestellt, dass die Zielgruppe immer sofort vorangebracht wird.

Die aktionsbasierte Zustellung ist für Canvas-Schritte mit In-App-Nachrichten nicht verfügbar. Canvas-Schritte mit In-App-Nachrichten müssen geplant werden. Stattdessen erscheinen die In-App-Nachrichten von Canvas das erste Mal, wenn Ihr:e Nutzer:in die App öffnet (getriggert durch die Startsitzung), nachdem die geplante Nachricht in der Canvas-Komponente an ihn oder sie gesendet wurde.

Wenn Sie mehrere In-App-Nachrichten in einem Canvas haben, muss ein Benutzer mehrere Sitzungen starten, um jede dieser einzelnen Nachrichten zu erhalten.

{% alert important %}
Wenn **Voranbringen, wenn In-App-Nachricht live ist** ausgewählt ist, bleibt die In-App-Nachricht so lange verfügbar, bis sie abläuft, auch wenn der oder die Nutzer:in die nachfolgenden Schritte übergegangen ist. Wenn Sie nicht möchten, dass die In-App-Nachricht live ist, wenn die nächsten Schritte im Canvas zugestellt werden, stellen Sie sicher, dass die Ablaufzeit kürzer ist als die Verzögerung der nachfolgenden Schritte.
{% endalert %}

#### Schritte mit mehreren Kanälen {#steps-multiple-channels}

Schritte mit einer In-App-Nachricht und einem anderen Kanal haben die folgenden Fortschrittsmöglichkeiten:

| Option | Beschreibung |
|---|---|---|
| Voranbringen, wenn Nachricht gesendet wird | Die Benutzer müssen eine E-Mail, einen Webhook oder eine Push-Benachrichtigung erhalten oder die In-App-Nachricht sehen, um zu den nächsten Schritten im Canvas zu gelangen.  <br> <br>  Wenn die In-App-Nachricht abläuft und der Benutzer die E-Mail, den Webhook oder die Push-Nachricht nicht erhalten oder die In-App-Nachricht nicht angesehen hat, verlässt er den Canvas und geht nicht zu den nächsten Schritten über. |
| Zielgruppe sofort voranbringen | Jeder in der Zielgruppe des Schritts bringt nach Ablauf der Verzögerung die nächsten Schritte voran, unabhängig davon, ob er oder sie die notierte Nachricht gesehen hat oder nicht. <br> <br> Nutzer:innen müssen mit den Segmentierungs- und Filterkriterien des Schritts übereinstimmen, um die nächsten Schritte vorbringen zu können. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Wenn die Option **Gesamte Zielgruppe** ausgewählt ist, bleibt die In-App-Nachricht bis zum Ablauf der Frist verfügbar, auch wenn der Benutzer zu den nachfolgenden Schritten übergeht. Wenn Sie nicht möchten, dass die In-App-Nachricht live ist, wenn die nächsten Schritte im Canvas zugestellt werden, stellen Sie sicher, dass die Ablaufzeit kürzer ist als die Verzögerung der nachfolgenden Schritte.
{% endalert %}

{% enddetails %}

## Trigger-Aktionen

Sie können aus den folgenden Aktionen triggern, um Ihre Nutzer:innen zu targetieren:

- **Kaufen Sie:** Targeting Nutzer:innen zusammenstellen, die einen beliebigen Kauf oder einen bestimmten Kauf tätigen
- **Sitzung beginnen:** Targeting Nutzer:innen, die eine Sitzung in einer beliebigen App oder einer bestimmten App beginnen
- **Angepasstes Event:** Targeting von Nutzern:innen, die das ausgewählte angepasste Event ausführen (das angepasste Event muss mit dem SDK gesendet werden).

Ein Nutzer:innen muss den Canvas-Schritt eingeben, eine Sitzung starten und dann den Trigger ausführen, um eine In-App-Nachricht zu erhalten. Das bedeutet, dass Updates mitten in der Sitzung nicht unterstützt werden. Wenn der Auslöser zum Beispiel der Start einer Sitzung ist, muss der Nutzer:innen nur den Canvas-Schritt betreten und eine Sitzung starten, um die In-App-Nachricht zu erhalten. Wenn der Auslöser nicht der Start einer Sitzung ist, muss der Nutzer:innen den Canvas-Schritt betreten, eine Sitzung starten und dann den Trigger ausführen, um die In-App-Nachricht zu erhalten.

!["Einen bestimmten Kauf tätigen" als triggernde Aktion ausgewählt.]({% image_buster /assets/img_archive/canvas_trigger_actions.png %}){: style="max-width:90%"}

Die folgenden Canvas Features sind bei In-App-Nachrichten nicht verfügbar. Sie werden also nicht auf Ihre In-App-Nachrichten angewendet, selbst wenn sie aktiviert sind.

- Intelligentes Timing
- Rate-Limiting
- Frequency-Capping
- Ausstiegskriterien
- Ruhezeiten

## Benutzerdefinierte Ereigniseigenschaften in einem Canvas

Angepasste Event-Eigenschaften in In-App-Nachrichten für Canvas werden unterstützt. Diese Eigenschaften stammen jedoch von dem angepassten Event oder dem Kauf, der die In-App-Nachricht auslöst, die sich im Schritt Nachricht befindet, und nicht vom vorhergehenden Aktions-Pfad.

## Überlegungen

Im Folgenden finden Sie einige Überlegungen zum Versenden von In-App-Nachrichten in einem Canvas.

- Wenn der Nutzer die App nie neu startet oder nie eine Sitzung beginnt, kann die App nicht herausfinden, ob der Nutzer für die In-App-Nachricht berechtigt ist, d.h. es wird keine In-App-Nachricht versendet.
- Wenn der erste Klick erfolgt und es eine Canvas-Kontextvariable gibt (Canvas-Eingangs-Eigenschaften) und ein Nutzer:innen fünfmal in ein Canvas eintritt, nimmt Braze den fünften Eingang und verwendet diese Kontextvariable in der In-App-Nachricht.
- Ein Nutzer:innen kann jeweils nur 10 In-App-Nachrichten erhalten. Wenn ein Nutzer:innen zum Beispiel für 10 In-App-Nachrichten verschiedene Canvas-Schritte durchläuft, können Sie nur bis zu 10 dieser Schritte haben.
