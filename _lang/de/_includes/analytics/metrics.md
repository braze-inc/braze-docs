{% if include.metric == "AMP Clicks" %}
<i>AMP-Klicks</i> ist die Gesamtzahl der Klicks in Ihrer AMP-HTML-E-Mail, kumuliert aus der HTML-, Klartext- und AMP-HTML-Version der E-Mail.
{% endif %}

{% if include.metric == "AMP Opens" %}
<i>AMP-Öffnungen</i> ist die Gesamtzahl der Öffnungen in Ihrer AMP-HTML-E-Mail und den AMP-HTML-Versionen der E-Mail.
{% endif %}

{% if include.metric == "Audience" %}
Die <i>Zielgruppe</i> ist der Prozentsatz der Nutzer, die eine bestimmte Nachricht erhalten haben. Diese Nummer wird von Braze empfangen.
{% endif %}

{% if include.metric == "Bounces" %}
<i>Bounces</i> ist die Gesamtzahl der Nachrichten, die nicht an die vorgesehenen Empfänger zugestellt werden konnten.
{% endif %}

{% if include.metric == "Estimated Real Opens" %}
Die <i>geschätzten realen Öffnungen</i> sind eine Schätzung der Anzahl der eindeutigen Öffnungen, die es geben würde, wenn es keine maschinellen Öffnungen gäbe, und sind das Ergebnis eines proprietären statistischen Modells von Braze.
{% endif %}

{% if include.metric == "Help" %}
<i>Hilfe</i> bedeutet, dass ein Benutzer auf Ihre Nachricht mit dem <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">Schlüsselwort HILFE</a> geantwortet hat und eine automatische HILFE-Antwort erhalten hat.
{% endif %}

{% if include.metric == "Hard Bounce" %}
Ein <i>Hard Bounce</i> liegt vor, wenn eine E-Mail aufgrund eines dauerhaften Zustellungsfehlers nicht an den Empfänger zugestellt werden kann. Ein Hard Bounce kann auftreten, weil der Domänenname nicht existiert oder weil der Empfänger unbekannt ist.
{% endif %}

{% if include.metric == "Soft Bounce" %}
Ein <i>Soft Bounce</i> liegt vor, wenn eine E-Mail aufgrund eines vorübergehenden Zustellungsfehlers nicht an den Empfänger zugestellt werden kann, obwohl die E-Mail-Adresse des Empfängers gültig ist. Ein Soft Bounce kann auftreten, weil der Posteingang des Empfängers voll ist, der Server ausgefallen ist oder die Nachricht zu groß für den Posteingang des Empfängers war.
{% endif %}

{% if include.metric == "Deferral" %}
Eine <i>Zurückstellung</i> liegt vor, wenn eine E-Mail nicht sofort zugestellt werden konnte. Braze versucht jedoch, die E-Mail bis zu 72 Stunden nach diesem vorübergehenden Zustellungsfehler erneut zuzustellen, um die Chancen auf eine erfolgreiche Zustellung zu maximieren, bevor die Versuche für diese spezifische Kampagne eingestellt werden.
{% endif %}

{% if include.metric == "Body Click" %}
Push-Story-Benachrichtigungen zeichnen einen <i>Body Click</i> auf, wenn die Benachrichtigung angeklickt wird. Sie wird nicht aufgezeichnet, wenn eine Nachricht erweitert oder ein Aktions-Button angeklickt wird.
{% endif %}

{% if include.metric == "Body Clicks" %}
<i>Body Clicks</i> treten auf, wenn ein Benutzer auf eine Nachricht klickt, die keine Schaltflächen (Schaltfläche 1, Schaltfläche 2) hat und mit dem traditionellen Editor erstellt wurde, und wenn eine Nachricht, die mit dem HTML-Editor oder dem Drag-and-Drop-Editor erstellt wurde, die <code>brazeBridge.logClick()</code> ohne Argumente.
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
<i>Button 1 Klicks</i> ist die Gesamtzahl der Klicks auf Button 1 der Nachricht.
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>Button 2 Klicks</i> ist die Gesamtzahl der Klicks auf Button 2 der Nachricht.
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>Eingereichte Auswahlen</i> ist die Gesamtzahl der ausgewählten Auswahlen, wenn der Benutzer auf der Seite mit den Umfragefragen einer <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen</a> Umfrage auf die Schaltfläche Senden klickt.
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
Die <i>Öffnungsrate</i> ist der Prozentsatz der geöffneten E-Mails, die von einem einzelnen Nutzer:innen oder Rechner mindestens einmal angeklickt wurden, und ist nur im <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>Berichts-Builder</a> verfügbar.
{% endif %}

{% if include.metric == "Close Message" %}
<i>Nachricht schließen</i> ist die Gesamtzahl der Klicks auf den Nachrichtenbutton "Schließen". Dies gilt nur für In-App-Nachrichten, die per Drag-and-Drop-Editor erstellt wurden – nicht für den herkömmlichen Editor.
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
<i>Bestätigte Zustellungen</i> liegen vor, wenn der Anbieter bestätigt hat, dass die Nachricht an die Zielrufnummer zugestellt wurde.
{% endif %}

{% if include.metric == "Confidence" %}
Die <i>Konfidenz</i> ist der Prozentsatz des Vertrauens, dass eine bestimmte Variante einer Nachricht besser abschneidet als die Kontrollgruppe.
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
<i>Bestätigungsseite Schaltfläche</i> ist die Gesamtzahl der Klicks auf die Schaltfläche mit der Aufforderung zum Handeln auf der Bestätigungsseite einer <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
<i>Bestätigungsseite Ausblendungen</i> ist die Gesamtzahl der Klicks auf den Button „Schließen“ (x) auf der Bestätigungsseite einer <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Conversion Rate" %}
<i>Die Konversionsrate</i> ist der Prozentsatz der Häufigkeit eines bestimmten Ereignisses im Vergleich zu allen Empfängern einer Nachricht. Dieses definierte Event wird festgelegt, wenn Sie die Kampagne erstellen.
{% endif %}

{% if include.metric == "Conversion Window" %}
Das <i>Konversionsfenster</i> zeigt die Anzahl der Tage nach Erhalt der Nachricht, in denen die Aktionen des Benutzers verfolgt und einem Konversions-Event zugeordnet werden. Konversionen, die nach diesem Fenster stattfinden, werden nicht dem Konversions-Event zugeschrieben.
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
<i>Konversionen (B, C, D)</i> sind zusätzliche Konversions-Events, die nach dem primären Konversions-Event hinzugefügt werden. Dies ist die Anzahl der Male, die ein definiertes Ereignis nach der Interaktion mit oder dem Betrachten einer empfangenen Nachricht aus einer Braze-Kampagne eingetreten ist.
{% endif %}

{% if include.metric == "Total Conversions" %}
Die <i>Gesamtzahl der Konversionen</i> ist die Gesamtzahl der Fälle, in denen ein Nutzer ein bestimmtes Konversions-Event abschließt, nachdem er eine In-App-Nachrichtenkampagne gesehen hat.
{% endif %}

{% if include.metric == "Deliveries" %}
<i>Zustellungen</i> ist die Gesamtzahl der Nachrichtenanfragen, die vom empfangenden Server angenommen wurden. Das bedeutet nicht, dass die Nachricht an ein Gerät zugestellt wurde, sondern nur, dass die Nachricht vom Server akzeptiert wurde.
{% endif %}

{% if include.metric == "Deliveries %" %}
<i>Zustellungen %</i> ist der prozentuale Anteil an der Gesamtzahl der Nachrichten (Sendungen), die erfolgreich an Empfänger gesendet und von diesen empfangen wurden.
{% endif %}

{% if include.metric == "Delivery Failures" %}
<i>Von Zustellungsfehlern</i> spricht man, wenn die SMS nicht versendet werden konnte, weil die Warteschlangen überfüllt waren (Versand von SMS mit einer höheren Rate, als Ihre Lang- oder Kurzcodes verarbeiten können).
{% endif %}

{% if include.metric == "Delivery Failures RCS" %}
<i>Zustellungsfehler</i> liegen vor, wenn der RCS nicht gesendet werden konnte, weil die Warteschlangen überlaufen sind (RCS werden mit einer höheren Rate gesendet, als Ihr RCS-überprüfter Sender verarbeiten kann).
{% endif %}

{% if include.metric == "Failed Delivery Rate" %}
Die <i>Rate der fehlgeschlagenen Zustellungen</i> ist der Prozentsatz der Sendungen, die fehlgeschlagen sind, weil die Nachricht nicht zugestellt werden konnte. Dafür kann es verschiedene Gründe geben, z. B. Überläufe in der Warteschlange, Kontosperrungen und Medienfehler bei MMS.
{% endif %}

{% if include.metric == "Direct Opens" %}
<i>Direkte Öffnungen</i> ist die Gesamtzahl der Nutzer:innen, die Ihre App oder Website durch direktes Drücken der Benachrichtigung geöffnet haben.
{% endif %}

{% if include.metric == "Emailable" %}
<i>Erreichbar</i> ist die Gesamtzahl der Nutzer, die über eine E-Mail-Adresse verfügen und sich explizit angemeldet oder abonniert haben.
{% endif %}

{% if include.metric == "Errors" %}
<i>Fehler</i> ist die Anzahl der von Webhook-Events zurückgegebenen Fehler (wird während des Sendevorgangs erhöht).
{% endif %}

{% if include.metric == "Failures" %}
<i>Misserfolge</i> sind, wenn die WhatsApp-Nachricht nicht gesendet werden konnte, weil der Internet-Provider einen Hard Bounce zurückgegeben hat. Ein Hard Bounce bedeutet einen dauerhaften Zustellbarkeitsfehler.
{% endif %}

{% if include.metric == "Influenced Opens" %}
<i>Beeinflusste Öffnungen</i> ist die Gesamtzahl (und der Prozentsatz) der Nutzer, die die App geöffnet haben, nachdem die Push-Benachrichtigung gesendet wurde, ohne die Push-Nachricht direkt zu öffnen.
{% endif %}

{% if include.metric == "Lifetime Revenue" %}
<i>Lifetime-Umsatz</i> ist der <code>PurchaseEvents</code> Gesamtpreiswert (in USD), der seit der Auflegung eingenommen wurde.
{% endif %}

{% if include.metric == "Lifetime Value Per User" %}
Der <i>Lifetime-Value pro Nutzer</i> ist der <i>Lifetime-Umsatz</i> geteilt durch Ihre gesamten <i>Nutzer</i>:innen (an den Standorten Ihrer Homepage).
{% endif %}

{% if include.metric == "Average Daily Revenue" %}
<i>Der durchschnittliche Tagesumsatz</i> ist der Durchschnitt der Summe der Kampagnen- und Canvas-Einnahmen für einen bestimmten Tag.
{% endif %}

{% if include.metric == "Daily Purchases" %}
<i>Tägliche Käufe</i> ist der Durchschnitt der gesamten einzigartigen <code>PurchaseEvents</code> im Laufe des Zeitraums.
{% endif %}

{% if include.metric == "Daily Revenue Per User" %}
Der <i>Tagesumsatz pro Benutzer</i> ist der durchschnittliche Tagesumsatz pro täglich aktivem Benutzer.
{% endif %}

{% if include.metric == "Machine Opens" %}
<i>Automatische Öffnungen</i> beinhaltet den Anteil der „Öffnungen“, die von Apples Mail Privacy Protection (MPP) für iOS 15 betroffen sind. Wenn ein Benutzer zum Beispiel eine E-Mail mit der Mail-App auf einem Apple-Gerät öffnet, wird dies als <i>Automatische Öffnungen</i> protokolliert.
{% endif %}

{% if include.metric == "Other Opens" %}
<i>Andere Öffnungen</i> umfasst E-Mails, die nicht als <i>Automatische Öffnungen</i> identifiziert wurden. Wenn ein Benutzer beispielsweise eine E-Mail auf einer anderen Plattform öffnet (z. B. Gmail-App auf einem Telefon, Gmail auf einem Desktop-Browser), wird dies als <i>"Andere Öffnungen</i>" protokolliert.
{% endif %}

{% if include.metric == "Opens" %}
<i>Öffnungen</i> sind sowohl <i>direkte Öffnungen</i> als auch <i>beeinflusste Öffnungen</i>, bei denen das Braze SDK mithilfe eines proprietären Algorithmus festgestellt hat, dass eine Push-Benachrichtigung einen Benutzer zum Öffnen der App veranlasst hat.
{% endif %}

{% if include.metric == "Opt-Out" %}
<i>Opt-Out</i> liegt vor, wenn ein Nutzer:innen auf Ihre Nachricht mit einem <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">Opt-Out-Schlüsselwort</a> geantwortet hat und sich von Ihrem SMS- oder RCS-Programm abgemeldet hat.
{% endif %}

{% if include.metric == "Pending Retry" %}
<i>Pending Retry</i> ist die Anzahl der Anfragen, die vom empfangenden Server vorübergehend abgelehnt wurden, bei denen der E-Mail-Dienstanbieter (ESP) aber dennoch versucht hat, sie erneut zuzustellen. Der ESP versucht die Zustellung so lange zu wiederholen, bis eine Timeout-Periode erreicht ist (normalerweise nach 72 Stunden).
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
<i>Primäre Conversions (A)</i> oder <i>primäres Conversion-Ereignis</i> ist die Anzahl der Male, die ein definiertes Ereignis nach der Interaktion mit oder dem Betrachten einer empfangenen Nachricht aus einer Braze-Kampagne eingetreten ist. Dieses definierte Event wird von Ihnen bei der Erstellung der Kampagne festgelegt.
{% endif %}

{% if include.metric == "Reads" %}
<i>Gelesen</i> ist, wenn der Nutzer:innen die Nachricht liest. Die Lesebestätigungen des Benutzers müssen aktiviert sein, damit Braze die Lesevorgänge verfolgen kann.
{% endif %}

{% if include.metric == "Read Rate" %}
Die <i>Leserate</i> ist der Prozentsatz der Sendungen, die zu einem Lesevorgang führten. Dies ist nur für Nutzer:innen möglich, die Lesebestätigungen aktiviert haben.
{% endif %}

{% if include.metric == "Received" %}
Der <i>Empfang</i> wird je nach Kanal unterschiedlich definiert und kann erfolgen, wenn Benutzer die Nachricht ansehen, wenn Benutzer eine definierte Auslöseaktion ausführen oder wenn die Nachricht an den Nachrichtenanbieter gesendet wird.
{% endif %}

{% if include.metric == "Rejections" %}
<i>Ablehnungen</i> liegen vor, wenn die SMS oder RCS vom Netzbetreiber abgelehnt wurde. Dies kann verschiedene Gründe haben, z. B. die Filterung von Inhalten durch den Anbieter, die Verfügbarkeit des Zielgeräts, die Telefonnummer ist nicht mehr in Betrieb und ähnliches.
{% endif %}

{% if include.metric == "Revenue" %}
Der <i>Umsatz</i> ist der Gesamtumsatz in Dollar von Kampagnenempfängern innerhalb des festgelegten <a href='/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events'>primären Konversionsfensters</a>.
{% endif %}

{% if include.metric == "Messages Sent" %}
<i>Gesendete Nachrichten</i> ist die Gesamtzahl der gesendeten Nachrichten in einer Kampagne. Nach dem Start einer geplanten Kampagne umfasst diese Metrik alle gesendeten Nachrichten, unabhängig davon, ob sie aufgrund der Ratenbegrenzung bereits versendet wurden. Das bedeutet nicht, dass die Nachricht empfangen oder an ein Gerät zugestellt wurde, sondern nur, dass die Nachricht gesendet wurde.
{% endif %}

{% if include.metric == "Sent" %}
<i>Gesendet</i> wird jedes Mal, wenn eine Kampagne oder ein Canvas-Schritt gestartet oder getriggert wurde und eine SMS oder RCS von Braze gesendet wurde. Es ist möglich, dass die SMS oder RCS das Gerät eines Nutzer:innen aufgrund von Fehlern nicht erreicht hat.
{% endif %}

{% if include.metric == "Sends" %}
<i>Sendungen</i> ist die Gesamtzahl der gesendeten Nachrichten in einer Kampagne. Nach dem Start einer geplanten Kampagne umfasst diese Metrik alle gesendeten Nachrichten, unabhängig davon, ob sie aufgrund der Ratenbegrenzung bereits versendet wurden. Das bedeutet nicht, dass die Nachricht empfangen oder an ein Gerät zugestellt wurde, sondern nur, dass die Nachricht gesendet wurde.
{% endif %}

{% if include.metric == "Sends to Carrier" %}
<i>Sendungen an Netzbetreiber</i> ist veraltet, wird aber für Benutzer, die es bereits haben, weiterhin unterstützt. Es handelt sich um die Summe der <i>Bestätigten Zustellungen</i>, <i>Ablehnungen</i> und <i>Sendungen</i>, bei denen die Zustellung oder Ablehnung nicht vom Zusteller bestätigt wurde. Dies gilt auch für Fälle, in denen Zusteller keine Zustell- oder Ablehnungsbestätigung liefern, da einige Zusteller diese Bestätigung nicht liefern oder zum Zeitpunkt des Versands nicht liefern können.
{% endif %}

{% if include.metric == "Sends to Carrier Rate" %}
<i>Die Rate der an den Netzbetreiber gesendeten Nachrichten</i> ist der Prozentsatz der insgesamt gesendeten Nachrichten, die als <i>an den Netzbetreiber gesendete Nachrichten</i> eingestuft wurden. Dies gilt auch für Instanzen, in denen Zustellungen oder Ablehnungen nicht bestätigt werden, da einige Spediteure diese Bestätigung nicht liefern oder zum Zeitpunkt der Sendung nicht liefern können. Diese Metrik ist veraltet, wird aber für Nutzer:innen, die sie bereits haben, weiterhin unterstützt.
{% endif %}

{% if include.metric == "Spam" %}
<i>Spam</i> ist die Gesamtzahl der zugestellten E-Mails, die vom Empfänger:in als "Spam" markiert wurden. Braze ändert zwar nicht den Abo-Status dieser Nutzer:innen, aber diese Nutzer:innen werden in zukünftigen E-Mails automatisch ausgeschlossen, es sei denn, Sie senden eine Transaktions-E-Mail, die so konfiguriert ist, dass sie an alle Nutzer:innen gesendet wird, einschließlich Abmelden.
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
<i>Umfrageseitenausblendungen</i> ist die Gesamtzahl der Klicks auf den Button „Schließen“ (x) auf der Seite mit den Umfragefragen einer <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Survey Submissions" %}
<i>Umfrageübermittlungen</i> ist die Gesamtzahl der Klicks auf den Button „Senden“ einer <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Total Clicks" %}
<i>Klicks insgesamt</i> ist die Anzahl eindeutiger Empfänger:innen, die auf einen Link in der zugestellten Nachricht geklickt haben.
{% endif %}

{% if include.metric == "Total Dismissals" %}
<i>Ausblendungen insgesamt</i> ist die Anzahl der Ablehnungen von Content-Cards aus einer Kampagne.
{% endif %}

{% if include.metric == "Total Impressions" %}
<i>Die Impressionen insgesamt</i> geben an, wie oft eine Nachricht angesehen wurde. Braze protokolliert eine Impression erst, wenn die Nachricht für die Nutzer:innen auf ihrem Bildschirm sichtbar wird. Wenn beispielsweise eine Nachricht am unteren Ende einer Seite platziert ist, wird die Impression erst protokolliert, wenn der Nutzer:innen nach unten scrollt und die Nachricht zu sehen ist. Wenn einem Nutzer:innen dieselbe Nachricht zweimal angezeigt wird, zählt dies als zwei Impressionen.
{% endif %}

{% if include.metric == "Total Opens" %}
<i>Öffnungen gesamt</i> ist die Gesamtzahl der Nachrichten, die geöffnet wurden.
{% endif %}

{% if include.metric == "Total Revenue" %}
<i>Gesamtumsatz</i> ist der Gesamtumsatz in Dollar von Kampagnenempfängern innerhalb des festgelegten primären Umrechnungsfensters.
{% endif %}

{% if include.metric == "Unique Clicks" %}
<i>Eindeutige Klicks</i> ist die eindeutige Anzahl von Empfängern, die mindestens einmal auf einen Link in einer Nachricht geklickt haben und wird durch <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a> gemessen.
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>Unique Dismissals</i> ist die Anzahl der eindeutigen Empfänger:innen, die eine Content-Card aus einer Kampagne entlassen haben. Ein Benutzer, der eine Content-Card aus einer Kampagne mehrmals ausblendet, stellt eine eindeutige Ausblendung dar.
{% endif %}

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

{% if include.metric == "Unique Impressions" %}
<i>Eindeutige Impressionen</i> ist die Gesamtzahl der Nutzer:innen, die eine Nachricht aus einer bestimmten Kampagne angesehen haben. Eine Impression wird erst protokolliert, wenn die Nachricht auf dem Bildschirm eines Nutzers:innen sichtbar wird.
{% endif %}

{% if include.metric == "Unique Recipients" %}
<i>Eindeutige Empfänger:innen</i> ist die Anzahl der eindeutigen täglichen Empfänger:innen, also der Nutzer:innen, die an einem Tag eine neue Nachricht erhalten haben. Damit diese Zahl für einen Nutzer:innen mehr als einmal erhöht wird, muss der Nutzer:innen eine neue Nachricht an einem anderen Tag erhalten.
{% endif %}

{% if include.metric == "Unique Opens" %}
<i>Unique Opens</i> ist die Gesamtzahl der zugestellten Nachrichten, die von einem einzelnen Nutzer mindestens einmal geöffnet wurden und über einen Zeitraum von sieben Tagen verfolgt werden.
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
<i>Unsubscribers</i> oder <i>Unsub</i> ist die Anzahl der Nachrichten, die zu einer Abmeldung führen. Abmeldungen erfolgen, wenn ein Benutzer auf den Braze Abmeldelink klickt.
{% endif %}

{% if include.metric == "Unsubscribes" %}
<i>Abbestellungen</i> ist die Anzahl der Empfänger, deren Abonnementstatus sich in „Abbestellt“ geändert hat, nachdem sie auf die von Braze bereitgestellte Abmeldungs-URL geklickt haben.
{% endif %}

{% if include.metric == "Variation" %}
<i>Variation</i> ist die Anzahl der Variationen einer Kampagne, die sich nach den Vorgaben des Erstellers unterscheiden.
{% endif %}
