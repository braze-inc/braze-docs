---
nav_title: Rate-Limiting und Frequency-Capping
article_title: Rate-Limiting und Frequency-Capping
page_order: 6
tool: Campaigns
page_type: reference
description: "In diesem Referenzartikel wird das Konzept der Ratenbegrenzung und der Frequenzbegrenzung in Kampagnen erörtert und wie Sie den Marketingdruck steuern können, um die Nutzererfahrung zu verbessern."

---

# Rate-Limiting und Frequency-Capping

> Rate-Limiting und Frequency-Capping können kombiniert eingesetzt werden, um sicherzustellen, dass Ihre Nutzer:innen die gewünschten Nachrichten erhalten.

## Über Rate-Limiting

Braze ermöglicht es Ihnen, den Druck im Marketing zu kontrollieren, indem Sie Ihre Kampagnen mit Rate-Limiting versehen und so die Menge des von Ihrer Plattform ausgehenden Datenverkehrs regulieren. Sie können zwei verschiedene Arten der Preisbegrenzung für Ihre Kampagnen einsetzen: 

1. [Benutzerorientierte Rate-Limiting-Strategie:](#user-centric-rate-limiting) Konzentriert sich darauf, den Nutzer:innen das beste Erlebnis zu bieten.
2. [Rate-Limiting für die Zustellung:](#delivery-speed-rate-limiting) Berücksichtigt die Bandbreite Ihrer Server.

Braze wird versuchen, die gesendeten Nachrichten gleichmäßig über die Minute zu verteilen, kann dies aber nicht garantieren. Wenn Sie beispielsweise eine Kampagne mit einem Rate-Limit von 5.000 Nachrichten pro Minute haben, versuchen wir, die 5.000 Anfragen gleichmäßig über die Minute zu verteilen (etwa 84 Nachrichten pro Sekunde), aber die Rate pro Sekunde kann variieren.

### Benutzerzentrierte Ratenbegrenzung

Wenn Sie mehr Segmente erstellen, wird es Fälle geben, in denen sich die Mitgliedschaft in diesen Segmenten überschneidet. Wenn Sie Kampagnen an diese Segmente versenden, sollten Sie darauf achten, dass Sie Ihre Nutzer nicht zu oft anschreiben. Wenn ein Benutzer zu viele Nachrichten innerhalb eines kurzen Zeitraums erhält, wird er sich überfordert fühlen und entweder die Push-Benachrichtigungen deaktivieren oder Ihre App deinstallieren.

#### Relevante Segmentfilter

Braze stellt die folgenden Filter zur Verfügung, mit denen Sie die Häufigkeit, mit der Ihre Nutzer:innen Nachrichten erhalten, einschränken können:

- Letzte Interaktion mit Nachricht
- Empfangszeitpunkt der letzten Nachricht
- Letzter empfangener Push
- Letzte empfangene E-Mail
- Letzte empfangene SMS

#### Implementieren von Filtern

Nehmen wir an, wir haben ein Segment mit dem Namen „Retargeting-Filter-Showcase” erstellt, das den Filter „Letzte Nutzung der App vor mehr als 7 Tagen” verwendet, um eine Zielgruppe zusammenzustellen. Dies wäre ein Standardsegment für erneute Interaktion.

Wenn Sie über andere, zielgerichtetere Segmente verfügen, die kürzlich Benachrichtigungen erhalten haben, möchten Sie möglicherweise nicht, dass Ihre Nutzer:innen von allgemeineren Kampagnen angesprochen werden, die sich an dieses Segment richten. Durch Hinzufügen des Filters „Zuletzt empfangene Push-Benachrichtigung“ zu diesem Segment hat die Nutzer:in sichergestellt, dass Personen, die in den letzten 24 Stunden eine weitere Benachrichtigung erhalten haben, für die nächsten 24 Stunden aus diesem Segment entfernt werden. Wenn sie 24 Stunden später weiterhin die anderen Kriterien des Segments erfüllen und keine weiteren Benachrichtigungen erhalten haben, werden sie wieder in das Segment zurückgestuft.

![Ein Segment mit dem Namen „Retargeting-Filter-Showcase“ und der Filtergruppe „Zuletzt vor mehr als 7 Tagen verwendete App“.]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"} 

Wenn Sie diesen Filter an alle Segmente anhängen, auf die Ihre Kampagnen abzielen, erhalten Ihre Nutzer maximal einen Push alle 24 Stunden. Sie können dann Ihre Nachrichten nach Prioritäten ordnen und sicherstellen, dass Ihre wichtigsten Nachrichten vor den weniger wichtigen Nachrichten zugestellt werden.

#### Festlegen einer maximalen Nutzer:innen-Begrenzung

Im Schritt **Zielgruppen** Ihres Kampagnen-Editors können Sie auch die Gesamtzahl der Nutzer:innen begrenzen, die Ihre Nachricht erhalten sollen. Dies dient als Überprüfung, die unabhängig von Ihren Kampagnenfiltern ist.

![Zielgruppenübersicht mit einem ausgewählten Kontrollkästchen zur Begrenzung der Anzahl der Personen, die die Kampagne erhalten.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"} 

Durch die Auswahl der maximalen Grenze für Nutzer:innen können Sie das Volumen der gesendeten Nachrichten pro Kanal oder global für alle Nachrichtentypen begrenzen.

{% alert note %}
Die maximale Anzahl an Nutzern begrenzt die Anzahl der versendeten Nutzer, nicht die Anzahl der erfolgreich gesendeten Nachrichten. Da abgebrochene Nachrichten auf dieses Limit angerechnet werden, kann die tatsächliche Anzahl der gesendeten Nachrichten geringer sein als das konfigurierte Limit. Wenn Sie beispielsweise eine Obergrenze von 10.000 festlegen und 2.000 Nachrichten aufgrund von Liquid-Logik oder anderen Bedingungen abgebrochen werden, werden nur 8.000 Nachrichten versendet.
{% endalert %}

##### Maximale Benutzerkapazität mit Optimierungen

Wenn Sie eine Optimierung wie Winning Variant oder Personalized Variant verwenden, besteht die Kampagne aus zwei Sendungen: dem anfänglichen Experiment und der endgültigen Sendung. 

Um in diesem Szenario eine maximale Benutzerzahl festzulegen, markieren Sie die Option **Anzahl der Personen begrenzen, die diese Kampagne erhalten sollen**, wählen Sie dann **Insgesamt sollte diese Kampagne** und geben Sie ein Zielgruppenlimit ein. Ihre Zielgruppe wird durch die im **A/B-Test-Panel** angezeigten Prozentsätze aufgeteilt. 

Wenn Sie **Jedes Mal, wenn die Kampagne geplant wird,** auswählen, werden diese beiden Phasen separat auf die eingestellte Anzahl begrenzt. Dies ist in der Regel nicht wünschenswert.

#### Festlegen einer maximalen Obergrenze für Impressionen für Kampagnen

Bei In-App-Nachrichten können Sie den Marketingdruck kontrollieren, indem Sie eine maximale Anzahl von Impressionen festlegen, die Ihrer Nutzerbasis angezeigt werden. Nach Erreichen dieser Anzahl sendet Braze keine weiteren Nachrichten an Ihre Nutzer:innen. Es ist jedoch wichtig zu beachten, dass diese Obergrenze nicht exakt ist. 

In-App-Nachrichtenregeln werden zu Beginn der Sitzung an eine App gesendet, was bedeutet, dass Braze eine Nachricht an den Nutzer:in senden kann, bevor das Limit erreicht ist. Wenn der Nutzer:in jedoch die Nachricht triggert, ist das Limit bereits erreicht. In diesem Fall zeigt das Gerät weiterhin die Meldung an.

Nehmen wir zum Beispiel an, Sie haben ein Spiel mit einer In-App-Nachricht, die ausgelöst wird, wenn ein Nutzer ein Level besiegt, und Sie begrenzen diese auf 100 Impressionen. Bisher gab es 99 Eindrücke. Alice und Bob starten beide das Spiel, und Braze teilt ihren Geräten mit, dass sie berechtigt sind, die Nachricht zu empfangen, wenn sie einen Level geschafft haben. Alice schafft zuerst ein Level und erhält die Nachricht. Bob besteht das nächste Level, aber da sein Gerät seit Beginn seiner Sitzung nicht mit den Braze-Servern kommuniziert hat, ist seinem Gerät nicht bekannt, dass die Nachricht ihr Limit erreicht hat, und er erhält die Nachricht ebenfalls. Wenn jedoch eine Impression-Obergrenze erreicht wurde, sendet das System bei der nächsten Anfrage eines Geräts nach der Liste der zulässigen In-App-Nachrichten diese Nachricht nicht und entfernt sie von diesem Gerät.

### Ratenbegrenzung und A/B-Tests

Wenn Sie die Ratenbegrenzung bei einem A/B-Test verwenden, wird die Ratenbegrenzung nicht in gleicher Weise auf die Kontrollgruppe angewandt wie auf die Testgruppe, was eine potenzielle Quelle für zeitliche Verzerrungen ist. Um diese Verzerrung zu vermeiden, verwenden Sie geeignete Konversionsfenster.

### Rate-Limiting für die Zustellungsgeschwindigkeit

Sollten Sie umfangreiche Kampagnen planen, die zu einem Anstieg der Nutzeraktivität und einer Überlastung Ihrer Server führen könnten, haben Sie die Möglichkeit, ein Minuten-Rate-Limit für den Versand von Nachrichten festzulegen. Dies bedeutet, dass Braze innerhalb einer Minute nicht mehr als die von Ihnen festgelegte Anzahl an Nachrichten versendet.

Wenn Sie während der Kampagnenerstellung Benutzer ansprechen, können Sie unter **Zielgruppen** (für Kampagnen) oder **Sendeeinstellungen** (für Canvas) ein Ratenlimit auswählen (in verschiedenen Abstufungen von 10 bis 500.000 Nachrichten pro Minute).

Beachten Sie, dass Kampagnen ohne Rate-Limits diese Zustellungslimits überschreiten können. Beachten Sie jedoch, dass Nachrichten abgebrochen werden, wenn sie aufgrund eines niedrigen Rate-Limits 72 Stunden oder länger auf sich warten lassen. Wenn das Ratenlimit zu niedrig ist, erhält der Ersteller der Kampagne Warnungen im Dashboard und per E-Mail.

#### Beispiel

Wenn Sie versuchen, 75.000 Nachrichten mit Rate-Limits von 10.000 Nachrichten pro Minute zu versenden, wird die Zustellung über acht Minuten verteilt. Ihre Kampagne wird nicht mehr als 10.000 Nachrichten in den ersten sieben Minuten und 5.000 in der letzten Minute zugestellt.

#### Anzahl der Sendungen

Beachten Sie, dass Nachrichten mit Ratenbeschränkung möglicherweise nicht gleichmäßig über jede Minute gesendet werden. Am Beispiel eines Rate-Limits von 10.000 pro Minute bedeutet dies, dass Braze sicherstellt, dass nicht mehr als 10.000 Nachrichten pro Minute gesendet werden. Das könnte bedeuten, dass ein höherer Prozentsatz der 10.000 Nachrichten innerhalb der ersten halben Minute gesendet wird als in der letzten halben Minute.

Die Rate-Limits werden zu Beginn des Versuchs, die Nachricht zu senden, angewendet. Wenn es zu Schwankungen bei der Dauer des Sendevorgangs kommt, kann die Anzahl der abgeschlossenen Sendungen für einige Minuten geringfügig über den Rate-Limits liegen. Mit der Zeit wird die Anzahl der Sendungen pro Minute im Durchschnitt nicht mehr als das Rate-Limit betragen.

{% alert important %}
Seien Sie vorsichtig, wenn Sie zeitkritische Nachrichten mit dieser Form des Rate-Limiting in Bezug auf die Gesamtzahl der Nutzer:innen in einem Segment verzögern. Wenn das Segment beispielsweise 30 Millionen Nutzer:innen umfasst, wir aber das Rate-Limits auf 10.000 pro Minute festlegen, wird ein großer Teil Ihrer Nutzer:innen die Nachricht erst am nächsten Tag erhalten.
{% endalert %}

#### Multichannel-Kampagnen und Canvases

Bei der Festlegung von Rate-Limits für die Zustellung bei einer Multichannel-Kampagne oder Canvas können Sie zwischen gemeinsamen Rate-Limits und kanalbasierten Rate-Limits wählen.

Wenn eine Multichannel-Kampagne oder Canvas ein gemeinsames Rate-Limit verwendet, bedeutet dies, dass die Gesamtzahl der pro Minute von der Kampagne oder Canvas gesendeten Nachrichten das Rate-Limit nicht überschreitet. Wenn Ihr Braze-Canvas beispielsweise Rate-Limits von 500.000 pro Minute aufweist und E-Mail- und SMS-Nachrichten-Schritte enthält, versendet Braze insgesamt 500.000 Nachrichten pro Minute per E-Mail und SMS.

![Die Option zur Begrenzung der Versandrate der Kampagne wurde mit 500.000 Nachrichten pro Minute ausgewählt.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"} 

Wenn eine Multichannel-Kampagne oder Canvas ein kanalbasiertes Rate-Limiting verwendet, gelten die Rate-Limits für jeden der von Ihnen ausgewählten Kanäle. Sie können beispielsweise Ihre Kampagne oder Canvas so einstellen, dass maximal 5.000 Webhooks und 2.500 SMS-Nachrichten pro Minute über die gesamte Kampagne oder Canvas versendet werden.

![Getrennte Rate-Limits für zwei Kanäle, Webhook und SMS/MMS/RCS, mit 5.000 bzw. 2.500 Nachrichten pro Minute.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Push-Benachrichtigungen

Für Kampagnen oder Canvases mit Push-Plattformen (wie Android, iOS, Web-Push oder Kindle) können Sie **Push-Benachrichtigungen** auswählen, um Rate-Limits durchzusetzen, die für alle Push-Plattformen in Ihrer Kampagne oder Ihrem Canvas gelten.

![Das Kanal-Dropdown-Menü mit Optionen für Push-Plattformen und Push-Benachrichtigungen.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"} 

{% alert note %}
Wenn Sie ein Limit für Push-Benachrichtigungen auswählen, können Sie keine individuellen Rate-Limits für Push-Kanäle festlegen. Wenn Sie Beschränkungen für einzelne Push-Kanäle auswählen, können Sie keine gemeinsamen Beschränkungen für Push-Benachrichtigungen festlegen.
{% endalert %}

{% alert important %}
**Updates der Schnittstelle zum Rate-Limiting**<br>
Braze hat die Schnittstelle zum Rate-Limiting aktualisiert, um mehr Transparenz und Kontrolle darüber zu bieten, wie Rate-Limits auf Multichannel-Kampagnen und Canvases angewendet werden.<br><br>

- **Bestehende Kampagnen und Canvases:** Alle bestehenden Kampagnen und Canvases wurden auf diese Schnittstelle migriert. Ihre Zustellung bleibt unverändert. Das Dashboard zeigt an, ob die Kampagne eine gemeinsame oder eine kanalbezogene Logik verwendet.<br>
- **Neue Kampagnen und Canvases:** Für alle neuen Kampagnen und Canvases steht eine manuelle Umschaltfunktion zur Verfügung, mit der Sie Ihre bevorzugte Logik für Rate-Limits auswählen können. Bitte stellen Sie sicher, dass Sie bei der Einrichtung oder dem Update einer Kampagne oder eines Canvas-Rate-Limits das Rate-Limiting-Verhalten auswählen, das Ihrem beabsichtigten Verhalten entspricht.
{% endalert %}

##### Überlegungen zum Rate-Limiting

Einige Hinweise, die Sie bei der Konfiguration von Rate-Limits beachten sollten, und welches Verhalten Sie erwarten können:

- Der Versand von SMS unterliegt Rate-Limits von 50.000 pro Abo-Gruppe. Einige SMS-Anbieter können andere Beschränkungen auferlegen.
- Die folgenden Nachrichten werden nicht gedrosselt oder auf die Rate-Limits angerechnet:
    - Test sendet
    - Seed-Gruppen
    - Content-Cards, die so konfiguriert sind, dass sie einen „ersten Eindruck“ erzeugen (dies wird durch die Häufigkeit der App-Impressionen gesteuert). Refernzieren Sie die Informationen zu den Unterschieden zwischen den Optionen zur Kartenerstellung unter [Kartenerstellung]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences).
- Für die folgenden Fälle werden keine Rate-Limits für die Zustellung unterstützt:
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

Anfragen für Connected-Content unterliegen nicht unabhängig von anderen Anfragen Rate-Limits und folgen den Webhook-Rate-Limits. Das bedeutet, dass Sie bei einem Connected-Content-Aufruf an einen eindeutigen Endpunkt pro Webhook mit 5.000 Webhooks und auch 5.000 Connected-Content-Aufrufen pro Minute rechnen müssen. Beachten Sie, dass die Zwischenspeicherung dies beeinflussen und die Anzahl der Connected-Content-Aufrufe reduzieren kann. Außerdem können Wiederholungsversuche die Connected-Content-Aufrufe erhöhen. Wir empfehlen daher zu überprüfen, ob der Connected-Content-Endpunkt hier mit einer gewissen Fluktuation umgehen kann.

{% alert note %}
**Rate-Limits sind Geschwindigkeitsbegrenzungen und legen keine genaue Sendegeschwindigkeit fest.** Im Allgemeinen werden Nachrichten innerhalb einer Minute gleichmäßig verteilt und in den allermeisten Fällen zum oder sehr nahe am konfigurierten Limit versendet. Dies ist jedoch nicht immer der Fall, beispielsweise wenn Nachrichten sehr groß sind (wie E-Mails mit vielen Content-Blöcken, Connected-Content-Tags oder Katalogartikel-Tags) oder wenn es zu vielen Liquid-Abbrüchen kommt (abgebrochene Nachrichten belegen weiterhin einen Speicherplatz und können die effektiven Sendegeschwindigkeiten verringern).

In der Praxis kann die nachhaltige Sendegeschwindigkeit (abgeschlossene Nachrichten pro Minute) aufgrund von Wiederholungsversuchen, Netzwerkschwankungen, Latenzzeiten am Downstream-Endpunkt und minutengenauer Glättung unter den konfigurierten Rate-Limits liegen.

Sollten Sie kontinuierlich einen deutlich geringeren Durchsatz als erwartet feststellen, überprüfen Sie bitte die Antwortzeiten von Connected-Content, die Fehlerraten (z. B. `429`) und das Wiederholungsverhalten.
{% endalert %}

## Über Frequency-Capping

Wenn Ihre Nutzerbasis weiter wächst und Ihre Nachrichten auf Lebenszyklus-, Trigger-, Transaktions- und Konversionskampagnen ausgeweitet werden, ist es wichtig, dass Ihre Benachrichtigungen nicht als „Spam“ oder störend empfunden werden. Durch eine bessere Kontrolle über die Erfahrung Ihrer Nutzer ermöglicht Ihnen die Frequenzbegrenzung die Erstellung der gewünschten Kampagnen, ohne Ihr Publikum zu überfordern.

### Übersicht über die Features {#freq-cap-feat-over}

Die Frequenzbegrenzung wird auf der Ebene der Kampagne oder der Canvas-Komponente angewendet und kann für jeden Arbeitsbereich unter **Einstellungen** > **Frequenzbegrenzungsregeln** eingerichtet werden.

Standardmäßig ist das Frequency-Capping aktiviert, wenn neue Kampagnen erstellt werden. Von hier aus können Sie Folgendes auswählen:

- Der Messaging-Kanal, den Sie begrenzen möchten: Push, E-Mail, SMS, Webhook, WhatsApp, LINE oder einer dieser Kanäle.
- Wie oft jede Nutzer:in eine Kampagne oder eine Canvas-Komponente erhalten soll, die von einem Kanal innerhalb eines bestimmten Zeitraums gesendet wird.
- Wie oft sollte jede Nutzer:in innerhalb eines bestimmten Zeitraums eine Kampagne oder eine Canvas-Komponente erhalten, die per [Tag](#frequency-capping-by-tag) gesendet wird?

Dieser Zeitrahmen kann in Minuten, Tagen oder Wochen (sieben Tage) gemessen werden, wobei die maximale Dauer 30 Tage beträgt.

Jede Zeile des Frequency-Capping-Systems wird mit dem`AND`Operator verbunden, und Sie können bis zu 10 Regeln pro Workspace hinzufügen. Sie können mehrere Obergrenzen für dieselben Nachrichtentypen festlegen. So können Sie beispielsweise die Anzahl der Nutzer auf einen Push pro Tag und drei Pushs pro Woche begrenzen. Bitte beachten Sie, dass abgebrochene Nachrichten nicht auf das Frequency-Capping angerechnet werden.

![Abschnitt zum Frequency-Capping mit Listen von Kampagnen und Canvases, für die die Regeln gelten bzw. nicht gelten.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"} 

#### Verhalten bei Frequency-Capping von Nutzer:innen in einem Canvas-Schritt

Wenn ein Canvas-Nutzer:in aufgrund von Frequency-Capping-Einstellungen einer Frequenzbegrenzung unterliegt, wird die Nutzer:in unverzüglich zum nächsten Canvas-Schritt vorangebracht. Der Nutzer:innen wird den Canvas wegen des Frequency-Cappings nicht verlassen.

### Regeln für die Zustellung

Es gibt vielleicht Kampagnen, wie z.B. Transaktionsnachrichten, die den Nutzer immer erreichen sollen, auch wenn er seine Frequenzgrenze bereits erreicht hat. Beispielsweise könnte eine App für die Zustellung eine E-Mail oder eine Push-Benachrichtigung senden, wenn ein Artikel zugestellt wurde, unabhängig davon, wie viele Kampagnen der Nutzer:in bereits erhalten hat.

Wenn Sie möchten, dass eine bestimmte Kampagne die Regeln für die Frequenzbegrenzung außer Kraft setzt, können Sie dies im Braze-Dashboard bei der Planung der Zustellung dieser Kampagne einrichten, indem Sie die **Frequenzbegrenzung** auf **AUS** setzen. 

Danach werden Sie gefragt, ob Sie diese Kampagne immer noch auf Ihre Frequenzobergrenze anrechnen lassen möchten. Nachrichten, die zum Frequency-Capping zählen, werden in die Berechnungen für den Filter „Intelligenter Kanal“ einbezogen. 

Beim Versenden von[ API-Kampagnen]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), die häufig transaktional sind, haben Sie die Möglichkeit, festzulegen, dass eine Kampagne die Regeln des Frequency-Capping ignorieren soll, indem Sie in der API-Anfrage`true` den`override_frequency_capping`Wert auf setzen.

Neue Kampagnen und Canvases, die sich nicht an die Häufigkeitsobergrenzen halten, werden standardmäßig auch nicht auf diese angerechnet. Dies ist für jede Kampagne und jeden Canvas konfigurierbar.

{% alert note %}
Dieses Verhalten ändert das Standardverhalten, wenn Sie das Frequency-Capping für eine Kampagne oder ein Canvas deaktivieren. Die Änderungen sind abwärtskompatibel und wirken sich nicht auf Nachrichten aus, die derzeit live geschaltet sind.
{% endalert %}

![Abschnitt „Zustellung“ mit aktiviertem Frequency-Capping.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"} 

Die verschiedenen Kanäle innerhalb einer Multichannel-Kampagne werden einzeln auf das Frequency-Capping angerechnet. Wenn Sie beispielsweise eine Multichannel-Kampagne mit Push-Benachrichtigungen und E-Mails erstellen und für beide Kanäle Frequency-Capping eingerichtet haben, wird die Push-Benachrichtigung einer Push-Kampagne zugerechnet und die E-Mail-Nachricht einer E-Mail-Kampagne. Die Kampagne zählt auch als eine „Kampagne beliebiger Art“. Wenn Nutzer:innen auf eine Push-Benachrichtigung und eine E-Mail-Kampagne pro Tag beschränkt sind und eine Nutzer:in diese Multichannel-Kampagne erhält, hat sie für den Rest des Tages keinen Anspruch mehr auf Push- oder E-Mail-Kampagnen (es sei denn, eine Kampagne ignoriert die Regeln des Frequency-Capping).

In-App-Nachrichten und Content-Cards werden nicht als Obergrenzen für Kampagnen oder Canvas-Komponenten jeglicher Art gezählt oder auf diese angerechnet.

{% alert important %}
Die globale Frequenzbegrenzung basiert auf der Zeitzone des Benutzers und wird nach Kalendertagen und nicht nach 24-Stunden-Perioden berechnet. Wenn Sie zum Beispiel eine Frequency-Capping-Regel einrichten, die vorsieht, dass nicht mehr als eine Kampagne pro Tag versendet wird, kann ein Nutzer:innen um 23 Uhr in seiner Ortszeit eine Nachricht erhalten und eine Stunde später eine weitere Nachricht bekommen.
{% endalert %}

#### Anwendungsfälle

{% tabs %}
{% tab Use case 1 %}

Angenommen, Sie legen eine Regel des Frequency-Capping fest, sodass Ihre Nutzer:innen nicht mehr als drei Kampagnen oder Canvas-Schritte pro Woche aus allen Kampagnen oder Canvas-Schritten erhalten.

Wenn Ihr Nutzer in dieser Woche drei Push-Benachrichtigungen, zwei In-App-Nachrichten und eine Content Card erhalten soll, wird er alle diese Nachrichten erhalten.

{% endtab %}
{% tab Use case 2 %}

Dieses Szenario verwendet eine Frequency-Capping-Regel, damit Nutzer:innen nicht mehr als zwei Kampagnen oder Canvas-Schritte pro Woche aus allen Kampagnen oder Canvas-Schritten erhalten.

**Wenn das folgende Szenario auftritt:**

- Eine Nutzer:in triggert dieselbe Kampagne innerhalb einer`Campaign ABC` Woche dreimal.
- Dieser Nutzer:innen triggert `Campaign ABC` einmal am Montag, einmal am Mittwoch und einmal am Donnerstag.

![Abschnitt „Frequency-Capping“ mit der Regel, dass einer Nutzer:in pro Woche maximal zwei Kampagnen mit Push-Benachrichtigungen/Canvas-Schritte aus allen Kampagnen/Canvas-Schritten gesendet werden dürfen.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Dann lautet das erwartete Verhalten wie folgt:**

- Dieser Benutzer wird die Kampagnensendungen erhalten, die am Montag und Mittwoch ausgelöst wurden.
- Dieser Benutzer wird die dritte Kampagnensendung am Donnerstag nicht erhalten, da er in dieser Woche bereits zwei Push-Kampagnensendungen erhalten hat.

{% endtab %}
{% endtabs %}

### Frequency-Capping nach Tag

[Regeln für die Frequenzbegrenzung](#delivery-rules) können auf Arbeitsbereiche angewendet werden, indem Sie bestimmte Tags verwenden, die Sie auf Ihre Kampagnen und Canvases angewendet haben, so dass Sie Ihre Frequenzbegrenzung im Wesentlichen auf benutzerdefinierte Gruppen stützen können.

Mit der Frequenzkappung nach Tag können Regeln für die Haupt- und verschachtelten Tags festgelegt werden, so dass Braze alle Tags berücksichtigt. Wenn Sie beispielsweise das Haupt-Tag A als Frequenzbegrenzung ausgewählt haben, berücksichtigen wir bei der Festlegung des Limits auch Informationen in allen verschachtelten Tags (z. B. Tags B und C).

Sie können auch die reguläre Frequenzkappung mit der Frequenzkappung durch Tags kombinieren. Beachten Sie die folgenden Regeln:

1. Bitte beachten Sie, dass pro Woche maximal drei Kampagnen mit Push-Benachrichtigungen oder Canvas-Komponenten aus allen Kampagnen und Canvas-Schritten zulässig sind. <br>**UND**
2. Bitte beschränken Sie sich auf maximal zwei Kampagnen mit Push-Benachrichtigungen oder Canvas-Komponenten pro Woche mit dem Tag`promotional`.

![Frequency-Capping mit zwei Regeln, die festlegen, wie viele Kampagnen/Canvase mit Push-Benachrichtigungen pro Woche an einen Nutzer:innen gesendet werden können.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Infolgedessen erhalten Ihre Benutzer nicht mehr als drei Kampagnensendungen pro Woche über alle Kampagnen und Canvas-Schritte und nicht mehr als zwei Push-Benachrichtigungskampagnen oder Canvas-Komponenten mit dem Tag `promotional`.

{% alert important %}
Leinwände werden auf der Ebene der Leinwand getaggt, im Gegensatz zum Tagging nach Komponente. Daher übernimmt jede Canvas-Komponente alle Tags auf Canvas-Ebene.
{% endalert %}

#### Widersprüchliche Regeln

Bei widersprüchlichen Regeln wird die restriktivste, anwendbare Frequency-Capping-Regel auf Ihre Nutzer:innen angewendet. Nehmen wir zum Beispiel an, Sie haben die folgenden Regeln:

1. Es darf nicht mehr als eine Kampagne mit Push-Benachrichtigungen oder Canvas-Komponente pro Woche aus allen Kampagnen und Canvas-Komponenten versendet werden. <br>**UND**
2. Nicht mehr als drei Push-Benachrichtigungskampagnen oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Abschnitt Frequency-Capping mit widersprüchlichen Regeln, um zu begrenzen, wie viele Push-Benachrichtigungen Kampagnen/Canvas-Schritte pro 1 Woche an einen Nutzer:innen gesendet werden.]({% image_buster /assets/img/global_rules.png %} "global rules")

In diesem Beispiel wird Ihr Benutzer in einer bestimmten Woche nicht mehr als eine Push-Benachrichtigungskampagne oder Canvas-Komponente mit dem Tag "Werbeaktion" erhalten, da Sie festgelegt haben, dass Benutzer nicht mehr als eine Push-Benachrichtigungskampagne oder Canvas-Komponente von allen Kampagnen und Canvas-Komponenten erhalten sollen. Mit anderen Worten, die restriktivste anwendbare Frequenzregel ist die Regel, die auf einen bestimmten Benutzer angewendet wird.

#### Anzahl der Tags

Das Frequency-Capping durch Tag-Regeln wird zum Zeitpunkt des Versendens einer Nachricht berechnet. Das bedeutet, dass die Häufigkeitsbegrenzung nach Tags nur die Tags zählt, die sich derzeit in den Kampagnen oder Canvases befinden, die ein Benutzer in der Vergangenheit erhalten hat. Es werden keine Tags gezählt, die zum Zeitpunkt des Versands in den Kampagnen oder Canvases vorhanden waren, aber inzwischen entfernt wurden. Es ist von Bedeutung, wenn ein Tag nachträglich zu einer Nachricht hinzugefügt wird, die ein Nutzer:in in der Vergangenheit erhalten hat, jedoch bevor die neueste getaggte Nachricht gesendet wurde.

##### Anwendungsfall

Betrachten Sie die folgenden Kampagnen und die Begrenzung der Häufigkeit nach Tag-Regeln:

**Kampagnen**:

- **Kampagne A** ist eine Push-Kampagne mit dem Tag `promotional`. Der Versand ist für Montag um 9 Uhr vorgesehen.
- **Kampagne B** ist eine Push-Kampagne mit der Bezeichnung `promotional`. Der Versand ist für Mittwoch um 9 Uhr vorgesehen.

**Frequency-Capping nach Tag-Regel:**

- Ihr Benutzer sollte nicht mehr als eine Push-Benachrichtigungskampagne pro Woche mit dem Tag `promotional` erhalten.<br><br>

| Aktion | Ergebnis |
|---|---|
| Der Tag `promotional` wird aus **Kampagne A** entfernt, nachdem Ihr Nutzer:innen die Nachricht erhalten hat, aber bevor **Kampagne B gesendet wurde.** | Ihre Nutzer:in erhält **Kampagne B**.|
| Das Tag `promotional` wurde versehentlich aus **Kampagne A** entfernt, nachdem Ihr Benutzer die Nachricht erhalten hat. <br> Der Tag wird am Dienstag wieder zu **Kampagne A** hinzugefügt, bevor **Kampagne B** versendet wird. | Ihre Nutzer:innen erhalten keine **Kampagne B**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Versenden in großem Maßstab {#sending-at-large-scales}

„Frequency-Capping nach Tag-Regeln“ wird bei großen Skalen, wie z. B. 100 Nachrichten pro Kanal aus Kampagnen oder Canvas-Komponenten, möglicherweise nicht richtig angewendet.

Wenn Ihre Regel für die Frequenzbegrenzung nach Tag zum Beispiel lautet:

> Nicht mehr als zwei E-Mail-Kampagnen oder Canvas-Komponenten mit dem Tag `Promotional` für einen Benutzer pro Woche.

Und wenn Sie dem Benutzer im Laufe einer Woche mehr als 100 E-Mails aus Kampagnen und Canvas-Schritten mit eingeschalteter Häufigkeitsbegrenzung senden, werden möglicherweise mehr als zwei E-Mails an den Benutzer gesendet.

Da 100 Nachrichten pro Kanal mehr sind, als die meisten Marken an ihre Nutzer:innen senden, ist es unwahrscheinlich, dass diese Beschränkung Auswirkungen hat. Um diese Einschränkung zu vermeiden, können Sie eine Obergrenze für die maximale Anzahl von E-Mails festlegen, die Ihre Benutzer im Laufe einer Woche erhalten sollen.

Sie könnten zum Beispiel die folgende Regel aufstellen:

> Maximal drei E-Mail-Kampagnen oder Canvas-Komponenten pro Woche aus allen Kampagnen und Canvas-Schritten.

Diese Regel legt fest, dass keine Nutzer:innen mehr als 100 E-Mails pro Woche erhalten, da Nutzer:innen höchstens drei E-Mails pro Woche aus Kampagnen oder Canvas-Komponenten erhalten, bei denen Frequency-Capping aktiviert ist.

## Häufig gestellte Fragen

### Wenn ich eine Sendungsdrosselung auf einer aktiven Canvas-Seite ändere, hat dies Auswirkungen auf Nutzer:innen, die sich bereits auf der Canvas-Seite befinden?

Ja, wenn Sie ein Canvas-Rate-Limit erhöhen oder verringern, wird das aktualisierte Rate-Limit aufgrund von Caching innerhalb von etwa 30 Sekunden nach der Änderung für neue Nachrichten wirksam.

### Führt Frequency-Capping dazu, dass Nutzer:innen ein Canvas verlassen?

Nein. Wenn ein Canvas-Nutzer:in aufgrund globaler Frequency-Capping-Einstellungen einer Frequenzbegrenzung unterliegt, wird der Nutzer:in sofort zum nächsten Canvas-Schritt vorangebracht. Die Nutzer:innen werden den Canvas aufgrund des Frequency-Capping **nicht** verlassen.

### Wie kann ich Nutzer:innen identifizieren, die im Canvas dem Frequency-Capping unterliegen?

Nutzer:innen, für die ein Frequency-Capping gilt, generieren kein Sendeereignis für diesen Schritt. Um diese Nutzer:innen zu identifizieren, können Sie [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) verwenden, um Ereignisse mit begrenzter Häufigkeit von Nachrichten zu verfolgen. Alternativ können Sie eine [Segment-Erweiterung]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) erstellen, um Nutzer:innen zu analysieren, die den Canvas betreten haben, jedoch nicht die erwartete Nachricht erhalten haben.

