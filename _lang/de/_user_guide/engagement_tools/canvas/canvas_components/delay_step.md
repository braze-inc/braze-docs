---
nav_title: Delay 
article_title: Delay 
alias: "/delay_step/"
page_order: 8
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie eine Verzögerung zu Ihrem Canvas hinzufügen können, ohne eine zugehörige Nachricht hinzufügen zu müssen."
tool: Canvas

---

# Delay

> Mit Delay-Komponenten können Sie einem Canvas eine eigenständige Verzögerung hinzufügen. Sie können eine Verzögerung zu Ihrem Canvas hinzufügen, ohne eine zugehörige Nachricht hinzufügen zu müssen. 

Verzögerungen können Ihr Canvas übersichtlicher gestalten. Sie können diese Komponente auch verwenden, um einen anderen Schritt bis zu einem genauen Datum, bis zu einem bestimmten Tag oder bis zu einem bestimmten Wochentag zu verschieben. Eine Delay-Komponente kann mit höchstens einem nachfolgenden Schritt verbunden werden. <br> ![Ein Delay-Schritt mit einer Verzögerung von einem Tag als erster Schritt eines Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Erstellen einer Verzögerung

Um eine Verzögerung zu erstellen, fügen Sie einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie die Delay-Komponente aus der Seitenleiste oder klicken Sie auf den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie dann **Delay**.

#### Erweiterte Verzögerungen

Sie können Delay-Schritte jetzt auf bis zu zwei Jahre verlängern. Wenn Sie beispielsweise neue Nutzer:innen für Ihre App onboarden, können Sie eine erweiterte Verzögerung von zwei Monaten einfügen, bevor Sie einen Nachrichten-Schritt senden, um die Nutzer:innen anzustupsen, die noch keine Sitzung gestartet haben.

## Zeitverzögerungstypen

Sie können die Art der Verzögerung vor der nächsten Nachricht in Ihrem Canvas auswählen. Sie können entweder eine Verzögerung festlegen, die bis nach einer bestimmten Zeitspanne andauert, oder Ihre Nutzer:innen bis zu einem bestimmten Datum und einer bestimmten Uhrzeit warten lassen.

{% tabs %}
{% tab Duration %}

Durch Auswahl von **Dauer** können Sie Nutzer:innen für eine bestimmte Anzahl von Sekunden, Minuten, Stunden, Tagen oder Wochen und zu einer bestimmten Uhrzeit zurückhalten. Sie können Nutzer:innen zum Beispiel vier Stunden oder einen Tag lang aufhalten.
  
Beachten Sie den Unterschied zwischen der Berechnung von „Tagen" und „Kalendertagen".
  
- Ein „Tag" entspricht 24 Stunden und wird ab dem Zeitpunkt berechnet, zu dem die Nutzer:in den Delay-Schritt betritt. 
- Ein „Kalendertag" bezeichnet die Wartezeit bis zum nächsten festgelegten Zeitpunkt, wobei dieser Zeitraum weniger als 24 Stunden betragen kann. Sie können wählen, ob die Verzögerung nach Unternehmenszeit oder nach der Ortszeit der Nutzer:innen berechnet werden soll. Wenn keine Zeit angegeben wird, wird die Nutzer:in bis Mitternacht des nächsten Tages in Unternehmenszeit verzögert.

Sie können auch **Zu einem bestimmten Zeitpunkt** auswählen, um festzulegen, wann die Nutzer:innen im Canvas vorankommen. Diese Option berücksichtigt den Zeitpunkt, zu dem die Nutzer:in den Delay-Schritt betreten hat. Wenn dieser Zeitpunkt über die in den Einstellungen konfigurierte Zeit hinausgeht, werden dem Delay weitere Stunden hinzugefügt. 

Nehmen wir beispielsweise an, heute ist der 11. Dezember und unser Delay-Schritt ist auf eine **Dauer** von einer Woche um 8 Uhr UTC eingestellt. Wenn eine Nutzer:in am 4. Dezember in den Delay-Schritt eintritt, würde sie heute aus dem Delay-Schritt entlassen, um ihre Journey fortzusetzen – vorausgesetzt, sie ist ursprünglich vor 8 Uhr UTC in den Delay-Schritt eingetreten. Wenn sie nach diesem Zeitpunkt in den Delay-Schritt eingetreten ist, wird sie bis zum nächsten Tag (dem nächsten Vorkommen dieses Zeitpunkts) verzögert. 

{% endtab %}
{% tab Calendar date %}

Durch Auswahl von **Kalenderdatum** können Sie Nutzer:innen bis zu einem bestimmten Datum und einer bestimmten Uhrzeit in diesem Schritt halten.

#### Überlegungen

##### Nutzer:innen erhalten keine veralteten Schritte oder Nachrichten

Wenn das ausgewählte Datum und die Uhrzeit bereits verstrichen sind, wenn die Nutzer:innen zum Delay-Schritt gelangen, verlassen sie den Canvas. Zwischen dem Beginn des Canvas und den für die Schritte „Warten bis zu einem bestimmten Tag" ausgewählten Daten können bis zu 31 Tage liegen.

{% alert important %}
Wenn Sie am [Early Access für Canvas Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) teilnehmen, können Sie Verzögerungen von bis zu zwei Jahren festlegen.
{% endalert %}

In diesen Szenarien erhalten Nutzer:innen zum Beispiel keine Schritte oder Nachrichten:

- Eine Nachricht soll am 3. Mai um 21 Uhr versendet werden, jedoch läuft der Delay-Schritt am 3. Mai um 9 Uhr ab. 
- Ein Canvas-Schritt verzögert sich bis zu einer bestimmten Zeit in der Ortszeit der Nutzer:in, aber die Nutzer:innen haben keine Zeitzone in ihrem Nutzerprofil eingestellt. Die Verzögerung wird dann standardmäßig auf die Zeitzone des Unternehmens für diese Nutzer:innen eingestellt, die die angegebene Zeit bereits überschritten hat. 
  
##### Nutzer:innen verlassen den Canvas, wenn ein nachfolgender Delay-Schritt innerhalb der Zeitlinie eines vorherigen Delay-Schritts liegt

Wenn der Canvas zwei Delay-Schritte aufweist, der erste Delay-Schritt jedoch länger ist als der zweite, werden die Nutzer:innen den Canvas ebenfalls verlassen. 

Nehmen wir an, ein Canvas hat diese Schritte:
- Schritt 1: Nachrichten-Schritt
- Schritt 2: Delay-Schritt bis 13. Dezember um 22 Uhr
- Schritt 3: Nachrichten-Schritt
- Schritt 4: Delay-Schritt bis 13. Dezember um 19 Uhr
- Schritt 5: Nachrichten-Schritt
  
Die Nutzer:innen, die Schritt 4 betreten, werden den Canvas verlassen, bevor sie Schritt 5 erhalten, da die Verzögerung von Schritt 4 Teil des Zeitrahmens von Schritt 2 ist.

{% endtab %}
{% tab Day of the week %}

Durch die Auswahl von **Wochentag** können Sie Nutzer:innen bis zu einem bestimmten Wochentag und einer bestimmten Uhrzeit in diesem Schritt halten. Sie können Nutzer:innen zum Beispiel bis zum nächsten Donnerstag um 16 Uhr in der Zeitzone des Unternehmens warten lassen. 

Um dies erfolgreich zu konfigurieren, müssen Sie auch festlegen, was passieren soll, wenn die Nutzer:in den Canvas am ausgewählten Wochentag (z. B. Donnerstag), aber nach der angegebenen Uhrzeit betritt. Sie können wählen, ob Sie die Nutzer:in noch am selben Tag voranbringen oder bis zur nächsten Woche zurückhalten.
{% endtab %}
{% endtabs %}

## Verwenden von Delay-Schritten

Nehmen wir an, es ist der 10. Juni. Am 11. Juni möchten Sie, dass die Nutzer:innen den Canvas betreten und eine Nachricht über eine bevorstehende Aktion erhalten. Dann möchten Sie die Nutzer:innen bis zum 17. Juni um 15 Uhr Ortszeit im Canvas halten. Am 17. Juni um 15 Uhr Ortszeit möchten Sie den Nutzer:innen eine Erinnerungsnachricht über die Aktion senden.

Die Abfolge der Canvas-Schritte könnte wie folgt aussehen:

1. Beginnen Sie mit dem Hinzufügen eines Nachrichten-Schritts, der sofort gesendet wird, nachdem Nutzer:innen am 11. Juni in den Canvas eingetreten sind.
2. Erstellen Sie einen Delay-Schritt, der Nutzer:innen bis 15 Uhr Ortszeit am 17. Juni hält.
3. Verknüpfen Sie den Delay-Schritt mit einem weiteren Nachrichten-Schritt, der seine Nachricht sofort sendet.

### Delay-Komponenten am Ende eines Canvas {#delay-as-last-step}

Wenn Sie Ihrem Canvas eine Delay-Komponente hinzufügen und es keine nachfolgenden Schritte gibt, wird jede Nutzer:in, die den letzten Schritt erreicht, automatisch aus dem Canvas herausgeführt. Dies gilt auch, wenn die Zeit des Delay-Schritts noch nicht erreicht ist. Das bedeutet, dass Nutzer:innen, die den Delay-Schritt bereits erreicht haben, keine Nachrichten erhalten, die Sie nach diesem Schritt hinzufügen. Wenn eine Nutzer:in jedoch den Delay-Schritt noch nicht erreicht hat und eine Nachricht hinzugefügt wird, würde sie diese Nachricht erhalten.

### Personalisierte Verzögerungen

{% multi_lang_include early_access_beta_alert.md feature='The personalized delays and extended delays feature' %}

Aktivieren Sie die Option **Verzögerung personalisieren**, um eine personalisierte Verzögerung für Ihre Nutzer:innen einzurichten. Sie können dies mit einem [Context-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) verwenden, um die Kontextvariable auszuwählen, nach der verzögert werden soll. Dadurch wird die im ausgewählten Attribut oder in der ausgewählten Eigenschaft festgelegte Tageszeit überschrieben. Dies ist nützlich, wenn Sie einen Versatz in Tagen oder Wochen anwenden und möchten, dass Nutzer:innen zu einem bestimmten Zeitpunkt fortfahren. Die Zeitzone wird aus dem Attribut oder der Eigenschaft abgeleitet. Falls keine verfügbar ist, wird der Fallback verwendet. 

#### Zeitzonenverhalten für „zu einer bestimmten Zeit"

Bei der Konfiguration personalisierter Verzögerungen mit der Option **Zu einer bestimmten Zeit** hängt das Zeitzonenverhalten vom Datentyp Ihres Attributs oder Ihrer Kontextvariablen ab:

- **String-Datentyp mit Zeitzone:** Wenn das Attribut oder die Kontextvariable ein String-Datentyp ist, der Zeitzoneninformationen enthält, wird die im String angegebene Zeitzone verwendet. Beispielsweise verwendet `2025-06-10T10:00:00-08:00` UTC-8.
- **String-Datentyp ohne Zeitzone:** Wenn das Attribut oder die Kontextvariable ein String-Datentyp ohne Zeitzoneninformationen ist, wird die Fallback-Zeitzone verwendet. Beispielsweise verwendet `2025-06-10` die Fallback-Zeitzone.
- **Datentyp „Zeit":** Wenn das Attribut oder die Kontextvariable ein Zeit-Datentyp ist, wird UTC verwendet. Dies liegt daran, dass der Datentyp „Zeit" beim Speichern in der Datenbank immer in UTC konvertiert wird, sodass „zu einer bestimmten Zeit" immer UTC referenziert, wenn die Variable auf den Datentyp „Zeit" gesetzt ist. Beispielsweise verwendet `2025-06-10T10:00:00-08:00` UTC+0.

{% alert note %}
Es ist möglich, dass ein angepasstes Attribut oder eine Kontextvariable weder eine bestimmte Zeit noch eine Zeitzone hat, wenn es sich um einen String-Datentyp handelt. Wenn es sich um einen Zeit-Datentyp handelt, müssen Sie die Uhrzeit und die Zeitzone angeben. Wenn das angepasste Attribut oder die Kontextvariable jedoch ein „irrelevanter" String ist (z. B. „product_name"), verlässt die Nutzer:in den Canvas.
{% endalert %}

#### Anwendungsfall

Nehmen wir an, Sie möchten Ihre Kund:innen daran erinnern, in 30 Tagen Zahnpasta zu kaufen. Mit einer Kombination aus einem Context-Schritt und einem Delay-Schritt können Sie diese Kontextvariable auswählen, nach der verzögert werden soll. In diesem Fall würde Ihr Context-Schritt die folgenden Felder enthalten:

- **Kontextvariablenname:** product_reminder_interval
- **Datentyp:** Zeit
- **Wert:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![Das „product_reminder_interval" und sein Wert.]({% image_buster /assets/img/context_step1.png %})

Da Sie Ihre Kund:innen in 30 Tagen erinnern möchten, wählen Sie als Nächstes **Bis zu einem bestimmten Tag** als Verzögerungsoption und aktivieren **Verzögerung personalisieren**, um die Informationen aus Ihrem Context-Schritt zu verwenden. Das bedeutet, dass Ihre Nutzer:innen bis zur ausgewählten Kontextvariablen verzögert werden.

## Delay-Analytics

Für Delay-Komponenten sind in der Analytics-Ansicht eines aktiven oder zuvor aktiven Canvas die folgenden Metriken verfügbar.

| Metrik | Beschreibung |
|---|---|
| _Eingetreten_ | Zeigt an, wie oft der Schritt betreten wurde. Wenn Ihr Canvas über eine erneute Qualifizierung verfügt und eine Nutzer:in zweimal in einen Delay-Schritt eintritt, werden zwei Einträge aufgezeichnet. |
| _Zum nächsten Schritt fortgefahren_ | Zeigt die Anzahl der Einträge an, die zum nächsten Schritt im Canvas weitergeleitet wurden. |
| _Canvas verlassen_ | Zeigt die Anzahl der Einträge an, die den Canvas verlassen haben und nicht zum nächsten Schritt weitergegangen sind. |
| _Personalisierung fehlgeschlagen_ | Gibt an, wie oft eine personalisierte Nachricht oder ein für eine Nutzer:in bestimmter Inhalt aus folgenden Gründen nicht zugestellt werden konnte:<br> {::nomarkdown}<ul><li>Verzögerungswert liegt in der Vergangenheit</li><li>Verzögerungswert liegt über 2 Jahre in der Zukunft</li><li><b>Nach einer Dauer</b>-Wert ist keine Zahl</li><li><b>Bis zu einem bestimmten Tag</b>-Wert ist kein Datum oder datumsformatierter String</li></ul>{:/} <br>Siehe [Fehler bei fehlgeschlagener Personalisierung](#personaliztion-failed-errors) für weitere Details. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Zeitreihen für diese Analytics sind in der erweiterten Komponentenansicht verfügbar.

## Fehlerbehebung

### Fehler bei fehlgeschlagener Personalisierung

Wenn Nutzer:innen keine personalisierte Verzögerung triggern, könnte das daran liegen, dass der Context-Schritt, den Sie festgelegt haben, um sie für den Delay-Schritt zu qualifizieren, nicht wie erwartet funktioniert. Wenn eine [Kontextvariable ungültig ist]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#troubleshooting), fährt eine Nutzer:in durch Ihr Canvas, ohne dass ihr Kontext durch den Context-Schritt festgelegt wurde. Dies kann dazu führen, dass sie sich nicht für spätere Schritte in Ihrem Canvas qualifizieren, z. B. für personalisierte Verzögerungen.