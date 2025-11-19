---
nav_title: FAQ
article_title: SMS-FAQ
page_order: 12
description: "Dieser Artikel behandelt einige der am häufigsten gestellten Fragen, die bei der Einrichtung von SMS-Kampagnen auftreten."
page_type: FAQ
alias: /sms_faq/
channel:
  - SMS
  
---

# Häufig gestellte Fragen

> Auf dieser Seite versuchen wir, Ihre wichtigsten Fragen zu SMS zu beantworten!

### Können Sie Links in eine SMS einfügen?

Sie können jeden Link in jede beliebige SMS-Kampagne einfügen. Es gibt jedoch ein paar Bedenken zu berücksichtigen:

- Links können einen Großteil des 160-Zeichen-Limits für SMS in Anspruch nehmen. Wenn Sie einen Link und einen Text einfügen, kann es sein, dass Sie zwei SMS-Nachrichten erhalten, anstatt nur einer.
- Unternehmen verwenden oft Linkverkürzer, um die Auswirkungen der Zeichenanzahl eines Links zu begrenzen. Wenn Sie jedoch einen verkürzten Link über einen langen Code versenden, kann es sein, dass die Betreiber die Nachricht blockieren oder ablehnen, da sie die Umleitung des Links für verdächtig halten.
- Die Verwendung einer [Kurznummer]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) wäre die zuverlässigste Art, Links einzubinden.

Braze verfügt auch über eine eigene Funktion zum Verkürzen von Links, die Links automatisch verkürzt und eine Analyse der Klickraten liefert. Weitere Informationen finden Sie unter [Link-Verkürzung]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/).

### Werden Test-SMS auf die Grenzwerte angerechnet?

Ja, das tun sie. Denken Sie daran, wenn Sie Nachrichten testen.

### Muss ein Benutzer Teil einer SMS-Abonnementgruppe sein, um SMS-Testnachrichten zu erhalten?

Ja, das tun sie. Nutzer:innen müssen über eine gültige Telefonnummer verfügen und zu der SMS-Abo-Gruppe gehören, die für den Testversand verwendet wird.

### Müssen Sie die Geschwindigkeit, mit der Sie SMS-Nachrichten versenden, begrenzen?

Die Standard-Gleichzeitigkeitsrate und der Durchsatz ermöglichen etwa 360.000 Nachrichten pro Stunde und Shortcode. Zusätzlicher Durchsatz erfordert zusätzliche Kurzcodes.

### Wie kann ich Mehrkosten vermeiden?

Wir können Ihnen zwar nicht versprechen, dass Sie nicht gelegentlich Mehrkosten haben werden, aber Sie können die folgenden Vorsichtsmaßnahmen ergreifen, um die Wahrscheinlichkeit zu verringern, dass Sie die Ihnen zugeteilten Limits überschreiten:

- Achten Sie auf die Anzahl der Zeichen in Ihrer SMS. Das unbeabsichtigte Senden von mehr als einem Segment kann zu Mehrkosten führen. Weitere Einzelheiten finden Sie in unserer [Segmentaufteilung]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown).
- Berechnen Sie Ihre SMS-Zeichen sorgfältig, um Liquid oder Connected-Content zu berücksichtigen. Der Braze SMS Composer in Ihrem Dashboard schätzt die Nutzung dieser beiden Funktionen nicht und berücksichtigt sie auch nicht.
- Bedenken Sie die Art der Kodierung, die Ihre Nachricht verwendet - wenn Ihre Nachricht die GSM-7-Kodierung verwendet, können Sie in der Regel davon ausgehen, dass Sie eine Nachricht mit 128 Zeichen pro Nachrichtensegment versenden können. Wenn Ihre Nachricht die [UCS-2-Kodierung](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) verwendet, können Sie in der Regel davon ausgehen, dass Sie eine Nachricht mit 67 Zeichen pro Nachrichtensegment versenden können.
- Testen, testen und testen! Testen Sie Ihre SMS Nachrichten immer vor dem Start, besonders wenn Sie Liquid und Connected-Content verwenden.

### Was sind die besten Versandmethoden, um die Erkennung von Spam bei SMS zu vermeiden?

1. Vergewissern Sie sich, dass die Anweisungen zum Ein- und Ausstieg klar sind.
2. Stellen Sie sicher, dass Sie (die Marke) eine Beziehung zu den Kund:innen haben.
3. Achten Sie darauf, dass die Inhalte für die Beziehung relevant sind und dass der Nutzer sich für den Erhalt der Inhalte entschieden hat.

Weitere Richtlinien zur Vermeidung von Spam-Erkennung finden Sie unter [SMS-Gesetze und -Vorschriften Richtlinien]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

### Wie erstellen Sie eine Logik für selektive Opt-ins für SMS, damit Nutzer:innen in der richtigen Abo-Gruppe sind?

Benutzerdefinierte Schlüsselwörter werden als benutzerdefinierte Ereignisse geschrieben, so dass Sie Segmente basierend auf den Schlüsselwörtern erstellen sollten, die Kunden eingeben können. Wenn sich ein Benutzer beispielsweise für SMS für VIP-Nachrichten, aber nicht für Warnungen entscheidet, können Sie ein VIP-Segment und ein Warnungssegment erstellen und den Benutzer dann dem entsprechenden Segment zuweisen.

### Wie viele Zeichen umfasst ein Emoji?

Emojis können knifflig sein, da es keine einheitliche Zeichenanzahl für alle Emojis gibt. Es besteht die Gefahr, dass das Emoji das Zeichenlimit überschreitet und die SMS in mehrere Nachrichten zerfällt, obwohl sie im Braze Composer als eine Nachricht angezeigt wird. Wenn Sie Ihre Nachrichten testen, können Sie mit Hilfe unseres [Segmentrechners]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator) besser überprüfen, ob eine Nachricht geteilt werden wird.

### Wenn ein Benutzer "Stopp" an unsere Kurzwahlnummer sendet, wird er dann aus der Abonnementgruppe abgemeldet?

Wie sieht das im Benutzerprofil aus? Die Abonnementgruppe wird auf 2 Bindestriche (- -) zurückgesetzt, und es werden benutzerdefinierte Ereignisse für die Anmeldung und Abmeldung angezeigt.

### Gibt es eine Möglichkeit zu sehen, ob ein Alias in einem Benutzerprofil existiert?

Aliase sind im Benutzerprofil nicht sichtbar. Sie müssen die Endpunkte für den [Export von Benutzerdaten]({{site.baseurl}}/api/endpoints/export/) verwenden, um zu bestätigen, dass Aliase festgelegt wurden.

### Was sind gemeinsame Shortcodes?

Mit einer gemeinsamen Kurzwahlnummer kommen alle Textnachrichten, unabhängig davon, von welchem Unternehmen oder welcher Organisation sie gesendet werden, auf dem mobilen Gerät eines Verbrauchers von derselben 5-6-stelligen Telefonnummer an. Gemeinsame Kurzwahlen sind zwar relativ kostengünstig und sofort verfügbar, aber das bedeutet, dass Ihr Unternehmen keine eigene Kurzwahlnummer hat.

Dieser Ansatz hat auch einige Nachteile:

- Wenn sich Ihre Kunden von den Nachrichten eines anderen Unternehmens abmelden, das einen gemeinsamen Shortcode mit Ihnen hat, haben sie sich auch von Ihren Nachrichten abgemeldet.
- Wenn ein Unternehmen gegen die Regeln verstößt, werden die Nachrichten aller Unternehmen ausgesetzt.
- Sicherheitsfragen

### Wie kann man URLs für SMS zulassen?

Bevor Sie SMS-Nachrichten mit URLs an Benutzer in bestimmten Ländern (z. B. Schweden oder Skandinavien) senden, müssen Sie diese URLs bei Ihrem Netzbetreiber registrieren lassen. Wenden Sie sich an Ihren Braze-Kundendienstleiter. Dieser Vorgang wird etwa fünf Tage dauern.  

### Was passiert, wenn mehrere Benutzer die gleiche Telefonnummer haben?

Wenn mehrere Nutzerprofile, die sich eine Telefonnummer teilen (die für SMS aktiviert ist), gleichzeitig für eine aktionsbasierte Kampagne oder eine Canvas-Komponente in Frage kommen, ausgelöst durch das Ereignis einer eingehenden SMS, wird Braze die Nutzer:innen auf der Ebene der Canvas-Komponente abziehen. Dadurch wird verhindert, dass Nutzer:innen mehr als eine SMS für eine Canvas-Komponente erhalten, selbst wenn mehrere Nutzer:innen dieselbe Telefonnummer haben. 

{% alert note %}
Braze zieht für geplante Canvase keine Telefonnummern ab.
{% endalert %}

Braze verwendet den folgenden Ablauf, um das Profil der Empfängerin oder des Empfängers zu bestimmen:
- Prüfen Sie, welches Profil zuletzt eine SMS erhalten hat (bis zu 7 Tage zurückliegend); wenn es eine gibt, senden Sie sie an diesen Benutzer.
- Wenn Sie bis vor 7 Tagen keine SMS erhalten haben, senden Sie sie an den Benutzer, dessen Benutzeralias "phone" mit der Telefonnummer übereinstimmt.
- Wenn keines von beiden vorhanden ist, wird ein zufälliges Profil aus den verfügbaren Profilen verwendet. 

Wenn Sie ein "START"- oder "STOP"-Schlüsselwort von der gemeinsamen Telefonnummer erhalten, werden alle Benutzerprofile abonniert und für SMS aktiviert oder abgemeldet. Dies gilt auch für Änderungen des API-Status. Wenn z.B. mehrere Profile mit unterschiedlichen externen IDs die gleichen Telefonnummern haben, wird eine Statusänderung der Abo-Gruppe über die API alle Profile mit dieser Telefonnummer aktualisieren, auch wenn nur eine externe ID angegeben ist.

{% alert important %}
Wenn Sie Ihre Benutzer in einem Canvas gestaffelt haben und für jede Canvas-Komponente unterschiedliche Zeitpläne haben, können Sie einem Benutzer mit derselben E-Mail oder demselben Telefon doppelte Nachrichten schicken.
{% endalert %}

### Werden SMS-Ereigniseigenschaften Schlüsselwörter in einem Satz erfassen?

Damit ein Schlüsselwort innerhalb eines Satzes erkannt wird (z. B. "Bitte hören Sie auf, mir eine SMS zu schreiben"), müssen Sie eine Liquid-Anweisung in der Nachricht verwenden, um das spezifische Wort zu erkennen. Event-Eigenschaften haben eine Zeichenbegrenzung von 256, ansonsten gibt es keine Zeichenbegrenzung.

### Warum warnt mich das Braze Dashboard, dass mir zusätzliche Nachrichtensegmente in Rechnung gestellt werden können, wenn meine Nachricht weniger als 160 (GCM-7) oder 70 (UCS-2) Zeichen umfasst?

Es kann sein, dass Ihnen zusätzliche Nachrichtensegmente berechnet werden, wenn Sie in Ihrer Nachricht eine Personalisierung mit Liquid vornehmen. Das Template für den Content-Block wird erst erstellt, wenn die Nachricht zum Versand vorbereitet wird. Wenn Sie eine SMS mit einem Inhaltsblock bearbeiten, weiß Braze nicht, was der Inhaltsblock enthalten wird, sondern liefert eine grobe Schätzung. Wir empfehlen, dass Nutzer:innen die Vorschau der Nachricht verwenden, um besser zu verstehen, was sie erwartet.

### Was ist ein `app_id` im SMS-API-Objekt?

Der API-Schlüssel für die App-Kennung oder `app_id` ist ein Parameter, der eine Aktivität mit einer bestimmten App in Ihrem Arbeitsbereich verknüpft. Es zeigt an, mit welcher App innerhalb des Arbeitsbereichs Sie interagieren. Sie werden zum Beispiel feststellen, dass Sie eine `app_id` für Ihre iOS App, eine `app_id` für Ihre Android App und eine `app_id` für Ihre Internet Integration haben werden. 

Sie können Ihre `app_id` finden, indem Sie zu **Einstellungen** > **App-Einstellungen** navigieren und den Abschnitt **Identifizierung** suchen.

### Wie werden mir die SMS in Rechnung gestellt?

Neben den Gebühren für Kurz- und Langcodes bietet Braze ein Kontingent an SMS-Nachrichten für verschiedene Länder. Das heißt, wir arbeiten mit Ihnen zusammen, um eine bestimmte Anzahl von Nachrichtensegmenten für verschiedene Länder festzulegen, die Sie für den Versand von SMS-Kampagnen verwenden. Die Abrechnung erfolgt nach der Anzahl der gesendeten Nachrichtensegmente pro Land. Weitere Informationen über die Berechnung von Nachrichtensegmenten finden Sie in unserem Leitfaden [Nachrichtensegmente und Kopierlimits]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown). Ihr Kundenbetreuer wird Sie informieren, wenn Sie Ihr Maximum fast erreicht haben, und Ihnen entsprechende Berichte zur Verfügung stellen, damit Sie auf dem Laufenden bleiben. Bei weiteren Fragen zu Überschreitungen wenden Sie sich bitte an Ihren Braze-Vertreter.

### Wird eine Nachricht, die an ein Festnetztelefon gesendet wird, trotzdem auf die Anzahl der gesendeten SMS angerechnet?

In den USA, Kanada und Großbritannien:
- Wenn eine SMS an einen Festnetzanschluss gesendet wird, wird sie als **nicht zugestellt** markiert. Beachten Sie, dass Twilio weiterhin für Zustellungsversuche Gebühren erhebt. Nachrichten, die in Ihren Nachrichtenprotokollen als **gesendet**, **zugestellt** oder **nicht zugestellt** markiert sind, werden also in Rechnung gestellt.
- In Großbritannien wandeln einige Anbieter die SMS in eine Voicemail um und übermitteln die Nachricht.

In anderen Ländern:
- Twilio (Twilio) gibt einen Fehler aus, und die versuchte SMS wird Ihnen nicht in Rechnung gestellt. 

### Wenn ein Benutzer abgemeldet ist und ein Schlüsselwort an unseren kurzen und langen Code sendet, erhält er dann die Antwort, die wir für dieses Schlüsselwort in Braze konfiguriert haben?

Wenn ein Benutzer sich abgemeldet hat und ein Schlüsselwort aus einer der [Standard-Schlüsselwortkategorien]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/) sendet, erhält er die Antwort für dieses Schlüsselwort. Wenn ein Benutzer abgemeldet ist und ein [benutzerdefiniertes Schlüsselwort]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/keyword_handling/) sendet, erhält er keine Antwort für dieses Schlüsselwort. 
