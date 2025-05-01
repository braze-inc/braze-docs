---
nav_title: Angepasste Content-Cards
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

# Angepasste Content-Cards

> Dieser Artikel beschreibt die grundlegende Vorgehensweise bei der Implementierung angepasster Content-Cards sowie drei gängige Anwendungsfälle: Banner-Bilder, ein Posteingang und ein Bilderkarussell. Es wird davon ausgegangen, dass Sie bereits die anderen Artikel der Anleitung zur Anpassung von Content-Cards gelesen haben, um zu verstehen, was standardmäßig möglich ist und was angepassten Code erfordert. Hier erfahren Sie, wie Sie für Ihre benutzerdefinierten Content Cards [die Analysen protokollieren]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) können. 

## Über Content-Cards

Braze bietet verschiedene [Content-Card-Typen]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details): `imageOnly`, `captionedImage`, `classic`, `classicImage`, und `control`. Diese können Sie als Ausgangspunkt für Ihre Implementierungen verwenden, indem Sie das Aussehen und die Bedienung anpassen. 

Sie können Content-Cards auch auf völlig angepasste Weise anzeigen, indem Sie Ihre eigene Präsentations-UI erstellen, die mit Daten aus den Braze-Modellen gefüllt ist. Analysieren Sie die Content-Card-Objekte und extrahieren Sie die Daten der Nutzdaten. Verwenden Sie dann die resultierenden Modelldaten, um Ihre angepasste UI zu füllen –  die "Run"-Phase des ["Crawl, Walk, Run"-Ansatzes]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

{% alert note %}
Jeder Standard Content-Card-Typ ist eine Unterklasse, die verschiedene Eigenschaften von der generischen Content-Card-Modellklasse erbt. Das Verständnis dieser vererbten Eigenschaften wird bei der Anpassung nützlich sein. Ausführliche Informationen finden Sie in der Dokumentation zur Kartenklasse[(Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard), [Internet](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)).
{% endalert %}

## Erstellen einer angepassten Karte

### Schritt 1: Erstellen Sie ein angepasstes UI 

{% tabs local %}
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

#### Beispiel

Sie möchten zum Beispiel zwei Messaging-Karten erstellen: einen Call-to-Action für Nutzer:innen, die Leseempfehlungen lesen können, und einen Gutschein-Code für Ihr neues Segment der Abonnent:innen.

Schlüssel wie `body`, `title` und `buttonText` können einfache String-Werte haben, die Ihre Marketer festlegen können. Schlüssel wie `terms` können Werte haben, die eine kleine Sammlung von Phrasen enthalten, die von Ihrer Rechtsabteilung genehmigt wurden. Schlüssel wie `style` und `class_type` haben String-Werte, die Sie einstellen können, um zu bestimmen, wie Ihre Karte in Ihrer App oder auf Ihrer Website dargestellt wird."

{% tabs local %}
{% tab Empfehlungen zum Lesen %}
Schlüssel-Wert-Paare für die Leseempfehlungskarte:

| Schlüssel         | Wert                                                                |
|------------|----------------------------------------------------------------------|
| `body`       | Fügen Sie Ihre Interessen zu Ihrem Politer Weekly Profil hinzu, um persönliche Leseempfehlungen zu erhalten. |
| `style`      | Infos                                                                 |
| `class_type` | benachrichtigung_zentrale                                                 |
| `card_priority` | (1 %)                                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab Coupon für neue Abonnent:innen %}
Schlüssel-Wert-Paare für einen neuen Abonnent:in-Gutschein:

| Schlüssel         | Wert                                                            |
|------------|------------------------------------------------------------------|
| `title`      | Unbegrenztes Spiele-Abo                                    |
| `body`       | End of Summer Special – Hol dir 10 % Rabatt auf Politer-Spiele              |
| `buttonText` | Jetzt abonnieren                                                    |
| `style`      | Promo                                                            |
| `class_type` | benachrichtigung_zentrale                                              |
| `card_priority` | (2 %)                                                              |
| `terms`      | neue_Abonnenten_ausschließlich                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

{% details Zusätzliche Informationen für Android %}

Im Android und FireOS SDK wird die Logik der Nachrichtenzentrale durch den Wert `class_type` gesteuert, der durch die Schlüssel-Wert-Paare von Braze bereitgestellt wird. Mit der Methode [`createContentCardable`]({{site.baseurl}}/developer_guide/platforms/android/content_cards/examples/) können Sie diese Klassentypen filtern und identifizieren.

{% tabs local %}
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

Sie können Content-Cards in Ihrem vollständig angepassten Karussell-Feed einrichten, die es Nutzern:innen erlauben, zusätzliche Feature-Cards zu durchstreichen und anzusehen. Standardmäßig werden Content-Cards nach Erstellungsdatum sortiert (das neueste zuerst), und Ihre Nutzer:innen sehen alle Karten, für die sie in Frage kommen.

So implementieren Sie ein Content-Card-Karussell:

1. Erstellen Sie eine angepasste Logik, die auf [Änderungen in Ihren Content-Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed) achtet und die Ankunft der Content-Cards behandelt.
2. Erstellen Sie eine angepasste Client-seitige Logik, um eine bestimmte Anzahl von Karten gleichzeitig im Karussell anzuzeigen. Sie könnten zum Beispiel die ersten fünf Content-Card-Objekte aus dem Array auswählen oder Schlüssel-Wert-Paare einführen, um die bedingte Logik aufzubauen.

{% alert tip %}
Wenn Sie ein Karussell als sekundären Content-Cards-Feed implementieren, stellen Sie sicher, dass Sie [die Karten mithilfe von Schlüssel-Wert-Paaren in den richtigen Feed einsortieren]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).
{% endalert %}

### Banner

Content-Cards müssen nicht wie "Karten" aussehen. Content-Cards können zum Beispiel als dynamisches Banner erscheinen, das persistent auf Ihrer Homepage oder am Anfang bestimmter Seiten angezeigt wird.

Um dies zu erreichen, erstellen Ihre Marketer eine Kampagne oder einen Canvas-Schritt mit einer Content-Card vom Typ **Nur Bild**. Legen Sie dann Schlüssel-Wert-Paare fest, die für die Verwendung von [Content-Cards als ergänzende Inhalte]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content) geeignet sind.
