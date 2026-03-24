---
nav_title: IP-Warming
article_title: IP-Warming
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt das Thema IP-Warming und Best Practices."
channel: email
local_redirect:
  automated-ip-warming: '/docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/automated_ip_warming/'
---

# IP-Warming

> IP-Warming bedeutet, dass die Anbieter von E-Mail-Postfächern daran gewöhnt werden, Nachrichten von Ihren dedizierten IP-Adressen zu empfangen. Es ist ein äußerst wichtiger Bestandteil des E-Mail-Versands bei jedem E-Mail-Anbieter (ESP) und bei Braze Standardpraxis, um sicherzustellen, dass Ihre Nachrichten den Posteingang mit einer gleichbleibend hohen Rate erreichen.

IP-Warming soll Ihnen helfen, einen positiven Ruf bei Internet-Providern (ISPs) aufzubauen. Jedes Mal, wenn eine neue IP-Adresse zum Versenden einer E-Mail verwendet wird, überwachen ISPs diese E-Mails programmatisch, um sicherzustellen, dass sie nicht zum Versenden von Spam an Nutzer:innen verwendet wird. Stellen Sie sich Ihre IP- und Domain-Reputation wie einen Kredit-Score vor – ISPs nutzen diese Reputation, um zu entscheiden, ob Ihre E-Mail im Posteingang oder im Spam-Ordner landet. Ähnlich wie bei einem Kredit-Score braucht es Zeit, eine positive Reputation aufzubauen, und noch länger, eine schlechte wiederherzustellen.

## Was ist, wenn ich keine Zeit zum Aufwärmen von IPs habe?

**IP-Warming ist erforderlich.** Wenn Sie die IPs nicht angemessen aufwärmen und das Muster Ihrer E-Mails Verdacht erregt, könnte Ihre E-Mail-Zustellgeschwindigkeit erheblich gedrosselt oder verlangsamt werden. Ihre Domain oder IP könnte auch von den ISPs blockiert werden, was dazu führen kann, dass Ihre E-Mails direkt im Spam-Ordner des Posteingangs Ihrer Nutzer:innen landen. Daher ist es wichtig, dass Sie Ihre IPs richtig aufwärmen.

ISPs drosseln die E-Mail-Zustellung, wenn der Verdacht auf Spam aufkommt, um ihre Nutzer:innen zu schützen. Wenn Sie z. B. an 100.000 Nutzer:innen senden, kann es sein, dass der ISP die E-Mail in der ersten Stunde nur an 5.000 dieser Nutzer:innen zustellt. Dann überwacht der ISP Engagement-Metriken wie Öffnungsraten, Klickraten, Abmeldungen und Spam-Berichte. Wenn also eine beträchtliche Anzahl von Spam-Meldungen auftritt, kann es sein, dass der Rest der Sendung in den Spam-Ordner verschoben wird, anstatt sie an den Posteingang zuzustellen. 

Bei mäßigem Engagement kann es vorkommen, dass Ihre E-Mails weiterhin gedrosselt werden, um weitere Engagement-Daten zu sammeln und so mit größerer Sicherheit festzustellen, ob es sich bei der E-Mail um Spam handelt oder nicht. Wenn die E-Mail sehr hohe Engagement-Metriken aufweist, wird die Drosselung möglicherweise vollständig aufgehoben. Diese Daten werden verwendet, um eine E-Mail-Reputation zu erstellen, die letztendlich bestimmt, ob Ihre E-Mails automatisch als Spam gefiltert werden oder nicht.

Wenn Ihre Domain oder IP von einem ISP blockiert wird, finden Sie in den Nachrichtenprotokollen im [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) Informationen darüber, welche Websites Sie besuchen sollten, um bei diesen ISPs Einspruch einzulegen und von diesen Listen entfernt zu werden.

## Zeitpläne für das IP-Warming

Wir empfehlen dringend, einen IP-Warming-Zeitplan strikt einzuhalten, um die Zustellbarkeit zu unterstützen. Es ist auch wichtig, dass Sie keine Tage auslassen, da eine konsistente Skalierung die Zustellmetriken verbessert. Wählen Sie einen Zeitplan basierend auf Ihrem bestehenden E-Mail-Versandverlauf und Ihren Zustellbarkeitsmetriken.

{% alert tip %}
Wenn Sie an einer dedizierten Zustellbarkeitsressource als Teil Ihres Konto-Teams interessiert sind, wenden Sie sich an Ihren Braze Account Manager für weitere Informationen.
{% endalert %}

{% tabs local %}
{% tab Konservativ %}

Der konservative Zeitplan ist ein langsamerer, vorsichtigerer Ansatz, der dabei hilft, eine starke Absender-Reputation von Grund auf aufzubauen. Dies wird empfohlen, wenn Sie neu im E-Mail-Versand sind, von einer geteilten IP migrieren oder Zustellbarkeitsprobleme wie Drosselung oder Blocklisting durch einen Posteingangsanbieter erlebt haben.

Tag | Anzahl der zu sendenden E-Mails
----|---------------------
1 | 50
2 | 50
3 | 50
4 | 100
5 | 100
6 | 100
7 | 500
8 | 500
9 | 500
10 | 1.000
11 | 1.000
12 | 1.000
13 | 2.000
14 | 2.000
15 | 2.000
16 | 4.000
17 | 4.000
18 | 4.000
19 | 8.000
20 | 8.000
21 | 8.000
22+ | Alle 3 Tage verdoppeln, bis das gewünschte Volumen erreicht ist

{% endtab %}
{% tab Moderat %}

Der moderate Zeitplan ist ein ausgewogener Ansatz, der das Sendevolumen in einem gleichmäßigen Tempo steigert. Dies wird für die meisten Absender empfohlen, einschließlich derjenigen mit etwas E-Mail-Versandhistorie, die auf eine neue IP wechseln.

Tag | Anzahl der zu sendenden E-Mails
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1.000
5 | 2.000
6 | 4.000
7 | 8.000
8 | 16.000
9 | 25.000
10 | 35.000
11 | 50.000
12 | 75.000
13 | 100.000
14 | 150.000
15 | 200.000
16 | 275.000
17 | 375.000
18 | 500.000
19 | 650.000
20 | 825.000
21 | 1.000.000
22+ | Alle 2 Tage verdoppeln, bis das gewünschte Volumen erreicht ist

{% endtab %}
{% tab Aggressiv %}

{% alert important %}
Der aggressive Zeitplan ist der schnellste Ansatz und wird nur für Absender mit einer etablierten, positiven Versandhistorie und Zustellbarkeitsmetriken empfohlen, die den Best Practices entsprechen, einschließlich hoher Öffnungsraten, hoher Klickraten und niedriger Absprungraten. Die Verwendung dieses Zeitplans ohne nachgewiesene Erfolgsbilanz kann Ihrer Absender-Reputation schaden.
{% endalert %}

Tag | Anzahl der zu sendenden E-Mails
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1.000
5 | 2.500
6 | 5.000
7 | 9.000
8 | 16.000
9 | 29.000
10 | 52.000
11 | 98.000
12 | 160.000
13 | 225.000
14 | 315.000
15 | 450.000
16 | 615.000
17 | 875.000
18 | 1.200.000
19 | 1.750.000
20 | 2.750.000
21+ | Täglich verdoppeln, bis das gewünschte Volumen erreicht ist

{% endtab %}
{% endtabs %}

In den meisten Fällen sollten Sie auf Ihr durchschnittliches tägliches Sendevolumen aufwärmen, nicht auf Ihr Spitzenvolumen. ISPs betrachten hauptsächlich das Sendeverhalten der letzten Wochen, um Ihre Reputation zu bewerten. Wenn Sie also nur alle paar Monate ein Spitzenvolumen erreichen (z. B. 7 Millionen während einer saisonalen Phase), können Sie näher am Sendedatum auf dieses Spitzenvolumen hochfahren. Wenn Sie jedoch alle ein bis zwei Wochen ein Spitzenvolumen erreichen, sollten Sie von Anfang an auf dieses Spitzenvolumen aufwärmen.

Nachdem das IP-Warming abgeschlossen ist und Sie Ihr gewünschtes Tagesvolumen erreicht haben, sollten Sie versuchen, dieses Volumen täglich beizubehalten. Gewisse Schwankungen sind zu erwarten, jedoch kann das Erreichen des gewünschten Volumens und die anschließende Durchführung einer Massenversendung nur einmal pro Woche Ihre Zustellmetriken und Ihre Absender-Reputation negativ beeinflussen. 

{% alert important %}
Die meisten ISPs speichern Reputationsdaten nur für 30 Tage. Wenn Sie einen Monat lang keine Nachrichten senden, müssen Sie das IP-Warming wiederholen.
{% endalert %}

## Sendungen beim Warming begrenzen

Die integrierte Funktion zur Nutzereinschränkung ist ein nützliches Hilfsmittel, um Ihnen beim Warming Ihrer IP-Adresse zu helfen. Nachdem Sie bei der Kampagnenerstellung die gewünschten Messaging-Segmente ausgewählt haben, wählen Sie im Schritt [Zielgruppe zusammenstellen]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas) das Dropdown-Menü **Erweiterte Optionen**, um Ihre Nutzer:innen einzuschränken. Mit fortschreitendem Warming-Zeitplan können Sie dieses Limit schrittweise erhöhen, um das Volumen der von Ihnen gesendeten E-Mails zu steigern.

![]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentierung von Subdomains

Viele ISPs und E-Mail-Zugangsanbieter filtern nicht mehr nur anhand der Reputation der IP-Adresse. Diese Filtertechnologien berücksichtigen jetzt auch die Domain-basierte Reputation. Das bedeutet, dass die Filter alle mit der Domain des Absenders verbundenen Daten prüfen und nicht nur die IP-Adresse isoliert betrachten. Aus diesem Grund empfehlen wir Ihnen, nicht nur Ihre E-Mail-IP aufzuwärmen, sondern auch separate Domains oder Subdomains für Marketing-, Transaktions- und Unternehmens-E-Mails zu verwenden. 

{% alert important %}
Die Segmentierung von Subdomains ist besonders wichtig für Absender mit großem Volumen. Diese Absender sollten bei der Einrichtung ihres Kontos mit einer Braze-Vertretung zusammenarbeiten, um sicherzustellen, dass sie sich an diese Praxis halten.
{% endalert %}

Wir empfehlen Ihnen, Ihre Domains so zu segmentieren, dass Unternehmens-E-Mails über Ihre Top-Level-Domain und Marketing- und Transaktions-E-Mails über verschiedene Domains oder Subdomains gesendet werden.

## Best Practices

Sie können alle Konsequenzen eines nicht durchgeführten IP-Warmings vermeiden, indem Sie die folgenden Best Practices befolgen:

### Beginnen Sie mit einem kleinen E-Mail-Volumen

Erhöhen Sie die Menge, die Sie täglich senden, so allmählich wie möglich. Abrupte, umfangreiche E-Mail-Kampagnen werden von ISPs mit größter Skepsis betrachtet. Beginnen Sie daher mit dem Versenden kleinerer Mengen von E-Mails und steigern Sie diese allmählich auf das Volumen, das Sie letztendlich versenden möchten. Bedenken Sie, dass Sie Ihre IP bei jedem ISP einzeln aufwärmen – ISPs teilen keine Reputationsdaten untereinander. Achten Sie beim Aufbau Ihrer Warming-Volumen darauf, dass Sie das Volumen bei keinem einzelnen ISP zu schnell steigern. Unabhängig vom Volumen empfehlen wir, sicherheitshalber ein IP-Warming durchzuführen. Siehe [Zeitpläne für das IP-Warming](#ip-warming-schedules).

### Präsentieren Sie ansprechende Einführungsinhalte

Stellen Sie sicher, dass Ihr erster Inhalt sehr ansprechend ist und die Wahrscheinlichkeit maximiert, dass Nutzer:innen klicken, öffnen und sich mit Ihrer E-Mail beschäftigen. Bevorzugen Sie beim IP-Warming immer gezielte E-Mails gegenüber wahllosen Massenversendungen.

### Legen Sie eine konsistente Sendekadenz fest

Sobald das IP-Warming abgeschlossen ist, erstellen Sie eine Sendekadenz und achten Sie darauf, Ihre E-Mails über einen Tag oder mehrere Tage zu verteilen. Indem Sie einen möglichst konsistenten Zeitplan erstellen, können Sie einen IP-Cooldown verhindern, der auftreten kann, wenn das Sendevolumen für mehr als ein paar Tage aufhört oder deutlich abnimmt. 

Nutzen Sie unseren [Zeitplan für das IP-Warming](#ip-warming-schedules), um Ihren Versand über einen längeren Zeitraum zu verteilen, anstatt einen Massenversand zu einem bestimmten Zeitpunkt durchzuführen.

### Bereinigen Sie Ihre E-Mail-Listen

Stellen Sie sicher, dass Ihre E-Mail-Liste bereinigt ist und keine alten oder unverifizierten E-Mail-Adressen enthält. Idealerweise sollten Sie sicherstellen, dass Sie sowohl [CASL- als auch CAN-SPAM-konform]({{site.baseurl}}/user_guide/administrative/privacy/spam_regulations/) sind.

### Überwachen Sie Ihre Absender-Reputation

Achten Sie bei der Durchführung des IP-Warming-Prozesses darauf, Ihre Absender-Reputation sorgfältig zu überwachen. Diese spezifischen Metriken sind besonders wichtig:
- **Absprungraten:** Wenn eine Kampagne eine Absprungrate von mehr als 3–5 % aufweist, sollten Sie die Sauberkeit Ihrer Liste überprüfen, indem Sie die Richtlinien in unserem Artikel [Keep It Clean: The Importance of Email List Hygiene](https://www.braze.com/blog/email-list-hygiene/) befolgen. Außerdem sollten Sie eine [Sunset-Richtlinie]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/) in Betracht ziehen, um das Senden an nicht engagierte oder inaktive E-Mail-Adressen einzustellen.
- **Spam-Berichte:** Wenn eine Kampagne zu mehr als 0,08 % als Spam gemeldet wird, sollten Sie den Inhalt, den Sie versenden, neu bewerten, überprüfen, ob er auf eine interessierte Zielgruppe ausgerichtet ist, und sicherstellen, dass Ihre E-Mails so formuliert sind, dass sie deren Interesse wecken.
- **Öffnungsraten:** Öffnungsraten sind ein nützlicher Indikator für die Platzierung im Posteingang. Wenn Ihre eindeutigen Öffnungsraten über 25 % liegen, haben Sie wahrscheinlich eine hohe Platzierung im Posteingang, was auf eine positive Absender-Reputation hinweist.

{% alert tip %}
Braze empfiehlt, [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) nicht zum Aufwärmen Ihrer IPs zu verwenden. Da IP-Warming-Kampagnen zu den ersten Kampagnen gehören, die Sie versenden, verfügt Braze nicht über genügend Informationen über Ihre Nutzer:innen, um einen optimalen Sendezeitpunkt zu berechnen. In diesem Fall würden alle Nachrichten mit intelligentem Timing standardmäßig auf die Fallback-Zeit zurückfallen und ohnehin zur gleichen Zeit gesendet.
{% endalert %}

{% alert tip %}
Es ist normal, dass E-Mails während des IP-Warmings im Spam-Ordner landen, da Ihre Domain und IP noch keine positive Reputation aufgebaut haben. Wenn E-Mails in Ihrem Spam-Ordner landen, muss Ihr E-Mail-Administrator möglicherweise Ihre Braze-Sendedomain und IP-Adresse zur Allowlist Ihres Unternehmens hinzufügen.
{% endalert %}