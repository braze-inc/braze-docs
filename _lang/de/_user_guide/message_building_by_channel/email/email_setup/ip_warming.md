---
nav_title: IP-Warming
article_title: IP Erwärmung
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt das Thema IP-Warming und Best Practices."
channel: email

---

# IP-Warming

> IP-Warming bedeutet, dass die Anbieter von E-Mail-Postfächern daran gewöhnt werden, Nachrichten von Ihren speziellen IP-Adressen zu empfangen. Es ist ein äußerst wichtiger Bestandteil des E-Mail-Versands bei jedem E-Mail-Dienstanbieter (ESP) und bei Braze Standard, zu bestätigen, dass Ihre Nachrichten den Posteingang des Empfängers oder der Empfängerin mit einer gleichbleibend hohen Rate erreichen.

IP-Warming soll Ihnen helfen, einen positiven Ruf bei Internet-Dienstanbieter (ISPs) aufzubauen. Jedes Mal, wenn eine neue IP-Adresse zum Versenden einer E-Mail verwendet wird, überwachen ISPs diese E-Mails programmatisch, um sicherzustellen, dass sie nicht zum Versenden von Spam an Benutzer verwendet wird.

## Was ist, wenn ich keine Zeit zum Aufwärmen von IPs habe?

**IP-Warming ist erforderlich.** Wenn Sie die IPs nicht angemessen erwärmen und das Muster Ihrer E-Mails Verdacht erregt, könnte Ihre E-Mail-Zustellgeschwindigkeit erheblich gedrosselt oder verlangsamt werden. Ihre Domain oder IP könnte auch von den ISPs blockiert werden, was dazu führen kann, dass Ihre E-Mails stattdessen direkt im Spam-Ordner des Posteingangs Ihres Benutzers landen. Daher ist es wichtig, dass Sie Ihre IPs richtig „aufwärmen“.

ISPs drosseln die E-Mail-Zustellung, wenn der Verdacht auf Spam aufkommt, damit sie ihre Benutzer schützen können. Wenn Sie z. B. an 100.000 Nutzer:innen senden, kann es sein, dass der ISP die E-Mail in der ersten Stunde nur an 5.000 dieser Nutzer:innen zustellt. Dann überwacht der ISP Maßnahmen wie Öffnungsraten, Klickraten, Abmeldungen und Spam-Berichte. Wenn also eine beträchtliche Anzahl von Spam-Meldungen auftritt, kann es sein, dass sie den Rest der Sendung in den Spam-Ordner verschieben, anstatt sie an den Posteingang des Benutzers zu senden. 

Wenn das Engagement mäßig ist, kann es sein, dass sie Ihre E-Mail weiter drosseln, um mehr Daten über das Engagement zu sammeln und mit größerer Sicherheit feststellen zu können, ob es sich bei der E-Mail um Spam handelt oder nicht. Wenn die E-Mail sehr hohe Engagement-Metriken aufweist, werden sie diese E-Mail möglicherweise nicht mehr drosseln. Sie verwenden diese Daten, um eine E-Mail-Reputation zu erstellen, die letztendlich bestimmt, ob Ihre E-Mails automatisch als Spam gefiltert werden oder nicht.

Wenn Ihre Domain oder IP von einem ISP blockiert wird, finden Sie in den [Nachrichtenprotokollen]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) Informationen darüber, welche Websites Sie besuchen sollten, um diese ISPs anzusprechen und von diesen Listen zu entfernen.

## Zeitplan für das IP-Warming

Wir empfehlen dringend, diesen Zeitplan für das IP-Warming strikt einzuhalten, um die Zustellbarkeit zu unterstützen. Es ist auch wichtig, dass Sie keine Tage auslassen, denn eine konsequente Skalierung verbessert die Zustellungsmetriken.

Tag | Anzahl der zu sendenden Emails
----|--------------------------|
(1 %) | (50 %)
(2 %) | (100 %)
3 | (500 %)
(4 %) | (1,000 %)
(5 %) | (5,000 %)
6 | 10,000
(7 %) | (20,000 %)
(8 %) | (40,000 %)
(9 %) | (70,000 %)
(10 %) | (100,000 %)
(11 %) | (150,000 %)
(12 %) | (250,000 %)
(13 %) | (400,000 %)
(14 %) | (600,000 %)
(15 %) | (1,000,000 %)
(16 %) | (2,000,000 %)
17 | (4,000,000 %)
18+ | Täglich verdoppeln, bis das gewünschte Volumen erreicht ist

Zum Erreichen Ihrer Höchstleistung empfehlen wir Ihnen, ein Warming durchzuführen. Das heißt, wenn Sie normalerweise 2 Millionen E-Mails pro Tag senden, aber planen, in einer bestimmten Saison 7 Millionen zu senden, sollten Sie sich auf diesen „Spitzenwert“ vorbereiten.

Sobald das Warming abgeschlossen ist und Sie Ihr gewünschtes tägliches Volumen erreicht haben, sollten Sie versuchen, dieses Volumen täglich beizubehalten. Eine gewisse Fluktuation ist zu erwarten, aber wenn Sie das gewünschte Volumen erreichen und dann nur einmal pro Woche einen Massenversand durchführen, kann sich das negativ auf Ihre Zustellungskennzahlen und Ihren Ruf als Absender auswirken. 

{% alert important %}
Die meisten ISPs speichern Reputationsdaten nur für 30 Tage. Wenn Sie einen Monat lang keine Nachrichten senden, müssen Sie das IP-Warming wiederholen.
{% endalert %}

## Sendungen beim Warming begrenzen

Unsere integrierte Funktion zur Nutzereinschränkung ist ein nützliches Hilfsmittel, um Ihnen beim Warming Ihrer IP-Adresse zu helfen. Nachdem Sie bei der Kampagnenerstellung die gewünschten Nachrichtensegmente ausgewählt haben, wählen Sie im Schritt [Zielbenutzer]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas) das Dropdown-Menü **Erweiterte Optionen**, um Ihre Benutzer einzuschränken. Mit fortschreitendem Warming können Sie dieses Limit schrittweise erhöhen, um das Volumen der von Ihnen gesendeten E-Mails zu steigern.

![]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentierung von Subdomains

Viele ISPs und E-Mail-Zugangsanbieter filtern nicht mehr nur nach der Reputation der IP-Adresse. Diese Filtertechnologien berücksichtigen jetzt auch die Domain-basierte Reputation. Das bedeutet, dass die Filter alle mit der Domain des Absenders oder der Absenderin verbundenen Daten prüfen und nicht nur die IP-Adresse herausfiltern. Aus diesem Grund empfehlen wir Ihnen, nicht nur Ihre E-Mail-IP aufzuwärmen, sondern auch separate Domänen oder Subdomänen für Marketing-, Transaktions- und Unternehmensmails zu verwenden. 

{% alert important %}
Die Segmentierung von Subdomains ist besonders wichtig für Absender:innen mit großem Volumen. Diese Absender:innen sollten bei der Einrichtung ihres Kontos mit einem Vertreter von Braze zusammenarbeiten, um zu bestätigen, dass sie sich an diese Vorgaben halten.
{% endalert %}

Wir empfehlen Ihnen, Ihre Domains so zu segmentieren, dass Unternehmensmails über Ihre Top-Level-Domain und Marketing- und Transaktionsmails über verschiedene Domains oder Subdomains gesendet werden.

## Bewährte Praktiken

Alle Folgen eines fehlenden IP-Warmings können vermieden werden, wenn Sie die folgenden Best Practices zum IP-Warming befolgen.

### Beginnen Sie mit einem kleinen E-Mail-Aufkommen

Erhöhen Sie die Menge, die Sie täglich senden, so allmählich wie möglich. Abrupte, umfangreiche E-Mail-Kampagnen werden von ISPs mit größter Skepsis betrachtet. Beginnen Sie daher mit dem Versenden kleinerer Mengen von E-Mails und steigern Sie diese allmählich auf das Volumen, das Sie letztendlich versenden möchten. Unabhängig von der Lautstärke empfehlen wir, sicherheitshalber ein IP-Warming durchzuführen. Siehe [Zeitplan für das IP-Warming](#ip-warming-schedule).

### Präsentieren Sie ansprechende Einführungsinhalte

Vergewissern Sie sich, dass Ihr erster Inhalt sehr ansprechend ist und die Wahrscheinlichkeit maximiert, dass Nutzer auf Ihre E-Mail klicken, sie öffnen und sich mit ihr beschäftigen. Bevorzugen Sie beim IP-Warming immer gezielte E-Mails gegenüber wahllosen Massen-E-Mails.

### Legen Sie eine konsistente Sendekadenz fest

Sobald das IP-Warming abgeschlossen ist, erstellen Sie eine Sendekadenz, wobei Sie darauf achten, dass Sie Ihre E-Mails über einen Tag oder mehrere Tage verteilen. Indem Sie einen möglichst konsistenten Zeitplan erstellen, können Sie einen IP-Cooldown verhindern, der auftreten kann, wenn das Sendevolumen für mehr als ein paar Tage aufhört oder deutlich abnimmt. 

Nutzen Sie unseren [Zeitplan für das IP-Warming](#ip-warming-schedules), um Ihren Versand über einen längeren Zeitraum zu verteilen, anstatt einen Massenversand zu einem bestimmten Zeitpunkt durchzuführen.

### Bereinigen Sie Ihre E-Mail-Listen

Vergewissern Sie sich, dass Ihre E-Mail-Liste bereinigt ist und keine alten oder ungeprüften E-Mail-Adressen enthält. Es ist ideal, wenn Sie sicherstellen, dass Sie sowohl [CASL- als auch CAN-SPAM-konform]({{site.baseurl}}/user_guide/administrative/privacy/spam_regulations/) sind.

### Überwachen Sie Ihre Absender-Reputation

Achten Sie bei der Durchführung des IP-Warming-Prozesses darauf, dass Sie Ihre Absender-Reputation sorgfältig überwachen. Diese spezifischen Metriken sind wichtig zu beobachten:
- **Absprungraten:** Wenn eine Kampagne zu mehr als 3-5% abprallt, sollten Sie die Sauberkeit Ihrer Liste überprüfen, indem Sie die Richtlinien in unserem [Keep It Clean befolgen: The Importance of Email List Hygiene](https://www.braze.com/blog/email-list-hygiene/). Außerdem sollten Sie eine [Sunsetting-Richtlinie]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/) in Betracht ziehen, um das Mailen von nicht aktivierten oder inaktiven E-Mail-Adressen einzustellen.
- **Spam-Berichte:** Wenn eine Kampagne zu mehr als 0,08% als Spam gemeldet wird, sollten Sie den Inhalt, den Sie versenden, neu bewerten, überprüfen, ob er auf eine interessierte Zielgruppe ausgerichtet ist, und sicherstellen, dass Ihre E-Mails so formuliert sind, dass sie deren Interesse wecken.
- **Öffnungsraten:** Öffnungsraten sind ein nützlicher Indikator für die Platzierung im Posteingang. Wenn Ihre einmaligen Öffnungsraten über 25% liegen, haben Sie wahrscheinlich eine hohe Platzierung im Posteingang, was auf einen guten Ruf des Absenders hinweist.

{% alert tip %}
Braze empfiehlt, [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) nicht zum Aufwärmen Ihrer IPs zu verwenden. Da IP-Warming-Kampagnen zu den ersten Kampagnen gehören, die Sie versenden, verfügt Braze nicht über genügend Informationen über Ihre Nutzer:innen, um einen optimalen Sendezeitpunkt zu berechnen. In diesem Fall würden alle Nachrichten mit Intelligent Timing standardmäßig auf die Ausweichzeit eingestellt und trotzdem zur gleichen Zeit gesendet.
{% endalert %}

{% alert tip %}
Es ist normal, dass E-Mails während der IP-Warming-Phase an den Spam-Ordner gesendet werden, da Ihre Domain und IP noch keinen positiven Ruf aufgebaut haben. Wenn eine E-Mail in Ihrem Spam-Ordner landet, muss Ihr E-Mail-Administrator Ihre Braze-Sendedomäne und IP-Adresse zur Liste der erlaubten Mails in Ihrem Unternehmen hinzufügen.
{% endalert %}

