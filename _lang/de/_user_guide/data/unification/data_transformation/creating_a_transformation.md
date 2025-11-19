---
nav_title: Eine Transformation schaffen
article_title: Eine Transformation schaffen
page_order: 1
page_type: reference
description: "Dieser referenzierte Artikel beschreibt die Schritte zur Erstellung einer Transformation mit Braze Data Transformation."
---

# Eine Transformation schaffen

> Mit Braze Data Transformation können Sie Webhook-Integrationen erstellen und verwalten, um den Datenfluss von externen Plattformen in Braze zu automatisieren. Diese Webhook-Integrationen können dann noch leistungsfähigere Anwendungsfälle im Marketing unterstützen. Sie können Ihre Datentransformation aus dem Standard Code erstellen oder unsere spezielle Bibliothek mit Templates verwenden, um Ihnen den Einstieg in bestimmte externe Plattformen zu erleichtern.

## Voraussetzungen 

| Anforderung | Beschreibung |
| --- | --- |
| Zwei-Faktor-Authentifizierung oder SSO | Sie müssen die [Zwei-Faktor-Authentifizierung]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#two-factor-authentication) (2FA) oder [Single Sign-on]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#single-sign-on-sso-authentication) (SSO) für Ihr Konto aktivieren. |
| Berechtigungen korrigieren | Sie müssen entweder Account Manager oder Workspace Administrator sein oder über die Nutzer:innen-Berechtigung "Transformationen verwalten" verfügen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Schritt 1: Bezeichner für eine Quellplattform

Identifizieren Sie eine externe Plattform, die Sie mit Braze verbinden möchten, und überprüfen Sie, ob die Plattform Webhooks unterstützt. Diese Einstellungen werden manchmal auch als "API-Benachrichtigungen" oder "Anfragen für Webdienste" bezeichnet.

Im Folgenden finden Sie ein Beispiel für einen [Typeform Webhook](https://www.typeform.com/help/a/webhooks-360029573471/), der durch Anmeldung bei der Plattform konfiguriert werden kann:

![]({% image_buster /assets/img/data_transformation/data_transformation8.png %})

## Schritt 2: Erstellen Sie eine Transformation

{% multi_lang_include create_transformation.md location="default" %}

## Schritt 3: Senden Sie einen Test-Webhook (empfohlen)

Dieser Schritt ist optional, aber wir empfehlen, einen Test-Webhook von Ihrer Ausgangsplattform an Ihre neu erstellte Transformation zu senden.

1. Kopieren Sie die URL aus Ihrer Transformation.
2. Suchen Sie in Ihrer Quellplattform nach einer "Test senden"-Funktion, um einen Webhook zu generieren, der an diese URL gesendet wird. 
- Wenn Ihre Quellplattform nach einem Typ für die Anfrage fragt, wählen Sie **POST**.
- Wenn Ihre Quellplattform Authentifizierungsoptionen bietet, wählen Sie **Keine Authentifizierung**.
- Wenn Ihre Quellplattform nach Geheimnissen fragt, wählen Sie **Keine Geheimnisse**.
3. Aktualisieren Sie Ihre Seite im Braze-Dashboard, um zu sehen, ob der Webhook empfangen wurde. Wenn er empfangen wurde, sollten Sie unter **Neuester Webhook** eine Webhook-Nutzlast sehen.

So sieht es bei Typeform aus:

![Beispiel für einen Code zur Datentransformation, der den Webhook auf Braze-Nutzerprofile abbildet.]({% image_buster /assets/img/data_transformation/data_transformation11.png %})

{% alert note %}
Braze Data Transformation unterstützt möglicherweise noch keine externen Plattformen, die eine spezielle Überprüfung oder Authentifizierung für Webhooks erfordern. Wenn Sie sich für diese Art von Plattform mit Braze Data Transformation interessieren, sollten Sie ein [Feedback zu Ihrem Produkt]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) abgeben.
{% endalert %}

## Schritt 4: Schreiben Sie Code für die Transformation

Wenn Sie wenig bis gar keine Erfahrung mit JavaScript Code haben oder detailliertere Anweisungen bevorzugen, folgen Sie dem **Beginner - POST: Nutzer:innen tracken** oder **Anfänger - PUT: Mehrere Artikel aktualisieren** Tab zum Schreiben Ihres Codes für die Transformation.

Wenn Sie Entwickler:in sind oder über umfangreiche Erfahrung mit JavaScript Code verfügen, folgen Sie dem **Advanced - POST: Tracking von Nutzer:innen** Tab für ausführliche Anweisungen zum Schreiben Ihres Transformation Codes.

{% alert tip %}
Braze Data Transformation verfügt über einen KI-Copiloten, der ChatGPT um Hilfe beim Schreiben Ihres Codes bittet. Um auf den KI-Kopiloten zuzugreifen, wählen Sie <i class="fa-solid fa-wand-magic-sparkles"></i> **Code für die Transformation erzeugen**. Um dies zu nutzen, muss ein Webhook an Ihre Transformation gesendet werden. Sie können auch auf die Bibliothek der Templates zugreifen, indem Sie **Code einfügen** > **Template einfügen** auswählen.

![]({% image_buster /assets/img/data_transformation/data_transformation3.png %})
{% endalert %}

{% tabs %}
{% tab Beginner - Track users %}

Schreiben Sie hier den Code für die Transformation, um zu definieren, wie verschiedene Webhook-Werte auf Braze-Nutzerprofile abgebildet werden.

1. Neue Transformationen haben dieses Standard Template im Abschnitt **Transformation Code**:

```java
// Here, we will define a variable, "brazecall", to build up a `/users/track` request
// Everything from the incoming webhook is accessible via the special variable "payload"
// So you can template in desired values in your `/users/track` request with dot notation, such as payload.x.y.z

let brazecall = {
  "attributes": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "attribute_1": payload.attribute_1
    }
  ],
  "events": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "name": payload.event_1,
      "time": new Date(),
      "properties": {
        "property_1": payload.event_1.property_1
      }
    }
  ],
  "purchases": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "product_id": payload.product_id,
      "currency": payload.currency,
      "price": payload.price,
      "quantity": payload.quantity,
      "time": payload.timestamp,
      "properties": {
        "property_1": payload.purchase_1.property_1
      }
    }
  ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2\. Um angepasste Attribute, angepasste Events und Käufe in Ihre Transformationsaufrufe einzubeziehen, fahren Sie mit Schritt 3 fort. Andernfalls löschen Sie die Abschnitte, die Sie nicht benötigen.<br><br>
3\. Für jedes Attribut, jedes Kauf-Event und jedes Kauf-Objekt ist ein Nutzer:in erforderlich, entweder ein `external_id`, `user_alias`, `braze_id`, `email` oder `phone`. Suchen Sie den Bezeichner des Nutzers:in der Nutzlast des eingehenden Webhooks und fügen Sie diesen Wert als Template in Ihren Transformation Code über eine Nutzlastzeile ein. Verwenden Sie die Punktnotation, um auf die Eigenschaften von Nutzlastobjekten zuzugreifen. <br><br>
4\. Finden Sie die Webhook-Werte, die Sie als Attribute, Ereignisse oder Käufe darstellen möchten, und erstellen Sie ein Template für diese Werte in Ihrem Transformation Code über eine Payload-Zeile. Verwenden Sie die Punktnotation, um auf die Eigenschaften von Nutzlastobjekten zuzugreifen.<br><br>
5\. Prüfen Sie für jedes Attribut, Ereignis und Kauf-Objekt den Wert `_update_existing_only`. Setzen Sie dies auf `false`, wenn Sie möchten, dass die Transformation einen neuen Nutzer:innen erstellt, der möglicherweise noch nicht existiert. Belassen Sie dies auf `true`, um nur bestehende Profile zu aktualisieren.<br><br>
6\. Klicken Sie auf **Validieren**, um eine Vorschau auf die Ausgabe Ihres Codes zu erhalten und um zu prüfen, ob es sich um eine akzeptable Anfrage handelt `/users/track`.<br><br>
7\. Aktivieren Sie Ihre Transformation. Wenn Sie weitere Hilfe zu Ihrem Code benötigen, bevor Sie ihn aktivieren, wenden Sie sich an Ihren Braze-Konto Manager:in.<br><br>
7\. Lassen Sie Ihre Quellplattform mit dem Senden von Webhooks beginnen. Ihr Code für die Transformation wird für jeden eingehenden Webhook ausgeführt, und die Nutzerprofile werden aktualisiert. 

Ihre Webhook-Integration ist nun vollständig!

{% endtab %}
{% tab Beginner - Update catalog items %}

Hier können Sie Transformations-Code schreiben, um zu definieren, wie Sie verschiedene Webhook-Werte auf Updates von Braze-Katalogartikeln abbilden möchten.

1. Neue Transformationen enthalten dieses Standard Template im Abschnitt **Transformations Code**:

```java
// This is a default template that you can use as a starting point
// Feel free to delete this entirely to start from scratch, or to edit specific components

// First, this code defines a variable, "brazecall", to build a PUT /catalogs/{catalog_name}/items request
// Everything from the incoming webhook is accessible via the special variable "payload"
// As such, you can template in desired values in your request with JS dot notation, such as payload.x.y.z

let brazecall = {
  // For Braze Data Transformation to update Catalog items, the special variable "catalog_name" is required
  // This variable is used to specify the catalog name which would otherwise go in the request URL
  "catalog_name": "catalog_name",
  
  // After defining "catalog name", construct the Update Multiple Catalog Items request as usual below
  // Documentation for the destination endpoint: https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/
  "items": [
    {
      "id": payload.item_id_1,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_2,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_3,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    }
  ]
};

// After the request body is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2\. Transformationen für `/catalogs` Ziele erfordern eine `catalog_name`, um den spezifischen Katalog zu definieren, der aktualisiert werden soll. Sie können dieses Feld fest codieren oder das Feld über eine Payload-Zeile mit einem Webhook-Feld templateen. Verwenden Sie die Punktnotation, um auf die Eigenschaften von Nutzlastobjekten zuzugreifen.<br><br>
3\. Definieren Sie die Artikel, die Sie im Katalog aktualisieren möchten, mit den Feldern `id` im Array Artikel. Sie können diese Felder fest codieren oder ein Template in ein Webhook-Feld über eine Nutzdatenzeile einfügen. <br><br> Denken Sie daran, dass `catalog_column` ein Platzhalterwert ist. Achten Sie darauf, dass Artikelobjekte nur Felder enthalten, die im Katalog vorhanden sind.<br><br>
4\. Wählen Sie **Validieren**, um eine Vorschau auf die Ausgabe Ihres Codes zu erhalten und um zu prüfen, ob es sich um eine akzeptable Anfrage für den [Endpunkt Mehrere Artikel aktualisieren]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) handelt.<br><br>
5\. Aktivieren Sie Ihre Transformation. Wenn Sie weitere Hilfe zu Ihrem Code benötigen, bevor Sie ihn aktivieren, wenden Sie sich an Ihren Braze-Konto Manager:in.<br><br>
6\. Vergewissern Sie sich, ob Ihre Quellplattform über eine Einstellung zum Senden von Webhooks verfügt. Ihr Code für die Transformation wird für jeden eingehenden Webhook ausgeführt und die Artikel im Katalog werden aktualisiert.

Ihre Webhook-Integration ist nun vollständig!

{% endtab %}
{% tab Advanced - Track users %}

In diesem Schritt transformieren Sie die Webhook-Nutzdaten von der Quellplattform in einen Rückgabewert für ein JavaScript-Objekt. Dieser Rückgabewert muss dem Format des Körpers der Anfrage für den Endpunkt `/users/track` entsprechen:

- Der Code für die Transformation wird in der Programmiersprache JavaScript akzeptiert. Jeder Standard-JavaScript-Kontrollfluss, wie z.B. die if/else-Logik, wird unterstützt.
- Der Code der Transformation greift über die Variable `payload` auf den Körper der Webhook-Anfrage zu. Diese Variable ist ein Objekt, das durch das Parsen des JSON-Körpers der Anfrage erstellt wird.
- Alle Features, die in unserem `/users/track` Endpunkt unterstützt werden, werden unterstützt, einschließlich:
  - Nutzer:in-Objekte, Ereignis-Objekte und Kauf-Objekte mit Attributen
  - Verschachtelte Attribute und verschachtelte Eigenschaften von angepassten Events
  - Updates für Abo-Gruppen
  - E-Mail Adresse als Bezeichner

Wählen Sie **Validieren** aus, um eine Vorschau auf die Ausgabe Ihres Codes zu erhalten und um zu prüfen, ob es sich um eine akzeptable `/users/track` Anfrage handelt.

{% alert note %}
Externe Netzwerkanfragen, Bibliotheken von Drittanbietern und Webhooks, die nicht JSON sind, werden derzeit nicht unterstützt.
{% endalert %}

{% endtab %}
{% endtabs %}

## Schritt 5: Überwachen Sie Ihre Transformation

Nachdem Sie Ihre Transformation aktiviert haben, finden Sie in den Analytics auf der Hauptseite **Transformationen** eine Zusammenfassung der Performance.

* **Eingehende Anfragen:** Dies ist die Anzahl der Webhooks, die unter der URL dieser Transformation empfangen wurden. Wenn die eingehenden Anfragen 0 sind, hat Ihre Quellplattform keine Webhooks übermittelt, oder die Verbindung kann nicht hergestellt werden.
* **Zustellungen:** Nach dem Empfang eingehender Anfragen wendet die Datentransformation Ihren Code zur Transformation an, um ihn an das ausgewählte Ziel in Braze zu senden.

Es ist ein gutes Ziel, dass 100% der eingehenden Anfragen zu Zustellungen führen. Die Anzahl der Zustellungen wird niemals die Anzahl der eingehenden Anfragen übersteigen.

### Fehlersuche

Für eine detailliertere Überwachung und Fehlerbehebung finden Sie auf der Seite **Protokolle** spezifische Protokolle, in denen die letzten 1.000 eingehenden Anfragen an alle Transformationen in Ihren Workspaces protokolliert werden. Sie können jedes Protokoll auswählen, um den Body der eingehenden Anfrage, den Output der Transformation und den Response Body des Ziels der Transformation anzuzeigen.

Wenn es keine Zustellungen gibt, überprüfen Sie Ihren Code für die Transformation auf Syntaxfehler und stellen Sie sicher, dass der Code kompiliert werden kann. Prüfen Sie dann, ob die Ausgabe eine gültige Anfrage für ein Ziel ist.

Zustellungen, die geringer sind als die Anzahl der eingehenden Anfragen, zeigen an, dass zumindest einige Webhooks erfolgreich zugestellt wurden. Schauen Sie in den Transformationsprotokollen nach, ob die Ausgabe der Transformation den Erwartungen entspricht. Es ist möglich, dass Ihr Code für die Transformation nicht alle Varianten der empfangenen Webhooks berücksichtigt.


