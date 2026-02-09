---
nav_title: Rate-Limiting und Frequency-Capping
article_title: Rate-Limiting und Frequency-Capping
page_order: 6
tool: Campaigns
page_type: reference
description: "In diesem Referenzartikel wird das Konzept der Ratenbegrenzung und der Frequenzbegrenzung in Kampagnen erörtert und wie Sie den Marketingdruck steuern können, um die Nutzererfahrung zu verbessern."

---

# Rate-Limiting und Frequency-Capping

> Rate-Limits und Frequency-Capping können zusammen verwendet werden, um sicherzustellen, dass Ihre Nutzer:innen die Nachrichten erhalten, die sie benötigen.

## Über Rate-Limiting

Braze ermöglicht es Ihnen, den Druck im Marketing zu kontrollieren, indem Sie Ihre Kampagnen mit Rate-Limiting versehen und so die Menge des von Ihrer Plattform ausgehenden Datenverkehrs regulieren. Sie können zwei verschiedene Arten der Preisbegrenzung für Ihre Kampagnen einsetzen: 

1. [**Nutzerzentriertes Rate-Limiting:**](#user-centric-rate-limiting) Konzentriert sich darauf, den Nutzer:innen das beste Erlebnis zu bieten.
2. [**Begrenzung der Liefergeschwindigkeit:**](#delivery-speed-rate-limiting) Berücksichtigt die Bandbreite Ihrer Server.

Braze wird versuchen, die gesendeten Nachrichten gleichmäßig über die Minute zu verteilen, kann dies aber nicht garantieren. Wenn Sie beispielsweise eine Kampagne mit einem Rate-Limit von 5.000 Nachrichten pro Minute haben, versuchen wir, die 5.000 Anfragen gleichmäßig über die Minute zu verteilen (etwa 84 Nachrichten pro Sekunde), aber die Rate pro Sekunde kann variieren.

### Benutzerzentrierte Ratenbegrenzung

Wenn Sie mehr Segmente erstellen, wird es Fälle geben, in denen sich die Mitgliedschaft in diesen Segmenten überschneidet. Wenn Sie Kampagnen an diese Segmente versenden, sollten Sie darauf achten, dass Sie Ihre Nutzer nicht zu oft anschreiben. Wenn ein Benutzer zu viele Nachrichten innerhalb eines kurzen Zeitraums erhält, wird er sich überfordert fühlen und entweder die Push-Benachrichtigungen deaktivieren oder Ihre App deinstallieren.

#### Relevante Segmentfilter

Braze stellt Ihnen die folgenden Filter zur Verfügung, mit denen Sie die Geschwindigkeit, mit der Ihre Nutzer:innen Nachrichten erhalten, begrenzen können:

- Letzte Interaktion mit Nachricht
- Empfangszeitpunkt der letzten Nachricht
- Letzter empfangener Push
- Letzte empfangene E-Mail
- Letzte empfangene SMS

#### Implementieren von Filtern

Nehmen wir an, wir haben ein Segment mit dem Namen "Retargeting Filter Showcase" mit einem Filter "Letzte Nutzung der App vor mehr als 7 Tagen" erstellt, um Nutzer:innen zu targetieren. Dies wäre ein Standardsegment für erneute Interaktion.

Wenn Sie andere, gezieltere Segmente haben, die in letzter Zeit Benachrichtigungen erhalten haben, möchten Sie vielleicht nicht, dass Ihre Nutzer:innen durch allgemeinere Kampagnen, die an dieses Segment gerichtet sind, angesprochen werden. Durch das Anhängen des Filters "Zuletzt erhaltener Push" an dieses Segment hat der Nutzer:innen sichergestellt, dass er für die nächsten 24 Stunden aus diesem Segment herausrutscht, wenn er in den letzten 24 Stunden eine andere Benachrichtigung erhalten hat. Wenn sie 24 Stunden später immer noch die anderen Kriterien des Segments erfüllen und keine weiteren Benachrichtigungen erhalten haben, rutschen sie wieder in das Segment.

![Ein Segment namens "Retargeting Filter Showcase" mit der Filter-Gruppe "Letzte Nutzung der App vor mehr als 7 Tagen".]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"} 

Wenn Sie diesen Filter an alle Segmente anhängen, auf die Ihre Kampagnen abzielen, erhalten Ihre Nutzer maximal einen Push alle 24 Stunden. Sie können dann Ihre Nachrichten nach Prioritäten ordnen und sicherstellen, dass Ihre wichtigsten Nachrichten vor den weniger wichtigen Nachrichten zugestellt werden.

#### Festlegen einer maximalen Nutzer:innen-Begrenzung

Im Schritt **Zielgruppen** Ihres Kampagnen-Editors können Sie auch die Gesamtzahl der Nutzer:innen begrenzen, die Ihre Nachricht erhalten sollen. Dies dient als Kontrolle, die unabhängig von Ihren Kampagnen-Filtern ist.

![Zusammenfassung der Zielgruppe mit einem ausgewählten Kontrollkästchen zur Begrenzung der Anzahl der Personen, die die Kampagne erhalten.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"} 

Indem Sie das maximale Nutzer:innen-Limit auswählen, können Sie das Volumen der gesendeten Nachrichten pro Kanal oder global für alle Nachrichtentypen begrenzen.

##### Maximale Benutzerkapazität mit Optimierungen

Wenn Sie eine Optimierung wie Winning Variant oder Personalized Variant verwenden, besteht die Kampagne aus zwei Sendungen: dem anfänglichen Experiment und der endgültigen Sendung. 

Um in diesem Szenario eine maximale Benutzerzahl festzulegen, markieren Sie die Option **Anzahl der Personen begrenzen, die diese Kampagne erhalten sollen**, wählen Sie dann **Insgesamt sollte diese Kampagne** und geben Sie ein Zielgruppenlimit ein. Ihre Zielgruppe wird durch die im **A/B-Test-Panel** angezeigten Prozentsätze aufgeteilt. 

Wenn Sie **Jedes Mal, wenn die Kampagne geplant wird,** auswählen, werden diese beiden Phasen separat auf die eingestellte Anzahl begrenzt. Dies ist in der Regel nicht wünschenswert.

#### Festlegen einer Obergrenze für Impressionen in Kampagnen

Für In-App-Nachrichten können Sie den Marketing-Druck kontrollieren, indem Sie eine maximale Anzahl von Impressionen festlegen, die Ihrer Nutzerbasis angezeigt werden. Danach wird Braze keine weiteren Nachrichten mehr an Ihre Nutzer:innen senden. Es ist jedoch wichtig zu beachten, dass diese Obergrenze nicht exakt ist. 

In-App-Nachricht-Regeln werden bei Sitzungsbeginn an eine App gesendet. Das bedeutet, dass Braze eine Nachricht an den Nutzer:innen senden kann, bevor die Obergrenze erreicht ist, aber zu dem Zeitpunkt, an dem der Nutzer:innen die Nachricht triggert, ist die Obergrenze bereits erreicht. In diesem Fall zeigt das Gerät weiterhin die Meldung an.

Nehmen wir zum Beispiel an, Sie haben ein Spiel mit einer In-App-Nachricht, die ausgelöst wird, wenn ein Nutzer ein Level besiegt, und Sie begrenzen diese auf 100 Impressionen. Bisher gab es 99 Eindrücke. Alice und Bob öffnen beide das Spiel und Braze teilt ihren Geräten mit, dass sie berechtigt sind, die Nachricht zu empfangen, wenn sie ein Level geschafft haben. Alice schafft zuerst ein Level und erhält die Nachricht. Bob schlägt die nächste Stufe, aber da sein Gerät seit Beginn der Sitzung nicht mit den Servern von Braze kommuniziert hat, weiß sein Gerät nicht, dass die Nachricht ihre Obergrenze erreicht hat, und er erhält die Nachricht ebenfalls. Wenn jedoch eine Obergrenze für Impressionen erreicht wurde, sendet das System bei der nächsten Anfrage eines Geräts an die Liste der in Frage kommenden In-App-Nachrichten diese Nachricht nicht und entfernt die Nachricht von diesem Gerät.

### Ratenbegrenzung und A/B-Tests

Wenn Sie die Ratenbegrenzung bei einem A/B-Test verwenden, wird die Ratenbegrenzung nicht in gleicher Weise auf die Kontrollgruppe angewandt wie auf die Testgruppe, was eine potenzielle Quelle für zeitliche Verzerrungen ist. Um diese Verzerrung zu vermeiden, verwenden Sie geeignete Konversionsfenster.

### Rate-Limiting für die Zustellungsgeschwindigkeit

Wenn Sie davon ausgehen, dass große Kampagnen zu einem Anstieg der Nutzer:innen-Aktivitäten führen und Ihre Server überlasten, können Sie ein Rate-Limit für den Versand von Nachrichten pro Minute festlegen. Das bedeutet, dass Braze innerhalb einer Minute nicht mehr als die von Ihnen festgelegte Rate-Limits sendet.

Wenn Sie während der Kampagnenerstellung Benutzer ansprechen, können Sie unter **Zielgruppen** (für Kampagnen) oder **Sendeeinstellungen** (für Canvas) ein Ratenlimit auswählen (in verschiedenen Abstufungen von 10 bis 500.000 Nachrichten pro Minute).

Beachten Sie, dass Kampagnen ohne Rate-Limits diese Zustellungslimits überschreiten können. Beachten Sie jedoch, dass Nachrichten abgebrochen werden, wenn sie aufgrund eines niedrigen Rate-Limits 72 Stunden oder länger auf sich warten lassen. Wenn das Ratenlimit zu niedrig ist, erhält der Ersteller der Kampagne Warnungen im Dashboard und per E-Mail.

#### Beispiel

Wenn Sie versuchen, 75.000 Nachrichten mit einem Rate-Limit von 10.000 pro Minute zu versenden, wird die Zustellung auf acht Minuten verteilt. Ihre Kampagne wird nicht mehr als 10.000 Nachrichten in den ersten sieben Minuten und 5.000 in der letzten Minute zugestellt.

#### Anzahl der Sendungen

Beachten Sie, dass Nachrichten mit Ratenbeschränkung möglicherweise nicht gleichmäßig über jede Minute gesendet werden. Am Beispiel eines Rate-Limits von 10.000 pro Minute bedeutet dies, dass Braze sicherstellt, dass nicht mehr als 10.000 Nachrichten pro Minute gesendet werden. Das könnte bedeuten, dass ein höherer Prozentsatz der 10.000 Nachrichten innerhalb der ersten halben Minute gesendet wird als in der letzten halben Minute.

Das Rate-Limit wird zu Beginn des Sendeversuchs einer Nachricht angewendet. Bei Schwankungen in der Sendezeit kann die Anzahl der abgeschlossenen Sendungen das Rate-Limit für einige Minuten leicht überschreiten. Mit der Zeit wird die Anzahl der Sendungen pro Minute im Durchschnitt nicht mehr als das Rate-Limit betragen.

{% alert important %}
Seien Sie vorsichtig, wenn Sie zeitkritische Nachrichten mit dieser Form des Rate-Limiting in Bezug auf die Gesamtzahl der Nutzer:innen in einem Segment verzögern. Wenn das Segment beispielsweise 30 Millionen Nutzer:innen umfasst, wir aber das Rate-Limits auf 10.000 pro Minute festlegen, wird ein großer Teil Ihrer Nutzer:innen die Nachricht erst am nächsten Tag erhalten.
{% endalert %}

#### Kampagnen und Canvase mit mehreren Kanälen

Wenn Sie ein Rate-Limit für die Zustellung für eine Multichannel-Kampagne oder Canvas festlegen, können Sie entweder ein gemeinsames Rate-Limit oder ein kanalbasiertes Limit festlegen.

Wenn eine Multichannel-Kampagne oder ein Canvas ein gemeinsames Rate-Limit verwendet, bedeutet dies, dass die Gesamtzahl der Nachrichten, die pro Minute von der Kampagne oder dem Canvas gesendet werden, das Rate-Limit nicht überschreitet. Wenn Ihr Canvas beispielsweise ein Rate-Limit von 500.000 pro Minute hat und E-Mail- und SMS-Nachrichten-Schritte enthält, sendet Braze insgesamt 500.000 Nachrichten pro Minute über E-Mail und SMS.

![Die Option, die Rate zu begrenzen, mit der die Kampagne sendet, ausgewählt mit 500.000 Nachrichten pro Minute.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"} 

Wenn eine Multichannel-Kampagne oder Canvas ein kanalbasiertes Rate-Limiting verwendet, gilt das Rate-Limits für jeden von Ihnen ausgewählten Kanal. Sie können Ihre Kampagne oder Ihr Canvas beispielsweise so einstellen, dass Sie maximal 5.000 Webhooks und 2.500 SMS-Nachrichten pro Minute über die Kampagne oder das Canvas versenden.

![Getrennte Rate-Limits für zwei Kanäle, Webhook und SMS/MMS/RCS, mit 5.000 bzw. 2.500 Nachrichten pro Minute.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Push-Benachrichtigungen

Für Kampagnen oder Canvase mit Push-Plattformen (wie Android, iOS, Web-Push oder Kindle) können Sie **Push-Benachrichtigungen** auswählen, um ein Rate-Limit zu erzwingen, das von allen Push-Plattformen in Ihrer Kampagne oder Ihrem Canvas gemeinsam genutzt wird.

![Das Kanal-Dropdown mit Optionen für Push-Plattformen und Push-Benachrichtigungen.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"} 

{% alert note %}
Wenn Sie ein Limit für Push-Benachrichtigungen auswählen, können Sie keine individuellen Rate-Limits für Push-Kanäle festlegen. Wenn Sie Grenzen für einzelne Push-Kanäle auswählen, können Sie auch keine gemeinsamen Grenzen für Push-Benachrichtigungen festlegen.
{% endalert %}

{% alert important %}
**Updates für Rate-Limiting Schnittstelle**<br>
Braze hat die Schnittstelle für Rate-Limiting aktualisiert, um mehr Transparenz und Kontrolle darüber zu bieten, wie Rate-Limits für Multichannel-Kampagnen und Canvase gelten.<br><br>

- **Bestehende Kampagnen und Canvase:** Alle bestehenden Kampagnen und Canvase sind auf diese Schnittstelle migriert worden. Ihr Zustellungsverhalten bleibt unverändert. Das Dashboard zeigt an, ob die Kampagne eine gemeinsame oder eine kanalbezogene Logik verwendet.<br>
- **Neue Kampagnen und Canvase:** Für alle neuen Kampagnen und Canvase gibt es einen manuellen Umschalter, mit dem Sie Ihre bevorzugte Rate-Limits-Logik auswählen können. Achten Sie darauf, das Rate-Limiting-Verhalten auszuwählen, das Ihrem beabsichtigten Verhalten entspricht, wenn Sie ein Rate-Limit für eine Kampagne oder ein Canvas festlegen oder aktualisieren.
{% endalert %}

##### Rate-Limiting Überlegungen

Einige Hinweise, die Sie bei der Konfiguration von Rate-Limits beachten sollten und welches Verhalten Sie erwarten sollten:

- Für den Versand von SMS gilt ein Rate-Limit von 50.000 pro Abo-Gruppe. Einige SMS-Anbieter setzen möglicherweise andere Grenzen fest.
- Die folgenden Nachrichten werden nicht durch das Rate-Limit gedrosselt oder auf dieses angerechnet:
    - Test sendet
    - Seed-Gruppen
    - Content-Cards, die so konfiguriert sind, dass sie "beim ersten Eindruck" erstellt werden (Dies wird durch die Rate der Impressionen der App gesteuert. Weitere Informationen zu den Unterschieden zwischen den Kartenerstellungsoptionen finden Sie unter [Kartenerstellung]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences) ).
- Geschwindigkeitsbegrenzungen für die Zustellung werden für die folgenden Fälle nicht unterstützt:
    - Automatische SMS-Antworten
    - SLA-gestützte Nachrichten (wie [Transaktions-E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign))
    - In-App-Nachrichten
    - Feature-Flags
    - Banner

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

Connected-Content-Anfragen sind nicht unabhängig von der Rate-Limitierung und folgen dem Rate-Limit des Webhooks. Das bedeutet, dass Sie bei einem Connected-Content-Aufruf an einen eindeutigen Endpunkt pro Webhook mit 5.000 Webhooks und auch 5.000 Connected-Content-Aufrufen pro Minute rechnen müssen. Beachten Sie, dass die Zwischenspeicherung dies beeinflussen und die Anzahl der Connected-Content-Aufrufe reduzieren kann. Außerdem können Wiederholungsversuche die Connected-Content-Aufrufe erhöhen. Wir empfehlen daher zu überprüfen, ob der Connected-Content-Endpunkt hier mit einer gewissen Fluktuation umgehen kann.

## Über Frequency-Capping

Wenn Ihre Nutzerbasis weiter wächst und Ihre Nachrichten auf Lebenszyklus-, Trigger-, Transaktions- und Konversionskampagnen ausgeweitet werden, ist es wichtig, dass Ihre Benachrichtigungen nicht als „Spam“ oder störend empfunden werden. Durch eine bessere Kontrolle über die Erfahrung Ihrer Nutzer ermöglicht Ihnen die Frequenzbegrenzung die Erstellung der gewünschten Kampagnen, ohne Ihr Publikum zu überfordern.

### Übersicht über die Features {#freq-cap-feat-over}

Die Frequenzbegrenzung wird auf der Ebene der Kampagne oder der Canvas-Komponente angewendet und kann für jeden Arbeitsbereich unter **Einstellungen** > **Frequenzbegrenzungsregeln** eingerichtet werden.

Standardmäßig ist das Frequency-Capping aktiviert, wenn neue Kampagnen erstellt werden. Von hier aus können Sie Folgendes auswählen:

- Der Messaging-Kanal, den Sie kappen möchten: Push, E-Mail, SMS, Webhook, WhatsApp, LINE oder einer dieser Kanäle.
- Wie oft jeder Nutzer:innen innerhalb eines bestimmten Zeitrahmens eine Kampagne oder eine Canvas-Komponente von einem Kanal erhalten soll.
- Wie oft jeder Nutzer:innen innerhalb eines bestimmten Zeitrahmens eine Kampagne oder eine Canvas-Komponente erhalten soll, die von einem [Tag](#frequency-capping-by-tag) gesendet wurde.

Dieser Zeitrahmen kann in Minuten, Tagen oder Wochen (sieben Tage) gemessen werden, wobei die maximale Dauer 30 Tage beträgt.

Jede Zeile von Frequency-Caps wird mit dem Operator `AND` verbunden, und Sie können bis zu 10 Regeln pro Workspace hinzufügen. Sie können mehrere Obergrenzen für dieselben Nachrichtenarten angeben. So können Sie beispielsweise die Anzahl der Nutzer auf einen Push pro Tag und drei Pushs pro Woche begrenzen. Beachten Sie, dass abgebrochene Nachrichten nicht zum Frequency-Capping zählen.

![Abschnitt Frequency-Capping mit Listen von Kampagnen und Canvase, für die die Regeln gelten und nicht gelten.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"} 

#### Verhalten bei Frequency-Capping von Nutzer:innen in einem Canvas-Schritt

Wenn ein Canvas-Nutzer:innen aufgrund globaler Einstellungen für Frequency-Capping ein Frequency-Capping hat, wird der Nutzer:innen sofort zum nächsten Canvas-Schritt vorgebracht. Der Nutzer:innen wird den Canvas wegen des Frequency-Cappings nicht verlassen.

### Regeln für die Zustellung

Es gibt vielleicht Kampagnen, wie z.B. Transaktionsnachrichten, die den Nutzer immer erreichen sollen, auch wenn er seine Frequenzgrenze bereits erreicht hat. Eine App für die Zustellung kann zum Beispiel eine E-Mail oder einen Push senden, wenn ein Artikel zugestellt wird, unabhängig davon, wie viele Kampagnen der Nutzer:innen erhalten hat.

Wenn Sie möchten, dass eine bestimmte Kampagne die Regeln für die Frequenzbegrenzung außer Kraft setzt, können Sie dies im Braze-Dashboard bei der Planung der Zustellung dieser Kampagne einrichten, indem Sie die **Frequenzbegrenzung** auf **AUS** setzen. 

Danach werden Sie gefragt, ob Sie diese Kampagne immer noch auf Ihre Frequenzobergrenze anrechnen lassen möchten. Nachrichten, die zum Frequency-Capping zählen, werden in die Berechnungen für den Filter „Intelligenter Kanal“ einbezogen. 

Beim Versenden von [API-Kampagnen]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), die oft transaktionsbezogen sind, können Sie angeben, dass eine Kampagne die Frequency-Capping-Regeln ignorieren soll, indem Sie in der API-Anfrage `override_frequency_capping` auf `true` setzen.

Neue Kampagnen und Canvases, die sich nicht an die Häufigkeitsobergrenzen halten, werden standardmäßig auch nicht auf diese angerechnet. Dies ist für jede Kampagne und jeden Canvas konfigurierbar.

{% alert note %}
Dieses Verhalten ändert das Standardverhalten, wenn Sie das Frequency-Capping für eine Kampagne oder ein Canvas deaktivieren. Die Änderungen sind abwärtskompatibel und wirken sich nicht auf Nachrichten aus, die derzeit live geschaltet sind.
{% endalert %}

![Abschnitt Zustellungssteuerung mit eingeschaltetem Frequency-Capping.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"} 

Verschiedene Kanäle innerhalb einer Multichannel-Kampagne zählen individuell für die Frequenzobergrenze. Wenn Sie zum Beispiel eine Multichannel-Kampagne mit Push und E-Mail erstellen und für beide Kanäle ein Frequency-Capping eingerichtet haben, dann zählt der Push zu einer Push-Kampagne und die E-Mail-Nachricht zu einer Messaging-Kampagne. Die Kampagne zählt auch für eine "Kampagne jeglicher Art". Wenn Nutzer:innen auf eine Push- und eine E-Mail-Kampagne pro Tag beschränkt sind und diese Multichannel-Kampagne erhalten, sind sie für den Rest des Tages nicht mehr für Push- oder E-Mail-Kampagnen zugelassen (es sei denn, eine Kampagne ignoriert die Frequency-Capping-Regeln).

In-App-Nachrichten und Content-Cards werden nicht als Obergrenzen für Kampagnen oder Canvas-Komponenten jeglicher Art gezählt oder auf diese angerechnet.

{% alert important %}
Die globale Frequenzbegrenzung basiert auf der Zeitzone des Benutzers und wird nach Kalendertagen und nicht nach 24-Stunden-Perioden berechnet. Wenn Sie zum Beispiel eine Frequency-Capping-Regel einrichten, die vorsieht, dass nicht mehr als eine Kampagne pro Tag versendet wird, kann ein Nutzer:innen um 23 Uhr in seiner Ortszeit eine Nachricht erhalten und eine Stunde später eine weitere Nachricht bekommen.
{% endalert %}

#### Anwendungsfälle

{% tabs %}
{% tab Use case 1 %}

Nehmen wir an, Sie legen eine Frequency-Capping-Regel fest, so dass Ihre Nutzer:innen von allen Kampagnen oder Canvas-Schritten nicht mehr als drei Push-Benachrichtigungen pro Woche erhalten.

Wenn Ihr Nutzer in dieser Woche drei Push-Benachrichtigungen, zwei In-App-Nachrichten und eine Content Card erhalten soll, wird er alle diese Nachrichten erhalten.

{% endtab %}
{% tab Use case 2 %}

Dieses Szenario verwendet eine Frequency-Capping-Regel für Nutzer:innen, die nicht mehr als zwei Push-Benachrichtigungen pro Woche von allen Kampagnen oder Canvas-Schritten erhalten.

**Wenn das folgende Szenario eintritt:**

- Ein Nutzer:in triggert dieselbe Kampagne `Campaign ABC` dreimal im Laufe einer Woche.
- Dieser Nutzer:innen triggert `Campaign ABC` einmal am Montag, einmal am Mittwoch und einmal am Donnerstag.

![Abschnitt Frequency-Capping mit der Regel, nicht mehr als 2 Push-Benachrichtigungen aus allen Kampagnen/Canvas-Schritten an einen Nutzer:innen alle 1 Woche zu senden.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Dann lautet das erwartete Verhalten wie folgt:**

- Dieser Benutzer wird die Kampagnensendungen erhalten, die am Montag und Mittwoch ausgelöst wurden.
- Dieser Benutzer wird die dritte Kampagnensendung am Donnerstag nicht erhalten, da er in dieser Woche bereits zwei Push-Kampagnensendungen erhalten hat.

{% endtab %}
{% endtabs %}

### Frequency-Capping nach Tag

[Regeln für die Frequenzbegrenzung](#delivery-rules) können auf Arbeitsbereiche angewendet werden, indem Sie bestimmte Tags verwenden, die Sie auf Ihre Kampagnen und Canvases angewendet haben, so dass Sie Ihre Frequenzbegrenzung im Wesentlichen auf benutzerdefinierte Gruppen stützen können.

Mit der Frequenzkappung nach Tag können Regeln für die Haupt- und verschachtelten Tags festgelegt werden, so dass Braze alle Tags berücksichtigt. Wenn Sie z.B. das Haupt-Tag A als Frequency-Cap ausgewählt haben, werden bei der Bestimmung des Limits auch die Informationen in allen verschachtelten Tags (z.B. Tags B und C) berücksichtigt.

Sie können auch die reguläre Frequenzkappung mit der Frequenzkappung durch Tags kombinieren. Beachten Sie die folgenden Regeln:

1. Nicht mehr als drei Push-Benachrichtigungs-Kampagnen oder Canvas-Komponenten pro Woche aus allen Kampagnen und Canvas-Schritten. <br>**UND**
2. Nicht mehr als zwei Push-Benachrichtigungs-Kampagnen oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Frequency-Capping mit zwei Regeln, die festlegen, wie viele Kampagnen/Canvase mit Push-Benachrichtigungen pro Woche an einen Nutzer:innen gesendet werden können.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Infolgedessen erhalten Ihre Benutzer nicht mehr als drei Kampagnensendungen pro Woche über alle Kampagnen und Canvas-Schritte und nicht mehr als zwei Push-Benachrichtigungskampagnen oder Canvas-Komponenten mit dem Tag `promotional`.

{% alert important %}
Leinwände werden auf der Ebene der Leinwand getaggt, im Gegensatz zum Tagging nach Komponente. Jede Canvas-Komponente erbt also alle Tags der Canvas-Ebene.
{% endalert %}

#### Widersprüchliche Regeln

Wenn sich Regeln widersprechen, wird die restriktivste, anwendbare Frequency-Capping-Regel auf Ihre Nutzer:innen angewendet. Nehmen wir zum Beispiel an, Sie haben die folgenden Regeln:

1. Nicht mehr als eine Push-Benachrichtigungs-Kampagne oder Canvas-Komponente pro Woche von allen Kampagnen und Canvas-Komponenten. <br>**UND**
2. Nicht mehr als drei Push-Benachrichtigungskampagnen oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Abschnitt Frequency-Capping mit widersprüchlichen Regeln, um zu begrenzen, wie viele Push-Benachrichtigungen Kampagnen/Canvas-Schritte pro 1 Woche an einen Nutzer:innen gesendet werden.]({% image_buster /assets/img/global_rules.png %} "global rules")

In diesem Beispiel wird Ihr Benutzer in einer bestimmten Woche nicht mehr als eine Push-Benachrichtigungskampagne oder Canvas-Komponente mit dem Tag "Werbeaktion" erhalten, da Sie festgelegt haben, dass Benutzer nicht mehr als eine Push-Benachrichtigungskampagne oder Canvas-Komponente von allen Kampagnen und Canvas-Komponenten erhalten sollen. Mit anderen Worten, die restriktivste anwendbare Frequenzregel ist die Regel, die auf einen bestimmten Benutzer angewendet wird.

#### Anzahl der Tags

Frequency-Capping durch Tag-Regeln wird zum Zeitpunkt des Versendens einer Nachricht berechnet. Das bedeutet, dass die Häufigkeitsbegrenzung nach Tags nur die Tags zählt, die sich derzeit in den Kampagnen oder Canvases befinden, die ein Benutzer in der Vergangenheit erhalten hat. Nicht mitgezählt werden die Tags, die sich zum Zeitpunkt der Versendung auf den Kampagnen oder Canvase befanden, aber inzwischen entfernt wurden. Es zählt, wenn ein Tag später zu einer Nachricht hinzugefügt wird, die ein Nutzer:innen in der Vergangenheit erhalten hat, aber bevor die neueste getaggte Nachricht gesendet wurde.

##### Anwendungsfall

Betrachten Sie die folgenden Kampagnen und die Begrenzung der Häufigkeit nach Tag-Regeln:

**Kampagnen**:

- **Kampagne A** ist eine Push-Kampagne mit dem Tag `promotional`. Sie soll am Montag um 9 Uhr verschickt werden.
- **Kampagne B** ist eine Push-Kampagne mit der Bezeichnung `promotional`. Sie soll am Mittwoch um 9 Uhr verschickt werden.

**Frequency-Capping nach Tag-Regel:**

- Ihr Benutzer sollte nicht mehr als eine Push-Benachrichtigungskampagne pro Woche mit dem Tag `promotional` erhalten.<br><br>

| Aktion | Ergebnis |
|---|---|
| Der Tag `promotional` wird aus **Kampagne A** entfernt, nachdem Ihr Nutzer:innen die Nachricht erhalten hat, aber bevor **Kampagne B gesendet wurde.** | Ihr Nutzer:innen erhält **Kampagne B**.|
| Das Tag `promotional` wurde versehentlich aus **Kampagne A** entfernt, nachdem Ihr Benutzer die Nachricht erhalten hat. <br> Der Tag wird am Dienstag wieder zu **Kampagne A** hinzugefügt, bevor **Kampagne B** versendet wird. | Ihr Nutzer:in erhält keine **Kampagne B**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Versenden in großem Maßstab {#sending-at-large-scales}

„Frequency-Capping nach Tag-Regeln“ wird bei großen Skalen, wie z. B. 100 Nachrichten pro Kanal aus Kampagnen oder Canvas-Komponenten, möglicherweise nicht richtig angewendet.

Wenn Ihre Regel für die Frequenzbegrenzung nach Tag zum Beispiel lautet:

> Nicht mehr als zwei E-Mail-Kampagnen oder Canvas-Komponenten mit dem Tag `Promotional` für einen Benutzer pro Woche.

Und wenn Sie dem Benutzer im Laufe einer Woche mehr als 100 E-Mails aus Kampagnen und Canvas-Schritten mit eingeschalteter Häufigkeitsbegrenzung senden, werden möglicherweise mehr als zwei E-Mails an den Benutzer gesendet.

Da 100 Nachrichten pro Kanal mehr Nachrichten sind, als die meisten Marken an ihre Nutzer:innen senden, ist es unwahrscheinlich, dass sich diese Einschränkung auswirkt. Um diese Einschränkung zu vermeiden, können Sie eine Obergrenze für die maximale Anzahl von E-Mails festlegen, die Ihre Benutzer im Laufe einer Woche erhalten sollen.

Sie könnten zum Beispiel die folgende Regel aufstellen:

> Nicht mehr als drei E-Mail-Kampagnen oder Canvas-Komponenten pro Woche aus allen Kampagnen und Canvas-Schritten.

Diese Regel legt fest, dass keine Nutzer:innen mehr als 100 E-Mails pro Woche erhalten, da sie höchstens drei E-Mails pro Woche von Kampagnen oder Canvas-Komponenten mit aktiviertem Frequency-Capping erhalten.

