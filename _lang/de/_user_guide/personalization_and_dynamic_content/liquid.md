---
nav_title: Liquid
article_title: Liquid
page_order: 0
layout: dev_guide
alias: /liquid/
search_rank: 3
guide_top_header: "Personalisierung mit Liquid Tags"
guide_top_text: "Braze kann automatisch Werte eines bestimmten Benutzers in Ihren Nachrichten ersetzen. Setzen Sie Ihren Ausdruck in zwei Gruppen von geschweiften Klammern, um Braze mitzuteilen, dass Sie einen interpolierten Wert verwenden. Innerhalb dieser Klammern müssen alle Benutzerwerte, die Sie ersetzen möchten, von einem zusätzlichen Satz von Klammern mit einem vorangestellten Dollarzeichen umgeben sein.<br><br>Weitere Informationen zu Liquid finden Sie im Leitfaden <b><a href='https://learning.braze.com/path/dynamic-personalization-with-liquid'>Dynamische Personalisierung mit Liquid</a></b>."
description: "Auf dieser Landing Page erfahren Sie alles über Liquid, wie z.B. unterstützte Personalisierungs-Tags, Filter, die Einstellung von Standardwerten und mehr."

guide_featured_title: "Artikel im Abschnitt"
guide_featured_list:
- name: Liquid verwenden
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/using_liquid/
  image: /assets/img/braze_icons/beaker-02.svg
- name: Unterstützte Personalisierungs-Tags
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
  image: /assets/img/braze_icons/tag-01.svg
- name: Operatoren
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/operators/
  image: /assets/img/braze_icons/code-02.svg
- name: Filter
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/filters/
  image: /assets/img/braze_icons/flag-02.svg
- name: Erweiterte Filter
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/
  image: /assets/img/braze_icons/settings-01.svg
- name: Standardwerte einstellen
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
  image: /assets/img/braze_icons/table.svg
- name: Logik für bedingte Nachrichten
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
  image: /assets/img/braze_icons/columns-01.svg
- name: Nachrichten abbrechen
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Liquid-Anwendungsbeispiele
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/
  image: /assets/img/braze_icons/list.svg
- name: Tutorials
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/tutorials/
  image: /assets/img/braze_icons/book-open-01.svg
- name: Häufig gestellte Fragen
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/faq/
  image: /assets/img/braze_icons/annotation-question.svg
  
---

## Liquid

> Liquid ist eine quelloffene Maskensprache, die von Shopify entwickelt und in Ruby geschrieben wurde. Bei Braze wird Liquid verwendet, um Benutzerprofildaten in Nachrichten zu übertragen. 

Sie können zum Beispiel ein benutzerdefiniertes Attribut aus einem Benutzerprofil abrufen, das einen ganzzahligen Datentyp hat, und diesen Wert auf die nächste ganze Zahl runden. Weitere Informationen zur Syntax und Verwendung von Liquid finden Sie unter [**Unterstützte Personalisierungs-Tags**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Liquid unterstützt Objekte, Tags und Filter.

- Mit [**Objekten**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) können Sie personalisierte Attribute in Ihre Nachrichten einfügen.
- [**Tags**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) ermöglichen es Ihnen, Daten in Nachrichten einzufügen und eine bedingte Logik zu verwenden, um Nachrichten zu senden, wenn bestimmte Bedingungen erfüllt sind. Sie können zum Beispiel Tags verwenden, um intelligente Logiken wie "if"-Anweisungen in Ihre Kampagnen einzubauen.
- Mit [**Filtern**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) können Sie personalisierte Attribute und dynamische Inhalte umformatieren. Sie könnten zum Beispiel den [Filter`date` ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#date-filter) verwenden, um einen Zeitstempel wie *2016-09-07 08:43:50 UTC* in ein Datum wie den *7. September 2016* umzuwandeln.

{% alert warning %}
Braze unterstützt Liquid von Shopify derzeit nicht komplett, sondern nur diejenigen Bestandteile, die in der Dokumentation beschrieben werden. Wir empfehlen dringend, alle Nachrichten mit Liquid zu testen, bevor Sie sie versenden, um das Risiko von Fehlern oder der Verwendung von nicht unterstütztem Liquid zu verringern.
{% endalert %}

### Unterstützung bis Liquid 5

Braze unterstützt Liquid bis einschließlich **Liquid 5 von Shopify**. Die Liquid-Implementierung unterstützt Tag-Typen für Syntaxpersonalisierung und Leerzeichenkontrolle. Weitere Informationen zu bestimmten Tags finden Sie unter [Syntax-Tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#syntax-tags).

Die folgenden neuen Array- und mathematischen Filter können Sie bei der Nachrichtenerstellung in Ihrem Liquid verwenden.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

Siehe [Filter]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) für Definitionen.

### Flüssige Updates

#### Farbige Beschriftung

Jedes Liquid-Element entspricht einer Farbe, sodass Sie im Liquid-Editor sofort den Überblick haben.

![]({% image_buster /assets/img/liquid_color_code.png %})

#### Vorausschauende Liquids

Sie können auch vorausschauende Liquids für benutzerdefinierte Attribute, Attributnamen etc. nutzen, wenn Sie personalisierte Nachrichten erstellen.

![]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## Begriffe, die Sie kennen sollten

Diese Begriffe sind eine Neuinterpretation aus der [**Dokumentation von Shopify**](https://shopify.github.io/liquid/basics/introduction/) basierend auf unserem Support-Level.

{% raw %}

| Begriff | Definition | Beispiel |  
|---|---|---|
| Liquid | Eine häufig verwendete, kundenorientierte Vorlagensprache, die von Shopify entwickelt und in Ruby geschrieben wurde und zum Laden und Abrufen dynamischer Inhalte verwendet wird. | `{{${first_name}}}` fügt den Vornamen eines Benutzers in eine Nachricht ein. |
| Objekt | Eine Bezeichnung für eine Variable und die Position des vorgesehenen Variablennamens, die Liquid mitteilt, wo der Inhalt in der Nachricht angezeigt werden soll. | `{{${city}}}` fügt die Stadt eines Benutzers in eine Nachricht ein. |
| Tag mit bedingter Logik | Wird verwendet, um Logik zu erstellen und den Fluss des Nachrichteninhalts zu steuern. In Braze werden Tags mit bedingter Logik für Ausnahmen und Nachrichtenvarianten verwendet, die auf bestimmten vorgegebenen Kriterien basieren. | ```{% if ${language} == 'en' %}``` löst Nachrichten auf eine bestimmte Art und Weise aus, wenn ein Benutzer als Sprache "Englisch" angegeben hat. |
| Filter | Wird verwendet, um die Ausgabe des Liquid-Objekts zu ändern, einzuschränken oder neu zu formatieren. Eignet sich auch zur Erstellung mathematischer Operationen | ```{{"Big Sale" | upcase}}``` bewirkt, dass die Zeichenfolge "Big Sale" in der Nachricht als "BIG SALE" erscheint. |
| Operatoren | Wird in Nachrichten verwendet, um Abhängigkeiten oder Kriterien zu erstellen, die beeinflussen können, welche Nachricht Ihr Benutzer erhält. | Wenn ein Benutzer die definierten Kriterien in einer mit `{% custom_attribute.${Total_Revenue} > 0%}` gekennzeichneten Nachricht erfüllt, erhält er die Nachricht. Ansonsten erhalten sie je nach Konfiguration eine andere Nachricht (oder auch nicht). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}

<br>

