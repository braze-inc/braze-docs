# SMS und RCS Absender

> Dieser Artikel bietet eine Übersicht über die Codes und Absender, die für den Versand von SMS- und RCS-Nachrichten verfügbar sind.

## Arten von SMS- und RCS-Sendern

{% tabs %}
{% tab RCS-Verified Sender %}

#### RCS-verifizierter Sender

RCS ist ein modernes Messaging-System, das mehr Features als herkömmliche SMS bietet und Möglichkeiten wie Marken-Absender-IDs, Rich Media und interaktive Inhalte wie scrollbare Karussells, Schnellantworten, CTA-Buttons und vieles mehr einführt. Es wurde entwickelt, um eine elegantere und mehr engagement fördernde Benutzererfahrung zu bieten.  

##### Details

| Visuelle Komponenten | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| \- Markenname<br>\- Logo<br>\- optionale Beschriftung<br> \- überprüftes Badge | 4–6 Wochen für die Genehmigung durch den Spediteur | Der Durchsatz und die Zustellung hängen davon ab, dass der Empfänger:in über eine aktive Datenverbindung (mobile Daten oder WLAN) verfügt. RCS unterliegt keinen festen netzwerkseitigen Beschränkungen wie SMS. RCS-Nachrichten werden über Datennetzwerke gesendet und nicht über die herkömmlichen Mobilfunk-Messaging-Kanäle, die von SMS genutzt werden. | -- | 2-Wege |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Pro und Kontra

| Profis |
| ---- |
| **Überprüftes Vertrauen und Markenbildung**<br> Im Gegensatz zu herkömmlichen SMS, bei denen Ihre Marke als zufälliger 5-stelliger Shortcode oder Langcode erscheint, ermöglicht RCS verifizierte Profile von Absendern. Diese Profile umfassen das Logo Ihrer Marke, den Namen und ein Häkchen, mit dem die Echtheit überprüft wird. |
| **Umfangreiche Features für Messaging**<br> RCS unterstützt Karussells, hochauflösende Videos und Aktions-Buttons für vorgeschlagene Aktionen (wie „Jetzt buchen“, „Tracking des Pakets“ oder „Rechnung bezahlen“). Nutzer:innen können komplexe Aufgaben ausführen, ohne ihre Messaging-App zu verlassen, was zu höheren Konversionsraten als bei einem einfachen Textlink führen kann. |
{: .reset-td-br-1 role="presentation"}

| Nachteile |
| ---- |
| **Fragmentierte Unterstützung**<br> Obwohl Google RCS für Android stark gepushed hat und Apple kürzlich RCS-Unterstützung für iOS eingeführt hat, kann die Umsetzung je nach Netzbetreiber und Region noch uneinheitlich sein. Wenn das Mobiltelefon oder der Mobilfunkanbieter eines Nutzers RCS nicht unterstützt, wird die Nachricht in der Regel als einfache SMS versendet, wodurch alle „erweiterten” RCS-Features verloren gehen. |
| **Plattforminkonsistenzen**<br> Das RCS-Erlebnis variiert je nach Mobilfunkanbieter, Gerätemodell und der verwendeten Messaging-App des Empfängers (z. B. Google Messages oder iMessage). |
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% tab SMS Short Codes %}

#### SMS Shortcodes

Ein Shortcode ist eine 5- bis 6-stellige Nummer, mit der SMS schneller als mit Langcodes an Mobiltelefone gesendet und von diesen empfangen werden können. Für den Versand großer Mengen und zeitkritischer Nachrichten werden Shortcodes empfohlen.

In einigen Ländern ist es zulässig, gegen eine erhöhte Gebühr eine bestimmte Nummer auszuwählen. Diese Shortcodes werden als Vanity-Shortcodes bezeichnet. Sollten Sie Interesse an Vanity-Shortcodes haben, wenden Sie sich bitte an Ihre Braze-Konto-Vertretung, um weitere Informationen zu erhalten.

##### Details

| Länge | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| 5-6 Ziffern | 4-12 Wochen Anwendung| 100 Nachrichten pro Sekunde oder mehr | Ja | 2-Wege |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Pro und Kontra

| Profis |
| ---- |
| **Geschwindigkeit und Skalierbarkeit**<br> Shortcodes sind speziell für hohen Datenverkehr ausgelegt. Sie können Nachrichten schneller versenden als Langcodes und da sie direkt von den Netzbetreibern vorab geprüft werden, ist das Risiko, dass sie von automatisierten Spam-Filtern markiert werden, am geringsten. |
| **Leicht zu merkende „Call to Action“-Botschaft**<br> Für Marketing-Kampagnen (z. B. „Senden Sie WIN an 55555“) ist ein Shortcode für Nutzer:innen wesentlich einfacher zu merken und einzugeben als eine 10-stellige Nummer. Dies macht Shortcodes zum bevorzugten Standard für Radio-, Fernseh- und Plakatwerbung, bei der die Nutzer:innen nur wenige Sekunden Zeit haben, die Nummer zu sehen oder zu hören. |
{: .reset-td-br-1 role="presentation"}

| Nachteile |
| ---- |
| **Kurzwahlen sind in weniger Ländern verfügbar**<br> Shortcodes sind nicht in allen Ländern verfügbar. Bitte wenden Sie sich an Ihr Braze-Konto-Team, um sich über die Länder zu informieren, in die Sie Nachrichten versenden möchten. |
| **Längerer Bewerbungsprozess**<br> Im Gegensatz zu Langcodes und alphanumerischen Absender-IDs, die manchmal innerhalb von 1–2 Wochen bereitgestellt werden können, kann die Bereitstellung eines Shortcodes 4–12 Wochen oder länger dauern. Jeder große Mobilfunkanbieter muss Ihre spezifische Anwendung manuell genehmigen, bevor der Code in seinem Netzwerk aktiviert wird. Wenn Sie nächste Woche eine Marketingkampagne starten, ist ein Shortcode keine Option. |
| **Höhere Kosten**<br> Shortcodes sind aufgrund der Einrichtungs- und jährlichen Mietgebühren in der Regel die teuerste Art des Absenders. |
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% tab SMS Long Codes %}

#### SMS-Langcodes

Ein Langcode ist eine Standard-Telefonnummer, die zum Senden und Empfangen von SMS-Nachrichten verwendet wird. Diese Telefonnummern werden im Vergleich zu SMS-Shortcodes (5- bis 6-stellige Nummern) in der Regel als „Langcodes“ (in vielen Ländern 10-stellige Nummern) bezeichnet.

##### Details

| Länge | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| 10 Ziffern | 4-6 Wochen Antragszeit (kann für verschiedene Länder kürzer oder länger sein) | In den Vereinigten Staaten hängt der Durchsatz von Langcodes von Ihrem 10DLC-Vertrauens-Score ab. Auf internationalen Märkten kann der Durchsatz unter bestimmten Umständen variieren oder steigen, beginnt jedoch in der Regel bei etwa 10 Nachrichten-Segmenten pro Sekunde (MPS). | Ja | 2-Wege (je nachdem, wohin Sie senden) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Pro und Kontra

| Profis |
| ---- |
| **Vertrautheit und Vertrauen**<br> Langcodes ähneln privaten Telefonnummern und enthalten häufig eine Ortsvorwahl. Für Marken bedeutet dies ein Gleichgewicht zwischen professioneller Präsenz und einer persönlichen, zugänglichen Ausstrahlung. |
| **Größere Verfügbarkeit weltweit**<br>Lange Codes sind in über 100 wichtigen Ländern weltweit verfügbar. Bitte wenden Sie sich an Ihren Customer-Success-Manager oder [den Braze-Support]({{site.baseurl}}/braze_support/), um eine Liste der verfügbaren Länder zu erhalten.|
{: .reset-td-br-1}

| Nachteile |
| --- |
| **Geringere Übertragungsgeschwindigkeiten und tägliche Limite für Messaging**<br> Langcodes sind nicht wie Shortcodes für „Blast“-Marketing konzipiert. Wenn Sie versuchen, eine zeitkritische Flash-Sale-Aktion über einen Langcode an 100.000 Personen gleichzeitig zu versenden, kann es mehrere Stunden dauern, bis alle Nachrichten zugestellt sind. In den USA können Mobilfunkanbieter wie T-Mobile auch tägliche Versandlimits für 10DLC basierend auf dem Vertrauens-Score Ihrer Marke festlegen. |
| **Strengere Filter**<br> Da Langcodes wie private Telefonnummern aussehen, werden sie von den Netzbetreibern streng überwacht, um zu verhindern, dass „Person-zu-Person”-Nummern für Spam-Anrufe verwendet werden. Selbst bei einer registrierten 10DLC-Kampagne besteht ein deutlich höheres Risiko, von Netzbetreibern blockiert zu werden, wenn der Inhalt Ihrer Nachricht zu sehr an Spam erinnert oder nicht den strengen Formatierungsvorschriften entspricht, im Vergleich zu einem vorab genehmigten Shortcode. |
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% tab SMS Alphanumeric Sender ID %}

#### SMS alphanumerische ID des Absenders

Eine alphanumerische Absender-ID (oft als „Alpha“ bezeichnet) ist ein erkennbarer String, der aus einer beliebigen Kombination von Buchstaben und Zahlen besteht (häufig Ihr Firmenname oder Ihre Marke) und als Absender-ID für einseitige Textnachrichten angezeigt wird.

Sie können bis zu 11 Zeichen lang sein und Großbuchstaben (A-Z), Kleinbuchstaben (a-z), Leerzeichen und Ziffern (0-9) enthalten. Sie **dürfen nicht** ausschließlich Zahlen enthalten.

##### Details

| Länge | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| Bis zu 11 Zeichen | Sofort verfügbar, wenn keine Voranmeldung erforderlich ist. Andernfalls beträgt die Bearbeitungszeit in den meisten Ländern, in denen eine Registrierung erforderlich ist, 1 bis 4 Wochen. | Variiert je nach Land | Kein:e | 1-Weg |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Pro und Kontra

| Profis | Nachteile |
| ---- | ---- | 
| {::nomarkdown} <ul><li> Verbesserte Markenbekanntheit </li><li> In vielen internationalen Märkten registrieren und überprüfen lokale Netzbetreiber alphanumerische Absender vorab, sodass Ihre Nachrichten weniger wahrscheinlich in aggressiven Spam-Filtern der Netzbetreiber hängen bleiben, die andernfalls zufällige Langcodes blockieren könnten. </li><li> Verfügbar innerhalb einer Woche, sofern keine Voranmeldung erforderlich ist. </li></ul> {:/} | {::nomarkdown} <ul><li> <a href='/docs/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses/'>Zwei-Wege-Nachrichten</a> werden nicht unterstützt </li><li> Nicht alle Länder unterstützen diese Features. Beispielsweise wird es in Großbritannien unterstützt, jedoch in den USA gesperrt. </li><li> In einigen Ländern besteht ein umfangreiches Vorregistrierungsverfahren, das die Einreichung von Dokumentationen und längere Vorlaufzeiten erfordert. </li></ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Für weitere Informationen zu alphanumerischen Absender-IDs wenden Sie sich bitte an Ihren Customer-Success-Manager.
{% endtab %}
{% tab SMS toll-free numbers %}

#### SMS-fähige gebührenfreie Rufnummern

Gebührenfreie Nummern verfügen über eindeutige dreistellige Codes (z. B. 800, 888, 877 und 866), die es Nutzer:innen ermöglichen, Unternehmen ohne Kosten zu erreichen. Sie werden häufig für den Kundenservice eingesetzt und können auch alle Arten von A2P-Nachrichten (Application-to-Person) verarbeiten, einschließlich Marketing.

##### Details

| Länge | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| 10 Ziffern	 | 2-4 Wochen Anwendung | Beginnt bei 3 MPS (Segmente pro Sekunde), kann gegen Aufpreis erhöht werden. | Ja | 2-Wege |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Pro und Kontra

| Profis |
| ---- |
| **Professionelles Image**<br> Gebührenfreie Rufnummern sind in Nordamerika für die geschäftliche Kommunikation weithin anerkannt und genießen hohes Vertrauen, da sie einen professionellen und seriösen Eindruck vermitteln. |
| **Flexibler Durchsatz; keine Beschränkungen beim Versand durch den Absender**<br> Im Gegensatz zu Standard-Langcodes, bei denen je nach Land Durchsatz- oder Versandbeschränkungen durch den Netzbetreiber gelten können, kann bei gebührenfreien Nummern der Durchsatz erhöht werden, um höhere Volumina zu unterstützen, und es gibt in den USA keine täglichen Versandbeschränkungen durch den Netzbetreiber.|
{: .reset-td-br-1 role="presentation"}

| Nachteile |
| --- |
| **Unpersönlichkeit und geografische Neutralität**<br> Da gebührenfreie Nummern keinen Ortscode haben, können sie einen zu „unternehmerischen“ oder anonymen Eindruck vermitteln. Für ein lokales Dienstleistungsunternehmen kann eine gebührenfreie Nummer weniger effektiv sein als ein Standard-Langcode, da sie keine lokale Verbindung aufweist und manchmal mit einer beliebigen Telemarketing-Nummer verwechselt werden kann. |
| **Zusätzliche Ebene der STOP-Filterung**<br> Gebührenfreie Nummern verfügen über eine Opt-out-Funktion außerhalb von Braze, die nicht entfernt oder angepasst werden kann. Wenn ein Nutzer:in „STOP” an Ihre gebührenfreie Nummer sendet, wird er von weiteren Nachrichten von Ihrer Nummer abgemeldet und erhält eine vom Netzwerk generierte automatische Antwort. Sie werden keine weiteren Nachrichten von Ihrer gebührenfreien Nummer erhalten, bis sie „START“ senden, um aus der Sperrliste der gebührenfreien Nummer entfernt zu werden. |
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% endtabs %}

## Einrichtung

Die Einrichtungsanforderungen und Zeitpläne variieren je nach Typ des Absenders und dem Land, in dem der Absender bereitgestellt wird.

{% tabs local %}
{% tab RCS-verified sender %}

### RCS-verifizierter Sender

RCS-überprüfte Sender werden auf Länderbasis bereitgestellt. Der Verifizierungs- und Einrichtungsprozess konzentriert sich auf Ihren Agenten oder Absender – die digitale Person, die mit den Nutzer:innen interagiert. Sie stellen uns Ihre Markenelemente und Verifizierungsdaten zur Verfügung.

#### Markenwerte

- **Überprüfter Name:** Der Name, den die Nutzer:innen oben im Nachrichten-Thread sehen. Es sollte sich um einen bekannten Handelsnamen handeln, nicht unbedingt um Ihren rechtlichen Firmennamen.
- **Logo:** Ein hochauflösendes Bild mit einer Größe von 224 x 224 Pixel. Dies wird in einem kreisförmigen Rahmen angezeigt, daher sollten Sie wichtige Elemente in der Mitte platzieren.
- **Banner (Hero-Bild):** Ein Hintergrundbild für Ihre Profilkarte (ähnlich wie ein Titelbild auf Facebook oder LinkedIn).
- **Markenfarbe:** Ein Hexadezimalwert für die Buttons und UI-Elemente, der dem Stil Ihres Unternehmens entspricht.

#### Details zur Überprüfung

- **Ansprechpartner:** Dies ist von entscheidender Bedeutung. Bitte geben Sie eine E-Mail-Adresse eines direkten Mitarbeiters der Marke an (keine E-Mail-Adresse einer Agentur). Google oder der Mobilfunkanbieter wird dieser Person eine E-Mail senden, um zu bestätigen, dass sie Braze autorisiert hat, in Ihrem Namen zu handeln.
- **Website und Datenschutzerklärung:** Eine aktive Website und eine Datenschutzerklärung, die erläutert, wie Sie mit Nutzerdaten und Messaging umgehen.
- **Anwendungsfallbeschreibung:** Eine klare Erklärung dessen, was Sie senden (zum Beispiel „Update zur Zustellung und Kundensupport für Einkäufe im Einzelhandel“).

Die Zeitpläne für RCS variieren je nach Land und je nachdem, wie viele Netzbetreiber den Kanal einführen. Derzeit können Sie davon ausgehen, dass ein RCS-Sender innerhalb von 3 bis 6 Wochen nach Einreichung der Anfrage für die Freischaltung von den Netzbetreibern genehmigt wird.

{% endtab %}
{% tab SMS short codes %}

### SMS Shortcodes

Shortcodes werden auf Länderbasis bereitgestellt. Je nach Land ist das Antragsverfahren für Shortcodes dafür bekannt, dass es unvorhersehbar sein kann. Braze unterstützt Sie bei jedem Schritt. Wenn Sie einen Shortcode benötigen, wenden Sie sich bitte an Ihren Onboarding-Manager oder eine andere Vertretung von Braze.

Braze unterstützt Sie bei der Zusammenstellung aller Materialien und Informationen, die für die Einreichung eines Antrags und die Konfiguration eines neuen Shortcodes erforderlich sind. Die Anforderungen variieren je nach Land, jedoch sind in vielen Fällen mindestens die folgenden Dokumente erforderlich:

| Bewerbungsunterlagen    | Beschreibung    | Anforderungen    |
|----------------------|----------------|-----------------|
| Aufruf zum Handeln (Opt-in) | Der Hauptzweck der Offenlegungen besteht darin, zu bestätigen, dass die Nutzer:innen dem Erhalt von Textnachrichten zustimmen und die Art des Programms verstehen. | {::nomarkdown}<ul><li>Produkt Beschreibung</li><li>Offenlegung der Häufigkeit von Nachrichten</li><li>Vollständige Geschäftsbedingungen ODER Link zu den vollständigen Geschäftsbedingungen</li><li>Datenschutz-Richtlinie ODER Link zur Datenschutz-Richtlinie</li><li>STOP-Schlüsselwort</li><li>Hinweis: Es können Gebühren für Nachrichten und Daten anfallen.</li></ul>{:/} |
| Allgemeine Geschäftsbedingungen | Die vollständigen Geschäftsbedingungen können unterhalb der Handlungsaufforderung dargestellt werden oder über einen Link in der Nähe der Handlungsaufforderung abgerufen werden. | {::nomarkdown}<ul><li>Name des Programms (Marke)</li><li>Offenlegung der Häufigkeit von Nachrichten</li><li>Produktbeschreibung</li><li>Kontaktdaten des Kundendienstes</li><li>Informationen zum Widerruf</li><li>Hinweis: Es können Gebühren für Nachrichten und Daten anfallen.</li></ul>{:/} |
| Nachrichtenfluss | Programme für wiederkehrende Nachrichten sollten das Opt-in mit einer einzigen SMS bestätigen, in der ausdrücklich angegeben ist, für welches Programm sich die Nutzer:in angemeldet hat, und klare Anweisungen zum Abmelden enthalten.<br><br> Braze verarbeitet Opt-in-, Opt-out- und Hilfsnachrichten und aktualisiert automatisch den Status der Abo-Gruppe für den Nutzer:in und die zugehörige Telefonnummer bei allen eingehenden Anfragen.<br><br> Beachten Sie, dass diese Standardschlüsselwörter und -antworten auch angepasst werden können. | {::nomarkdown}<ul><li>Bestätigung des Opt-in:<ul><li>Programmname (Markenname) ODER Produktbeschreibung</li><li>Informationen zum Widerruf</li><li>Kontaktdaten des Kundendienstes</li><li>Offenlegung der Häufigkeit von Nachrichten</li><li>Hinweis: Es können Gebühren für Nachrichten und Daten anfallen.</li></ul></li><li>HELP-Antwort:<ul><li>Programmname (Markenname) ODER Produktbeschreibung</li><li>Kontaktdaten des Kundendienstes (Support-E-Mail oder Telefonnummer).</li></ul></li><li>Abmeldung (STOP):<ul><li>Programmname (Markenname) ODER Produktbeschreibung</li><li>Bestätigung, dass keine weiteren Nachrichten zugestellt werden.</li></ul></li></ul>{:/} |
| Programmnachrichten | Nachrichten werden im Rahmen des Shortcode-Programms versendet, nachdem die Nutzer:innen eine Opt-in-Bestätigung erhalten haben. | {::nomarkdown}<ul><li>Anweisungen zum Abmelden sollten in regelmäßigen Abständen und mindestens einmal pro Monat bereitgestellt werden.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Sobald alle Ihre Bewerbungsunterlagen vollständig sind, reicht Braze die Bewerbung in Ihrem Namen bei unseren Anbietern ein. Der Antrag wird anschließend von den lokalen Operatoren geprüft und genehmigt, die möglicherweise zusätzliches Feedback geben oder Anfragen an die Verwaltung stellen. Nachdem alle Operator ihre Zustimmung erteilt haben, können Sie den Shortcode umgehend für die Verwendung in Braze konfigurieren.

Der Zeitrahmen für die Überprüfung und Genehmigung von Shortcodes variiert, beträgt jedoch in der Regel 4 bis 12 Wochen, abhängig vom Land und der Art des Programms.

{% alert important %}
Sollten Sie bereits über einen eigenen Shortcode verfügen, wenden Sie sich bitte während des Onboarding-Prozesses an Ihren Customer-Success-Manager, um die Migration oder Übertragung Ihres Shortcodes zu besprechen.
{% endalert %}

{% endtab %}
{% tab SMS long codes and toll-free numbers %}

### SMS-Langcodes (10DLC) und gebührenfreie Nummern

In zahlreichen Ländern hat sich die Einrichtung von Langcodes (auch „10DLCs” oder „10-stellige Langcodes” genannt) und gebührenfreien Nummern für den SMS-Versand von einem „Plug-and-Play”-Verfahren zu einem regulierten Überprüfungssystem gewandelt. Die Transportunternehmen möchten vor dem Versand genau wissen, wer Sie sind und was Sie versenden möchten.

Während des umfangreichen Prozesses zur Einrichtung des Langcodes werden Sie voraussichtlich Details zu Ihrer Markenidentität und Ihrer Kampagnen-Absicht mitteilen.

#### Markenidentität

- **Name der juristischen Person:** Muss genau mit Ihrer Steuerdokumentation übereinstimmen (zum Beispiel „Acme Corp LLC” und nicht „Acme”).
- **Steuer-ID:** In den USA ist dies Ihre Arbeitgeberidentifikationsnummer (EIN). Für internationale Geschäfte benötigen Sie eine Umsatzsteuer-Identifikationsnummer (USt-IdNr.) oder eine lokale Gewerbeanmeldungsnummer (BRN).
- **Digitale Präsenz:** Eine aktive und funktionsfähige Website. Versandunternehmen können dies überprüfen, um sicherzustellen, dass es sich nicht um eine Briefkastenfirma handelt.
- **Befugte Kontaktperson:** Name, E-Mail-Adresse und Telefonnummer der für das Konto verantwortlichen Person.

#### Kampagnenabsicht

- **Anwendungsfälle:** Bitte geben Sie an, ob Sie 2FA-Codes, Terminerinnerungen, Marketingaktionen oder andere Nachrichten versenden.
- **Beispielnachrichten:** Bitte nennen Sie 2–5 Beispiele dafür, was Sie versenden werden.
- **Opt-in-Nachweis:** Bitte beschreiben Sie (und zeigen Sie häufig einen Screenshot davon), wie eine Nutzer:in sich registriert. Beispiele hierfür sind ein Internetformular mit einem Kontrollkästchen oder das Schlüsselwort „Text START“ auf einem Plakat.

Braze wird mit Ihnen zusammenarbeiten, um alle erforderlichen Angaben für die Bereitstellung Ihrer Langcode- oder gebührenfreien Nummer zu erfassen, und diese anschließend zur Prüfung und Genehmigung an unseren Anbieter weiterleiten. Sobald unser Anbieter das Programm genehmigt hat, konfigurieren wir umgehend den Langcode oder die gebührenfreie Nummer in Braze.

Der Zeitplan für die Einrichtung hängt vom Land der Bereitstellung ab. In der Regel dauert die Genehmigung von Langcodes und gebührenfreien Nummern zwischen 1 und 4 Wochen.

{% alert important %}
Alle Kund:innen, die derzeit US-Langcodes besitzen und/oder verwenden, um Nachrichten an US-Kunden zu senden, sind verpflichtet, ihre Langcodes zu registrieren. Um mehr über die Einzelheiten der US-amerikanischen A2P-10DLC-Registrierung und deren Notwendigkeit zu erfahren, besuchen Sie bitte unseren speziellen [10DLC-Artikel]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/).
{% endalert %}

{% endtab %}
{% tab SMS alphanumeric sender ID %}

### SMS alphanumerische ID des Absenders

Alphanumerische Sender-IDs unterliegen strengen Vorschriften, da sie leicht für Phishing-Zwecke missbraucht werden können. Während es in einigen Ländern zulässig ist, einen Namen zu registrieren und zu versenden, muss man in vielen Ländern zunächst nachweisen, dass man Eigentümer der Marke ist.

Möglicherweise werden Sie um die Angabe der folgenden Daten gebeten, um eine alphanumerische ID des Absenders einzurichten.

- **Bevorzugte ID:** Eine String-Zeichenfolge mit bis zu 11 Zeichen. Es muss mindestens einen Buchstaben enthalten und darf kein allgemeiner Begriff wie „BANK” oder „INFO” sein.
- **Nachweis der Markeninhaberschaft:** Bitte legen Sie Ihr Markenzertifikat oder ein Dokument zur Gewerbeanmeldung vor (beispielsweise eine innerhalb der letzten 12 Monate ausgestellte Gründungsurkunde).
- **Vollmacht:** Ein unterschriebenes Schreiben auf Ihrem Firmenbriefpapier, in dem Sie Braze und unseren Anbieter ermächtigen, in Ihrem Namen Nachrichten unter Verwendung dieser spezifischen ID zu versenden.
- **Beispiel-Templates für Nachrichten:** In einigen Regionen müssen Sie die genauen „Templates” der Nachrichten, die Sie versenden möchten, registrieren. Abweichungen in den tatsächlichen Nachrichten können in diesen Ländern zu Fehlern bei der Zustellung führen.

Der Zeitrahmen für die Einrichtung einer alphanumerischen Absender-ID hängt stark davon ab, ob das jeweilige Land eine „dynamische“ Einrichtung (sofort, keine Registrierung erforderlich) zulässt oder eine „Vorabregistrierung“ verlangt. In Ländern, in denen eine Vorabregistrierung erforderlich ist, variiert der Zeitrahmen für die Einrichtung, beträgt jedoch in der Regel zwischen 1 und 4 Wochen.

{% endtab %}
{% endtabs %}

## Häufig gestellte Fragen

Für Antworten auf häufig gestellte Fragen zu SMS- und RCS-Sendern referieren Sie bitte auf unsere Seite [mit häufig gestellten Fragen zu SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/faqs#frequently-asked-questions).