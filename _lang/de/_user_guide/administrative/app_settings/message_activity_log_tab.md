---
nav_title: Protokoll der Nachrichtenaktivitäten
article_title: Nachrichten-Aktivitätsprotokoll
page_order: 5
page_type: reference
description: "Dieser Referenzartikel beschreibt das Nachrichten-Aktivitätsprotokoll, das Ihnen die mit Ihren Kampagnen und Sendungen verbundenen Nachrichten anzeigt. Hier finden Sie auch Informationen zum Verständnis von Protokollnachrichten."

---

# Nachrichten-Aktivitätsprotokoll

> Das **Nachrichten-Aktivitätsprotokoll** bietet Ihnen die Möglichkeit, alle Nachrichten (insbesondere Fehlermeldungen) im Zusammenhang mit Ihren Kampagnen und Sendungen zu sehen.

Sie können API-Kampagnentransaktionen einsehen, Details zu fehlgeschlagenen Nachrichten untersuchen und Erkenntnisse darüber gewinnen, wie Sie die Zustellung von Benachrichtigungen verbessern oder bestehende technische Probleme lösen können.

Um auf das Protokoll zuzugreifen, gehen Sie zu **Einstellungen** > **Nachrichtenaktivitätsprotokoll**.

![Nachrichten-Aktivitätsprotokoll]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
Zusätzlich zu diesem Artikel empfehlen wir Ihnen auch unseren Braze Learning-Kurs [Qualitätssicherung und Debugging-Tools](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), in dem Sie lernen, wie Sie das Message Activity Log für Ihre eigene Fehlersuche und -behebung nutzen können.
{% endalert %}

Sie können nach den folgenden im **Nachrichten-Aktivitätsprotokoll** protokollierten Inhalten filtern:

- Fehler bei Push-Benachrichtigungen
- Fehler bei abgebrochener Nachricht
- Webhook-Fehler
- Mail-Fehler
- API-Nachrichteneinträge
- Connected-Content-Fehler
- REST API: Fehler bei verbundener Zielgruppe
- User-Aliasing-Fehler
- A/B-Testing-Fehler
- SMS/MMS-Fehler
- WhatsApp-Fehler
- Live-Aktivitätsfehler
- Fehler beim Triggern durch Nutzer:in
- Fehler [beim täglichen Aufruflimit]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/#monitor-your-agent) von Braze Agents

Diese Nachrichten können von unserem eigenen System, Ihren Anwendungen oder Plattformen oder von unseren Drittpartnern stammen. Dies kann zu einer unendlichen Anzahl von Meldungen führen, die in diesem Protokoll erscheinen können.

## Verstehen von Protokollmeldungen

Um herauszufinden, was Ihre Nachrichten bedeuten, achten Sie auf den Wortlaut jeder Nachricht und die dazugehörigen Spalten, denn das kann Ihnen bei der Fehlersuche mit Hilfe von Kontexthinweisen helfen. 

Wenn Sie beispielsweise einen Protokolleintrag mit der "empty-cart_app"Nachricht haben und sich nicht sicher sind, was dies bedeutet, überprüfen Sie bitte die Spalte **„Typ“** auf der linken Seite. Wenn Sie „Fehler bei abgebrochener Nachricht“ sehen, können Sie davon ausgehen, dass die Nachricht so geschrieben wurde, wie die Abbruch-Nachricht mit Liquid, und dass die Nachricht abgebrochen wurde, weil der oder die beabsichtigte Empfänger:in der Nachricht einen leeren Warenkorb in Ihrer App hatte.

### Allgemeine Nachrichten

Es gibt einige häufige Meldungstypen, die Sie sehen können, und einige enthalten sogar Links zur Fehlerbehebung, die Ihnen bei der Diagnose und Behebung von Problemen helfen.

Die folgenden Meldungen dienen als Beispiel und stimmen möglicherweise nicht genau mit dem überein, was in der Spalte **Meldung** in Ihrem Protokoll angezeigt wird.

| Nachrichtentyp | Potenzielle Nachricht | Beschreibung |
|---|---|---|
| Soft Bounce | Zustellfehler mit E-Mail-Adresse same@example.com. | Die E-Mail-Adresse war gültig und die E-Mail-Nachricht erreichte den Mailserver des Empfängers, wurde aber wegen eines "temporären" Problems abgelehnt. <br><br>Häufige Gründe für Zustellfehler: {::nomarkdown} <ul> <li> Die Mailbox war voll (der Benutzer hat seine Quote überschritten) </li> <li> Der Server war ausgefallen </li> <li> Die Nachricht war zu groß für den Posteingang des Empfängers </li>  </ul> {:/} Wenn eine E-Mail einen Soft Bounce erhalten hat, versuchen wir in der Regel innerhalb von 72 Stunden erneut, den Versand durchzuführen. Die Anzahl der Wiederholungsversuche variiert jedoch je nach Empfänger. |
| Hard Bounce | Das E-Mail-Konto, das Sie versucht haben zu erreichen, existiert nicht. Versuchen Sie, die E-Mail-Adresse des Empfängers noch einmal auf Tippfehler oder unnötige Leerzeichen zu überprüfen. | Ihre Nachricht hat den Posteingang dieser Person nie erreicht, weil es keinen Posteingang zu erreichen gab. Sollten Sie weitere Informationen benötigen, können Nachrichten wie diese manchmal Links in der Spalte **„Details anzeigen“** enthalten, über die Sie das Profil des vorgesehenen Empfängers einsehen können.|
| Block | Die Spam-Nachricht wird aufgrund der Anti-Spam-Richtlinie zurückgewiesen. | Ihre Nachricht wurde als Spam kategorisiert. Dieser E-Mail-Fehler wird für eine:n Nutzer:in protokolliert, wenn wir ein Event vom ESP erhalten haben, das anzeigt, dass die E-Mail gelöscht wurde. Es könnte sein, dass dies nur für die vorgesehenen Empfänger:innen gilt, aber wenn Sie diese Nachricht häufig erhalten, sollten Sie Ihre Versandgewohnheiten oder den Inhalt Ihrer Nachricht möglicherweise überdenken. Denken Sie auch zurück - haben Sie [Ihre IP aufgewärmt]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)? Falls nicht, wenden Sie sich bitte an Braze, um Unterstützung zu erhalten.|
| Fehler bei abgebrochener Nachricht | empty-cart_web | Wenn Sie eine App mit einem Warenkorb haben oder eine Sendung mit einer Abbruchnachricht im Liquid erstellen, können Sie festlegen, welche Nachricht Sie erhalten, wenn die Sendung abgebrochen wird. In diesem Fall lautet die zurückgegebene Nachricht empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Warum ist meine Nachricht hier nicht aufgeführt?

Die Nachrichten im Nachrichten-Aktivitätsprotokoll können aus einer Vielzahl von Quellen stammen: Braze, Ihre Anwendungen oder Plattformen oder unsere Drittparteipartner. Das bedeutet, dass es eine unendliche Anzahl von Meldungen gibt, die in diesem Protokoll erscheinen könnten - wie Sie sich vorstellen können, können wir sie nicht alle auflisten!

Zum Beispiel könnten einige potenzielle „Block“-Nachrichten zusätzlich zu der in der obigen Tabelle aufgeführten wie folgt lauten:

- Leider wurden die Nachrichten von[_IP_ADDRESS_]nicht versendet. Bitte wenden Sie sich an Ihren Internet Service Provider, da ein Teil seines Netzwerks auf unserer Sperrliste steht.
- Nachricht aufgrund lokaler Richtlinien abgelehnt.
- Die Nachricht wurde vom Empfänger als Spam blockiert.
- Der Dienst ist derzeit nicht verfügbar, der Client-Host[_IP_ADDRESS_]wurde über Spamhaus gesperrt.

## Aufbewahrungsdauer der Bindung

Die Fehler der letzten 60 Stunden finden Sie in den Protokollen der Nachrichtenaktivitäten. Protokolle, die mehr als 60 Stunden alt sind, werden gelöscht und sind nicht mehr zugänglich.

### Anzahl der gespeicherten Fehlerprotokolle

Die Anzahl der gespeicherten Protokolle wird von mehreren Bedingungen beeinflusst. Wenn zum Beispiel eine geplante Kampagne an Tausende von Nutzer:innen gesendet wird, sehen wir im Nachrichten-Aktivitätsprotokoll möglicherweise eine Auswahl der Fehler statt aller Fehler. Im Folgenden finden Sie eine Übersicht über die Bedingungen, die sich darauf auswirken, wie viele Protokolle gespeichert werden:
- Für dieselbe Kampagne oder denselben Canvas-Schritt werden innerhalb einer festgelegten Stunde bis zu 20 Fehlerprotokolle desselben Fehlertyps gespeichert. Dies gilt für die folgenden Fehlertypen:
    - Connected-Content-Fehler
    - Fehler bei der Abbrech-Nachricht
    - Webhook-Fehler
    - Fehler bei der SMS-Ablehnung
    - Fehler bei der SMS-Zustellung
    - Fehler bei WhatsApp
    - Fehler bei A/B-Tests
- Für dieselbe Kampagne oder dieselbe Kombination aus Canvas-Schritt und App werden bis zu 20 Protokolle der Fehler bei Push-Benachrichtigungen desselben Fehlertyps für die folgenden Fehlertypen gespeichert:
    - Ungültige Push-Zugangsdaten
    - Ungültiges Push-Token
    - Keine Push-Zugangsdaten
    - Token-Fehler
    - Kontingent überschritten
    - Zeitüberschreitung bei Wiederholungsversuchen
    - Ungültige Nutzlast
    - Unerwarteter Fehler
- Für die folgenden Fehlertypen werden bis zu 100 Fehlerprotokolle desselben Fehlertyps für dieselbe App innerhalb einer festgelegten Stunde gespeichert:
    - Fehler bei Live-Aktivität (keine Push-Zugangsdaten)
    - Fehler bei Live-Aktivität (ungültige Push-Zugangsdaten)
    - Andere Live-Aktivitätsfehler
    - APN-Feedback: Fehler bei entfernten Tokens
- Für dieselbe Kampagne oder denselben Canvas-Schritt werden innerhalb einer festgelegten Stunde bis zu 100 Fehlerprotokolle desselben Fehlertyps gespeichert. Dies gilt für die folgenden Fehlertypen:
    - E-Mail-Soft-Bounce-Fehler
    - E-Mail-Hard-Bounce-Fehler
    - Fehler beim Blockieren von E-Mails
- Bis zu 100 Protokolle zum Auftreten von Fehlern beim User-Aliasing werden für denselben Workspace innerhalb einer festgelegten Stunde gespeichert.

## Test sendet

Das **Nachrichtenaktivitätsprotokoll** zeigt Testprotokolle für die folgenden Messaging-Kanäle an:

- SMS
- WhatsApp
- LINE
- Webhook

Testversandprotokolle sind für die folgenden Kanäle nicht verfügbar: E-Mail, Content-Cards, In-App-Nachrichten und Push-Benachrichtigungen.

Test-Sende-Protokolle sind mit „[TEST SEND]” gekennzeichnet, jedoch kann nicht garantiert werden, dass alle Test-Sende-Protokolle diese Kennzeichnung aufweisen (beispielsweise weisen Fehler bei Connected-Content diese Kennzeichnung nicht auf).
