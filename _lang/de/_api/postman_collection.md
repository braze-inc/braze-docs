---
nav_title: Briefträger und Musteranfragen
article_title: Briefträger und Musteranfragen
page_order: 3
description: "Dieser Referenzartikel behandelt die Braze Postman Collection, was sie ist, wie Sie die Collection einrichten und verwenden und wie Sie Anfragen bearbeiten und versenden."
page_type: reference

---

# Briefträger und Musteranfragen

> Mit Braze können Sie über unsere Postman Collection Beispiel-API-Anfragen für alle unsere Endpunkte generieren. Dieser Referenzartikel behandelt die Braze Postman Collection, was sie ist, wie Sie die Collection einrichten und verwenden und wie Sie Anfragen bearbeiten und versenden.

## Was ist Postman?

Postman ist ein kostenloses visuelles Bearbeitungstool zum Erstellen und Testen von API-Anfragen. Im Gegensatz zu anderen Methoden für die Interaktion mit APIs (z.B. mit cURL) können Sie mit Postman API-Anfragen einfach bearbeiten, Header-Informationen anzeigen und vieles mehr. Postman bietet Ihnen die Möglichkeit, Sammlungen oder Bibliotheken mit vorgefertigten API-Anfragen zu speichern. Um unseren Kunden den Einstieg in unsere REST-API zu erleichtern, haben wir eine Sammlung mit vorgefertigten Beispielen für alle unsere API-Endpunkte erstellt.

Sehen Sie sich unsere Postman Collection an oder laden Sie sie herunter, indem Sie auf **Run in Postman** in unseren [Postman-Dokumenten](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) klicken.

## Verwendung der Braze Postman Kollektion

Wenn Sie über ein Postman-Konto verfügen (Sie können die Versionen für macOS, Windows und Linux von der [Postman-Website][1] herunterladen), können Sie unsere Postman-Dokumentation in Ihrer eigenen Postman-App öffnen, indem Sie auf die orangefarbene Schaltfläche **In Postman ausführen** klicken. Sie können dann [eine Umgebung erstellen](#setting-up-your-postman-environment) oder unsere Braze REST API-Umgebung als Vorlage verwenden und die verfügbaren `POST` und `GET` Anfragen nach Ihren eigenen Bedürfnissen bearbeiten.

### Einrichten Ihrer Postman-Umgebung

{% raw %}
Die Braze Postman Collection verwendet eine Template-Variable, `{{instance_url}}`, um die REST-API-URL Ihrer Braze-Instanz in den vorgefertigten Anfragen zu ersetzen, und die Variable `{{api_key}}` für Ihren API-Schlüssel. Anstatt alle Anfragen in der Sammlung manuell zu bearbeiten, können Sie diese Variable in Ihrer Postman-Umgebung einrichten. Sie können entweder unsere Umgebungsvorlage (Braze REST API Environment Template) aus dem Dropdown-Menü auswählen und die Variablenwerte durch Ihre eigenen ersetzen, oder Sie können Ihre eigene Umgebung einrichten.
{% endraw %}

Um Ihre eigene Umgebung einzurichten, führen Sie die folgenden Schritte aus:

1. Wählen Sie auf der Registerkarte **Arbeitsbereiche** die Option **Umgebungen**.
2. Klicken Sie auf die Schaltfläche **+** plus, um eine neue Umgebung zu erstellen.
3. Geben Sie dieser Umgebung einen Namen (z.B. "Braze API Requests") und fügen Sie Schlüssel für `instance_url` und `api_key` mit Werten hinzu, die Ihrer [Braze-Instanz][7] und Ihrem [Braze REST API Key][8] entsprechen.
4. Klicken Sie auf **Speichern**.

{% alert note %}
In `POST` Anfragekörpern sollte `api_key` in Anführungszeichen eingeschlossen sein: `"MY-API-KEY-EXAMPLE"`. In `GET` URLs sollte dies nicht der Fall sein. Wir haben diese Formatierung bereits in den `POST` Anfragekörpern, `GET` URLs und der Umgebungsvorlage für `YOUR-API-KEY-HERE` in dieser Dokumentation für Sie bereitgestellt.
{% endalert %}

![Hinzufügen von Variablen für API-Schlüssel und Instanz-URL zur Braze REST API-Umgebung in Postman.][3]

### Verwendung der vorgefertigten Anfragen aus der Sammlung

Nachdem Sie Ihre Umgebung konfiguriert haben, können Sie jede der vorgefertigten Anfragen in der Sammlung als Vorlage für die Erstellung neuer API-Anfragen verwenden. Um eine der vorgefertigten Anfragen zu verwenden, klicken Sie im Menü **Sammlungen** von Postman auf diese. Dadurch wird die Anfrage in einer neuen Registerkarte im Hauptfenster der Postman-App geöffnet.

Im Allgemeinen gibt es zwei Arten von Anfragen, die Braze API-Endpunkte akzeptieren - `GET` und `POST`. Je nachdem, welche `HTTP` Methode der Endpunkt verwendet, müssen Sie die vorgefertigte Anfrage anders bearbeiten.

#### Eine POST-Anfrage bearbeiten

Wenn Sie eine `POST` Anfrage bearbeiten, öffnen Sie die Anfrage und navigieren Sie im Anfrage-Editor zum Abschnitt **Body**. Wählen Sie zur besseren Lesbarkeit das Optionsfeld **raw**, um den `JSON` Anfragekörper zu formatieren.

![Registerkarte Body bei der Bearbeitung einer POST User Track-Anfrage in Postman][4]

#### Eine GET-Anfrage bearbeiten

Wenn Sie eine `GET` Anfrage bearbeiten, bearbeiten Sie die in der Anfrage-URL übergebenen Parameter. Wählen Sie dazu die Registerkarte **Params** und bearbeiten Sie die Schlüssel-Wert-Paare in den angezeigten Feldern.

![Registerkarte Parameter bei der Bearbeitung einer GET Query List of Unsubscribed Email Addresses Anfrage in Postman.][5]

### Senden Sie Ihre Anfrage

Nachdem Ihre API-Anfrage fertig ist, klicken Sie auf **Senden**. Die Anfrage wird gesendet und die Antwortdaten werden in einem Bereich unterhalb des Anfrage-Editors angezeigt. Von hier aus können Sie die von der Braze-API zurückgegebenen Rohdaten, den HTTP-Antwortcode, die Dauer der Bearbeitung der Anfrage und die Header-Informationen einsehen.

![Beispiel Body-Antwortdaten einer POST-Anfrage mit dem Status 201 Erstellt und einer Antwortzeit von 269 Millisekunden.][6]

[1]: https://www.getpostman.com
[3]: {% image_buster /assets/img_archive/postman_variable.png %}
[4]: {% image_buster /assets/img_archive/postman_post.png %}
[5]: {% image_buster /assets/img_archive/postman_get.png %}
[6]: {% image_buster /assets/img_archive/postman_response.png %}
[7]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[8]: {{site.baseurl}}/api/api_key/
