---
nav_title: Swym
article_title: Swym
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Swym, die es den Käufern ermöglicht, Produkte zu speichern und nahtlos über Websites, mobile Apps und Shops weiter zu reisen."
alias: /partners/swym/
page_type: partner
search_tag: Partner
---

# Swym

> [Swym](https://getswym.com/) unterstützt E-Commerce-Marken bei der Erfassung von Kaufabsichten mit Wunschlisten, Speichern für später, Geschenkelisten und Back-in-Stock-Warnungen. Mithilfe umfangreicher Daten, die auf Berechtigungen basieren, können Sie zielgerichtete Kampagnen erstellen und personalisierte Einkaufserlebnisse bieten, die das Engagement fördern, die Konversion steigern und die Loyalität erhöhen.

*Diese Integration wird von Swym gepflegt.*

## Über die Integration

Die Integration von Swym und Braze ermöglicht es Ihnen, personalisierte, ereignisgesteuerte Kampagnen zuzustellen, die die Absichten der Kunden in Verkäufe umwandeln. Nutzen Sie die Integration, damit die Kunden dort weitermachen können, wo sie aufgehört haben, mit anderen während ihrer Einkaufsreise zusammenarbeiten und leistungsstarke Retargeting Kampagnen erhalten.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung          | Beschreibung                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Swym  | Die Apps Swym Wishlist Plus, Back in Stock oder beide müssen auf Ihrer E-Commerce-Plattform (Shopify oder BigCommerce) installiert sein, und Sie müssen den Enterprise-Tarif nutzen.       |
| Ein Braze REST API-Schlüssel  | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Ein Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Anwendungsfälle

Indem Sie die Apps Wishlist Plus und Back in Stock Alerts von Swym mit Braze verbinden, können Sie automatisch Ereignisse für Kundenaktivitäten, wie z.B. Hinzufügungen zur Wunschliste, Back-in-Stock-Abos, Preissenkungswarnungen und Erinnerungen, als angepasste Events an Braze senden. Diese Ereignisse können dann verwendet werden, um automatisierte Nachrichten in Braze zu triggern und so eine zeitnahe, relevante und ansprechende Kommunikation zu ermöglichen, die den Kunden zum Kauf zurückbringt.

## Integration von Swym

### Schritt 1: Verbinden Sie Ihre Swym App mit Braze

Derzeit ist die Braze-Integration mit Swym eine verwaltete Integration und nicht zur Selbstbedienung geeignet. Wenden Sie sich an das Swym Support Team unter [support@getswym.com](mailto:support@getswym.com) und geben Sie die folgenden Informationen an, damit Swym die Integration in Ihrem Namen einrichten kann:

1. Erzeugen Sie einen [REST API-Schlüssel]({{site.baseurl}}/api/basics/#about-rest-api-keys) in Ihrem Braze-Dashboard mit der Berechtigung `users.track`.

![Generierung eines API-Schlüssels in Braze.]({% image_buster /assets/img/swym/braze-api-key.png %})

{% alert important %}
Um Ihre API-Schlüssel zu schützen, empfiehlt Swym die sichere Weitergabe von Zugangsdaten mit einem einmaligen, selbstzerstörenden Link-Tool (z.B. [OneTimeSecret](https://onetimesecret.com/)).
{% endalert %}

{: start="2"}
2\. Braze verwaltet mehrere Instanzen für sein Dashboard und seine REST-Endpunkte. Geben Sie den [REST-Endpunkt]({{site.baseurl}}/api/basics/#endpoints) für die Instanz an, die Sie bereitstellen.

3. Nachdem Sie den API-Schlüssel und die Instanz-URL an das Swym Support Team weitergegeben haben, wird dieses die Integration für Sie einrichten und Ihnen eine Bestätigung schicken.

4. Nachdem die Einrichtung abgeschlossen ist, werden die angepassten Events von Swym automatisch in Braze registriert. Sie können die Liste der registrierten Swym Events im Braze-Dashboard einsehen, indem Sie zu **Dateneinstellungen** > Angepasste Events gehen. 

5. Zeigen Sie die Eigenschaften der einzelnen Swym Events an, indem Sie **Eigenschaften** für das entsprechende angepasste Event auswählen. Diese Eigenschaften enthalten die Event-Eigenschaften, die zur Personalisierung Ihrer Nachrichten verwendet werden können.

![Angepasste Eigenschaften in Braze.]({% image_buster /assets/img/swym/braze-custom-properties.png %})

### Schritt 2: Abonnieren Sie die Ereignisse, die Sie an Braze senden möchten

Gehen Sie in Ihrer Wishlist Plus App auf den Tab **Marketing** und suchen Sie den Bereich **Automatisierungen**. Hier können Sie die Ereignisse auswählen, die Sie abonnieren möchten. 

![Ereignisse, die abonniert werden sollen.]({% image_buster /assets/img/swym/braze-event-subscription.png %})

#### Swym Wishlist Plus App Ereignisse

| Event-Name | Wenn dieses Ereignis getriggert wird |  
|------------|------------------------------|  
| Wunschzettel teilen | Wenn ein Käufer eine Wunschliste mit jemandem teilt |  
| Zum Wunschzettel hinzufügen | Wenn ein Käufer einen Artikel zu seiner Wunschliste hinzufügt |  
| Wunschzettel-Erinnerung | Erinnerung an Artikel auf dem Wunschzettel eines Käufers|   
| Für später speichern Erinnerung | Erinnerung an die für später gespeicherten Artikel eines Käufers |  
| Preissenkungsalarm | Produkt auf einer Wunschliste geht in den Verkauf |  
| Alarm bei niedrigem Lagerbestand | Das Produkt auf der Wunschliste ist nicht mehr vorrätig |  
| Wieder auf Lager Alarm | Produkt auf der Wunschliste ist wieder auf Lager |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Swym Back in Stock Alerts App Ereignisse

| Event-Name | Wenn dieses Ereignis getriggert wird |  
|------------|------------------------------|  
| Wieder vorrätig-Bestätigung | Shopper abonniert, um benachrichtigt zu werden, wenn ein Produkt wieder auf Lager ist |  
| Wiederauffüllungs-Alarm | Das Produkt, für das ein Käufer eine Vorratswarnmeldung angefordert hat, ist wieder auf Lager |  
| Erinnerung an die Wiederauffüllung | Folgewarnung (in der Regel ca. 24 Stunden nach der ersten Wiederauffüllungswarnung, konfigurierbar)|   
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Schritt 3: Erstellen Sie eine Braze-Kampagne oder ein Braze-Canvas

Um die Zustellung personalisierter Nachrichten für Ihre Kunden zu automatisieren, müssen Sie in Braze für jede Veranstaltung, die Sie abonniert haben, eine eigene Kampagne oder ein eigenes Canvas erstellen. Jede Kampagne oder jedes Canvas sollte so konfiguriert werden, dass sie/es auf der Grundlage eines bestimmten Ereignisses ausgelöst wird und die entsprechenden Event-Eigenschaften verwendet, um dynamische Inhalte in Ihre Nachrichten einzufügen. Eine schrittweise Anleitung finden Sie unter [Erste Schritte: Kampagnen und Leinwände]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases/).

![Ein handlungsorientiertes Ereignis.]({% image_buster /assets/img/swym/braze-canvas-setup.png %})

Weitere Einzelheiten finden Sie im [Swym-Hilfecenter](https://help.getswym.com/en/articles/12344153-braze-integration) oder kontaktieren Sie das Swym-Supportteam unter [support@getswym.com](mailto:support@getswym.com). 