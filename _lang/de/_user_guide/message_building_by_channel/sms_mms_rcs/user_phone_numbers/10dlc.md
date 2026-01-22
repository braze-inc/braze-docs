---
nav_title: "A2P 10DLC"
article_title: A2P 10DLC
page_order: 2.9
description: "Dieser Artikel behandelt A2P 10DLC, warum die 10DLC-Registrierung für US-Kund:innen mit Longcode erforderlich ist, hilfreiche Informationen zu Kosten und Durchsatz und wie Sie mit der Registrierung beginnen können."
page_type: reference
channel:
  - SMS
  
---

# Anwendung-zu-Person 10-stellige lange Codes

> A2P 10DLC bezieht sich auf ein System in den Vereinigten Staaten, das es Unternehmen ermöglicht, Nachrichten vom Typ Application-to-Person (A2P) über einen standardmäßigen 10-stelligen langen Code (10DLC) zu versenden. Diese registrierten Langcodes haben einen höheren Durchsatz, eine bessere Zustellbarkeit und eine bessere Compliance als der Standard-Langcode.

{% alert important %}
Alle Kunden, die derzeit US-Langcodes haben und/oder verwenden, um an US-Kunden zu senden, müssen ihre Langcodes für 10DLC registrieren; wer dies nicht tut, muss mit einer starken Filterung aller Nachrichten rechnen. Dieses Bewerbungsverfahren dauert 4-6 Wochen.
{% endalert %}

## Warum es notwendig ist

Der Dienst 10DLC wurde speziell für das A2P-Messaging mit Langcodes entwickelt. In der Vergangenheit waren lange Codes für die Nachrichtenübermittlung von Person zu Person (P2P) gedacht. Wenn sie jedoch für Marketingzwecke verwendet wurden, führten sie dazu, dass Unternehmen durch den begrenzten Durchsatz und die verstärkte Filterung behindert wurden. 

10DLC hilft Ihnen, diese Probleme zu lösen, indem es Folgendes bietet: 
- **Höherer Durchsatz**: 10DLC-Nummern unterstützen ein höheres Volumen an Nachrichten als normale Langcodes.
- **Bessere Zustellbarkeit**: 10DLC-Nummern sind für den A2P-Verkehr bestimmt. Daher ist es wahrscheinlicher, dass Nachrichten, die mit diesen Nummern versendet werden, den Empfänger erreichen und weniger wahrscheinlich, dass sie vom Netzbetreiber gefiltert oder zurückgewiesen werden als Nachrichten, die über normale lokale Vorwahlen versendet werden. 
- **Verbesserte Compliance**: Die Verwendung eines lokalen langen Codes für kommerzielle Textnachrichten verstößt gegen die [CTIA-Richtlinien](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf). Die 10DLC-Nummern wurden für Massennachrichten konzipiert und ermöglichen es Marken, die Branchenvorschriften einzuhalten, ohne sich auf Kurznummern verlassen zu müssen.
- **Budgetfreundlich**: 10DLC ist eine ausgezeichnete Option für Unternehmen, die mit dem SMS-Versand beginnen oder SMS in kleinen Mengen versenden möchten. Für Marken, die ein größeres Messaging-Volumen von über 100.000 Nachrichten pro Tag versenden, empfehlen wir die Verwendung eines Shortcodes. 

Seit 2019 haben die Netzbetreiber damit begonnen, 10DLC für kommerzielles Messaging zu übernehmen. Derzeit unterstützen Verizon und AT&T 10DLC, und wir erwarten, dass alle großen Netzbetreiber bald folgen werden. Auch wenn dies kurzfristig zu Unannehmlichkeiten führen kann, werden die Kunden langfristig von besseren Zustellungsraten profitieren und gleichzeitig ihre Kunden vor unerwünschten Nachrichten schützen. 

## Was Sie wissen müssen

### Zugang

Die Registrierung von langen Codes bei A2P 10DLC dauert 4-6 Wochen.

### Kosten 

Die Registrierung bei A2P 10DLC kann verschiedene Arten von Gebühren beinhalten:

| Gebührentyp | Beschreibung |
| -------- | ---------- |
| Gebühren für die Registrierung | Nominale Gebühren bei der Registrierung Ihrer Marke und Ihres Anwendungsfalls in allen großen US-Netzwerken. |
| Gebühren für sekundäre Überprüfungen | Marken können gegen ihren [Brand Trust Score](#trust-score) Einspruch erheben und ein zweites Prüfverfahren beantragen, um ihren Gesamtdurchsatz zu verbessern; dieses Verfahren ist gebührenpflichtig. |
| Spediteur-Gebühren | Gebühren, die von Netzbetreibern für ausgehende SMS- und MMS-Nachrichten erhoben werden, die nach der 10DLC-Registrierung an Benutzer gesendet werden. Ab dem 1\. Oktober 2021 werden die Gebühren für nicht registrierten Datenverkehr (Standard-Langcodes) höher sein als für registrierten Datenverkehr (10DLC). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Besuchen Sie den Twilio-Artikel 10DLC, um sich über die aktualisierten [Gebührenschätzungen](https://support.twilio.com/hc/en-us/articles/1260803965530-What-pricing-and-fees-are-associated-with-the-A2P-10DLC-service-) zu informieren.

### Durchsatz

Der Nachrichtendurchsatz für Ihren 10DLC hängt von mehreren Faktoren ab, u.a. vom Vertrauens-Score der Marke, den täglichen Höchstgrenzen für Nachrichten und den Anwendungsfällen für Ihr Messaging.

#### Vertrauens-Score für Marken {#trust-score}

The Campaign Registry (TCR) ist eine Drittanbieter-Agentur, die einen Reputationsalgorithmus verwendet, um bestimmte Kriterien in Bezug auf Ihr Unternehmen zu überprüfen und einen Vertrauenswert zuzuweisen, der den Durchsatz von Nachrichten für jede Marke bestimmt. Dieser Vertrauens-Score wird zugewiesen, wenn sich ein:e Kund:in für das US 10DLC-Messaging registriert. Je höher der Vertrauens-Score, desto besser sind die Nachrichten pro Sekunde (MPS), die Sie erhalten. 

|     | Vertrauens-Score | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| Hoch | 75-100 | 75 MPS | 75 MPS | 75 MPS |
| Medium | 50-74 | 40 MPS | 40 MPS | 40 MPS |
| Niedrig | 1-49 | 4 MPS | 4 MPS | 4 MPS | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert tip %}
Unternehmen, die im Russel 3000-Index gelistet sind, erhalten nach der 10DLC-Registrierung und -Überprüfung einen hohen Durchsatz und Vertrauens-Score.
{% endalert %} 

#### Tägliche Nachrichtenlimits

Die täglichen Limits liegen zwischen 2.000 und 200.000 Nachrichten, je nach Vertrauens-Score Ihrer Marke, und gelten für alle Langcodes. Während hohe Vertrauens-Scores mit einem Durchsatz von 60 Messages pro Sekunde einhergehen, gelten die vom Netzbetreiber festgelegten Grenzen für tägliche Messages weiterhin. Das bedeutet, dass Shortcodes eine bessere Option sind, wenn die täglichen Nachrichtenspitzen einer Marke höher sind als das vorgegebene Tageslimit. 

#### Anwendungsfälle für Messaging

Der Durchsatz hängt auch von der Art des Messaging-Anwendungsfalls ab, den Sie wählen. Die meisten Kund:innen fallen unter den Anwendungsfall des Standard-Marketings oder des gemischten Marketings. Für andere, weniger häufige Anwendungsfälle gelten andere Durchsatzwerte.

Je nach Anwendungsfall variiert der Vertrauens-Score, den Sie benötigen, um den maximalen Durchsatz zu erreichen. In den folgenden Tabellen sind die Standard-Anwendungsfälle und die üblichen Vertrauens-Score-Bereiche für Anwendungsfälle aufgeführt. Für spezielle Anwendungsfälle wie Notdienste oder Wohltätigkeitsorganisationen lesen Sie bitte die [Twilio-Dokumente](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

| Standard Anwendungsfälle | Beschreibung |
| ------------------ | ----------- |
| Marketing | Werbeinhalte wie Verkäufe und zeitlich begrenzte Angebote. |
| Gemischt | Kampagne, die mehrere Anwendungsfälle abdeckt, wie z.B. die Kundenbetreuung. | 
| Höhere Bildung | Kampagnen für höhere Bildungseinrichtungen. |
| Abstimmen & Abstimmen | Nicht-politische Umfragen und Abstimmungen, wie z.B. Kundenumfragen. |
| PSA | PSAs, um das Bewusstsein für ein bestimmtes Thema zu schärfen. |
| Kundenbetreuung | Support, Kontoverwaltung und andere Kundeninteraktionen. |
| Zustellungsbenachrichtigungen | Status der Zustellung von Nachrichten. |
| Konto-Benachrichtigungen | Benachrichtigungen über den Status eines Kontos. |
| 2FA | Jegliche Authentifizierung der Kontoverifizierung, wie OTP. | 
| Sicherheitswarnungen | Benachrichtigung über ein kompromittiertes System. |
| Betrugswarnungen | Benachrichtigung über potenziell betrügerische Aktivitäten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs %}
{% tab Declared Use Case %}
Ein erklärter Anwendungsfall bedeutet, dass Sie sich für einen bestimmten, nicht marketingbezogenen Anwendungsfall entschieden haben (z. B. 2FA oder Kontobenachrichtigungen).

| Vertrauens-Score | Gesamtdurchsatz in den wichtigsten US-Netzwerken | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74	 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS| 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% tab Mixed Marketing Use Case %}

Gemischte Marketing-Anwendungsfälle können für Kunden registriert werden, die Nachrichten für mehrere Anwendungsfälle von derselben Gruppe von Nummern oder für Marketingzwecke senden möchten.

| Vertrauens-Score | Gesamtdurchsatz in den wichtigsten US-Netzwerken | AT&T | T-Mobile  | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS| 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}

Besuchen Sie den Twilio-Artikel 10DLC, um die aktualisierten [Durchsatzschätzungen](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US) zu überprüfen.

## Nächste Schritte

Kund:innen, die sich noch nicht für 10DLC registriert haben, müssen mit ihrem Customer-Success-Manager zusammenarbeiten, um ihre Langcodes zu registrieren. **Wenn Kunden:innen es versäumen, ihre Langcodes zu registrieren, werden ab dem 1\. Oktober 2021 alle A2P-Sender, die Langcodes verwenden, stark gefiltert werden.** Wenden Sie sich an Ihren Customer-Success-Manager, um Ihre 10DLC-Registrierung in Angriff zu nehmen. 
