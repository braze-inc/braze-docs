
# SMS und RCS Absender

> In diesem Artikel erfahren Sie mehr über die wichtigsten Konzepte für das Senden von Telefonnummern mit Braze.

## Arten von SMS- und RCS-Sendern

{% tabs %}
{% tab RCS-überprüfter Sender %}

#### RCS-verifizierter Sender

Ein RCS-verifizierter Sender ist eine visuelle Darstellung Ihrer Marke, die einen Markennamen, ein Logo, eine optionale Beschriftung und ein überprüftes Badge enthält. Dies verschafft dem RCS-verifizierten Sender einen erheblichen Vorteil gegenüber SMS Codes, wenn es darum geht, das Vertrauen der Nutzer:innen zu gewinnen.  

##### Details

| Visuelle Komponenten | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| \- Markenname<br>\- Logo<br>\- optionale Beschriftung<br> \- überprüftes Badge | 4-6 Wochen für eine Bewerbung (kann variieren) | Ungefähr 100 Messages pro Sender pro Sekunde. Die tatsächliche Durchsatzrate kann je nach Anbieter, Netzwerkbedingungen und spezifischen Implementierungsdetails variieren. | Kein:e | 2-Wege |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

##### Pro und Kontra

| Profis |
| ---- |
| **Vertrauen schaffen**<br> RCS-verifizierte Absender sind weitaus effektiver beim Aufbau von Nutzer:innen-Vertrauen als SMS Codes, da sie sehr visuell sind und vom Betreiber ausdrücklich überprüft werden. 
<br><br>**Umfangreiche Features für Messaging**<br>RCS-überprüfte Absender ermöglichen den Versand von Nachrichten mit umfangreicheren Messaging-Funktionen als SMS, einschließlich Rich Media, wie Bilddateien und interaktive Buttons. |
{: .reset-td-br-1}

| Nachteile |
| ---- |
| **Neuheit und dynamischer Charakter des Marktes**<br> RCS ist ein relativ neues Protokoll, was bedeutet, dass sich die Netzabdeckung, die Zustellbarkeit und die Preise in den verschiedenen Regionen unterschiedlich schnell entwickeln. Die jüngste Zustimmung von Apple, RCS zu unterstützen, bedeutet jedoch, dass die große Mehrheit der Nutzer:innen von Smartphones nun über dieses Protokoll erreichbar ist. <br><br>**Höhere Kosten für Rich Messaging**<br> RCS-Nachrichten, die viele Rich Messaging-Funktionen nutzen, kosten tendenziell mehr pro Nachricht als SMS-Nachrichten. Das ist angesichts der Vorteile umfangreicher Features nicht überraschend, kann aber für Ihr Marketing-Budget von Bedeutung sein. |
{: .reset-td-br-1}

{% endtab %}
{% tab SMS Shortcodes %}

#### SMS Shortcodes

Ein Kurzcode ist eine einprägsame 5- bis 6-stellige Sequenz, die es Absendern ermöglicht, Nachrichten mit höherer Geschwindigkeit zu versenden als lange Codes. Dies macht Short Codes perfekt für zeitkritische Sendungen mit hohem Volumen.

##### Details

| Länge | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| 5-6 Ziffern | 8-12 Wochen Anwendung| 100 Nachrichten pro Sekunde oder mehr | Ja | 2-Wege |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pro und Kontra

| Profis |
| ---- |
| **Geschwindigkeit und Skalierbarkeit**<br> Short Codes bieten Geschwindigkeit und Skalierbarkeit mit Übertragungsraten von 100 Segmenten pro Sekunde, 6.000 Segmenten pro Minute, 360 Tausend Segmenten pro Stunde und 1 Million Segmenten pro 2 Stunden. Kurzwahlnummern können aufgrund der Überprüfung, die während des Antragsverfahrens für Kurzwahlnummern erforderlich ist, so hohe Raten erreichen.<br><br>**MMS für einige Kurznummern aktiviert**<br>Einige Kurzwahlnummern unterstützen MMS, auch bekannt als Multimedia Message Service. Damit können Sie Nachrichten mit Multimedia-Inhalten (JPEG, GIF, PNG) an Mobiltelefone senden. Weitere Informationen über MMS bei Braze finden Sie unter [Über MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/about_mms/). |
{: .reset-td-br-1}

| Nachteile |
| ---- |
| **Kurzwahlen sind in weniger Ländern verfügbar**<br> Kurzwahlnummern sind derzeit in einigen Ländern verfügbar, darunter in den USA, Großbritannien und Kanada.<br><br>**Längerer Bewerbungsprozess**<br> Ein aufwendiger Bewerbungsprozess, bei dem die Anwendungsfälle sehr detailliert beschrieben werden müssen, ist erforderlich. Dies ist notwendig, um die Zustellbarkeit zu unterstützen, da die Netzbetreiber nach der Vergabe eines Shortcodes zwar die Shortcodes prüfen, die Nachrichten aber **nicht** filtern, so dass höhere Versandraten möglich sind. Die Dauer dieses Prozesses variiert je nach Land.<br><br>**Höhere Kosten**<br> Kurze Codes kosten mehr als lange Codes und es dauert länger, bis sie genehmigt werden. Wenn Sie jedoch eine Kurznummer haben, gelten Sie als "vorgenehmigt", um Nachrichten zu besseren und schnelleren Tarifen zu versenden, und werden während des Sendevorgangs weniger genau überprüft, da Sie bei der Beantragung der Kurznummer bereits alle Prüfungen durchlaufen haben. |
{: .reset-td-br-1}

{% endtab %}
{% tab SMS Langcodes %}

#### SMS-Langcodes

Eine lange Vorwahl ist eine Standardtelefonnummer, die zum Senden und Empfangen von Sprachanrufen und SMS-Nachrichten verwendet wird. Telefonnummern werden in der Regel als "lange Codes" (in vielen Ländern 10-stellige Nummern) bezeichnet, wenn man sie mit SMS-Kurznummern (5-6-stellige Nummern) vergleicht.

##### Details

| Länge | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| 10 Ziffern | 4-6 Wochen Antragszeit (kann für verschiedene Länder kürzer oder länger sein) | In den USA hängt der Durchsatz von Ihrem 10DLC-Trust-Score ab. Auf internationalen Märkten kann der Durchsatz variieren oder unter bestimmten Umständen erhöht werden. | Ja | 2-Wege (je nachdem, wohin Sie senden) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pro und Kontra

| Profis |
| ---- |
| **Kann sofort zum Versenden von Nachrichten verwendet werden (für bestimmte Länder)**<br>Lange Codes sorgen für ein lokalisiertes und persönliches Kundenerlebnis, wenn Sie Nachrichten von Person zu Person versenden. Im Gegensatz zu SMS-Kurzcodes ist der Erwerb eines langen Codes in einigen Ländern ein recht schneller Prozess. (Für andere Länder dauert es genauso lange oder länger als ein Kurzcode.). Lange Codes können auch als Ausweichnummer festgelegt werden, wenn ein kurzer Code nicht funktioniert.<br><br>**Größere Verfügbarkeit weltweit**<br>Lange Codes sind in über 100 wichtigen Ländern weltweit verfügbar. Bitte wenden Sie sich an Ihren Customer Success Manager oder den [Braze-Support]({{site.baseurl}}/braze_support/), um eine Liste der verfügbaren Länder zu erhalten.<br><br>**MMS für bestimmte Länder aktiviert**<br>Unterstützt MMS, auch bekannt als Multimedia Message Service, so dass Sie Nachrichten mit Multimedia-Inhalten (JPEG, GIF, PNG) an Mobiltelefone senden können. Weitere Informationen über MMS bei Braze finden Sie in unserer Dokumentation [hier]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/about_mms/).|
{: .reset-td-br-1}

| Nachteile |
| --- |
| **Langsamere Sendegeschwindigkeiten**<br>Lange Codes können nicht mit der Geschwindigkeit und dem Versand von kurzen Codes mithalten. Die Preise für den SMS-Versand hängen von Ihrem 10DLC-Vertrauensindex in den USA ab. |
{: .reset-td-br-1}

{% endtab %}
{% tab SMS Vanity Shortcode %}

#### SMS Vanity Shortcodes

Eine Vanity-Kurznummer ist eine 5-6-stellige Telefonnummer, die speziell von einer Marke ausgewählt wird. Vanity-Kurznummern haben ein Markenzeichen und sind für die Verbraucher leichter zu merken, sind aber in der Regel teurer. Zum Beispiel:
- Die Gesundheitsbehörde von New York City hat einen Vanity Short Code `692-692`, der auf einer Telefontastatur NYC-NYC buchstabiert.
- Amazon verwendet für die Aktualisierung der Sendungsverfolgung den Kurzcode `262-966`, der mit AMA-ZON geschrieben wird.
- PayPal verwendet für SMS-Befehle den Kurzcode `729-725`, der PAY-PAL buchstabiert.<br><br>

##### Details

| Länge | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| 5-6 Ziffern | 8-12 Wochen Anwendung | 100 Nachrichten pro Sekunde | Ja | 2-Wege |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pro und Kontra

| Profis |
| ---- |
| **Geschwindigkeit und Skalierbarkeit**<br> Short Codes bieten Geschwindigkeit und Skalierbarkeit mit Übertragungsraten von 100 Segmenten pro Sekunde, 6.000 Segmenten pro Minute, 360 Tausend Segmenten pro Stunde und 1 Million Segmenten pro 2 Stunden. Kurzwahlnummern können aufgrund der Überprüfung, die während des Antragsverfahrens für Kurzwahlnummern erforderlich ist, so hohe Raten erreichen.<br><br>**MMS aktiviert**<br>Unterstützt MMS, auch bekannt als Multimedia Message Service, so dass Sie Nachrichten mit Multimedia-Inhalten (JPEG, GIF, PNG) an Mobiltelefone senden können. Weitere Informationen über MMS bei Braze finden Sie unter [Über MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/about_mms/). |
{: .reset-td-br-1}

| Nachteile |
| ---- |
| **Kurzcodes sind nicht überall verfügbar**<br> Kurznummern sind derzeit nur in den **USA und Kanada (CA)** verfügbar.<br><br>**Längerer Bewerbungsprozess**<br> Ein 8-12-wöchiger Bewerbungsprozess, bei dem die Anwendungsfälle sehr detailliert beschrieben werden müssen, ist erforderlich. Dieser aufwändige Prozess ist notwendig, um die Zustellbarkeit zu unterstützen, denn nach der Vergabe eines Short Codes prüfen die Netzbetreiber die Short Codes, filtern die Nachrichten aber **nicht**, so dass höhere Versandraten möglich sind.<br><br>**Höhere Kosten in den USA**<br> In Kalifornien gibt es keine zusätzlichen Kosten für kurze Codes, aber in den USA kosten kurze Codes mehr als lange Codes und es dauert länger, bis sie genehmigt werden. Wenn Sie jedoch eine Kurznummer haben, gelten Sie als "vorgenehmigt", um Nachrichten zu besseren und schnelleren Tarifen zu versenden, und werden während des Sendevorgangs weniger genau überprüft, da Sie bei der Beantragung der Kurznummer bereits alle Prüfungen durchlaufen haben. |
{: .reset-td-br-1}

{% endtab %}
{% tab SMS Alphanumerische Sender ID %}

#### SMS alphanumerische ID des Absenders

Absender-IDs sind die kurzen oder langen Codes, die oben in einer SMS-Nachricht erscheinen und angeben, von wem die Nachricht gesendet wurde. Wenn ein Benutzer mit einer Absender-ID nicht vertraut ist, kann er sich dafür entscheiden, diese Nachrichten ganz zu ignorieren. Durch die Verwendung von alphanumerischen Absender-IDs können Nutzer schnell erkennen, von wem sie Nachrichten erhalten, was die Öffnungsrate erhöht. 

Mit alphanumerischen Absender-IDs können Sie Ihren Firmennamen oder Ihre Marke (z. B. „Kitchenerie“ oder „CashBlastr“) als Absender-ID festlegen, wenn Sie Einwegnachrichten an mobile Benutzer senden. Sie können bis zu 11 Zeichen lang sein und akzeptieren Groß- (A-Z) und Kleinbuchstaben (a-z), Leerzeichen und Ziffern (0-9). Es **kann nicht** nur Zahlen geben. 

##### Details

| Länge | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| Bis zu 11 Zeichen | Sofort verfügbar, wenn keine Vorregistrierung erforderlich ist | Variiert je nach Land | Kein:e | 1-Weg |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pro und Kontra

| Profis | Nachteile |
| ---- | ---- | 
| {::nomarkdown} <ul> <li> Keine zusätzlichen Kosten für die Implementierung </li> <li> Verbessert das Markenbewusstsein </li> <li> Erhöht die Öffnungsrate von SMS </li> <li> Passt die Sendegeschwindigkeit von Telefonnummern innerhalb der Abonnementgruppe an </li> <li> Sofort verfügbar, wenn keine Vorregistrierung erforderlich ist </li> </ul> {:/} | {::nomarkdown} <ul> <li> <a href='/docs/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses/'>Zwei-Wege-Nachrichten</a> werden nicht unterstützt </li> <li> Nicht alle Länder unterstützen diese Funktion </li> <li> Einige Länder verlangen ein zusätzliches Genehmigungsverfahren </li> <li> MMS ist nicht aktiviert </li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2}

Für weitere Informationen zur alphanumerischen Absender-ID wenden Sie sich bitte an Ihren Customer-Success-Manager.
{% endtab %}
{% tab SMS-Gebührenfreie Nummer %}

#### SMS-fähige gebührenfreie Nummer

Eine gebührenfreie Telefonnummer ist eine Telefonnummer, bei der alle ankommenden Anrufe in Rechnung gestellt werden, anstatt dass bei den anfragenden Teilnehmer:innen Gebühren anfallen. Gebührenfreie Nummern in den USA und Kanada sind SMS-fähig, bei denen die Teilnehmer:innen für ein- und ausgehende Texte bezahlen müssen.

##### Details

| Länge | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| 10 Ziffern	 | 2-4 Wochen Anwendung | Hängt von Ihrer Zulassung ab und kann durch höhere Zahlungen erhöht werden | Kein:e | 2-Wege |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pro und Kontra

| Profis | Nachteile |
| ---- | ---- | 
| {::nomarkdown} <ul> <li> Muss vor dem Versand registriert werden. </li> </ul> {:/} | {::nomarkdown} <ul> <li> Gebührenfreie Nummern sind nur für die USA und Kanada </li><li> MMS ist nicht aktiviert </li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2} 

{% endtab %}
{% endtabs %}

{% alert important %}
Wenn der Durchsatz überschritten wird, können einige Nachrichten fehlschlagen.
{% endalert %}

Abgesehen von diesen Unterschieden sollten Sie wissen, dass eine Marke in der Regel einen kurzen Code hat, aber mehrere lange Codes als Reserve, je nachdem, wie viele Empfänger sie plant, SMS zu versenden.

{% alert important %}
Sie fragen sich, was es mit gemeinsamen Kurzcodes auf sich hat? Wenn Sie mehr darüber erfahren möchten, warum wir empfehlen, von gemeinsam genutzten Kurzcodes Abstand zu nehmen, besuchen Sie das Thema in unseren [SMS-FAQ]({{site.baseurl}}/sms_faq/).
{% endalert %}

## Telefonnummern für den SMS-Versand

Kurz- und Langvorwahlen sind die Telefonnummern, von denen aus Sie Nachrichten an Ihre Benutzer oder Kunden senden. Sie können 5- bis 6-stellige Shortcodes oder 10-stellige Langcodes sein. Jede Art von Code bietet spezifische Vorteile und alle Faktoren sollten berücksichtigt werden, bevor Sie sich entscheiden, ob Sie einen Kurzcode benötigen und welche Art von Kurzcode Sie zusätzlich zu dem Ihnen bereits zugewiesenen Langcode benötigen.

## Wie erhalte ich einen SMS Shortcode?

Die Beantragung eines Kurzcodes kann ein langwieriger Prozess sein. Aber es kann sich lohnen! Wenn Sie einen Kurzcode wünschen, wenden Sie sich an Ihren Onboarding-Manager oder einen anderen Braze-Mitarbeiter und lassen Sie es ihn wissen. Nachdem Sie das getan haben, wird man einen Antrag für Sie stellen - man wird Sie nach einigen grundlegenden Informationen fragen, die Ihnen helfen, sich zu qualifizieren. Dann brauchen Sie nur noch zu warten!

### Kurzcode-Anwendung

Braze ist zwar für die eigentliche Beantragung des Kurzcodes verantwortlich, aber wir benötigen einige Informationen von Ihnen. Wir empfehlen Ihnen, diese Fragen durchzugehen, bevor Sie sich an Braze wenden. 

Die Vorschriften verlangen, dass es Antworten auf alle Opt-In-, Opt-Out- und Hilfe/Info-Schlüsselwortantworten gibt. Sie müssen uns die spezifischen Nachrichtenflüsse (die Antworten, die Sie an Benutzer senden möchten, nachdem sie ein [Schlüsselwort]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/) gesendet haben) mitteilen, die Sie für die folgenden Situationen wünschen.

| Benötigter Fluss | Typ | Beispiel |
| ----------- | ---- | ------- |
| Opt-In <br><br>Doppeltes Opt-In| SMS | `Welcome to our SMS system! Reply "YES" to receive updates from our company. Respond "STOP" to opt-out and "HELP" for more info.` |
| Opt-In | Website | `Hi there, would you like to sign up for SMS? Text "START" to "23456". Or, enter your number below.` |
| Opt-out | SMS | `Sorry to see you go! If this was a mistake, text back "UNSTOP". Text "HELP" for more information.` |
| Hilfe | -- | `Our company is a company that does this and that. For more info on the company, let us know here. Or, you can contact support at 1-800-111-1111.` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Je nach Ihrer Situation müssen Sie mehr oder weniger Bewegungen wie die in der vorangegangenen Tabelle aufgeführten bereitstellen. Sie müssen uns auch **drei allgemeine Beispiele** für Nachrichten mitteilen, die Sie per SMS versenden möchten - fragen Sie Ihren Braze-Vertreter um Rat.

Außerdem müssen Sie uns unabhängig von der von Ihnen verwendeten Nummer mitteilen, wie viele Nachrichten Sie pro Monat versenden möchten.

{% alert important %}
Wenn Sie einen eigenen Kurzcode haben, wenden Sie sich während des Einführungsprozesses an Ihren Customer Success Manager, um die Migration oder Übertragung Ihres Kurzcodes zu besprechen. Die Kurzcodes müssen von Ihrem Customer Success Manager eingerichtet werden.
{% endalert %}

## SMS Application-to-Person 10-Digit Long Codes (A2P 10DLC)

A2P 10DLC bezieht sich auf ein System in den Vereinigten Staaten, das es Unternehmen ermöglicht, Nachrichten vom Typ Application-to-Person (A2P) über einen standardmäßigen 10-stelligen langen Code (10DLC) zu versenden. 10-stellige lange Codes wurden traditionell für den Person-to-Person (P2P)-Verkehr entwickelt, was dazu führte, dass Unternehmen durch einen begrenzten Durchsatz und verstärkte Filterung behindert wurden. Dieser Service trägt dazu bei, diese Probleme zu lösen, indem er die Zustellbarkeit von Nachrichten insgesamt verbessert, es Marken ermöglicht, Nachrichten in großem Umfang zu versenden, einschließlich Links und Aufforderungen zum Handeln, und hilft, die Verbraucher vor unerwünschten Nachrichten zu schützen. 

Alle Kunden, die derzeit US-Langcodes haben und/oder verwenden, um an US-Kunden zu senden, müssen ihre Langcodes für 10DLC registrieren. Dieses Bewerbungsverfahren dauert 4-6 Wochen. Wenn Sie mehr über die Besonderheiten von 10DLC erfahren möchten und warum es erforderlich ist, besuchen Sie unseren speziellen [10DLC-Artikel]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/).

## Häufig gestellte Fragen

### Wie ist der Durchsatz von RCS Nachrichten im Vergleich zum Durchsatz von SMS Nachrichten?

Der Durchsatz von RCS Nachrichten ist nicht so streng definiert oder vom Netzbetreiber kontrolliert wie bei SMS. Da RCS Nachrichten über Datennetzwerke und nicht über die traditionellen zellularen Signalisierungskanäle der SMS versendet werden, ist RCS nicht wie die SMS auf feste netzwerkbedingte Grenzen angewiesen. 

### Unterstützen RCS-verifizierte Absender einen hohen Durchsatz an Nachrichten wie einen Shortcode?

Nein. RCS-überprüfte Absender haben nicht die Möglichkeit, einen separaten hohen Durchsatz an Nachrichten zu erhalten.

### Kann ein RCS-verifizierter Sender von mehreren Abo-Gruppen gemeinsam genutzt werden? 

Nein. Ähnlich wie bei einem SMS-Sender kann ein RCS-verifizierter Sender nur mit einer einzigen Abo-Gruppe verwendet werden.

### Kann ein SMS Fallback-Sender von mehreren Abo-Gruppen gemeinsam genutzt werden?

Nein. SMS Fallback-Sender können nur mit einer einzigen Abo-Gruppe verwendet werden.


