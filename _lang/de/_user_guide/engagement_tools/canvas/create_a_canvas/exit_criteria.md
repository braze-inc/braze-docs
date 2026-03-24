---
nav_title: Ausstiegskriterien
article_title: Ausstiegskriterien 
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Dieser Referenzartikel behandelt Ausstiegskriterien und wie Nutzer:innen Ihr Canvas auf der Grundlage der ausgewählten Kriterien verlassen können."
tool: Canvas
---

# Ausstiegskriterien

> Indem Sie Ausnahme-Events direkt zu Ihren Canvas-Eingangsregeln hinzufügen, können Ihre Nutzer:innen Ihr Canvas verlassen, sobald das Event am Ende des Schritts eintritt. Dies ermöglicht einen gezielteren Ansatz für das Canvas-Messaging bei Ihrer Zielgruppe.

### Wie Nutzer:innen aussteigen

Nach der Ausführung des Exit-Events werden die Nutzer:innen aus dem Canvas ausgeschlossen, sobald der Schritt, in dem sie sich gerade befinden, beendet wurde. Wenn sich ein:e Nutzer:in beispielsweise 30 Tage lang in einem Delay-Schritt befindet und das Exit-Event am ersten Tag des Delay-Schritts ausführt, wird der/die Nutzer:in den Canvas erst nach weiteren 29 Tagen verlassen.

Betrachten wir ein weiteres Beispiel für die Verwendung von zeitbasierten Ausstiegskriterien. Ein:e Nutzer:in tritt am 1. Juli um 0 Uhr in einen Delay-Schritt ein, der auf 24 Stunden eingestellt ist. In dieser Verzögerungszeit führt er/sie das Exit-Event „Letzter Kauf vor weniger als 1 Stunde" um 3 Uhr morgens aus. Diese:r Nutzer:in wird am 2. Juli um 0 Uhr, also am Ende der Laufzeit des Delay-Schritts, auf die Ausstiegskriterien geprüft. Da seit dem Kauf am 1. Juli um 3 Uhr morgens 21 Stunden vergangen sind, wird er/sie den Canvas nicht verlassen, weil innerhalb der einen Stunde vor Verlassen des Delay-Schritts am 2. Juli kein Kauf getätigt wurde. Dies wirkt sich auf die „Gesamtausgänge nach Ausstiegskriterien" in Ihren Canvas-Analytics aus, die erst aktualisiert werden, wenn ein:e Nutzer:in den Canvas vollständig verlassen hat.

## Festlegung von Ausstiegskriterien

Im Schritt **Zielgruppe** des Canvas-Erstellers können Sie Ausstiegskriterien festlegen, um die Nutzer:innen zu identifizieren, die Ihr Canvas verlassen sollen. 

Das Ausstiegskriterium enthält ein Ausnahme-Event, d. h. die spezifische Aktion, die Nutzer:innen zum Verlassen des Canvas veranlassen kann.

![Die Ausstiegskriterien, die eingerichtet wurden, um Nutzer:innen erneut anzusprechen, die Produkte angesehen, aber noch nicht in den Warenkorb gelegt oder eine Bestellung aufgegeben haben.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Ausnahme-Events auswählen {#exception-events}

Wenn ein:e Nutzer:in das Ausnahme-Event ausführt, verlässt er/sie den Canvas. Beachten Sie, dass Ausnahme-Events nur dann Ausstiege triggern, wenn sich ein:e Nutzer:in im Canvas befindet und die User Journey durchläuft.

Nehmen wir an, Sie haben ein Canvas eingerichtet, um ein neues Produkt zu bewerben. In diesem Fall wäre der Kauf des Produkts das Ausnahme-Event. Auf diese Weise erhalten Nutzer:innen nach dem Kauf keine weiteren Nachrichten über ein Produkt, das sie bereits gekauft haben. Ausnahme-Events halten Ihre Nachrichten relevant und personalisiert.

Weitere Ausnahme-Events sind:

- Einen Kauf tätigen
- Eine Sitzung starten
- Ein angepasstes Event ausführen
- Ein Konversions-Event ausführen
- Eine E-Mail-Adresse hinzufügen
- Einen angepassten Attributwert ändern
- Einen Abo-Status aktualisieren
- Einen Abo-Gruppenstatus aktualisieren
- Mit einer Kampagne interagieren
- Einen Standort eingeben
- Einen Geofence triggern
- Eine eingehende SMS-Nachricht senden
- Eine eingehende WhatsApp-Nachricht senden
- Eine eingehende LINE-Nachricht senden
- Ein Warenkorb-aktualisiert-Event ausführen
- Ein „Checkout abgeschlossen"-Event ausführen
- Ein „Checkout gestartet"-Event ausführen

#### Geplante Schritte

Wenn ein Canvas-Schritt geplant ist, steigt der/die Nutzer:in nach dem Auftreten des Ausnahme-Events sofort aus dem Canvas aus. Nehmen wir an, ein:e Nutzer:in betritt einen Canvas, bei dem der erste Schritt eine einwöchige Verzögerung und ein Ausnahme-Event aufweist. Wenn der/die Nutzer:in das Ausnahme-Event an Tag 5 ausführt, würde er/sie sofort nach der Ausführung des Ausnahme-Events (an Tag 5) aussteigen. 
 
#### Getriggerte Schritte

Wenn ein Canvas-Schritt durch ein Event getriggert wird, wird der letzte geplante Sendevorgang, der durch diesen Trigger in die Warteschlange gestellt wurde, abgebrochen, aber der/die Nutzer:in bleibt für die Dauer des Fensters im Canvas. Das bedeutet, dass der/die Nutzer:in den Schritt weiterhin erhalten kann, wenn er/sie das triggernde Event innerhalb des Fensters erneut ausführt. Nachdem das Fenster abgelaufen ist, verlässt der/die Nutzer:in den Canvas.

### Segmente und Filter verwenden

Sie können auch Segmente und Filter in den Ausstiegskriterien hinzufügen. Das bedeutet, dass Nutzer:innen, die dem Segment und dem Filter entsprechen, das Canvas verlassen und keine weiteren Nachrichten erhalten. 

Wenn zum Beispiel der erste Schritt in einem Canvas ein Delay-Schritt mit einer fünftägigen Verzögerung ist, dann gelten die Ausstiegskriterien am Ende dieses Schritts. Wenn also ein:e Nutzer:in die Ausstiegskriterien erfüllt, steigt er/sie am Ende der fünf Tage aus.

{% alert note %}
Array-Attribute werden derzeit nicht als Ausstiegskriterien für Ausnahme-Events unterstützt.
{% endalert %}

### Dasselbe Exit-Event und Konversions-Event

Wenn das Exit-Event und das Konversions-Event identisch sind, werden sowohl die Konversion als auch das Exit-Event berücksichtigt. Wenn ein Canvas beispielsweise einen Delay-Schritt hat und ein:e Nutzer:in in diesem Delay-Schritt das Ausstiegskriterium erfüllt, wird das Exit-Event inkrementiert, sobald der/die Nutzer:in den Delay-Schritt verlässt. Die Konversion wird ebenfalls inkrementiert, sobald das Event im Nutzerprofil protokolliert wird.

Konversionen werden auch nach Beendigung des Canvas getrackt, Ausstiege hingegen nicht mehr, sobald der/die Nutzer:in den Canvas verlässt. Das Konversions-Fenster erstreckt sich auf drei Tage über die maximale Dauer des Canvas hinaus. Das bedeutet, dass Konversionen auch dann noch getrackt werden, wenn das Tracking der Ausstiege bereits eingestellt wurde. 

Die Mindestzeit für ein Konversions-Fenster beträgt fünf Minuten. Setzen Sie die Konversions-Fenster für Ihre Konversions-Events auf fünf Minuten, um so nah wie möglich an die Parität mit den Exit-Events heranzukommen. Wir empfehlen außerdem, das Konversions-Fenster so einzustellen, dass es mindestens dem längsten Pfad im Canvas entspricht.

Betrachten Sie das folgende Beispiel, wie Analytics berechnet werden:

1. Zehn Nutzer:innen durchlaufen den Canvas.
2. Drei Nutzer:innen führen das Konversions-Event innerhalb von fünf Minuten aus (die Anzahl der Exit-Events ist drei, die Anzahl der Konversions-Events ist drei).
3. Weitere fünf Nutzer:innen verlassen den Canvas nach fünf Minuten, führen aber das Konversions-Event nach zwei Tagen aus (die Anzahl der Exit-Events bleibt gleich, aber die Konversions-Events erhöhen sich auf acht).
4. Die letzten beiden Nutzer:innen verlassen den Canvas nach fünf Minuten, führen aber das Konversions-Event nicht aus oder führen es nach drei Tagen und fünf Minuten aus (sie werden weder in den Metriken für Exit-Events noch für Konversions-Events gezählt).

## Beispiel

Nehmen wir an, wir möchten Nutzer:innen ansprechen, die noch nicht bei unserem Rucksacklieferanten eingekauft haben. Um die Ausstiegskriterien festzulegen, würden wir:

1. **Kauf tätigen** als Ausnahme-Event auswählen.
2. **Trigger hinzufügen** auswählen. 
3. Für **Segmente** die Option **Am letzten Tag verwendet** auswählen, damit bei der Einführung unseres Canvas die Zielgruppe Nutzer:innen ausschließt, die Käufe getätigt haben.
4. Für **Filter** die Option **Kaufverhalten** > **Anzahl der Käufe** > **Gekauftes Produkt** auswählen.
5. Die Filtergruppe auf `backpack-example exactly 1` setzen. Das bedeutet, dass Nutzer:innen, die unser Rucksack-Produkt gekauft haben, das Canvas verlassen würden.

![Ausstiegskriterien-Einstellungen mit „Kauf tätigen" als Ausnahme-Event. Wenn ein:e Nutzer:in einen Kauf tätigt, verlässt er/sie diesen Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}

{% alert tip %}
Um Ausstiegskriterien einzurichten, die Event-Eigenschaften mit Eingangs-Eigenschaften vergleichen (z. B. nur dann aussteigen, wenn ein:e Nutzer:in den spezifischen Artikel kauft, den er/sie abgebrochen hat), lesen Sie [Ausstiegskriterien mit Eingangs-Events abgleichen]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/matching_entry_and_exit_criteria/).
{% endalert %}