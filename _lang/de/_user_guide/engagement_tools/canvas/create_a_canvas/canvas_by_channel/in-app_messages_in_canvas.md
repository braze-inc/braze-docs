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

 

## Hinzufügen einer In-App-Nachricht zu Ihrer Nutzer:innen-Reise

Um eine In-App-Nachricht zu Ihrem Canvas hinzuzufügen, gehen Sie wie folgt vor:

1. Fügen Sie Ihrer Nutzer:innen-Reise einen Schritt für [Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) hinzu.
2. Wählen Sie **In-App-Nachricht** für Ihren **Messaging-Kanal**. 
3. Legen Sie fest, [wann Ihre Nachricht abläuft](#in-app-message-expiration) und welches [Vorbringungsverhalten](#advancement-behavior-options) sie haben wird.

## 



  

Bei Canvas-Schritten mit einem durch eine Aktion getriggerter Entry können Nutzer:innen den Canvas mitten in der Sitzung betreten. 

## Ablauf von In-App-Nachrichten

  Nachdem die In-App-Nachricht gesendet wurde, kann sie einmalig angesehen werden.



| Option | Beschreibung | Beispiel |
|---|---|---|
|  |  |  Sie wäre dann für 2 Tage (48 Stunden) verfügbar und während dieser zwei Tage könnten die Nutzer die In-App-Nachricht sehen, wenn sie die App öffnen. |
|  |  |  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Anwendungsfälle



{% tabs %}
  {% tab Aktionen %}

Aktionen, Gutscheine und Verkäufe haben oft ein festes Verfallsdatum. Die folgende Leinwand soll Ihre Nutzer zu den günstigsten Zeitpunkten auf eine Werbeaktion aufmerksam machen, die sie nutzen und vielleicht zu einem Kauf führen kann. 

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

 

  {% endtab %}
{% endtabs %}


## Priorisierung von In-App-Nachrichten

 In diesem Fall hält sich Braze an die folgende Prioritätsreihenfolge, um zu bestimmen, welche In-App-Nachricht angezeigt wird. 

 Standardmäßig werden frühere Schritte in einer Canvas-Variante vor späteren Schritten angezeigt. 



### 

  

## 

  

 





Sie können Canvase nicht mehr mit dem Original-Editor erstellen oder duplizieren. In diesem Abschnitt können Sie referenzieren, wie das Fortschrittsverhalten bei Schritten mit In-App-Nachrichten funktioniert.

Für Canvase, die im Original-Editor erstellt wurden, müssen Sie ein Fortschrittsverhalten festlegen – die Kriterien für den Fortschritt durch Ihre Canvas-Komponente.  Für In-App-Nachrichten in einem Canvas Flow-Workflow ist diese Option so eingestellt, dass die Zielgruppe immer sofort weitergeschaltet wird.

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

## 



-  
-  
-  

   





- 
- 
- 
- 
- 

## Benutzerdefinierte Ereigniseigenschaften in einem Canvas

 

## 



- 
- 
-  
