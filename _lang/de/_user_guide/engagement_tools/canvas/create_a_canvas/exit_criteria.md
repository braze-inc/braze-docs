---
nav_title: Exit-Kriterien 
article_title: Exit-Kriterien 
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Dieser Artikel referenziert die Ausstiegskriterien und wie Nutzer:innen Ihr Canvas auf der Grundlage der ausgewählten Kriterien verlassen können."
tool: Canvas
---

# Ausstiegskriterien

> Indem Sie Ausnahme-Events direkt zu Ihren Canvas-Eingangsregeln hinzufügen, können Ihre Nutzer:innen Ihr Canvas verlassen, sobald das Ereignis am Ende des Schritts eintritt. Dies ermöglicht ein gezielteres Targeting des Messagings auf Canvas bei Ihrer Zielgruppe.

## Festlegung von Ausstiegskriterien

Im Schritt **Zielgruppe** des Canvas-Erstellers können Sie Ausstiegskriterien festlegen, um die Nutzer zu identifizieren, die Ihr Canvas verlassen sollen. 

Das Ausstiegskriterium enthält ein Ausnahme-Event, d.h. die spezifische Aktion, die Nutzer:innen zum Verlassen des Canvas veranlassen kann.

![Die Ausstiegskriterien, die eingerichtet wurden, um Nutzer:innen wieder zu engagieren, die Produkte angesehen, aber noch nicht in den Warenkorb gelegt oder eine Bestellung aufgegeben haben.][1]{: style="max-width:90%;"}

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

### Segmente und Filter verwenden

Sie können auch Segmente und Filter in den Ausstiegskriterien hinzufügen. Das bedeutet, dass Nutzer:innen, die dem Segment oder Filter entsprechen, das Canvas verlassen und keine weiteren Nachrichten erhalten. 

Wenn zum Beispiel der erste Schritt in einem Canvas ein Verzögerungsschritt mit einer fünftägigen Verzögerung ist, dann gelten die Ausstiegskriterien am Ende dieses Schritts. Wenn also ein:e Nutzer:in die Ausstiegskriterien erfüllt, wird er am Ende der fünf Tage aussteigen.

{% alert note %}
Array-Attribute werden derzeit nicht als Exit-Kriterien für Ausnahmeereignisse unterstützt.
{% endalert %}

## Beispiel

Nehmen wir an, wir wollen Nutzer:innen zusammenstellen, die noch nicht bei unserem Rucksacklieferanten eingekauft haben. Um die Ausstiegskriterien festzulegen, würden wir:

1. Wählen Sie **Kauf-Event** als Ausnahme-Event aus.
2. Wählen Sie **Auslöser hinzufügen**. 
3. Wählen Sie bei **Segmente** die Option **Am letzten Tag verwendet** aus, damit bei der Einführung unseres Canvas die Zielgruppe Nutzer:innen ausschließt, die keine Käufe getätigt haben.
4. Für **Filter** wählen Sie **Kaufverhalten** > **Anzahl der Käufe** > **Gekauftes Produkt**.
5. Setzen Sie die Filtergruppe auf `backpack-example exactly 1`. Das bedeutet, dass Nutzer:innen, die unser Produkt Rucksack gekauft haben, das Canvas verlassen würden.

![Exit Criteria-Einstellungen mit "Kauf-Event" als Ausnahme-Event. Wenn ein Nutzer:innen einen Kauf tätigt, verlässt er diesen Canvas.][2]{: style="max-width:80%;"}


[1]: {% image_buster /assets/img/exit_criteria.png %}
[2]: {% image_buster /assets/img_archive/exit_criteria_example.png %}
