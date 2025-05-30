## Voraussetzungen

Bevor Sie Content-Cards verwenden können, müssen Sie das [Braze Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) in Ihre App integrieren. Dann müssen Sie die Schritte zur Einrichtung Ihrer tvOS App ausführen.

{% alert important %}
Denken Sie daran, dass Sie Ihre eigene angepasste UI implementieren müssen, da Content-Cards über Headless UI mit dem Swift SDK unterstützt werden, das keine Standard-UI oder Standard-Ansichten für tvOS enthält.
{% endalert %}

## Einrichten Ihrer tvOS-App

### Schritt 1: Erstellen Sie eine neue iOS-App

Wählen Sie in Braze **Einstellungen** > **App-Einstellungen** und wählen Sie dann **App hinzufügen**. Geben Sie einen Namen für Ihre tvOS-App ein, wählen Sie **iOS** – _nicht tvOS_ – und dann **App hinzufügen** aus.

![ALT_TEXT.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
Wenn Sie das Kontrollkästchen **tvOS** aktivieren, können Sie die Content-Cards für tvOS nicht anpassen.
{% endalert %}

### Schritt 2: Holen Sie sich den API-Schlüssel für Ihre App

Wählen Sie in Ihren App-Einstellungen Ihre neue tvOS-App aus und notieren Sie sich den API-Schlüssel Ihrer App. Sie verwenden diesen Schlüssel, um Ihre App in Xcode zu konfigurieren.

![ALT_TEXT]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Schritt 3: BrazeKit integrieren

Verwenden Sie den API-Schlüssel Ihrer App, um das [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) in Ihr tvOS-Projekt in Xcode zu integrieren. Sie müssen nur BrazeKit über das Braze Swift SDK integrieren.

### Schritt 4: Angepasste UI erstellen

Da Braze unter tvOS keine Standard-UI für Content-Cards bietet, müssen Sie diese selbst anpassen. Eine ausführliche Anleitung finden Sie in unserem Schritt-für-Schritt-Tutorial: [Anpassen von Content-Cards für tvOS](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/). Ein Beispielprojekt finden Sie unter [Braze Swift SDK Beispiele](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui).
