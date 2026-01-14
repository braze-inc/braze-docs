---
nav_title: FAQ
article_title: E-Mail-FAQ
page_order: 14
description: "Auf dieser Seite finden Sie Antworten auf häufig gestellte Fragen zum Thema E-Mail-Nachrichten."
channel: email

---

# Häufig gestellte Fragen

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu E-Mails.

### Was passiert, wenn eine E-Mail verschickt wird und mehrere Profile die gleiche E-Mail-Adresse haben?

Wenn mehrere Benutzer mit übereinstimmenden E-Mail-Adressen in einem Segment sind, das eine Kampagne erhalten soll, wird zum Zeitpunkt des Versands ein zufälliges Benutzerprofil mit dieser E-Mail-Adresse ausgewählt. Auf diese Weise wird die E-Mail nur einmal versendet und dedupliziert, wodurch sichergestellt wird, dass die E-Mail nicht mehrmals an dieselbe E-Mail-Adresse gesendet wird.

Beachten Sie, dass diese Deduplizierung erfolgt, wenn die anvisierten Benutzer in derselben Sendung enthalten sind. Ausgelöste Kampagnen können zu mehreren Versendungen an dieselbe E-Mail-Adresse führen (sogar innerhalb eines Zeitraums, in dem Benutzer aufgrund einer erneuten Teilnahmeberechtigung ausgeschlossen werden könnten), wenn verschiedene Benutzer mit übereinstimmenden E-Mail-Adressen das auslösende Ereignis zu unterschiedlichen Zeiten protokollieren. Benutzer werden bei der Eingabe in ein Canvas nicht per E-Mail deduziert. Es ist also möglich, dass Benutzer nicht über den ersten Schritt eines Canvas hinaus deduziert werden, wenn sie aufgrund der begrenzten Eingabegeschwindigkeit zu leicht unterschiedlichen Zeiten vorankommen. Wenn ein Benutzer, der an eine bestimmte E-Mail-Adresse gebunden ist, eine E-Mail öffnet oder anklickt, werden alle Benutzerprofile, die die gleiche E-Mail-Adresse haben, als Öffner und Klicker der Kampagne markiert.

#### Eine Ausnahme: Per API ausgelöste Kampagnen

API-abhängige Kampagnen werden dedupliziert oder versenden Duplikate – je nachdem, wo die Zielgruppe definiert ist. Mail-Doubletten müssen also direkt als separate `user_ids` im API-Aufruf angegangen werden, um mehrere Details zu erhalten. Hier werden drei mögliche Szenarien für API-gestützte Kampagnen vorgestellt:

- **Szenario 1: Doppelte E-Mails im Zielsegment:** Wenn dieselbe E-Mail in mehreren Benutzerprofilen erscheint, die in den Zielgruppenfiltern des Dashboards für eine API-ausgelöste Kampagne gruppiert sind, erhält nur eines der Profile die E-Mail.
- **Szenario 2: Doppelte E-Mails in verschiedenen `user_ids` des Empfängerobjekts ** Wenn dieselbe E-Mail in mehreren `External_user_IDs` auftaucht, die durch das Objekt `Empfänger` referenziert werden, wird die E-Mail zweimal gesendet.
- **Szenario 3: Doppelte E-Mails aufgrund von doppelten user_ids innerhalb des Empfänger:in-Objekts:** Wenn Sie versuchen, dasselbe Benutzerprofil zweimal hinzuzufügen, wird nur eines der Profile die E-Mail erhalten.

### Werden Aktualisierungen meiner Einstellungen für ausgehende E-Mails rückwirkend angewendet?

Nein. Aktualisierungen der Einstellungen für ausgehende E-Mails wirken sich nicht rückwirkend auf bestehende Sendungen aus. Wenn Sie beispielsweise Ihren Standard-Anzeigenamen in den E-Mail-Einstellungen ändern, wird der bestehende Standard-Anzeigename in Ihren aktiven Kampagnen oder Canvases nicht automatisch ersetzt. 

### Wie hoch sollte eine gute E-Mail-Zustellungsrate sein?

Normalerweise sind etwa 98 % zugestellte Nachrichten mit einer Bounce-Rate von höchstens 3 % ideal. Wenn Ihre Lieferung unter diesen Wert sinkt, besteht in der Regel Grund zur Sorge.

Allerdings kann es auch bei über 98 % Probleme mit der Zustellbarkeit geben. Wenn zum Beispiel alle Ihre Bounces von einer bestimmten Domain kommen, ist das ein klares Signal, dass es ein Reputationsproblem mit diesem Provider gibt.

Außerdem kann es vorkommen, dass Nachrichten zugestellt werden und im Spam landen, was auf potenziell ernsthafte Reputationsprobleme hinweist. Es kommt darauf an, nicht nur die Anzahl zugestellter Nachrichten zu kontrollieren sondern auch die Öffnungs- und Klickraten, um festzustellen, ob Ihre Nachrichten im Posteingang tatsächlich gesehen werden. Da die Anbieter in der Regel nicht jeden Spam melden, kann selbst eine Spam-Quote von 1 % Anlass zur Sorge und zu weiteren Analysen sein.

Schließlich können auch Ihr Unternehmen und die Art der von Ihnen versendeten E-Mails die Zustellung beeinflussen. Wer zum Beispiel hauptsächlich [Transaktions-E-Mails]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) versendet, sollte mit einer besseren Quote rechnen als jemand, der viele Marketing-Nachrichten verschickt.

### Warum betragen die Kennzahlen zur E-Mail-Zustellung zusammengenommen weniger als 100%?

Die Kennzahlen zur E-Mail-Zustellung (Zustellungen, Bounces und Spamquote) können sich auf unter 100 % summieren, da nicht zugestellte E-Mails nach bis zu 72 Stunden Wartezeit erneut zugestellt werden.

Sog. Soft Bounces sind E-Mails, die wegen eines temporären Problems wie eines vollen Postfachs, eines zeitweilig nicht verfügbaren Servers o. Ä. zurückgeschickt werden. Wenn eine Soft-Bounce-E-Mail nach 72 Stunden immer noch nicht zugestellt wurde, wird diese E-Mail in den Zustellungsmetriken der Kampagne nicht berücksichtigt.

### Was versteht man unter Öffnungs-Trackingpixeln?

[Open-Trackingpixel]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) erfassen E-Mail-Öffnungsereignisse mithilfe der E-Mail-Klick-Trackingdomain des Absenders. Ein Pixel ist ein Bild-Tag, das an den HTML-Code der E-Mail angehängt wird. Meistens ist es das letzte HTML-Element innerhalb des body-Tags. Wenn ein Benutzer sein E-Mail-Programm lädt, wird eine Anfrage zum Auffüllen des Bildes mit der jeweiligen Tracking-Domain gestellt, um das Öffnungsereignis zu erfassen.

### Was passiert, wenn eine E-Mail-Kampagne oder ein Canvas gestoppt wird?

Die Benutzer werden daran gehindert, den Canvas zu betreten, und es werden keine weiteren Nachrichten verschickt. Bei E-Mail-Kampagnen und Canvases bewirkt die Stopptaste nicht, dass der Versand sofort beendet wird. Denn wenn die Sendeaufträge übermittelt werden, kann ihre Zustellung nicht verhindert werden.

### Warum erhalte ich mehr E-Mail-Klicks als Öffnungen?

Es kann sein, dass Sie aus einem der folgenden Gründe mehr Klicks als Öffnungen verzeichnen:
- Die Benutzer führen mehrere Klicks auf den Text der E-Mail aus, wenn sie diese nur einmal öffnen.
- Benutzer klicken auf einige E-Mail-Links im Vorschaufenster ihres Telefons. In diesem Fall protokolliert Braze, dass die E-Mail angeklickt, aber nicht geöffnet wurde.
- Benutzer öffnen eine E-Mail erneut, die sie zuvor in der Vorschau angesehen haben.

### Warum werden meine E-Mails weder geöffnet noch angeklickt?

Es kann sein, dass Sie keine Öffnungen und Klicks per E-Mail erhalten, wenn Ihre Tracking Domain falsch konfiguriert ist. Dafür kann es einen der folgenden Gründe geben:
- Es gibt ein SSL-Problem, bei dem Tracking-URLs `http` statt `https` sind.
- Es gibt ein Problem mit Ihrem CDN, bei dem der Nutzer:in String bei den Öffnungs- oder Klick-Ereignissen oder bei beiden nicht ausgefüllt wird.

### Welche potenziellen Risiken birgt das Auslösen von Serverklicks?

Bestimmte Elemente von E-Mails wie überlange Nachrichten oder zu viele Ausrufezeichen können Sicherheitsfunktionen auslösen. Diese können sich auf die Berichterstattung und die IP-Reputation auswirken und zu Abmeldungen führen. 

Bewährte Methoden für den Umgang mit diesen Antworten finden Sie unter [Handhabung von höheren Klickraten]({{site.baseurl}}/help/help_articles/email/open_rates/).

### Kann Braze Abmeldelinks ermitteln, die als Abmeldungen gezählt werden?

Braze erfasst Abmeldelinks, wenn folgende Liquid in E-Mails verwendet wird: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Kann ich einen Link "Diese E-Mail in einem Browser anzeigen" zu meinen E-Mails hinzufügen?

Nein, Braze bietet diese Funktion nicht an. Der Grund dafür ist, dass ein immer größerer Teil der E-Mails auf mobilen Geräten und modernen E-Mail-Clients geöffnet wird, die Bilder und Inhalte ohne Probleme darstellen.

**Workaround:** Um dasselbe Ergebnis zu erzielen, können Sie den Inhalt Ihrer E-Mail auf einer externen Landing Page (z. B. Ihrer Website) hosten, die dann von der E-Mail-Kampagne, die Sie erstellen, mit dem **Link-Tool** beim Bearbeiten des E-Mail-Textes verlinkt werden kann.

