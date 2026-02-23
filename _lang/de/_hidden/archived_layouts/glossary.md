---
nav_title: Glossar
article_title: Glossar Layout
page_order: 0
noindex: true
---

# Beispiel-Layout: Glossar

> Das Layout des Glossars ist in YAML. Es erfordert mehrere Komponenten und Parameter. Glossar-Layouts eignen sich gut für lokalisierte, durchsuchbare Inhalte, wie Wörterbücher und bestimmte Inhaltskategorien.

## Erforderliche Komponenten

1. YAML-Notation für Öffnungen und Schließungen. Mit anderen Worten: `---` vor dem Inhalt und `---` danach. 
2. Anführungszeichen um bestimmte Parameterinhalte. (Header-Parameter, Textparameter, Inhalte mit Bindestrichen oder anderen Sonderzeichen).
3. Glossar Tags Notation (Dies sind Filter Tags)

## Erforderliche Parameter

|Parameter | Inhaltstyp | Details |
|---|---|---|
|`page_order`| Numerisch | Ordnen Sie die Seite innerhalb des Abschnitts. Diese Reihenfolge wird in der linken Navigation angezeigt. |
| `nav-title`| Alphanumerisch | Titel, der in der linken Navigation erscheinen wird. |
|`layout`| Alphanumerisch - Keine Leerzeichen | Wählen Sie ein Layout aus dem [Layoutbereich](https://github.com/Appboy/braze-docs/tree/develop/_layouts) der Dokumentation aus. | 
|`glossary_top_header` | Alphanumerisch | Erfordert doppelte Anführungszeichen. Der Titel erscheint oben auf der Seite. |
|`glossary_top_text`| String, Alphanumerisch | Beschreiben Sie Ihre Glossarseite. Dies erscheint über der Suchleiste und den Filtern (falls Sie diese aktiviert haben). Dies ist im Wesentlichen in HTML geschrieben, so dass Sie \`\`\`\` verwenden können.<br> um Zeilenumbrüche zu erstellen. | 
|`glossary_tag_name` | Einzelnes Wort, Alphanumerisch | Benennen Sie Ihre Filter. Diese erscheinen in Kontrollkästchen unterhalb der Suchleiste sowie in den Daten darunter. | 
|`glossary_filter_text`| String, Alphanumerisch | Beschreiben Sie Ihre Filter. Wird in der Regel zur Belehrung verwendet. | 
|`glossary_tags`| Mehr YAML plus Inhalt. | Format wie unten gezeigt: <br> glossary_tags: <br>  \- Name: Content-Cards <br>  \- Name: E-Mail | 
| `glossaries`| Mehr YAML plus Inhalt. | Siehe [Glossare Parameter](#glossaries-parameters) unten. |

### Glossare Parameter

|Parameter | Inhaltstyp | Details |
|---|---|---|
|`name`| Alphanumerisch | Benennen Sie Ihren Artikel im Glossar.| 
|`description`| String, Alphanumerisch | Beschreiben Sie Ihren Artikel im Glossar. | 
|`calculation`| String | (optional) Beschreiben Sie, wie Ihr Glossarartikel berechnet wird (wird normalerweise bei der Beschreibung von Daten oder Metriken verwendet. | 
|`tags`| Alphanumerisch | Sollte mit dem übereinstimmen, was als `name` unter `glossary_tags` aufgeführt ist. Führen Sie so viele auf, wie zutreffend sind. Wenn Sie `All` schreiben, wird der Artikel in alle Filter aufgenommen.|

## Beispiel

```
---
page_order: 0
nav_title: Report Metrics Glossary
layout: glossary_page
glossary_top_header: "Report Metrics Glossary"
glossary_top_text: "These are terms you'll find in your reports in your Braze account. Search for the metrics you need, or filter by channel. <br>  <br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."

glossary_tag_name: Channels
glossary_filter_text: "Select Channels below to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Content Cards
  - name: Email
  - name: In-App Message
  - name: News Feed
  - name: Web Push
  - name: iOS Push
  - name: Android Push
  - name: Webhook

glossaries:
  - name: Variation
    description: Variation of a campaign, differing as defined by the creator.
    calculation: Count
    tags:
      - All
  - name: Audience
    description: Percentage of users who received a particular message. This number is received from Braze.
    calculation: (Number of Recipients in Variant) / (Unique Recipients)
    tags:
      - All
  - name: Unique Recipients
    description: Exact number of users who received a particular message. This number is received from Braze.
    calculation: Count
    tags:
      - Email
      - Web Push
      - iOS Push
      - Android Push
      - In-App Message
      - News Feed
  - name: Total Impressions
    description: The number of users whose devices reported that the in-app message has been delivered (if a user receives a message twice, they will be counted twice). This number is a sum of number of impression events that Braze receives from the SDKs.
    calculation: Count
    tags:
      - In-App Message
      - News Feed
      - Content Cards
---
```
