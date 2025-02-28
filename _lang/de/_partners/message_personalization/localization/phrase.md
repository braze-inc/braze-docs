---
nav_title: Phrase
article_title: Phrase
alias: /partners/phrase/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Phrase, einer cloudbasierten Software für die Lokalisierung. Mit dieser Integration können Sie E-Mail-Vorlagen und Inhaltsblöcke übersetzen, ohne die Braze-Oberfläche zu verlassen."
page_type: partner
search_tag: Partner

---

# Phrase 

> [Phrase](https://phrase.com/) ist eine cloudbasierte Software für das Lokalisierungsmanagement. Phrase ermöglicht automatisierte Übersetzungsworkflows und unterstützt die kontinuierliche Lokalisierung für agile Teams.

Mit der Phrase- und Braze-Integration können Sie E-Mail-Vorlagen und Inhaltsblöcke übersetzen, ohne die Braze-Oberfläche zu verlassen. Mit der Phrase TMS-Integration für Braze können Sie die Kundenbindung erhöhen und das Wachstum in neuen Märkten mit nahtloser Lokalisierung vorantreiben.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Phrase TMS-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Phrase TMS Ultimate- oder Enterprise-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit allen Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

## Schritt 1: Phrase TMS Einstellungen

Navigieren Sie in Phrase zu **Einstellungen > Integrationen > Konnektoren > Neu**.

1. Geben Sie einen Namen für die Verbindung ein und ändern Sie den Typ in **Hartlöten**.<br><br>
2. Geben Sie den REST-API-Schlüssel und den REST-Endpunkt von Braze ein. <br><br>
3. Wählen Sie aus, wie der Connector E-Mail-Vorlagen mit verknüpften Inhaltsblöcken importieren soll. 
- Nur ausgewählte E-Mail-Vorlage
- Inhaltsblöcke einbeziehen<br><br>
4. Wählen Sie aus, wie der Connector Übersetzungen von E-Mail-Vorlagen exportieren soll. 
- Neuen Artikel erstellen
- Original Artikel
  - Der ursprüngliche Artikel exportiert Übersetzungen in dieselbe Vorlage/denselben Block. Sprachsegmente werden durch das angegebene Attribut definiert.<br><br>
    {% raw %}
    Geben Sie das Sprachattribut an, wenn der Originalartikel ausgewählt ist. Das Attribut language definiert die Sprache des if/elsif-Arguments. Wenn Sie die Option Originalartikel verwenden, muss der Artikel wie unten gezeigt aufgebaut sein:

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
    Oder Sie verwenden die Zuordnung Schlüssel/Werte:
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
    Das obige Liquid muss strikt befolgt werden, aber das Attribut language sowie language, keys und value sind anpassbar.<br><br>
    Jeder Sprachcode kann nur einmal verwendet werden. Es können jedoch mehrere Sprachen für ein Segment verwendet werden, zum Beispiel:
    ```liquid
    {% elsif {{custom_attribute.${attribute_name}}} == 'de-DE' or {{custom_attribute.${attribute_name}}} == 'de-AT' or {{custom_attribute.${attribute_name}}} == 'de-CH' %}
    {% endraw %}
    ```
5. Klicken Sie auf **Verbindung testen**. Wenn die Verbindung erfolgreich ist, erscheint ein Häkchen. Bewegen Sie den Mauszeiger über das Symbol, um weitere Details zu sehen.<br><br>
7. Klicken Sie abschließend auf **Speichern**. Dieser Konnektor wird auf der Seite **Konnektoren** verfügbar sein.

## Schritt 3: Inhalte an Phrase senden und zurück nach Braze exportieren

1. Richten Sie zunächst das [Einreicherportal](https://support.phrase.com/hc/en-us/articles/5709602111132) ein, damit die Einreicher den Anträgen direkt aus dem Online-Repository Dateien hinzufügen können.<br><br>
2. Verwenden Sie die [automatische Projekterstellung (APC)](https://support.phrase.com/hc/en-us/articles/5709647363356), damit Phrase TMS automatisch neue Projekte erstellt, wenn eine Änderung in den angegebenen Workflow-Status festgestellt wird.<br><br>
3. Ausgewählte Inhalte werden bereits bei der ersten Ausführung von APC importiert.

Die [Connector API](https://cloud.memsource.com/web/docs/api#) kann Schritte automatisieren, die sonst manuell über die Benutzeroberfläche ausgeführt werden. Mit [Webhooks](https://support.phrase.com/hc/en-us/articles/5709693398812) kann Phrase TMS Systeme von Drittanbietern über bestimmte Ereignisse benachrichtigen (z.B. eine Änderung des Auftragsstatus).

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
