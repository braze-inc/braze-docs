---
page_order: 2
nav_title: Segmentierungsfilter
article_title: Filter für die Segmentierung
layout: glossary_page
glossary_top_header: "Filter für die Segmentierung"
glossary_top_text: "Das Braze SDK bietet Ihnen ein leistungsstarkes Arsenal an Filtern, mit denen Sie Ihre Nutzer:innen anhand spezifischer Features und Attribute segmentieren und gezielt ansprechen können. Sie können diese Filter nach Filterkategorie suchen oder eingrenzen.<br><br>Um mehr über die verschiedenen Datentypen angepasster Attribute zu erfahren, die Sie zur Segmentierung von Nutzer:innen verwenden können, lesen Sie bitte <a href=\"/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types\">Datentypen angepasster Attribute</a>."

page_type: glossary
tool: Segments
description: "Dieses Glossar listet die verfügbaren Filter auf, mit denen Sie Ihre Nutzer:innen segmentieren und gezielt ansprechen können."
search_rank: 2
glossary_tag_name: Filterkategorie
glossary_filter_text: "Wählen Sie eine Kategorie aus, um das Glossar einzugrenzen:"

# channel to icon/fa or image mapping
# NOTE: glossary_tags names must match the "tags" under each glossary entry exactly (filter/checkbox logic). Do not translate.
glossary_tags:
  - name: Segment or CSV membership
  - name: Custom attribute
  - name: Custom events
  - name: Sessions
  - name: Retargeting
  - name: Channel subscription behavior
  - name: Purchase behavior
  - name: eCommerce
  - name: Demographic attributes
  - name: App
  - name: Uninstall
  - name: Devices
  - name: Location
  - name: Cohort membership
  - name: Install attribution
  - name: Intelligence and predictive
  - name: Social activity
  - name: Other Filters
  - name: Advertising use cases
  - name: User Attributes

glossaries:
  - name: Segmentzugehörigkeit
    description: "Ermöglicht es Ihnen, überall dort, wo Filter verwendet werden (z. B. Segmente, Kampagnen und andere), nach der Segmentzugehörigkeit zu filtern und mehrere verschiedene Segmente innerhalb einer Kampagne anzusprechen. <br><br>Beachten Sie, dass Segmente, die diesen Filter bereits verwenden, nicht weiter in andere Segmente eingeschlossen oder verschachtelt werden können, da dies zu einem Zyklus führen kann, bei dem Segment A Segment B einschließt, das dann wiederum versucht, Segment A einzuschließen. In diesem Fall würde das Segment immer wieder auf sich selbst verweisen, sodass es unmöglich wäre, zu berechnen, wer tatsächlich dazugehört. Außerdem wird die Verschachtelung von Segmenten auf diese Weise komplizierter und kann die Arbeit verlangsamen. Erstellen Sie stattdessen das Segment, das Sie einbeziehen möchten, mit denselben Filtern neu."
    tags:
      - Segment or CSV membership
  - name: Braze-Segmenterweiterungen
    description: "Nachdem Sie eine Segmenterweiterung im Braze-Dashboard erstellt haben, können Sie wählen, ob Sie diese Erweiterungen in Ihr Segment aufnehmen oder ausschließen möchten."
    tags:
      - Segment or CSV membership
  - name: Aktualisiert/Importiert aus CSV
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie Teil eines CSV-Uploads waren oder nicht."
    tags:
      - Segment or CSV membership
  - name: Angepasste Attribute
    description: "Ermittelt, ob ein:e Nutzer:in mit einem angepassten Attribut-Wert übereinstimmt oder nicht. <br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Custom attribute
  - name: Erstellt am
    description: "Segmentiert Nutzer:innen danach, wann ihr Nutzerprofil erstellt wurde. Wenn ein:e Nutzer:in per CSV oder API hinzugefügt wurde, zeigt dieser Filter das Datum an, an dem sie hinzugefügt wurden. Wenn der oder die Nutzer:in nicht per CSV oder API hinzugefügt wurde und die erste Sitzung durch das SDK getrackt wurde, spiegelt dieser Filter das Datum dieser ersten Sitzung wider."
    tags:
      - Other Filters
  - name: Erstellt über
    description: "Segmentiert Nutzer:innen danach, wo ihr Nutzerprofil erstellt wurde.<br><br>Die folgenden Werte werden unterstützt:<br>- SDK (<code>sdk</code>): Nutzerprofil über das Braze SDK erstellt.<br>- REST API (<code>rest</code>): Nutzerprofil über die Braze REST API erstellt.<br>- Push-Token-Import (<code>pti</code>): Nutzerprofil über Push-Token-Import erstellt.<br>- CSV (<code>csv</code>): Nutzerprofil über CSV-Import erstellt.<br>- Demo (<code>demo</code>): Nutzerprofil über Demodaten erstellt.<br>- SMS (<code>sms</code>): Nutzerprofil über SMS erstellt.<br>- Shopify (<code>shopify</code>): Nutzerprofil über Shopify erstellt.<br>- WhatsApp (<code>whats_app</code>): Nutzerprofil über WhatsApp erstellt.<br>- Provider-Event (<code>provider_event</code>): Nutzerprofil über ein Provider-Event erstellt.<br>- Provider-Sync (<code>provider_sync</code>): Nutzerprofil über einen Provider-Sync erstellt.<br>- Landing-Page (<code>landing_page</code>): Nutzerprofil über eine Landing-Page erstellt."
    tags:
      - Other Filters
  - name: Verschachtelte angepasste Attribute
    description: "Attribute, die die Eigenschaften von angepassten Attributen sind.<br><br>Wenn Sie ein verschachteltes angepasstes Zeitattribut filtern, können Sie wählen, ob Sie nach „Tag des Jahres" oder „Zeit" filtern möchten. „Tag des Jahres" überprüft lediglich den Monat und den Tag zum Vergleich. „Zeit" vergleicht den vollständigen Zeitstempel, einschließlich des Jahres."
    tags:
      - Custom attribute
  - name: Tag des wiederkehrenden Events
    description: "Dieser Filter betrachtet den Monat und den Tag eines angepassten Attributs mit dem Datentyp „Datum", aber nicht das Jahr. Dieser Filter ist nützlich für jährliche Events.<br><br>Zeitzone&#58;<br>Dieser Filter passt sich an die Zeitzone der Nutzer:innen an, sofern die Nachricht mit der Option „Ortszeit" versendet wird. Andernfalls verwendet dieser Filter die Zeitzone Ihres Unternehmens."
    tags:
      - Custom attribute
  - name: Angepasstes Event
    description: "Ermittelt, ob ein:e Nutzer:in ein speziell aufgezeichnetes Event durchgeführt hat oder nicht.<br><br> Beispiel:<br>Aktivität mit der Eigenschaft activity_name abgeschlossen.<br><br>Zeitzone:<br>UTC – Kalendertag = 1 Kalendertag umfasst 24 bis 48 Stunden des Verlaufs der Nutzer:innen"
    tags:
      - Custom events
  - name: Erste Durchführung von angepasstem Event
    description: "Ermittelt den frühesten Zeitpunkt, zu dem ein:e Nutzer:in ein speziell aufgezeichnetes Event durchgeführt hat. (24-Stunden-Zeitraum) <br><br>Beispiel:<br> Erster Warenkorb-Abbruch vor weniger als 1 Tag<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Custom events
  - name: Letzte Durchführung von angepasstem Event
    description: "Ermittelt den spätesten Zeitpunkt, an dem ein:e Nutzer:in ein speziell aufgezeichnetes Event durchgeführt hat. Dieser Filter unterstützt Dezimalzahlen, z. B. 0,25 Stunden. (24-Stunden-Zeitraum) <br><br>Beispiel:<br> Letzter Warenkorb-Abbruch vor weniger als 1 Tag<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Custom events
  - name: X angepasstes Event in Y Tagen
    description: "Ermittelt, ob ein:e Nutzer:in in der letzten angegebenen Anzahl von Kalendertagen zwischen 1 und 30 ein speziell aufgezeichnetes Event zwischen 0 und 50 Mal durchgeführt hat oder nicht. (Kalendertag = 1 Kalendertag umfasst 24 bis 48 Stunden des Verlaufs der Nutzer:innen)<br> <a href=\"/docs/x-in-y-behavior/\"> Erfahren Sie hier mehr über das X-in-Y-Verhalten.</a> <br><br>Beispiel:<br>In den letzten 1 Kalendertagen genau 0 Mal den Warenkorb verlassen<br><br>Zeitzone:<br>UTC – Um alle Zeitzonen zu berücksichtigen, umfasst ein Kalendertag je nach Zeitpunkt der Segmentauswertung 24 bis 48 Stunden des Verlaufs der Nutzer:innen; zwei Kalendertage umfassen 48 bis 72 Stunden des Verlaufs der Nutzer:innen usw."
    tags:
      - Custom events
  - name: X angepasstes eigenschaftsbezogenes Event in Y Tagen
    description: "Ermittelt, ob ein:e Nutzer:in ein speziell aufgezeichnetes Event in Bezug auf eine bestimmte Eigenschaft zwischen 0 und 50 Mal in der letzten angegebenen Anzahl von Kalendertagen zwischen 1 und 30 durchgeführt hat oder nicht. (Kalendertag = 1 Kalendertag umfasst 24 bis 48 Stunden des Verlaufs der Nutzer:innen)<br><a href=\"/docs/x-in-y-behavior/\">Erfahren Sie hier mehr über das X-in-Y-Verhalten.</a> <br><br>Beispiel:<br> Zu den Favoriten hinzugefügt mit der Eigenschaft \"event_name\" genau 0 Mal in den letzten 1 Kalendertag<br><br>Zeitzone:<br>UTC – Um alle Zeitzonen zu berücksichtigen, umfasst ein Kalendertag je nach Zeitpunkt der Segmentauswertung 24 bis 48 Stunden des Verlaufs der Nutzer:innen; zwei Kalendertage umfassen 48 bis 72 Stunden des Verlaufs der Nutzer:innen usw."
    tags:
      - Custom events
  - name: E-Mail-Adresse
    description: "Ermöglicht es Ihnen, Ihre Kampagnenempfänger:innen zu Testzwecken nach einzelnen E-Mail-Adressen zu bestimmen. Sie können damit auch Transaktions-E-Mails an alle Ihre Nutzer:innen (auch an abgemeldete) senden, indem Sie im Filter den Parameter „E-Mail-Adresse ist nicht leer" angeben. So können Sie die Zustellung von E-Mails unabhängig vom Opt-in-Status maximieren. <br><br>Dieser Filter prüft nur, ob Nutzerprofile eine E-Mail-Adresse haben, während der Filter <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-available\">E-Mail verfügbar</a> nach zusätzlichen Kriterien prüft."
    tags:
      - Other Filters
  - name: Externe Nutzer-ID
    description: "Ermöglicht es Ihnen, Ihre Kampagnenempfänger:innen zu Testzwecken nach individuellen Nutzer-IDs zu bestimmen."
    tags:
      - Other Filters
  - name: "Zufällige Bucket-Nr."
    description: "Segmentiert Ihre Nutzer:innen nach einer zufällig zugewiesenen Nummer (0 bis 9999 einschließlich). Sie kann die Erstellung gleichmäßig verteilter Segmente von wirklich zufälligen Nutzer:innen für A/B- und multivariate Tests ermöglichen."
    tags:
      - Other Filters
  - name: Sitzungsanzahl
    description: "Segmentiert Ihre Nutzer:innen nach der Anzahl der Sitzungen, die sie in einer Ihrer Apps innerhalb Ihres Workspace hatten."
    tags:
      - Sessions
  - name: Sitzungsanzahl für App
    description: "Segmentiert Ihre Nutzer:innen nach der Anzahl der Sitzungen, die sie in einer bestimmten, festgelegten App hatten."
    tags:
      - Sessions
  - name: X Sitzungen in den letzten Y Tagen
    description: "Segmentiert Ihre Nutzer:innen nach der Anzahl der Sitzungen (zwischen 0 und 50), die sie in Ihrer App in der letzten angegebenen Anzahl von Kalendertagen zwischen 1 und 30 hatten. <br> <a href=\"/docs/x-in-y-behavior/\">Erfahren Sie hier mehr über das X-in-Y-Verhalten.</a>"
    tags:
      - Sessions
  - name: Erste App-Nutzung
    description: "Segmentiert Ihre Nutzer:innen nach dem frühesten aufgezeichneten Zeitpunkt, zu dem sie Ihre App geöffnet haben. <em>Dies erfasst die erste Sitzung, in der sie eine Version Ihrer App mit integriertem Braze SDK verwenden.</em> (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Sessions
  - name: Erste Nutzung einer bestimmten App
    description: "Segmentiert Ihre Nutzer:innen nach dem frühesten aufgezeichneten Zeitpunkt, zu dem sie eine Ihrer Apps innerhalb Ihres Workspace geöffnet haben. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Sessions
  - name: Letzte App-Nutzung
    description: "Segmentiert Ihre Nutzer:innen nach dem Zeitpunkt, an dem sie Ihre App zuletzt geöffnet haben. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Sessions
  - name: Letzte Nutzung einer bestimmten App
    description: "Segmentiert Ihre Nutzer:innen nach dem Zeitpunkt, an dem sie zuletzt eine bestimmte App geöffnet haben. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Sessions
  - name: Mediane Sitzungsdauer
    description: "Segmentiert Ihre Nutzer:innen nach der medianen Länge ihrer Sitzungen in Ihrer App."
    tags:
      - Sessions
  - name: Hat Nachricht aus Kampagne empfangen
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie eine bestimmte Kampagne erhalten haben oder nicht. Dieser Filter erfasst nur Nutzer:innen, denen die Nachricht explizit gesendet wurde, und nicht andere Nutzer:innen mit derselben E-Mail-Adresse oder Telefonnummer, die doppelte Nachrichten erhalten haben. Um doppelte Nutzer:innen zu erfassen, verwenden Sie <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Nachricht aus Kampagne oder Canvas mit Tag empfangen</a>.<br><br> Bei Content Cards, Bannern und In-App-Nachrichten ist dies der Zeitpunkt, an dem ein:e Nutzer:in eine Impression protokolliert, nicht der Zeitpunkt, an dem die Karte oder die In-App-Nachricht gesendet wird.<br><br>Bei Push und Webhooks ist dies der Zeitpunkt, an dem die Nachricht an die Nutzer:innen gesendet wird.<br><br> Bei WhatsApp ist dies der Zeitpunkt, an dem die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht der Zeitpunkt, an dem die Nachricht an das Gerät der Nutzer:innen zugestellt wird. <br><br>Bei E-Mails ist dies der Zeitpunkt, an dem eine E-Mail-Anfrage an den E-Mail-Anbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird).<br><br>Bei SMS ist dies der Zeitpunkt, an dem die letzte Nachricht an den SMS-Anbieter zugestellt wurde. Dies ist keine Garantie dafür, dass die Nachricht auf dem Gerät der Nutzer:innen angekommen ist."
    tags:
      - Retargeting
  - name: Empfangene Kampagnenvariante
    description: "Segmentiert Ihre Nutzer:innen danach, welche Variante einer multivariaten Kampagne sie erhalten haben. Dieser Filter erfasst nur Nutzer:innen, denen die Nachricht explizit gesendet wurde, und nicht andere Nutzer:innen mit derselben E-Mail-Adresse oder Telefonnummer, die doppelte Nachrichten erhalten haben. Um doppelte Nutzer:innen zu erfassen, verwenden Sie <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Nachricht aus Kampagne oder Canvas mit Tag empfangen</a>.<br><br> Bei Content Cards, Bannern und In-App-Nachrichten ist dies der Zeitpunkt, an dem ein:e Nutzer:in eine Impression protokolliert, nicht der Zeitpunkt, an dem die Karte oder die In-App-Nachricht gesendet wird.<br><br>Bei Push und Webhooks ist dies der Zeitpunkt, an dem die Nachricht an die Nutzer:innen gesendet wird.<br><br> Bei WhatsApp ist dies der Zeitpunkt, an dem die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht der Zeitpunkt, an dem die Nachricht an das Gerät der Nutzer:innen zugestellt wird. <br><br>Bei E-Mails ist dies der Zeitpunkt, an dem eine E-Mail-Anfrage an den E-Mail-Anbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird).<br><br>Bei SMS ist dies der Zeitpunkt, an dem die letzte Nachricht an den SMS-Anbieter zugestellt wurde. Dies ist keine Garantie dafür, dass die Nachricht auf dem Gerät der Nutzer:innen angekommen ist."
    tags:
      - Retargeting
  - name: Hat Nachricht aus Canvas-Schritt empfangen
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie eine bestimmte Canvas-Komponente erhalten haben oder nicht. Dieser Filter erfasst nur Nutzer:innen, denen die Nachricht explizit gesendet wurde, und nicht andere Nutzer:innen mit derselben E-Mail-Adresse oder Telefonnummer, die doppelte Nachrichten erhalten haben. Um doppelte Nutzer:innen zu erfassen, verwenden Sie <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Nachricht aus Kampagne oder Canvas mit Tag empfangen</a>.<br><br> Bei Content Cards und In-App-Nachrichten ist dies der Zeitpunkt, an dem ein:e Nutzer:in eine Impression protokolliert, nicht der Zeitpunkt, an dem die Karte oder In-App-Nachricht gesendet wird.<br><br>Bei Push und Webhooks ist dies der Zeitpunkt, an dem die Nachricht an die Nutzer:innen gesendet wird.<br><br> Bei WhatsApp ist dies der Zeitpunkt, an dem die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht der Zeitpunkt, an dem die Nachricht an das Gerät der Nutzer:innen zugestellt wird. <br><br>Bei E-Mails ist dies der Zeitpunkt, an dem eine E-Mail-Anfrage an den E-Mail-Anbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird).<br><br>Bei SMS ist dies der Zeitpunkt, an dem die letzte Nachricht an den SMS-Anbieter zugestellt wurde. Dies ist keine Garantie dafür, dass die Nachricht auf dem Gerät der Nutzer:innen angekommen ist."
    tags:
      - Retargeting
  - name: Letzte empfangene Nachricht aus einem bestimmten Canvas-Schritt
    description: "Segmentiert Ihre Nutzer:innen danach, wann sie eine bestimmte Canvas-Komponente erhalten haben. Dieser Filter erfasst nur Nutzer:innen, denen die Nachricht explizit gesendet wurde, und keine anderen Nutzer:innen mit derselben E-Mail-Adresse oder Telefonnummer, die doppelte Nachrichten erhalten haben. Um doppelte Nutzer:innen zu erfassen, verwenden Sie <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Nachricht aus Kampagne oder Canvas mit Tag empfangen</a>. Dieser Filter berücksichtigt nicht, wann Nutzer:innen andere Canvas-Komponenten erhalten haben."
    tags:
      - Retargeting
  - name: Letzte empfangene Nachricht aus einer bestimmten Kampagne
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie eine bestimmte Kampagne erhalten haben oder nicht. Dieser Filter erfasst nur Nutzer:innen, denen die Nachricht explizit gesendet wurde, und keine anderen Nutzer:innen mit derselben E-Mail-Adresse oder Telefonnummer, die doppelte Nachrichten erhalten haben. Um doppelte Nutzer:innen zu erfassen, verwenden Sie <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Nachricht aus Kampagne oder Canvas mit Tag empfangen</a>. Dieser Filter berücksichtigt nicht, wann Nutzer:innen andere Kampagnen erhalten haben."
    tags:
      - Retargeting
  - name: Hat Nachricht aus Kampagne oder Canvas mit Tag empfangen
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie eine bestimmte Kampagne oder ein bestimmtes Canvas mit einem bestimmten Tag erhalten haben oder nicht. Im Gegensatz zu „Nachricht aus Kampagne empfangen" und „Nachricht aus Canvas-Schritt empfangen" erfasst dieser Filter alle Nutzer:innen mit derselben E-Mail-Adresse oder Telefonnummer, die doppelte Nachrichten erhalten haben.<br><br> Bei Content Cards, Bannern (nur Kampagnen) und In-App-Nachrichten ist dies der Zeitpunkt, an dem ein:e Nutzer:in eine Impression protokolliert, nicht der Zeitpunkt, an dem die Karte oder die In-App-Nachricht gesendet wird.<br><br>Bei Push und Webhooks ist dies der Zeitpunkt, an dem die Nachricht an die Nutzer:innen gesendet wird.<br><br> Bei WhatsApp ist dies der Zeitpunkt, an dem die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht der Zeitpunkt, an dem die Nachricht an das Gerät der Nutzer:innen zugestellt wird. <br><br>Bei E-Mails ist dies der Zeitpunkt, an dem eine E-Mail-Anfrage an den E-Mail-Anbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird). Wenn mehrere Nutzer:innen dieselbe E-Mail-Adresse verwenden:<br>- Beim ersten Senden wird nur das Profil der spezifisch angesprochenen Nutzer:innen aktualisiert. <br>- Wenn die E-Mail zugestellt wird oder wenn die Nutzer:innen die E-Mail oder einen Link in der E-Mail öffnen, scheinen alle Nutzer:innen, die diese E-Mail-Adresse verwenden, die Nachricht erhalten zu haben.<br><br>Bei SMS ist dies der Zeitpunkt, an dem die letzte Nachricht an den SMS-Anbieter zugestellt wurde. Dies ist keine Garantie dafür, dass die Nachricht auf dem Gerät der Nutzer:innen angekommen ist."
    tags:
      - Retargeting
  - name: Letzte empfangene Nachricht aus einer Kampagne oder einem Canvas mit Tag
    description: "Segmentiert Ihre Nutzer:innen danach, wann sie eine bestimmte Kampagne oder ein bestimmtes Canvas mit einem bestimmten Tag erhalten haben. Dieser Filter berücksichtigt nicht, wann Nutzer:innen andere Kampagnen oder Canvase erhalten haben. (24-Stunden-Zeitraum)"
    tags:
      - Retargeting
  - name: Hat nie eine Nachricht aus der Kampagne oder dem Canvas-Schritt empfangen
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie eine Kampagne oder eine Canvas-Komponente erhalten haben oder nicht."
    tags:
      - Retargeting
  - name: Letzte empfangene E-Mail
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, an dem sie eine Ihrer E-Mail-Nachrichten erhalten haben. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Letzter empfangener Push
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, an dem sie eine Ihrer Push-Benachrichtigungen erhalten haben. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Letzte In-App-Nachricht-Impression
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, an dem sie eine In-App-Nachricht angesehen haben."
    tags:
      - Retargeting
  - name: Letzte empfangene SMS
    description: "Segmentiert Ihre Nutzer:innen nach dem Zeitpunkt, zu dem die letzte Nachricht an den SMS-Anbieter zugestellt wurde. Dies ist keine Garantie dafür, dass die Nachricht auf dem Gerät der Nutzer:innen angekommen ist. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Letzter empfangener Webhook
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, an dem Braze einen Webhook für diese Nutzer:innen gesendet hat. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Letzte empfangene WhatsApp-Nachricht
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, an dem sie eine WhatsApp-Nachricht erhalten haben. Dies ist der Zeitpunkt, an dem die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht der Zeitpunkt, an dem die Nachricht an das Gerät der Nutzer:innen zugestellt wird. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Live-Aktivitäten Push to Start für App registriert
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie registriert sind, um eine Live-Aktivität über iOS-Push-Benachrichtigungen für eine bestimmte App zu starten."
    tags:
      - Devices
  - name: Kampagne angeklickt/geöffnet
    description: "Filtern Sie nach der Interaktion mit einer bestimmten Kampagne. Bei E-Mail-Messaging umfasst das Öffnungsereignis sowohl maschinelle als auch nicht-maschinelle Öffnungen.<br><br> Bei E-Mails umfasst dies auch die Option, nach „geöffnete E-Mails (maschinelle Öffnungen)" und „geöffnete E-Mails (andere Öffnungen)" zu filtern. Klicks auf Links zum Abmelden und Präferenzzentren werden bei diesem Filter nicht berücksichtigt. Wenn mehrere Nutzer:innen dieselbe E-Mail-Adresse verwenden:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden die Profile aller anderen Nutzer:innen mit derselben E-Mail-Adresse ebenfalls aktualisiert. <br>- Wenn die ursprünglichen Nutzer:innen ihre E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändern, wird das Öffnen oder Klicken auf alle verbleibenden Nutzer:innen mit dieser E-Mail-Adresse anstelle der ursprünglichen Nutzer:innen angewendet.<br><br>Für SMS ist eine Interaktion definiert als:<br>- Die Nutzer:innen haben zuletzt eine Antwort-SMS gesendet, die einer bestimmten Keyword-Kategorie entspricht. Dies wird der letzten Kampagne zugeschrieben, die alle Nutzer:innen mit dieser Telefonnummer erhalten haben. Die Kampagne muss in den letzten vier Stunden eingegangen sein.<br>- Die Nutzer:innen haben zuletzt einen verkürzten Link in einer SMS-Nachricht ausgewählt, bei der das Klick-Tracking aktiviert ist, und zwar in einer bestimmten Kampagne."
    tags:
      - Retargeting
  - name: Kampagne oder Canvas mit Tag angeklickt/geöffnet
    description: "Filtern Sie nach Interaktionen mit einer bestimmten Kampagne, die ein bestimmtes Tag hat. Bei E-Mail-Messaging umfasst das Öffnungsereignis sowohl maschinelle als auch nicht-maschinelle Öffnungen.<br><br> Bei E-Mails umfasst dies die Option, nach „geöffnete E-Mails (maschinelle Öffnungen)" und „geöffnete E-Mails (andere Öffnungen)" zu filtern. Wenn mehrere Nutzer:innen dieselbe E-Mail-Adresse verwenden:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden die Profile aller anderen Nutzer:innen mit derselben E-Mail-Adresse ebenfalls aktualisiert. <br>- Wenn die ursprünglichen Nutzer:innen ihre E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändern, wird das Öffnen oder Klicken auf alle verbleibenden Nutzer:innen mit dieser E-Mail-Adresse anstelle der ursprünglichen Nutzer:innen angewendet.<br><br>Für SMS ist eine Interaktion definiert als:<br>- Die Nutzer:innen haben zuletzt eine Antwort-SMS gesendet, die einer bestimmten Keyword-Kategorie entspricht. Dies wird der letzten Kampagne zugeschrieben, die alle Nutzer:innen mit dieser Telefonnummer erhalten haben. Die Kampagne muss in den letzten vier Stunden eingegangen sein.<br>- Die Nutzer:innen haben zuletzt einen verkürzten Link in einer SMS-Nachricht ausgewählt, bei der das Klick-Tracking aktiviert ist, und zwar in einer bestimmten Kampagne oder einem Canvas-Schritt mit Tag."
    tags:
      - Retargeting
  - name: Schritt angeklickt/geöffnet
    description: "Filtern Sie nach der Interaktion mit einer bestimmten Canvas-Komponente. Bei E-Mail-Messaging umfasst das Öffnungsereignis sowohl maschinelle als auch nicht-maschinelle Öffnungen.<br><br>Bei E-Mails umfasst dies die Option, nach „geöffnete E-Mails (maschinelle Öffnungen)" und „geöffnete E-Mails (andere Öffnungen)" zu filtern.<br><br>Für SMS ist eine Interaktion definiert als:<br>- Die Nutzer:innen haben zuletzt eine Antwort-SMS gesendet, die einer bestimmten Keyword-Kategorie entspricht. Dies wird der letzten Kampagne zugeschrieben, die alle Nutzer:innen mit dieser Telefonnummer erhalten haben. Die Kampagne muss in den letzten vier Stunden eingegangen sein. <br>- Die Nutzer:innen haben zuletzt einen verkürzten Link in einer SMS-Nachricht ausgewählt, bei der das Klick-Tracking aktiviert ist, und zwar in einem bestimmten Canvas-Schritt."
    tags:
      - Retargeting
  - name: Alias in Kampagne angeklickt
    description: "Filtern Sie Ihre Nutzer:innen danach, ob sie einen bestimmten Alias in einer bestimmten Kampagne angeklickt haben. Dies gilt nur für E-Mail-Nachrichten. <br><br> Wenn mehrere Nutzer:innen dieselbe E-Mail-Adresse verwenden:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden die Profile aller anderen Nutzer:innen mit derselben E-Mail-Adresse ebenfalls aktualisiert. <br>- Wenn die ursprünglichen Nutzer:innen ihre E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändern, wird das Öffnen oder Klicken auf alle verbleibenden Nutzer:innen mit dieser E-Mail-Adresse anstelle der ursprünglichen Nutzer:innen angewendet."
    tags:
      - Retargeting
  - name: Alias in Canvas-Schritt angeklickt
    description: "Filtern Sie Ihre Nutzer:innen danach, ob sie einen bestimmten Alias in einem bestimmten Canvas angeklickt haben. Dies gilt nur für E-Mail-Nachrichten. <br><br> Wenn mehrere Nutzer:innen dieselbe E-Mail-Adresse verwenden:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden die Profile aller anderen Nutzer:innen mit derselben E-Mail-Adresse ebenfalls aktualisiert. <br>- Wenn die ursprünglichen Nutzer:innen ihre E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändern, wird das Öffnen oder Klicken auf alle verbleibenden Nutzer:innen mit dieser E-Mail-Adresse anstelle der ursprünglichen Nutzer:innen angewendet."
    tags:
      - Retargeting
  - name: Angeklickter Alias in einem beliebigen Kampagnen- oder Canvas-Schritt
    description: "Filtern Sie Ihre Nutzer:innen danach, ob sie einen bestimmten Alias in einer Kampagne oder einem Canvas angeklickt haben. Dies gilt nur für E-Mail-Nachrichten. <br><br> Wenn mehrere Nutzer:innen dieselbe E-Mail-Adresse verwenden:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden die Profile aller anderen Nutzer:innen mit derselben E-Mail-Adresse ebenfalls aktualisiert. <br>- Wenn die ursprünglichen Nutzer:innen ihre E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändern, wird das Öffnen oder Klicken auf alle verbleibenden Nutzer:innen mit dieser E-Mail-Adresse anstelle der ursprünglichen Nutzer:innen angewendet."
    tags:
      - Retargeting
  - name: Rückläufer (Hard Bounced)
    description: "Segmentieren Sie Ihre Nutzer:innen danach, ob ihre E-Mail-Adresse einen Hard Bounce aufweist (z. B. weil die E-Mail-Adresse ungültig ist)."
    tags:
      - Retargeting
  - name: Zustellfehler (Soft Bounced)
    description: "Segmentieren Sie Ihre Nutzer:innen danach, ob sie X-mal in Y Tagen einen Soft Bounce hatten. Segmentfilter können nur auf die letzten 30 Tage zurückblicken, aber mit Segmenterweiterungen können Sie weiter zurückblicken.<br><br>Dieser Filter funktioniert anders als ein Soft-Bounce-Ereignis in Currents. Der Soft-Bounced-Segmentfilter zählt einen Soft Bounce, wenn während der 72-stündigen Wiederholungsperiode keine erfolgreiche Zustellung stattgefunden hat. In Currents wird jeder erfolglose Wiederholungsversuch als Soft-Bounce-Ereignis gesendet."
    tags:
      - Retargeting
  - name: Hat Sie als Spam markiert
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie Ihre Nachrichten als Spam markiert haben oder nicht."
    tags:
      - Retargeting
  - name: Ungültige Telefonnummer
    description: "Segmentiert Ihre Nutzer:innen danach, ob ihre Telefonnummer ungültig ist oder nicht."
    tags:
      - Retargeting
  - name: Keyword-Kategorie der letzten gesendeten eingehenden SMS
    description: "Segmentiert Ihre Nutzer:innen danach, wann sie zuletzt eine SMS an eine bestimmte Abo-Gruppe innerhalb einer bestimmten Keyword-Kategorie gesendet haben."
    tags:
      - Retargeting
  - name: Von Kampagne konvertiert
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie bei einer bestimmten Kampagne konvertiert haben oder nicht. Dieser Filter schließt Nutzer:innen, die sich in der Kontrollgruppe befinden, nicht ein."
    tags:
      - Retargeting
  - name: Von Canvas konvertiert
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie bei einem bestimmten Canvas konvertiert haben oder nicht. Dieser Filter schließt Nutzer:innen, die sich in der Kontrollgruppe befinden, nicht ein."
    tags:
      - Retargeting
  - name: In Kampagnen-Kontrollgruppe
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie in der Kontrollgruppe für eine bestimmte multivariate Kampagne waren oder nicht."
    tags:
      - Retargeting
  - name: In Canvas-Kontrollgruppe
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie in der Kontrollgruppe für ein bestimmtes Canvas waren oder nicht. Dieser Filter berücksichtigt nur Nutzer:innen, die das Canvas betreten haben, sodass Nutzer:innen, die das Canvas nie betreten haben, vollständig aus den Ergebnissen ausgeschlossen werden.<br><br>Wenn Sie beispielsweise nach Nutzer:innen filtern, die nicht zur Kontrollgruppe für ein Canvas gehören, erhalten Sie nur Nutzer:innen, die das Canvas betreten haben und einer Nicht-Kontrollvariante zugewiesen wurden – Nutzer:innen, die das Canvas nie betreten haben, werden nicht berücksichtigt. Um alle Nutzer:innen unabhängig vom Canvas-Eintritt einzubeziehen, verwenden Sie stattdessen den Filter <code>Entered Canvas Variation</code>."
    tags:
      - Retargeting
  - name: Letzte Teilnahme an einer Kontrollgruppe
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten Zeitpunkt, an dem sie in einer Kampagne in die Kontrollgruppe fielen. <br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: In Canvas-Variante aufgenommen
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie einen Variationspfad eines bestimmten Canvas eingegeben haben oder nicht. Dieser Filter wertet alle Nutzer:innen aus.<br><br>Wenn Sie beispielsweise nach Nutzer:innen filtern, die keine Canvas-Variationskontrollgruppe eingegeben haben, erhalten Sie alle Nutzer:innen, die nicht in der Kontrollgruppe sind, unabhängig davon, ob sie das Canvas betreten haben."
    tags:
      - Retargeting
  - name: Empfangszeitpunkt der letzten Nachricht
    description: "Segmentiert Ihre Nutzer:innen anhand der zuletzt erhaltenen Nachricht. (24-Stunden-Zeitraum)<br><br> Bei Content Cards, Bannern und In-App-Nachrichten ist dies der Zeitpunkt, an dem ein:e Nutzer:in zuletzt eine Impression erfasst hat, nicht der Zeitpunkt, an dem die Karte oder In-App-Nachricht zuletzt gesendet wurde.<br><br>Bei Push und Webhooks ist dies der Zeitpunkt, an dem eine Nachricht an die Nutzer:innen gesendet wurde.<br><br> Bei WhatsApp ist dies der Zeitpunkt, an dem die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wurde, nicht der Zeitpunkt, an dem die Nachricht an das Gerät der Nutzer:innen zugestellt wurde. <br><br>Bei E-Mails ist dies der Zeitpunkt, an dem eine E-Mail-Anfrage an den E-Mail-Anbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird). Wenn mehrere Nutzer:innen dieselbe E-Mail-Adresse verwenden:<br>- Beim ersten Senden wird nur das Profil der spezifisch angesprochenen Nutzer:innen aktualisiert. <br>- Wenn die E-Mail zugestellt wird oder wenn die Nutzer:innen die E-Mail oder einen Link in der E-Mail öffnen, scheinen alle Nutzer:innen, die diese E-Mail-Adresse verwenden, die Nachricht erhalten zu haben.<br><br>Bei SMS ist dies der Zeitpunkt, an dem die letzte Nachricht an den SMS-Anbieter zugestellt wurde. Dies ist keine Garantie dafür, dass die Nachricht auf dem Gerät der Nutzer:innen angekommen ist.<br><br>Beispiel:<br>Letzte erhaltene Nachricht vor weniger als 1 Tag = vor weniger als 24 Stunden<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Letzte Interaktion mit Nachricht
    description: "Segmentiert Ihre Nutzer:innen danach, wann sie zuletzt auf einen Ihrer Messaging-Kanäle (Banner, Content Card, E-Mail, In-App, SMS, Push, WhatsApp) geklickt oder diesen geöffnet haben. Bei E-Mail-Messaging umfasst das Öffnungsereignis sowohl maschinelle als auch nicht-maschinelle Öffnungen. (24-Stunden-Zeitraum)<br><br>Bei E-Mails ist dies der Zeitpunkt, an dem eine E-Mail-Anfrage an den E-Mail-Anbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird). Dazu gehört auch die Möglichkeit, nach „geöffnete E-Mails (maschinelle Öffnungen)" und „geöffnete E-Mails (andere Öffnungen)" zu filtern. Wenn mehrere Nutzer:innen dieselbe E-Mail-Adresse verwenden:<br>- Beim ersten Senden wird nur das Profil der spezifisch angesprochenen Nutzer:innen aktualisiert. <br>- Wenn die E-Mail zugestellt wird oder wenn die Nutzer:innen die E-Mail oder einen Link in der E-Mail öffnen, scheinen alle Nutzer:innen, die diese E-Mail-Adresse verwenden, die Nachricht erhalten zu haben.<br><br>Bei SMS ist dies der Zeitpunkt, an dem die Nutzer:innen zuletzt einen verkürzten Link in einer Nachricht ausgewählt haben, für die das Klick-Tracking aktiviert ist.<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Angeklickte Karte
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie auf eine bestimmte Content Card geklickt haben oder nicht. Dieser Filter ist als Unterfilter für „Kampagne angeklickt/geöffnet", „Kampagne oder Canvas mit Tag angeklickt/geöffnet" und „Schritt angeklickt/geöffnet" verfügbar."
    tags:
      - Retargeting
  - name: Feature-Flags
    description: "Das Segment Ihrer Nutzer:innen, bei denen ein bestimmtes <a href=\"/docs/developer_guide/feature_flags/\">Feature-Flag</a> derzeit aktiviert ist."
    tags:
      - Retargeting
  - name: Abo-Gruppe
    description: "Segmentiert Ihre Nutzer:innen nach ihrer Abo-Gruppe für E-Mail, SMS/MMS oder WhatsApp. Archivierte Gruppen werden nicht angezeigt und können nicht verwendet werden."
    tags:
      - Channel subscription behavior
  - name: E-Mail verfügbar
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie über eine gültige E-Mail-Adresse verfügen und ob sie E-Mails abonniert oder ein Opt-in durchgeführt haben. Dieser Filter prüft drei Kriterien&#58; ob die Nutzer:innen sich von E-Mails abgemeldet haben, ob Braze einen Hard Bounce erhalten hat und ob die E-Mail als Spam markiert wurde. Wenn eines dieser Kriterien erfüllt ist oder wenn für Nutzer:innen keine E-Mail-Adresse vorhanden ist, werden die Nutzer:innen nicht berücksichtigt.<br><br>Nutzer:innen, deren E-Mail-Verfügbarkeit <code>false</code> ist, werden aus der Kampagnen-Zielgruppe ausgeschlossen und erhalten die E-Mail nicht – selbst wenn Ihre Sendeeinstellungen so konfiguriert sind, dass an alle Nutzer:innen (einschließlich abgemeldeter) gesendet wird.<br><br>Für E-Mails, bei denen der Opt-in-Status von Bedeutung ist, verwenden Sie „E-Mail verfügbar" anstelle von <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-address\">E-Mail-Adresse</a>. Die zusätzlichen Kriterien helfen Ihnen dabei, Nutzer:innen anzusprechen, die berechtigt sind, E-Mails zu erhalten."
    tags:
      - Channel subscription behavior
  - name: Datum des E-Mail-Opt-ins
    description: "Segmentiert Ihre Nutzer:innen nach dem Datum, an dem sie sich für E-Mails entschieden haben."
    tags:
      - Channel subscription behavior
  - name: E-Mail-Abostatus
    description: "Segmentiert Ihre Nutzer:innen nach ihrem Abo-Status für E-Mails."
    tags:
      - Channel subscription behavior
  - name: Datum der E-Mail-Abmeldung
    description: "Segmentiert Ihre Nutzer:innen nach dem Datum, an dem sie sich von zukünftigen E-Mails abgemeldet haben."
    tags:
      - Channel subscription behavior
  - name: Foreground-Push aktiviert
    description: "Segmentiert Ihre Nutzer:innen, die über eine vorläufige Push-Autorisierung verfügen oder für Push im Vordergrund aktiviert sind. Diese Zählung umfasst insbesondere:<br>1. iOS-Nutzer:innen, die vorläufig für Push autorisiert sind. <br>2. Nutzer:innen, die Push-Benachrichtigungen im Vordergrund aktiviert haben und deren Push-Abo-Status für eine Ihrer Apps nicht abgemeldet ist. Für diese Nutzer:innen umfasst diese Zählung nur den Push im Vordergrund.<br><br>„Foreground-Push aktiviert" schließt Nutzer:innen, die sich abgemeldet haben, nicht ein. <br><br>Nach der Segmentierung mit diesem Filter können Sie im unteren Panel unter <em>Erreichbare Nutzer:innen</em> eine Aufschlüsselung der Personen in diesem Segment für Android, iOS und Web einsehen."
    tags:
      - Channel subscription behavior
  - name: Push im Vordergrund für App aktiviert
    description: "Segmentiert danach, ob Nutzer:innen Push für Ihre App auf ihrem Gerät aktiviert haben. Nutzer:innen, die für eine App Push-Benachrichtigungen im Vordergrund aktiviert haben. Der Push-Abo-Status wird dabei nicht berücksichtigt. Diese Zahl umfasst Nutzer:innen, die vorläufig autorisierte Vordergrund- und Hintergrund-Push-Tokens haben."
    tags:
      - Channel subscription behavior
  - name: Push im Hinter- oder Vordergrund aktiviert
    description: "Segmentiert danach, ob Nutzer:innen ein Push-Token haben und sich nicht abgemeldet haben. Nutzer:innen, die für eine Ihrer Apps Hintergrund- oder Vordergrund-Push aktiviert haben."
    tags:
      - Channel subscription behavior
  - name: Datum des Push-Opt-ins
    description: "Segmentiert Ihre Nutzer:innen nach dem Datum, an dem sie sich für Push entschieden haben."
    tags:
      - Channel subscription behavior
  - name: Push-Abostatus
    description: "Segmentiert Ihre Nutzer:innen nach ihrem <a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">Abo-Status</a> für Push."
    tags:
      - Channel subscription behavior
  - name: Datum der Push-Abmeldung
    description: "Segmentiert Ihre Nutzer:innen nach dem Datum, an dem sie sich von zukünftigen Push-Benachrichtigungen abgemeldet haben."
    tags:
      - Channel subscription behavior
  - name: Gekauftes Produkt
    description: "Segmentiert Ihre Nutzer:innen nach den in Ihrer App gekauften Produkten."
    tags:
      - Purchase behavior
  - name: Gesamtzahl der Käufe
    description: "Segmentiert Ihre Nutzer:innen danach, wie viele Käufe sie in Ihrer App getätigt haben."
    tags:
      - Purchase behavior
  - name: X Produktkäufe in Y Tagen
    description: "Filtern Sie Nutzer:innen danach, wie oft ein bestimmtes Produkt gekauft wurde."
    tags:
      - Purchase behavior
  - name: X Käufe in den letzten Y Tagen
    description: "Segmentiert Ihre Nutzer:innen nach der Anzahl der Käufe (zwischen 0 und 50), die sie in den letzten angegebenen Kalendertagen (zwischen 1 und 30) getätigt haben. <br> <a href=\"/docs/x-in-y-behavior/\">Erfahren Sie hier mehr über das X-in-Y-Verhalten.</a>"
    tags:
      - Purchase behavior
  - name: X Kaufeigenschaft in Y Tagen
    description: "Segmentiert Ihre Nutzer:innen nach der Anzahl der Käufe, die in Bezug auf eine bestimmte Kaufeigenschaft in den letzten angegebenen Kalendertagen zwischen 1 und 30 getätigt wurden. <br> <a href=\"/docs/x-in-y-behavior/\">Erfahren Sie hier mehr über das X-in-Y-Verhalten.</a>"
    tags:
      - Purchase behavior
  - name: Erster Kauf erfolgt
    description: "Segmentiert Ihre Nutzer:innen nach dem frühesten Zeitpunkt, an dem ein:e Nutzer:in einen Kauf in Ihrer App getätigt hat."
    tags:
      - Purchase behavior
  - name: Erster Kauf für App
    description: "Segmentiert Ihre Nutzer:innen nach dem frühesten Zeitpunkt, an dem ein:e Nutzer:in einen Kauf über Ihre App getätigt hat."
    tags:
      - Purchase behavior
  - name: Letzter Kauf erfolgt
    description: "Filtern Sie Nutzer:innen nach dem letzten Kauf, den sie getätigt haben."
    tags:
      - Purchase behavior
  - name: Letztes gekauftes Produkt
    description: "Filtern Sie Nutzer:innen danach, wann sie zuletzt ein bestimmtes Produkt gekauft haben."
    tags:
      - Purchase behavior
  - name: Ausgegebener Betrag
    description: "Segmentiert Ihre Nutzer:innen nach dem Geldbetrag, den sie in Ihrer App ausgegeben haben."
    tags:
      - Purchase behavior
  - name: X Geld ausgegeben in Y Tagen
    description: "Segmentiert Ihre Nutzer:innen nach dem Geldbetrag, den sie in Ihrer App in der letzten angegebenen Anzahl von Kalendertagen zwischen 1 und 30 ausgegeben haben. Dieser Betrag umfasst lediglich die Summe der letzten 50 Käufe. <br> <a href=\"/docs/x-in-y-behavior/\">Erfahren Sie hier mehr über das X-in-Y-Verhalten.</a>"
    tags:
      - Purchase behavior
  - name: Letzte Bestellung (letzte 730 Tage)
    description: "Segmentiert Ihre Nutzer:innen nach dem Zeitpunkt ihrer letzten Bestellung, basierend auf dem <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für aufgegebene Bestellungen (Workspaces, die keine E-Commerce-Events tracken, verfügen nicht über Daten für diesen Filter). Die Nutzer:innen werden einmal täglich für diesen Filter ausgewertet, wobei das maximale Rückblickfenster die letzten 2 Jahre umfasst.<br><br>Dieser Filter befindet sich in der Beta-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Verwendung dieses Filters interessiert sind."
    tags:
      - eCommerce
  - name: Gesamtzahl der Bestellungen (letzte 730 Tage)
    description: "Segmentiert Ihre Nutzer:innen nach der Gesamtzahl der Bestellungen innerhalb der letzten 2 Jahre, basierend auf dem <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für aufgegebene Bestellungen (Workspaces, die keine E-Commerce-Events tracken, verfügen nicht über Daten für diesen Filter). Diese Zählung schließt stornierte Bestellungen aus, die mithilfe des <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Events</a> für stornierte Bestellungen per Tracking nachverfolgt werden müssen. Nutzer:innen werden einmal täglich für diesen Filter ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Verwendung dieses Filters interessiert sind."
    tags:
      - eCommerce
  - name: Bestellungen gesamt
    description: "Segmentiert Ihre Nutzer:innen anhand der Gesamtzahl der Bestellungen während der gesamten Lifetime, basierend auf dem <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für aufgegebene Bestellungen (Workspaces, die keine E-Commerce-Events tracken, verfügen nicht über Daten für diesen Filter). Diese Zählung schließt stornierte Bestellungen aus, die mithilfe des <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Events</a> für stornierte Bestellungen per Tracking nachverfolgt werden müssen. Die Nutzer:innen werden für diesen Filter in Echtzeit ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Verwendung dieses Filters interessiert sind."
    tags:
      - eCommerce
  - name: Gesamtzahl der stornierten Bestellungen (letzte 730 Tage)
    description: "Segmentiert Ihre Nutzer:innen anhand der Gesamtzahl der Bestellungen, die in den letzten 2 Jahren storniert wurden, basierend auf dem <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für aufgegebene Bestellungen (Workspaces, die keine E-Commerce-Events tracken, verfügen nicht über Daten für diesen Filter). Nutzer:innen werden einmal täglich für diesen Filter ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Verwendung dieses Filters interessiert sind."
    tags:
      - eCommerce
  - name: Lifetime-Value Kund:in (letzte 730 Tage)
    description: "Segmentiert Ihre Nutzer:innen anhand des Gesamtumsatzes, den ein:e Nutzer:in voraussichtlich im Laufe der Kaufhistorie mit Ihrer Marke generieren wird. Die Berechnung berücksichtigt die letzten 730 Tage und multipliziert den durchschnittlichen Bestellwert (AOV) mit der Gesamtzahl der aufgegebenen Bestellungen. Anschließend wird die aktive Kaufdauer der Nutzer:innen (der Zeitraum zwischen der ersten und der letzten Bestellung) berücksichtigt. Dieser Filter verwendet Daten, die in <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Events</a> erfasst werden (Workspaces, die keine E-Commerce-Events tracken, verfügen nicht über Daten für diesen Filter). Nutzer:innen werden einmal täglich für diesen Filter ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Verwendung dieses Filters interessiert sind."
    tags:
      - eCommerce
  - name: Gesamterstattungswert (letzte 730 Tage)
    description: "Segmentiert Ihre Nutzer:innen nach dem Wert der Rückerstattungen, die in den letzten 2 Jahren gewährt wurden, basierend auf dem <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für zurückerstattete Bestellungen (Workspaces, die keine E-Commerce-Events tracken, verfügen nicht über Daten für diesen Filter). Nutzer:innen werden einmal täglich für diesen Filter ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Verwendung dieses Filters interessiert sind."
    tags:
      - eCommerce
  - name: Erstattung gesamt
    description: "Segmentiert Ihre Nutzer:innen nach dem Gesamtwert der Rückerstattungen, die während der gesamten Nutzungsdauer gewährt wurden, basierend auf dem <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für zurückerstattete Bestellungen (Workspaces, die keine E-Commerce-Events tracken, verfügen nicht über Daten für diesen Filter). Die Nutzer:innen werden für diesen Filter in Echtzeit ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Verwendung dieses Filters interessiert sind."
    tags:
      - eCommerce
  - name: Gesamtumsatz (letzte 730 Tage)
    description: "Segmentiert Ihre Nutzer:innen nach dem Gesamtumsatz, der in den letzten 2 Jahren durch Bestellungen generiert wurde. Dieser wird berechnet, indem der Umsatz des <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Events</a> für zurückerstattete Bestellungen vom Umsatz des E-Commerce-Events für aufgegebene Bestellungen abgezogen wird (Workspaces, die keine E-Commerce-Events tracken, verfügen nicht über Daten für diesen Filter). Nutzer:innen werden einmal täglich für diesen Filter ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Verwendung dieses Filters interessiert sind."
    tags:
      - eCommerce
  - name: Umsatz gesamt
    description: "Segmentiert Ihre Nutzer:innen anhand des Gesamtumsatzes, der durch Bestellungen während der gesamten Lifetime generiert wurde. Dieser wird berechnet, indem der Umsatz des <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Events</a> für zurückerstattete Bestellungen vom Umsatz des E-Commerce-Events für aufgegebene Bestellungen abgezogen wird (Workspaces, die keine E-Commerce-Events tracken, verfügen nicht über Daten für diesen Filter). Die Nutzer:innen werden für diesen Filter in Echtzeit ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Verwendung dieses Filters interessiert sind."
    tags:
      - eCommerce
  - name: Durchschnittlicher Bestellwert (letzte 730 Tage)
    description: "Segmentiert Ihre Nutzer:innen anhand des Durchschnittswerts (Mittelwerts) der Bestellungen in den letzten 2 Jahren, basierend auf dem <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">empfohlenen E-Commerce-Event</a> für aufgegebene Bestellungen (Workspaces, die keine E-Commerce-Events tracken, verfügen nicht über Daten für diesen Filter). Nutzer:innen werden einmal täglich für diesen Filter ausgewertet.<br><br>Dieser Filter befindet sich in der Beta-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Verwendung dieses Filters interessiert sind."
    tags:
      - eCommerce
  - name: Land
    description: "Segmentiert Ihre Nutzer:innen nach ihrem zuletzt angegebenen Standort (Land)."
    tags:
      - Demographic attributes
  - name: Ort
    description: "Segmentiert Ihre Nutzer:innen nach ihrem zuletzt angegebenen Wohnort (Stadt)."
    tags:
      - Demographic attributes
  - name: Sprache
    description: "Segmentiert Ihre Nutzer:innen nach ihrer bevorzugten Sprache."
    tags:
      - Demographic attributes
  - name: Alter
    description: "Segmentiert Ihre Nutzer:innen nach ihrem Alter, das sie in Ihrer App angegeben haben."
    tags:
      - Demographic attributes
  - name: Geburtstag
    description: "Segmentiert Ihre Nutzer:innen nach ihrem Geburtstag, den sie in Ihrer App angegeben haben. <br> Nutzer:innen, deren Geburtstag auf den 29. Februar fällt, werden in Segmenten einschließlich des 1. März berücksichtigt.<br><br>Wenn Sie auf Dezember- oder Januar-Geburtstage abzielen möchten, fügen Sie die Filterlogik nur innerhalb der 12-Monats-Spanne des Jahres ein, auf das Sie abzielen. Mit anderen Worten: Fügen Sie keine Logik ein, die bis zum Dezember des vorigen Kalenderjahres zurück oder bis zum Januar des nächsten Jahres vorwärts blickt. Um beispielsweise die Geburtstage im Dezember zu ermitteln, können Sie nach „am 31. Dezember", „vor dem 31. Dezember" oder „nach dem 30. November" filtern."
    tags:
      - Demographic attributes
  - name: Geschlecht
    description: "Segmentiert Ihre Nutzer:innen nach Geschlecht, wie sie es in Ihrer App angegeben haben."
    tags:
      - Demographic attributes
  - name: Unformatierte Telefonnummer
    description: "Segmentiert Ihre Nutzer:innen nach ihrer unformatierten Telefonnummer. Enthält keine Klammern, Bindestriche oder andere Symbole."
    tags:
      - Demographic attributes
  - name: Vorname
    description: "Segmentiert Ihre Nutzer:innen nach ihrem Vornamen, den sie in Ihrer App angegeben haben."
    tags:
      - Demographic attributes
  - name: Nachname
    description: "Segmentiert Ihre Nutzer:innen nach ihrem Nachnamen, den sie in Ihrer App angegeben haben."
    tags:
      - Demographic attributes
  - name: Hat App
    description: "Segmentiert danach, ob Nutzer:innen Ihre App jemals installiert haben. Dies umfasst sowohl Nutzer:innen, die Ihre App derzeit installiert haben, als auch diejenigen, die sie in der Vergangenheit deinstalliert haben. Dies erfordert im Allgemeinen, dass Nutzer:innen die App öffnen (eine Sitzung starten), um in diesen Filter aufgenommen zu werden. Es gibt jedoch einige Ausnahmen, z. B. wenn Nutzer:innen in Braze importiert und manuell mit Ihrer App verknüpft wurden."
    tags:
      - App
  - name: Aktuellster Name der App-Version
    description: "Segmentiert nach dem aktuellen Namen der App-Version der Nutzer:innen.<br><br>Bei Verwendung von „kleiner als" oder „kleiner oder gleich" gibt dieser Filter `true` zurück, wenn die Haupt-App-Version nicht vorhanden ist, da die Nutzer:innen älter als die App-Version sind. Das bedeutet, dass wenn die letzte Haupt-App-Version der Nutzer:innen nicht vorhanden ist, sie automatisch dem Filter entsprechen."
    tags:
      - App
  - name: Aktuellste Nummer der App-Version
    description: "Segmentiert nach der aktuellen Versionsnummer der App der Nutzer:innen.<br><br>Bei Verwendung von „kleiner als" oder „kleiner oder gleich" gibt dieser Filter `true` zurück, wenn die Haupt-App-Version nicht vorhanden ist, da die Nutzer:innen älter als die App-Version sind. Das bedeutet, dass wenn die letzte Haupt-App-Version der Nutzer:innen nicht vorhanden ist, sie automatisch dem Filter entsprechen.<br><br>Es kann einige Zeit dauern, bis die aktuellen App-Versionen angezeigt werden. Die App-Version im Nutzerprofil wird aktualisiert, sobald die Informationen vom SDK erfasst werden, was davon abhängt, wann die Nutzer:innen ihre Apps öffnen. Wenn die Nutzer:innen die App nicht öffnen, wird die aktuelle Version nicht aktualisiert. Diese Filter werden ebenfalls nicht rückwirkend angewendet. Es ist empfehlenswert, „größer als" oder „gleich" für aktuelle und zukünftige Versionen zu verwenden, jedoch kann die Verwendung von Filtern für frühere Versionen zu unerwarteten Ergebnissen führen."
    tags:
      - App
  - name: Deinstalliert
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie Ihre App deinstalliert und nicht neu installiert haben."
    tags:
      - Uninstall
  - name: Netzbetreiber des Geräts
    description: "Segmentiert Ihre Nutzer:innen nach dem Netzbetreiber ihres Geräts."
    tags:
      - Devices
  - name: Gerätezahl
    description: "Segmentiert Ihre Nutzer:innen danach, auf wie vielen Geräten sie Ihre App verwendet haben."
    tags:
      - Devices
  - name: Gerätemodell
    description: "Segmentiert Ihre Nutzer:innen nach der Modellversion ihres Mobiltelefons."
    tags:
      - Devices
  - name: Betriebssystem
    description: "Segmentiert Ihre Nutzer:innen, die über ein oder mehrere Geräte mit dem angegebenen Betriebssystem verfügen. Um Nutzer:innen nach einem Bereich von Betriebssystemen zu segmentieren, verwenden Sie den Filter <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#device-os-version-number\">Versionsnummer des Geräte-Betriebssystems</a>."
    tags:
      - Devices
  - name: Versionsnummer des Geräte-Betriebssystems
    description: "Segmentiert Ihre Nutzer:innen, die über ein oder mehrere Geräte mit einem Betriebssystem innerhalb eines bestimmten Bereichs verfügen. Sie können beispielsweise Nutzer:innen ansprechen, die über ein iOS-Betriebssystem der Version 26.0 oder höher verfügen."
    tags:
      - Devices
  - name: Neuestes Gebietsschema des Geräts
    description: "Segmentiert Ihre Nutzer:innen anhand der <a href=\"/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/\">Gebietsschema-Informationen</a> des zuletzt verwendeten Geräts."
    tags:
      - Devices
  - name: Aktuellstes Smartwatch-Modell
    description: "Segmentiert Ihre Nutzer:innen nach ihrem neuesten Smartwatch-Modell."
    tags:
      - Devices
  - name: Vorläufige Autorisierung unter iOS
    description: "Ermöglicht es Ihnen, Nutzer:innen zu finden, die unter iOS 12 für eine bestimmte App vorläufig autorisiert sind."
    tags:
      - Devices
  - name: Webbrowser
    description: "Segmentiert Ihre Nutzer:innen nach dem Webbrowser, den sie für den Zugriff auf Ihre Website verwenden."
    tags:
      - Devices
  - name: Geräte-IDFA
    description: "Ermöglicht es Ihnen, die Empfänger:innen Ihrer Kampagnen zu Testzwecken nach IDFA zu bestimmen."
    tags:
      - Advertising use cases
  - name: Geräte-IDFV
    description: "Ermöglicht es Ihnen, die Empfänger:innen Ihrer Kampagnen zu Testzwecken nach IDFV zu bestimmen."
    tags:
      - Advertising use cases
  - name: Google-Werbe-ID des Geräts
    description: "Segmentiert Ihre Nutzer:innen nach der Google-Werbe-ID."
    tags:
      - Advertising use cases
  - name: Roku-Werbe-ID des Geräts
    description: "Segmentiert Ihre Nutzer:innen nach der Roku-Werbe-ID."
    tags:
      - Advertising use cases
  - name: Windows-Werbe-ID des Geräts
    description: "Segmentiert Ihre Nutzer:innen nach der Windows-Werbe-ID."
    tags:
      - Advertising use cases
  - name: Ad-Tracking aktiviert
    description: "Ermöglicht es Ihnen, danach zu filtern, ob Ihre Nutzer:innen dem Ad-Tracking zugestimmt haben. Ad-Tracking bezieht sich auf den IDFA oder „Identifier for Advertisers", der allen iOS-Geräten von Apple zugewiesen wird und der von SDKs eingestellt werden kann. Dieser Bezeichner ermöglicht es Werbetreibenden, Nutzer:innen zu verfolgen und ihnen gezielte Werbung anzuzeigen."
    tags:
      - Advertising use cases
  - name: Letzter Standort
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten aufgezeichneten Standort, an dem sie Ihre App genutzt haben."
    tags:
      - Location
  - name: Standort verfügbar
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie ihren Standort gemeldet haben oder nicht. Um diesen Filter verwenden zu können, muss in Ihrer App <a href=\"/docs/search/?query=location%20tracking\">das Standort-Tracking integriert sein.</a>"
    tags:
      - Location
  - name: Amplitude-Kohorten
    description: "Kund:innen, die Amplitude verwenden, können ihre Segmente durch Auswahl und Import ihrer Kohorten in Amplitude ergänzen."
    tags:
      - Cohort membership
  - name: Census-Kohorten
    description: "Kund:innen, die Census verwenden, können ihre Segmente durch Auswahl und Import ihrer Kohorten in Census ergänzen."
    tags:
      - Cohort membership
  - name: Heap-Kohorten
    description: "Kund:innen, die Heap verwenden, können ihre Segmente ergänzen, indem sie ihre Kohorten in Heap auswählen und importieren."
    tags:
      - Cohort membership
  - name: Hightouch-Kohorten
    description: "Kund:innen, die Hightouch verwenden, können ihre Segmente ergänzen, indem sie ihre Kohorten in Hightouch auswählen und importieren."
    tags:
      - Cohort membership
  - name: Kubit-Kohorten
    description: "Kund:innen, die Kubit verwenden, können ihre Segmente ergänzen, indem sie ihre Kohorten in Kubit auswählen und importieren."
    tags:
      - Cohort membership
  - name: Mixpanel-Kohorten
    description: "Kund:innen, die Mixpanel verwenden, können ihre Segmente ergänzen, indem sie ihre Kohorten in Mixpanel auswählen und importieren."
    tags:
      - Cohort membership
  - name: Segment-Kohorten
    description: "Kund:innen, die Segment verwenden, können ihre Segmente ergänzen, indem sie ihre Kohorten in Segment auswählen und importieren."
    tags:
      - Cohort membership
  - name: Tinyclues-Kohorten
    description: "Kund:innen, die Tinyclues verwenden, können ihre Segmente ergänzen, indem sie ihre Kohorten in Tinyclues auswählen und importieren."
    tags:
      - Cohort membership
  - name: Install-Attribution-Anzeige
    description: "Segmentiert Ihre Nutzer:innen nach der Anzeige, der ihre Installation zugewiesen wurde."
    tags:
      - User Attributes
  - name: Install-Attribution-Anzeigengruppe
    description: "Segmentiert Ihre Nutzer:innen nach der Anzeigengruppe, der ihre Installation zugewiesen wurde."
    tags:
      - Install attribution
  - name: Install-Attribution-Kampagne
    description: "Segmentiert Ihre Nutzer:innen nach der Werbekampagne, der ihre Installation zugewiesen wurde."
    tags:
      - Install attribution
  - name: Install-Attribution-Quelle
    description: "Segmentiert Ihre Nutzer:innen nach der Quelle, der ihre Installation zugeschrieben wurde."
    tags:
      - Install attribution
  - name: Kategorie „Abwanderungsrisiko"
    description: "Segmentiert Ihre Nutzer:innen nach Abwanderungsrisiko-Kategorie gemäß einer bestimmten Prognose."
    tags:
      - Intelligence and predictive
  - name: Abwanderungsrisiko-Score
    description: "Segmentiert Ihre Nutzer:innen nach dem Abwanderungsrisiko-Score gemäß einer bestimmten Prognose."
    tags:
      - Intelligence and predictive
  - name: Kategorie „Event-Wahrscheinlichkeit"
    description: "Segmentiert Ihre Nutzer:innen nach der Wahrscheinlichkeit, ein Event gemäß einer bestimmten Prognose durchzuführen."
    tags:
      - Intelligence and predictive
  - name: Event-Wahrscheinlichkeits-Score
    description: "Segmentiert Ihre Nutzer:innen nach der Wahrscheinlichkeit, ein Event gemäß einer bestimmten Prognose durchzuführen."
    tags:
      - Intelligence and predictive
  - name: Intelligenter Kanal
    description: "Segmentiert Ihre Nutzer:innen nach ihrem aktivsten Kanal in den letzten drei Monaten."
    tags:
      - Intelligence and predictive
  - name: Wahrscheinlichkeit der Nachrichtenöffnung
    description: "Filtert Ihre Nutzer:innen anhand der <a href=\"/docs/user_guide/brazeai/intelligence/intelligent_channel/#individual-channels\">Wahrscheinlichkeit, mit der sie eine Nachricht auf einem bestimmten Kanal öffnen,</a> auf einer Skala von 0 bis 100 %. Nutzer:innen ohne ausreichende Daten, um eine Wahrscheinlichkeit für einen Kanal zu messen, können mit „ist leer" ausgewählt werden.<br><br>Bei E-Mails werden maschinelle Öffnungen aus der Wahrscheinlichkeitsberechnung ausgeschlossen."
    tags:
      - Intelligence and predictive
  - name: Anzahl der Facebook-Freunde, die die App nutzen
    description: "Segmentiert Ihre Nutzer:innen danach, wie viele Facebook-Freunde sie haben, die dieselbe App verwenden."
    tags:
      - Social activity
  - name: Mit Facebook verbunden
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie Ihre App mit Facebook verbunden haben."
    tags:
      - Social activity
  - name: Mit X verbunden
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie Ihre App mit X (früher Twitter) verbunden haben."
    tags:
      - Social activity
  - name: Anzahl der X-Follower
    description: "Segmentiert Ihre Nutzer:innen danach, wie viele X (früher Twitter) Follower sie haben."
    tags:
      - Social activity
  - name: Telefonnummer
    description: "Segmentiert Ihre Nutzer:innen nach dem E.164-formatierten Telefonnummernfeld.<br><br> Wenn eine Telefonnummer an Braze gesendet wird, versucht Braze, sie in das <a href=\"/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers\">E.164-Format</a> zu konvertieren, das für den Versand über SMS- und WhatsApp-Kanäle verwendet wird. Der Konvertierungsprozess kann fehlschlagen, wenn die Nummer nicht richtig formatiert ist, was dazu führt, dass das Nutzerprofil zwar eine unformatierte Telefonnummer, aber keine sendende Telefonnummer enthält. Dieser Segmentfilter gibt Nutzer:innen nach ihrer E.164-formatierten Telefonnummer zurück (sofern verfügbar).<br><br>Anwendungsfälle:<br> - Verwenden Sie diesen Filter, um beim Versenden von SMS- oder WhatsApp-Nachrichten die genaueste Größe der Zielgruppe zu ermitteln.  <br>- Verwenden Sie mit diesem Filter reguläre Ausdrücke (Regex), um nach Telefonnummern mit einer bestimmten Landesvorwahl zu segmentieren. <br>- Verwenden Sie diesen Filter, um Nutzer:innen nach Telefonnummern zu segmentieren, bei denen die E.164-Konvertierung fehlgeschlagen ist."
    tags:
      - Other Filters
---