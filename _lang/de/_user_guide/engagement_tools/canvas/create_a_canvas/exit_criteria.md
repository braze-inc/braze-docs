---
nav_title: Ausstiegskriterien
article_title: Exit-Kriterien 
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Dieser Artikel referenziert die Ausstiegskriterien und wie Nutzer:innen Ihr Canvas auf der Grundlage der ausgewählten Kriterien verlassen können."
tool: Canvas
---

# Ausstiegskriterien

> Indem Sie Ausnahme-Events direkt zu Ihren Canvas-Eingangsregeln hinzufügen, können Ihre Nutzer:innen Ihr Canvas verlassen, sobald das Ereignis am Ende des Schritts eintritt. Dies ermöglicht ein gezielteres Targeting des Messagings auf Canvas bei Ihrer Zielgruppe.

### Wie Nutzer:innen aussteigen

Nach der Ausführung des Exit-Ereignisses werden die Nutzer:innen aus dem Canvas verlassen, sobald der Schritt, in dem sie sich gerade befinden, beendet wurde. Wenn sich ein Nutzer:innen beispielsweise 30 Tage lang in einem Delay-Schritt befindet und das Exit-Ereignis am ersten Tag des Delay-Schrittes ausführt, wird der Nutzer:innen den Canvas erst nach 29 Tagen verlassen.

Betrachten wir ein weiteres Beispiel für die Verwendung von zeitbasierten Ausstiegskriterien. Ein Nutzer:innen gibt einen Verzögerungsschritt ein, der auf 24 Stunden am 1\. Juli um 12 Uhr eingestellt ist. In dieser Verzögerungszeit führen sie das Exit-Event "Letzter Kauf vor weniger als 1 Stunde" um 3 Uhr morgens aus. Dieser Nutzer:innen wird am 2\. Juli um 12 Uhr, also am Ende der Laufzeit des Verzögerungsschritts, auf die Ausstiegskriterien geprüft. Da seit ihrem Kauf am 1\. Juli um 3 Uhr morgens 21 Stunden vergangen sind, werden sie den Canvas nicht verlassen, weil sie innerhalb der einen Stunde nach Verlassen des Verzögerungsschritts am 2\. Juli keinen Kauf getätigt haben. Dies wirkt sich auf die "Gesamtausgänge nach Ausstiegskriterien" in Ihren Canvas Analytics aus, die erst aktualisiert werden, wenn ein Nutzer:innen den Canvas vollständig verlassen hat.

## Festlegung von Ausstiegskriterien

Im Schritt **Zielgruppe** des Canvas-Erstellers können Sie Ausstiegskriterien festlegen, um die Nutzer zu identifizieren, die Ihr Canvas verlassen sollen. 

Das Ausstiegskriterium enthält ein Ausnahme-Event, d.h. die spezifische Aktion, die Nutzer:innen zum Verlassen des Canvas veranlassen kann.

![Die Ausstiegskriterien, die eingerichtet wurden, um Nutzer:innen, die Produkte angesehen, aber noch nicht in den Warenkorb gelegt oder eine Bestellung aufgegeben haben, wieder zu engagieren.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Ausnahme-Events auswählen {#exception-events}

Wenn ein Nutzer:innen das Ausnahme-Event ausführt, verlässt er den Canvas. Beachten Sie, dass Ausnahme-Events nur dann Ausgänge triggern, wenn sich ein Nutzer:innen im Canvas befindet und den Fortschritt durch die User Journey voranbringt.

Nehmen wir an, Sie haben ein Canvas eingerichtet, um ein neues Produkt zu bewerben. In diesem Fall wäre der Kauf des Produkts das Ausnahme-Event. Auf diese Weise erhalten Nutzer:innen nach dem Kauf keine weiteren Nachrichten über ein Produkt, das sie bereits gekauft haben. Ausnahme-Events halten Ihre Nachrichten relevant und personalisiert.

Weitere Ausnahmeereignisse sind:

- Einen Kauf tätigen
- Eine Sitzung starten
- Ausführen eines benutzerdefinierten Ereignisses
- Durchführen eines Konversions-Events
- Hinzufügen einer E-Mail-Adresse
- Ändern eines benutzerdefinierten Attributwerts
- Update eines Abo-Status
- Aktualisieren des Status einer Abonnementgruppe
- Mit einer Kampagne interagieren
- Einen Standort eingeben
- Triggern eines Geofence
- Versenden einer eingehenden SMS-Nachricht
- Versenden einer eingehenden WhatsApp-Nachricht
- Versenden einer eingehenden LINE-Nachricht
- Durchführen eines Warenkorb-aktualisiert-Events
- Durchführen eines "Checkout abgeschlossen"-Events
- Durchführen eines "Checkout gestartet"-Events

#### Geplante Schritte

Wenn ein Canvas-Schritt auf dem Zeitplan steht, wird der Nutzer:innen nach dem Auftreten des Ausnahme-Events sofort aus dem Canvas aussteigen. Nehmen wir an, ein Nutzer:in betritt einen Canvas, bei dem der erste Schritt eine einwöchige Verzögerung und ein Ausnahme-Event aufweist. Wenn der Nutzer:innen das Ausnahme-Event an Tag 5 durchführt, würde er sofort nach der Durchführung des Ausnahme-Events (an Tag 5) aussteigen. 
 
#### Getriggerte Schritte

Wenn ein Canvas-Schritt durch ein Ereignis getriggert wird, wird der letzte geplante Sendevorgang, der durch diesen Trigger ausgelöst wurde, abgebrochen, aber der Nutzer:innen bleibt für die Dauer des Fensters im Canvas. Das bedeutet, dass der Nutzer:innen den Schritt auch dann noch erhalten kann, wenn er das triggernde Ereignis innerhalb des Fensters erneut ausführt. Nachdem das Fenster durchgelaufen ist, verlässt der Nutzer:innen den Canvas.

### Segmente und Filter verwenden

Sie können auch Segmente und Filter in den Ausstiegskriterien hinzufügen. Das bedeutet, dass Nutzer:innen, die dem Segment und dem Filter entsprechen, das Canvas verlassen und keine weiteren Nachrichten erhalten. 

Wenn zum Beispiel der erste Schritt in einem Canvas ein Verzögerungsschritt mit einer fünftägigen Verzögerung ist, dann gelten die Ausstiegskriterien am Ende dieses Schritts. Wenn also ein:e Nutzer:in die Ausstiegskriterien erfüllt, wird er am Ende der fünf Tage aussteigen.

{% alert note %}
Array-Attribute werden derzeit nicht als Exit-Kriterien für Ausnahmeereignisse unterstützt.
{% endalert %}

### Dasselbe Exit-Event und Konversions-Event

Wenn das Exit-Event und das Konversions-Event identisch sind, werden sowohl die Konversion als auch das Exit-Event berücksichtigt. Wenn ein Canvas beispielsweise einen Verzögerungsschritt hat und ein Nutzer:innen in diesem Verzögerungsschritt das Ausstiegskriterium ausführt, wird das Ausstiegsereignis inkrementiert, sobald der Nutzer:innen den Verzögerungsschritt verlässt. Die Konversion wird auch erhöht, sobald das Ereignis im Nutzerprofil protokolliert wird.

Konversionen werden auch nach Beendigung des Canvas getrackt, aber Ausstiege werden nicht getrackt, sobald der Nutzer:innen den Canvas verlässt. Das Zeitfenster für die Konversion erstreckt sich auf drei Tage über die maximale Dauer des Canvas hinaus. Das bedeutet, dass Konversionen auch dann noch getrackt werden, wenn das Tracking der Ausgänge eingestellt wurde. 

Die Mindestzeit für ein Konvertierungsfenster beträgt fünf Minuten. Setzen Sie die Konversions-Fenster für Ihre Konversions-Ereignisse auf fünf Minuten, um so weit wie möglich mit den Exit-Ereignissen gleichzuziehen. Wir empfehlen außerdem, das Konvertierungsfenster so einzustellen, dass es mindestens dem längsten Pfad im Canvas entspricht.

Betrachten Sie das folgende Beispiel, wie Analytics berechnet werden:

1. Zehn Nutzer:innen gehen durch den Canvas.
2. Drei Nutzer:innen führen das Konversions-Event innerhalb von fünf Minuten durch (die Anzahl der Exit-Events ist drei, die Anzahl der Konversions-Events ist drei).
3. Weitere fünf Nutzer:innen verlassen den Canvas nach fünf Minuten, führen aber das Konversions-Event nach zwei Tagen durch (die Anzahl der Exit-Events bleibt gleich, aber das Konversions-Event erhöht sich auf acht).
4. Die letzten beiden Nutzer:innen verlassen den Canvas nach fünf Minuten, führen aber das Konversions-Event nicht durch oder führen es nach drei Tagen und fünf Minuten durch (sie werden weder in den Metriken für Exit-Events noch für Konversions-Events gezählt).

## Beispiel

Nehmen wir an, wir wollen Nutzer:innen zusammenstellen, die noch nicht bei unserem Rucksacklieferanten eingekauft haben. Um die Ausstiegskriterien festzulegen, würden wir:

1. Wählen Sie **Kauf-Event** als Ausnahme-Event aus.
2. Wählen Sie **Auslöser hinzufügen**. 
3. Wählen Sie bei **Segmente** die Option **Am letzten Tag verwendet** aus, damit bei der Einführung unseres Canvas die Zielgruppe Nutzer:innen ausschließt, die keine Käufe getätigt haben.
4. Für **Filter** wählen Sie **Kaufverhalten** > **Anzahl der Käufe** > **Gekauftes Produkt**.
5. Setzen Sie die Filtergruppe auf `backpack-example exactly 1`. Das bedeutet, dass Nutzer:innen, die unser Produkt Rucksack gekauft haben, das Canvas verlassen würden.

![Exit-Kriterien-Einstellungen mit "Kauf-Event" als Ausnahme-Event, d.h. wenn ein Nutzer:innen einen Kauf tätigt, verlässt er diesen Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}


