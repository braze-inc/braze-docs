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

{% if include.metric == "Body Click" %}
Push-Story-Benachrichtigungen zeichnen einen <i>Body Click</i> auf, wenn die Benachrichtigung angeklickt wird. Sie wird nicht aufgezeichnet, wenn eine Nachricht erweitert wird oder wenn eine Aktionsschaltfläche angeklickt wird.
{% endif %}

{% if include.metric == "Body Clicks" %}
<i>Body Clicks</i> treten auf, wenn ein Benutzer auf eine Nachricht klickt, die keine Schaltflächen (Schaltfläche 1, Schaltfläche 2) hat und mit dem traditionellen Editor erstellt wurde, und wenn eine Nachricht, die mit dem HTML-Editor oder dem Drag-and-Drop-Editor erstellt wurde, die <code>brazeBridge.logClick()</code> ohne Argumente.
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
<i>Schaltfläche 1 Klicks</i> ist die Gesamtzahl der Klicks auf Schaltfläche 1 der Nachricht.
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>Button 2 Klicks</i> ist die Gesamtzahl der Klicks auf Button 2 der Nachricht.
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>Eingereichte Auswahlen</i> ist die Gesamtzahl der ausgewählten Auswahlen, wenn der Benutzer auf der Seite mit den Umfragefragen einer <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen</a> Umfrage auf die Schaltfläche Senden klickt.
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
<i>Die Klick-zu-Öffnen-Rate</i> ist der Prozentsatz der zugestellten E-Mails, die von einem einzelnen Benutzer oder Rechner mindestens einmal geöffnet wurden, und ist nur im <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>Report Builder</a> verfügbar.
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
<i>Confirmation Page Dismissals</i> ist die Gesamtzahl der Klicks auf die Schaltfläche Schließen (x) auf der Bestätigungsseite einer <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Conversion Rate" %}
<i>Die Konversionsrate</i> ist der Prozentsatz der Häufigkeit eines bestimmten Ereignisses im Vergleich zu allen Empfängern einer Nachricht. Dieses definierte Ereignis wird festgelegt, wenn Sie die Kampagne erstellen.
{% endif %}

{% if include.metric == "Conversion Window" %}
Das <i>Conversion-Fenster</i> ist die Anzahl der Tage nach Erhalt der Nachricht, in denen die Aktionen des Benutzers verfolgt und einem Conversion-Ereignis zugeordnet werden. Konvertierungen, die nach diesem Fenster stattfinden, werden nicht dem Konvertierungsereignis zugeschrieben.
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
<i>Konvertierungen (B, C, D)</i> sind zusätzliche Konvertierungsereignisse, die nach dem primären Konvertierungsereignis hinzugefügt werden. Dies ist die Anzahl der Male, die ein definiertes Ereignis nach der Interaktion mit oder dem Betrachten einer empfangenen Nachricht aus einer Braze-Kampagne eingetreten ist.
{% endif %}

{% if include.metric == "Total Conversions" %}
Die <i>Gesamtzahl der Conversions</i> ist die Gesamtzahl der Fälle, in denen ein Nutzer ein bestimmtes Conversion-Ereignis abschließt, nachdem er eine In-App-Kampagne gesehen hat.
{% endif %}

{% if include.metric == "Deliveries" %}
<i>Deliveries</i> ist die Gesamtzahl der Nachrichtenanfragen, die vom empfangenden Server angenommen wurden. Das bedeutet nicht, dass die Nachricht an ein Gerät zugestellt wurde, sondern nur, dass die Nachricht vom Server akzeptiert wurde.
{% endif %}

{% if include.metric == "Deliveries %" %}
<i>Zustellungen %</i> ist der prozentuale Anteil an der Gesamtzahl der Nachrichten (Sendungen), die erfolgreich an Empfänger gesendet und von diesen empfangen wurden.
{% endif %}

{% if include.metric == "Delivery Failures" %}
<i>Von Zustellungsfehlern</i> spricht man, wenn die SMS nicht versendet werden konnte, weil die Warteschlangen überfüllt waren (Versand von SMS mit einer höheren Rate, als Ihre Lang- oder Kurzcodes verarbeiten können).
{% endif %}

{% if include.metric == "Direct Opens" %}
<i>Direkte Öffnungen</i> ist die Gesamtzahl (und der Prozentsatz) der Push-Benachrichtigungen, die direkt von dieser Push-Nachricht geöffnet wurden.
{% endif %}

{% if include.metric == "Emailable" %}
<i>Erreichbar</i> ist die Gesamtzahl der Nutzer, die über eine E-Mail-Adresse verfügen und sich explizit angemeldet oder abonniert haben.
{% endif %}

{% if include.metric == "Errors" %}
<i>Fehler</i> ist die Anzahl der von Webhook-Ereignissen zurückgegebenen Fehler (wird während des Sendevorgangs erhöht).
{% endif %}

{% if include.metric == "Failures" %}
<i>Misserfolge</i> sind, wenn die WhatsApp-Nachricht nicht gesendet werden konnte, weil der Internet Service Provider einen Hard Bounce zurückgegeben hat. Ein Hard Bounce bedeutet einen dauerhaften Zustellbarkeitsfehler.
{% endif %}

{% if include.metric == "Influenced Opens" %}
<i>Beeinflusste Öffnungen</i> ist die Gesamtzahl (und der Prozentsatz) der Nutzer, die die App geöffnet haben, nachdem die Push-Benachrichtigung gesendet wurde, ohne die Push-Nachricht direkt zu öffnen.
{% endif %}

{% if include.metric == "Lifetime Revenue" %}
<i>Lifetime Revenue</i> ist die Summe der <code>PurchaseEvents</code> Wert des Preises (in USD), der seit der Auflegung erhalten wurde.
{% endif %}

{% if include.metric == "Lifetime Value Per User" %}
<i>Der Lifetime Value Per User</i> ist der Durchschnitt der Summe der Kampagnen- und Canvas-Einnahmen für einen bestimmten Tag.
{% endif %}

{% if include.metric == "Average Daily Revenue" %}
<i>Der durchschnittliche Tagesumsatz</i> ist der <i>Umsatz auf Lebenszeit</i>, geteilt durch die Gesamtzahl Ihrer <i>Nutzer</i> (auf Ihrer Homepage).
{% endif %}

{% if include.metric == "Daily Purchases" %}
<i>Tägliche Käufe</i> ist der Durchschnitt der gesamten einzigartigen <code>PurchaseEvents</code> im Laufe des Zeitraums.
{% endif %}

{% if include.metric == "Daily Revenue Per User" %}
Der <i>Tagesumsatz pro Benutzer</i> ist der durchschnittliche Tagesumsatz pro täglich aktivem Benutzer.
{% endif %}

{% if include.metric == "Machine Opens" %}
<i>Maschinelle Öffnungen</i> beinhaltet den Anteil der "Öffnungen", die von Apples Mail Privacy Protection (MPP) für iOS 15 betroffen sind. Wenn ein Benutzer zum Beispiel eine E-Mail mit der Mail-App auf einem Apple-Gerät öffnet, wird dies als " <i>Maschine öffnet"</i> protokolliert.
{% endif %}

{% if include.metric == "Other Opens" %}
<i>Andere Öffnungen</i> umfasst E-Mails, die nicht als <i>maschinelle Öffnungen</i> identifiziert wurden. Wenn ein Benutzer beispielsweise eine E-Mail auf einer anderen Plattform öffnet (z. B. Gmail-App auf einem Telefon, Gmail auf einem Desktop-Browser), wird dies als <i>"Andere Öffnungen</i>" protokolliert.
{% endif %}

{% if include.metric == "Opens" %}
<i>Öffnungen</i> sind sowohl <i>direkte Öffnungen</i> als auch <i>beeinflusste Öffnungen</i>, bei denen das Braze SDK mithilfe eines proprietären Algorithmus festgestellt hat, dass eine Push-Benachrichtigung einen Benutzer zum Öffnen der App veranlasst hat.
{% endif %}

{% if include.metric == "Opt-Out" %}
Ein <i>Opt-Out</i> liegt vor, wenn ein Nutzer auf Ihre Nachricht mit einem <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">Opt-Out-Schlüsselwort</a> geantwortet hat und sich von Ihrem SMS-Programm abgemeldet hat.
{% endif %}

{% if include.metric == "Pending Retry" %}
<i>Pending Retry</i> ist die Anzahl der Anfragen, die vom empfangenden Server vorübergehend abgelehnt wurden, bei denen der E-Mail-Dienstanbieter (ESP) aber dennoch versucht hat, sie erneut zuzustellen. Der ESP versucht die Zustellung so lange zu wiederholen, bis eine Timeout-Periode erreicht ist (normalerweise nach 72 Stunden).
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
<i>Primäre Conversions (A)</i> oder <i>primäres Conversion-Ereignis</i> ist die Anzahl der Male, die ein definiertes Ereignis nach der Interaktion mit oder dem Betrachten einer empfangenen Nachricht aus einer Braze-Kampagne eingetreten ist. Dieses definierte Ereignis wird von Ihnen bei der Erstellung der Kampagne festgelegt.
{% endif %}

{% if include.metric == "Reads" %}
<i>Liest</i> ist, wenn der Benutzer die WhatsApp-Nachricht liest. Die Lesebestätigungen des Benutzers müssen "Ein" sein, damit Braze die Lesevorgänge verfolgen kann.
{% endif %}

{% if include.metric == "Received" %}
Der <i>Empfang</i> wird je nach Kanal unterschiedlich definiert und kann erfolgen, wenn Benutzer die Nachricht ansehen, wenn Benutzer eine definierte Auslöseaktion ausführen oder wenn die Nachricht an den Nachrichtenanbieter gesendet wird.
{% endif %}

{% if include.metric == "Rejections" %}
<i>Ablehnungen</i> liegen vor, wenn die SMS vom Netzbetreiber abgelehnt wurde. Dies kann verschiedene Gründe haben, z. B. die Filterung von Inhalten durch den Anbieter, die Verfügbarkeit des Zielgeräts, die Telefonnummer ist nicht mehr in Betrieb und ähnliches.
{% endif %}

{% if include.metric == "Revenue" %}
Der <i>Umsatz</i> ist der Gesamtumsatz in Dollar von Kampagnenempfängern innerhalb des festgelegten <a href='/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events'>primären Konversionsfensters</a>.
{% endif %}

{% if include.metric == "Messages Sent" %}
<i>Gesendete Nachrichten</i> ist die Gesamtzahl der gesendeten Nachrichten in einer Kampagne. Nach dem Start einer geplanten Kampagne umfasst diese Metrik alle gesendeten Nachrichten, unabhängig davon, ob sie aufgrund der Ratenbegrenzung bereits versendet wurden. Das bedeutet nicht, dass die Nachricht empfangen oder an ein Gerät zugestellt wurde, sondern nur, dass die Nachricht gesendet wurde.
{% endif %}

{% if include.metric == "Sent" %}
<i>Gesendet</i> wird jedes Mal, wenn eine Kampagne oder ein Canvas-Schritt gestartet oder ausgelöst wurde und eine SMS von Braze gesendet wurde. Es ist möglich, dass die SMS das Gerät eines Benutzers aufgrund von Fehlern nicht erreicht hat.
{% endif %}

{% if include.metric == "Sends" %}
<i>Sendungen</i> ist die Gesamtzahl der gesendeten Nachrichten in einer Kampagne. Nach dem Start einer geplanten Kampagne umfasst diese Metrik alle gesendeten Nachrichten, unabhängig davon, ob sie aufgrund der Ratenbegrenzung bereits versendet wurden. Das bedeutet nicht, dass die Nachricht empfangen oder an ein Gerät zugestellt wurde, sondern nur, dass die Nachricht gesendet wurde.
{% endif %}

{% if include.metric == "Sends to Carrier" %}
<i>Sends to Carrier</i> ist veraltet, wird aber für Benutzer, die es bereits haben, weiterhin unterstützt. Es handelt sich um die Summe der <i>Bestätigten Zustellungen</i>, <i>Ablehnungen</i> und <i>Sendungen</i>, bei denen die Zustellung oder Ablehnung nicht vom Zusteller bestätigt wurde. Dies gilt auch für Fälle, in denen Zusteller keine Zustell- oder Ablehnungsbestätigung liefern, da einige Zusteller diese Bestätigung nicht liefern oder zum Zeitpunkt des Versands nicht liefern können.
{% endif %}

{% if include.metric == "Spam" %}
<i>Spam</i> ist die Gesamtzahl der zugestellten E-Mails, die als "Spam" markiert wurden. Braze meldet Benutzer, die eine E-Mail als Spam markiert haben, automatisch ab, so dass diese Benutzer nicht mehr von zukünftigen E-Mails angesprochen werden.
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
<i>Umfrageseitenabbrüche</i> ist die Gesamtzahl der Klicks auf die Schaltfläche Schließen (x) auf der Seite mit den Umfragefragen einer <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Survey Submissions" %}
<i>Umfrageübermittlungen</i> ist die Gesamtzahl der Klicks auf die Schaltfläche "Senden" einer <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Total Clicks" %}
<i>Gesamtklicks</i> ist die Gesamtzahl (und der Prozentsatz) der Nutzer, die innerhalb der zugestellten Nachricht geklickt haben, unabhängig davon, ob derselbe Nutzer mehrmals geklickt hat.
{% endif %}

{% if include.metric == "Total Dismissals" %}
<i>Ablehnungen insgesamt</i> ist die Anzahl der Ablehnungen von Inhaltskarten aus einer Kampagne. Wenn ein Benutzer eine Nachricht zweimal ablehnt, wird sie nur einmal gezählt.
{% endif %}

{% if include.metric == "Total Impressions" %}
<i>Die Gesamtzahl der Impressionen</i> gibt an, wie oft die Nachricht geladen wurde und auf dem Bildschirm des Benutzers erscheint, unabhängig von der vorherigen Interaktion (wenn einem Benutzer beispielsweise eine Nachricht zweimal angezeigt wird, wird sie zweimal gezählt).
{% endif %}

{% if include.metric == "Total Opens" %}
<i>Total Opens</i> ist die Gesamtzahl der Nachrichten, die geöffnet wurden.
{% endif %}

{% if include.metric == "Total Revenue" %}
<i>Gesamtumsatz</i> ist der Gesamtumsatz in Dollar von Kampagnenempfängern innerhalb des festgelegten primären Umrechnungsfensters.
{% endif %}

{% if include.metric == "Unique Clicks" %}
<i>Eindeutige Klicks</i> ist die eindeutige Anzahl von Empfängern, die mindestens einmal innerhalb einer Nachricht geklickt haben, und wird durch <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a> gemessen.
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>Unique Dismissals</i> ist die Anzahl der Benutzer, die Content Cards aus einer Kampagne entlassen haben. Ein Benutzer, der eine Inhaltskarte mehrmals aus einer Kampagne ablehnt, stellt eine einzige Ablehnung dar.
{% endif %}

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

{% if include.metric == "Unique Impressions" %}
<i>Unique Impressions</i> ist die Gesamtzahl der Nutzer, die eine bestimmte Nachricht an einem Tag erhalten und angesehen haben.
{% endif %}

{% if include.metric == "Unique Recipients" %}
<i>Eindeutige Empfänger</i> ist die Anzahl der eindeutigen täglichen Empfänger oder Nutzer, die eine bestimmte Nachricht an einem Tag erhalten haben.
{% endif %}

{% if include.metric == "Unique Opens" %}
<i>Unique Opens</i> ist die Gesamtzahl der zugestellten Nachrichten, die von einem einzelnen Nutzer mindestens einmal geöffnet wurden und über einen Zeitraum von sieben Tagen verfolgt werden.
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
<i>Unsubscribers</i> oder <i>Unsub</i> ist die Anzahl der Nachrichten, die zu einer Abmeldung führen. Abmeldungen erfolgen, wenn ein Benutzer auf den Braze Abmeldelink klickt.
{% endif %}

{% if include.metric == "Unsubscribes" %}
<i>Abbestellungen</i> ist die Anzahl der Empfänger, deren Abonnementstatus sich in "Abbestellt" geändert hat, nachdem sie auf die von Braze bereitgestellte Abbestellungs-URL geklickt haben.
{% endif %}

{% if include.metric == "Variation" %}
<i>Variation</i> ist die Anzahl der Variationen einer Kampagne, die sich nach den Vorgaben des Erstellers unterscheiden.
{% endif %}