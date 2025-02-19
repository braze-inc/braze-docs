---
nav_title: In-App-Nachrichten
article_title: In-App-Nachrichten in Canvas
alias: "/canvas_in-app_messages/"
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt die Features und Nuancen von Canvas-In-App-Nachrichten, die Sie zu Ihrem Canvas hinzufügen können, um umfangreiche Nachrichten zu senden."
tool: Canvas
channel: in-app messages

---

# In-App-Nachrichten in Canvas

> In-App-Nachrichten können als Teil Ihrer Canvas-Journey hinzugefügt werden, um Rich-Messaging anzuzeigen, wenn Ihr:e Kund:in eine Interaktion mit Ihrer App durchführt. Dieser Artikel beschreibt die Features und Feinheiten von Canvas In-App-Nachrichten.

Bevor Sie fortfahren, sollten Sie bereits [Ihr Canvas erstellt]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) und die Optionen für Verzögerung und Zielgruppe eingerichtet haben. 

Jetzt können Sie eine In-App-Nachricht zu Ihrem Canvas hinzufügen. Schritt [Nachricht]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) hinzufügen und wählen Sie **In-App-Nachricht** für Ihren **Nachrichtenkanal**. Nachdem alle Verzögerungen verstrichen sind und die Optionen für die Zielgruppe aktiviert wurden, wird die In-App-Nachricht live geschaltet und Nutzer:innen sehen sie, wenn sie die App öffnen. In-App-Nachrichten in Canvas können nur durch das Trigger-Ereignis `start session` ausgelöst werden – sie können nicht durch angepasste Ereignisse in einer Canvas-Komponente getriggert werden.

Bei Canvas-Schritten mit einem durch eine Aktion getriggerter Entry können Nutzer:innen den Canvas mitten in der Sitzung betreten. Wie bereits erwähnt, werden In-App-Nachrichten jedoch erst bei Beginn der nächsten Sitzung getriggert. Diese Nutzer:innen würden also die erste In-App-Nachricht verpassen, da sie nicht berechtigt waren, den Canvas vor Beginn der Sitzung zu betreten.

Sie können selbst bestimmen, [wann Ihre Nachricht abläuft](#in-app-message-expiration) und welches [Verhalten](#advancement-behavior-options) sie haben wird.

## Ablauf von In-App-Nachrichten

Im In-App-Nachrichten-Editor können Sie festlegen, wann die In-App-Nachricht abläuft. Während dieser Zeit bleibt die In-App-Nachricht stehen und wartet darauf, angesehen zu werden, bis sie das Ablaufdatum erreicht hat. Nachdem die In-App-Nachricht gesendet wurde, kann sie einmalig angesehen werden.

![][1]

| Option | Beschreibung | Beispiel |
|---|---|---|
| Nachricht läuft nach einer bestimmten Zeit ab | Mit der ersten Option können Sie die In-App-Nachricht in Abhängigkeit von dem Zeitpunkt ablaufen lassen, an dem der Schritt für den oder die Nutzer:in verfügbar wird. | Eine In-App-Nachricht mit einer Ablauffrist von zwei Tagen wäre beispielsweise erst verfügbar, wenn die Verzögerungszeit des Schritts verstrichen ist und die Optionen für die Zielgruppe überprüft wurden. Sie wäre dann für 2 Tage (48 Stunden) verfügbar und während dieser zwei Tage könnten die Nutzer die In-App-Nachricht sehen, wenn sie die App öffnen. |
| Nachricht läuft bis zu einem bestimmten Datum ab | Mit der zweiten Option können Sie ein bestimmtes Datum und eine bestimmte Uhrzeit wählen, zu der die In-App-Nachricht nicht mehr verfügbar sein wird. | Wenn Sie z.B. ein Angebot haben, das zu einem bestimmten Datum und einer bestimmten Uhrzeit endet, können Sie diese Option wählen, damit die Nutzer die zugehörige In-App-Nachricht nicht mehr sehen, wenn das Angebot endet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Anwendungsfälle

Wann sollten Sie diese Funktion nutzen? Braze empfiehlt Ihnen dringend, dieses Feature in Ihren Canvase für Aktionen und Onboarding zu verwenden.

{% tabs %}
  {% tab Aktionen %}

Aktionen, Gutscheine und Verkäufe haben oft ein festes Verfallsdatum. Die folgende Leinwand soll Ihre Nutzer zu den günstigsten Zeitpunkten auf eine Werbeaktion aufmerksam machen, die sie nutzen und vielleicht zu einem Kauf führen kann. Diese Aktion läuft am 28\. Februar 2019 um 11:15 Uhr in der Zeitzone des Unternehmens ab.

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

Wie Sie sehen können, laufen die In-App-Nachrichten ab, wenn die Aktion abläuft, um Diskrepanzen zwischen dem Messaging und dem Kundenerlebnis zu vermeiden.

  {% endtab %}
  {% tab Onboarding von Nutzer:innen %}

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

Wie Sie sehen können, sind die Push-Nachrichten um eine In-App-Nachricht herum angeordnet, um sicherzustellen, dass der Benutzer die App besucht und mit dem Onboarding begonnen hat. So vermeiden Sie lästigen Spam oder unpassende Nachrichten, die Benutzer davon abhalten könnten, Ihre App zu besuchen, und schaffen stattdessen eine fließende, sinnvolle Reihenfolge für ihre ersten Erfahrungen mit Ihrer App.

  {% endtab %}
{% endtabs %}

## Optionen für Fortschrittsverhalten

### Canvas Flow

In Canvas Flow bringen die Nachrichtenkomponenten automatisch alle Nutzer:innen voran, die den Schritt aufrufen. Es ist nicht erforderlich, das Verhalten des Nachrichtenfortschritts anzugeben, wodurch die Konfiguration des Gesamtschritts vereinfacht wird. Wenn Sie die Option **Weiterleiten, wenn Nachricht gesendet wurde** implementieren möchten, fügen Sie einen separaten [Zielgruppenpfad]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) hinzu, um Benutzer zu filtern, die den vorherigen Schritt nicht erhalten haben.

### Original Canvas Editor

{% alert important %}
Ab dem 28\. Februar 2023 können Sie keine Canvase mehr mit dem Original-Editor erstellen oder duplizieren. In diesem Abschnitt können Sie referenzieren, wie das Fortschrittsverhalten bei Schritten mit In-App-Nachrichten funktioniert.
{% endalert %}

Für Canvase, die im Original-Editor erstellt wurden, müssen Sie ein Fortschrittsverhalten festlegen – die Kriterien für den Fortschritt durch Ihre Canvas-Komponente. [Schritte mit ausschließlich In-App-Nachrichten](#steps-iam-only) haben andere Fortschrittsoptionen als [Schritte mit mehreren Nachrichtentypen](#steps-multiple-channels) (Push, E-Mail usw.). Für In-App-Nachrichten in einem Canvas Flow-Workflow ist diese Option so eingestellt, dass die Zielgruppe immer sofort weitergeschaltet wird.

Die aktionsbasierte Zustellung ist für Canvas-Schritte mit In-App-Nachrichten nicht verfügbar. Canvas-Schritte mit In-App-Nachrichten müssen geplant werden. Stattdessen erscheinen die In-App-Nachrichten von Canvas das erste Mal, wenn Ihr:e Nutzer:in die App öffnet (getriggert durch die Startsitzung), nachdem die geplante Nachricht in der Canvas-Komponente an ihn oder sie gesendet wurde.

Wenn Sie mehrere In-App-Nachrichten in einem Canvas haben, muss ein Benutzer mehrere Sitzungen starten, um jede dieser einzelnen Nachrichten zu erhalten.

{% alert important %}
In-App-Nachrichten können nicht durch Ereignisse in Canvas ausgelöst werden.
{% endalert %}

![][2]

{% alert important %}
Wenn **Voranbringen, wenn In-App-Nachricht live ist** ausgewählt ist, bleibt die In-App-Nachricht so lange verfügbar, bis sie abläuft, auch wenn der oder die Nutzer:in die nachfolgenden Schritte übergegangen ist. Wenn Sie nicht möchten, dass die In-App-Nachricht live ist, wenn die nächsten Schritte im Canvas zugestellt werden, stellen Sie sicher, dass die Ablaufzeit kürzer ist als die Verzögerung der nachfolgenden Schritte.
{% endalert %}

#### Schritte mit mehreren Kanälen {#steps-multiple-channels}

Schritte mit einer In-App-Nachricht und einem anderen Kanal haben die folgenden Fortschrittsmöglichkeiten:

| Option | Beschreibung |
|---|---|---|
| Voranbringen, wenn Nachricht gesendet wird | Die Benutzer müssen eine E-Mail, einen Webhook oder eine Push-Benachrichtigung erhalten oder die In-App-Nachricht sehen, um zu den nächsten Schritten im Canvas zu gelangen.  <br> <br>  Wenn die In-App-Nachricht abläuft und der Benutzer die E-Mail, den Webhook oder die Push-Nachricht nicht erhalten oder die In-App-Nachricht nicht angesehen hat, verlässt er den Canvas und geht nicht zu den nächsten Schritten über. |
| Zielgruppe sofort voranbringen | Jeder in der Zielgruppe des Schritts bringt nach Ablauf der Verzögerung die nächsten Schritte voran, unabhängig davon, ob er oder sie die notierte Nachricht gesehen hat oder nicht.  <br> <br> Nutzer:innen müssen mit den Segmentierungs- und Filterkriterien des Schritts übereinstimmen, um die nächsten Schritte vorbringen zu können. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][3]

{% alert important %}
Wenn die Option **Gesamte Zielgruppe** ausgewählt ist, bleibt die In-App-Nachricht bis zum Ablauf der Frist verfügbar, auch wenn der Benutzer zu den nachfolgenden Schritten übergeht. Wenn Sie nicht möchten, dass die In-App-Nachricht live ist, wenn die nächsten Schritte im Canvas zugestellt werden, stellen Sie sicher, dass die Ablaufzeit kürzer ist als die Verzögerung der nachfolgenden Schritte.
{% endalert %}

## Priorisierung von In-App-Nachrichten

Ein Kunde kann gleichzeitig zwei In-App-Nachrichten in Ihrem Canvas auslösen. In diesem Fall hält sich Braze an die folgende Prioritätsreihenfolge, um zu bestimmen, welche In-App-Nachricht angezeigt wird. Ziehen Sie verschiedene Canvas-Schritte, um ihre Priorität neu zu ordnen. Standardmäßig werden frühere Schritte in einer Canvas-Variante vor späteren Schritten angezeigt.

![]({% image_buster /assets/img_archive/step_priority.png %}){: style="max-width:80%"}

Navigieren Sie zu den **Sendeeinstellungen** des Abschnitts Canvas, um In-App-Nachrichten von einem Canvas gegenüber In-App-Nachrichten von anderen Canvases und Kampagnen zu priorisieren.

![]({% image_buster /assets/img_archive/canvas_send_settings.png %})

Standardmäßig ist die Priorität der Canvas-Komponenten auf mittel eingestellt, wobei die zuletzt erstellten Schritte die höchste relative Priorität haben. Die Prioritäten auf Leinwand- und Kampagnenebene sind ebenfalls standardmäßig auf mittel eingestellt, wobei die höchste relative Priorität den zuletzt erstellten Objekten zugewiesen wird.

![]({% image_buster /assets/img_archive/canvas_priority.png %}){: style="max-width:85%"}

### Entwürfe eines aktiven Canvas

Wenn Sie einen Entwurf eines aktiven Canvas bearbeiten, werden Änderungen an der In-App-Nachrichtenpriorität in den **Sendeeinstellungen** nicht mit einem Entwurf gespeichert. Diese Änderungen werden direkt auf das aktive Canvas angewendet, wenn das Modal für die Prioritätensortierung geschlossen wird. In einem Nachrichten-Schritt wird die Prioritätssortierung jedoch aktualisiert, wenn ein:e Nutzer:in den Entwurf startet, da die Schritt-Einstellungen auf Schritt-Ebene gelten.

## Benutzerdefinierte Ereigniseigenschaften in einem Canvas

Da die aktionsbasierte Zustellung für Canvas-Schritte mit In-App-Nachrichten nicht verfügbar ist, können Sie auch keine angepassten Event-Eigenschaften für diese Schritte verwenden. Zur Vorlage von Event-Eigenschaften in Canvas empfehlen wir Ihnen, Ihre Event-Eigenschaften als angepasste Attribute in Ihrem ersten Canvas-Schritt zu speichern und dann Ihre In-App-Nachricht im zweiten Schritt mit den angepassten Attributen zu personalisieren.


[1]: {% image_buster /assets/img/expires-after.png %} "IAM Live"
[2]: {% image_buster /assets/img/iam-advancement-behavior.png %} "IAM Live"
[3]: {% image_buster /assets/img/push-advancement-behavior.png %} "IAM Live"
