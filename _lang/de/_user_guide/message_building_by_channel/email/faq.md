---
nav_title: FAQ
article_title: E-Mail-FAQ
page_order: 15
description: "Auf dieser Seite finden Sie Antworten auf häufig gestellte Fragen zum Thema E-Mail-Nachrichten."
channel: email

---

# Häufig gestellte Fragen

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu E-Mails.

### Was passiert, wenn eine E-Mail verschickt wird und mehrere Profile die gleiche E-Mail-Adresse haben?

Wenn mehrere Nutzer:innen mit übereinstimmenden E-Mail-Adressen in einem Segment sind, das eine Kampagne erhalten soll, wird zum Zeitpunkt des Versands ein zufälliges Nutzerprofil mit dieser E-Mail-Adresse ausgewählt. Auf diese Weise wird die E-Mail nur einmal versendet und dedupliziert, wodurch sichergestellt wird, dass die E-Mail nicht mehrmals an dieselbe E-Mail-Adresse gesendet wird.

Beachten Sie, dass diese Deduplizierung erfolgt, wenn die anvisierten Nutzer:innen in derselben Sendung enthalten sind. Getriggerte Kampagnen können zu mehreren Versendungen an dieselbe E-Mail-Adresse führen (sogar innerhalb eines Zeitraums, in dem Nutzer:innen aufgrund einer erneuten Teilnahmeberechtigung ausgeschlossen werden könnten), wenn verschiedene Nutzer:innen mit übereinstimmenden E-Mail-Adressen das auslösende Ereignis zu unterschiedlichen Zeiten protokollieren. Nutzer:innen werden beim Eingang in ein Canvas nicht per E-Mail dedupliziert. Es ist also möglich, dass sie nicht über den ersten Schritt eines Canvas hinaus dedupliziert werden, wenn sie aufgrund einer begrenzten Eingangsgeschwindigkeit zu leicht unterschiedlichen Zeiten vorankommen. Wenn eine Nutzer:in, die mit einer bestimmten E-Mail-Adresse verknüpft ist, eine E-Mail öffnet oder anklickt, werden alle Nutzerprofile, die dieselbe E-Mail-Adresse haben, als Öffner:innen bzw. Klicker:innen der Kampagne markiert.

#### Eine Ausnahme: Per API getriggerte Kampagnen

Per API getriggerte Kampagnen werden dedupliziert oder versenden Duplikate – je nachdem, wo die Zielgruppe definiert ist. Doppelte E-Mails müssen im API-Aufruf als separate `user_ids` angegeben werden, um mehrere Zustellungen zu erhalten. Hier sind drei mögliche Szenarien für per API getriggerte Kampagnen:

- **Szenario 1: Doppelte E-Mails im Zielsegment:** Wenn dieselbe E-Mail in mehreren Nutzerprofilen erscheint, die in den Zielgruppen-Filtern des Dashboards für eine per API getriggerte Kampagne gruppiert sind, erhält nur eines der Profile die E-Mail.
- **Szenario 2: Doppelte E-Mails in verschiedenen `user_ids` des Empfängerobjekts:** Sollte dieselbe E-Mail-Adresse in mehreren vom `recipients`-Objekt referenzierten `external_user_id`-Werten enthalten sein, wird die E-Mail zweimal versendet.
- **Szenario 3: Doppelte E-Mails aufgrund von doppelten `user_ids` innerhalb des Empfängerobjekts:** Wenn Sie versuchen, dasselbe Nutzerprofil zweimal hinzuzufügen, erhält nur eines der Profile die E-Mail.

### Werden Aktualisierungen meiner Einstellungen für ausgehende E-Mails rückwirkend angewendet?

Nein. Aktualisierungen der Einstellungen für ausgehende E-Mails wirken sich nicht rückwirkend auf bestehende Sendungen aus. Wenn Sie beispielsweise Ihren Standard-Anzeigenamen in den E-Mail-Einstellungen ändern, wird der bestehende Standard-Anzeigename in Ihren aktiven Kampagnen oder Canvases nicht automatisch ersetzt. 

### Wie hoch sollte eine gute E-Mail-Zustellungsrate sein?

Normalerweise sind etwa 98 % zugestellte Nachrichten mit einer Absprungrate von höchstens 3 % ideal. Wenn Ihre Zustellungsrate unter diesen Wert sinkt, besteht in der Regel Grund zur Sorge.

Allerdings kann es auch bei über 98 % Probleme mit der Zustellbarkeit geben. Wenn zum Beispiel alle Ihre Bounces von einer bestimmten Domain kommen, ist das ein klares Signal für ein Reputationsproblem mit diesem Anbieter.

Außerdem kann es vorkommen, dass Nachrichten zwar zugestellt werden, aber im Spam landen, was auf potenziell ernsthafte Reputationsprobleme hinweist. Es kommt darauf an, nicht nur die Anzahl zugestellter Nachrichten zu kontrollieren, sondern auch die Öffnungs- und Klickraten, um festzustellen, ob Ihre Nachrichten im Posteingang tatsächlich gesehen werden. Da die Anbieter in der Regel nicht jeden Spam-Fall melden, kann selbst eine Spam-Quote von 1 % Anlass zur Sorge und zu weiteren Analysen sein.

Schließlich können auch Ihr Unternehmen und die Art der von Ihnen versendeten E-Mails die Zustellung beeinflussen. Wer zum Beispiel hauptsächlich [Transaktions-E-Mails]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) versendet, sollte mit einer besseren Quote rechnen als jemand, der viele Marketing-Nachrichten verschickt.

### Warum ergeben die Kennzahlen zur E-Mail-Zustellung zusammengenommen nicht 100 %?

Die Kennzahlen zur E-Mail-Zustellung (Zustellungen, Bounces und Spam-Quote) können sich auf weniger als 100 % summieren, da E-Mails, die einen Soft Bounce erhalten, nach einer Wiederholungsfrist von bis zu 72 Stunden möglicherweise nicht zugestellt werden.

Soft Bounces sind E-Mails, die wegen eines temporären Problems wie eines vollen Postfachs, eines zeitweilig nicht verfügbaren Servers o. Ä. zurückgeschickt werden. Wenn eine Soft-Bounce-E-Mail nach 72 Stunden immer noch nicht zugestellt wurde, wird diese E-Mail in den Zustellungsmetriken der Kampagne nicht berücksichtigt.

### Was versteht man unter Öffnungs-Trackingpixeln?

[Öffnungs-Trackingpixel]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) erfassen E-Mail-Öffnungsereignisse mithilfe der E-Mail-Klick-Tracking-Domain des Absenders. Ein Pixel ist ein Bild-Tag, das an den HTML-Code der E-Mail angehängt wird. Meistens ist es das letzte HTML-Element innerhalb des body-Tags. Wenn eine Nutzer:in ihre E-Mail lädt, wird eine Anfrage zum Laden des Bildes von der gebrandeten Tracking-Domain gestellt, wodurch ein Öffnungsereignis protokolliert wird.

### Was passiert, wenn eine E-Mail-Kampagne oder ein Canvas gestoppt wird?

Die Nutzer:innen werden daran gehindert, den Canvas zu betreten, und es werden keine weiteren Nachrichten verschickt. Bei E-Mail-Kampagnen und Canvases bewirkt die Stopptaste nicht, dass der Versand sofort beendet wird. Denn wenn die Sendeaufträge einmal übermittelt wurden, kann ihre Zustellung nicht mehr verhindert werden.

### Warum erhalte ich mehr E-Mail-Klicks als Öffnungen?

Es kann sein, dass Sie aus einem der folgenden Gründe mehr Klicks als Öffnungen verzeichnen:
- Die Nutzer:innen klicken bei einer einzigen Öffnung mehrfach auf den Text der E-Mail.
- Nutzer:innen klicken auf E-Mail-Links im Vorschaufenster ihres Telefons. In diesem Fall protokolliert Braze, dass die E-Mail angeklickt, aber nicht geöffnet wurde.
- Nutzer:innen öffnen eine E-Mail erneut, die sie zuvor in der Vorschau angesehen haben.

### Warum werden bei meinen E-Mails weder Öffnungen noch Klicks angezeigt?

Es kann sein, dass keine E-Mail-Öffnungen oder -Klicks angezeigt werden, wenn Ihre Tracking-Domain falsch konfiguriert ist. Dafür kann es einen der folgenden Gründe geben:
- Es gibt ein SSL-Problem, bei dem Tracking-URLs `http` statt `https` verwenden.
- Es gibt ein Problem mit Ihrem CDN, bei dem der User-Agent-String bei den Öffnungs- oder Klick-Ereignissen oder bei beiden nicht ausgefüllt wird.

### Welche potenziellen Risiken birgt das Auslösen von Serverklicks?

Bestimmte Elemente von E-Mails wie überlange Nachrichten oder zu viele Ausrufezeichen können E-Mail-Sicherheitsmechanismen auslösen. Diese können sich auf die Berichterstattung und die IP-Reputation auswirken und dazu führen, dass sich Nutzer:innen abmelden.

Bewährte Methoden für den Umgang mit diesen Reaktionen finden Sie unter [Handhabung von höheren Klickraten]({{site.baseurl}}/help/help_articles/email/open_rates/).

### Kann Braze Abmeldelinks erfassen, die zur Metrik „Abmeldungen" gezählt werden?

Braze erfasst Abmeldelinks, wenn folgendes Liquid in E-Mails verwendet wird: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Kann ich einen Link „Diese E-Mail im Browser anzeigen" zu meinen E-Mails hinzufügen?

Nein, Braze bietet diese Funktion nicht an. Der Grund dafür ist, dass ein immer größerer Teil der E-Mails auf mobilen Geräten und in modernen E-Mail-Clients geöffnet wird, die Bilder und Inhalte ohne Probleme darstellen.

**Workaround:** Um dasselbe Ergebnis zu erzielen, können Sie den Inhalt Ihrer E-Mail auf einer externen Landing-Page (z. B. Ihrer Website) hosten, die dann über die E-Mail-Kampagne verlinkt werden kann, die Sie gerade erstellen. Verwenden Sie dazu das **Link-Tool** beim Bearbeiten des E-Mail-Textes.

### Warum werden meine Nutzer:innen von E-Mail-Sicherheitssoftware automatisch abgemeldet?

Einige E-Mail-Sicherheitstools für Unternehmen (wie Barracuda, Proofpoint und ähnliche Dienste) laden alle URLs in eingehenden E-Mails vorab herunter oder scannen sie – einschließlich Links zum Abmelden. Dies kann zu unbeabsichtigten Abmeldungen führen, wenn das Sicherheitstool dem Ein-Klick-Link zum Abmelden von der Liste folgt.

Um dies zu vermeiden:

- **Empfehlen Sie den Empfänger:innen, Ihre Absender-Domain auf die Allowlist zu setzen:** Arbeiten Sie mit den IT-Teams der betroffenen Empfänger:innen zusammen, um Ihre Absender-Domain und die Tracking-Domains von Braze zur Allowlist ihrer E-Mail-Sicherheit hinzuzufügen.
- **Nutzen Sie ein Einstellungscenter:** Verwenden Sie anstelle eines direkten Abmeldelinks ein [Einstellungscenter]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/), das eine Interaktion der Nutzer:innen erfordert, um die Abmeldung zu bestätigen. Sicherheitsscanner füllen in der Regel keine mehrstufigen Formulare aus.
- **Überprüfen Sie die Abmeldeprotokolle:** Prüfen Sie den `User-Agent`-Header und die IP-Adresse in Ihren Currents-Abmeldeereignisdaten, um Muster zu identifizieren, die auf automatisiertes Scannen hindeuten (z. B. übereinstimmende `User-Agent`-Header bei mehreren Abmeldungen).

Weitere Informationen darüber, wie sich serverseitiges Scannen auf E-Mail-Metriken auswirken kann, finden Sie unter [Umgang mit steigenden Klickraten]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#handling-increases-in-click-rates).

### Warum hat sich meine maschinelle Öffnungsrate unerwartet verändert?

[Maschinelle Öffnungen]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics/#machine-opens) werden durch E-Mail-Sicherheitsfunktionen wie Apple Mail Privacy Protection (MPP) getriggert, die E-Mail-Inhalte (einschließlich des Tracking-Pixels) vorladen, ohne dass die Nutzer:innen die E-Mail tatsächlich öffnen. Die maschinellen Öffnungsraten können aufgrund folgender Faktoren schwanken:

- Veränderungen im Anteil Ihrer Zielgruppe, der Apple Mail oder andere E-Mail-Clients mit Datenschutzfunktionen verwendet.
- Updates der Datenschutz-Features von E-Mail-Anbietern oder der Bot-Erkennungsmechanismen.
- Änderungen in Ihrer Segmentierung der Zielgruppe oder im Targeting.

Die Prozentsätze der maschinellen Öffnungen stellen keinen verlässlichen Maßstab für das tatsächliche Engagement dar. Für eine genauere Darstellung der E-Mail-Performance sollten Sie sich auf *Andere Öffnungen* (nicht maschinelle Öffnungen) und *Eindeutige Klicks* konzentrieren. Sie können diese Metriken auch im Zeitverlauf mithilfe des [E-Mail-Performance-Dashboards]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard/) vergleichen.

### Beinhaltet die Metrik *Eindeutige Öffnungen* auch *Maschinelle Öffnungen*?

Ja. *Eindeutige Öffnungen* beinhalten *Maschinelle Öffnungen*. In der Ansicht **Kampagnen-Analytics** und im **Berichts-Builder** können Sie beide Metriken einsehen.