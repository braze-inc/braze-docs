---
nav_title: Exit-Kriterien 
article_title: Exit-Kriterien 
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Dieser Referenzartikel behandelt das Feature Exit Criteria für Canvas Flow."
tool: Canvas
---

# Ausstiegskriterien

> Indem Sie [Ausnahme-Events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events) direkt zu Ihren Canvas-Entry-Regeln hinzufügen, können Ihre Nutzer:innen Ihr Canvas verlassen, sobald das Event am Ende des Schritts eintritt. Dies ermöglicht ein gezielteres Targeting des Messagings auf Canvas bei Ihrer Zielgruppe.

Im Schritt **Zielgruppe** des Canvas-Erstellers können Sie Ausstiegskriterien festlegen, um die Nutzer zu identifizieren, die Ihr Canvas verlassen sollen. Fügen Sie Ihr Ausnahme-Event hinzu und wählen Sie dann **Trigger hinzufügen**. 

Sie können auch Segmente und Filter in die Ausstiegskriterien aufnehmen. Das bedeutet, dass Benutzer, die dem Segment oder Filter entsprechen, den Canvas verlassen und keine weiteren Nachrichten erhalten. Wenn der erste Schritt in einem Canvas ein Verzögerungsschritt mit einer fünftägigen Verzögerung ist, dann gelten die Ausstiegskriterien am Ende dieses Schritts. Wenn also ein:e Nutzer:in die Ausstiegskriterien erfüllt, wird er am Ende der fünf Tage aussteigen.

{% alert note %}
Array-Attribute werden derzeit nicht als Exit-Kriterien für Ausnahmeereignisse unterstützt.
{% endalert %}

## Ausnahme-Events

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

## Anwendungsfall

Nehmen wir an, Sie möchten Nutzer ansprechen, die noch keine Einkäufe bei Ihrem Unternehmen getätigt haben. Wählen Sie zunächst **Kauf tätigen** als Ausnahmeereignis. Wählen Sie dann **Auslöser hinzufügen**. Wenn Ihr Canvas gestartet wird, schließt Ihre Zielgruppe Nutzer aus, die mit den folgenden Einstellungen für **Exit Criteria** einen Kauf getätigt haben. 

Im folgenden Beispiel wird dieses Ausstiegskriterium auch auf das Segment "Am letzten Tag benutzt" für jeden Benutzer angewendet, der genau einen Kauf getätigt hat.

![Exit Criteria-Einstellungen mit "Kauf-Event" als Ausnahme-Event. Wenn ein:e Nutzer:in einen Kauf tätigt, verlässt er diesen Canvas.][1]

[1]: {% image_buster /assets/img_archive/exit_criteria_example.png %} 
