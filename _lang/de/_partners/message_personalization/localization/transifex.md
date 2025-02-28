---
nav_title: Transifex
article_title: Transifex
alias: /partners/transifex/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Transifex, einer Lokalisierungsplattform, die es Ihnen ermöglicht, die Übersetzung zu automatisieren, so dass sich Ihre Teams auf die Bereitstellung eines hervorragenden Kundenerlebnisses konzentrieren können."
page_type: partner
search_tag: Partner

---

# Transifex

> Transifex ermöglicht eine robuste Lokalisierung für Ihre gesamte Benutzerbasis, unabhängig von der jeweiligen Sprache.

Die Integration von Braze und Transifex nutzt Connected Content, damit Sie eine Sammlung von Ressourcenstrings abrufen und relevante Übersetzungen in Ihre Nachrichten einfügen können, anstatt Zeilen mit sprachbasierter bedingter Formatierung. Dies automatisiert die Übersetzung und gibt Ihren Teams den nötigen Freiraum, um sich auf die Bereitstellung brillanter Kundenerlebnisse zu konzentrieren.

{% alert important %}
Ab dem 7\. April 2022 hat Transifex die API-Versionen 2 und 2.5 veraltet, um Platz für Version 3 zu machen. v2 und v2.5 sind nicht mehr funktionsfähig, und entsprechende Anfragen werden fehlschlagen. <br><br>Die folgenden Integrationsanweisungen beziehen sich auf das Update auf Version 3. Aktualisieren Sie Ihre Connected Content-Aufrufe entsprechend.
{% endalert %}

## Voraussetzungen

| Anforderung| Beschreibung|
| ---| ---|
|Transifex Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Transifex-Konto](https://www.transifex.com/signin/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Die Transifex-Integration verwendet die [API für Ressourcenübersetzungen](https://developers.transifex.com/reference/get_resource-translations) von Transifex. Mit der folgenden cURL können Sie feststellen, ob Ihr Konto Inhaltswerte hat, die mit Übersetzungen verbunden sind. 

Geben Sie zunächst die in Ihrem Transifex-Konto gefundenen `<ORGANIZATION_NAME>`, `<PROJECT_NAME>` und `<RESOURCE_NAME>` ein. Als nächstes ersetzen Sie `<LANGUAGE>` durch den Sprachcode, nach dem Sie die Übersetzungen filtern möchten, und `<TRANSIFEX_BEARER_TOKEN>` durch Ihr [Transifex-Token](https://developers.transifex.com/reference/api-authentication).

```
curl --request GET \
     --url 'https://rest.api.transifex.com/resource_translations?filter\[resource\]=o:<ORGANIZATION_NAME>:p:<PROJECT_NAME>:r:<RESOURCE_NAME>&filter\[language\]=l:<LANGUAGE>' \
     --header 'Accept: application/vnd.api+json' \
     --header 'Authorization: Bearer 1/<TRANSFIX_BEARER_TOKEN>'
```

Wenn sich Ihr Transifex-Projekt zum Beispiel auf `https://www.transifex.com/appboy-3/french2/french_translationspo/` befindet, wird `project_name` zu "french2" und `resource_name` zu "french_translationspo".

## Beispiel für eine Nachricht von Connected Content

Dieser Beispielcode nutzt die Transifex-API für die Ressourcenübersetzung und das Attribut `language` des Benutzers. Je nach Bedarf können Sie dann eine Schleife durch die String-Objekte ziehen und den relevanten Inhalt mit dem folgenden Liquid einlesen: `{{strings.data[X].attributes.strings.other}}`.

{% raw %}
```
{% assign organization = "<ORGANIZATION_NAME>" %}
{% assign project = "<PROJECT_NAME>" %}
{% assign resource = "<RESOURCE_NAME>" %}

{% if {{${language}}} == "en" or {{${language}}} == "it" or {{${language}}} == "de" or {{${language}}} == "another_language_you_support"  %}
{% connected_content
     https://rest.api.transifex.com/resource_translations?filter[resource]=o:{{organization}}:p:{{project}}:r:{{resource}}&filter[language]=l:{{${language}}}
     :method GET
     :headers {
       "Authorization": "Bearer <TRANSIFEX_BEARER_TOKEN>"
  }
     :accept application/vnd.api+json
     :save strings
%}
{% endif %}

{% if {{strings}} != null and {{strings.data[0].attributes.strings.other}} != "" and {{${language}}} != null %}
  {{strings.data[0].attributes.strings.other}}
{% else %}
  {% abort_message('null or blank') %}
{% endif %}
```
{% endraw %}

[16]: [success@braze.com](mailto:success@braze.com)
[31]: https://docs.transifex.com/api/translation-strings
