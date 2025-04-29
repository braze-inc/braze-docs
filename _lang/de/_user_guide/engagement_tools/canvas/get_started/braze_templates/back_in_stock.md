---
nav_title: Wieder auf Lager
article_title: Wieder auf Lager
page_order: 2
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie eine Braze Canvas-Vorlage verwenden können, um Käufe zu fördern, indem Sie Ihre Benutzer mit einer personalisierten Nachricht benachrichtigen, wenn ein Artikel wieder auf Lager ist."
tool: Canvas
---

# Wieder verfügbar

> Verwenden Sie die Vorlage "Wieder vorrätig", um Nachrichten zu erstellen, die sich an Benutzer richten, die zuvor einen Artikel angesehen oder Interesse an einem Artikel bekundet haben, der nicht vorrätig war, aber jetzt wieder erhältlich ist. Dies hilft den Nutzer:innen, die gewünschten Produkte zu erhalten, indem sie sich in dem kritischen Moment engagieren, wenn ein Produkt wieder verfügbar ist.

Dieser Artikel führt Sie durch einen Anwendungsfall für das Template **Zurück auf Lager**, das für den Schritt der Konversion im Lebenszyklus der Nutzer:innen gedacht ist. Wenn Sie fertig sind, haben Sie ein Canvas erstellt, das eine Push-Mitteilung (Web oder Handy), eine SMS oder eine E-Mail an Benutzer sendet, wenn ein Artikel wieder vorrätig ist, sowie bis zu zwei Erinnerungen.

## Voraussetzungen

Um dieses Template erfolgreich zu verwenden, benötigen Sie Folgendes:

- Ein [Katalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog) mit Informationen über Ihren Artikel
- [Back-in-Stock-Benachrichtigungen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/#how-back-in-stock-notifications-work) müssen für den Artikel eingerichtet werden, über den Sie Nutzer:innen Nachrichten schicken möchten.

## Anpassen des Templates an Ihre Bedürfnisse

Nehmen wir an, wir arbeiten für PantsLabyrinth, einen Direktvertrieb für Bekleidung, der sich auf Hosen, Jeans, Culottes und viele andere Arten von Hosen spezialisiert hat. Wir können das Template „Wieder verfügbar“ verwenden, um Kund:innen auf verschiedenen Kanälen zu benachrichtigen, wenn eine beliebte Jeans, die Classic Straight Leg, wieder auf Lager ist.

Bevor wir das Canvas erstellt haben, haben wir [einen Katalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog) mit Informationen über unseren Bestand an Straight Leg-Hosen [erstellt]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog) und [Benachrichtigungen über die Verfügbarkeit der]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/#setting-up-back-in-stock-notifications) Classic Straight Leg-Jeans [eingerichtet]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/#setting-up-back-in-stock-notifications). Wir haben es so eingerichtet, dass Benutzer Benachrichtigungen abonnieren, nachdem sie das benutzerdefinierte Ereignis des Favorisierens der Classic Straight Leg Jeans in der App ausgeführt haben.

Um auf die vorrätige Vorlage zuzugreifen, wählen Sie bei der Erstellung eines neuen Canvas die Option **Eine Canvas-Vorlage verwenden** > **Lötvorlagen**. Wählen Sie dann neben **Wieder auf Lager** die Option **Vorlage anwenden**. Jetzt können wir das Template durchgehen, um es an unsere Bedürfnisse anzupassen.

### Schritt 1: Details einrichten

Passen wir die Canvas-Details an, um unser Ziel zu erreichen.

1. Wählen Sie **Bearbeiten** neben dem Namen der Vorlage.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2\. Aktualisieren Sie den Namen des Canvas, um anzugeben, dass das Canvas dafür gedacht ist, Nutzer anzusprechen, wenn unser Produkt Classic Straight Leg wieder auf Lager ist.
3\. Aktualisieren Sie die Beschreibung, um zu erklären, dass dieses Canvas personalisiertes Messaging enthält.
4\. Fügen Sie das Tag **Back in Stock** hinzu, das unter dem Tag **Promotional** verschachtelt ist, damit wir auf der Startseite von Canvas danach filtern können. 

![Schritt "Canvas-Details einrichten" mit dem Canvas-Namen "Wieder auf Lager - Klassisches gerades Bein" und einer kurzen Canvas-Beschreibung.][1]

### Schritt 2: Konversions-Events zuweisen

Ändern Sie das **primäre Umrechnungsereignis - A** in **Einen bestimmten Kauf tätigen** und wählen Sie **Klassisches gerades Bein** als Produktnamen.

![„Konversions-Events zuweisen“ für den Konversions-Event-Typ des Kaufs des Produkts Classic Straight Leg mit einer Konversionsfrist von 7 Tagen.][2]

### Schritt 3: Entry-Zeitplan anpassen

Behalten wir den Zeitplan für den Eingang als **aktionsbasiert** bei, so dass Nutzer:innen unser Canvas betreten, wenn sie eine Aktion ausführen, die in der Vorlage bereits auf **Back in Stock Event ausführen** eingestellt ist.

In diesem Schritt nehmen wir zwei Anpassungen vor:

1. Wählen Sie den Katalog aus, der Informationen über unsere Classic Straight Leg Jeans enthält, die wir „Straight Leg Pants“ genannt haben. 

![„Entry-Zeitplan“ für ein aktionsbasiertes Canvas.][3]

{: start="2"}
2\. Setzen Sie die **Startzeit (erforderlich)** auf das gewünschte Startdatum und die Uhrzeit.

![Abschnitt „Entry-Fenster“ mit einer Startzeit von 2\. Januar 2025 um 12 Uhr.][4]

### Schritt 4: Zielgruppe auswählen

Wir definieren unsere Zielgruppe als Nutzer, von denen wir annehmen, dass sie mit größerer Wahrscheinlichkeit die Classic Straight Leg Jeans kaufen würden.

1. Wählen Sie unser Targeting-Segment „Zu Favoriten hinzugefügt – Classic Straight Leg Jeans“ aus, das aus Nutzer:innen besteht, die unsere Classic Straight Leg Jeans auf unserer App oder Website als Favoriten hinzugefügt haben.
2. Wählen Sie einen Filter, um Benutzer einzuschließen, die "Jeans" mehr als "0" Mal gekauft haben.

![Schritt „Zielgruppe“ mit dem Segment „Zu Favoriten hinzugefügt – Classic Straight Leg Jeans“.][5]

{: start="3"}
3\. Passen Sie die Eingangskontrollen so an, dass Nutzer:innen nach der maximalen Dauer des Canvas wieder in den Canvas eintreten können, um zu verhindern, dass sie denselben Schritt gleichzeitig triggern.

!["Eingangskontrollen" mit einem Kontrollkästchen, das es Nutzern:innen erlaubt, diesen Canvas mit einer maximalen Dauer des Canvas erneut zu betreten.][6]

{: start="4"}
4\. Passen Sie die Ausstiegskriterien an, um Nutzer:innen zu entfernen, die das angepasste Event der Ablehnung der Classic Straight Leg Jeans durchgeführt haben.

![Abschnitt „Exit-Kriterien“ mit einer Ausnahme für Nutzer:innen, die das angepasste Event „Aus der Favoritenliste entfernt“ ausführen.][7]

### Schritt 5: Wählen Sie Ihre Sendeeinstellungen aus

Wir behalten die Standardeinstellungen für Abonnements bei, d.h. wir senden nur an Benutzer, die Nachrichten oder Benachrichtigungen abonniert oder sich dafür entschieden haben, und überspringen die anderen Einstellungen (Häufigkeitsbegrenzung, ruhige Stunden und Seed-Gruppen).

![Der Schritt „Sendeeinstellungen“ stellt das Targeting von Nutzern:in zusammen, die Abonnent:in sind oder sich angemeldet haben.][8]

### Schritt 6: Canvas anpassen

Jetzt bauen wir unser Canvas auf, indem wir die Kanäle und Inhalte anpassen, die an die Nutzer:innen gesendet werden sollen. Da wir alle vier Vorlagenkanäle (Mobile- und Web-Push, SMS und E-Mail) verwenden und den [intelligenten Kanalfilter]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) einsetzen, müssen wir keine weiteren Kanäle hinzufügen oder entfernen.

{% alert tip %}
Sie können die [Canvas-Eingabeeigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) verwenden, um die Nachrichten in Ihrem Canvas je nach dem Produkt, auf das Sie sich beziehen, anzupassen.
{% endalert %}

Wir beginnen unsere Anpassung, indem wir jeden Schritt der Nachrichten durchgehen, um den Content zu aktualisieren.

1. Ersetzen Sie `!!YOURCATALOGHERE!!` durch unseren Katalognamen ("Straight_Leg_Pants").
2. Ersetzen Sie `[0]` durch die Indexnummer der Classic Straight Leg Jeans, die „9“ lautet, da die Jeans der zehnte Artikel im `items`-Array unseres Katalogs ist. (Arrays sind in Liquid nullindiziert, daher ist der erste Artikel `0` und nicht `1`.)
3. Wiederholen Sie die Schritte 1 und 2 für alle verbleibenden Nachrichtenschritte, einschließlich:
    - Die Nachricht „In-Product-Nachricht und E-Mail“, die nach dem eintägigen Delay gesendet wird
    - Die "Push+Email Alert"-Nachrichten, die an Benutzer gesendet werden, die keinen Kauf getätigt haben
4. Aktualisieren Sie den Schritt Aktionspfade, indem Sie die Aktionsgruppe **Einkauf** auswählen. Wählen Sie dann **Gezielt einkaufen** und wählen Sie Classic Straight Leg Jeans als Produkt.

![Mobile Push Canvas Schritt mit einer Nachricht, die den Benutzer darüber informiert, dass ein Produkt wieder auf Lager ist.][9]

### Schritt 7: Testen und starten Sie Ihr Canvas

Nachdem wir unser Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, starten wir es, indem wir **Canvas starten** wählen. Jetzt erhalten unsere Nutzer:innen, die unsere Classic Straight Leg Jeans favorisiert und unsere Messaging-Kanäle abonniert haben, Benachrichtigungen, wenn sie wieder vorrätig sind!

{% alert tip %}
In unserer [Checkliste für die Zeit vor und nach dem Start eines]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) Canvas finden Sie die Dinge, die Sie beachten sollten, bevor und nachdem Sie ein Canvas starten.
{% endalert %}

[1]: {% image_buster /assets/img/canvas_templates/back_in_stock_1.png %}
[2]: {% image_buster /assets/img/canvas_templates/back_in_stock_2.png %}
[3]: {% image_buster /assets/img/canvas_templates/back_in_stock_3.png %}
[4]: {% image_buster /assets/img/canvas_templates/back_in_stock_4.png %}
[5]: {% image_buster /assets/img/canvas_templates/back_in_stock_5.png %}
[6]: {% image_buster /assets/img/canvas_templates/back_in_stock_6.png %}
[7]: {% image_buster /assets/img/canvas_templates/back_in_stock_7.png %}
[8]: {% image_buster /assets/img/canvas_templates/back_in_stock_8.png %}
[9]: {% image_buster /assets/img/canvas_templates/back_in_stock_9.png %}