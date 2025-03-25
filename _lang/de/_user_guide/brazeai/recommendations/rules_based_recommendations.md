---
nav_title: Regelbasierte Empfehlungen
article_title: Regelbasierte Empfehlungen
page_type: tutorial
page_order: 16
alias: "/rules_based_recommendations/"
description: "Dieser Artikel beschreibt, wie Sie ein regelbasiertes Empfehlungssystem erstellen, das Kataloge oder Connected-Content verwendet."
tool:
  - Campaigns
  - Canvas

---

# Regelbasierte Empfehlungen

> Eine regelbasierte Empfehlungsmaschine verwendet Benutzerdaten und Produktinformationen, um dem Benutzer relevante Artikel in den Nachrichten vorzuschlagen. Es verwendet [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) und entweder [Braze-Kataloge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) oder [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), um Inhalte auf der Grundlage von Benutzerverhalten und -attributen dynamisch zu personalisieren.

Wenn Sie mehr über Liquid, Kataloge und Connected-Content erfahren möchten, sehen Sie sich diese Braze-Lernkurse an:

- [Personalisierte Empfehlungen per E-Mail](https://learning.braze.com/personalized-recommendations-with-email)
- [Dynamische Personalisierung mit Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid)
- [Connected-Content-Grundlagen](https://learning.braze.com/path/dynamic-personalization-with-liquid/connected-content-fundamentals)

{% alert important %}
Regelbasierte Empfehlungen basieren auf einer festen Logik, die Sie manuell einstellen müssen. Das bedeutet, dass sich Ihre Empfehlungen nicht an die Kaufhistorie und den Geschmack eines Nutzers anpassen, wenn Sie die Logik nicht aktualisieren.<br><br>Um personalisierte KI-Empfehlungen zu erstellen, die sich automatisch an den Verlauf eines Nutzers:innen anpassen, sehen Sie sich [KI-Artikel-Empfehlungen]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/) an.
{% endalert %}

## Erstellen einer Katalog-Empfehlungsmaschine

1. [Erstellen Sie einen Katalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/) mit Produkten.
2. Fügen Sie für jedes Produkt eine Liste der empfohlenen Produkte als String, getrennt durch ein Trennzeichen (z. B. eine Pipe `|`), in eine Spalte namens „product_recommendations“ ein.
3. Übergeben Sie dem Katalog die ID des Produkts, für das Sie Empfehlungen finden möchten.
4. Rufen Sie den Wert `product_recommendations` für diesen Katalogartikel ab und teilen Sie ihn durch das Trennzeichen mit einem Liquid-Split-Filter auf.
5. Geben Sie eine oder mehrere dieser IDs an den Katalog zurück, um die anderen Produktdetails zu erfassen.

### Anwendungsfall „Kataloge“

Nehmen wir an, Sie haben eine App für gesunde Ernährung und möchten eine Content-Card-Kampagne erstellen, die verschiedene Rezepte versendet, je nachdem, wie lange ein Nutzer bereits bei Ihrer App angemeldet ist. 

1. Erstellen und laden Sie einen Katalog per CSV hoch, der die folgenden Informationen enthält:<br>- **id:** Eine eindeutige Zahl, die mit der Anzahl der Tage seit der Anmeldung des Benutzers bei Ihrer App korreliert. Zum Beispiel entspricht `3` drei Tagen.<br>- **Typ:** Die Rezeptkategorie, wie `comfort`, `fresh`, und andere.<br>- **Titel:** Der Titel der Content-Card, die für jede ID verschickt wird, z. B. „Bereiten Sie diese Woche das Mittagessen vor“ oder „Lassen Sie uns Tacos machen“.<br>- **Link:** Der Link zum Rezeptartikel.<br>- **image_url:** Das Bild, das dem Rezept entspricht.

{: start="2"}
2\. Nachdem der Katalog in Braze hochgeladen wurde, überprüfen Sie die Vorschau einer ausgewählten Anzahl von Katalogartikeln, um die Richtigkeit der importierten Informationen zu bestätigen. Die Artikel können in der Vorschau zufällig angeordnet sein, aber das hat keinen Einfluss auf die Ausgabe des Empfehlungssystems.

![][1]

{: start="3"}
3\. Erstellen Sie eine Content Card Kampagne. Geben Sie im Composer die Liquid-Logik ein, um zu bestimmen, welche Benutzer die Kampagne erhalten sollen und welches Rezept und welches Bild angezeigt werden soll. In diesem Anwendungsfall zieht Braze die `start_date` (oder das Datum der Registrierung) des Nutzers:innen und vergleicht sie mit dem aktuellen Datum. Die Differenz in Tagen bestimmt, welche Inhaltskarte gesendet wird. 

![][2]

**Titel:**

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].title }}
```
{% endraw %}

**Nachricht:**

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{% if items[0].title != blank %}
{{ items[0].body }}
{% else %}
{% abort_message('no card for today') %}
{% endif %}
```
{% endraw %}

**Bild:**

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].image_url }}
```
{% endraw %}

{: start="4"}
4\. Geben Sie im Abschnitt **Bei Klick-Verhalten** die Liquid-Logik ein, wohin Benutzer weitergeleitet werden sollen, wenn sie auf iOS-, Android- und Web-Geräten auf die Content Card klicken. 

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].link }}
```
{% endraw %}

![][3]{: style="max-width:60%;"}<br><br>

{: start="5"}
5\. Gehen Sie auf die Registerkarte **Test** und wählen Sie **Benutzerdefiniert** unter **Vorschau der Nachricht als Benutzer**. Geben Sie ein Datum in das Feld **Benutzerdefiniertes Attribut** ein, um eine Vorschau der Inhaltskarte zu erhalten, die an einen Benutzer gesendet wird, der sich an diesem Datum angemeldet hat. <br><br>

![][4]

## Erstellen eines Connected-Content-Empfehlungssystems

1. Erstellen Sie einen Connected-Content-Endpunkt auf eine der folgenden Arten:
- Konvertieren Sie eine Kalkulationstabelle in einen JSON-API-Endpunkt, indem Sie einen Dienst wie SheetDP verwenden, und notieren Sie sich die API-URL, die dadurch erzeugt wird
- Erstellen, hosten und pflegen Sie einen speziell entwickelten internen Endpunkt
- Kaufen Sie eine Empfehlungsmaschine über einen Drittanbieter, z. B. einen unserer [Alloy-Partner]({{site.baseurl}}/partners/message_personalization/dynamic_content/), einschließlich [Amazon Personalise]({{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/), [Certona]({{site.baseurl}}/partners/message_personalization/dynamic_content/certona/), [Dynamic Yield]({{site.baseurl}}/partners/message_personalization/dynamic_content/dynamic_yield/) und andere.

2. Schreiben Sie Connected Content Liquid in den Nachrichtentext oder in den HTML-Editor des Inhaltsblocks, der Ihren Endpunkt aufruft, um Ihre Datenbank zu durchsuchen.
3. Richten Sie das Liquid an einem benutzerdefinierten Attributwert aus, den es im Profil eines bestimmten Benutzers findet.
4. Ziehen Sie daraufhin die richtige Empfehlung.

{% raw %}
```
{% connected_content YOUR-API-URL :save items %}

{% assign recommended_item_ids_from_user_profile = custom_attribute.${RECOMMENDED_ITEM_IDS} | split: ';' %}

{% for item_id in recommended_item_ids_from_user_profile %}
  {% assign recommended_item = items | where: "ITEM_ID", ITEM_ID | first %}
  recommended_item.item_name
{% endfor %}
```
{% endraw %}

| Attribut | Ersatz |
| --- | --- |
|`YOUR-API-URL` | Ersetzen Sie durch die tatsächliche URL Ihrer API. |
|`RECOMMENDED_ITEM_IDS` | Ersetzen Sie durch den tatsächlichen Namen Ihres benutzerdefinierten Attributs, das die IDs der empfohlenen Artikel enthält. Dieses Attribut wird als eine durch Semikolon getrennte Kette von IDs erwartet. |
|`ITEM_ID` | Ersetzen Sie durch den tatsächlichen Namen des Attributs in Ihrer API-Antwort, das der ID des Artikels entspricht. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Dies ist ein einfaches Beispiel, das Sie je nach Ihren spezifischen Bedürfnissen und Ihrer Datenstruktur möglicherweise weiter anpassen müssen. Ausführlichere Anleitungen finden Sie in der [Liquid-Dokumentation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) oder wenden Sie sich an einen Entwickler.
{% endalert %}

## Connected-Content-Anwendungsfall

Nehmen wir an, Sie möchten Restaurantempfehlungen aus der Zomato Restaurants-Datenbank abrufen und das Ergebnis als lokale Variable namens `restaurants` speichern. Sie können den folgenden Connected-Content-Aufruf tätigen:

{% raw %}
```liquid

{% connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

Nehmen wir als nächstes an, Sie möchten Restaurantempfehlungen auf der Grundlage der Stadt und der Art des Essens eines Benutzers abrufen. Sie können dies tun, indem Sie die angepassten Attribute für den Ort des Nutzers oder der Nutzerin und die Art des Essens dynamisch am Anfang des Aufrufs einfügen und dann den Wert von `restaurants` der Variablen `city_food.restaurants` zuweisen.

Der Aufruf von Connected Content würde wie folgt aussehen:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

Wenn Sie die Antwort so anpassen möchten, dass nur der Name und die Bewertung des Restaurants abgerufen werden, können Sie am Ende des Aufrufs Filter hinzufügen, etwa so:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0].restaurant.name}}
{{city_food.restaurants[0].restaurant.user_rating.rating_text}}
```
{% endraw %}

Nehmen wir an, Sie möchten die Restaurantempfehlungen nach Bewertung gruppieren. Gehen Sie wie folgt vor:

1. Verwenden Sie `assign`, um leere Felder für die Bewertungskategorien „ausgezeichnet“, „sehr gut“ und „gut“ zu erstellen.
2. Fügen Sie eine `for` Schleife hinzu, die die Bewertungen der einzelnen Restaurants in der Liste untersucht. 
- Wenn eine Bewertung „Ausgezeichnet“ lautet, fügen Sie den Namen des Restaurants an den String `excellent_restaurants` an und fügen Sie dann am Ende ein *-Zeichen hinzu, um die einzelnen Restaurantnamen voneinander zu trennen. 
- Wenn eine Bewertung „Sehr gut“ lautet, fügen Sie den Namen des Restaurants an den String `very_good_restaurants` an und fügen Sie dann am Ende ein *-Zeichen hinzu.
- Wenn eine Bewertung „Gut“ lautet, fügen Sie den Namen des Restaurants an den String `good_restaurants` an und fügen Sie dann am Ende ein *-Zeichen hinzu.
3. Begrenzen Sie die Anzahl der zurückgegebenen Restaurantempfehlungen auf vier pro Kategorie.

So würde der endgültige Anruf aussehen:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}
{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}
{% assign excellent_restaurants = “” %}
{% assign very_good_resturants = “” %}
{% assign good_restaurants = “” %}
{% for list in restaurants %}
{% if {{list.restaurant.user_rating.rating_text}} == `Excellent` %}
{% assign excellent_restaurants = excellent_restaurants | append: list.restaurant.name | append: `*` %}
{% elseif {{list.restaurant.user_rating.rating_text}} == `Very Good` %}
{% assign very_good_restaurants = very_good_restaurants | append: list.restaurant.name | append: `*` %}
{% elseif {{list.restaurant.user_rating.rating_text}} == `Good` %}
{% assign good_restaurants = good_restaurants | append: list.restaurant.name | append: `*` %}
{% endif %}
{% endfor %}
{% assign excellent_array = excellent_restaurants | split: `*` %}
{% assign very_good_array = very_good_restaurants | split: `*` %}
{% assign good_array = good_restaurants | split: `*` %}

Excellent places
{% for list in excellent_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Very good places
{% for list in very_good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Good places
{% for list in good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}
```
{% endraw %}

Im folgenden Screenshot sehen Sie ein Beispiel dafür, wie die Antwort auf dem Gerät eines Benutzers angezeigt wird.

![][5]{: style="max-width:30%;"}

## Überlegungen

Bei der Entscheidung, welches Empfehlungssystem zu Ihren verfügbaren Ressourcen und Anwendungsfällen passt, sollten Sie sich an dieser Tabelle orientieren:

| Überlegungen | Liquid | Kataloge CSV | Kataloge API | Connected-Content |
| --- | --- | --- | --- | --- |
| Verbraucht keine Datenpunkte | Nicht unterstützt | Unterstützt | Unterstützt | Unterstützt |
| Keine Code-Lösung | Nicht unterstützt | Unterstützt, wenn vorgeneriert Liquid | Nicht unterstützt | Nicht unterstützt |
| Erweitertes Liquid oft erforderlich | Unterstützt | Nicht unterstützt | Nicht unterstützt | Unterstützt |
| Aktualisierungen der Daten im Produkt-Feed | Nicht unterstützt | Unterstützt, wenn die Empfehlungen nicht oft aktualisiert werden | Unterstützt, wenn Empfehlungen bis zu stündlich aktualisiert werden | Unterstützt und Empfehlungen werden in Echtzeit aktualisiert |
| Generieren Sie Empfehlungen innerhalb der Braze UI | Unterstützt | Unterstützt | Unterstützt | Nicht unterstützt, wenn außerhalb von Braze erstellt |
| Kein Hosting, keine Verwaltung, keine Fehlerbehebung von Empfehlungen Daten | Unterstützt | Unterstützt | Unterstützt | Nicht unterstützt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

[1]: {% image_buster /assets/img/recs/catalog_items.png %}
[2]: {% image_buster /assets/img/recs/content_card_preview.png %}
[3]: {% image_buster /assets/img/recs/on_click_behavior.png %}
[4]: {% image_buster /assets/img/recs/custom_attributes_test.png %}
[5]: {% image_buster /assets/img/recs/sample_response.png %}