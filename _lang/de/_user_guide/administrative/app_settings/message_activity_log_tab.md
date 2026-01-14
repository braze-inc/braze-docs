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

Diese Nachrichten können von unserem eigenen System, Ihren Anwendungen oder Plattformen oder von unseren Drittpartnern stammen. Dies kann zu einer unendlichen Anzahl von Meldungen führen, die in diesem Protokoll erscheinen können.

## Verstehen von Protokollmeldungen

Um herauszufinden, was Ihre Nachrichten bedeuten, achten Sie auf den Wortlaut jeder Nachricht und die dazugehörigen Spalten, denn das kann Ihnen bei der Fehlersuche mit Hilfe von Kontexthinweisen helfen. 

Wenn Sie z.B. einen Protokolleintrag haben, dessen Nachricht "empty-cart_app" lautet und Sie sich nicht sicher sind, was das bedeutet, schauen Sie links in die Spalte **Typ**. Wenn Sie „Fehler bei abgebrochener Nachricht“ sehen, können Sie davon ausgehen, dass die Nachricht so geschrieben wurde, wie die Abbruch-Nachricht mit Liquid, und dass die Nachricht abgebrochen wurde, weil der oder die beabsichtigte Empfänger:in der Nachricht einen leeren Warenkorb in Ihrer App hatte.

### Allgemeine Nachrichten

Es gibt einige häufige Meldungstypen, die Sie sehen können, und einige enthalten sogar Links zur Fehlerbehebung, die Ihnen bei der Diagnose und Behebung von Problemen helfen.

Die folgenden Meldungen dienen als Beispiel und stimmen möglicherweise nicht genau mit dem überein, was in der Spalte **Meldung** in Ihrem Protokoll angezeigt wird.

| Nachrichtentyp | Potenzielle Nachricht | Beschreibung |
|---|---|---|
| Soft Bounce | Zustellfehler mit E-Mail-Adresse same@example.com. | Die E-Mail-Adresse war gültig und die E-Mail-Nachricht erreichte den Mailserver des Empfängers, wurde aber wegen eines "temporären" Problems abgelehnt. <br><br>Häufige Gründe für Zustellfehler: {::nomarkdown} <ul> <li> Die Mailbox war voll (der Benutzer hat seine Quote überschritten) </li> <li> Der Server war ausgefallen </li> <li> Die Nachricht war zu groß für den Posteingang des Empfängers </li>  </ul> {:/} Wenn eine E-Mail einen Soft Bounce erhalten hat, versuchen wir es normalerweise innerhalb von 72 Stunden erneut, aber die Anzahl der Wiederholungsversuche variiert von Empfänger zu Empfänger. |
| Hard Bounce | Das E-Mail-Konto, das Sie versucht haben zu erreichen, existiert nicht. Versuchen Sie, die E-Mail-Adresse des Empfängers noch einmal auf Tippfehler oder unnötige Leerzeichen zu überprüfen. | Ihre Nachricht hat den Posteingang dieser Person nie erreicht, weil es keinen Posteingang zu erreichen gab. Wenn Sie tiefer in die Materie eindringen möchten, enthalten solche Nachrichten manchmal Links in der Spalte **Details anzeigen**, mit denen Sie das Profil des Empfängers einsehen können.|
| Block | Die Spam-Nachricht wird aufgrund der Anti-Spam-Richtlinie zurückgewiesen. | Ihre Nachricht wurde als Spam kategorisiert. Dieser E-Mail-Fehler wird für eine:n Nutzer:in protokolliert, wenn wir ein Event vom ESP erhalten haben, das anzeigt, dass die E-Mail gelöscht wurde. Wenn Sie diese Nachricht jedoch häufig sehen, sollten Sie vielleicht Ihre Sendegewohnheiten oder den Content Ihrer Nachricht überdenken. Denken Sie auch zurück - haben Sie [Ihre IP aufgewärmt]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)? Wenn nicht, wenden Sie sich an Braze, um sich beraten zu lassen, wie Sie dies in die Wege leiten können.|
| Fehler bei abgebrochener Nachricht | empty-cart_web | Wenn Sie eine App mit einem Warenkorb haben oder eine Sendung mit einer Abbruchnachricht im Liquid erstellen, können Sie festlegen, welche Nachricht Sie erhalten, wenn die Sendung abgebrochen wird. In diesem Fall lautet die zurückgegebene Nachricht empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Warum ist meine Nachricht hier nicht aufgeführt?

Die Nachrichten im Nachrichten-Aktivitätsprotokoll können aus einer Vielzahl von Quellen stammen: Braze, Ihre Anwendungen oder Plattformen oder unsere Drittparteipartner. Das bedeutet, dass es eine unendliche Anzahl von Meldungen gibt, die in diesem Protokoll erscheinen könnten - wie Sie sich vorstellen können, können wir sie nicht alle auflisten!

Zum Beispiel könnten einige potenzielle „Block“-Nachrichten zusätzlich zu der in der obigen Tabelle aufgeführten wie folgt lauten:

- Leider wurden die Nachrichten von [_IP_ADDRESS_] nicht gesendet. Bitte wenden Sie sich an Ihren Internet Service Provider, da ein Teil seines Netzwerks auf unserer Sperrliste steht.
- Nachricht aufgrund lokaler Richtlinien abgelehnt.
- Die Nachricht wurde vom Empfänger als Spam blockiert.
- Dienst nicht verfügbar, Client-Host [_IP_ADDRESS_] mit Spamhaus blockiert.

## Aufbewahrungsdauer der Bindung

Die Fehler der letzten 60 Stunden finden Sie in den Protokollen der Nachrichtenaktivitäten. Protokolle, die mehr als 60 Stunden alt sind, werden gelöscht und sind nicht mehr zugänglich.

### Anzahl der gespeicherten Fehlerprotokolle

Die Anzahl der gespeicherten Protokolle wird von mehreren Bedingungen beeinflusst. Wenn zum Beispiel eine geplante Kampagne an Tausende von Nutzer:innen gesendet wird, sehen wir im Nachrichten-Aktivitätsprotokoll möglicherweise eine Auswahl der Fehler statt aller Fehler. Im Folgenden finden Sie eine Übersicht über die Bedingungen, die beeinflussen, wie viele Protokolle gespeichert werden:
- Es werden bis zu 20 Fehlerprotokolle desselben Fehlertyps für dieselbe Kampagne oder denselben Canvas-Schritt innerhalb einer festen Uhrzeit für die folgenden Fehlertypen gespeichert:
    - Connected-Content-Fehler
    - Abbruch Nachrichtenfehler
    - Webhook-Fehler
    - SMS Ablehnungsfehler
    - Fehler bei der SMS-Zustellung
    - WhatsApp-Fehler
    - A/B-Tests Fehler
- Bis zu 20 Push-Benachrichtigungs-Fehlerprotokolle desselben Fehlertyps werden für dieselbe Kombination aus Kampagne oder Canvas-Schritt und App für die folgenden Fehlertypen gespeichert:
    - Ungültige Push-Zugangsdaten
    - Ungültiges Push-Token
    - Keine Push-Zugangsdaten
    - Token-Fehler
    - Quote Überschritten
    - Zeitüberschreitung der Wiederholungsversuche
    - Ungültige Nutzlast
    - Unerwarteter Fehler
- Bis zu 100 Fehlerprotokolle desselben Fehlertyps werden für dieselbe App innerhalb einer festen Uhrzeit für die folgenden Fehlertypen gespeichert:
    - Live Activity-Fehler (Kein Push-Zugangsdaten-Fehler)
    - Live Activity-Fehler (Ungültige Push-Zugangsdaten)
    - Andere Fehler bei Live-Aktivitäten
    - APNS Feedback Entfernte Token-Fehler
- Es werden bis zu 100 Fehlerprotokolle desselben Fehlertyps für dieselbe Kampagne oder denselben Canvas-Schritt innerhalb einer festen Uhrzeit für die folgenden Fehlertypen gespeichert:
    - E-Mail Soft Bounce-Fehler
    - E-Mail Hard Bounce-Fehler
    - E-Mail Block Fehler
- Es werden bis zu 100 User-Aliasing-Fehlerprotokolle für denselben Workspace innerhalb einer festen Uhrzeit gespeichert.

