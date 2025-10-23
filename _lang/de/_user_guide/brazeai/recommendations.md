---
nav_title: Artikel-Empfehlungen
article_title: Artikel-Empfehlungen in Braze
page_order: 15
search_rank: 1
description: "Erfahren Sie alles über Empfehlungssysteme für Artikel in Braze."
---

# Artikel-Empfehlungen

> Verbessern Sie Ihr Empfehlungssystem mit Braze, indem Sie ein Empfehlungssystem erstellen, das Ihren Nutzer:innen Artikel und Inhalte vorschlägt, die sie tatsächlich haben möchten. Von der Anpassung von Erlebnissen mit KI bis zum Aufbau eigener Engines mit Liquid oder Connected-Content finden Sie alles, was Sie brauchen, damit jede Empfehlung zählt.

## Voraussetzungen

Bevor Sie Artikel-Empfehlungen in Braze erstellen oder verwenden können, müssen Sie [mindestens einen Katalog erstellen - nur]({{site.baseurl}}/user_guide/data/activation/catalogs/create/)Artikel aus diesem Katalog werden den Nutzer:innen empfohlen.

## Typen und Anwendungsfälle

### KI Personalisiert {#ai}

Als Teil der Funktion [KI-Artikel-Empfehlungen]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/) nutzen die personalisierten KI-Empfehlungen Deep Learning, um vorherzusagen, wofür sich Ihre Nutzer als Nächstes interessieren werden, basierend auf dem, wofür sie sich in der Vergangenheit interessiert haben. Diese Methode bietet ein dynamisches und maßgeschneidertes Empfehlungssystem, das sich dem Nutzerverhalten anpasst.

Personalisierte KI-Empfehlungen verwenden die Daten der letzten 6 Monate zu Artikelinteraktionen, wie Käufe oder angepasste Events, um das Empfehlungsmodell zu erstellen. Für Benutzer, die nicht genügend Daten für eine personalisierte Liste haben, dienen die beliebtesten Artikel als Ausweichmöglichkeit, damit Ihre Benutzer immer noch relevante Vorschläge erhalten.

Mit den KI-Artikelempfehlungen können Sie die verfügbaren Artikel auch weiter mit
[Auswahlen]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) filtern. Allerdings können Auswahlen mit Liquid nicht in KI-Empfehlungen verwendet werden. Beachten Sie dies also, wenn Sie Ihre Katalogauswahlen erstellen.

{% alert tip %}
Personalisierte KI-Empfehlungen funktionieren am besten bei Hunderten oder Tausenden von Artikeln und typischerweise mindestens 30.000 Nutzer:innen mit Kauf- oder Interaktionsdaten. Dies ist nur ein grober Richtwert und kann variieren. Die anderen Empfehlungstypen können mit weniger Daten arbeiten.
{% endalert %}

#### Anwendungsfälle

Auf der Grundlage der getrackten Interaktionsdaten könnten die Anwendungsfälle für dieses Modell folgende sein:

{% tabs local %}
{% tab Most likely to purchase next %}
Sagen Sie voraus und empfehlen Sie die Artikel, die ein Benutzer wahrscheinlich als nächstes kaufen wird, basierend auf Kaufereignissen oder benutzerdefinierten Ereignissen im Zusammenhang mit Käufen. Zum Beispiel:

- Eine Reiseseite könnte auf der Grundlage des Browserverlaufs und früherer Buchungen eines Benutzers Urlaubspakete, Flüge oder Hotelaufenthalte vorschlagen und so das nächste Reiseziel vorhersehen und die Reiseplanung erleichtern.
- Eine Streaming-Plattform kann die Sehgewohnheiten analysieren, um einem Nutzer die Sendungen oder Filme zu empfehlen, die er sich als nächstes ansehen möchte, um ihn bei der Stange zu halten und die Abwanderungsrate zu senken.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Eine Methode zur Verfolgung von Käufen, entweder ein Kauf-Objekt oder ein angepasstes Event
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **AI Personalisiert**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie, wie Sie derzeit Kauf-Events und die entsprechende Event-Eigenschaft verfolgen.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung in der Nachrichtenübermittlung]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Beliebtester Artikel {#most-popular}

Das Empfehlungsmodell "Beliebteste Artikel" enthält Artikel, mit denen Nutzer:innen am meisten Engagement zeigen.

#### Anwendungsfälle

Basierend auf den erfassten Interaktionsdaten könnten Anwendungsfälle für dieses Modell Folgendes umfassen:

{% tabs local %}
{% tab most popular %}
Animieren Sie Nutzer:innen dazu, beliebte Artikel in Ihrem Katalog basierend auf Käufen zu erkunden. Um sicherzustellen, dass Sie nur relevante Inhalte angezeigt bekommen, empfehlen wir Ihnen, diese mit einer Auswahl zu filtern. Ein Essenslieferdienst könnte zum Beispiel Gerichte oder Restaurants in der Umgebung eines Nutzers hervorheben, die am besten bewertet wurden, basierend auf der Beliebtheit der Bestellungen auf der Plattform, und so zum Probieren und Entdecken anregen.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Ein Kaufobjekt oder ein beliebiges benutzerdefiniertes Ereignis
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Beliebteste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken. Der Essenslieferdienst könnte zum Beispiel eine Auswahl haben, um nach dem Standort des Restaurants oder der Art des Gerichts zu filtern.
5. Wählen Sie Ihre derzeitige Methode zur Nachverfolgung von Events und die entsprechende Event-Eigenschaft aus.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung in der Nachrichtenübermittlung]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab most liked %}
Ermuntern Sie die Nutzer:innen, Artikel zu entdecken, die ihnen kürzlich gefallen haben, oder Artikel, die sehr beliebt sind, basierend auf einem angepassten Event für Likes. Eine Musik-Streaming-App könnte zum Beispiel personalisierte Wiedergabelisten erstellen oder neue Alben vorschlagen, die auf den Genres oder Künstlern basieren, die ein Nutzer in der Vergangenheit mochte, und so das Engagement des Nutzers und die Verweildauer in der App erhöhen.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Angepasstes Event für Likes
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Neueste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie **Benutzerdefiniertes Ereignis** und wählen Sie Ihr benutzerdefiniertes Ereignis für Likes aus der Liste aus.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung in der Nachrichtenübermittlung]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab most viewed %}
Heben Sie Artikel hervor, die in Ihrer Nutzerbasis durch Aufrufe Aufmerksamkeit erregt haben, um zum Engagement oder zum Kauf anzuregen. Eine Immobilien-Website könnte zum Beispiel die am meisten angesehenen Angebote im Suchbereich eines Benutzers anzeigen, um Objekte hervorzuheben, die viel Aufmerksamkeit auf sich ziehen und möglicherweise auf gute Angebote oder begehrte Standorte hinweisen.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Angepasstes Event für Aufrufe
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Beliebteste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie **Benutzerdefiniertes Ereignis** und wählen Sie Ihr benutzerdefiniertes Ereignis für Ansichten aus der Liste aus.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung in der Nachrichtenübermittlung]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab popular in cart %}
Präsentieren Sie Artikel, die von vielen anderen Käufer:innen in den Warenkorb gelegt wurden, und geben Sie den Nutzer:innen einen Einblick in die aktuellen Trends in Ihrem Angebot.

Ein Modehändler könnte z. B. Kleidung und Accessoires bewerben, die gerade im Trend liegen, basierend auf den beliebten Zugängen zu den Warenkörben anderer Kund:innen. Sie können dann einen dynamischen „Jetzt Trending“-Bereich auf ihrer Startseite und in ihrer mobilen App erstellen, der in Echtzeit aktualisiert wird, um Käufer:innen zum Kauf zu animieren, bevor die Artikel ausverkauft sind.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Benutzerdefiniertes Ereignis für in den Warenkorb gelegt
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Beliebteste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie **Benutzerdefiniertes Ereignis** und wählen Sie aus der Liste Ihr benutzerdefiniertes Ereignis aus, das Sie in den Warenkorb legen möchten.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung in der Nachrichtenübermittlung]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Neuester Artikel {#most-recent}

Das Empfehlungsmodell "Neueste Artikel" enthält Artikel, mit denen Nutzer:innen sich am meisten beschäftigen. Nutzen Sie dieses Modell, um die Abwanderung von Nutzer:innen zu verringern, indem Sie sie ermutigen, sich erneut mit relevanten Content zu beschäftigen.

#### Anwendungsfälle

Basierend auf den erfassten Interaktionsdaten könnten Anwendungsfälle für dieses Modell Folgendes umfassen:

{% tabs local %}
{% tab Recently clicked %}
Ermuntern Sie Nutzer:innen dazu, Artikel, auf die sie kürzlich geklickt haben, erneut aufzurufen, basierend auf einem angepasstes Events für Klicks. Ein Online-Modehändler könnte zum Beispiel eine Empfehlung erstellen, um Folge-E-Mails oder Push-Benachrichtigungen mit Kleidungsstücken zu versenden, für die sich ein Benutzer durch Anklicken interessiert hat, und den Benutzer so zu einem erneuten Besuch des Artikels und einem Kauf zu ermutigen.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Angepasstes Event für Klicks
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Neueste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie **Benutzerdefiniertes Ereignis** und wählen Sie Ihr benutzerdefiniertes Ereignis für Klicks aus der Liste aus.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung in der Nachrichtenübermittlung]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}

{% endtab %}
{% tab Recently liked %}
Ermuntern Sie die Nutzer:innen, Artikel zu entdecken, die ihnen kürzlich gefallen haben, oder Artikel, die sehr beliebt sind, basierend auf einem angepassten Event für Likes. Eine Musik-Streaming-App könnte zum Beispiel personalisierte Wiedergabelisten erstellen oder neue Alben vorschlagen, die auf den Genres oder Künstlern basieren, die ein Nutzer in der Vergangenheit mochte, und so das Engagement des Nutzers und die Verweildauer in der App erhöhen.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Angepasstes Event für Likes
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Neueste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie **Benutzerdefiniertes Ereignis** und wählen Sie Ihr benutzerdefiniertes Ereignis für Likes aus der Liste aus.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung in der Nachrichtenübermittlung]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Recently engaged %}
Bewerben Sie Artikel, mit denen Nutzer:innen kürzlich interagiert haben, z. B. durch Aufrufe, Klicks oder Käufe. Auf diese Weise bleiben Ihre Empfehlungen frisch und auf die aktuellen Interessen des Benutzers abgestimmt.. Zum Beispiel:

- **Bildung:** Eine Online-Bildungsplattform könnte Nutzer, die sich kürzlich ein Lernvideo angesehen, sich aber noch nicht für einen Kurs angemeldet haben, dazu ermutigen, sich ähnliche Kurse oder Themen anzusehen, die sie interessieren, um den Nutzer bei der Stange zu halten und zum Lernen zu motivieren.
- **Fitness:** Eine Fitness-App kann Workouts oder Herausforderungen vorschlagen, die denen ähneln, die ein Benutzer kürzlich absolviert oder mit denen er interagiert hat. So bleibt die Trainingsroutine abwechslungsreich und fesselnd.
- **Einzelhändler für Heimwerkerbedarf:** Nachdem ein Kunde ein Elektrowerkzeug gekauft hat, kann ein Baumarkt auf der Grundlage seines letzten Kaufs entsprechendes Zubehör oder Sicherheitsausrüstungen empfehlen, um die Erfahrung und Sicherheit des Benutzers zu verbessern.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Ein Kaufobjekt oder ein beliebiges angepasstes Event für eine Interaktion
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Neueste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie **Benutzerdefiniertes Ereignis** und wählen Sie Ihr benutzerdefiniertes Ereignis für Klicks aus der Liste aus.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung in der Nachrichtenübermittlung]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Recently added %}
Erinnern Sie Benutzer an ihr Interesse an Artikeln, die sie kürzlich in ihren Warenkorb gelegt, aber noch nicht gekauft haben. Ein Online-Händler könnte zum Beispiel Erinnerungen versenden oder zeitlich begrenzte Rabatte auf die Artikel in seinem Warenkorb anbieten, um die Benutzer zu ermutigen, ihre Einkäufe abzuschließen, bevor die Angebote ablaufen.
{% details Requirements %}

- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Benutzerdefiniertes Ereignis für in den Warenkorb gelegt
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Setzen Sie den **Typ** auf **Neueste**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie **Benutzerdefiniertes Ereignis** und wählen Sie aus der Liste Ihr benutzerdefiniertes Ereignis aus, das Sie in den Warenkorb legen möchten.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung in der Nachrichtenübermittlung]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Aktueller Artikel {#trending}

Das "Trending"-Empfehlungsmodell enthält Artikel, die in den letzten Nutzer:innen-Interaktionen die größte positive Dynamik gezeigt haben. Wir berechnen dies anhand einer gewichteten Analyse von etwa 10 Wochen des Verlaufs der Ereignisse, wobei die stärkste Gewichtung auf die letzten etwa 2 Wochen angewandt wird. Um zu verhindern, dass kleine Schwankungen die Qualität der Empfehlungen beeinträchtigen, wenden wir einen Aktivitätsschwellenwert und statistische Glättungsverfahren an.

Im Gegensatz zum Modell "Beliebteste Artikel", das Artikel mit konstant hoher Interaktion enthält, enthält dieses Modell Artikel, die einen Anstieg der Interaktionen erfahren haben. Sie können es verwenden, um Produkte zu empfehlen, die im Kommen sind und derzeit eine erhöhte Zugkraft verzeichnen.

#### Anwendungsfälle

Basierend auf den erfassten Interaktionsdaten könnten Anwendungsfälle für dieses Modell Folgendes umfassen:

{% tabs local %}
{% tab Trending purchased %}
Heben Sie Artikel hervor, die Ihre Nutzer in letzter Zeit besonders häufig gekauft haben. Ein E-Commerce-Unternehmen könnte zum Beispiel saisonale Artikel empfehlen, die Nutzer:innen bei ihren Vorbereitungen für die nächste Saison auf Vorrat kaufen wollen. 

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Eine Methode zur Verfolgung von Käufen (entweder ein Kaufobjekt oder ein angepasstes Event)
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/ai_item_recommendations/).
2. Setzen Sie den **Typ** auf **Trending**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie entweder ein Kauf-Event oder ein angepasstes Event, das Käufe verfolgt, zusammen mit der entsprechenden Eigenschaft.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung in der Nachrichtenübermittlung.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)
{% enddetails %}
{% endtab %}

{% tab Trending liked %}
Heben Sie Artikel, die Ihren Nutzern in letzter Zeit gefallen haben, besonders häufig hervor. Eine Musik-App könnte zum Beispiel aufstrebende Künstler vorstellen, die in letzter Zeit einen starken Anstieg der Nutzer-Likes erfahren haben.

{% details Requirements %}
- KI-Artikelempfehlungen
- Katalog der relevanten Artikel
- Angepasstes Event zum Verfolgen von Likes
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine [KI-Artikelempfehlung]({{site.baseurl}}/ai_item_recommendations/).
2. Setzen Sie den **Typ** auf **Trending**.
3. Wählen Sie Ihren Katalog aus.
4. (Optional) Fügen Sie eine Auswahl hinzu, um Ihre Empfehlung auf relevante Artikel zu beschränken.
5. Wählen Sie Ihr angepasstes Event für die Verfolgung von Likes zusammen mit der entsprechenden Eigenschaft.
6. Trainieren Sie die Empfehlung.
7. [Verwenden Sie die Empfehlung in der Nachrichtenübermittlung.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging/)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Auf Auswahlen basierend {#selections-based}

[Selektionen]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) sind bestimmte Gruppen von Katalogdaten. Wenn Sie eine Auswahl verwenden, richten Sie im Wesentlichen nutzerdefinierte Filter ein, die auf bestimmten Spalten in Ihrem Katalog basieren. Dies könnte Filter für Marke, Größe, Ort, Hinzufügedatum und mehr beinhalten. Damit haben Sie die Kontrolle über Ihre Empfehlungen, da Sie Kriterien definieren können, die Artikel erfüllen müssen, um Nutzer:innen angezeigt zu werden.

Bei den drei vorangegangenen Typen geht es darum, ein Empfehlungsmodell in Braze einzurichten und zu trainieren. Sie können zwar auch in diesen Modellen Auswahlen verwenden, aber Sie können einige Empfehlungsanwendungen auch nur mit Katalogauswahlen und Liquid-Personalisierung erreichen.

#### Anwendungsfälle

Basierend auf den erfassten Interaktionsdaten könnten Anwendungsfälle für dieses Modell Folgendes umfassen:

{% tabs local %}
{% tab New items %}
Dieses Szenario basiert nicht direkt auf Nutzeraktionen, sondern vielmehr auf Katalogdaten. Sie können nach neuen Artikeln auf der Grundlage des Datums ihrer Aufnahme in den Katalog filtern und diese durch gezielte Kampagnen oder Canvase bewerben, ohne dass Sie ein Empfehlungsmodell trainieren müssen.

Eine E-Commerce-Plattform für Technik könnte zum Beispiel Technikbegeisterte über die neuesten Gadgets oder anstehende Vorbestellungen informieren und dabei Filter verwenden, um Artikel zu finden, die kürzlich in den Katalog aufgenommen wurden.

{% details Requirements %}
- Katalog der relevanten Artikel mit einem Feld für das Datum hinzugefügt
{% enddetails %}

{% details Setting it up %}
1. Erstellen Sie eine Auswahl auf der Grundlage Ihres Katalogs. Vergewissern Sie sich, dass Ihr Katalog ein Zeitfeld enthält (ein Feld, dessen **Datentyp** auf **Zeit** eingestellt ist), das dem Datum entspricht, an dem der Artikel hinzugefügt wurde.
2. (Optional) Fügen Sie ggf. Filter hinzu.
3. Stellen Sie sicher, dass die **zufällige Sortierung** ausgeschaltet ist.
4. Wählen Sie unter **Sortierfeld** Ihr Feld für das hinzugefügte Datum aus.
5. Setzen Sie die **Sortierreihenfolge** auf absteigend.
6. [Verwenden Sie die Auswahl in der Nachrichtenübermittlung]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Random items %}
Für ein vielfältiges Nutzererlebnis kann die Empfehlung von Zufallsartikeln für Abwechslung sorgen und möglicherweise das Interesse an weniger besuchten Katalogbereichen wecken. Diese Methode erfordert keine bestimmten Modelle oder Events, sondern verwendet eine Katalogauswahl, um sicherzustellen, dass die Artikel zufällig angezeigt werden.

Eine Online-Buchhandlung könnte zum Beispiel eine "Überraschungsfunktion" anbieten, die dem Benutzer auf der Grundlage seiner früheren Einkäufe oder seiner Surfgewohnheiten ein zufällig ausgewähltes Buch empfiehlt und ihn so dazu anregt, sich auch außerhalb seines normalen Lesegenres umzusehen.

{% details Requirements %}
- Katalog der relevanten Artikel
- Auswahl mit aktivierter **Zufälliger Sortierreihenfolge** 
{% enddetails %}

{% details Setting it up %}
1. [Erstellen Sie eine Auswahl]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#creating-a-selection) auf der Grundlage Ihres Katalogs.
2. (Optional) Fügen Sie ggf. Filter hinzu.
3. Aktivieren Sie **Zufällige Sortierung**.
4. [Verwenden Sie die Auswahl in der Nachrichtenübermittlung]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Regelbasierte {#rules-based}

Eine [regelbasierte Empfehlungsmaschine]({{site.baseurl}}/rules_based_recommendations/) verwendet Benutzerdaten und Produktinformationen, um dem Benutzer relevante Artikel in den Nachrichten vorzuschlagen. Sie verwendet Liquid und entweder Braze-Kataloge oder Connected.Content, um Content auf der Grundlage von Nutzerverhalten und Attributen dynamisch zu personalisieren.

Regelbasierte Empfehlungen basieren auf einer festen Logik, die Sie manuell einstellen müssen. Das bedeutet, dass sich Ihre Empfehlungen nicht an die individuelle Kaufhistorie und den Geschmack eines Nutzers anpassen, solange Sie die Logik nicht aktualisieren. Daher ist diese Methode am besten für Empfehlungen geeignet, die nicht häufig aktualisiert werden müssen.

#### Anwendungsfälle

Auf der Grundlage der getrackten Interaktionsdaten könnten die Anwendungsfälle für dieses Modell folgende sein:

- **Erinnerungen zur Nachbestellung:** Erinnerungen zur Nachbestellung von Artikeln mit einem vorhersehbaren Nutzungszyklus, wie z. B. monatliche Vitamine oder wöchentliche Lebensmittel, basierend auf dem letzten Kaufdatum.
- **Erstkäufer:in:** Empfehlen Sie Erstkäufer:innen Starterkits oder Einführungsangebote, um sie zu einem zweiten Kauf zu bewegen.
Loyalitätsprogramme: Heben Sie Produkte hervor, mit denen ein:e Kund:in seine oder ihre Treuepunkte oder Prämien auf der Grundlage seines oder ihres aktuellen Punktestandes maximieren kann.
- **Pädagogischer Content:** Schlagen Sie neue Kurse oder Inhalte vor, die auf den Themen der bereits konsumierten oder gekauften Materialien basieren.

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Häufig gestellte Fragen {#faq}

### Wie kommt es dazu, dass "Beliebteste" Artikel mit den Empfehlungen anderer Modelle vermischt werden?

Wenn das Empfehlungssystem eine Liste für Sie zusammenstellt, priorisiert sie zunächst die personalisierte Auswahl auf der Grundlage des von Ihnen gewählten Modells, also z. B. "Neu" oder "KI personalisiert". Wenn dieses Modell aus irgendeinem Grund nicht die komplette Liste mit 30 Empfehlungen füllen kann, werden einige Ihrer bei allen Nutzern beliebtesten Artikel hinzugefügt, um sicherzustellen, dass jeder Nutzer immer einen vollständigen Satz an Empfehlungen hat.

Dies geschieht unter einigen besonderen Bedingungen:

- Das Modell findet weniger als 30 Artikel, die Ihren Kriterien entsprechen.
- Die entsprechenden Artikel sind nicht mehr verfügbar oder auf Lager.
- Die Artikel entsprechen nicht den aktuellen Auswahlkriterien, z.B. weil sich der Bestand oder die Präferenzen des Benutzers geändert haben.

### Werden bestehende Empfehlungen nach dem Upgrade auf Item Recommendations Pro wöchentlich trainiert?

Ja, aber erst nach ihrem nächsten geplanten Update. Bestehende Empfehlungen schalten beim Upgrade auf Artikel-Empfehlungen Pro nicht sofort auf wöchentliches Training und tägliche Prognosen um. Sie werden den neuen Zeitplan jedoch automatisch bei ihrem nächsten Umschulungszyklus übernehmen. Wenn eine Empfehlung zum Beispiel zuletzt am 1\. Februar trainiert wurde und so eingestellt ist, dass sie alle 30 Tage neu trainiert wird, übernimmt sie den neuen wöchentlichen Zeitplan nach dem nächsten Update am 2\. März.