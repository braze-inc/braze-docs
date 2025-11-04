---
nav_title: Contentful
article_title: Contentful
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Contentful, einem Content-Management-System, das es Ihnen erlaubt, dynamisch Connected-Content zu nutzen, um Inhalte aus Contentful in Ihre Braze Kampagnen zu ziehen."
alias: /partners/contentful/
page_type: partner
search_tag: Partner
---

# Contentful

>[Contentful](https://www.contentful.com/) ist ein Headless Content Management System, mit dem Sie Inhalte erstellen, verwalten und auf jeder Plattform verbreiten können. Im Gegensatz zu einem Content Management System (CMS) ist es bei Contentful zulässig, dass Sie Ihr Inhaltsmodell erstellen, so dass Sie entscheiden können, welche Inhalte Sie verwalten möchten.<br><br>Auf dieser Seite finden Sie eine schrittweise Anleitung zur Konfiguration von Braze Connected Content, um Daten von der Contentful API für die Zustellung von Inhalten abzurufen. 

Nach der Integration können Sie die RESTful APIs von Contentful nutzen, um Ihre Inhalte über verschiedene Kanäle wie Websites, mobile Apps (iOS, Android und Windows) oder viele andere Plattformen zuzustellen. Sie können auch dynamisch Inhalte von Contentful abrufen, um sie in Ihren Kampagnen zu verwenden.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung          | Beschreibung                        |
|-----------------------|------------------------------------|
| Ein Contentful-Konto | Sie benötigen ein Contentful-Konto mit Zugriff auf die Content Delivery API. |
| Ein Braze-Konto | Sie benötigen ein Braze-Konto mit Zugriff auf das Connected-Content Feature. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erhalten Sie Ihre Contentful API-Zugangsdaten

1. [Melden Sie sich bei Contentful an](https://app.contentful.com/login), indem Sie Ihre Zugangsdaten eingeben.
2. Erstellen oder rufen Sie API-Zugangs-Token im Contentful Dashboard unter **Einstellungen** > **API-Schlüssel** ab. Wenn Sie noch keinen API-Schlüssel haben, erstellen Sie einen neuen:<br>2.1 Wählen Sie **API-Schlüssel hinzufügen**.<br>2.2 Geben Sie die erforderlichen Details ein und wählen Sie die entsprechende Umgebung aus.<br>2.3 Wählen Sie **Speichern** und notieren Sie sich die **Space ID** und das **Content Delivery API - Zugangstoken**.
3. Identifizieren Sie das Inhaltsmodell, auf das Sie über die Contentful API zugreifen möchten.

### Schritt 2: Konfigurieren Sie Braze Connected-Content

1. [Melden Sie sich bei Braze an](https://dashboard.braze.com/sign_in), indem Sie Ihre Zugangsdaten eingeben.
2. Gehen Sie im Braze-Dashboard zu **Templates** > **Content-Blöcke** > **Content-Block erstellen** > **HTML Content-Block**.
3. Erstellen Sie eine Connected-Content-Anfrage an die Contentful [API URL für die Zustellung von Contentful-Inhalten](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/links). Ein Beispiel für die Contentful Content Delivery API URL ist ```https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries```.<br><br> Das Abrufen verschiedener Assets erfordert die Einbeziehung bestimmter Variablen. Die beispielhafte Connected-Content-URL-Anfrage zielt auf den Eingang-Endpunkt von Contentful [.](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries/entry/get-a-single-entry/console)  Dieser Endpunkt benötigt Variablen wie `{space_id}` und `{environment_id}`, oder `{entry_id}` und `{access_token}`. Diese können von Ihrer Contentful Instanz übernommen werden. In diesem Beispiel Content-Block müssen die Variablen durch Ihre Contentful Space ID und Environment ID ersetzt werden.<br><br>Die Beispiel-URL der Content Delivery API verwendet nur einen der verfügbaren Endpunkte von Contentful. Verschiedene Anwendungsfälle können durch das Nutzen verschiedener URLs erreicht werden. Die [Image API](https://www.contentful.com/developers/docs/references/images-api/) kann zum Beispiel dazu verwendet werden, in Contentful gespeicherte Bilder zu erfassen. Weitere Informationen finden Sie unter [Content Delivery API](https://www.contentful.com/developers/docs/references/content-delivery-api/).

{% alert note %}
Verschiedene Endpunkte können neue Variablen erfordern, zum Beispiel die Images API erfordert eine `{asset_id}`, `{unique_id},` und `{name}`. Für weitere Informationen wenden Sie sich bitte an Contentful.
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
4\. Verwenden Sie "Endpunkt testen", um zu prüfen, ob Braze sich erfolgreich mit der Contentful API verbinden und die gewünschten Daten abrufen kann.
5\. Wählen Sie **Fertig**, um Ihren Content-Block zu speichern.
6\. Geben Sie Ihrem Content-Block einen beschreibenden Namen, z. B. "Contentful API", und wählen Sie dann **Content-Block starten**.

### Schritt 3: Verwenden Sie Connected-Content in Kampagnen und Werbekampagnen

1. Erstellen Sie in Braze eine neue Kampagne oder bearbeiten Sie eine bestehende Kampagne.
2. Verwenden Sie den Connected-Content-Block, um von Contentful abgerufene Daten einzufügen. Verwenden Sie die Datenpfade, die Sie bei der Konfiguration festgelegt haben, um den Inhalt der Kampagne dynamisch zu füllen.<br><br>
- **Antwortpfad:** Nachdem Sie den Content-Block in eine Braze-Kampagne oder ein Braze-Canvas eingebunden haben, wird die Antwort verfügbar, wenn Sie die Variable `{response}` in Ihre Nachricht einfügen.<br><br>Mit der JSON-Punktnotation können Sie angeben, welchen Teil des Antwortkörpers von Contentful Sie in Ihre Nachricht aufnehmen möchten. Dies hängt von Ihrem Anwendungsfall ab. Sie können zum Beispiel den Titelwert ({% raw %}```liquid{{response.items[0].fields.title}}```{% endraw %}) aus dem Eingang-Endpunkt von Contentful verwenden und eine Antwort wie diese erhalten:

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
3\. Machen Sie eine Vorschau und testen Sie Ihre Kampagne, um sicherzustellen, dass die Connected-Content-Daten korrekt angezeigt werden.
4\. Wenn Sie mit der Einrichtung zufrieden sind, starten Sie Ihre Kampagne.

## Fehlersuche

### API-Antwort

Vergewissern Sie sich, dass Ihre Contentful API-Zugangsdaten und die URL des Endpunkts korrekt sind. Suchen Sie in Braze nach Fehlermeldungen, die auf Probleme mit dem API-Aufruf hinweisen könnten.

### Abbildung der Daten

Überprüfen Sie, ob die Abbildungen der Antwortpfade korrekt konfiguriert sind und ob die API-Antwortstruktur Ihren Erwartungen entspricht.

## Zusätzliche Ressourcen

- [Contentful Content Delivery API Dokumentation](https://www.contentful.com/developers/docs/references/content-delivery-api/)
- [Braze Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)
- [Braze Content-Blöcke]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
