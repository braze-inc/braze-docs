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

Verzögerungen können Ihr Canvas sauberer aussehen lassen. Sie können diese Komponente auch verwenden, um einen anderen Schritt bis zu einem genauen Datum, bis zu einem bestimmten Tag oder bis zu einem bestimmten Wochentag zu verschieben. <br> ![Ein Verzögerungsschritt mit einer 1-tägigen Verzögerung als erster Schritt eines Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Erstellen einer Verzögerung

Um einen Delay zu erstellen, fügen Sie einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie die Komponente Delay aus der Seitenleiste oder klicken Sie auf die Plus-Schaltfläche <i class="fas fa-plus-circle"></i> am unteren Rand eines Schritts und wählen Sie **Delay**.

Es gibt einige Details zu beachten, wenn Sie einen Delay in Ihrer Canvas-Journey erstellen.

- Die Frist beträgt 30 Tage.
- Eine Delay-Komponente kann nur mit einem nächsten Schritt verbunden werden.

#### Erweiterte Verzögerungen

Sie können jetzt Verzögerungsstufen bis zu zwei Jahre verlängern. Wenn Sie z.B. neue Nutzer:innen für Ihre App onboarding, können Sie eine längere Verzögerung von zwei Monaten einfügen, bevor Sie eine Nachricht senden, um die Nutzer:innen, die noch keine Sitzung begonnen haben, anzustupsen.

## Zeitverzögerungsarten

Sie können die Art der Verzögerung vor der nächsten Nachricht in Ihrem Canvas auswählen. Sie können entweder eine Verzögerung für Ihre Benutzer festlegen, die bis nach einer bestimmten Zeitspanne andauert, oder Ihre Benutzer bis zu einem bestimmten Datum und einer bestimmten Uhrzeit warten lassen.

{% tabs %}
{% tab Duration %}

Wenn Sie **Dauer** auswählen, können Sie Nutzer:innen für eine bestimmte Anzahl von Sekunden, Minuten, Stunden, Tagen oder Wochen und zu einem bestimmten Zeitpunkt aufhalten. Sie können Nutzer:innen zum Beispiel vier Stunden oder einen Tag lang aufhalten.
  
Beachten Sie den Unterschied zwischen der Berechnung von „Tagen“ und „Kalendertagen“.
  
- Ein "Tag" umfasst 24 Stunden und wird ab dem Zeitpunkt berechnet, an dem der Nutzer:innen den Schritt Verzögerung eingibt. 
- Ein "Kalendertag" definiert die Wartezeit bis zur nächsten angegebenen Zeit, die weniger als 24 Stunden betragen kann. Sie können wählen, ob die Verzögerung zur Unternehmenszeit oder zur Ortszeit des Nutzers:innen erfolgen soll. Wenn keine Zeit angegeben wird, wird der Nutzer:in bis Mitternacht des nächsten Tages in Firmenzeit verschoben.

Sie können auch **Zu einem bestimmten Zeitpunkt** auswählen, um festzulegen, wann die Nutzer:innen im Canvas zum nächsten Schritt übergehen. Diese Option berücksichtigt den Zeitpunkt, zu dem der oder die Nutzer:in zum Schritt „Delay“ übergegangen ist. Wenn diese Zeit über die in den Einstellungen konfigurierte Zeit hinausgeht, fügen wir dem Delay weitere Stunden hinzu. 

Nehmen wir zum Beispiel an, heute ist der 11\. Dezember und unser Verzögerungsschritt ist auf **Dauer** einer Woche um 8 Uhr UTC eingestellt. Wenn ein:e Nutzer:in am 4\. Dezember in den Delay-Schritt übergeht, verlässt er oder den Delay-Schritt, um seine oder ihre Journey heute fortzusetzen, wenn er oder sie ursprünglich zu einer Zeit vor 8 Uhr UTC in den Delay-Schritt übergegangen ist. Wenn der oder die Nutzer:in nach diesem Zeitpunkt in den Delay-Schritt übergegangen ist, wird er oder sie bis zum nächsten Tag (dem nächsten Vorkommen dieses Zeitpunkts) verzögert. 

{% endtab %}
{% tab Calendar date %}

Wenn Sie **das Kalenderdatum** auswählen, können Sie Nutzer:innen bis zu einem bestimmten Datum und einer bestimmten Uhrzeit im Schritt halten.

#### Überlegungen

##### Nutzer:innen erhalten keine veralteten Schritte oder Nachrichten mehr

Wenn das ausgewählte Datum und die Uhrzeit bereits verstrichen sind, wenn die Nutzer:innen zum Schritt Verzögerung übergehen, verlassen sie den Canvas. Es können bis zu 31 Tage zwischen dem Start des Canvas und den Daten liegen, die für die Schritte "Warten bis zu einem bestimmten Tag" gewählt wurden.

{% alert important %}
Wenn Sie am [Canvas Context Frühzugang]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) teilnehmen, können Sie Verzögerungen von bis zu 2 Jahren festlegen.
{% endalert %}

In diesen Szenarien erhalten Nutzer:innen zum Beispiel keine Schritte oder Nachrichten:

- Eine Nachricht soll am 3\. Mai um 21 Uhr gesendet werden, aber der Schritt Verzögerung läuft am 3\. Mai um 9 Uhr ab. 
- Ein Canvas-Schritt verzögert sich bis zu einer bestimmten Zeit in der Ortszeit des Nutzers, aber die Nutzer:innen haben keine Zeitzone in ihrem Nutzerprofil eingestellt. Die Verzögerung wird dann standardmäßig auf die Zeitzone des Unternehmens für diese Nutzer:innen eingestellt, die die angegebene Zeit bereits überschritten hat. 
  
##### Nutzer:innen verlassen das Programm, wenn ein nachfolgender Verzögerungsschritt innerhalb der Zeitlinie eines vorherigen Verzögerungsschritts liegt.

Wenn der Canvas zwei Verzögerungsschritte hat, aber der erste Verzögerungsschritt länger ist als der zweite, werden Nutzer:innen den Canvas ebenfalls verlassen. 

Nehmen wir an, ein Canvas hat diese Schritte:
- Schritt 1: Nachrichtenschritt
- Schritt 2: Verzögerungsstufe bis 13\. Dezember um 10 Uhr
- Schritt 3: Nachrichtenschritt
- Schritt 4: Verzögerungsstufe bis 13\. Dezember um 19 Uhr
- Schritt 5: Nachrichtenschritt
  
Die Nutzer:innen von Schritt 4 werden den Canvas verlassen, bevor sie Schritt 5 erhalten, da die Verzögerung von Schritt 4 Teil des Zeitrahmens von Schritt 2 ist.

{% endtab %}
{% tab Day of the week %}

Wenn Sie den **Wochentag** auswählen, können Sie Nutzer:innen bis zu einem bestimmten Wochentag und zu einer bestimmten Uhrzeit im Schritt halten. Sie können Nutzer:innen zum Beispiel bis zum nächsten Donnerstag um 16 Uhr in der Zeitzone des Unternehmens warten lassen. 

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

Wenn Sie Ihrem Canvas eine Verzögerungskomponente hinzufügen und es keine weiteren Schritte gibt, wird jeder Nutzer:innen, der den letzten Schritt erreicht, automatisch aus dem Canvas vorangebracht. Dies gilt auch, wenn die Zeit des Delay-Schritts noch nicht erreicht ist. Das bedeutet, dass Nutzer:innen, die den Schritt Verzögerung bereits erreicht haben, keine Nachrichten mehr erhalten, die Sie nach diesem Schritt hinzufügen. Wenn ein Nutzer:innen jedoch die Verzögerungsstufe noch nicht erreicht hat und eine Nachricht hinzugefügt wird, würde er diese Nachricht erhalten.

### Personalisierte Verzögerungen

{% alert important %}
Personalisierte Verzögerungen und erweiterte Verzögerungen sind bereits verfügbar. Wenden Sie sich an Ihren Braze-Konto Manager:in, wenn Sie an der Teilnahme an diesem frühen Zugang interessiert sind.
{% endalert %}

Wählen Sie die Option **Verzögerung personalisieren** aus, um eine personalisierte Verzögerung für Ihre Nutzer:innen einzurichten. Sie können dies mit einem [Kontextschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) verwenden, um die Kontextvariable auszuwählen, um die Sie verzögern möchten. Dadurch wird die in dem ausgewählten Attribut oder der Eigenschaft eingestellte Tageszeit außer Kraft gesetzt. Dies ist nützlich, wenn Sie einen Versatz in Tagen oder Wochen anwenden und die Nutzer:innen zu einem bestimmten Zeitpunkt nach vorne gehen sollen. Die Zeitzone stammt aus dem Attribut oder der Eigenschaft oder verwendet den Fallback, wenn keiner verfügbar ist. 

#### Zeitzonenverhalten für "zu einer bestimmten Zeit"

Wenn Sie personalisierte Verzögerungen mit der Option **zu einer bestimmten Zeit** konfigurieren, hängt das Zeitzonenverhalten vom Datentyp Ihres Attributs oder Ihrer Kontextvariablen ab:

- **String-Datentyp mit Zeitzone:** Wenn es sich bei dem Attribut oder der Kontextvariablen um einen String-Datentyp handelt, der Zeitzoneninformationen enthält, entspricht sie der im String angegebenen Zeitzone. Zum Beispiel verwendet `2025-06-10T10:00:00-08:00` UTC-8.
- **String-Datentyp ohne Zeitzone:** Wenn es sich bei dem Attribut oder der Kontextvariablen um einen String-Datentyp ohne Zeitzoneninformationen handelt, entspricht er der Fallback-Zeitzone. Zum Beispiel verwendet `2025-06-10` die Fallback-Zeitzone.
- **Typ der Zeitdaten:** Wenn es sich bei dem Attribut oder der Kontextvariablen um einen Zeitdatentyp handelt, entspricht er der UTC. Das liegt daran, dass der Datentyp "Zeit" immer in UTC konvertiert wird, wenn er in der Datenbank gespeichert wird. Daher referenziert "zu einer bestimmten Zeit" immer UTC, wenn die Variable auf den Datentyp "Zeit" gesetzt ist. Zum Beispiel verwendet `2025-06-10T10:00:00-08:00` UTC+0.

{% alert note %}
Es ist möglich, dass ein angepasstes Attribut oder eine Kontextvariable weder eine bestimmte Zeit noch eine Zeitzone hat, wenn es sich um einen String-Datentyp handelt. Wenn es sich um einen Datentyp mit Zeitangaben handelt, müssen Sie die Uhrzeit und die Zeitzone angeben. Handelt es sich bei dem angepassten Attribut oder der Kontextvariablen jedoch um einen "irrelevanten" String (wie "product_name"), ), verlässt der Nutzer:innen den Canvas.
{% endalert %}

#### Anwendungsfall

Nehmen wir an, Sie möchten Ihre Kund:innen daran erinnern, in 30 Tagen Zahnpasta zu kaufen. Mit einer Kombination aus einem Kontextschritt und einem Verzögerungsschritt können Sie diese Kontextvariable auswählen, um die verzögert werden soll. In diesem Fall würde Ihr Schritt Kontext die folgenden Felder enthalten:

- **Name der Kontextvariable:** product_reminder_interval
- **Daten-Typ:** Uhrzeit
- **Wert:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![Die "product_reminder_interval" und ihr Wert.]({% image_buster /assets/img/context_step1.png %})

Da Sie Ihre Kund:in in 30 Tagen erinnern möchten, wählen Sie als nächstes **Bis zu einem bestimmten Tag** als Verzögerungsoption aus und wählen **Verzögerung personalisieren**, um die Informationen aus Ihrem Schritt Kontext zu verwenden. Das bedeutet, dass Ihre Nutzer:in so lange verzögert werden, bis die ausgewählte Kontextvariable ausgewählt ist.

## Analyse der Verzögerung

Für Verzögerungskomponenten sind in der Analytics-Ansicht eines aktiven oder zuvor aktiven Canvas die folgenden Metriken verfügbar.

| Metrisch | Beschreibung |
|---|---|
| _Eingetreten_ | Zeigt an, wie oft der Schritt bereits eingegeben wurde. Wenn Ihr Canvas über eine erneute Qualifizierung verfügt und ein:e Nutzer:in zweimal in einen Delay-Schritt übergeht, werden zwei Entrys aufgezeichnet. |
| _Fortgefahren mit nächstem Schritt_ | Zeigt die Anzahl der Einträge an, die zum nächsten Schritt im Canvas weitergeleitet wurden. |
| _Canvas wurde verlassen_ | Zeigt die Anzahl der Einträge an, die den Canvas verlassen haben und nicht zum nächsten Schritt weitergegangen sind. |
| _Personalisierung fehlgeschlagen_ | Gibt an, wie oft eine personalisierte Nachricht oder ein für einen Nutzer:innen bestimmter Inhalt aus folgenden Gründen nicht zugestellt werden konnte:<br> {::nomarkdown}<ul><li>Verzögerungswert liegt in der Vergangenheit</li><li>Der Verzögerungswert liegt über 2 Jahre in der Zukunft</li><li><b>Nachdem ein Dauerwert</b> keine Zahl ist</li><li><b>Bis ein bestimmter Tageswert</b> kein Datum oder ein datumsformatierter String ist</li></ul>{:/} <br>Siehe [Fehler bei der Personalisierung](#personaliztion-failed-errors) für weitere Details. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Zeitreihen für diese Analysen sind in der erweiterten Komponentenansicht verfügbar.

## Fehlersuche

### Fehler bei der Personalisierung

Wenn Nutzer:innen keine personalisierte Verzögerung triggern, könnte das daran liegen, dass der Kontextschritt, den Sie festgelegt haben, um sie für den Verzögerungsschritt zu qualifizieren, nicht wie erwartet funktioniert. Wenn eine [Kontextvariable ungültig ist]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#troubleshooting), fährt ein Nutzer:in durch Ihr Canvas, ohne dass sein Kontext durch den Context-Schritt festgelegt wurde. Dies kann dazu führen, dass sie sich nicht für spätere Schritte in Ihrem Canvas qualifizieren, z. B. für personalisierte Verzögerungen.

