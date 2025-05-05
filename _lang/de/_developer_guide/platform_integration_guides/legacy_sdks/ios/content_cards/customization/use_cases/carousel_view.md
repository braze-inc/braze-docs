---
nav_title: Karussell-Ansicht
article_title: Inhaltskarten-Karussell-Ansicht für iOS
platform: iOS
page_order: 5
description: "Dieser Artikel beschreibt, wie Sie eine Content-Card-Karussell-Ansicht für iOS-Anwendungen implementieren."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Anwendungsfall: Karussell-Ansicht

![Beispiel einer Nachrichten-App, die ein Karussell von Inhaltskarten in einem Artikel zeigt.]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

In diesem Abschnitt erfahren Sie, wie Sie einen Karussell-Feed mit mehreren Karten implementieren, bei dem ein Benutzer horizontal wischen kann, um weitere vorgestellte Karten anzuzeigen. Für die Integration einer Karussell-Ansicht müssen Sie eine vollständig angepasste Content-Card-Implementierung verwenden – die Run-Phase des [Crawl-Walk-Run-Ansatzes]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches).

Bei diesem Ansatz verwenden Sie nicht die Braze-Ansichten und die Standardlogik, sondern zeigen die Content Cards auf eine völlig benutzerdefinierte Weise an, indem Sie Ihre eigenen Ansichten verwenden, die mit Daten aus den Braze-Modellen gefüllt sind.

Die wichtigsten Unterschiede im Hinblick auf den Entwicklungsaufwand einer Basis-Implementierung und einer Karussell-Implementierung sind Folgende:

- Erstellen Sie Ihre eigenen Ansichten
- Protokollierung der Inhaltskarten-Analysen
- Einführung einer zusätzlichen clientseitigen Logik, um zu bestimmen, wie viele und welche Karten im Karussell angezeigt werden sollen

## Implementierung

### Schritt 1: Erstellen Sie einen benutzerdefinierten View Controller

Um das Content-Cards Karussell zu erstellen, erstellen Sie einen angepassten View Controller (z. B. `UICollectionViewController`) und [abonnieren Sie Datenaktualisierungen]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/#getting-the-data). Beachten Sie, dass Sie den standardmäßigen `ABKContentCardTableViewController` nicht erweitern oder in Unterklassen verwenden können, da er nur unsere standardmäßigen Content-Card-Typen verarbeiten kann.

### Schritt 2: Analytics implementieren

Wenn Sie einen vollständig angepassten View Controller erstellen, werden Impressionen, Klicks und Ausblendungen von Content-Cards nicht automatisch protokolliert. Sie müssen die entsprechenden Analytics-Methoden implementieren, um sicherzustellen, dass Impressionen, Ausblende-Events und Klicks ordnungsgemäß in den Analytics des Braze Dashboards aufgezeichnet werden.

Informationen zu den Analysemethoden finden Sie unter [Kartenmethoden]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/#card-methods). 

{% alert note %}
Auf der gleichen Seite finden Sie auch die verschiedenen Eigenschaften, die von unserer generischen Modellklasse Content Card geerbt wurden und die Sie bei der Implementierung Ihrer Ansicht nützlich finden könnten.
{% endalert %}

### Schritt 3: Beobachter für Content-Cards erstellen

Erstellen Sie einen [Beobachter für Inhaltskarten]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/#step-2-set-up-a-content-card-listener), der für das Eintreffen von Inhaltskarten verantwortlich ist, und implementieren Sie eine bedingte Logik, um eine bestimmte Anzahl von Karten gleichzeitig im Karussell anzuzeigen. Standardmäßig werden Content-Cards nach dem Erstellungsdatum (neuestes zuerst) sortiert. Einem Nutzer werden alle Karten angezeigt, für deren Anzeige der berechtigt ist.

Allerdings können Sie zusätzliche Anzeigelogik auf verschiedene Weise bestellen und anwenden. Sie könnten zum Beispiel die ersten fünf Inhaltskartenobjekte aus dem Array auswählen oder Schlüssel-Wert-Paare einführen (die Eigenschaft `extras` im Datenmodell), um die Sie eine bedingte Logik aufbauen können.

Wenn Sie ein Karussell als sekundären Content-Cards-Feed implementieren, lesen Sie den Abschnitt [Mehrere Content-Card-Feeds verwenden]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/), um sicherzustellen, dass Sie die Karten anhand von Schlüssel-Wert-Paaren in den richtigen Feed sortieren.

{% alert important %}
Es ist wichtig, dass sich Ihre Marketing- und Entwicklerteams darüber abstimmen, welche Schlüssel-Wert-Paare verwendet werden sollen (z.B. `feed_type = brand_homepage`), denn alle Schlüssel-Wert-Paare, die Marketer in das Braze-Dashboard eingeben, müssen exakt mit den Schlüssel-Wert-Paaren übereinstimmen, die die Entwickler in die App-Logik einbauen.
{% endalert %}

Die iOS-spezifische Entwicklerdokumentation zu der Klasse, den Methoden und Attributen von Content-Cards finden Sie in der [`ABKContentCard` Class Reference](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html) für iOS.

## Überlegungen

- Wenn Sie vollständig angepasste Ansichten verwenden, können Sie die in `ABKContentCardsController` verwendeten Methoden nicht erweitern oder in Unterklassen verwenden. Stattdessen müssen Sie die Methoden und Eigenschaften des Datenmodells selbst integrieren.
- Die Logik und die Implementierung der Karussellansicht ist kein Standard-Content-Card-Typ in Braze. Daher muss die Logik zur Erreichung dieses Anwendungsfalls von Ihrem Entwicklungsteam bereitgestellt und unterstützt werden.
- Sie müssen eine clientseitige Logik implementieren, um jeweils eine bestimmte Anzahl von Karten im Karussell anzuzeigen.

