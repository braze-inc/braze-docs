---
nav_title: Rate-Limiting und Frequency-Capping
article_title: Rate-Limiting und Frequency-Capping
page_order: 6
tool: Campaigns
page_type: reference
description: "In diesem Referenzartikel wird das Konzept des Rate-Limiting und des Frequency-Capping in Kampagnen erläutert und wie Sie den Marketingdruck steuern können, um die Nutzererfahrung zu verbessern."

---

# Rate-Limiting und Frequency-Capping

> Rate-Limiting und Frequency-Capping können kombiniert eingesetzt werden, um sicherzustellen, dass Ihre Nutzer:innen die gewünschten Nachrichten erhalten.

## Über Rate-Limiting

Braze ermöglicht es Ihnen, den Marketingdruck zu kontrollieren, indem Sie Ihre Kampagnen mit Rate-Limiting versehen und so die Menge des von Ihrer Plattform ausgehenden Datenverkehrs regulieren. Sie können zwei verschiedene Arten von Rate-Limiting für Ihre Kampagnen einsetzen: 

1. [Nutzerzentriertes Rate-Limiting:](#user-centric-rate-limiting) Konzentriert sich darauf, den Nutzer:innen das beste Erlebnis zu bieten.
2. [Rate-Limiting für die Zustellungsgeschwindigkeit:](#delivery-speed-rate-limiting) Berücksichtigt die Bandbreite Ihrer Server.

Braze versucht, die gesendeten Nachrichten gleichmäßig über die Minute zu verteilen, kann dies aber nicht garantieren. Wenn Sie beispielsweise eine Kampagne mit einem Rate-Limit von 5.000 Nachrichten pro Minute haben, versuchen wir, die 5.000 Anfragen gleichmäßig über die Minute zu verteilen (etwa 84 Nachrichten pro Sekunde), aber die Rate pro Sekunde kann variieren.

### Nutzerzentriertes Rate-Limiting

Wenn Sie mehr Segmente erstellen, wird es Fälle geben, in denen sich die Mitgliedschaft in diesen Segmenten überschneidet. Wenn Sie Kampagnen an diese Segmente versenden, sollten Sie darauf achten, dass Sie Ihre Nutzer:innen nicht zu oft anschreiben. Wenn Nutzer:innen zu viele Nachrichten innerhalb eines kurzen Zeitraums erhalten, fühlen sie sich überfordert und deaktivieren entweder die Push-Benachrichtigungen oder deinstallieren Ihre App.

#### Relevante Segmentfilter

Braze stellt die folgenden Filter zur Verfügung, mit denen Sie die Häufigkeit, mit der Ihre Nutzer:innen Nachrichten erhalten, einschränken können:

- Letzte Interaktion mit Nachricht
- Empfangszeitpunkt der letzten Nachricht
- Letzter empfangener Push
- Letzte empfangene E-Mail
- Letzte empfangene SMS

#### Implementieren von Filtern

Nehmen wir an, wir haben ein Segment mit dem Namen „Retargeting-Filter-Showcase" erstellt, das den Filter „Letzte Nutzung der App vor mehr als 7 Tagen" verwendet, um eine Zielgruppe zusammenzustellen. Dies wäre ein Standardsegment für erneute Interaktion.

Wenn Sie über andere, zielgerichtetere Segmente verfügen, die kürzlich Benachrichtigungen erhalten haben, möchten Sie möglicherweise nicht, dass Ihre Nutzer:innen von allgemeineren Kampagnen angesprochen werden, die sich an dieses Segment richten. Durch Hinzufügen des Filters „Zuletzt empfangene Push-Benachrichtigung" zu diesem Segment wird sichergestellt, dass Personen, die in den letzten 24 Stunden eine weitere Benachrichtigung erhalten haben, für die nächsten 24 Stunden aus diesem Segment entfernt werden. Wenn sie 24 Stunden später weiterhin die anderen Kriterien des Segments erfüllen und keine weiteren Benachrichtigungen erhalten haben, werden sie wieder in das Segment aufgenommen.

![Ein Segment mit dem Namen „Retargeting-Filter-Showcase" und der Filtergruppe „Zuletzt vor mehr als 7 Tagen verwendete App".]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"} 

Wenn Sie diesen Filter an alle Segmente anhängen, auf die Ihre Kampagnen abzielen, erhalten Ihre Nutzer:innen maximal einen Push alle 24 Stunden. Sie können dann Ihre Nachrichten nach Prioritäten ordnen und sicherstellen, dass Ihre wichtigsten Nachrichten vor den weniger wichtigen Nachrichten zugestellt werden.

#### Festlegen einer maximalen Nutzerobergrenze

Im Schritt **Zielgruppen** Ihres Kampagnen-Editors können Sie auch die Gesamtzahl der Nutzer:innen begrenzen, die Ihre Nachricht erhalten sollen. Dies dient als Überprüfung, die unabhängig von Ihren Kampagnenfiltern ist.

![Zielgruppenübersicht mit einem ausgewählten Kontrollkästchen zur Begrenzung der Anzahl der Personen, die die Kampagne erhalten.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"} 

Durch die Auswahl der maximalen Nutzerobergrenze können Sie das Volumen der gesendeten Nachrichten pro Kanal oder global für alle Nachrichtentypen begrenzen.

{% alert note %}
Die maximale Nutzerobergrenze begrenzt die Anzahl der angesprochenen Nutzer:innen, nicht die Anzahl der erfolgreich gesendeten Nachrichten. Da abgebrochene Nachrichten auf dieses Limit angerechnet werden, kann die tatsächliche Anzahl der gesendeten Nachrichten geringer sein als das konfigurierte Limit. Wenn Sie beispielsweise eine Obergrenze von 10.000 festlegen und 2.000 Nachrichten aufgrund von Liquid-Logik oder anderen Bedingungen abgebrochen werden, werden nur 8.000 Nachrichten versendet.
{% endalert %}

##### Maximale Nutzerobergrenze mit Optimierungen

Wenn Sie eine Optimierung wie Winning Variant oder Personalized Variant verwenden, besteht die Kampagne aus zwei Sendungen: dem anfänglichen Experiment und der endgültigen Sendung. 

Um in diesem Szenario eine maximale Nutzerobergrenze festzulegen, markieren Sie die Option **Anzahl der Personen begrenzen, die diese Kampagne erhalten sollen**, wählen Sie dann **Insgesamt sollte diese Kampagne** und geben Sie ein Zielgruppenlimit ein. Ihre Zielgruppe wird durch die im **A/B-Test**-Panel angezeigten Prozentsätze aufgeteilt. 

Wenn Sie **Jedes Mal, wenn die Kampagne geplant wird** auswählen, werden diese beiden Phasen separat auf die eingestellte Anzahl begrenzt. Dies ist in der Regel nicht wünschenswert.

#### Festlegen einer maximalen Impressionen-Obergrenze für Kampagnen

Bei In-App-Nachrichten können Sie den Marketingdruck kontrollieren, indem Sie eine maximale Anzahl von Impressionen festlegen, die Ihrer Nutzerbasis angezeigt werden. Nach Erreichen dieser Anzahl sendet Braze keine weiteren Nachrichten an Ihre Nutzer:innen. Es ist jedoch wichtig zu beachten, dass diese Obergrenze nicht exakt ist. 

In-App-Nachrichtenregeln werden zu Beginn der Sitzung an eine App gesendet, was bedeutet, dass Braze eine Nachricht an die Nutzer:in senden kann, bevor das Limit erreicht ist. Wenn die Nutzer:in jedoch die Nachricht triggert, ist das Limit bereits erreicht. In diesem Fall zeigt das Gerät weiterhin die Nachricht an.

Nehmen wir zum Beispiel an, Sie haben ein Spiel mit einer In-App-Nachricht, die ausgelöst wird, wenn Nutzer:innen ein Level schaffen, und Sie begrenzen diese auf 100 Impressionen. Bisher gab es 99 Impressionen. Alice und Bob starten beide das Spiel, und Braze teilt ihren Geräten mit, dass sie berechtigt sind, die Nachricht zu empfangen, wenn sie ein Level schaffen. Alice schafft zuerst ein Level und erhält die Nachricht. Bob schafft das nächste Level, aber da sein Gerät seit Beginn seiner Sitzung nicht mit den Braze-Servern kommuniziert hat, ist seinem Gerät nicht bekannt, dass die Nachricht ihr Limit erreicht hat, und er erhält die Nachricht ebenfalls. Wenn jedoch eine Impressionen-Obergrenze erreicht wurde, sendet das System bei der nächsten Anfrage eines Geräts nach der Liste der zulässigen In-App-Nachrichten diese Nachricht nicht und entfernt sie von diesem Gerät.

### Rate-Limiting und A/B-Tests

Wenn Sie Rate-Limiting bei einem A/B-Test verwenden, wird das Rate-Limit nicht in gleicher Weise auf die Kontrollgruppe angewandt wie auf die Testgruppe, was eine potenzielle Quelle für zeitliche Verzerrungen ist. Um diese Verzerrung zu vermeiden, verwenden Sie geeignete Konversionsfenster.

### Rate-Limiting für die Zustellungsgeschwindigkeit

Sollten Sie umfangreiche Kampagnen planen, die zu einem Anstieg der Nutzeraktivität und einer Überlastung Ihrer Server führen könnten, haben Sie die Möglichkeit, ein Rate-Limit pro Minute für den Versand von Nachrichten festzulegen. Dies bedeutet, dass Braze innerhalb einer Minute nicht mehr als die von Ihnen festgelegte Anzahl an Nachrichten versendet.

Wenn Sie während der Kampagnenerstellung Nutzer:innen ansprechen, können Sie unter **Zielgruppen** (für Kampagnen) oder **Sendeeinstellungen** (für Canvas) ein Rate-Limit auswählen (in verschiedenen Abstufungen von 10 bis 500.000 Nachrichten pro Minute).

Beachten Sie, dass Kampagnen ohne Rate-Limits diese Zustellungslimits überschreiten können. Beachten Sie jedoch auch, dass Nachrichten abgebrochen werden, wenn sie aufgrund eines niedrigen Rate-Limits 72 Stunden oder länger verzögert werden. Wenn das Rate-Limit zu niedrig ist, erhält die erstellende Person der Kampagne Warnungen im Dashboard und per E-Mail.

#### Beispiel

Wenn Sie versuchen, 75.000 Nachrichten mit einem Rate-Limit von 10.000 pro Minute zu versenden, wird die Zustellung über acht Minuten verteilt. Ihre Kampagne wird in den ersten sieben Minuten jeweils maximal 10.000 Nachrichten und in der letzten Minute 5.000 Nachrichten zustellen.

#### Anzahl der Sendungen

Beachten Sie, dass Nachrichten mit Rate-Limiting möglicherweise nicht gleichmäßig über jede Minute gesendet werden. Am Beispiel eines Rate-Limits von 10.000 pro Minute bedeutet dies, dass Braze sicherstellt, dass nicht mehr als 10.000 Nachrichten pro Minute gesendet werden. Das könnte bedeuten, dass ein höherer Prozentsatz der 10.000 Nachrichten innerhalb der ersten halben Minute gesendet wird als in der letzten halben Minute.

Das Rate-Limit wird zu Beginn des Sendeversuchs angewendet. Wenn es zu Schwankungen bei der Dauer des Sendevorgangs kommt, kann die Anzahl der abgeschlossenen Sendungen für einige Minuten geringfügig über dem Rate-Limit liegen. Mit der Zeit wird die Anzahl der Sendungen pro Minute im Durchschnitt nicht mehr als das Rate-Limit betragen.

{% alert important %}
Seien Sie vorsichtig, wenn Sie zeitkritische Nachrichten mit dieser Form des Rate-Limiting in Bezug auf die Gesamtzahl der Nutzer:innen in einem Segment verzögern. Wenn das Segment beispielsweise 30 Millionen Nutzer:innen umfasst, Sie aber das Rate-Limit auf 10.000 pro Minute festlegen, wird ein großer Teil Ihrer Nutzerbasis die Nachricht erst am nächsten Tag erhalten.
{% endalert %}

#### Multichannel-Kampagnen und Canvase

Bei der Festlegung von Rate-Limits für die Zustellungsgeschwindigkeit bei einer Multichannel-Kampagne oder einem Canvas können Sie zwischen gemeinsamen Rate-Limits und kanalbasierten Rate-Limits wählen.

Wenn eine Multichannel-Kampagne oder ein Canvas ein gemeinsames Rate-Limit verwendet, bedeutet dies, dass die Gesamtzahl der pro Minute von der Kampagne oder dem Canvas gesendeten Nachrichten das Rate-Limit nicht überschreitet. Wenn Ihr Canvas beispielsweise ein Rate-Limit von 500.000 pro Minute aufweist und E-Mail- sowie SMS-Nachrichten-Schritte enthält, versendet Braze insgesamt 500.000 Nachrichten pro Minute über E-Mail und SMS.

![Die Option zur Begrenzung der Versandrate der Kampagne wurde mit 500.000 Nachrichten pro Minute ausgewählt.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"} 

Wenn eine Multichannel-Kampagne oder ein Canvas kanalbasiertes Rate-Limiting verwendet, gelten die Rate-Limits für jeden der von Ihnen ausgewählten Kanäle. Sie können beispielsweise Ihre Kampagne oder Ihren Canvas so einstellen, dass maximal 5.000 Webhooks und 2.500 SMS-Nachrichten pro Minute über die gesamte Kampagne oder den Canvas versendet werden.

![Getrennte Rate-Limits für zwei Kanäle, Webhook und SMS/MMS/RCS, mit 5.000 bzw. 2.500 Nachrichten pro Minute.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Push-Benachrichtigungen

Für Kampagnen oder Canvase mit Push-Plattformen (wie Android, iOS, Web-Push oder Kindle) können Sie **Push-Benachrichtigungen** auswählen, um ein Rate-Limit durchzusetzen, das für alle Push-Plattformen in Ihrer Kampagne oder Ihrem Canvas gilt.

![Das Kanal-Dropdown-Menü mit Optionen für Push-Plattformen und Push-Benachrichtigungen.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"} 

Wenn Sie ein Limit für Push-Benachrichtigungen auswählen, können Sie keine individuellen Rate-Limits für Push-Kanäle festlegen. Wenn Sie Limits für einzelne Push-Kanäle auswählen, können Sie keine gemeinsamen Limits für Push-Benachrichtigungen festlegen.

{% alert important %}
**Updates der Rate-Limiting-Schnittstelle**<br>
Braze hat die Rate-Limiting-Schnittstelle aktualisiert, um mehr Transparenz und Kontrolle darüber zu bieten, wie Rate-Limits auf Multichannel-Kampagnen und Canvase angewendet werden.<br><br>

- **Bestehende Kampagnen und Canvase:** Alle bestehenden Kampagnen und Canvase wurden auf diese Schnittstelle migriert. Ihr Zustellungsverhalten bleibt unverändert. Das Dashboard zeigt an, ob die Kampagne eine gemeinsame oder eine kanalbezogene Logik verwendet.<br>
- **Neue Kampagnen und Canvase:** Für alle neuen Kampagnen und Canvase steht eine manuelle Umschaltfunktion zur Verfügung, mit der Sie Ihre bevorzugte Rate-Limit-Logik auswählen können. Stellen Sie sicher, dass Sie bei der Einrichtung oder Aktualisierung eines Rate-Limits für eine Kampagne oder einen Canvas das Rate-Limiting-Verhalten auswählen, das Ihrem beabsichtigten Verhalten entspricht.
{% endalert %}

##### Überlegungen zum Rate-Limiting

Einige Hinweise, die Sie bei der Konfiguration von Rate-Limits beachten sollten, und welches Verhalten Sie erwarten können:

- Der Versand von SMS unterliegt einem Rate-Limit von 50.000 pro Abo-Gruppe. Einige SMS-Anbieter können andere Beschränkungen auferlegen.
- Die folgenden Nachrichten werden nicht gedrosselt oder auf das Rate-Limit angerechnet:
    - Testsendungen
    - Seed-Gruppen
    - Content-Cards, die so konfiguriert sind, dass sie „beim ersten Eindruck" erstellt werden (dies wird durch die Häufigkeit der App-Impressionen gesteuert. Weitere Informationen zu den Unterschieden zwischen den Optionen zur Kartenerstellung finden Sie unter [Kartenerstellung]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences).)
- Für die folgenden Fälle werden keine Rate-Limits für die Zustellungsgeschwindigkeit unterstützt:
    - Automatische SMS-Antworten
    - SLA-gestützte Nachrichten (wie [Transaktions-E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign))
    - In-App-Nachrichten
    - Feature-Flags
    - Banner

#### Rate-Limiting und Connected-Content-Wiederholungsversuche

Wenn die [Wiederholungsfunktion für Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/) aktiviert ist, wiederholt Braze fehlgeschlagene Aufrufe unter Einhaltung des Rate-Limits, das Sie für jede erneute Sendung festgelegt haben. Betrachten wir das Szenario des Versands von 75.000 Nachrichten mit einem Rate-Limit von 10.000 pro Minute. Stellen Sie sich vor, dass der Aufruf in der ersten Minute fehlschlägt oder langsam ist und nur 4.000 Nachrichten versendet werden.

Anstatt zu versuchen, die Verzögerung auszugleichen und die verbleibenden 6.000 Nachrichten in der zweiten Minute zu senden oder sie zu den 10.000 Nachrichten hinzuzufügen, die bereits zum Senden eingeplant sind, verschiebt Braze diese 6.000 Nachrichten ans Ende der Warteschlange und fügt gegebenenfalls eine Minute zu den Gesamtminuten hinzu, die für den Versand Ihrer Nachricht erforderlich wären.

| Minute | Kein Fehler | 6.000 Fehler in Minute 1 |
|--------|------------|---------------------------|
| 1      | 10.000     | 4.000                     |
| 2      | 10.000     | 10.000                    |
| 3      | 10.000     | 10.000                    |
| 4      | 10.000     | 10.000                    |
| 5      | 10.000     | 10.000                    |
| 6      | 10.000     | 10.000                    |
| 7      | 10.000     | 10.000                    |
| 8      | 5.000      | 10.000                    |
| 9      | 0          | 6.000                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Connected-Content-Anfragen unterliegen keinem unabhängigen Rate-Limit und folgen dem Webhook-Rate-Limit. Das bedeutet, dass Sie bei einem Connected-Content-Aufruf an einen eindeutigen Endpunkt pro Webhook mit 5.000 Webhooks und auch 5.000 Connected-Content-Aufrufen pro Minute rechnen können. Beachten Sie, dass Caching dies beeinflussen und die Anzahl der Connected-Content-Aufrufe reduzieren kann. Außerdem können Wiederholungsversuche die Connected-Content-Aufrufe erhöhen. Wir empfehlen daher zu überprüfen, ob der Connected-Content-Endpunkt mit einer gewissen Schwankung umgehen kann.

{% alert note %}
**Rate-Limits sind Geschwindigkeitsbegrenzungen und legen keine exakte Sendegeschwindigkeit fest.** Im Allgemeinen werden Nachrichten innerhalb einer Minute gleichmäßig verteilt und in den allermeisten Fällen zum oder sehr nahe am konfigurierten Limit versendet. Dies ist jedoch nicht immer der Fall – beispielsweise wenn Nachrichten sehr groß sind (wie E-Mails mit vielen Content-Blöcken, Connected-Content-Tags oder Katalogartikel-Tags) oder wenn es zu vielen Liquid-Abbrüchen kommt (abgebrochene Nachrichten belegen weiterhin einen Platz und können die effektive Sendegeschwindigkeit verringern).<br><br>
In der Praxis kann die nachhaltige Sendegeschwindigkeit (abgeschlossene Nachrichten pro Minute) aufgrund von Wiederholungsversuchen, Netzwerkschwankungen, Latenzzeiten am Downstream-Endpunkt und minutengenauer Glättung unter dem konfigurierten Rate-Limit liegen. Sollten Sie kontinuierlich einen deutlich geringeren Durchsatz als erwartet feststellen, überprüfen Sie die Antwortzeiten von Connected-Content, die Fehlerraten (z. B. `429`) und das Wiederholungsverhalten.
{% endalert %}

## Über Frequency-Capping

Wenn Ihre Nutzerbasis weiter wächst und Ihre Nachrichten auf Lebenszyklus-, Trigger-, Transaktions- und Konversionskampagnen ausgeweitet werden, ist es wichtig, dass Ihre Benachrichtigungen nicht als „Spam" oder störend empfunden werden. Durch eine bessere Kontrolle über die Erfahrung Ihrer Nutzer:innen ermöglicht Ihnen das Frequency-Capping die Erstellung der gewünschten Kampagnen, ohne Ihre Zielgruppe zu überfordern.

### Feature-Übersicht {#freq-cap-feat-over}

Das Frequency-Capping wird auf der Ebene der Kampagne oder der Canvas-Komponente angewendet und kann für jeden Workspace unter **Einstellungen** > **Frequency-Capping-Regeln** eingerichtet werden.

Standardmäßig ist das Frequency-Capping aktiviert, wenn neue Kampagnen erstellt werden. Von hier aus können Sie Folgendes auswählen:

- Den Messaging-Kanal, den Sie begrenzen möchten: Push, E-Mail, SMS, Webhook, WhatsApp, LINE oder einen dieser Kanäle.
- Wie oft jede Nutzer:in eine Kampagne oder Canvas-Komponente erhalten soll, die von einem Kanal innerhalb eines bestimmten Zeitraums gesendet wird.
- Wie oft jede Nutzer:in eine Kampagne oder Canvas-Komponente erhalten soll, die per [Tag](#frequency-capping-by-tag) innerhalb eines bestimmten Zeitraums gesendet wird.

Dieser Zeitrahmen kann in Minuten, Tagen oder Wochen (sieben Tage) gemessen werden, wobei die maximale Dauer 30 Tage beträgt.

Jede Zeile des Frequency-Capping wird mit dem `AND`-Operator verbunden, und Sie können bis zu 10 Regeln pro Workspace hinzufügen. Sie können mehrere Obergrenzen für dieselben Nachrichtentypen festlegen. So können Sie beispielsweise Nutzer:innen auf maximal einen Push pro Tag und maximal drei Pushs pro Woche begrenzen. Beachten Sie, dass abgebrochene Nachrichten nicht auf das Frequency-Capping angerechnet werden.

![Abschnitt zum Frequency-Capping mit Listen von Kampagnen und Canvasen, für die die Regeln gelten bzw. nicht gelten.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"} 

#### Verhalten bei Frequency-Capping in einem Canvas-Schritt

Wenn eine Canvas-Nutzer:in aufgrund globaler Frequency-Capping-Einstellungen einer Frequenzbegrenzung unterliegt, wird sie sofort zum nächsten Canvas-Schritt vorangebracht. Die Nutzer:in wird den Canvas aufgrund des Frequency-Capping nicht verlassen.

### Regeln für die Zustellung

Es gibt möglicherweise Kampagnen, wie z. B. Transaktionsnachrichten, die Nutzer:innen immer erreichen sollen, auch wenn sie ihre Frequenzgrenze bereits erreicht haben. Beispielsweise könnte eine Liefer-App eine E-Mail oder Push-Benachrichtigung senden, wenn ein Artikel zugestellt wurde, unabhängig davon, wie viele Kampagnen die Nutzer:in bereits erhalten hat.

Wenn Sie möchten, dass eine bestimmte Kampagne die Frequency-Capping-Regeln außer Kraft setzt, können Sie dies im Braze-Dashboard bei der Planung der Zustellung dieser Kampagne einrichten, indem Sie **Frequency-Capping** auf **AUS** umschalten. 

Danach werden Sie gefragt, ob Sie diese Kampagne weiterhin auf Ihre Frequenzobergrenze anrechnen lassen möchten. Nachrichten, die zum Frequency-Capping zählen, werden in die Berechnungen für den Filter „Intelligenter Kanal" einbezogen. 

Beim Versenden von [API-Kampagnen]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), die häufig transaktional sind, haben Sie die Möglichkeit festzulegen, dass eine Kampagne die Frequency-Capping-Regeln ignorieren soll, indem Sie in der API-Anfrage `override_frequency_capping` auf `true` setzen.

Neue Kampagnen und Canvase, die sich nicht an die Frequency-Caps halten, werden standardmäßig auch nicht auf diese angerechnet. Dies ist für jede Kampagne und jeden Canvas konfigurierbar.

{% alert note %}
Dieses Verhalten ändert das Standardverhalten, wenn Sie das Frequency-Capping für eine Kampagne oder einen Canvas deaktivieren. Die Änderungen sind abwärtskompatibel und wirken sich nicht auf Nachrichten aus, die derzeit live sind.
{% endalert %}

![Abschnitt „Zustellungssteuerung" mit aktiviertem Frequency-Capping.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"} 

Die verschiedenen Kanäle innerhalb einer Multichannel-Kampagne werden einzeln auf das Frequency-Capping angerechnet. Wenn Sie beispielsweise eine Multichannel-Kampagne mit Push und E-Mail erstellen und für beide Kanäle Frequency-Capping eingerichtet haben, wird der Push einer Push-Kampagne zugerechnet und die E-Mail-Nachricht einer E-Mail-Kampagne. Die Kampagne zählt auch als eine „Kampagne beliebiger Art". Wenn Nutzer:innen auf eine Push- und eine E-Mail-Kampagne pro Tag beschränkt sind und eine Nutzer:in diese Multichannel-Kampagne erhält, ist sie für den Rest des Tages nicht mehr für Push- oder E-Mail-Kampagnen berechtigt (es sei denn, eine Kampagne ignoriert die Frequency-Capping-Regeln).

In-App-Nachrichten und Content-Cards werden nicht als Obergrenzen für Kampagnen oder Canvas-Komponenten jeglicher Art gezählt oder auf diese angerechnet.

{% alert important %}
Das globale Frequency-Capping basiert auf der Zeitzone der Nutzer:innen und wird nach Kalendertagen und nicht nach 24-Stunden-Perioden berechnet. Wenn Sie zum Beispiel eine Frequency-Capping-Regel einrichten, die vorsieht, dass nicht mehr als eine Kampagne pro Tag versendet wird, kann eine Nutzer:in um 23 Uhr in ihrer Ortszeit eine Nachricht erhalten und eine Stunde später eine weitere Nachricht bekommen.
{% endalert %}

#### Anwendungsfälle

{% tabs %}
{% tab Use case 1 %}

Angenommen, Sie legen eine Frequency-Capping-Regel fest, sodass Ihre Nutzer:innen nicht mehr als drei Push-Benachrichtigungs-Kampagnen oder Canvas-Schritte pro Woche aus allen Kampagnen oder Canvas-Schritten erhalten.

Wenn Ihre Nutzer:in in dieser Woche drei Push-Benachrichtigungen, zwei In-App-Nachrichten und eine Content-Card erhalten soll, wird sie alle diese Nachrichten erhalten.

{% endtab %}
{% tab Use case 2 %}

Dieses Szenario verwendet eine Frequency-Capping-Regel, damit Nutzer:innen nicht mehr als zwei Push-Benachrichtigungs-Kampagnen oder Canvas-Schritte pro Woche aus allen Kampagnen oder Canvas-Schritten erhalten.

**Wenn das folgende Szenario auftritt:**

- Eine Nutzer:in triggert dieselbe Kampagne `Campaign ABC` dreimal innerhalb einer Woche.
- Diese Nutzer:in triggert `Campaign ABC` einmal am Montag, einmal am Mittwoch und einmal am Donnerstag.

![Abschnitt „Frequency-Capping" mit der Regel, dass einer Nutzer:in pro Woche maximal zwei Push-Benachrichtigungs-Kampagnen/Canvas-Schritte aus allen Kampagnen/Canvas-Schritten gesendet werden dürfen.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Dann lautet das erwartete Verhalten wie folgt:**

- Diese Nutzer:in wird die Kampagnensendungen erhalten, die am Montag und Mittwoch ausgelöst wurden.
- Diese Nutzer:in wird die dritte Kampagnensendung am Donnerstag nicht erhalten, da sie in dieser Woche bereits zwei Push-Kampagnensendungen erhalten hat.

{% endtab %}
{% endtabs %}

### Frequency-Capping nach Tag

[Frequency-Capping-Regeln](#delivery-rules) können auf Workspaces angewendet werden, indem Sie bestimmte Tags verwenden, die Sie auf Ihre Kampagnen und Canvase angewendet haben, sodass Sie Ihr Frequency-Capping im Wesentlichen auf benutzerdefinierte Gruppen stützen können.

Mit dem Frequency-Capping nach Tag können Regeln für Haupt- und verschachtelte Tags festgelegt werden, sodass Braze alle Tags berücksichtigt. Wenn Sie beispielsweise das Haupt-Tag A als Frequenzbegrenzung ausgewählt haben, berücksichtigen wir bei der Festlegung des Limits auch Informationen in allen verschachtelten Tags (z. B. Tags B und C).

Sie können auch das reguläre Frequency-Capping mit dem Frequency-Capping nach Tags kombinieren. Betrachten Sie die folgenden Regeln:

1. Maximal drei Push-Benachrichtigungs-Kampagnen oder Canvas-Komponenten pro Woche aus allen Kampagnen und Canvas-Schritten. <br>**UND**
2. Maximal zwei Push-Benachrichtigungs-Kampagnen oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Frequency-Capping mit zwei Regeln, die festlegen, wie viele Push-Benachrichtigungs-Kampagnen/Canvase pro Woche an eine Nutzer:in gesendet werden können.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Infolgedessen erhalten Ihre Nutzer:innen nicht mehr als drei Kampagnensendungen pro Woche über alle Kampagnen und Canvas-Schritte und nicht mehr als zwei Push-Benachrichtigungs-Kampagnen oder Canvas-Komponenten mit dem Tag `promotional`.

{% alert important %}
Canvase werden auf der Canvas-Ebene getaggt, im Gegensatz zum Tagging nach Komponente. Daher übernimmt jede Canvas-Komponente alle Tags auf Canvas-Ebene.
{% endalert %}

#### Widersprüchliche Regeln

Bei widersprüchlichen Regeln wird die restriktivste, anwendbare Frequency-Capping-Regel auf Ihre Nutzer:innen angewendet. Nehmen wir zum Beispiel an, Sie haben die folgenden Regeln:

1. Maximal eine Push-Benachrichtigungs-Kampagne oder Canvas-Komponente pro Woche aus allen Kampagnen und Canvas-Komponenten. <br>**UND**
2. Maximal drei Push-Benachrichtigungs-Kampagnen oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Abschnitt „Frequency-Capping" mit widersprüchlichen Regeln zur Begrenzung, wie viele Push-Benachrichtigungs-Kampagnen/Canvas-Schritte pro Woche an eine Nutzer:in gesendet werden.]({% image_buster /assets/img/global_rules.png %} "global rules")

In diesem Beispiel wird Ihre Nutzer:in in einer bestimmten Woche nicht mehr als eine Push-Benachrichtigungs-Kampagne oder Canvas-Komponente mit dem Tag „promotional" erhalten, da Sie festgelegt haben, dass Nutzer:innen nicht mehr als eine Push-Benachrichtigungs-Kampagne oder Canvas-Komponente aus allen Kampagnen und Canvas-Komponenten erhalten sollen. Mit anderen Worten: Die restriktivste anwendbare Frequenzregel ist die Regel, die auf eine bestimmte Nutzer:in angewendet wird.

#### Tag-Zählung

Das Frequency-Capping nach Tag wird zum Zeitpunkt des Nachrichtenversands berechnet. Das bedeutet, dass das Frequency-Capping nach Tag nur die Tags zählt, die sich derzeit in den Kampagnen oder Canvasen befinden, die eine Nutzer:in in der Vergangenheit erhalten hat. Es werden keine Tags gezählt, die zum Zeitpunkt des Versands in den Kampagnen oder Canvasen vorhanden waren, aber inzwischen entfernt wurden. Es wird berücksichtigt, wenn ein Tag nachträglich zu einer Nachricht hinzugefügt wird, die eine Nutzer:in in der Vergangenheit erhalten hat, jedoch bevor die neueste getaggte Nachricht gesendet wurde.

##### Anwendungsfall

Betrachten Sie die folgenden Kampagnen und die Frequency-Capping-nach-Tag-Regel:

**Kampagnen**:

- **Kampagne A** ist eine Push-Kampagne mit dem Tag `promotional`. Der Versand ist für Montag um 9 Uhr vorgesehen.
- **Kampagne B** ist eine Push-Kampagne mit dem Tag `promotional`. Der Versand ist für Mittwoch um 9 Uhr vorgesehen.

**Frequency-Capping-nach-Tag-Regel:**

- Ihre Nutzer:in sollte nicht mehr als eine Push-Benachrichtigungs-Kampagne pro Woche mit dem Tag `promotional` erhalten.<br><br>

| Aktion | Ergebnis |
|---|---|
| Das Tag `promotional` wird aus **Kampagne A** entfernt, nachdem Ihre Nutzer:in die Nachricht erhalten hat, aber bevor **Kampagne B gesendet wurde.** | Ihre Nutzer:in erhält **Kampagne B**.|
| Das Tag `promotional` wurde versehentlich aus **Kampagne A** entfernt, nachdem Ihre Nutzer:in die Nachricht erhalten hat. <br> Das Tag wird am Dienstag wieder zu **Kampagne A** hinzugefügt, bevor **Kampagne B** versendet wird. | Ihre Nutzer:in erhält **Kampagne B** nicht. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Versenden in großem Maßstab {#sending-at-large-scales}

Frequency-Capping-nach-Tag-Regeln werden bei großen Skalen, wie z. B. 100 Nachrichten pro Kanal aus Kampagnen oder Canvas-Komponenten, möglicherweise nicht korrekt angewendet.

Wenn Ihre Frequency-Capping-nach-Tag-Regel zum Beispiel lautet:

> Maximal zwei E-Mail-Kampagnen oder Canvas-Komponenten mit dem Tag `Promotional` für eine Nutzer:in pro Woche.

Und wenn Sie der Nutzer:in im Laufe einer Woche mehr als 100 E-Mails aus Kampagnen und Canvas-Schritten mit aktiviertem Frequency-Capping senden, werden möglicherweise mehr als zwei E-Mails an die Nutzer:in gesendet.

Da 100 Nachrichten pro Kanal mehr sind, als die meisten Marken an ihre Nutzer:innen senden, ist es unwahrscheinlich, dass diese Beschränkung Auswirkungen hat. Um diese Einschränkung zu vermeiden, können Sie eine Obergrenze für die maximale Anzahl von E-Mails festlegen, die Ihre Nutzer:innen im Laufe einer Woche erhalten sollen.

Sie könnten zum Beispiel die folgende Regel aufstellen:

> Maximal drei E-Mail-Kampagnen oder Canvas-Komponenten pro Woche aus allen Kampagnen und Canvas-Schritten.

Diese Regel stellt sicher, dass keine Nutzer:innen mehr als 100 E-Mails pro Woche erhalten, da Nutzer:innen höchstens drei E-Mails pro Woche aus Kampagnen oder Canvas-Komponenten erhalten, bei denen Frequency-Capping aktiviert ist.

## Häufig gestellte Fragen

### Wenn ich eine Sendungsdrosselung bei einem aktiven Canvas ändere, hat dies Auswirkungen auf Nutzer:innen, die sich bereits im Canvas befinden?

Ja, wenn Sie ein Canvas-Rate-Limit erhöhen oder verringern, wird das aktualisierte Limit aufgrund von Caching innerhalb von etwa 30 Sekunden nach der Änderung für neue Nachrichten wirksam.

### Führt Frequency-Capping dazu, dass Nutzer:innen einen Canvas verlassen?

Nein. Wenn eine Canvas-Nutzer:in aufgrund globaler Frequency-Capping-Einstellungen einer Frequenzbegrenzung unterliegt, wird sie sofort zum nächsten Canvas-Schritt vorangebracht. Die Nutzer:in wird den Canvas aufgrund des Frequency-Capping **nicht** verlassen.

### Wie kann ich Nutzer:innen identifizieren, die in einem Canvas dem Frequency-Capping unterlagen?

Nutzer:innen, für die ein Frequency-Capping gilt, generieren kein Sendeereignis für diesen Schritt. Um diese Nutzer:innen zu identifizieren, können Sie [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) verwenden, um Ereignisse mit begrenzter Nachrichtenfrequenz zu verfolgen. Alternativ können Sie eine [Segmenterweiterung]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) erstellen, um Nutzer:innen zu analysieren, die den Canvas betreten haben, jedoch nicht die erwartete Nachricht erhalten haben.