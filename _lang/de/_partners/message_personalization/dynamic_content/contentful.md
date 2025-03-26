---
nav_title: Contentful
article_title: Contentful
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Contentful, einem Content-Management-System, das es Ihnen ermöglicht, mit Connected Content dynamisch Inhalte aus Contentful in Ihre Braze-Kampagnen zu ziehen."
alias: /partners/contentful/
page_type: partner
search_tag: Partner
---

# Contentful

>[Contentful](https://www.contentful.com/) ist ein Headless Content Management System, mit dem Sie Inhalte erstellen, verwalten und auf jeder Plattform verteilen können. Im Gegensatz zu einem Content Management System (CMS) können Sie bei Contentful Ihr Inhaltsmodell selbst erstellen, so dass Sie entscheiden können, welche Inhalte Sie verwalten möchten.<br><br>Auf dieser Seite finden Sie eine Schritt-für-Schritt-Anleitung zur Konfiguration von Braze Connected Content für den Abruf von Daten aus der Content Delivery API von Contentful. 

Nach der Integration können Sie die RESTful-APIs von Contentful nutzen, um Ihre Inhalte über verschiedene Kanäle wie Websites, mobile Apps (iOS, Android und Windows) oder viele andere Plattformen bereitzustellen. Sie können auch dynamisch Inhalte aus Contentful zur Verwendung in Ihren Braze-Kampagnen abrufen.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung          | Beschreibung                        |
|-----------------------|------------------------------------|
| A Zufriedenes Konto | Sie benötigen ein Contentful-Konto mit Zugriff auf die Content Delivery API. |
| Ein Braze-Konto | Sie benötigen ein Braze-Konto mit Zugriff auf die Funktion Connected Content. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation/) verwenden, können Sie einen API-Schlüssel unter **Entwicklerkonsole** > **API-Einstellungen** erstellen.
{% endalert %}

## Integration

### Schritt 1: Holen Sie sich Ihre Contentful-API-Anmeldeinformationen

1. [Melden Sie sich](https://app.contentful.com/login) mit Ihren Anmeldedaten [bei Contentful an](https://app.contentful.com/login).
2. Erstellen oder rufen Sie API-Zugriffstoken im Contentful-Dashboard ab, indem Sie zu **Einstellungen** > **API-Schlüssel** gehen. Wenn Sie noch keinen API-Schlüssel haben, erstellen Sie einen neuen:<br>2.1 Wählen Sie **API-Schlüssel hinzufügen**.<br>2.2 Geben Sie die erforderlichen Details ein und wählen Sie die entsprechende Umgebung aus.<br>2.3 Wählen Sie **Speichern** und notieren Sie sich die **Space ID** und das **Content Delivery API - Access Token**.
3. Bestimmen Sie das Inhaltsmodell, auf das Sie über die Contentful-API zugreifen möchten.

### Schritt 2: Konfigurieren Sie Braze Connected Content

1. [Melden Sie sich](https://dashboard.braze.com/sign_in) mit Ihren Anmeldedaten [bei Braze an](https://dashboard.braze.com/sign_in).
2. Gehen Sie im Braze Dashboard zu **Vorlagen** > **Inhaltsblöcke** > **Inhaltsblock erstellen** > **HTML-Inhaltsblock**.
3. Erstellen Sie eine Anfrage für Connected Content an die Contentful [Content Delivery API URL](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/links) von Contentful. Ein Beispiel für die Contentful Content Delivery API URL ist ```https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries```.<br><br> Das Abrufen verschiedener Assets erfordert die Einbeziehung bestimmter Variablen. Die Beispiel-URL-Anfrage für Connected Content zielt auf den [Entry-Endpunkt](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries/entry/get-a-single-entry/console) von Contentful. Dieser Endpunkt benötigt Variablen wie `{space_id}` und `{environment_id}`, oder `{entry_id}` und `{access_token}`. Diese können von Ihrer Contentful-Instanz übernommen werden. In diesem Beispiel Content Block müssen die Variablen durch Ihre Contentful Space ID und Environment ID ersetzt werden.<br><br>Die Beispiel-URL der Content Delivery API verwendet nur einen der verfügbaren Endpunkte von Contentful. Verschiedene Anwendungsfälle können durch die Verwendung verschiedener URLs erreicht werden. Die [Image API](https://www.contentful.com/developers/docs/references/images-api/) kann zum Beispiel verwendet werden, um in Contentful gespeicherte Bilder zu erfassen. Weitere Informationen finden Sie unter [Content Delivery API](https://www.contentful.com/developers/docs/references/content-delivery-api/).

{% alert note %}
Für verschiedene Endpunkte können neue Variablen erforderlich sein, z.B. erfordert die Bilder-API eine `{asset_id}`, `{unique_id},` und `{name}`. Für weitere Informationen wenden Sie sich bitte an Contentful.
{% endalert %}

{% raw %}
```json
        {% assign space_id = "YOUR-CONTENTFUL-SPACE-ID"}
        {% assign environment_id = "YOUR-CONTENTFUL-ENVIRONMENT-ID"}
        {% assign entry_id = "YOUR-CONTENTFUL-ENTRY-ID"}
        {% assign access_token = "YOUR-CONTENTFUL-ACCESS-TOKEN"}
         {% connected_content https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries/{entry_id}?access_token={access_token}
         :method get
         :headers {
             "Authorization": "YOUR_CONTENTFUL_ACCESS_TOKEN"
                 }
               :content_type application/json
               :save response %}
```
{% endraw %}

{: start="4"}
4\. Verwenden Sie "Test Endpoint", um zu testen, ob Braze sich erfolgreich mit der Contentful-API verbinden und die gewünschten Daten abrufen kann.
5\. Wählen Sie **Fertig**, um Ihren Inhaltsblock zu speichern.
6\. Geben Sie Ihrem Inhaltsblock einen beschreibenden Namen, z. B. "Contentful API", und wählen Sie dann **Inhaltsblock starten**.

### Schritt 3: Verwenden Sie verknüpfte Inhalte in Kampagnen und Werbekampagnen

1. Erstellen Sie in Braze eine neue Kampagne oder bearbeiten Sie eine bestehende Kampagne.
2. Verwenden Sie den Block Connected Content, um Daten aus Contentful einzufügen. Verwenden Sie die Datenpfade, die Sie während der Konfiguration definiert haben, um den Inhalt der Kampagne dynamisch aufzufüllen.<br><br>
- **Antwortpfad:** Nachdem Sie den Inhaltsblock in eine Braze-Kampagne oder ein Canvas eingebunden haben, wird die Antwort verfügbar, wenn Sie die Variable `{response}` in Ihre Nachricht einfügen.<br><br>Mit der JSON-Punktnotation können Sie angeben, welchen Teil des Antwortkörpers von Contentful Sie in Ihre Nachricht aufnehmen möchten. Dies hängt von Ihrem Anwendungsfall ab. Sie können zum Beispiel den Wert title ({% raw %}```liquid{{response.items[0].fields.title}}```{% endraw %}) vom Contentful-Endpunkt Entry verwenden und erhalten eine Antwort wie diese:

{% raw %}
```json
   {
  "fields": {
    "title": {
      "en-US": "Hello!"
    },
    "body": {
      "en-US": "This is a sample message!"
    }
  },
  "metadata": {
    "tags": [
      {
        "sys": {
          "type": "Link",
          "linkType": "Tag",
          "id": "nyCampaign"
        }
      }
    ]
  },
  "sys": {
    "id": "5KsDBWseXY6QegucYAoacS",
    "type": "Entry",
    "version": 1,
    "space": {
      "sys": {
        "type": "Link",
        "linkType": "Space",
        "id": "yadj1kx9rmg0"
      }
    },
    "contentType": {
      "sys": {
        "type": "Link",
        "linkType": "ContentType",
        "id": "hfM9RCJIk0wIm06WkEOQY"
      }
    },
    "createdAt": "2016-12-20T10:43:35.772Z",
    "updatedAt": "2016-12-20T10:43:35.772Z",
    "revision": 1
  }
}
```
{% endraw %}

{: start="3" }
3\. Zeigen Sie eine Vorschau an und testen Sie Ihre Kampagne, um sicherzustellen, dass die Connected Content-Daten korrekt angezeigt werden.
4\. Wenn Sie mit der Einrichtung zufrieden sind, starten Sie Ihre Kampagne.

## Fehlersuche

### API-Antwort

Vergewissern Sie sich, dass Ihre Contentful-API-Anmeldedaten und die Endpunkt-URL korrekt sind. Prüfen Sie auf Fehlermeldungen in Braze, die auf Probleme mit dem API-Aufruf hinweisen könnten.

### Datenzuordnung

Überprüfen Sie, ob die Antwortpfad-Zuordnungen korrekt konfiguriert sind und ob die API-Antwortstruktur Ihren Erwartungen entspricht.

## Zusätzliche Ressourcen

- [Contentful Content Delivery API Dokumentation](https://www.contentful.com/developers/docs/references/content-delivery-api/)
- [Braze Connected Inhalt]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)
- [Löten von Inhaltsblöcken]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
