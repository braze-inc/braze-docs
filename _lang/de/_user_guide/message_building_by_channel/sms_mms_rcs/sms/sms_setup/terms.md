---
page_order: 1
nav_title: "Begriffe, die Sie kennen sollten"
article_title: SMS-Begriffe zum Kennenlernen
alias: /sms_terms_to_know/

layout: glossary_page
glossary_top_header: "Terms to Know"
glossary_top_text: "SMS–everyone has it and knows what it is. What they don't know is the nuance. Check out the following terms to learn more about SMS ecosystems, technologies, and processes."
page_type: glossary
description: "Dieses Glossar definiert verschiedene SMS-Begriffe, die Sie kennen sollten."
channel: SMS 

glossaries:
  - name: SMS (Kurznachrichtendienst)
    description: "Ein 1980 geschaffener Nachrichtenkanal und eine der ältesten Texting-Technologien. Außerdem ist es einer der am weitesten verbreiteten und am häufigsten genutzten Kanäle für Textnachrichten. Über diesen Kanal erreichen Sie Ihre Nutzer:innen und Kund:innen direkter als über die meisten anderen Messaging-Kanäle, da er ihre persönliche Telefonnummer nutzt, um sie zu erreichen. Daher gelten für SMS mehr Regeln und Vorschriften als für andere Nachrichtenkanäle."
  - name: Kurzcode
    description: "Dabei handelt es sich um eine kurze, einprägsame 5- bis 6-stellige Sequenz, die es den Absendern ermöglicht, mehr Nachrichten mit gleichmäßigeren Raten zu versenden als lange Nummern (eine Nachricht pro Sekunde).<br><br>Es ist entweder ein kurzer oder ein langer Code erforderlich."
  - name: Langcode
    description: "Dies ist die standardmäßige, 10-stellige Telefonnummer (in den meisten Ländern), die es dem Absender ermöglicht, mehrere Nachrichten mit einer Geschwindigkeit von einer Nachricht pro Sekunde zu versenden.<br><br>Es ist entweder ein kurzer oder ein langer Code erforderlich."
  - name: Kodierung
    description: Die Umwandlung von etwas in eine kodierte Form. SMS-Inhalte können entweder in GSM-7 oder UCS-2 kodiert werden.
  - name: GSM-7 Kodierung (Globales System für mobile Kommunikation)
    description: "GSM-7 ist der gängigste Kodierungsstandard für die meisten SMS-Nachrichten. Es verwendet die meisten der griechischen und englischen Alphabete sowie einige zusätzliche Zeichen. Mehr über die GSM-7-Kodierung und welche Zeichensätze Sie verwenden können, erfahren Sie unter <a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title=\"GSM 7-bit default alphabet and extension tableWikipedia\"></a>. Sprachen wie Chinesisch, Koreanisch oder Japanisch müssen mit der 16-Bit UCS-2-Zeichenkodierung übertragen werden. <br> <br> Sie können davon ausgehen, dass das Zeichenlimit pro Segment bei dieser Art der Kodierung bei 128 Zeichen liegt."
  - name: UCS-2-Kodierung (Universal Coded Character Set)
    description: "Die UCS-2-Kodierung ist ein Fallback-Kodierungsstandard, insbesondere wenn eine Nachricht nicht mit GSM-7 kodiert werden kann oder wenn eine Sprache mehr als 128 Zeichen für die Darstellung benötigt. USC-2 wird besser in <a href='https://en.wikipedia.org/wiki/Code_point'>Codepunkten</a> als in \"Zeichen\" gemessen. Unabhängig davon können Sie davon ausgehen, dass das Zeichenlimit pro Segment für diese Art der Kodierung 67 Zeichen beträgt."
  - name: Abonnementgruppen für SMS
    description: "Abonnementgruppen sind ein Tool von Braze, mit dem Sie bestimmte Abonnementstufen von Benutzern oder Kunden ansprechen können. Abonnementgruppen für SMS werden intern auf der Grundlage Ihres Nachrichtendienstes erstellt und können nicht über Arbeitsbereiche hinweg gemeinsam genutzt werden."
  - name: Nachrichtensegmente
    description: "Ein Nachrichtensegment ist eine Gruppierung von bis zu einer bestimmten Anzahl von Zeichen (160 bei GSM-7-Kodierung; 67 bei UCS-2-Kodierung), die in einer einzigen SMS versendet werden. Wenn Sie eine SMS mit 161 Zeichen in GSM-7-Kodierung versenden, werden Sie feststellen, dass zwei (2) Nachrichtensegmente gesendet wurden. Das Versenden mehrerer Nachrichtensegmente kann zu zusätzlichen Kosten führen."
  - name: Messaging-Dienst
    description: "Eine Sammlung von langen Codes, kurzen Codes und alphanumerischen IDs, die für den Versand Ihrer SMS mit Braze verwendet werden."
  - name: Schlüsselwort
    description: "Ein kurzes Wort, das an einen kurzen oder langen Code gesendet wird, um mit einem vordefinierten SMS-Programm zu interagieren oder um das OPT-OUT eines bestimmten Programms oder aller Programme eines Codes zu verlangen. Zum Beispiel, <code>STOP</code>. Schlüsselwörter sollten <br> - alphanumerisch sein <br> - keine Leerzeichen haben <br> - weniger als 10 Zeichen sein. <br> <br> Eine bestimmte Kombination aus Schlüsselwort und Kurzcode kann jeweils nur für ein aktives Programm verwendet werden. Wenn Sie ein Schlüsselwort eingeben, das bereits von einem anderen Programm verwendet wird, erscheint ein Validierungsfehler. <br> <br> Es gibt zwei verpflichtende Schlüsselwortkategorien, die alle Anbieter von SMS-Inhalten einhalten müssen: <code>STOPP</code> und <code>HILFE</code>."
  - name: Pflichtfeld Schlüsselwort HELP
    description: "Für jedes Programm, das in der SMS Campaign Manager-Plattform erstellt wird, muss der Inhalt für dieses Schlüsselwort bereitgestellt werden. Er muss den Best Practices und der Konformität mit dem Netzbetreiber für das Land oder die Region entsprechen, in dem der SMS-Verkehr gesendet und empfangen wird. In den meisten Fällen sollte dieser Inhalt eine kurze Erläuterung des SMS-Programms und die Möglichkeit zum OPT-OUT enthalten."
  - name: Global STOP Schlüsselwörter
    description: "Variationen sind <code>STOP</code>, <code>END</code>, <code>QUIT</code>, <code>UNSUBSCRIBE</code>, <code>CANCEL</code>, <code>STOPALL</code>. Diese werden als <code>Global-Stop-Keywords</code> bezeichnet. Wenn eines dieser Schlüsselwörter in einen Kurz- oder Langcode eingegeben wird, führt dies dazu, dass die Handynummer (die Nummer des Absenders) von allen aktiven SMS-Programmen, die mit diesem Code verbunden sind, abgemeldet wird."
  - name: Vanity Code
    description: "Eine Vanity-Kurznummer ist eine 5-6-stellige Telefonnummer, die speziell von einer Marke ausgewählt wird. Vanity-Kurznummern sind gebrandet und für die Verbraucher leichter zu merken."
  - name: Gemeinsamer Shortcode
    description: "Wenn Sie eine gemeinsame Kurzwahlnummer verwenden, werden alle Textnachrichten, unabhängig davon, von welchem Unternehmen oder welcher Organisation sie gesendet werden, von derselben 5-6-Telefonnummer auf dem mobilen Gerät des Verbrauchers empfangen. Gemeinsame Kurzwahlen sind zwar relativ kostengünstig und sofort verfügbar, aber das bedeutet, dass Ihr Unternehmen keine eigene Kurzwahlnummer hat und davon abhängig ist, dass andere Unternehmen das korrekte Protokoll mit Ihrer gemeinsamen Kurzwahlnummer befolgen." 
  - name: Alphanumerische Sender-ID
    description: "Mit der alphanumerischen Sender-ID können Sie Ihren Firmennamen oder Ihre Marke als Sender-ID mit alphanumerischen Zeichen festlegen, wenn Sie Ein-Weg-Nachrichten in unterstützte Länder senden."
  - name: Gebührenfreie Nummer
    description: "Eine gebührenfreie Telefonnummer ist eine Telefonnummer, bei der alle ankommenden Anrufe in Rechnung gestellt werden, anstatt dass dem anfragenden Abonnenten:in Kosten entstehen. Gebührenfreie Nummern in den USA und Kanada sind SMS-fähig, bei denen die Teilnehmer:innen für ein- und ausgehende Texte bezahlen müssen.<br><br>Gebührenfreie Nachrichten eignen sich am besten für den Einsatz von Mensch zu Mensch, z. B. für den Kundensupport oder den Vertrieb, wobei sowohl der Absender als auch der Empfänger ein Gespräch per Text führen."
  - name: Ein-Weg-Messaging
    description: "Mit Ein-Weg-Messaging können Sie mit Ihren Kund:innen durch das Versenden von Nachrichten kommunizieren. Ein-Weg-Messaging ist nützlich, wenn Sie eine alphanumerische Sender-ID in Märkten implementieren, in denen Lang- und Shortcodes nicht verfügbar sind." 
  - name: Zwei-Wege-Messaging
    description: "Mit Zwei-Wege-Messaging können Sie ein Gespräch führen, indem Sie sowohl Nachrichten senden als auch empfangen." 
---
