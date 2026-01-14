---
nav_title: Auswahlen
article_title: Auswahlen
page_order: 5
description: "In diesem Referenzartikel erfahren Sie, wie Sie Auswahlen mit Ihren Katalogen erstellen und verwenden, um Daten in Ihren Kampagnen von Braze zu referenzieren."
---

# Auswahlen

> Auswahlen sind Gruppen von Daten, die dazu verwendet werden können, eine Nachricht für jeden Nutzer in Ihrer Kampagne zu personalisieren. Wenn Sie eine Auswahl verwenden, richten Sie im Wesentlichen benutzerdefinierte Filter ein, die auf bestimmten Spalten in Ihrem Katalog basieren. Dies könnte Filter für Marke, Größe, Ort, Hinzufügedatum und mehr beinhalten. Damit haben Sie die Kontrolle darüber, was Sie den Nutzer:innen zeigen, indem Sie Kriterien festlegen, die die Artikel zuerst erfüllen müssen.<br><br>Auf dieser Seite erfahren Sie, wie Sie Auswahlen für Ihre Kataloge erstellen und verwenden.

Nachdem Sie einen [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs/) erstellt haben, können Sie Ihre Katalogdaten weiter referenzieren, indem Sie Auswahlen in Ihre Kampagnen oder Empfehlungen von Braze einbauen.

![Der Abschnitt Selektionen in einem Beispielkatalog.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## Was Sie wissen sollten

- Sie können bis zu 30 Auswahlen pro Katalog erstellen.
- Sie können bis zu 10 Filter pro Auswahl hinzufügen.
- Die Selektionen eignen sich hervorragend zur Verfeinerung von Empfehlungen aus den Daten des Braze Katalogs. Wenn Sie nach Inspirationen suchen, sehen Sie sich die Anwendungsbeispiele unter [About item recommendations]({{site.baseurl}}/user_guide/brazeai/recommendations/) an.

## Eine Auswahl erstellen

Um eine Auswahl zu erstellen, gehen Sie wie folgt vor.

1. Gehen Sie zu **Kataloge** und wählen Sie Ihren Katalog aus der Liste aus.
2. Wählen Sie die Registerkarte **Auswahl** und klicken Sie auf **Auswahl erstellen**.
3. Geben Sie Ihrer Auswahl einen Namen und optional eine Beschreibung.
4. Wählen Sie unter **Filterfeld** die Katalogspalte, nach der Sie filtern möchten. String-Felder mit mehr als 1.000 Zeichen können nicht für Filter ausgewählt werden.
5. Schließen Sie die Definition Ihrer Filterkriterien ab, indem Sie den entsprechenden Operator (z. B. "ist gleich" oder "ist nicht gleich") und das Attribut auswählen.
6. Im Bereich **Sortierart** legen Sie fest, wie die Ergebnisse sortiert werden. Standardmäßig werden die Ergebnisse in keiner bestimmten Reihenfolge zurückgegeben. Um die Sortierung nach einem bestimmten Feld festzulegen, deaktivieren Sie **Zufällige Sortierung** und geben Sie das **Sortierfeld** und die **Sortierreihenfolge** (aufsteigend oder absteigend) an.
7. Geben Sie Im Abschnitt **Max. Anzahl an Ergebnissen** die Ergebnisse ein (bis zu 50).
8. Wählen Sie **Auswahl erstellen**.

### Test und Vorschau

Nachdem Sie eine Auswahl erstellt haben, können Sie im Bereich **Vorschau für Nutzer:innen** sehen, was die Auswahl für einen zufälligen Nutzer oder einen bestimmten Nutzer:innen ergeben würde. Bei Auswahlen, die Personalisierung verwenden, können Sie die Vorschau erst nach dem Auswählen einer Nutzerin oder eines Nutzers sehen.

### Liquid in den Auswahlergebnissen

Die Verwendung von Liquid in Katalogen, wie z.B. benutzerdefinierte Attribute und benutzerdefinierte Ereignisse, kann dazu führen, dass Sie für jeden Benutzer in Ihrer Auswahl unterschiedliche Ergebnisse erhalten. 

{% alert note %}
Connected Content Liquid wird in diesen Filter-Einstellungen nicht unterstützt.
{% endalert %}

![Filtereinstellungen für die Katalogauswahl, bei denen das Attribut auf ein angepasstes Liquid Attribut gesetzt ist.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## Auswählen von Nachrichten im Messaging

Nachdem Sie Ihre Auswahl getroffen haben, personalisieren Sie Ihre Nachrichten mit Liquid, um die gefilterten Artikel aus diesem Katalog einzufügen. Sie können das Liquid von Braze über das Personalisierungsfenster in den Nachrichtenverfassern generieren lassen:

1. Wählen Sie in jedem Nachrichtenkomponisten, der Personalisierung unterstützt, die Option <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Personalisierung hinzufügen"></i> um das Fenster für die Personalisierung zu öffnen.
2. Wählen Sie für **Personalisierungstyp** die Option **Katalogartikel**.
3. Wählen Sie Ihren Katalognamen.
4. Wählen Sie für **Objektauswahlmethode** die Option **Eine Auswahl verwenden**.
4. Wählen Sie Ihre Auswahl aus der Liste.
5. Wählen Sie unter **Anzuzeigende Informationen**, welche Felder aus dem Katalog für jeden Artikel angezeigt werden sollen.
6. Wählen Sie das Symbol **Kopieren** und fügen Sie die Flüssigkeit an der Stelle ein, an der sie in Ihrer Nachricht erscheinen soll.

![Das Modal "Personalisierung hinzufügen" mit den folgenden Auswahlmöglichkeiten: "Katalogartikel" für "Personalisierungstyp", "Spiele" für "Katalogname", "Auswahlen" für "Auswahltyp", "game_selection" für "Auswahl" und "Titel" und "description_en" für "Anzuzeigende Informationen".]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

## Anwendungsfall

Nehmen wir an, Sie besitzen einen Essenslieferdienst und möchten Ihren Nutzern, die bestimmte Essensvorlieben haben, eine personalisierte Nachricht auf der Grundlage ihrer zuletzt angesehenen Lebensmittelkategorie senden. 

Mithilfe eines Katalogs mit den Informationen Ihres Essenslieferdienstes zu Name, Preis, Bild und Kategorie der Mahlzeit können Sie eine Auswahl erstellen, um drei Mahlzeiten auf der Grundlage der zuletzt angesehenen Kategorie eines Benutzers zu empfehlen.

![Ein Beispiel für die Auswahl eines Dienstes für die Zustellung von Mahlzeiten mit zwei Filtern: einer, der einen Produkttyp als Mahlzeit auswählt, und einer, der die Kategorie als die zuletzt angesehene identifiziert. Die Auswahl ist so eingestellt, dass die Reihenfolge, in der die drei Ergebnisse zurückgegeben werden, zufällig ist.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

Um diesen Katalog und die Auswahl in einer Kampagne zu verwenden, verwenden Sie das Modal **Personalisierung hinzufügen** im Abschnitt Nachrichtenzusammenstellung beim Erstellen einer Kampagne. In diesem Beispiel haben wir den Katalog mit den Informationen Ihres Essenslieferdienstes und die Auswahl für Essensempfehlungen basierend auf der zuletzt angesehenen Kategorie ausgewählt. So können wir den Namen und den Preis der Mahlzeit anzeigen. Um Ihre Nachricht weiter auszubauen, können Sie die Auswahl nutzen, um auch ein Bild der ersten empfohlenen Mahlzeit hinzuzufügen.

![Eine Content-Card mit der Überschrift "Sie werden diese hoch bewerteten Mahlzeiten LIEBEN!" mit der Auswahl "recommendations_be_recent_category" im Bereich Nachrichtengestaltung.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

Nehmen wir an, Sie haben eine:n Nutzer:in, deren:dessen zuletzt angesehene Kategorie "Huhn" ist. Mit der eingestellten Personalisierung und einer Content Card-Kampagne können Sie diesem Nutzer drei Essensempfehlungen mit Huhn schicken.

![Eine Content-Card mit einem Bild von gegrilltem Zitronenhähnchen und einer Liste von drei Essensempfehlungen, die Hähnchen enthalten, basierend auf der zuletzt angesehenen Kategorie des Nutzers:innen.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

Mit der gleichen Personalisierung können Sie auch drei Essensempfehlungen an einen Nutzer senden, dessen zuletzt angesehene Kategorie "Rindfleisch" ist.

![Eine Content-Card mit einem Bild von Beef Stroganoff und einer Liste von zwei Essensempfehlungen, die Rindfleisch enthalten, basierend auf der zuletzt angesehenen Kategorie des Nutzers:innen.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}


