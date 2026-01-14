---
nav_title: FAQ
article_title: Häufig gestellte Fragen
page_order: 12
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu Liquid."

---

# Häufig gestellte Fragen

> Auf dieser Seite finden Sie Antworten auf einige häufig gestellte Fragen zu Liquid.<br><br>Braze unterstützt derzeit nicht 100 % von Shopify's Liquid, sondern nur bestimmte Teile, die wir in unserer Dokumentation zu beschreiben versucht haben. Wir empfehlen dringend, alle Nachrichten mit Liquid zu testen, bevor Sie sie versenden, um das Risiko von Fehlern oder der Verwendung von nicht unterstütztem Liquid zu verringern.

### Wie verwende ich Liquid Snippets in Braze?

In vielen Fällen können Sie Liquid-Snippets einbinden, indem Sie zu Ihren Kampagnen oder Canvases navigieren und Liquid in das Personalisierungsmodal in Bereichen wie dem E-Mail-Text oder in Ihren Segmenten einfügen. 

#### Wo kann ich mehr erfahren?

Wenn Sie mehr über Liquid erfahren möchten, sehen Sie sich unseren geführten Lernangebote [zur dynamischen Personalisierung mit Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid) Braze an! Sie können sich auch in der [Bibliothek der Liquid-Anwendungsfälle]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/) inspirieren lassen und eine Reihe von Beispielen für die Personalisierung mit Liquid finden.

### Was ist der Unterschied zwischen der Verwendung von Liquid und Connected Content für die Personalisierung?

Braze Connected Content ist ein Beispiel für ein Liquid-Tag. Es wird auch für die Personalisierung verwendet, aber diese Daten stammen von einem externen Endpunkt und nicht von innerhalb von Braze gespeicherten Daten. In unserem speziellen Bereich für [verknüpfte Inhalte]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) erfahren Sie mehr darüber, wie Sie Ihre Nachrichten personalisieren können.

### Was ist Liquid Templating?

Dies ist die gängigste Art, Liquid in Braze zu verwenden. Beim Liquid Templating werden Daten aus dem Profil eines Benutzers in eine Nachricht gezogen. Diese Daten können vom Vornamen einer Nutzerin oder eines Nutzers bis zu angepassten Events aus einer durch ein Event getriggerten Nachricht reichen.

Unter [Unterstützte Personalisierungs-Tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) finden Sie eine vollständige Liste der unterstützten Liquid-Tags.

### Wie weise ich Variablen mit Liquid zu?

Sie können Variablen mit dem Tag `assign` erstellen und zuweisen. Dadurch wird eine Variable im Nachrichten-Editor erstellt, auf die Sie auch in Ihrer Nachricht referenzieren können.

### Werden mit Liquid Datenpunkte aufgezeichnet?

Nein.

### Wie kann ich Liquid verwenden, um einen personalisierten Gruß zu versenden?

Für eine personalisierte Begrüßung unter Verwendung des Vornamens einer Nutzerin oder eines Nutzers können Sie die Standardattribute des Nutzerprofils verwenden, z. B. {% raw %} `{{${first_name}}}`, `{{${last_name}}}`.

Sie können auch eine Liquid `{% if X %}` {% endraw %}Anweisung verwenden, um ein bedingtes Rendering auf der Grundlage beliebiger Daten durchzuführen, z. B. des Wochentags oder angepasster Attribute. Weitere Informationen zu den unterstützten Liquid-Operatoren, die in bedingten Anweisungen verwendet werden können, finden Sie unter [Operatoren]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/).

### Wie kann ich eine Nachricht basierend auf dem Standort eines Kunden personalisieren?

{% raw %}
Es gibt ein Standardattribut für den Standort des Benutzers: `{{${most_recent_location}}}`.

### Was ist der Unterschied zwischen {{campaign.${name}}} und {{campaign.${message_name}}}?

Sowohl `{{campaign.${name}}}` als auch `{{campaign.${message_name}}}` werden von Liquid Personalization Tags unterstützt. Beide Tags referenzieren Kampagnenattribute. `{{campaign.${name}}}` bezeichnet den Namen Ihrer Kampagne, und `{{campaign.${message_name}}}` ist der Name Ihrer Variante der Nachricht.
{% endraw %}

### Wie kann ich Liquid mit verschachtelten Objekten verwenden?

Braze verfügt über ein eingebautes Feature, das Liquid Code für Segmente generiert, die in einer Nachricht verwendet werden können. Genauer gesagt, können Sie ein Segment erstellen, das mehrere Kriterien in einem Objekt erfüllt.

Weitere Informationen finden Sie unter [Multikriterielle Segmentierung]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#multi-criteria-segmentation).

### Wie verwende ich Event-Attribute, um eine Nachricht zu personalisieren, die durch ein Event getriggert wurde?

{% raw %}
Mit dem Tag `api_triggered_property` können Sie auf Eigenschaften von API-getriggerten Events zugreifen: `{{api_trigger_properties.${attribute_key}}}`.  
{% endraw %}

### Was ist die Abbruchlogik, und wie kann ich sie verwenden?

Die Abbruchlogik ermöglicht es Ihnen, den Versand einer Nachricht zu stoppen, wenn die Bedingungen erfüllt sind. Dies ist besonders hilfreich, um zu verhindern, dass unvollständige Nachrichten an Ihre Nutzer:innen gesendet werden. Beispiele für die Abbruchlogik in Ihren Marketing Kampagnen finden Sie unter [Abbruch von Nachrichten]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/).

### Was ist die for-Schleifenlogik und wie kann ich sie verwenden?

For-Schleifen werden auch als [Iterations-Tags](https://shopify.github.io/liquid/tags/iteration/) bezeichnet. Die Verwendung der for-Schleifenlogik in Ihren Liquid Snippets erlaubt es Ihnen, Liquid-Blöcke zu durchlaufen, bis eine Bedingung erfüllt ist. 

In Braze könnte dies für die Überprüfung von Artikeln in einem angepassten Attribut oder einer Liste von Werten und Objekten verwendet werden, die von einer [Katalog-]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs), [Auswahl-]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) oder [Connected-Content-Aufrufantwort]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) zurückgegeben werden. Insbesondere können Sie die For-Loop-Logik als Teil Ihres Messagings verwenden, um zu prüfen, ob ein Produkt auf Lager ist oder ob ein Produkt eine Mindestbewertung hat. 

Nehmen wir an, Sie haben einen Katalog mit dem Namen "Spiele", der eine Auswahl mit dem Namen "cheap_games". enthält. Um die Titel der Spiele in "cheap_games", zu finden, können Sie dieses Liquid Snippet verwenden:

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Sobald die festgelegten Bedingungen erfüllt sind, kann Ihre Nachricht fortgesetzt werden. Die Verwendung dieser Logik ist eine hilfreiche Methode, um Zeit zu sparen, anstatt Liquid-Blöcke für verschiedene Bedingungen zu wiederholen.
