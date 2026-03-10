{% if include.metric == "AMP Clicks" %}
<i>AMP-Klicks</i> ist die Gesamtzahl der Klicks in Ihrer AMP-HTML-E-Mail, kumuliert aus der HTML-, Klartext- und AMP-HTML-Version der E-Mail.
{% endif %}

{% if include.metric == "AMP Opens" %}
<i>AMP-Öffnungen</i> ist die Gesamtzahl der Öffnungen in Ihrer AMP-HTML-E-Mail und den AMP-HTML-Versionen der E-Mail.
{% endif %}

{% if include.metric == "Audience" %}
Die <i>Zielgruppe</i> ist der Prozentsatz der Nutzer:innen, die eine bestimmte Nachricht erhalten haben. Diese Zahl wird von Braze bereitgestellt.
{% endif %}

{% if include.metric == "Bounces" %}
<i>Bounces</i> ist die Gesamtzahl der Nachrichten, die nicht erfolgreich an die vorgesehenen Empfänger:innen zugestellt werden konnten.
{% endif %}

{% if include.metric == "Estimated Real Opens" %}
Die <i>geschätzten realen Öffnungen</i> sind eine Schätzung der Anzahl der eindeutigen Öffnungen, die es geben würde, wenn es keine maschinellen Öffnungen gäbe, und sind das Ergebnis eines proprietären statistischen Modells von Braze.
{% endif %}

{% if include.metric == "Help" %}
<i>Hilfe</i> bedeutet, dass ein:e Nutzer:in auf Ihre Nachricht mit dem <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">Schlüsselwort HILFE</a> geantwortet hat und eine automatische HILFE-Antwort erhalten hat.
{% endif %}

{% if include.metric == "Hard Bounce" %}
Ein <i>Hard Bounce</i> liegt vor, wenn eine E-Mail aufgrund eines dauerhaften Zustellungsfehlers nicht an den/die Empfänger:in zugestellt werden kann. Ein Hard Bounce kann auftreten, weil der Domain-Name nicht existiert oder weil der/die Empfänger:in unbekannt ist.
{% endif %}

{% if include.metric == "Soft Bounce" %}
Ein <i>Soft Bounce</i> liegt vor, wenn eine E-Mail aufgrund eines vorübergehenden Zustellungsfehlers nicht an den/die Empfänger:in zugestellt werden kann, obwohl die E-Mail-Adresse des/der Empfänger:in gültig ist. Ein Soft Bounce kann auftreten, weil der Posteingang des/der Empfänger:in voll ist, der Server ausgefallen ist oder die Nachricht zu groß für den Posteingang des/der Empfänger:in war.
{% endif %}

{% if include.metric == "Deferral" %}
Eine <i>Zurückstellung</i> liegt vor, wenn eine E-Mail nicht sofort zugestellt werden konnte. Braze versucht jedoch, die E-Mail bis zu 72 Stunden nach diesem vorübergehenden Zustellungsfehler erneut zuzustellen, um die Chancen auf eine erfolgreiche Zustellung zu maximieren, bevor die Versuche für diese spezifische Kampagne eingestellt werden.
{% endif %}

{% if include.metric == "Body Click" %}
Push-Story-Benachrichtigungen zeichnen einen <i>Body Click</i> auf, wenn die Benachrichtigung angeklickt wird. Er wird nicht aufgezeichnet, wenn eine Nachricht erweitert oder ein Aktions-Button angeklickt wird.
{% endif %}

{% if include.metric == "Body Clicks" %}
<i>Body Clicks</i> treten auf, wenn ein:e Nutzer:in auf eine Nachricht klickt, die keine Buttons (Button 1, Button 2) hat und mit dem traditionellen Editor erstellt wurde, und wenn eine Nachricht, die mit dem HTML-Editor oder dem Drag-and-Drop-Editor erstellt wurde, <code>brazeBridge.logClick()</code> ohne Argumente verwendet.
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
<i>Button-1-Klicks</i> ist die Gesamtzahl der Klicks auf Button 1 der Nachricht.
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>Button-2-Klicks</i> ist die Gesamtzahl der Klicks auf Button 2 der Nachricht.
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>Eingereichte Auswahlen</i> ist die Gesamtzahl der ausgewählten Optionen, wenn der/die Nutzer:in auf der Seite mit den Umfragefragen einer <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a> auf den Senden-Button klickt.
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
Die <i>Klick-zu-Öffnen-Rate</i> ist der Prozentsatz der zugestellten E-Mails, die von einem/einer einzelnen Nutzer:in oder einer Maschine mindestens einmal geöffnet wurden, und ist nur im <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>Berichts-Builder</a> verfügbar.
{% endif %}

{% if include.metric == "Close Message" %}
<i>Nachricht schließen</i> ist die Gesamtzahl der Klicks auf den Schließen-Button der Nachricht. Dies gilt nur für In-App-Nachrichten, die mit dem Drag-and-Drop-Editor erstellt wurden, nicht mit dem traditionellen Editor.
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
<i>Bestätigte Zustellungen</i> liegen vor, wenn der Anbieter bestätigt hat, dass die Nachricht an die Zielrufnummer zugestellt wurde.
{% endif %}

{% if include.metric == "Confidence" %}
Die <i>Konfidenz</i> ist der Prozentsatz der Wahrscheinlichkeit, dass eine bestimmte Variante einer Nachricht besser abschneidet als die Kontrollgruppe.
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
<i>Bestätigungsseiten-Button</i> ist die Gesamtzahl der Klicks auf den Call-to-Action-Button auf der Bestätigungsseite einer <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
<i>Bestätigungsseiten-Ausblendungen</i> ist die Gesamtzahl der Klicks auf den Schließen-Button (x) auf der Bestätigungsseite einer <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Conversion Rate" %}
Die <i>Konversionsrate</i> ist der Prozentsatz der Häufigkeit, mit der ein definiertes Event im Vergleich zu allen Empfänger:innen einer Nachricht eingetreten ist. Dieses definierte Event wird festgelegt, wenn Sie die Kampagne erstellen.
{% endif %}

{% if include.metric == "Conversion Window" %}
Das <i>Konversionsfenster</i> ist die Anzahl der Tage nach Erhalt der Nachricht, in denen die Aktionen der Nutzer:innen verfolgt und einem Konversions-Event zugeordnet werden. Konversionen, die nach diesem Fenster stattfinden, werden nicht dem Konversions-Event zugeschrieben.
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
<i>Konversionen (B, C, D)</i> sind zusätzliche Konversions-Events, die nach dem primären Konversions-Event hinzugefügt werden. Dies ist die Anzahl der Male, die ein definiertes Event nach der Interaktion mit oder dem Betrachten einer empfangenen Nachricht aus einer Braze-Kampagne eingetreten ist.
{% endif %}

{% if include.metric == "Total Conversions" %}
Die <i>Gesamtzahl der Konversionen</i> ist die Gesamtzahl der Fälle, in denen ein:e Nutzer:in ein bestimmtes Konversions-Event abschließt, nachdem er/sie eine In-App-Nachrichtenkampagne gesehen hat.
{% endif %}

{% if include.metric == "Deliveries" %}
<i>Zustellungen</i> ist die Gesamtzahl der Nachrichtenanfragen, die vom empfangenden Server angenommen wurden. Das bedeutet nicht, dass die Nachricht an ein Gerät zugestellt wurde, sondern nur, dass die Nachricht vom Server akzeptiert wurde.
{% endif %}

{% if include.metric == "Deliveries %" %}
<i>Zustellungen %</i> ist der prozentuale Anteil an der Gesamtzahl der Nachrichten (Sendungen), die erfolgreich an E-Mail-fähige Empfänger:innen gesendet und von diesen empfangen wurden.
{% endif %}

{% if include.metric == "Delivery Failures" %}
<i>Zustellungsfehler</i> treten auf, wenn die SMS nicht versendet werden konnte, weil die Warteschlangen überfüllt waren (Versand von SMS mit einer höheren Rate, als Ihre Lang- oder Shortcodes verarbeiten können).
{% endif %}

{% if include.metric == "Delivery Failures RCS" %}
<i>Zustellungsfehler</i> treten auf, wenn die RCS nicht gesendet werden konnte, weil die Warteschlangen überlaufen sind (RCS werden mit einer höheren Rate gesendet, als Ihr RCS-verifizierter Sender verarbeiten kann).
{% endif %}

{% if include.metric == "Failed Delivery Rate" %}
Die <i>Rate der fehlgeschlagenen Zustellungen</i> ist der Prozentsatz der Sendungen, die fehlgeschlagen sind, weil die Nachricht nicht zugestellt werden konnte. Dafür kann es verschiedene Gründe geben, z. B. Überläufe in der Warteschlange, Kontosperrungen und Medienfehler bei MMS.
{% endif %}

{% if include.metric == "Direct Opens" %}
<i>Direkte Öffnungen</i> ist die Gesamtzahl der Nutzer:innen, die Ihre App oder Website durch direktes Drücken der Benachrichtigung geöffnet haben.
{% endif %}

{% if include.metric == "Emailable" %}
<i>E-Mail-erreichbar</i> ist die Gesamtzahl der Nutzer:innen, die über eine E-Mail-Adresse verfügen und sich explizit angemeldet oder abonniert haben.
{% endif %}

{% if include.metric == "Errors" %}
<i>Fehler</i> ist die Anzahl der von Webhook-Events zurückgegebenen Fehler (wird während des Sendevorgangs erhöht).
{% endif %}

{% if include.metric == "Failures" %}
<i>Fehlschläge</i> treten auf, wenn die WhatsApp-Nachricht nicht gesendet werden konnte, weil der Internet-Provider einen Hard Bounce zurückgegeben hat. Ein Hard Bounce bedeutet einen dauerhaften Zustellbarkeitsfehler.
{% endif %}

{% if include.metric == "Influenced Opens" %}
<i>Beeinflusste Öffnungen</i> ist die Gesamtzahl (und der Prozentsatz) der Nutzer:innen, die die App geöffnet haben, nachdem die Push-Benachrichtigung gesendet wurde, ohne die Push-Nachricht direkt zu öffnen.
{% endif %}

{% if include.metric == "Lifetime Revenue" %}
<i>Lifetime-Umsatz</i> ist der gesamte <code>PurchaseEvents</code>-Preiswert (in USD), der seit der Einführung eingenommen wurde.
{% endif %}

{% if include.metric == "Lifetime Value Per User" %}
Der <i>Lifetime-Value pro Nutzer:in</i> ist der <i>Lifetime-Umsatz</i> geteilt durch Ihre gesamten <i>Nutzer:innen</i> (auf Ihrer Startseite).
{% endif %}

{% if include.metric == "Average Daily Revenue" %}
Der <i>durchschnittliche Tagesumsatz</i> ist der Durchschnitt der Summe der Kampagnen- und Canvas-Umsätze für einen bestimmten Tag.
{% endif %}

{% if include.metric == "Daily Purchases" %}
<i>Tägliche Käufe</i> ist der Durchschnitt der gesamten eindeutigen <code>PurchaseEvents</code> über den Zeitraum.
{% endif %}

{% if include.metric == "Daily Revenue Per User" %}
Der <i>Tagesumsatz pro Nutzer:in</i> ist der durchschnittliche Tagesumsatz pro täglich aktive:r Nutzer:in.
{% endif %}

{% if include.metric == "Machine Opens" %}
<i>Automatische Öffnungen</i> beinhaltet den Anteil der „Öffnungen", die von Apples E-Mail-Datenschutz (MPP) für iOS 15 betroffen sind. Wenn ein:e Nutzer:in zum Beispiel eine E-Mail mit der Mail-App auf einem Apple-Gerät öffnet, wird dies als <i>Automatische Öffnungen</i> protokolliert.
{% endif %}

{% if include.metric == "Other Opens" %}
<i>Andere Öffnungen</i> umfasst E-Mails, die nicht als <i>Automatische Öffnungen</i> identifiziert wurden. Wenn ein:e Nutzer:in beispielsweise eine E-Mail auf einer anderen Plattform öffnet (z. B. Gmail-App auf einem Telefon, Gmail auf einem Desktop-Browser), wird dies als <i>Andere Öffnungen</i> protokolliert.
{% endif %}

{% if include.metric == "Opens" %}
<i>Öffnungen</i> sind Instanzen, die sowohl <i>direkte Öffnungen</i> als auch <i>beeinflusste Öffnungen</i> umfassen, bei denen das Braze SDK mithilfe eines proprietären Algorithmus festgestellt hat, dass eine Push-Benachrichtigung eine:n Nutzer:in zum Öffnen der App veranlasst hat.
{% endif %}

{% if include.metric == "Opt-Out" %}
<i>Opt-Out</i> liegt vor, wenn ein:e Nutzer:in auf Ihre Nachricht mit einem <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">Opt-Out-Schlüsselwort</a> geantwortet hat und sich von Ihrem SMS- oder RCS-Programm abgemeldet hat.
{% endif %}

{% if include.metric == "Pending Retry" %}
<i>Ausstehender Wiederholungsversuch</i> ist die Anzahl der Anfragen, die vom empfangenden Server vorübergehend abgelehnt wurden, bei denen der E-Mail-Anbieter (ESP) aber dennoch versucht hat, sie erneut zuzustellen. Der ESP versucht die Zustellung so lange zu wiederholen, bis eine Timeout-Periode erreicht ist (normalerweise nach 72 Stunden).
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
<i>Primäre Konversionen (A)</i> oder <i>primäres Konversions-Event</i> ist die Anzahl eindeutiger Nutzer:innen, die ein definiertes Event ausführen, nachdem sie eine Nachricht aus einer Braze-Kampagne erhalten oder angesehen haben. Dieses Event wird von Ihnen ausgewählt, wenn Sie die Kampagne einrichten, und wird als primäre Erfolgsmetrik für die Berichterstattung und Optimierung verwendet.
{% endif %}

{% if include.metric == "Reads" %}
<i>Gelesen</i> ist, wenn der/die Nutzer:in die Nachricht liest. Die Lesebestätigungen des/der Nutzer:in müssen aktiviert sein, damit Braze die Lesevorgänge verfolgen kann.
{% endif %}

{% if include.metric == "Read Rate" %}
Die <i>Leserate</i> ist der Prozentsatz der Sendungen, die zu einem Lesevorgang führten. Dies gilt nur für Nutzer:innen, die Lesebestätigungen aktiviert haben.
{% endif %}

{% if include.metric == "Received" %}
<i>Erhalten</i> wird je nach Kanal unterschiedlich definiert und kann erfolgen, wenn Nutzer:innen die Nachricht ansehen, Nutzer:innen eine definierte Trigger-Aktion ausführen oder die Nachricht an den Nachrichtenanbieter gesendet wird.
{% endif %}

{% if include.metric == "Rejections" %}
<i>Ablehnungen</i> liegen vor, wenn die SMS oder RCS vom Netzbetreiber abgelehnt wurde. Dies kann verschiedene Gründe haben, z. B. die Filterung von Inhalten durch den Anbieter, die Verfügbarkeit des Zielgeräts, die Telefonnummer ist nicht mehr in Betrieb und ähnliches.
{% endif %}

{% if include.metric == "Revenue" %}
Der <i>Umsatz</i> ist der Gesamtumsatz in Dollar von Kampagnenempfänger:innen innerhalb des festgelegten <a href='/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events'>primären Konversionsfensters</a>.
{% endif %}

{% if include.metric == "Messages Sent" %}
<i>Gesendete Nachrichten</i> ist die Gesamtzahl der gesendeten Nachrichten in einer Kampagne. Nach dem Start einer geplanten Kampagne umfasst diese Metrik alle gesendeten Nachrichten, unabhängig davon, ob sie aufgrund von Rate-Limiting bereits versendet wurden. Das bedeutet nicht, dass die Nachricht empfangen oder an ein Gerät zugestellt wurde, sondern nur, dass die Nachricht gesendet wurde.
{% endif %}

{% if include.metric == "Sent" %}
<i>Gesendet</i> wird jedes Mal gezählt, wenn eine Kampagne oder ein Canvas-Schritt gestartet oder getriggert wurde und eine SMS oder RCS von Braze gesendet wurde. Es ist möglich, dass die SMS oder RCS das Gerät eines/einer Nutzer:in aufgrund von Fehlern nicht erreicht hat.
{% endif %}

{% if include.metric == "Sends" %}
<i>Sendungen</i> ist die Gesamtzahl der gesendeten Nachrichten in einer Kampagne. Nach dem Start einer geplanten Kampagne umfasst diese Metrik alle gesendeten Nachrichten, unabhängig davon, ob sie aufgrund von Rate-Limiting bereits versendet wurden. Das bedeutet nicht, dass die Nachricht empfangen oder an ein Gerät zugestellt wurde, sondern nur, dass die Nachricht gesendet wurde.
{% endif %}

{% if include.metric == "Sends to Carrier" %}
<i>Sendungen an Netzbetreiber</i> ist veraltet, wird aber für Nutzer:innen, die es bereits haben, weiterhin unterstützt. Es handelt sich um die Summe der <i>Bestätigten Zustellungen</i>, <i>Ablehnungen</i> und <i>Sendungen</i>, bei denen die Zustellung oder Ablehnung nicht vom Netzbetreiber bestätigt wurde. Dies umfasst auch Fälle, in denen Netzbetreiber keine Zustell- oder Ablehnungsbestätigung liefern, da einige Netzbetreiber diese Bestätigung nicht liefern oder zum Zeitpunkt des Versands nicht liefern können.
{% endif %}

{% if include.metric == "Sends to Carrier Rate" %}
Die <i>Rate der Sendungen an Netzbetreiber</i> ist der Prozentsatz der insgesamt gesendeten Nachrichten, die als <i>Sendungen an Netzbetreiber</i> eingestuft wurden. Dies umfasst auch Instanzen, in denen Netzbetreiber keine Zustell- oder Ablehnungsbestätigung liefern, da einige Netzbetreiber diese Bestätigung nicht liefern oder zum Zeitpunkt des Versands nicht liefern können. Diese Metrik ist veraltet, wird aber für Nutzer:innen, die sie bereits haben, weiterhin unterstützt.
{% endif %}

{% if include.metric == "Spam" %}
<i>Spam</i> ist die Gesamtzahl der zugestellten E-Mails, die vom/von der Empfänger:in als „Spam" markiert wurden. Braze ändert zwar nicht den Abo-Status dieser Nutzer:innen, aber diese Nutzer:innen werden in zukünftigen E-Mails automatisch ausgeschlossen, es sei denn, Sie senden eine Transaktions-E-Mail, die so konfiguriert ist, dass sie „an alle Nutzer:innen gesendet wird, einschließlich Abgemeldete".
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
<i>Umfrageseiten-Ausblendungen</i> ist die Gesamtzahl der Klicks auf den Schließen-Button (x) auf der Seite mit den Umfragefragen einer <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Survey Submissions" %}
<i>Umfrage-Übermittlungen</i> ist die Gesamtzahl der Klicks auf den Senden-Button einer <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Total Clicks" %}
<i>Klicks insgesamt</i> ist die Anzahl eindeutiger Empfänger:innen, die auf einen Link in der zugestellten Nachricht geklickt haben.
{% endif %}

{% if include.metric == "Total Dismissals" %}
<i>Ausblendungen insgesamt</i> ist die Anzahl der Ausblendungen von Content-Cards aus einer Kampagne.
{% endif %}

{% if include.metric == "Total Impressions" %}
Die <i>Gesamtzahl der Impressionen</i> gibt an, wie oft die Nachricht geladen wurde und auf dem Bildschirm eines/einer Nutzer:in erschienen ist, unabhängig von vorheriger Interaktion (wenn einem/einer Nutzer:in beispielsweise eine Nachricht zweimal angezeigt wird, wird sie zweimal gezählt).
{% endif %}

{% if include.metric == "Total Opens" %}
<i>Öffnungen gesamt</i> ist die Gesamtzahl der Nachrichten, die geöffnet wurden.
{% endif %}

{% if include.metric == "Total Revenue" %}
<i>Gesamtumsatz</i> ist der Gesamtumsatz in Dollar von Kampagnenempfänger:innen innerhalb des festgelegten primären Konversionsfensters.
{% endif %}

{% if include.metric == "Unique Clicks" %}
<i>Eindeutige Klicks</i> ist die eindeutige Anzahl von Empfänger:innen, die mindestens einmal auf einen Link in einer Nachricht geklickt haben, und wird gemessen durch <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>.
{% endif %}

<!-- Pull channels like Banners that don't have a Dispatch ID-->
{% if include.metric == "Unique Clicks No Dispatch ID" %}
<i>Eindeutige Klicks</i> ist die eindeutige Anzahl von Empfänger:innen, die mindestens einmal auf einen Link innerhalb einer Nachricht geklickt haben.
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>Eindeutige Ausblendungen</i> ist die Anzahl der eindeutigen Empfänger:innen, die eine Content-Card aus einer Kampagne ausgeblendet haben. Ein:e Nutzer:in, der/die eine Content-Card aus einer Kampagne mehrmals ausblendet, stellt eine eindeutige Ausblendung dar.
{% endif %}

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

{% if include.metric == "Unique Impressions" %}
<i>Eindeutige Impressionen</i> ist die Gesamtzahl der Nutzer:innen, die eine Nachricht aus einer bestimmten Kampagne erhalten und angesehen haben.
{% endif %}

{% if include.metric == "Unique Recipients" %}
<i>Eindeutige Empfänger:innen</i> ist die Anzahl der eindeutigen täglichen Empfänger:innen, also der Nutzer:innen, die an einem Tag eine neue Nachricht erhalten haben. Damit diese Zahl für eine:n Nutzer:in mehr als einmal erhöht wird, muss der/die Nutzer:in eine neue Nachricht an einem anderen Tag erhalten.
{% endif %}

{% if include.metric == "Unique Opens" %}
<i>Eindeutige Öffnungen</i> ist die Gesamtzahl der zugestellten Nachrichten, die von einem/einer einzelnen Nutzer:in mindestens einmal geöffnet wurden und über einen Zeitraum von sieben Tagen verfolgt werden.
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
<i>Abmelder:innen</i> oder <i>Abmeldungen</i> ist die Anzahl der Nachrichten, die zu einer Abmeldung führen. Abmeldungen erfolgen, wenn ein:e Nutzer:in auf den Braze-Abmeldelink klickt.
{% endif %}

{% if include.metric == "Unsubscribes" %}
<i>Abmeldungen</i> ist die Anzahl der Empfänger:innen, deren Abo-Status sich in „Abgemeldet" geändert hat, nachdem sie auf die von Braze bereitgestellte Abmeldungs-URL geklickt haben.
{% endif %}

{% if include.metric == "Variation" %}
<i>Variante</i> ist die Anzahl der Varianten einer Kampagne, die sich nach den Vorgaben des Erstellers unterscheiden.
{% endif %}