---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Certona, einer Realtime Omnichannel-Personalisierungslösung, die Personalisierung über den gesamten Kundenlebenszyklus hinweg bietet. Verwenden Sie Certona mit Braze Connected-Content Partner, um auf einfache Weise Inhaltsempfehlungen in Multichannel-Kampagnen einzufügen."
page_type: partner
search_tag: Partner

---

# Certona

> Die Plattform von Certona fördert die Personalisierung über den gesamten Kundenlebenszyklus hinweg. Von hochgradig individualisierten E-Mail Kampagnen bis hin zu maschinellen Lernangeboten für Produktempfehlungen - Certona sorgt dafür, dass Sie sich die leistungsstarke Personalisierung zunutze machen.

_Diese Integration wird von Certona gepflegt._

## Über die Integration

Die Integration von Braze und Certona nutzt die Produktempfehlungen von Certona für maschinelles Lernen in Kampagnen und Canvase von Braze über Connected-Content.

## Voraussetzungen

| Anforderung| Beschreibung|
| ---| ---|
| [Certona Konto](https://manage.certona.com/) | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Certona-Konto. |
| [Certona REST API Endpunkt](https://manage.certona.com/) | Dieser Endpunkt wird direkt in der Nachricht Ihrer Braze-Kampagne verwendet, um empfohlene Inhalte auf der Grundlage der Nutzer:in abzurufen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Nutzen Sie die REST API von Certona, um personalisierte Inhalte in Ihre Nachrichten einzufügen. Dazu fügen Sie die folgende Connected-Content-Vorlage in Ihren Nachrichten-Editor von Braze zusammen mit Ihrem Certona REST API Endpunkt ein.

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

Als nächstes definieren Sie den Inhalt, den Sie aufrufen möchten, z. B. relevante Texte oder Bilder. Zum Beispiel: `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`.

{% endraw %}

![Ein Bild einer Push-Kampagne mit Connected-Content von Certona in der Nachricht.]({% image_buster /assets/img/certona.png %})

Sobald Sie diese Nachricht in den Composer-Body eingefügt haben, sollten Sie eine Vorschau Ihres Connected-Content-Aufrufs anzeigen, um sicherzustellen, dass Sie die richtigen Informationen angezeigt haben.

![Ein Bild, das den Tab "Test" zeigt, der Nutzer:innen dazu anregt, ihre Nachricht vor dem Versand gründlich zu testen.]({% image_buster /assets/img/certona2.png %})


