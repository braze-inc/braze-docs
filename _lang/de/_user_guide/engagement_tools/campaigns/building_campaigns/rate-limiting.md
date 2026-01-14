---
nav_title: Rate-Limiting und Frequency-Capping
article_title: Rate-Limiting und Frequency-Capping
page_order: 6
tool: Campaigns
page_type: reference
description: "In diesem Referenzartikel wird das Konzept der Ratenbegrenzung und der Frequenzbegrenzung in Kampagnen erörtert und wie Sie den Marketingdruck steuern können, um die Nutzererfahrung zu verbessern."

---

# Rate-Limiting und Frequency-Capping

> Ratenbegrenzung und Häufigkeitsbegrenzung können zusammen verwendet werden, um sicherzustellen, dass Ihre Nutzer die Nachrichten erhalten, die sie benötigen, und keine, die sie nicht benötigen.

## Über Rate-Limiting

Braze ermöglicht es Ihnen, den Druck im Marketing zu kontrollieren, indem Sie Ihre Kampagnen mit Rate-Limiting versehen und so die Menge des von Ihrer Plattform ausgehenden Datenverkehrs regulieren. Sie können zwei verschiedene Arten der Preisbegrenzung für Ihre Kampagnen einsetzen: 

1. [**Nutzerzentriertes Rate-Limiting:**](#user-centric-rate-limiting) Konzentriert sich darauf, den Nutzer:innen das beste Erlebnis zu bieten.
2. [**Begrenzung der Liefergeschwindigkeit:**](#delivery-speed-rate-limiting) Berücksichtigt die Bandbreite Ihrer Server.

Braze wird versuchen, die gesendeten Nachrichten gleichmäßig über die Minute zu verteilen, kann dies aber nicht garantieren. Wenn Sie beispielsweise eine Kampagne mit einem Rate-Limit von 5.000 Nachrichten pro Minute haben, versuchen wir, die 5.000 Anfragen gleichmäßig über die Minute zu verteilen (etwa 84 Nachrichten pro Sekunde), aber die Rate pro Sekunde kann variieren.

### Benutzerzentrierte Ratenbegrenzung

Wenn Sie mehr Segmente erstellen, wird es Fälle geben, in denen sich die Mitgliedschaft in diesen Segmenten überschneidet. Wenn Sie Kampagnen an diese Segmente versenden, sollten Sie darauf achten, dass Sie Ihre Nutzer nicht zu oft anschreiben. Wenn ein Benutzer zu viele Nachrichten innerhalb eines kurzen Zeitraums erhält, wird er sich überfordert fühlen und entweder die Push-Benachrichtigungen deaktivieren oder Ihre App deinstallieren.

#### Relevante Segmentfilter

Braze stellt Ihnen die folgenden Filter zur Verfügung, mit denen Sie die Geschwindigkeit, mit der Ihre Benutzer Nachrichten erhalten, begrenzen können:

- Letzte Interaktion mit Nachricht
- Empfangszeitpunkt der letzten Nachricht
- Letzte erhaltene Push-Kampagne
- Zuletzt empfangene E-Mail-Kampagne
- Letzte empfangene SMS

#### Implementieren von Filtern

Nehmen wir an, wir haben ein Segment mit dem Namen "Retargeting Filter Showcase" mit dem Filter "Diese Apps wurden zuletzt vor mehr als 7 Tagen verwendet" erstellt, um Nutzer anzusprechen. Dies wäre ein Standardsegment für erneute Interaktion.

Wenn Sie andere zielgerichtetere Segmente haben, die in letzter Zeit Benachrichtigungen erhalten haben, möchten Sie vielleicht nicht, dass Ihre Nutzer durch allgemeinere Kampagnen, die an dieses Segment gerichtet sind, angesprochen werden. Durch das Anhängen des Filters "Zuletzt erhaltene Push-Kampagne" an dieses Segment hat der Benutzer sichergestellt, dass er, wenn er in den letzten 24 Stunden eine andere Benachrichtigung erhalten hat, für die nächsten 24 Stunden aus diesem Segment herausfällt. Wenn sie 24 Stunden später immer noch die anderen Kriterien des Segments erfüllen und keine weiteren Benachrichtigungen erhalten haben, werden sie wieder in das Segment aufgenommen.

![Abschnitt Segmentdetails mit hervorgehobenem Filter für das Segment "Zuletzt empfangene Nachricht".]({% image_buster /assets/img_archive/rate_limit_daily.png %})

Wenn Sie diesen Filter an alle Segmente anhängen, auf die Ihre Kampagnen abzielen, erhalten Ihre Nutzer maximal einen Push alle 24 Stunden. Sie können dann Ihre Nachrichten nach Prioritäten ordnen und sicherstellen, dass Ihre wichtigsten Nachrichten vor den weniger wichtigen Nachrichten zugestellt werden.

#### Festlegen einer maximalen Nutzer:innen-Begrenzung

Im Schritt **Zielgruppen** Ihres Kampagnen-Editors können Sie auch die Gesamtzahl der Nutzer:innen begrenzen, die Ihre Nachricht erhalten sollen. Dies dient als Kontrolle, die unabhängig von Ihren Kampagnenfiltern ist. So können Sie die Nutzer frei segmentieren, ohne sich Sorgen über zu viel Spam machen zu müssen.

![Zusammenfassung der Zielgruppe mit einem ausgewählten Kontrollkästchen zur Begrenzung der Anzahl der Personen, die die Kampagne erhalten.]({% image_buster /assets/img_archive/total_limit.png %})

Durch die Auswahl des maximalen Benutzerlimits können Sie die Rate, mit der Ihre Benutzer Benachrichtigungen erhalten, pro Kanal oder global für alle Nachrichtentypen begrenzen.

##### Maximale Benutzerkapazität mit Optimierungen

Wenn Sie eine Optimierung wie Winning Variant oder Personalized Variant verwenden, besteht die Kampagne aus zwei Sendungen: dem anfänglichen Experiment und der endgültigen Sendung. 

Um in diesem Szenario eine maximale Benutzerzahl festzulegen, markieren Sie die Option **Anzahl der Personen begrenzen, die diese Kampagne erhalten sollen**, wählen Sie dann **Insgesamt sollte diese Kampagne** und geben Sie ein Zielgruppenlimit ein. Ihre Zielgruppe wird durch die im **A/B-Test-Panel** angezeigten Prozentsätze aufgeteilt. 

Wenn Sie **Jedes Mal, wenn die Kampagne geplant wird,** auswählen, werden diese beiden Phasen separat auf die eingestellte Anzahl begrenzt. Dies ist in der Regel nicht wünschenswert.

#### Festlegen einer Obergrenze für Impressionen

Für In-App-Nachrichten und Content Cards können Sie den Marketingdruck kontrollieren, indem Sie eine maximale Anzahl von Impressionen festlegen, die Ihrer Benutzerbasis angezeigt werden. Danach wird Braze keine weiteren Nachrichten an Ihre Benutzer senden. Es ist jedoch wichtig zu beachten, dass diese Obergrenze nicht exakt ist. 

Neue Inhaltskarten und Regeln für In-App-Nachrichten werden beim Start einer Sitzung an eine App gesendet. Das bedeutet, dass Braze eine Nachricht an den Benutzer senden kann, bevor die Obergrenze erreicht ist, aber zu dem Zeitpunkt, an dem der Benutzer die Nachricht auslöst, ist die Obergrenze bereits erreicht. In diesem Fall zeigt das Gerät weiterhin die Meldung an.

Nehmen wir zum Beispiel an, Sie haben ein Spiel mit einer In-App-Nachricht, die ausgelöst wird, wenn ein Nutzer ein Level besiegt, und Sie begrenzen diese auf 100 Impressionen. Bisher gab es 99 Eindrücke. Alice und Bob öffnen beide das Spiel und Braze teilt ihren Geräten mit, dass sie berechtigt sind, die Nachricht zu erhalten, wenn sie einen Level geschafft haben. Alice schafft zuerst ein Level und erhält die Nachricht. Bob schlägt das nächste Level, aber da sein Gerät seit Beginn der Sitzung nicht mit den Braze-Servern kommuniziert hat, weiß sein Gerät nicht, dass die Nachricht ihre Obergrenze erreicht hat und er wird die Nachricht ebenfalls erhalten. Wenn jedoch die Obergrenze für die Anzahl der Impressionen erreicht ist, wird die Nachricht bei der nächsten Anfrage eines Geräts nach der Liste der zulässigen In-App-Nachrichten nicht mehr gesendet und von diesem Gerät entfernt.

### Ratenbegrenzung und A/B-Tests

Wenn Sie die Ratenbegrenzung bei einem A/B-Test verwenden, wird die Ratenbegrenzung nicht in gleicher Weise auf die Kontrollgruppe angewandt wie auf die Testgruppe, was eine potenzielle Quelle für zeitliche Verzerrungen ist. Um diese Verzerrung zu vermeiden, verwenden Sie geeignete Konversionsfenster.

### Rate-Limiting für die Zustellungsgeschwindigkeit

Wenn Sie davon ausgehen, dass große Kampagnen zu einem Anstieg der Nutzer:innen-Aktivitäten führen und Ihre Server überlasten, können Sie ein Rate-Limits für den Versand von Nachrichten pro Minute festlegen. Das bedeutet, dass Braze innerhalb einer Minute nicht mehr als das von Ihnen festgelegte Rate-Limits sendet.

Wenn Sie während der Kampagnenerstellung Benutzer ansprechen, können Sie unter **Zielgruppen** (für Kampagnen) oder **Sendeeinstellungen** (für Canvas) ein Ratenlimit auswählen (in verschiedenen Abstufungen von 10 bis 500.000 Nachrichten pro Minute).

Beachten Sie, dass Kampagnen ohne Rate-Limits diese Zustellungslimits überschreiten können. Beachten Sie jedoch, dass Nachrichten abgebrochen werden, wenn sie aufgrund eines niedrigen Rate-Limits 72 Stunden oder länger auf sich warten lassen. Wenn das Ratenlimit zu niedrig ist, erhält der Ersteller der Kampagne Warnungen im Dashboard und per E-Mail.

![Zusammenfassung der Zielgruppe mit einem ausgewählten Kontrollkästchen zur Begrenzung der Rate, mit der die Kampagne endet, und einer Rate von 500.000 pro Minute.]({% image_buster /assets/img_archive/per_minute_rate_limit.png %})

#### Beispiel

Wenn Sie versuchen, 75.000 Nachrichten mit einem Rate-Limit von 10.000 pro Minute zu versenden, wird die Zustellung auf acht Minuten verteilt. Ihre Kampagne wird nicht mehr als 10.000 Nachrichten in den ersten sieben Minuten und 5.000 in der letzten Minute zugestellt.

#### Anzahl der Sendungen

Beachten Sie, dass Nachrichten mit Ratenbeschränkung möglicherweise nicht gleichmäßig über jede Minute gesendet werden. Am Beispiel eines Rate-Limits von 10.000 pro Minute bedeutet dies, dass Braze sicherstellt, dass nicht mehr als 10.000 Nachrichten pro Minute gesendet werden. Das könnte bedeuten, dass ein höherer Prozentsatz der 10.000 Nachrichten innerhalb der ersten halben Minute gesendet wird als in der letzten halben Minute.

Das Rate-Limit wird zu Beginn des Sendeversuchs einer Nachricht angewendet. Bei Schwankungen in der Sendezeit kann die Anzahl der abgeschlossenen Sendungen das Rate-Limit in einigen Minuten leicht überschreiten. Mit der Zeit wird die Anzahl der Sendungen pro Minute im Durchschnitt nicht mehr als das Rate-Limit betragen.

{% alert important %}
Seien Sie vorsichtig, wenn Sie zeitkritische Nachrichten mit dieser Form des Rate-Limiting in Bezug auf die Gesamtzahl der Nutzer:innen in einem Segment verzögern. Wenn das Segment beispielsweise 30 Millionen Nutzer:innen umfasst, wir aber das Rate-Limits auf 10.000 pro Minute festlegen, wird ein großer Teil Ihrer Nutzer:innen die Nachricht erst am nächsten Tag erhalten.
{% endalert %}

#### Kampagnen mit einem Kanal

Wenn Sie eine Kampagne mit einem Kanal und einem Rate-Limit versenden, wird das Rate-Limit für alle Nachrichten zusammen angewendet.

#### Mehrkanalige Kampagnen

Wenn Sie eine Multichannel-Kampagne mit einem Rate-Limit versenden, wird jeder Kanal unabhängig von den anderen gesendet. Infolgedessen kann Folgendes passieren:

- Die Gesamtzahl der pro Minute gesendeten Nachrichten könnte über dem Rate-Limit liegen. 
    - Wenn Ihre Kampagne beispielsweise ein Ratenlimit von 10.000 pro Minute hat und E-Mail und SMS verwendet, kann Braze insgesamt maximal 20.000 Nachrichten pro Minute versenden (10.000 E-Mail und 10.000 SMS).
- Die Nutzer können die verschiedenen Kanäle zu unterschiedlichen Zeiten empfangen, und es ist nicht vorhersehbar, welchen Kanal sie zuerst erhalten werden. 
    - Wenn Sie beispielsweise eine Kampagne versenden, die eine E-Mail und eine SMS enthält, haben Sie vielleicht 10.000 Nutzer mit gültigen Telefonnummern und 50.000 Nutzer mit gültigen E-Mail-Adressen. Wenn Sie die Kampagne so einstellen, dass 100 Nachrichten pro Minute versendet werden (eine langsame Ratengrenze für die Größe der Kampagne), könnte ein Benutzer die SMS im ersten Stapel von Sendungen und die E-Mail im letzten Stapel von Sendungen erhalten, also fast neun Stunden später.

#### Plattformübergreifende Push-Kampagnen

Bei Push-Kampagnen, die auf mehreren Plattformen durchgeführt werden, wird das gewählte Preislimit gleichmäßig auf die Plattformen verteilt. Bei einer Push-Kampagne für Android und iOS mit einem Ratenlimit von 10.000 pro Minute werden die 10.000 Nachrichten gleichmäßig auf die beiden Plattformen verteilt.

#### Rate-Limiting für die Canvas-Zustellungsgeschwindigkeit {#canvas-delivery-speed}

Wenn Sie ein Canvas mit einem Rate-Limit senden, wird das Rate-Limit zwischen den Kanälen aufgeteilt. Das bedeutet, dass die Gesamtzahl der pro Minute vom Canvas gesendeten Nachrichten das Ratenlimit nicht überschreiten wird. Wenn Ihr Canvas beispielsweise ein Ratenlimit von 10.000 pro Minute hat und E-Mail und SMS verwendet, wird Braze insgesamt 10.000 Nachrichten pro Minute per E-Mail und SMS versenden.

#### Ratenbegrenzung und Wiederholungsversuche für Connected Content

Wenn die [Wiederholungsfunktion für Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/) aktiviert ist, wiederholt Braze fehlgeschlagene Anrufe unter Einhaltung des Rate-Limits, das Sie für jede erneute Übertragung festgelegt haben. Betrachten wir das Szenario des Versands von 75.000 Nachrichten mit einem Rate-Limit von 10.000 pro Minute. Stellen Sie sich vor, dass der Anruf in der ersten Minute fehlschlägt oder langsam ist und nur 4.000 Nachrichten versendet.

Anstatt zu versuchen, die Verzögerung auszugleichen und die verbleibenden 6.000 Nachrichten in der zweiten Minute zu senden oder sie zu den 10.000 Nachrichten hinzuzufügen, die bereits zum Senden eingestellt sind, verschiebt Braze diese 6.000 Nachrichten in die "hintere Warteschlange" und fügt gegebenenfalls eine Minute zu den Gesamtminuten hinzu, die für das Senden Ihrer Nachricht erforderlich wären.

| Minute | Kein Misserfolg | 6.000 Versagen in Minute 1 |
|--------|------------|---------------------------|
| (1 %)      | 10,000     | 4,000                     |
| (2 %)      | 10,000     | 10,000                    |
| 3      | 10,000     | 10,000                    |
| (4 %)      | 10,000     | 10,000                    |
| (5 %)      | 10,000     | 10,000                    |
| 6      | 10,000     | 10,000                    |
| (7 %)      | 10,000     | 10,000                    |
| (8 %)      | (5,000 %)      | 10,000                    |
| (9 %)      | 0          | 6,000                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Connected-Content-Anfragen sind nicht unabhängig voneinander Rate-Limits unterworfen und folgen dem Rate-Limit des Webhooks. Das bedeutet, dass Sie bei einem Connected-Content-Aufruf an einen eindeutigen Endpunkt pro Webhook mit 5.000 Webhooks und auch 5.000 Connected-Content-Aufrufen pro Minute rechnen müssen. Beachten Sie, dass die Zwischenspeicherung dies beeinflussen und die Anzahl der Connected-Content-Aufrufe reduzieren kann. Außerdem können Wiederholungsversuche die Connected-Content-Aufrufe erhöhen. Wir empfehlen daher zu überprüfen, ob der Connected-Content-Endpunkt hier mit einer gewissen Fluktuation umgehen kann.

## Über Frequency-Capping

Wenn Ihre Nutzerbasis weiter wächst und Ihre Nachrichten auf Lebenszyklus-, Trigger-, Transaktions- und Konversionskampagnen ausgeweitet werden, ist es wichtig, dass Ihre Benachrichtigungen nicht als „Spam“ oder störend empfunden werden. Durch eine bessere Kontrolle über die Erfahrung Ihrer Nutzer ermöglicht Ihnen die Frequenzbegrenzung die Erstellung der gewünschten Kampagnen, ohne Ihr Publikum zu überfordern.

### Übersicht über die Features {#freq-cap-feat-over}

Die Frequenzbegrenzung wird auf der Ebene der Kampagne oder der Canvas-Komponente angewendet und kann für jeden Arbeitsbereich unter **Einstellungen** > **Frequenzbegrenzungsregeln** eingerichtet werden.

Standardmäßig ist das Frequency-Capping aktiviert, wenn neue Kampagnen erstellt werden. Von hier aus können Sie Folgendes auswählen:

- Welchen Nachrichtenkanal möchten Sie begrenzen: Push, E-Mail, SMS, Webhook, WhatsApp oder einen dieser fünf?
- Wie oft jeder Benutzer innerhalb eines bestimmten Zeitrahmens eine Kampagne oder eine Canvas-Komponente von einem Kanal gesendet bekommen soll.
- Wie oft jeder Benutzer innerhalb eines bestimmten Zeitraums eine Kampagne oder eine Canvas-Komponente per [Tag](#frequency-capping-by-tag) erhalten soll.

Dieser Zeitrahmen kann in Minuten, Tagen oder Wochen (sieben Tage) gemessen werden, wobei die maximale Dauer 30 Tage beträgt.

Jede Frequency-Capping-Zeile wird mit dem Operator `AND` verbunden, und Sie können bis zu 10 Regeln pro Workspace hinzufügen. Außerdem können Sie mehrere Obergrenzen für dieselben Nachrichtenarten festlegen. So können Sie beispielsweise die Anzahl der Nutzer auf einen Push pro Tag und drei Pushs pro Woche begrenzen.

![Frequency-Capping-Abschnitt mit Listen von Kampagnen und Canvase, für die die Regeln gelten und nicht gelten werden.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %})

#### Verhalten bei Frequency-Capping von Nutzer:innen in einem Canvas-Schritt

Wenn ein Canvas-Nutzer:innen aufgrund globaler Einstellungen für Frequency-Capping mit einem Frequency-Capping belegt ist, wird der Nutzer:innen sofort zum nächsten Canvas-Schritt vorgebracht. Der Nutzer:innen wird den Canvas wegen des Frequency-Cappings nicht verlassen.

### Regeln für die Zustellung

Es gibt vielleicht Kampagnen, wie z.B. Transaktionsnachrichten, die den Nutzer immer erreichen sollen, auch wenn er seine Frequenzgrenze bereits erreicht hat. Eine Zustellungs-App kann zum Beispiel eine E-Mail oder eine Push-Mitteilung senden, wenn ein Artikel zugestellt wurde, unabhängig davon, wie viele Kampagnen der Benutzer erhalten hat.

Wenn Sie möchten, dass eine bestimmte Kampagne die Regeln für die Frequenzbegrenzung außer Kraft setzt, können Sie dies im Braze-Dashboard bei der Planung der Zustellung dieser Kampagne einrichten, indem Sie die **Frequenzbegrenzung** auf **AUS** setzen. 

Danach werden Sie gefragt, ob Sie diese Kampagne immer noch auf Ihre Frequenzobergrenze anrechnen lassen möchten. Nachrichten, die zum Frequency-Capping zählen, werden in die Berechnungen für den Filter „Intelligenter Kanal“ einbezogen. Beim Versenden von [API Kampagnen]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), die oft transaktional sind, können Sie angeben, dass eine Kampagne Frequency-Capping Regeln [innerhalb der API Anfrage]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns) ignorieren soll, indem Sie `override_messaging_limits` auf `true` setzen.

Neue Kampagnen und Canvases, die sich nicht an die Häufigkeitsobergrenzen halten, werden standardmäßig auch nicht auf diese angerechnet. Dies ist für jede Kampagne und jeden Canvas konfigurierbar.

{% alert note %}
Dieses Verhalten ändert das Standardverhalten, wenn Sie das Frequency-Capping für eine Kampagne oder ein Canvas deaktivieren. Die Änderungen sind abwärtskompatibel und wirken sich nicht auf Nachrichten aus, die derzeit live geschaltet sind.
{% endalert %}

![Bereich Zustellungssteuerung mit eingeschaltetem Frequency-Capping.]({% image_buster /assets/img_archive/frequencycappingupdate.png %})

Verschiedene Kanäle innerhalb einer Multichannel-Kampagne zählen individuell die Frequenzobergrenze. Wenn Sie z.B. eine Multichannel-Kampagne mit Push- und E-Mail-Kampagnen erstellen und für beide Kanäle eine Frequenzbegrenzung eingerichtet haben, wird die Push-Nachricht für eine Push-Kampagne und die E-Mail-Nachricht für eine E-Mail-Kampagne gezählt. Die Kampagne wird auch als eine „Kampagne jeglicher Art“ angerechnet. Wenn Benutzer auf eine Push- und eine E-Mail-Kampagne pro Tag beschränkt sind und ein Benutzer diese Multichannel-Kampagne erhält, kann er für den Rest des Tages keine Push- oder E-Mail-Kampagnen mehr erhalten (es sei denn, eine Kampagne ignoriert die Regeln für die Frequenzbegrenzung).

In-App-Nachrichten und Content-Cards werden nicht als Obergrenzen für Kampagnen oder Canvas-Komponenten jeglicher Art gezählt oder auf diese angerechnet.

{% alert important %}
Die globale Frequenzbegrenzung basiert auf der Zeitzone des Benutzers und wird nach Kalendertagen und nicht nach 24-Stunden-Perioden berechnet. Wenn Sie z. B. eine Regel zur Begrenzung der Häufigkeit des Versands von maximal einer Kampagne pro Tag einrichten, kann ein Benutzer um 23 Uhr in seiner lokalen Zeitzone eine Nachricht erhalten und wäre eine Stunde später zum Empfang einer weiteren Nachricht berechtigt.
{% endalert %}

#### Anwendungsfälle

{% tabs %}
{% tab Use case 1 %}

Nehmen wir an, Sie legen eine Frequency-Capping-Regel fest, die vorsieht, dass Ihr Nutzer:innen nicht mehr als drei Push-Benachrichtigungen pro Woche von allen Kampagnen oder Canvas-Komponenten erhalten.

Wenn Ihr Nutzer in dieser Woche drei Push-Benachrichtigungen, zwei In-App-Nachrichten und eine Content Card erhalten soll, wird er alle diese Nachrichten erhalten.

{% endtab %}
{% tab Use case 2 %}

Dieses Szenario verwendet die folgenden Regeln für die Frequenzbegrenzung:

**Wenn folgendes Szenario eintritt:**

- Ein Nutzer:innen triggert dieselbe Kampagne, `Campaign ABC`, dreimal im Laufe einer Woche.
- Dieser Nutzer:innen triggert `Campaign ABC` einmal am Montag, einmal am Mittwoch und einmal am Donnerstag.

![Abschnitt Frequency-Capping mit der Regel, nicht mehr als 2 Push-Benachrichtigungen Kampagnen/Canvas-Schritte von allen Kampagnen/Canvas-Schritten an einen Nutzer:innen alle 1 Woche zu senden.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Dann lautet das erwartete Verhalten wie folgt:**

- Dieser Benutzer wird die Kampagnensendungen erhalten, die am Montag und Mittwoch ausgelöst wurden.
- Dieser Benutzer wird die dritte Kampagnensendung am Donnerstag nicht erhalten, da er in dieser Woche bereits zwei Push-Kampagnensendungen erhalten hat.

{% endtab %}
{% endtabs %}

### Frequency-Capping nach Tag

[Regeln für die Frequenzbegrenzung](#delivery-rules) können auf Arbeitsbereiche angewendet werden, indem Sie bestimmte Tags verwenden, die Sie auf Ihre Kampagnen und Canvases angewendet haben, so dass Sie Ihre Frequenzbegrenzung im Wesentlichen auf benutzerdefinierte Gruppen stützen können.

Mit der Frequenzkappung nach Tag können Regeln für die Haupt- und verschachtelten Tags festgelegt werden, so dass Braze alle Tags berücksichtigt. Wenn Sie beispielsweise das Haupt-Tag A zum Frequenz-Capping verwenden, werden bei der Festlegung des Grenzwerts auch Informationen in allen verschachtelten Tags (z. B. Tags B und C) berücksichtigt.

Sie können auch die reguläre Frequenzkappung mit der Frequenzkappung durch Tags kombinieren. Beachten Sie die folgenden Regeln:

1. Nicht mehr als drei Push-Benachrichtigungskampagnen oder Canvas-Komponenten pro Woche aus allen Kampagnen- und Canvas-Schritten. <br>**UND**
2. Nicht mehr als zwei Push-Benachrichtigungs-Kampagnen oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Abschnitt Frequency-Capping mit zwei Regeln, die begrenzen, wie viele Push-Benachrichtigungen Kampagnen/Canvase pro 1 Woche an einen Nutzer:innen gesendet werden können.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Infolgedessen erhalten Ihre Benutzer nicht mehr als drei Kampagnensendungen pro Woche über alle Kampagnen und Canvas-Schritte und nicht mehr als zwei Push-Benachrichtigungskampagnen oder Canvas-Komponenten mit dem Tag `promotional`.

{% alert important %}
Leinwände werden auf der Ebene der Leinwand getaggt, im Gegensatz zum Tagging nach Komponente. Jede Canvas-Komponente erbt also alle Tags der Canvas-Ebene.
{% endalert %}

#### Widersprüchliche Regeln

Wenn sich Regeln widersprechen, wird die restriktivste, anwendbare Frequenzbegrenzungsregel auf Ihre Benutzer angewendet. Nehmen wir zum Beispiel an, Sie haben die folgenden Regeln:

1. Nicht mehr als eine Push-Benachrichtigungskampagne oder Canvas-Komponente pro Woche von allen Kampagnen und Canvas-Komponenten. <br>**UND**
2. Nicht mehr als drei Push-Benachrichtigungskampagnen oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Abschnitt Frequency-Capping mit widersprüchlichen Regeln, um zu begrenzen, wie viele Push-Benachrichtigungen Kampagnen/Canvas-Schritte pro 1 Woche an einen Nutzer:innen gesendet werden.]({% image_buster /assets/img/global_rules.png %} "global rules")

In diesem Beispiel wird Ihr Benutzer in einer bestimmten Woche nicht mehr als eine Push-Benachrichtigungskampagne oder Canvas-Komponente mit dem Tag "Werbeaktion" erhalten, da Sie festgelegt haben, dass Benutzer nicht mehr als eine Push-Benachrichtigungskampagne oder Canvas-Komponente von allen Kampagnen und Canvas-Komponenten erhalten sollen. Mit anderen Worten, die restriktivste anwendbare Frequenzregel ist die Regel, die auf einen bestimmten Benutzer angewendet wird.

#### Anzahl der Tags

Die Frequenzbegrenzung durch Tag-Regeln wird zum Zeitpunkt des Sendens einer Nachricht berechnet. Das bedeutet, dass die Häufigkeitsbegrenzung nach Tags nur die Tags zählt, die sich derzeit in den Kampagnen oder Canvases befinden, die ein Benutzer in der Vergangenheit erhalten hat. Nicht mitgezählt werden die Tags, die sich zum Zeitpunkt des Versands auf den Kampagnen oder Leinwänden befanden, aber inzwischen wieder entfernt wurden. Es wird gezählt, wenn ein Tag später zu einer Nachricht hinzugefügt wird, die ein Nutzer:innen in der Vergangenheit erhalten hat, aber bevor die neueste getaggte Nachricht gesendet wurde.

##### Anwendungsfall

Betrachten Sie die folgenden Kampagnen und die Begrenzung der Häufigkeit nach Tag-Regeln:

**Kampagnen**:

- **Kampagne A** ist eine Push-Kampagne mit dem Tag `promotional`. Es soll am Montag um 9 Uhr gesendet werden.
- **Kampagne B** ist eine Push-Kampagne mit der Bezeichnung `promotional`. Sie soll am Mittwoch um 9 Uhr gesendet werden.

**Frequency-Capping nach Tag-Regel:**

- Ihr Benutzer sollte nicht mehr als eine Push-Benachrichtigungskampagne pro Woche mit dem Tag `promotional` erhalten.<br><br>

| Aktion | Ergebnis |
|---|---|
| Der Tag `promotional` wird aus **Kampagne A** entfernt, nachdem Ihr Nutzer:innen die Nachricht erhalten hat, aber bevor **Kampagne B gesendet wurde.** | Ihr Nutzer erhält **Kampagne B**.|
| Das Tag `promotional` wurde versehentlich aus **Kampagne A** entfernt, nachdem Ihr Benutzer die Nachricht erhalten hat. <br> Der Tag wird am Dienstag wieder zu **Kampagne A** hinzugefügt, bevor **Kampagne B** versendet wird. | Ihr Benutzer wird keine **Kampagne B** erhalten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Versenden in großem Maßstab {#sending-at-large-scales}

„Frequency-Capping nach Tag-Regeln“ wird bei großen Skalen, wie z. B. 100 Nachrichten pro Kanal aus Kampagnen oder Canvas-Komponenten, möglicherweise nicht richtig angewendet.

Wenn Ihre Regel für die Frequenzbegrenzung nach Tag zum Beispiel lautet:

> Nicht mehr als zwei E-Mail-Kampagnen oder Canvas-Komponenten mit dem Tag `Promotional` für einen Benutzer pro Woche.

Und wenn Sie dem Benutzer im Laufe einer Woche mehr als 100 E-Mails aus Kampagnen und Canvas-Schritten mit eingeschalteter Häufigkeitsbegrenzung senden, werden möglicherweise mehr als zwei E-Mails an den Benutzer gesendet.

Da 100 Nachrichten pro Kanal mehr Nachrichten sind, als die meisten Marken an ihre Nutzer senden, ist es unwahrscheinlich, dass Sie von dieser Einschränkung betroffen sind. Um diese Einschränkung zu vermeiden, können Sie eine Obergrenze für die maximale Anzahl von E-Mails festlegen, die Ihre Benutzer im Laufe einer Woche erhalten sollen.

Sie könnten zum Beispiel die folgende Regel aufstellen:

> Nicht mehr als drei E-Mail-Kampagnen oder Canvas-Komponenten pro Woche aus allen Kampagnen- und Canvas-Schritten.

Diese Regel stellt sicher, dass kein Benutzer mehr als 100 E-Mails pro Woche erhält, da Benutzer höchstens drei E-Mails pro Woche von Kampagnen oder Canvas-Komponenten mit aktivierter Frequenzbegrenzung erhalten.

