---
nav_title: Delay 
article_title: Delay 
alias: "/delay_step/"
page_order: 3
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie eine Verzögerung zu Ihrem Canvas hinzufügen können, ohne eine zugehörige Nachricht hinzufügen zu müssen."
tool: Canvas

---

# Delay

> Mit Delay-Komponenten können Sie einem Canvas eine eigenständige Verzögerung hinzufügen. Sie können eine Verzögerung zu Ihrem Canvas hinzufügen, ohne dass Sie eine zugehörige Nachricht hinzufügen müssen. 

Verzögerungen können Ihr Canvas sauberer aussehen lassen. Sie können diese Komponente auch verwenden, um einen anderen Schritt bis zu einem genauen Datum, bis zu einem bestimmten Tag oder bis zu einem bestimmten Wochentag zu verschieben. <br> ![][1]{: style="float:right;max-width:35%;margin-left:15px;"}

## Delay erstellen

Um einen Delay zu erstellen, fügen Sie einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie die Komponente Delay aus der Seitenleiste oder klicken Sie auf die Plus-Schaltfläche <i class="fas fa-plus-circle"></i> am unteren Rand eines Schritts und wählen Sie **Delay**.

Es gibt einige Details zu beachten, wenn Sie einen Delay in Ihrer Canvas-Journey erstellen.

- Die Frist beträgt 30 Tage.
- Eine Delay-Komponente kann nur mit einem nächsten Schritt verbunden werden.

### Personalisierte Verzögerungen

{% alert important %}
Personalisierte Verzögerungen und erweiterte Verzögerungen sind bereits verfügbar. Wenden Sie sich an Ihren Braze-Konto Manager:in, wenn Sie an der Teilnahme an diesem frühen Zugang interessiert sind.
{% endalert %}

Wählen Sie die Option **Verzögerung personalisieren** aus, um eine personalisierte Verzögerung für Ihre Nutzer:innen einzurichten. Sie können dies mit einem [Kontextschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) verwenden, um die Kontextvariable auszuwählen, um die Sie verzögern möchten.

Braze beendet einen Nutzer:innen bei diesem Schritt, wenn:

- Die Kontextvariable kehrt zu keinem Wert zurück.
- Ein eingebetteter Connected-Content-Aufruf schlägt fehl.
- Die Typen der Kontextvariablen stimmen nicht überein.

Nehmen wir an, wir möchten unsere Kund:innen daran erinnern, in 30 Tagen Zahnpasta zu kaufen. Mit einer Kombination aus einem Kontextschritt und einem Verzögerungsschritt können wir diese Kontextvariable auswählen, um die wir verzögern wollen. In diesem Fall würde unser Schritt Context die folgenden Felder enthalten:

- **Name der Kontextvariablen:** product_reminder_interval
- **Daten-Typ:** Uhrzeit
- **Wert:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![Das "product_reminder_interval" und sein Wert.][2]

Da wir unsere Kund:in in 30 Tagen erinnern möchten, wählen wir als nächstes **Bis zu einem bestimmten Tag** als Verzögerungsoption aus und wählen **Verzögerung personalisieren**, um die Informationen aus unserem Schritt Kontext zu verwenden. Das bedeutet, dass unsere Nutzer:in so lange verzögert werden, bis die gewählte Kontextvariable ausgewählt ist.

![Beispiel für die Verwendung von Kontextvariablen mit einem Verzögerungsschritt, um Nutzer:innen auf der Grundlage des "product_reminder_interval" zu verzögern.][3]

#### Erweiterte Verzögerungen

Sie können jetzt Verzögerungsstufen bis zu zwei Jahre verlängern. Wenn Sie z.B. neue Nutzer:innen für Ihre App onboarding, können Sie eine längere Verzögerung von zwei Monaten einfügen, bevor Sie eine Nachricht senden, um die Nutzer:innen, die noch keine Sitzung begonnen haben, anzustupsen.

### Optionen für die Zeitverzögerung

Sie können die Art der Verzögerung vor der nächsten Nachricht in Ihrem Canvas auswählen. Sie können entweder eine Verzögerung für Ihre Benutzer festlegen, die bis nach einer bestimmten Zeitspanne andauert, oder Ihre Benutzer bis zu einem bestimmten Datum und einer bestimmten Uhrzeit warten lassen.

{% tabs %}
  {% tab Nach einer gewissen Zeit %}

  Mit der Option **Nach einer Zeitspanne** können Sie Benutzer für eine bestimmte Anzahl von Sekunden, Minuten, Stunden, Tagen oder Wochen und zu einem bestimmten Zeitpunkt aufhalten. Sie können Nutzer:innen zum Beispiel vier Stunden oder einen Tag lang aufhalten.
  
  Beachten Sie den Unterschied zwischen der Berechnung von „Tagen“ und „Kalendertagen“.
  
    - A "day" is 24 hours and calculated from the time the user enters the Delay step. 
    - A "calendar day" defines a day as 24 hours after a specified time. When a calendar day is chosen and the time is specified, you can choose to delay at company time or at a user's local time. If a time isn't specified, the user will be delayed until midnight the next day in company time.

  Sie können auch **Zu einem bestimmten Zeitpunkt** auswählen, um festzulegen, wann die Nutzer:innen im Canvas zum nächsten Schritt übergehen. Diese Option berücksichtigt den Zeitpunkt, zu dem der oder die Nutzer:in zum Schritt „Delay“ übergegangen ist. Wenn diese Zeit über die in den Einstellungen konfigurierte Zeit hinausgeht, fügen wir dem Delay weitere Stunden hinzu. Nehmen wir zum Beispiel an, heute ist der 11\. Dezember und unser Delay-Schritt ist über **Nach einer gewissen Zeit** auf eine Woche um 8 Uhr UTC eingestellt. Wenn ein:e Nutzer:in am 4\. Dezember in den Delay-Schritt übergeht, verlässt er oder den Delay-Schritt, um seine oder ihre Journey heute fortzusetzen, wenn er oder sie ursprünglich zu einer Zeit vor 8 Uhr UTC in den Delay-Schritt übergegangen ist. Wenn der oder die Nutzer:in nach diesem Zeitpunkt in den Delay-Schritt übergegangen ist, wird er oder sie bis zum nächsten Tag (dem nächsten Vorkommen dieses Zeitpunkts) verzögert. 

  {% endtab %}
  {% tab Bis zu einem bestimmten Datum %}

  Mit der Option **Bis zu einem bestimmten Datum** können Sie Benutzer bis zu einem bestimmten Datum und einer bestimmten Uhrzeit in dem Schritt halten.

  {% alert important %}
  Wenn das ausgewählte Datum und die Uhrzeit bereits verstrichen sind, wenn die Nutzer:innen zum Schritt Verzögerung übergehen, verlassen sie den Canvas. Zwischen dem Start des Canvas und den für die Schritte "Warten bis zum genauen Datum" gewählten Daten können maximal 31 Tage liegen.
  {% endalert %}
  {% endtab %}
  {% tab Bis zu einem bestimmten Tag der Woche %}

  Mit der Option **Bis zu einem bestimmten Wochentag** können Sie Benutzer bis zu einem bestimmten Wochentag und zu einer bestimmten Uhrzeit in dem Schritt halten. Sie können Nutzer:innen zum Beispiel bis zum nächsten Donnerstag um 16 Uhr in der Zeitzone des Unternehmens warten lassen. 

  Um dies erfolgreich zu konfigurieren, müssen Sie auch festlegen, was passieren soll, wenn der Benutzer das Canvas am ausgewählten Wochentag (z. B. Donnerstag), aber nach der angegebenen Uhrzeit betritt. Sie können wählen, ob Sie die Nutzer:innen noch am selben Tag voranbringen oder bis zur nächsten Woche zurückhalten.
  {% endtab %}
{% endtabs %}

## Verwenden von Delay-Schritten

Nehmen wir an, es ist der 10\. Juni. Am 11\. Juni möchten Sie, dass die Benutzer den Canvas betreten und eine Nachricht über eine bevorstehende Werbeaktion erhalten. Dann wollen Sie die Benutzer bis zum 17\. Juni um 15 Uhr Ortszeit im Canvas halten. Am 17\. Juni um 15 Uhr Ortszeit möchten Sie den Nutzern eine Erinnerungsnachricht über die Aktion schicken.

Die Abfolge der Canvas-Schritte könnte wie folgt aussehen:

1. Beginnen Sie mit dem Hinzufügen eines Messaging-Schritts, der sofort gesendet wird, nachdem Nutzer:innen am 11\. Juni in das Canvas übergegangen sind.
2. Erstellen Sie einen Delay-Schritt, der Nutzer:innen bis 13 Uhr Ortszeit am 17\. Juni bindet.
3. Verknüpfen Sie den Delay-Schritt mit einem anderen Nachrichten-Schritt, der seine Nachricht sofort sendet.

### Verzögerungskomponenten am Ende eines Canvas {#delay-as-last-step}

Wenn Sie Ihrem Canvas eine Verzögerungskomponente hinzufügen, aber nach der Verzögerungskomponente keine weiteren Nutzer:innen mehr vorhanden sind, wird jeder Nutzer:innen, der den letzten Schritt erreicht, automatisch aus dem Canvas vorangebracht. Dies gilt auch, wenn die Zeit des Delay-Schritts noch nicht erreicht ist. Das bedeutet, dass Nutzer:innen, die die Verzögerungsstufe bereits erreicht haben, keine Nachrichten mehr erhalten, die Sie nach der Verzögerungsstufe hinzufügen. Wenn ein Nutzer:innen jedoch die Verzögerungsstufe noch nicht erreicht hat und eine Nachricht hinzugefügt wird, würde er diese Nachricht erhalten.

## Analyse der Verzögerung

Für Verzögerungen gibt es drei Statistiken, die in der Analyseansicht eines aktiven oder zuvor aktiven Canvas verfügbar sind.

| Metrisch | Beschreibung |
|---|---|
| `Entered` | Zeigt an, wie oft der Schritt bereits eingegeben wurde. Wenn Ihr Canvas über eine erneute Qualifizierung verfügt und ein:e Nutzer:in zweimal in einen Delay-Schritt übergeht, werden zwei Entrys aufgezeichnet. |
| `Proceeded to Next Step` | Zeigt die Anzahl der Einträge an, die zum nächsten Schritt im Canvas weitergeleitet wurden. |
| `Exited Canvas` | Zeigt die Anzahl der Einträge an, die den Canvas verlassen haben und nicht zum nächsten Schritt weitergegangen sind. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Zeitreihen für diese Analysen sind in der erweiterten Komponentenansicht verfügbar.

[1]: {% image_buster /assets/img/canvas_delay.png %}
[2]: {% image_buster /assets/img/context_step1.png %}
[3]: {% image_buster /assets/img/context_step2.png %}
