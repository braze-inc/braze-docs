---
nav_title: Nutzer:innen Produkte empfehlen
article_title: Nutzer:innen Produkte empfehlen
page_order: 4
page_type: reference
description: "Dieser Referenzartikel zeigt Ihnen, wie Sie die Braze REST API, Kataloge und Connected-Content nutzen, um Nutzer:innen über verschiedene Messaging-Kanäle personalisierte Produktempfehlungen anzuzeigen."
---

# Nutzer:innen Produkte empfehlen

> Nutzen Sie die Braze REST API zusammen mit [Katalogen]({{site.baseurl}}/user_guide/data/activation/catalogs/create/) oder [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), um personalisierte Produktempfehlungen in Ihren Nachrichten anzuzeigen. Mit diesem Ansatz können Sie Ihr eigenes Empfehlungssystem in das Braze-Messaging-Ökosystem einbinden, sodass nicht-technische Nutzer:innen den Inhalt und die Nachrichten rund um jede Empfehlung eigenständig verwalten können.

Mit diesem Ansatz können Sie:

- Produktempfehlungen aus Ihrem Backend über die REST API in Nutzerprofilen speichern.
- Produkt-Metadaten zum Sendezeitpunkt über Kataloge oder Connected-Content abrufen.
- Personalisierte Empfehlungen über jeden Messaging-Kanal anzeigen, einschließlich E-Mail, Push, In-App-Nachrichten und mehr.

## Voraussetzungen

Um diese Anleitung abzuschließen, benötigen Sie:

| Anforderung | Beschreibung |
| --- | --- |
| Braze REST-API-Schlüssel | Einen Schlüssel mit der Berechtigung `users.track` und, falls Sie Kataloge über die API verwalten, den entsprechenden Katalog-Berechtigungen. Um einen zu erstellen, gehen Sie zu **Einstellungen** > **API-Schlüssel**. |
| Braze-Katalog | Einen Katalog mit Ihren Produkt-Metadaten (wie Name, Kategorie, Preis und Bild-URL). Informationen zur Erstellung finden Sie unter [Katalog erstellen]({{site.baseurl}}/user_guide/data/activation/catalogs/create/). |
| Liquid-Kenntnisse | Mittlere Vertrautheit mit [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) für das Templating personalisierter Variablen und die Nutzung von Connected-Content. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 1. Schritt: Empfehlungen in Nutzerprofilen speichern

Speichern Sie zunächst die von Ihrem Empfehlungssystem generierten Produktempfehlungen als angepasste Attribute in Braze-Nutzerprofilen. So können Sie die empfohlenen Produkte jedes Nutzers bzw. jeder Nutzerin zum Sendezeitpunkt der Nachricht referenzieren.

1. Legen Sie fest, welche Empfehlungsdaten gespeichert werden sollen, z. B. Produkt-IDs oder bevorzugte Kategorien.
2. Verwenden Sie den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)-Endpunkt, um die Empfehlung als angepasstes Attribut im Nutzerprofil zu speichern.

### Beispielanfrage

```http
POST YOUR_REST_ENDPOINT/users/track
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Ersetzen Sie `YOUR_REST_ENDPOINT` durch die [REST-Endpunkt-URL]({{site.baseurl}}/api/basics/#endpoints) für Ihren Workspace.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "recommended_product_id": "1001"
    }
  ]
}
```

Verwenden Sie aussagekräftige Attributnamen (wie `recommended_product_id`), damit sie sich später in Liquid-Templates leicht referenzieren lassen. Halten Sie die Empfehlungen aktuell, indem Sie sie regelmäßig aktualisieren, sobald Ihr Empfehlungssystem neue Ergebnisse liefert.

## 2. Schritt: Produkt-Metadaten abrufen

Nachdem Sie einen Empfehlungsbezeichner in jedem Nutzerprofil gespeichert haben, müssen Sie die vollständigen Produkt-Metadaten (Name, Preis, Bild usw.) abrufen, um sie in Ihre Nachricht einzubinden. Dafür stehen Ihnen zwei Optionen zur Verfügung:

- **Option A:** [Braze-Kataloge](#option-a-braze-catalogs) — Produktinformationen direkt in Braze speichern für schnelle, integrierte Abfragen.
- **Option B:** [Connected-Content](#option-b-connected-content) — Produktinformationen zum Sendezeitpunkt von einer externen API abrufen.

### Option A: Braze-Kataloge

Wenn Sie einen [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs/create/) mit Ihrem Produktbestand erstellt haben, können Sie Artikel direkt in Ihrer Nachricht per Liquid nachschlagen. Eine vollständige Anleitung finden Sie unter [Kataloge verwenden]({{site.baseurl}}/user_guide/data/activation/catalogs/use/).

#### Einen bestimmten Katalogartikel empfehlen

{% raw %}
Um ein bestimmtes Produkt anhand seiner ID zu referenzieren, verwenden Sie den Liquid-Tag `catalog_items`. Um beispielsweise Produkt `1001` aus einem Katalog namens `retail_products` zu empfehlen:

```liquid
{% catalog_items retail_products 1001 %}

We have a new item we think you'll like:
Category: {{ items[0].category }}
Name: {{ items[0].name }}
Price: ${{ items[0].price }}
```
{% endraw %}

#### Mehrere Katalogartikel empfehlen

{% raw %}
Sie können auch mehrere Artikel in einem einzigen Tag referenzieren. Um beispielsweise drei Produkte hervorzuheben:

```liquid
{% catalog_items retail_products 1001 1003 1005 %}

New items added in:
- {{ items[0].category }}
- {{ items[1].category }}
- {{ items[2].category }}

Visit our store to learn more!
```
{% endraw %}

#### Artikel mithilfe der Empfehlung eines Nutzers bzw. einer Nutzerin templaten

{% raw %}
Kombinieren Sie das angepasste Attribut aus [1. Schritt](#step-1-store-recommendations-on-user-profiles) mit einer Katalogabfrage, um die Empfehlung für jeden Nutzer bzw. jede Nutzerin zu personalisieren:

```liquid
{% catalog_items retail_products {{custom_attribute.${recommended_product_id}}} %}

Hi {{${first_name}}}, check out our pick for you:
{{ items[0].name }} — ${{ items[0].price }}
```
{% endraw %}

### Option B: Connected-Content

Wenn Ihre Produkt-Metadaten in einem externen Dienst statt in einem Braze-Katalog gespeichert sind, verwenden Sie [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/), um sie zum Sendezeitpunkt abzurufen.

{% raw %}
Wenn Ihre interne API beispielsweise Produktdetails anhand der ID zurückgibt:

```liquid
{% connected_content https://api.yourcompany.com/products/{{custom_attribute.${recommended_product_id}}} :save product %}

Hi {{${first_name}}}, we think you'll love:
{{ product.name }} — ${{ product.price }}
```
{% endraw %}

Weitere Informationen zum Ausführen von API-Aufrufen aus Ihren Nachrichten finden Sie unter [Einen API-Aufruf durchführen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/).

{% alert warning %}
Vermeiden Sie es, Connected-Content zu verwenden, um eine große Liste von Produkten abzurufen und diese dann zum Sendezeitpunkt in Liquid zu durchlaufen. Große Antwort-Payloads erhöhen die Sendelatenz und können bei großem Volumen zu Nachrichten-Timeouts oder Zustellungsfehlern führen. Speichern Sie stattdessen nur die spezifischen Produkt-IDs, die ein Nutzer bzw. eine Nutzerin benötigt, in deren Profil (siehe [1. Schritt](#step-1-store-recommendations-on-user-profiles)) und rufen Sie Metadaten für diese einzelnen Artikel ab oder verwenden Sie [Kataloge](#option-a-braze-catalogs), die für schnelle Abfragen optimiert sind.
{% endalert %}

## 3. Schritt: Integration überprüfen

Überprüfen Sie nach Abschluss der Einrichtung Ihre Integration:

1. Verwenden Sie den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)-Endpunkt, um eine Testempfehlung in Ihr eigenes Nutzerprofil zu schreiben.
2. Senden Sie eine Testnachricht, die das empfohlene Produkt über Kataloge oder Connected-Content referenziert.
3. Bestätigen Sie, dass die Produktdetails in der zugestellten Nachricht korrekt dargestellt werden.
4. Gehen Sie im Braze-Dashboard zur Ergebnisseite der Kampagne oder des Canvas und bestätigen Sie, dass der Versand aufgezeichnet wurde.

## Hinweise

- Halten Sie die Empfehlungsdaten aktuell, indem Sie angepasste Attribute regelmäßig aktualisieren, sobald Ihr Empfehlungssystem neue Ergebnisse liefert.
- Nutzen Sie die [Personalisierungsfunktionen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) von Braze, um Nachrichten weiter anzupassen, z. B. durch die Einbindung nutzerspezifischer Daten neben Produktdetails.
- Erwägen Sie die Verwendung von [API-getriggerter Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/), um Nachrichten aus Ihrem Backend mithilfe von im Braze-Dashboard definierten Templates zu triggern.