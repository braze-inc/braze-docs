---
nav_title: Anpassen von Content-Cards
article_title: Anpassen von Content-Cards
page_order: 5
description: "Dieser Artikel behandelt die Komponenten der Erstellung einer angepassten Content-Card-UI."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Anpassen von Content-Cards

> Dieser Artikel beschreibt die grundlegende Vorgehensweise bei der Implementierung angepasster Content-Cards sowie drei gängige Anwendungsfälle: Banner-Bilder, ein Posteingang und ein Bilderkarussell. Es wird davon ausgegangen, dass Sie bereits die anderen Artikel der Anleitung zur Anpassung von Content-Cards gelesen haben, um zu verstehen, was standardmäßig möglich ist und was angepassten Code erfordert. Hier erfahren Sie, wie Sie für Ihre benutzerdefinierten Content Cards [die Analysen protokollieren]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics) können. 

Braze bietet verschiedene [Content-Card-Typen]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details): `imageOnly`, `captionedImage`, `classic`, `classicImage`, und `control`. Diese können Sie als Ausgangspunkt für Ihre Implementierungen verwenden, indem Sie das Aussehen und die Bedienung anpassen. 

Sie können Content-Cards auch auf völlig angepasste Weise anzeigen, indem Sie Ihre eigene Präsentations-UI erstellen, die mit Daten aus den Braze-Modellen gefüllt ist. Analysieren Sie die Content-Card-Objekte und extrahieren Sie die Daten der Nutzdaten. Verwenden Sie dann die resultierenden Modelldaten, um Ihre angepasste UI zu füllen –  die "Run"-Phase des ["Crawl, Walk, Run"-Ansatzes]({{site.baseurl}}/developer_guide/customization_guides/customization_overview).

{% alert note %}
Jeder Standard Content-Card-Typ ist eine Unterklasse, die verschiedene Eigenschaften von der generischen Content-Card-Modellklasse erbt. Das Verständnis dieser vererbten Eigenschaften wird bei der Anpassung nützlich sein. Ausführliche Informationen finden Sie in der Dokumentation zur Kartenklasse[(Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard), [Internet](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)).
{% endalert %}


## Anpassungsübersicht

Je nach Anwendungsfall wird die genaue Implementierung Ihrer angepassten Content-Card ein wenig variieren, aber Sie sollten sich an diese Grundformel halten:

1. Erstellen Sie Ihre eigene UI
2. Hören Sie sich Daten Updates an
3. Manuelles Protokollieren von Analytics

### Schritt 1: Erstellen Sie ein angepasstes UI 

{% tabs %}
{% tab Android %}

Erstellen Sie zunächst Ihr eigenes angepasstes Fragment. Das standardmäßige [`ContentCardFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) ist nur für unsere Standard-Content-Card-Typen gedacht, ist aber ein guter Ausgangspunkt.

{% endtab %}
{% tab iOS %}

Erstellen Sie zunächst Ihre eigene angepasste View-Controller-Komponente. Das standardmäßige [`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller) ist nur für unsere Standard-Content-Card-Typen gedacht, ist aber ein guter Ausgangspunkt.

{% endtab %}
{% tab Web %}

Erstellen Sie zunächst Ihre angepasste HTML-Komponente, die zum Rendern der Karten verwendet werden soll. 

{% endtab %}
{% endtabs %}

### Schritt 2: Updates für Karten abonnieren

Registrieren Sie dann eine Callback-Funktion, um [Daten-Updates zu abonnieren]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#listening-for-card-updates), wenn die Karten aktualisiert werden. 

### Schritt 3: Analytics implementieren

Impressionen, Klicks und Abbrüche von Content-Cards werden nicht automatisch in Ihrer angepassten Ansicht protokolliert. Sie müssen [die jeweilige Methode implementieren]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#logging-events), um alle Metriken ordnungsgemäß in Braze Dashboard Analytics zu protokollieren.

## Platzierung von Content-Cards

Content-Cards können auf viele verschiedene Arten verwendet werden. Drei gängige Implementierungen sind die Verwendung als Messaging Center, als Werbebanner oder als Bildkarussell. Für jede dieser Platzierungen weisen Sie Ihren Content-Cards [Schlüssel-Wert-Paare]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) (die Eigenschaft `extras` im Datenmodell) zu und passen auf der Grundlage der Werte das Verhalten, das Aussehen oder die Funktionalität der Karte während der Laufzeit dynamisch an. 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Posteingang für Nachrichten

Content-Cards können verwendet werden, um eine Nachrichtenzentrale zu simulieren. In diesem Format ist jede Nachricht eine eigene Karte, die [Schlüssel-Wert-Paare]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) enthält, die Events beim Klicken triggern. Diese Schlüssel-Wert-Paare sind die Bezeichner, anhand derer die Anwendung entscheidet, wohin der Nutzer eine Nachricht im Posteingang klickt. Die Werte der Schlüssel-Wert-Paare sind frei wählbar. 

Hier sehen Sie ein Beispiel für eine Dashboard-Konfiguration, mit der Sie zwei Messaging-Karten erstellen können: eine Nachricht ist eine Aufforderung an einen Nutzer, seine Präferenzen hinzuzufügen, um gezielte Leseempfehlungen zu erhalten, und eine Nachricht enthält einen Gutschein-Code für ein Segment neuer Abonnenten. 

![]({% image_buster /assets/img/content_cards/content-card-message-inbox-with-kvps.png %}){: style="max-width:20%;float:right;margin-left:15px;border:0px;"}

Ein Beispiel für Schlüssel-Wert-Paare für die Leseempfehlungskarte könnte sein:

- body: Fügen Sie Ihre Interessen zu Ihrem Politer Weekly Profil hinzu, um persönliche Leseempfehlungen zu erhalten.
- style: info
- class_type: notification_center
- card_priority: (1 %)

Ein Beispiel für Schlüssel-Wert-Paare für einen neuen Abonnent:in-Gutschein könnte sein:

- title: Unbegrenztes Spiele-Abo
- body: End of Summer Special – Hol dir 10 % Rabatt auf Politer-Spiele
- buttonText: Jetzt abonnieren
- style: promo
- class_type: notification_center
- card_priority: (2 %)
- terms: new_subscribers_only

Ihre Marketer könnten diese Content-Card nur für ein Segment von neuen Nutzer:innen zur Verfügung stellen. 

Sie würden jeden der Werte bearbeiten. Schlüssel wie `body`, `title` und `buttonText` können einfache String-Werte haben, die Ihre Marketer festlegen können. Schlüssel wie `terms` können Werte haben, die eine kleine Sammlung von Phrasen enthalten, die von Ihrer Rechtsabteilung genehmigt wurden. Sie entscheiden, wie `style` und `class_type` auf Ihrer App oder Website dargestellt werden sollen. 

{% details Weitere Erklärung für Android %}

Im Android und FireOS SDK wird die Logik der Nachrichtenzentrale durch den Wert `class_type` gesteuert, der durch die Schlüssel-Wert-Paare von Braze bereitgestellt wird. Mit der Methode [`createContentCardable`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/implementation_guide) können Sie diese Klassentypen filtern und identifizieren.

{% tabs %}
{% tab Kotlin %}
**Verwendung von `class_type` für das Verhalten beim Klicken**<br>
Wenn wir die Content-Card-Daten in unsere angepassten Klassen aufblasen, verwenden wir die Eigenschaft `ContentCardClass` der Daten, um zu bestimmen, welche konkrete Unterklasse zum Speichern der Daten verwendet werden soll.

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass?): ContentCardable?{
        return when(type){
            ContentCardClass.AD -> Ad(metadata)
            ContentCardClass.MESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass.NOTIFICATION_CENTER -> FullPageMessage(metadata)
            ContentCardClass.ITEM_GROUP -> Group(metadata)
            ContentCardClass.ITEM_TILE -> Tile(metadata)
            ContentCardClass.COUPON -> Coupon(metadata)
            else -> null
        }
    }
```

Bei der Bearbeitung der Benutzerinteraktion mit der Nachrichtenliste können wir dann anhand des Typs der Nachricht bestimmen, welche Ansicht dem Nutzer:innen angezeigt werden soll.

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //...
        listView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
           when (val card = dataProvider[position]){
                is WebViewMessage -> {
                    val intent = Intent(this, WebViewActivity::class.java)
                    val bundle = Bundle()
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.contentString)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
                is FullPageMessage -> {
                    val intent = Intent(this, FullPageContentCard::class.java)
                    val bundle = Bundle()
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.icon)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.messageTitle)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.cardDescription)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        }
    }
```
{% endtab %}
{% tab Java %}
**Verwendung von `class_type` für das Verhalten beim Klicken**<br>
Wenn wir die Content-Card-Daten in unsere angepassten Klassen aufblasen, verwenden wir die Eigenschaft `ContentCardClass` der Daten, um zu bestimmen, welche konkrete Unterklasse zum Speichern der Daten verwendet werden soll.

```java
private ContentCardable createContentCardable(Map<String, ?> metadata,  ContentCardClass type){
    switch(type){
        case ContentCardClass.AD:{
            return new Ad(metadata);
        }
        case ContentCardClass.MESSAGE_WEB_VIEW:{
            return new WebViewMessage(metadata);
        }
        case ContentCardClass.NOTIFICATION_CENTER:{
            return new FullPageMessage(metadata);
        }
        case ContentCardClass.ITEM_GROUP:{
            return new Group(metadata);
        }
        case ContentCardClass.ITEM_TILE:{
            return new Tile(metadata);
        }
        case ContentCardClass.COUPON:{
            return new Coupon(metadata);
        }
        default:{
            return null;
        }
    }
}

```

Bei der Bearbeitung der Benutzerinteraktion mit der Nachrichtenliste können wir dann anhand des Typs der Nachricht bestimmen, welche Ansicht dem Nutzer:innen angezeigt werden soll.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        //...
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
               ContentCardable card = dataProvider.get(position);
               if (card instanceof WebViewMessage){
                    Bundle intent = new Intent(this, WebViewActivity.class);
                    Bundle bundle = new Bundle();
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.getContentString());
                    intent.putExtras(bundle);
                    startActivity(intent);
                }
                else if (card instanceof FullPageMessage){
                    Intent intent = new Intent(this, FullPageContentCard.class);
                    Bundle bundle = Bundle();
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.getIcon());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.getMessageTitle());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.getCardDescription());
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        });
    }
```

{% endtab %}
{% endtabs %}
{% enddetails %}

### Karussell

Content-Cards können in einem Karussell-Feed eingestellt werden, in dem ein Nutzer:innen horizontal wischen kann, um zusätzliche Feature-Cards zu sehen. 

Um ein Content-Card-Karussell zu erstellen, implementieren Sie eine Logik, die die [Änderungen in Ihren Content-Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed) überwacht und die Ankunft von Content-Cards behandelt. Standardmäßig werden Content-Cards nach dem Erstellungsdatum (neuestes zuerst) sortiert. Einem Benutzer werden alle Karten angezeigt, für deren Anzeige der berechtigt ist. Implementieren Sie clientseitige Logik, um eine bestimmte Anzahl von Karten gleichzeitig im Karussell anzuzeigen.

Auf diese Weise können Sie zusätzliche Anzeigelogik auf verschiedene Weise bestellen und anwenden. Sie könnten zum Beispiel die ersten fünf Content-Card-Objekte aus dem Array auswählen oder Schlüssel-Wert-Paare einführen, um die bedingte Logik aufzubauen.

Wenn Sie ein Karussell als sekundären Content-Cards-Feed implementieren, lesen Sie bitte den Abschnitt [Anpassen des Standard Content-Card-Feeds]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds), um zu erfahren, wie Sie die Karten anhand von Schlüssel-Wert-Paaren in den richtigen Feed sortieren.

### Banner

Content-Cards müssen nicht wie "Karten" aussehen. Content-Cards können zum Beispiel als dynamisches Banner erscheinen, das persistent auf Ihrer Homepage oder am Anfang bestimmter Seiten angezeigt wird.

Um dies zu erreichen, erstellen Ihre Marketer eine Kampagne oder einen Canvas-Schritt mit einer Content-Card vom Typ **Nur Bild**. Legen Sie dann Schlüssel-Wert-Paare fest, die für die Verwendung von [Content-Cards als ergänzende Inhalte]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content) geeignet sind.


