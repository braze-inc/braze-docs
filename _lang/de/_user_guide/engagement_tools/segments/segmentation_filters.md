---
page_order: 2
nav_title: Segmentierungsfilter
article_title: Filter für die Segmentierung
layout: glossary_page
glossary_top_header: "Segmentation Filters"
glossary_top_text: The Braze SDK provides you with a powerful arsenal of filters to segment and target your users based off of specific features and attributes. You can search or narrow these filters by filter category.<br><br>To learn about the different custom attribute data types you can use to segment users, view <a href="/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types">Custom attribute data types</a>.

page_type: glossary
tool: Segments
description: "Dieses Glossar listet die verfügbaren Filter auf, mit denen Sie Ihre Benutzer segmentieren und gezielt ansprechen können."
search_rank: 2
glossary_tag_name: Filter Category
glossary_filter_text: "Select a category to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Segment- oder CSV-Zugehörigkeit
  - name: Angepasste Attribute
  - name: Angepasste Events
  - name: Sitzungen
  - name: Retargeting
  - name: Kanalspezifisches Aboverhalten
  - name: Kaufverhalten
  - name: Demografische Attribute
  - name: App
  - name: Deinstallation
  - name: Geräte
  - name: Standort
  - name: Kohortenzugehörigkeit
  - name: Install-Attribution
  - name: Intelligence und Predictive
  - name: Social-Aktivitäten
  - name: Andere Filter

glossaries:
  - name: Segmentzugehörigkeit
    description: "Ermöglicht es Ihnen, überall dort, wo Filter verwendet werden (z. B. Segmente, Kampagnen und andere), nach der Segmentzugehörigkeit zu filtern und mehrere verschiedene Segmente innerhalb einer Kampagne anzusprechen. <br><br>Beachten Sie, dass Segmente, die diesen Filter bereits verwenden, nicht weiter in andere Segmente eingeschlossen oder verschachtelt werden können, da dies zu einem Zyklus führen kann, bei dem Segment A Segment B einschließt, das dann wiederum versucht, Segment A einzuschließen. In diesem Fall würde das Segment immer wieder auf sich selbst verweisen, so dass es unmöglich wäre, zu berechnen, wer tatsächlich dazugehört. Außerdem wird die Verschachtelung von Segmenten auf diese Weise komplizierter und kann die Arbeit verlangsamen. Erstellen Sie stattdessen das Segment, das Sie einbeziehen möchten, mit denselben Filtern neu."
    tags:
      - Segment or CSV membership
  - name: Braze-Segmenterweiterungen
    description: "Nachdem Sie eine Segmenterweiterung im Braze Dashboard erstellt haben, können Sie wählen, ob Sie diese Erweiterungen in Ihr Segment aufnehmen oder ausschließen möchten."
    tags:
      - Segment or CSV membership
  - name: Aktualisiert/Importiert aus CSV
    description: "Segmentiert Ihre Benutzer danach, ob sie an einem CSV-Upload beteiligt waren oder nicht."
    tags:
      - Segment or CSV membership
  - name: Angepasste Attribute
    description: "Ermittelt, ob ein:e Nutzer:in mit einem angepassten Attribut-Wert übereinstimmt oder nicht. <br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Custom attributes
  - name: Erstellt am
    description: "Unterteilt die Benutzer danach, wann ihr Benutzerprofil erstellt wurde. Wenn ein:e Nutzer:in per CSV oder API hinzugefügt wurde, zeigt dieser Filter das Datum an, an dem er hinzugefügt wurde. Wenn der oder die Nutzer:in nicht per CSV oder API hinzugefügt wurde und seine erste Sitzung durch das SDK getrackt wurde, spiegelt dieser Filter das Datum dieser ersten Sitzung wider."
    tags:
      - Other Filters
  - name: Verschachtelte angepasste Attribute
    description: "Attribute, die die Eigenschaften von benutzerdefinierten Attributen sind.<br><br>Beim Filtern eines verschachtelten nutzerdefinierten Zeitattributs können Sie wählen, ob Sie nach „Tag des Jahres“ oder „Zeit“ filtern möchten. Bei \"Tag des Jahres\" werden nur der Monat und der Tag zum Vergleich herangezogen. \"Zeit\" vergleicht den vollständigen Zeitstempel, einschließlich des Jahres."
    tags:
      - Custom attributes
  - name: Tag des wiederkehrenden Events
    description: "Dieser Filter betrachtet den Monat und den Tag eines benutzerdefinierten Attributs mit dem Datentyp \"Datum\", aber nicht das Jahr. Dieser Filter ist nützlich für jährliche Events.<br><br>Zeitzone:<br>Dieser Filter passt sich an alle Zeitzonen an, in denen sich der Nutzer:innen befindet, sofern die Nachricht mit der Option für die Lokalisierung des Zeitplans gesendet wird. Andernfalls verwendet dieser Filter die Zeitzone Ihres Unternehmens."
    tags:
      - Custom attributes
  - name: Angepasstes Event
    description: "Ermittelt, ob ein:e Nutzer:in ein speziell aufgezeichnetes Event durchgeführt hat oder nicht.<br><br> Beispiel:<br>Aktivität mit der Eigenschaft activty_name abgeschlossen.<br><br>Zeitzone:<br>UTC - Kalendertag = 1 Kalendertag betrachtet 24-48 Stunden der Benutzerhistorie"
    tags:
      - Custom events
  - name: Erste Durchführung von angepasstem Event
    description: "Ermittelt den frühesten Zeitpunkt, zu dem ein:e Nutzer:in ein speziell aufgezeichnetes Event durchgeführt hat. (24-Stunden-Zeitraum) <br><br>Beispiel:<br> Erster abgebrochener Warenkorb Vor weniger als 1 Tag<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Custom events
  - name: Letzte Durchführung von angepasstem Event 
    description: "Ermittelt den spätesten Zeitpunkt, an dem ein:e Nutzer:inn ein speziell aufgezeichnetes Event durchgeführt hat. Dieser Filter unterstützt Dezimalzahlen, z.B. 0,25 Stunden. (24-Stunden-Zeitraum) <br><br>Beispiel:<br> Letzter verlassener Warenkorb Vor weniger als 1 Tag<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Custom events
  - name: X angepasstes Event in Y Tagen
    description: "Ermittelt, ob ein:e Nutzer:in in der letzten angegebenen Anzahl von Kalendertagen zwischen 1 und 30 ein speziell aufgezeichnetes Event zwischen 0 und 50 Mal durchgeführt hat oder nicht. (Kalendertag = 1 Kalendertag betrachtet 24-48 Stunden der Benutzerhistorie)<br> <a href=\"/docs/x-in-y-behavior/\"> Erfahren Sie hier mehr über das X-in-Y-Verhalten.</a> <br><br>Beispiel:<br>In den letzten 1 Kalendertagen genau 0 Mal den Warenkorb verlassen<br><br>Zeitzone:<br>UTC - Um alle Zeitzonen zu berücksichtigen, werden für 1 Kalendertag 24-48 Stunden der Benutzerhistorie betrachtet, je nachdem, zu welchem Zeitpunkt das Segment ausgewertet wird; für 2 Kalendertage werden 48-72 Stunden der Benutzerhistorie betrachtet und so weiter."
    tags:
      - Custom events
  - name: X angepasstes eigenschaftsbezogenes Event in Y Tagen
    description: "Ermittelt, ob ein Benutzer ein speziell aufgezeichnetes Ereignis in Bezug auf eine bestimmte Eigenschaft zwischen 0 und 50 Mal in der letzten angegebenen Anzahl von Kalendertagen zwischen 1 und 30 durchgeführt hat oder nicht. (Kalendertag = 1 Kalendertag betrachtet 24-48 Stunden der Benutzerhistorie)<br><a href=\"/docs/x-in-y-behavior/\">Erfahren Sie hier mehr über das X-in-Y-Verhalten.</a> <br><br>Beispiel:<br> Zu den Favoriten hinzugefügt mit der Eigenschaft \"event_name\" genau 0 Mal in den letzten 1 Kalendertag<br><br>Zeitzone:<br>UTC - Um alle Zeitzonen zu berücksichtigen, werden für 1 Kalendertag 24-48 Stunden der Benutzerhistorie betrachtet, je nachdem, zu welchem Zeitpunkt das Segment ausgewertet wird; für 2 Kalendertage werden 48-72 Stunden der Benutzerhistorie betrachtet und so weiter."
    tags:
      - Custom events
  - name: E-Mail-Adresse 
    description: "Ermöglicht es Ihnen, Ihre Kampagnenempfänger zu Testzwecken nach einzelnen E-Mail-Adressen zu benennen. Sie können damit auch Transaktions-E-Mails an alle Ihre Nutzer:innen (auch an die, die sich abgemeldet haben) senden, indem Sie im Filter den Parameter \"E-Mail-Adresse ist nicht leer\" angeben. So können Sie die Zustellung von E-Mails unabhängig vom Opt-in-Status maximieren. <br><br>Dieser Filter prüft nur, ob Nutzerprofile eine E-Mail Adresse haben, während der Filter <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-available\">E-Mail verfügbar</a> nach zusätzlichen Kriterien prüft."
    tags:
      - Other Filters
  - name: Externe Nutzer-ID
    description: "Ermöglicht es Ihnen, Ihre Kampagnenempfänger zu Testzwecken nach individuellen Benutzer-IDs zu benennen."
    tags:
      - Other Filters
  - name: "Zufällige Bucket-Nr."
    description: "Segmentiert Ihre Benutzer nach einer zufällig zugewiesenen Nummer (0 bis 9999 einschließlich). Sie kann die Erstellung gleichmäßig verteilter Segmente von wirklich zufälligen Nutzer:innen für A/B- und multivariate Tests ermöglichen."
    tags:
      - Other Filters
  - name: Sitzungsanzahl
    description: "Segmentiert Ihre Benutzer nach der Anzahl der Sitzungen, die sie in einer Ihrer Anwendungen innerhalb Ihres Arbeitsbereichs hatten."
    tags:
      - Sessions
  - name: Sitzungsanzahl für App
    description: "Segmentiert Ihre Nutzer:innen nach der Anzahl der Sitzungen, die sie in einer bestimmten, festgelegten App hatten."
    tags:
      - Sessions
  - name: X Sitzungen in den letzten Y Tagen
    description: "Segmentiert Ihre Benutzer nach der Anzahl der Sitzungen (zwischen 0 und 50), die sie in Ihrer App in der letzten angegebenen Anzahl von Kalendertagen zwischen 1 und 30 hatten. <br> <a href=\"/docs/x-in-y-behavior/\">Erfahren Sie hier mehr über das X-in-Y-Verhalten.</a>"
    tags:
      - Sessions
  - name: Erste App-Nutzung
    description: "Segmentiert Ihre Nutzer nach dem frühesten aufgezeichneten Zeitpunkt, zu dem sie Ihre App geöffnet haben. <em>Beachten Sie, dass damit die erste Sitzung erfasst wird, die sie mit einer Version Ihrer App mit integriertem Braze-SDK durchführen.</em> (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Sessions
  - name: Erste Nutzung einer bestimmten App
    description: "Segmentiert Ihre Benutzer nach dem frühesten aufgezeichneten Zeitpunkt, zu dem sie eine Ihrer Anwendungen innerhalb Ihres Arbeitsbereichs geöffnet haben. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Sessions
  - name: Letzte App-Nutzung
    description: "Segmentiert Ihre Nutzer nach dem Zeitpunkt, an dem sie Ihre App zuletzt geöffnet haben. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Sessions
  - name: Letzte Nutzung einer bestimmten App
    description: "Segmentiert Ihre Nutzer nach dem Zeitpunkt, an dem sie zuletzt eine bestimmte App geöffnet haben. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Sessions
  - name: Mediane Sitzungsdauer
    description: Segmentiert Ihre Nutzer nach der durchschnittlichen Länge ihrer Sitzungen in Ihrer App.
    tags:
      - Sessions
  - name: Hat Nachricht aus Kampagne empfangen
    description: "Segmentiert Ihre Nutzer danach, ob sie eine bestimmte Kampagne erhalten haben oder nicht.<br><br> Bei Content-Cards, Bannern und In-App-Nachrichten ist dies der Zeitpunkt, an dem ein Nutzer:innen eine Impression protokolliert, nicht der Zeitpunkt, an dem die Karte oder die In-App-Nachricht gesendet wird.<br><br>Bei Push- und Webhooks ist dies der Zeitpunkt, an dem die Nachricht an den Benutzer gesendet wird.<br><br> Bei WhatsApp ist dies der Zeitpunkt, an dem die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht der Zeitpunkt, an dem die Nachricht an das Gerät des Benutzers geliefert wird. <br><br>Bei E-Mails ist dies der Zeitpunkt, an dem eine E-Mail-Anfrage an den E-Mail-Dienstanbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird). Wenn mehrere Benutzer dieselbe E-Mail-Adresse verwenden:<br>- Beim ersten Senden wird nur das Profil des oder der spezifischen Targeting-Nutzer:in aktualisiert. <br>- Wenn die E-Mail zugestellt wird oder wenn der Benutzer die E-Mail oder einen Link in der E-Mail öffnet, scheinen alle Benutzer, die die gleiche E-Mail-Adresse haben, die Nachricht erhalten zu haben.<br><br>Bei SMS ist dies der Zeitpunkt, an dem die letzte Nachricht an den SMS-Anbieter zugestellt wurde. Dies ist keine Garantie dafür, dass die Nachricht auf dem Gerät des Benutzers angekommen ist."
    tags:
      - Retargeting
  - name: Empfangene Kampagnenvariante
    description: "Segmentiert Ihre Nutzer danach, welche Variante einer multivariaten Kampagne sie erhalten haben.<br><br> Bei Content-Cards, Bannern und In-App-Nachrichten ist dies der Zeitpunkt, an dem ein Nutzer:innen eine Impression protokolliert, nicht der Zeitpunkt, an dem die Karte oder die In-App-Nachricht gesendet wird.<br><br>Bei Push- und Webhooks ist dies der Zeitpunkt, an dem die Nachricht an den Benutzer gesendet wird.<br><br> Bei WhatsApp ist dies der Zeitpunkt, an dem die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht der Zeitpunkt, an dem die Nachricht an das Gerät des Benutzers geliefert wird. <br><br>Bei E-Mails ist dies der Zeitpunkt, an dem eine E-Mail-Anfrage an den E-Mail-Dienstanbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird). Wenn mehrere Benutzer dieselbe E-Mail-Adresse verwenden:<br>- Beim ersten Senden wird nur das Profil des oder der spezifischen Targeting-Nutzer:in aktualisiert. <br>- Wenn die E-Mail zugestellt wird oder wenn der Benutzer die E-Mail oder einen Link in der E-Mail öffnet, scheinen alle Benutzer, die die gleiche E-Mail-Adresse haben, die Nachricht erhalten zu haben.<br><br>Bei SMS ist dies der Zeitpunkt, an dem die letzte Nachricht an den SMS-Anbieter zugestellt wurde. Dies ist keine Garantie dafür, dass die Nachricht auf dem Gerät des Benutzers angekommen ist."
    tags:
      - Retargeting
  - name: Hat Nachricht aus Canvas-Schritt empfangen
    description: "Unterteilt Ihre Nutzer danach, ob sie eine bestimmte Canvas-Komponente erhalten haben oder nicht.<br><br> Bei Content-Cards und In-App-Nachrichten ist dies der Zeitpunkt, an dem ein:e Nutzer:in eine Impression protokolliert, nicht der Zeitpunkt, an dem die Karte oder In-App-Nachricht gesendet wird.<br><br>Bei Push- und Webhooks ist dies der Zeitpunkt, an dem die Nachricht an den Benutzer gesendet wird.<br><br> Bei WhatsApp ist dies der Zeitpunkt, an dem die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht der Zeitpunkt, an dem die Nachricht an das Gerät des Benutzers geliefert wird. <br><br>Bei E-Mails ist dies der Zeitpunkt, an dem eine E-Mail-Anfrage an den E-Mail-Dienstanbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird). Wenn mehrere Benutzer dieselbe E-Mail-Adresse verwenden:<br>- Beim ersten Senden wird nur das Profil des oder der spezifischen Targeting-Nutzer:in aktualisiert. <br>- Wenn die E-Mail zugestellt wird oder wenn der Benutzer die E-Mail oder einen Link in der E-Mail öffnet, scheinen alle Benutzer, die die gleiche E-Mail-Adresse haben, die Nachricht erhalten zu haben.<br><br>Bei SMS ist dies der Zeitpunkt, an dem die letzte Nachricht an den SMS-Anbieter zugestellt wurde. Dies ist keine Garantie dafür, dass die Nachricht auf dem Gerät des Benutzers angekommen ist."
    tags:
      - Retargeting
  - name: Letzte empfangene Nachricht aus einem bestimmten Canvas-Schritt
    description: "Segmentiert Ihre Nutzer danach, wann sie eine bestimmte Canvas-Komponente erhalten haben. Dieser Filter berücksichtigt nicht, wenn Benutzer andere Canvas-Komponenten erhalten haben."
    tags:
      - Retargeting
  - name: Letzte empfangene Nachricht aus einer bestimmten Kampagne
    description: "Segmentiert Ihre Nutzer danach, ob sie eine bestimmte Kampagne erhalten haben oder nicht. Dieser Filter berücksichtigt nicht, wann Benutzer andere Kampagnen erhalten haben."
    tags:
      - Retargeting
  - name: Hat Nachricht aus Kampagne oder Canvas mit Tag empfangen
    description: "Segmentiert Ihre Nutzer danach, ob sie eine bestimmte Kampagne oder Leinwand mit einem bestimmten Tag erhalten haben oder nicht.<br><br> Bei Content-Cards, Bannern (nur Kampagnen) und In-App-Nachrichten ist dies der Zeitpunkt, an dem ein Nutzer:innen eine Impression protokolliert, nicht der Zeitpunkt, an dem die Karte oder die In-App-Nachricht gesendet wird.<br><br>Bei Push- und Webhooks ist dies der Zeitpunkt, an dem die Nachricht an den Benutzer gesendet wird.<br><br> Bei WhatsApp ist dies der Zeitpunkt, an dem die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht der Zeitpunkt, an dem die Nachricht an das Gerät des Benutzers geliefert wird. <br><br>Bei E-Mails ist dies der Zeitpunkt, an dem eine E-Mail-Anfrage an den E-Mail-Dienstanbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird). Wenn mehrere Benutzer dieselbe E-Mail-Adresse verwenden:<br>- Beim ersten Senden wird nur das Profil des oder der spezifischen Targeting-Nutzer:in aktualisiert. <br>- Wenn die E-Mail zugestellt wird oder wenn der Benutzer die E-Mail oder einen Link in der E-Mail öffnet, scheinen alle Benutzer, die die gleiche E-Mail-Adresse haben, die Nachricht erhalten zu haben.<br><br>Bei SMS ist dies der Zeitpunkt, an dem die letzte Nachricht an den SMS-Anbieter zugestellt wurde. Dies ist keine Garantie dafür, dass die Nachricht auf dem Gerät des Benutzers angekommen ist."
    tags:
      - Retargeting
  - name: Letzte empfangene Nachricht aus einer Kampagne oder einem Canvas mit Tag
    description: "Segmentieren Sie Ihre Nutzer danach, wann sie eine bestimmte Kampagne oder Leinwand mit einem bestimmten Tag erhalten haben. Dieser Filter berücksichtigt nicht, wenn Benutzer andere Kampagnen oder Canvases erhalten haben. (24-Stunden-Zeitraum)"
    tags:
      - Retargeting
  - name: Hat nie eine Nachricht aus der Kampagne oder dem Canvas-Schritt empfangen
    description: "Segmentiert Ihre Nutzer danach, ob sie eine Kampagne oder eine Canvas-Komponente erhalten haben oder nicht."
    tags:
      - Retargeting
  - name: Letzte empfangene E-Mail
    description: "Segmentiert Ihre Nutzer nach dem letzten Mal, dass sie eine Ihrer E-Mail-Nachrichten erhalten haben. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Letzter empfangener Push
    description: "Segmentiert Ihre Nutzer nach dem letzten Mal, als sie eine Ihrer Push-Benachrichtigungen erhalten haben. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Letzte In-App-Nachricht-Impression
    description: "Segmentiert Ihre Nutzer nach dem letzten Mal, als sie eine In-App-Nachricht angesehen haben."
    tags:
      - Retargeting
  - name: Letzte empfangene SMS
    description: "Segmentiert Ihre Nutzer nach dem Zeitpunkt, zu dem die letzte Nachricht an den SMS-Anbieter zugestellt wurde. Dies ist keine Garantie dafür, dass die Nachricht auf dem Gerät des Benutzers angekommen ist. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Letzter empfangener Webhook
    description: "Segmentiert Ihre Benutzer nach dem letzten Mal, als Braze einen Webhook für diesen Benutzer gesendet hat. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Letzte empfangene WhatsApp
    description: "Segmentiert Ihre Nutzer nach dem letzten Zeitpunkt, an dem sie eine WhatsApp-Nachricht erhalten haben. Dies ist der Zeitpunkt, an dem die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wird, nicht der Zeitpunkt, an dem die Nachricht an das Gerät des Benutzers geliefert wird. (24-Stunden-Zeitraum)<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Kampagne angeklickt/geöffnet
    description: "Filtern Sie nach der Interaktion mit einer bestimmten Kampagne. Bei E-Mail Messaging umfasst das Öffnungsereignis sowohl maschinell geöffnete als auch nicht maschinell geöffnete Nachrichten.<br><br> Bei E-Mails umfasst dies auch die Option, nach \"geöffneten E-Mails (Maschinenöffnungen)\" und \"geöffneten E-Mails (andere Öffnungen)\" zu filtern. Wenn mehrere Benutzer dieselbe E-Mail-Adresse verwenden:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden die Profile aller anderen Benutzer mit der gleichen E-Mail-Adresse ebenfalls aktualisiert. <br>- Wenn der ursprüngliche Benutzer seine E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändert, wird das Öffnen oder Klicken auf alle verbleibenden Benutzer mit dieser E-Mail-Adresse anstelle des ursprünglichen Benutzers angewendet.<br><br>Für SMS ist eine Interaktion definiert als:<br>- Der Benutzer hat zuletzt eine Antwort-SMS gesendet, die einer bestimmten Stichwortkategorie entspricht. Dies wird der letzten Kampagne zugeschrieben, die alle Nutzer mit dieser Telefonnummer erhalten haben. Die Kampagne muss in den letzten vier Stunden eingegangen sein.<br>- Der Benutzer hat zuletzt einen verkürzten Link in einer SMS-Nachricht ausgewählt, bei der die Klickverfolgung für den Benutzer aktiviert ist, und zwar in einer bestimmten Kampagne."
    tags:
      - Retargeting
  - name: Kampagne oder Canvas mit Tag angeklickt/geöffnet
    description: "Filtern Sie nach Interaktionen mit einer bestimmten Kampagne, die ein bestimmtes Tag hat. Bei E-Mail Messaging umfasst das Öffnungsereignis sowohl maschinell geöffnete als auch nicht maschinell geöffnete Nachrichten.<br><br> Für E-Mails beinhaltet dies die Option, nach \"geöffnete E-Mails (Maschinenöffnungen)\" und \"geöffnete E-Mails (andere Öffnungen)\" zu filtern. Wenn mehrere Benutzer dieselbe E-Mail-Adresse verwenden:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden die Profile aller anderen Benutzer mit der gleichen E-Mail-Adresse ebenfalls aktualisiert. <br>- Wenn der ursprüngliche Benutzer seine E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändert, wird das Öffnen oder Klicken auf alle verbleibenden Benutzer mit dieser E-Mail-Adresse anstelle des ursprünglichen Benutzers angewendet.<br><br>Für SMS ist eine Interaktion definiert als:<br>- Der Benutzer hat zuletzt eine Antwort-SMS gesendet, die einer bestimmten Stichwortkategorie entspricht. Dies wird der letzten Kampagne zugeschrieben, die alle Nutzer mit dieser Telefonnummer erhalten haben. Die Kampagne muss in den letzten vier Stunden eingegangen sein.<br>- Wenn der oder die Nutzer:in einer SMS-Nachricht, in der das Tracking von Klicks eingeschaltet ist, zuletzt einen verkürzten Link aus einer bestimmten Kampagne oder einem Canvas-Schritt mit Tag ausgewählt hat."
    tags:
      - Retargeting
  - name: Schritt angeklickt/geöffnet
    description: "Filtern Sie nach der Interaktion mit einer bestimmten Canvas-Komponente. Bei E-Mail Messaging umfasst das Öffnungsereignis sowohl maschinell geöffnete als auch nicht maschinell geöffnete Nachrichten.<br><br>Für E-Mails beinhaltet dies die Option, nach \"geöffnete E-Mails (Maschinenöffnungen)\" und \"geöffnete E-Mails (andere Öffnungen)\" zu filtern.<br><br>Für SMS ist eine Interaktion definiert als:<br>- Der Benutzer hat zuletzt eine Antwort-SMS gesendet, die einer bestimmten Stichwortkategorie entspricht. Dies wird der letzten Kampagne zugeschrieben, die alle Nutzer mit dieser Telefonnummer erhalten haben. Die Kampagne muss in den letzten vier Stunden eingegangen sein. <br>- Der oder die Nutzer:in hat zuletzt einen verkürzten Link in einer SMS-Nachricht ausgewählt, in der das Tracking von Nutzerklicks aktiviert ist, und zwar in einem bestimmten Canvas-Schritt."
    tags:
      - Retargeting
  - name: Alias in Kampagne angeklickt
    description: "Filtern Sie Ihre Nutzer danach, ob sie einen bestimmten Alias in einer bestimmten Kampagne angeklickt haben. Dies gilt nur für E-Mail-Nachrichten. <br><br> Wenn mehrere Benutzer dieselbe E-Mail-Adresse verwenden:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden die Profile aller anderen Benutzer mit der gleichen E-Mail-Adresse ebenfalls aktualisiert. <br>- Wenn der ursprüngliche Benutzer seine E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändert, wird das Öffnen oder Klicken auf alle verbleibenden Benutzer mit dieser E-Mail-Adresse anstelle des ursprünglichen Benutzers angewendet."
    tags:
      - Retargeting
  - name: Alias in Canvas-Schritt angeklickt
    description: "Filtern Sie Ihre Benutzer danach, ob sie einen bestimmten Alias in einem bestimmten Canvas angeklickt haben. Dies gilt nur für E-Mail-Nachrichten. <br><br> Wenn mehrere Benutzer dieselbe E-Mail-Adresse verwenden:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden die Profile aller anderen Benutzer mit der gleichen E-Mail-Adresse ebenfalls aktualisiert. <br>- Wenn der ursprüngliche Benutzer seine E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändert, wird das Öffnen oder Klicken auf alle verbleibenden Benutzer mit dieser E-Mail-Adresse anstelle des ursprünglichen Benutzers angewendet."
    tags:
      - Retargeting
  - name: Angeklickter Alias in einem beliebigen Kampagnen- oder Canvas-Schritt
    description: "Filtern Sie Ihre Nutzer danach, ob sie einen bestimmten Alias in einer Kampagne oder einem Canvas angeklickt haben. Dies gilt nur für E-Mail-Nachrichten. <br><br> Wenn mehrere Benutzer dieselbe E-Mail-Adresse verwenden:<br>- Wenn die E-Mail geöffnet oder angeklickt wird, werden die Profile aller anderen Benutzer mit der gleichen E-Mail-Adresse ebenfalls aktualisiert. <br>- Wenn der ursprüngliche Benutzer seine E-Mail-Adresse nach dem Senden der Nachricht und vor dem Öffnen oder Klicken ändert, wird das Öffnen oder Klicken auf alle verbleibenden Benutzer mit dieser E-Mail-Adresse anstelle des ursprünglichen Benutzers angewendet."
    tags:
      - Retargeting
  - name: Rückläufer (Hard Bounced)
    description: "Segmentieren Sie Ihre Nutzer:innen danach, ob ihre E-Mail-Adresse einen Hard Bounce aufweist (z. B. weil die E-Mail-Adresse ungültig ist)."
    tags:
      - Retargeting
  - name: Zustellfehler (Soft Bounced)
    description: "Segmentieren Sie Ihre Nutzer:innen danach, ob sie X-mal in Y Tagen einen Soft Bounce hatten. Segmentfilter können nur auf die letzten 30 Tage zurückblicken, aber mit Segmenterweiterungen können Sie weiter zurückblicken.<br><br>Dieser Filter funktioniert anders als ein Soft Bounce-Ereignis in Currents. Der Soft Bounced-Segmentfilter zählt einen Soft Bounce, wenn während der 72-stündigen Wiederholungsperiode keine erfolgreiche Zustellung stattgefunden hat. In Currents wird jeder erfolglose Wiederholungsversuch als Soft Bounce-Ereignis gesendet." 
    tags:
      - Retargeting
  - name: Hat Sie als Spam markiert
    description: "Unterteilt Ihre Nutzer danach, ob sie Ihre Nachrichten als Spam markiert haben oder nicht."
    tags:
      - Retargeting
  - name: Ungültige Telefonnummer 
    description: "Segmentiert Ihre Nutzer danach, ob ihre Telefonnummer ungültig ist oder nicht."
    tags:
      - Retargeting
  - name: Keyword-Kategorie der letzten gesendeten SMS
    description: "Segmentiert Ihre Nutzer danach, wann sie zuletzt eine SMS an eine bestimmte Abonnentengruppe innerhalb einer bestimmten Stichwortkategorie gesendet haben." 
    tags:
      - Retargeting
  - name: Von Kampagne konvertiert
    description: "Segmentiert Ihre Nutzer danach, ob sie bei einer bestimmten Kampagne konvertiert haben oder nicht. Dieser Filter schließt Nutzer:innen, die sich in der Kontrollgruppe befinden, nicht ein."
    tags:
      - Retargeting
  - name: Von Canvas konvertiert
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie auf einem bestimmten Canvas konvertiert haben oder nicht. Dieser Filter schließt Nutzer:innen, die sich in der Kontrollgruppe befinden, nicht ein."
    tags:
      - Retargeting
  - name: In Kampagnen-Kontrollgruppe
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie in der Kontrollgruppe für eine bestimmte multivariate Kampagne waren oder nicht."
    tags:
      - Retargeting
  - name: In Canvas-Kontrollgruppe
    description: "Segmentiert Ihre Nutzer danach, ob sie in der Kontrollgruppe für ein bestimmtes Canvas waren oder nicht. Dieser Filter wertet nur Benutzer aus, die das Canvas betreten haben.<br><br>Wenn Sie zum Beispiel nach Benutzern filtern, die nicht in der Kontrollgruppe für ein Canvas sind, erhalten Sie alle Benutzer, die das Canvas betreten haben, aber nicht in der Kontrollgruppe sind."
    tags:
      - Retargeting
  - name: Letzte Teilnahme an einer Kontrollgruppe
    description: "Segmentiert Ihre Nutzer nach dem letzten Mal, als sie in einer Kampagne in die Kontrollgruppe fielen. <br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: In Canvas-Variation aufgenommen
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie einen Variationspfad eines bestimmten Canvas eingegeben haben oder nicht. Dieser Filter wertet alle Benutzer aus.<br><br>Wenn Sie zum Beispiel nach Benutzern filtern, die nicht an einer Kontrollgruppe für die Canvas-Variation teilgenommen haben, erhalten Sie alle Benutzer, die nicht in der Kontrollgruppe sind, unabhängig davon, ob sie am Canvas teilgenommen haben."
    tags:
      - Retargeting
  - name: Empfangszeitpunkt der letzten Nachricht
    description: "Segmentiert Ihre Benutzer anhand der zuletzt erhaltenen Nachricht. (24-Stunden-Zeitraum)<br><br> Bei Content-Cards, Bannern und In-App-Nachrichten ist dies der Zeitpunkt, an dem ein Nutzer:innen zuletzt eine Impression erfasst hat, nicht der Zeitpunkt, an dem die Karte oder In-App-Nachricht zuletzt gesendet wurde.<br><br>Bei Push- und Webhooks ist dies der Zeitpunkt, an dem eine Nachricht an den Benutzer gesendet wurde.<br><br> Bei WhatsApp ist dies der Zeitpunkt, an dem die letzte Nachrichten-API-Anfrage an WhatsApp gesendet wurde, nicht der Zeitpunkt, an dem die Nachricht an das Gerät des Benutzers zugestellt wurde. <br><br>Bei E-Mails ist dies der Zeitpunkt, an dem eine E-Mail-Anfrage an den E-Mail-Dienstanbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird). Wenn mehrere Benutzer dieselbe E-Mail-Adresse verwenden:<br>- Beim ersten Senden wird nur das Profil des oder der spezifischen Targeting-Nutzer:in aktualisiert. <br>- Wenn die E-Mail zugestellt wird oder wenn der Benutzer die E-Mail oder einen Link in der E-Mail öffnet, scheinen alle Benutzer, die die gleiche E-Mail-Adresse haben, die Nachricht erhalten zu haben.<br><br>Bei SMS ist dies der Zeitpunkt, an dem die letzte Nachricht an den SMS-Anbieter zugestellt wurde. Dies ist keine Garantie dafür, dass die Nachricht auf dem Gerät des Benutzers angekommen ist.<br><br>Beispiel:<br>Letzte erhaltene Nachricht vor weniger als 1 Tag = vor weniger als 24 Stunden<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Letzte Interaktion mit Nachricht
    description: "Segmentiert Ihre Nutzer danach, wann sie das letzte Mal auf einen Ihrer Messaging-Kanäle (Banner, Content-Card, E-Mail, In-App, SMS, Push, WhatsApp) geklickt oder diesen geöffnet haben. Bei E-Mail Messaging umfasst das Öffnungsereignis sowohl maschinell geöffnete als auch nicht maschinell geöffnete Nachrichten. (24-Stunden-Zeitraum)<br><br>Bei E-Mails ist dies der Zeitpunkt, an dem eine E-Mail-Anfrage an den E-Mail-Dienstanbieter gesendet wird (unabhängig davon, ob sie tatsächlich zugestellt wird). Dazu gehört auch die Möglichkeit, nach \"geöffneten E-Mails (Maschinenöffnungen)\" und \"geöffneten E-Mails (andere Öffnungen)\" zu filtern. Wenn mehrere Benutzer dieselbe E-Mail-Adresse verwenden:<br>- Beim ersten Senden wird nur das Profil des oder der spezifischen Targeting-Nutzer:in aktualisiert. <br>- Wenn die E-Mail zugestellt wird oder wenn der Benutzer die E-Mail oder einen Link in der E-Mail öffnet, scheinen alle Benutzer, die die gleiche E-Mail-Adresse haben, die Nachricht erhalten zu haben.<br><br>Bei SMS ist dies der Zeitpunkt, an dem der Benutzer zuletzt einen verkürzten Link in einer Nachricht ausgewählt hat, für die die Klickverfolgung aktiviert ist.<br><br>Zeitzone:<br>Zeitzone des Unternehmens"
    tags:
      - Retargeting
  - name: Angeklickte Karte 
    description: "Segmentiert Ihre Nutzer danach, ob sie auf eine bestimmte Inhaltskarte geklickt haben oder nicht. Dieser Filter ist als Unterfilter für „angeklickte/geöffnete Kampagne“, „angeklickte/geöffnete Kampagne oder Canvas mit Tag“ und „angeklickter/geöffneter Schritt“ verfügbar."
    tags:
      - Retargeting
  - name: Feature-Flags
    description: "Das Segment Ihrer Nutzer:innen, bei denen ein bestimmtes <a href=\"/docs/developer_guide/feature_flags/\">Feature-Flag</a> derzeit aktiviert ist."
    tags:
      - Retargeting
  - name: Abo-Gruppe
    description: "Segmentiert Ihre Nutzer nach ihrer Abonnementgruppe für E-Mail, SMS/MMS oder WhatsApp. Archivierte Gruppen werden nicht angezeigt und können nicht verwendet werden."
    tags:
      - Channel subscription behavior
  - name: E-Mail-Adresse verfügbar
    description: "Segmentiert Ihre Nutzer:innen danach, ob sie eine gültige E-Mail-Adresse haben und ob sie ein Abonnent:in sind oder ein Opt-in für E-Mails haben. Dieser Filter prüft auf drei Kriterien: ob der Nutzer:innen sich von E-Mails abgemeldet hat, ob Braze einen Hard Bounce erhalten hat und ob die E-Mail als Spam markiert wurde. Wenn eines dieser Kriterien erfüllt ist, oder wenn für einen Benutzer keine E-Mail existiert, wird der Benutzer nicht berücksichtigt.<br><br>Beachten Sie, dass Nutzer:innen, deren \"E-Mail verfügbar\" <code>falsch</code> ist, nicht in die Berechnung der Zielgruppe einbezogen werden, aber dennoch eine Nachricht erhalten können, wenn Sie eine Transaktions-E-Mail senden. Bei der Berechnung der Zielgruppe werden jedoch nur Abonnent:innen oder Opt-in-Nutzer:innen berücksichtigt. <br><br>Für E-Mails, bei denen der Opt-in-Status wichtig ist, empfehlen wir die Verwendung des Filters \"E-Mail verfügbar\" anstelle des Filters \" <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-address\">E-Mail-Adresse\"</a>. Die zusätzlichen Kriterien können Ihnen helfen, Nutzer:innen zu targetieren, die Ihre Nachrichten wirklich sehen wollen."
    tags:
      - Channel subscription behavior
  - name: Datum des E-Mail-Opt-ins
    description: "Segmentiert Ihre Nutzer:innen nach dem Datum, an dem sie sich für E-Mails entschieden haben."
    tags:
      - Channel subscription behavior
  - name: E-Mail-Abostatus
    description: Segmentiert Ihre Benutzer nach ihrem Abonnementstatus für E-Mails.
    tags:
      - Channel subscription behavior
  - name: Datum der E-Mail-Abbestellung 
    description: "Segmentiert Ihre Nutzer:innen nach dem Datum, an dem sie sich von zukünftigen E-Mails abgemeldet haben."
    tags:
      - Channel subscription behavior
  - name: Foreground-Push aktiviert
    description: "Segmentiert Ihre Benutzer, die über eine vorläufige Push-Autorisierung verfügen oder für Push im Vordergrund aktiviert sind. Diese Zählung umfasst insbesondere:<br>1. iOS-Benutzer, die vorläufig für Push autorisiert sind. <br>2. Nutzer:innen, die Push im Vordergrund aktiviert haben und deren Push-Abonnementstatus nicht abgemeldet ist, für jede Ihrer Apps. Für diese Benutzer umfasst diese Zählung nur den Push im Vordergrund.<br><br>Bei Foreground Push Enablement werden Nutzer:innen, die sich abgemeldet haben, nicht berücksichtigt. <br><br>Nachdem Sie mit diesem Filter eine Segmentierung vorgenommen haben, können Sie im unteren Bereich mit der Bezeichnung <em>Erreichbare Nutzer</em> eine Aufschlüsselung der Mitglieder dieses Segments für Android, iOS und Web sehen."
    tags:
      - Channel subscription behavior
  - name: Push im Vordergrund für App aktiviert
    description: "Segmentiert danach, ob Nutzer Push für Ihre App auf ihrem Gerät aktiviert haben. Nutzer:innen, die für eine App Push im Vordergrund aktiviert haben. Der Status des Push-Abos wird dabei nicht berücksichtigt. Diese Zahl umfasst Benutzer, die vorläufig autorisierte Vordergrund- und Hintergrund-Push-Tokens haben."
    tags:
      - Channel subscription behavior
  - name: Push im Hinter- oder Vordergrund aktiviert
    description: "Segmentiert danach, ob Nutzer:innen ein Push-Token haben und sich nicht abgemeldet haben. Nutzer:innen, die im Hintergrund oder im Vordergrund Push für eine Ihrer Apps aktiviert haben."
    tags:
      - Channel subscription behavior
  - name: Datum des Push-Opt-ins
    description: "Segmentiert Ihre Nutzer:innen nach dem Datum, an dem sie sich für Push entschieden haben."
    tags:
      - Channel subscription behavior
  - name: Push-Abostatus
    description: "Segmentiert Ihre Nutzer nach ihrem <a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">Abonnementstatus</a> für Push."
    tags:
      - Channel subscription behavior
  - name: Datum der Push-Abmeldung
    description: "Segmentiert Ihre Nutzer nach dem Datum, an dem sie sich von zukünftigen Push-Benachrichtigungen abgemeldet haben."
    tags:
      - Channel subscription behavior
  - name: Gekauftes Produkt
    description: Segmentiert Ihre Nutzer nach den in Ihrer App gekauften Produkten.
    tags:
      - Purchase behavior
  - name: Gesamtzahl der Käufe
    description: "Segmentiert Ihre Nutzer danach, wie viele Käufe sie in Ihrer App getätigt haben."
    tags:
      - Purchase behavior
  - name: X Produktkäufe in Y Tagen
    description: "Filtern Sie Benutzer nach der Zeit, in der ein bestimmtes Produkt gekauft wurde."
    tags:
      - Purchase behavior
  - name: X Käufe in den letzten Y Tagen
    description: "Segmentiert Ihre Nutzer:innen nach der Anzahl der Käufe (zwischen 0 und 50), die sie in den letzten angegebenen Kalendertagen (zwischen 1 und 30) getätigt haben. <br> <a href=\"/docs/x-in-y-behavior/\">Erfahren Sie hier mehr über das X-in-Y-Verhalten.</a>"
    tags:
      - Purchase behavior
  - name: X Kaufeigenschaft in Y Tagen
    description: "Segmentiert Ihre Nutzer nach der Anzahl der Käufe, die in Bezug auf ein bestimmtes Kaufobjekt in den letzten angegebenen Kalendertagen zwischen 1 und 30 getätigt wurden. <br> <a href=\"/docs/x-in-y-behavior/\">Erfahren Sie hier mehr über das X-in-Y-Verhalten.</a>"
    tags:
      - Purchase behavior
  - name: Erster Kauf erfolgt
    description: "Segmentiert Ihre Nutzer nach dem frühesten Zeitpunkt, an dem ein Nutzer einen Kauf in Ihrer App getätigt hat."
    tags:
      - Purchase behavior
  - name: Erster Kauf für App
    description: "Segmentiert Ihre Nutzer nach dem frühesten Zeitpunkt, an dem ein Nutzer einen Kauf in Ihrer App getätigt hat."
    tags:
      - Purchase behavior
  - name: Letzter Kauf erfolgt
    description: "Filtern Sie die Benutzer nach dem letzten Kauf, den sie getätigt haben."
    tags: 
      - Purchase behavior
  - name: Letztes gekauftes Produkt
    description: "Filtern Sie Benutzer danach, wann sie zuletzt ein bestimmtes Produkt gekauft haben."
    tags:
      - Purchase behavior
  - name: Ausgegebener Betrag
    description: "Segmentiert Ihre Nutzer nach dem Geldbetrag, den sie in Ihrer App ausgegeben haben."
    tags:
      - Purchase behavior
  - name: X Geld ausgegeben in Y Tagen
    description: "Segmentiert Ihre Nutzer nach dem Geldbetrag, den sie in Ihrer App in der letzten angegebenen Anzahl von Kalendertagen zwischen 1 und 30 ausgegeben haben. Dieser Betrag umfasst nur die Summe der letzten 50 Einkäufe. <br> <a href=\"/docs/x-in-y-behavior/\">Erfahren Sie hier mehr über das X-in-Y-Verhalten.</a>"
    tags:
      - Purchase behavior
  - name: Land
    description: "Segmentiert Ihre Nutzer:innen nach ihrem zuletzt angegebenen Standort."
    tags:
      - Demographic attributes
  - name: Ort
    description: Segmentiert Ihre Nutzer nach ihrem zuletzt angegebenen Wohnort.
    tags:
      - Demographic attributes
  - name: Sprache
    description: Segmentiert Ihre Benutzer nach deren bevorzugter Sprache.
    tags:
      - Demographic attributes
  - name: Alter
    description: "Segmentiert Ihre Nutzer:innen nach ihrem Alter, das sie in Ihrer App angegeben haben."
    tags:
      - Demographic attributes
  - name: Geburtstag
    description: "Segmentiert Ihre Nutzer nach ihrem Geburtstag, den sie in Ihrer App angegeben haben. <br> Nutzer:innen mit einem Geburtstag am 29. Februar werden in Segmente bis einschließlich 1. März aufgenommen.<br><br>Wenn Sie auf Dezember- oder Januar-Geburtstage abzielen möchten, fügen Sie die Filterlogik nur innerhalb der 12-Monats-Spanne des Jahres ein, auf das Sie abzielen. Mit anderen Worten: Fügen Sie keine Logik ein, die bis zum Dezember des vorigen Kalenderjahres zurück oder bis zum Januar des nächsten Jahres vorwärts blickt. Um beispielsweise die Geburtstage im Dezember zu ermitteln, können Sie nach „am 31. Dezember“, „vor dem 31. Dezember“ oder „nach dem 30. November“ filtern."
    tags:
      - Demographic attributes
  - name: Geschlecht
    description: "Segmentiert Ihre Nutzer nach Geschlecht, wie sie es in Ihrer App angegeben haben."
    tags:
      - Demographic attributes
  - name: Unformatierte Telefonnummer
    description: "Segmentiert Ihre Nutzer:innen nach ihrer unformatierten Telefonnummer. Enthält keine Klammern, Bindestriche oder andere Symbole."
    tags:
      - Demographic attributes
  - name: Vorname
    description: "Segmentiert Ihre Nutzer nach ihrem Vornamen, den sie in Ihrer App angegeben haben."
    tags:
      - Demographic attributes
  - name: Nachname
    description: "Segmentiert Ihre Nutzer nach ihrem Nachnamen, den sie in Ihrer App angegeben haben."
    tags:
      - Demographic attributes
  - name: Hat App
    description: "Segmentiert danach, ob ein Nutzer Ihre App bereits installiert hat oder nicht. Dazu gehören Nutzer, die Ihre App derzeit installiert haben und solche, die sie in der Vergangenheit deinstalliert haben. Dies erfordert im Allgemeinen, dass Nutzer:innen die App öffnen (eine Sitzung starten), um in diesen Filter aufgenommen zu werden. Es gibt jedoch einige Ausnahmen, z. B. wenn ein: Nutzer:in in Braze importiert und manuell mit Ihrer App verknüpft wurde."
    tags:
      - App
  - name: Aktuellster Name der App-Version
    description: "Segmente nach dem aktuellen Namen der App des Nutzers oder der Nutzerin.<br><br>Wenn Sie \"kleiner als\" oder \"kleiner oder gleich\" verwenden und die Hauptversion der App nicht existiert, gibt dieser Filter `true` zurück, weil der Nutzer:in älter ist als die App-Version. Das heißt, wenn die letzte Hauptversion der App des Nutzers:innen nicht existiert, passt sie automatisch zu dem Filter."
    tags:
      - App 
  - name: Aktuellste Nummer der App-Version
    description: "Segmentiert nach der Versionsnummer der letzten App des Benutzers.<br><br>Wenn Sie \"kleiner als\" oder \"kleiner oder gleich\" verwenden und die Hauptversion der App nicht existiert, gibt dieser Filter `true` zurück, da der Nutzer:in älter ist als die App-Version. Das heißt, wenn die letzte Hauptversion der App des Nutzers:innen nicht existiert, passt sie automatisch zu dem Filter.<br><br>Es kann einige Zeit dauern, bis die aktuellen Versionen der Apps angezeigt werden. Die App-Version im Nutzerprofil wird aktualisiert, wenn die Informationen vom SDK erfasst werden, das sich darauf verlässt, wann Nutzer:innen ihre Apps öffnen. Wenn der Nutzer:innen die App nicht öffnet, wird die aktuelle Version nicht aktualisiert. Diese Filter können auch nicht rückwirkend angewendet werden. Es ist gut, \"größer als\" oder \"gleich\" für aktuelle und zukünftige Versionen zu verwenden, aber die Verwendung von Filtern für frühere Versionen kann zu unerwartetem Verhalten führen."
    tags:
      - App 
  - name: Deinstalliert
    description: "Unterteilt Ihre Nutzer danach, ob sie Ihre App deinstalliert und nicht neu installiert haben."
    tags:
      - Uninstall 
  - name: Netzbetreiber des Geräts
    description: "Segmentiert Ihre Nutzer:innen nach dem Netzbetreiber ihres Geräts"
    tags:
      - Devices
  - name: Gerätezahl
    description: "Segmentiert Ihre Nutzer:innen danach, auf wie vielen Geräten sie Ihre App verwendet haben."
    tags:
      - Devices
  - name: Gerätemodell
    description: Segmentiert Ihre Nutzer nach der Modellversion ihres Mobiltelefons.
    tags:
      - Devices
  - name: Betriebssystem
    description: "Segmentiert Ihre Benutzer, die über ein oder mehrere Geräte mit dem angegebenen Betriebssystem verfügen."
    tags:
      - Devices
  - name: Neuestes Gebietsschema des Geräts
    description: "Segmentiert Ihre Benutzer anhand der <a href=\"/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/\">Gebietsschema-Informationen</a> des zuletzt verwendeten Geräts."
    tags:
      - Devices      
  - name: Aktuellstes Smartwatch-Modell
    description: Segmentiert Ihre Nutzer nach ihrem neuesten Smartwatch-Modell.
    tags:
      - Devices    
  - name: Vorläufige Autorisierung unter iOS
    description: "Ermöglicht es Ihnen, Benutzer zu finden, die unter iOS 12 für eine bestimmte App vorläufig autorisiert sind."
    tags:
      - Devices   
  - name: Webbrowser
    description: "Segmentiert Ihre Nutzer nach dem Webbrowser, den sie für den Zugriff auf Ihre Website verwenden."
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
    description: Segmentiert Ihre Nutzer nach der Google-Anzeigen-ID.
    tags:
      - Advertising use cases
  - name: Roku-Werbe-ID des Geräts
    description: Segmentiert Ihre Nutzer nach der Roku-Anzeigen-ID.
    tags:
      - Advertising use cases
  - name: Windows-Werbe-ID des Geräts
    description: Segmentiert Ihre Nutzer nach der Windows-Anzeigen-ID.
    tags:
      - Advertising use cases  
  - name: Ad-Tracking aktiviert
    description: "Ermöglicht es Ihnen, danach zu filtern, ob Ihre Nutzer der Anzeigenverfolgung zugestimmt haben. Das Ad Tracking bezieht sich auf den IDFA oder „Identifier for Advertisers“, der allen iOS Geräten von Apple zugewiesen wird und der von SDKs eingestellt werden kann. Diese Kennung ermöglicht es Werbetreibenden, Nutzer zu verfolgen und ihnen gezielte Werbung anzuzeigen."
    tags:
      - Advertising use cases
  - name: Letzter Standort
    description: "Segmentiert Ihre Nutzer:innen nach dem letzten aufgezeichneten Standort, an dem sie Ihre App genutzt haben."
    tags:
      - Location
  - name: Standort verfügbar
    description: "Segmentiert Ihre Nutzer danach, ob sie ihren Standort gemeldet haben oder nicht. Um diesen Filter verwenden zu können, muss in Ihrer App <a href=\"/docs/search/?query=location%20tracking\">das Standort-Tracking integriert sein.</a>"
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
    description: "Segmentiert Ihre Nutzer nach der Anzeige, der ihre Installation zugewiesen wurde."
    tags:
      - User Attributes
  - name: Install-Attribution-Anzeigengruppe
    description: "Segmentiert Ihre Nutzer nach der Anzeigengruppe, der ihre Installation zugewiesen wurde."
    tags:
      - Install Attribution
  - name: Install-Attribution-Kampagne
    description: "Segmentiert Ihre Nutzer nach der Werbekampagne, der ihre Installation zugewiesen wurde."
    tags:
      - Install Attribution
  - name: Install-Attribution-Quelle
    description: "Segmentiert Ihre Nutzer:innen nach der Quelle, der ihre Installation zugeschrieben wurde."
    tags:
      - Install Attribution
  - name: Kategorie „Abwanderungsrisiko“
    description:  Segmentiert Ihre Nutzer nach Abwanderungsrisiko-Kategorie gemäß einer bestimmten Vorhersage.
    tags:
      - Intelligence and predictive
  - name: Abwanderungsrisiko-Score
    description: Segmentiert Ihre Nutzer nach dem Abwanderungsrisiko gemäß einer bestimmten Vorhersage.
    tags:
      - Intelligence and predictive
  - name: Kategorie „Event-Wahrscheinlichkeit“
    description: "Segmentiert Ihre Nutzer nach der Wahrscheinlichkeit, ein Ereignis gemäß einer bestimmten Vorhersage durchzuführen."
    tags:
      - Intelligence and predictive
  - name: Event-Wahrscheinlichkeits-Score
    description: "Segmentiert Ihre Nutzer nach der Wahrscheinlichkeit, ein Ereignis gemäß einer bestimmten Vorhersage durchzuführen."
    tags:
      - Intelligence and predictive
  - name: Intelligenter Kanal
    description: Segmentieren Sie Ihre Nutzer nach ihrem aktivsten Kanal in den letzten drei Monaten.
    tags:
      - Intelligence and predictive
  - name: Wahrscheinlichkeit der Nachrichtenöffnung
    description: "Filtert Ihre Nutzer auf der Grundlage ihrer Wahrscheinlichkeit, eine Nachricht auf einem bestimmten Kanal zu öffnen, auf einer Skala von 0-100%. Benutzer ohne ausreichende Daten, um eine Wahrscheinlichkeit für einen Kanal zu messen, können mit \"ist leer\" ausgewählt werden."
    tags:
      - Intelligence and predictive
  - name: "Anzahl der Facebook-Freunde, die die App nutzen"
    description: "Segmentiert Ihre Nutzer danach, wie viele Facebook-Freunde sie haben, die die gleiche App verwenden."
    tags:
      - Social activity
  - name: Mit Facebook verbunden
    description: "Segmentiert Ihre Nutzer danach, ob sie Ihre App mit Facebook verbunden haben."
    tags:
      - Social activity
  - name: Mit X verbunden
    description: "Segmentiert Ihre Nutzer danach, ob sie Ihre App mit X (früher Twitter) verbunden haben."
    tags:
      - Social activity
  - name: Anzahl der X-Follower
    description: "Segmentiert Ihre Nutzer danach, wie viele X (früher Twitter) Follower sie haben."
    tags:
      - Social activity
  - name: Telefonnummer
    description: "Segmentiert Ihre Nutzer:innen nach dem E.164-formatierten Rufnummernfeld.<br><br> Wenn eine Telefonnummer an Braze gesendet wird, versucht Braze, sie in das <a href=\"/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers\">e.164-Format</a> zu zwingen, das für den Versand über SMS- und WhatsApp-Kanäle verwendet wird. Der Zwangsprozess kann fehlschlagen, wenn die Nummer nicht richtig formatiert ist, was dazu führt, dass das Nutzerprofil zwar eine unformatierte Telefonnummer, aber keine sendende Telefonnummer enthält. Dieser Segmente Filter liefert Nutzer:innen nach ihrer e.164-formatierten Telefonnummer (sofern verfügbar).<br><br>Anwendungsfälle:<br> - Verwenden Sie diesen Filter, um beim Versenden von SMS- oder WhatsApp-Nachrichten die genaueste Größe der Zielgruppe zu ermitteln.  <br>- Verwenden Sie mit diesem Filter reguläre Ausdrücke (regex), um nach Telefonnummern mit einer bestimmten Landesvorwahl zu segmentieren. <br>- Verwenden Sie diesen Filter, um Nutzer:innen nach Telefonnummern zu segmentieren, die die e.164-Erzwingung nicht bestanden haben."
    tags:
      - Other filters
---
