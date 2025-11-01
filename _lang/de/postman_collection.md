---
nav_title: Postbote und Musteranfragen
article_title: Briefträger und Musteranfragen
page_order: 3
description: "Dieser referenzierte Artikel behandelt die Braze Postman Collection, was sie ist, wie Sie die Collection einrichten und verwenden und wie Sie Anfragen bearbeiten und versenden können."
page_type: reference

---

# Postbote und Musteranfragen

> Braze ermöglicht es Ihnen, über unsere Postman Collection API-Anfragen für alle unsere Endpunkte zu generieren. Dieser referenzierte Artikel behandelt die Braze Postman Collection, was sie ist, wie Sie die Collection einrichten und verwenden und wie Sie Anfragen bearbeiten und versenden können.

## Was ist Postman?

Postman ist ein kostenloses visuelles Bearbeitungstool zum Erstellen und Testen von API-Anfragen. Im Gegensatz zu anderen Methoden für die Interaktion mit APIs (z.B. mit cURL) können Sie mit Postman API-Anfragen einfach bearbeiten, Header-Informationen anzeigen und vieles mehr. Postman bietet Ihnen die Möglichkeit, Sammlungen oder Bibliotheken mit vorgefertigten API-Anfragen zu speichern. Um unseren Kund:innen den Einstieg in unsere REST API zu erleichtern, haben wir eine Sammlung mit vorgefertigten Beispielen für alle unsere API-Endpunkte erstellt.

Sehen Sie sich unsere Postman Collection an oder laden Sie sie herunter, indem Sie auf **Run in Postman** in unseren [Postman-Dokumenten](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) klicken.

## Verwendung der Braze Postman Kollektion

Wenn Sie ein Postman-Konto haben (Sie können die macOS-, Windows- und Linux-Versionen von der [Postman Website](https://www.getpostman.com) herunterladen), können Sie unsere Dokumentation in Ihrer eigenen Postman App öffnen, indem Sie auf den orangefarbenen Button **In Postman ausführen** klicken. Sie können dann [eine Umgebung erstellen](#setting-up-your-postman-environment) oder unsere Braze REST API-Umgebung als Template verwenden und die verfügbaren `POST` und `GET` Anfragen nach Ihren eigenen Bedürfnissen bearbeiten.

### Einrichten Ihrer Postman-Umgebung

{% raw %}
Die Braze Postman Collection verwendet eine Template-Variable, `{{instance_url}}`, um die REST API-URL Ihrer Braze-Instanz in den vorgefertigten Anfragen zu ersetzen, und die Variable `{{api_key}}` für Ihren API-Schlüssel. Anstatt alle Anfragen in der Collection manuell zu bearbeiten, können Sie diese Variable in Ihrer Postman-Umgebung einrichten. Sie können entweder unsere Template-Umgebung (Braze REST API Environment Template) aus dem Dropdown-Menü auswählen und die Variablenwerte durch Ihre eigenen ersetzen, oder Sie können Ihre eigene Umgebung einrichten.
{% endraw %}

Um Ihre eigene Umgebung einzurichten, führen Sie die folgenden Schritte aus:

1. Wählen Sie auf dem Tab **Workspaces** die Option **Umgebungen** aus.
2. Klicken Sie auf den **+** plus Button, um eine neue Umgebung zu erstellen.
3. Geben Sie dieser Umgebung einen Namen (z.B. "Braze API Requests") und fügen Sie Schlüssel für `instance_url` und `api_key` mit Werten hinzu, die Ihrer [Braze-Instanz]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) und Ihrem [Braze REST API-Schlüssel]({{site.baseurl}}/api/api_key/) entsprechen.
4. Klicken Sie auf **Speichern**.

{% alert note %}
In `POST` Anfragekörpern sollte die `api_key` in Anführungszeichen eingeschlossen sein: `"MY-API-KEY-EXAMPLE"`. In `GET` URLs sollte dies nicht der Fall sein. Wir haben diese Formatierung bereits in den `POST` Anfragekörpern, `GET` URLs und der Umgebungsvorlage für `YOUR-API-KEY-HERE` in dieser Dokumentation für Sie bereitgestellt.
{% endalert %}

![Hinzufügen von Variablen für API-Schlüssel und Instanz-URL zur REST API-Umgebung von Braze in Postman.]({% image_buster /assets/img_archive/postman_variable.png %})

### Verwendung der vorgefertigten Anfragen aus der Sammlung

Nachdem Sie Ihre Umgebung konfiguriert haben, können Sie jede der vorgefertigten Anfragen in der Sammlung als Template für die Erstellung neuer APIs verwenden. Um eine der vorgefertigten Anfragen zu verwenden, klicken Sie im Menü **Sammlungen** von Postman auf diese. Dadurch wird die Anfrage in einem neuen Tab im Hauptfenster der Postman App geöffnet.

Im Allgemeinen gibt es zwei Arten von Anfragen, die Braze API Endpunkte akzeptieren - `GET` und `POST`. Je nachdem, welche `HTTP` Methode der Endpunkt verwendet, müssen Sie die vorgefertigte Anfrage anders bearbeiten.

#### Bearbeiten einer POST-Anfrage

Wenn Sie eine `POST` Anfrage bearbeiten, öffnen Sie die Anfrage und navigieren Sie zum Abschnitt **Body** im Anfrage-Editor. Um die Lesbarkeit zu verbessern, wählen Sie den Button **Rohdaten** aus, um den Body der Anfrage `JSON` zu formatieren.

![Body Tab beim Bearbeiten einer POST User Tracking Anfrage in Postman]({% image_buster /assets/img_archive/postman_post.png %})

#### Eine GET-Anfrage bearbeiten

Wenn Sie eine `GET` Anfrage bearbeiten, bearbeiten Sie die in der Anfrage-URL übergebenen Parameter. Wählen Sie dazu den Tab **Params** und bearbeiten Sie die Schlüssel-Wert-Paare in den angezeigten Feldern.

![Tab Params bei der Bearbeitung einer Anfrage GET Query List of Unsubscribed Email Addresses in Postman.]({% image_buster /assets/img_archive/postman_get.png %})

### Senden Sie Ihre Anfrage

Nachdem Ihre API-Anfrage fertig ist, klicken Sie auf **Senden**. Die Anfrage wird gesendet und die Daten der Antwort werden in einem Bereich unterhalb des Anfrage-Editors angezeigt. Von hier aus können Sie die von der Braze API zurückgegebenen Rohdaten, den HTTP Response Code, die Dauer der Bearbeitung der Anfrage und die Header-Informationen einsehen.

![Beispiel für Body-Antwortdaten aus einer POST-Anfrage mit dem Status 201 Erstellt und einer Antwortzeit von 269 Millisekunden.]({% image_buster /assets/img_archive/postman_response.png %})

