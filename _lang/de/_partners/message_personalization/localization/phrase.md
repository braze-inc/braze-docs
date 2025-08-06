---
nav_title: Phrase
article_title: Phrase
alias: /partners/phrase/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Phrase, einer cloudbasierten Software für die Lokalisierung. Diese Integration erlaubt es Ihnen, E-Mail Templates und Content-Blöcke zu übersetzen, ohne die Schnittstelle von Braze zu verlassen."
page_type: partner
search_tag: Partner

---

# Phrase 

> [Phrasee](https://phrase.com/) ist eine cloudbasierte Software zur Verwaltung der Lokalisierung. Phrase ermöglicht automatisierte Übersetzungsworkflows und unterstützt die kontinuierliche Lokalisierung für agile Teams.

_Diese Integration wird von Phrasee gepflegt._

## Über die Integration

Die Integration von Phrase und Braze erlaubt es Ihnen, E-Mail Templates und Content-Blöcke zu übersetzen, ohne die Schnittstelle von Braze zu verlassen. Mit der Phrase TMS Integration für Braze können Sie das Customer-Engagement STEIGERN und das Wachstum in neuen Märkten mit nahtloser Lokalisierung vorantreiben.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Phrase TMS-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Phrase TMS Ultimate- oder Enterprise-Konto. |
| Braze REST API-Schlüssel | Ein REST-API-Schlüssel von Braze mit allen Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

## Schritt 1: Phrase TMS Einstellungen

Navigieren Sie in Phrasee zu **Einstellungen > Integrationen > Konnektoren > Neu.**

1. Geben Sie einen Namen für die Verbindung ein und ändern Sie den Typ in **Braze**.<br><br>
2. Geben Sie den REST API-Schlüssel und den Braze REST-Endpunkt ein. <br><br>
3. Wählen Sie aus, wie der Konnektor E-Mail Templates mit verknüpften Content-Blöcken importieren soll. 
- Nur ausgewählte E-Mail Templates
- Content-Blöcke einbinden<br><br>
4. Wählen Sie aus, wie der Konnektor Übersetzungen von E-Mail Templates exportieren soll. 
- Neuen Artikel erstellen
- Original Artikel
  - Der ursprüngliche Artikel exportiert Übersetzungen in dasselbe Template/Block. Sprachsegmente werden durch das angegebene Attribut definiert.<br><br>
    {% raw %}
    Geben Sie das Attribut "Sprache" an, wenn der ursprüngliche Artikel ausgewählt ist. Das Attribut language definiert die Sprache des if/elsif-Arguments. Wenn Sie die Option für den ursprünglichen Artikel verwenden, muss er wie unten dargestellt aufgebaut sein:

    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
    danish content
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
    portuguese content
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
    swedish content
    {% else %}
    Original content
    {% endif %}
    ```
    Oder Sie verwenden die Abbildung Schlüssel/Werte zuweisen:
    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
      {% assign abc_key1 = "danish_value1" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
      {% assign abc_key = "portuguese value" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
      {% assign abc_key = "swedish value" %}
    {% else %}
      {% assign abc_key = "Source language value" %}
    {% endif %}
    ```
    Das obige Liquid muss strikt befolgt werden, aber das Attribut language und language, die Schlüssel und der Wert sind anpassbar.<br><br>
    Jeder Code kann nur einmal verwendet werden. Für ein Segment können jedoch z.B. mehrere Sprachen verwendet werden:
    ```liquid
    {% elsif {{custom_attribute.${attribute_name}}} == 'de-DE' or {{custom_attribute.${attribute_name}}} == 'de-AT' or {{custom_attribute.${attribute_name}}} == 'de-CH' %}
    {% endraw %}
    ```
5. Klicken Sie auf **Verbindung testen**. Wenn die Verbindung erfolgreich ist, erscheint ein Häkchen. Bewegen Sie den Mauszeiger über das Symbol, um weitere Details zu sehen.<br><br>
7. Klicken Sie abschließend auf **Speichern**. Dieser Konnektor wird auf der Seite **Konnektoren** verfügbar sein.

## Schritt 3: Inhalte an Phrase senden und zurück nach Braze exportieren

1. Richten Sie zunächst das [Portal für Einreicher](https://support.phrase.com/hc/en-us/articles/5709602111132) ein, damit diese den Anfragen direkt aus dem Online-Repository Dateien hinzufügen können.<br><br>
2. Verwenden Sie die [automatische Projekterstellung (APC)](https://support.phrase.com/hc/en-us/articles/5709647363356), damit Phrase TMS automatisch neue Projekte erstellt, wenn eine Änderung in den angegebenen Workflow-Status festgestellt wird.<br><br>
3. Ausgewählte Artikel werden bei der ersten Ausführung von APC importiert.

Die [Konnektor API](https://cloud.memsource.com/web/docs/api#) kann Schritte automatisieren, die sonst manuell über die UI ausgeführt werden. Mit [Webhooks](https://support.phrase.com/hc/en-us/articles/5709693398812) kann Phrase TMS Systeme von Drittanbietern über bestimmte Ereignisse benachrichtigen (z.B. eine Änderung des Auftragsstatus).


