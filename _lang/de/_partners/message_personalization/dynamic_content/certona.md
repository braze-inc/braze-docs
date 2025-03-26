---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Certona, einer Omnichannel-Personalisierungslösung in Echtzeit, die Personalisierung über den gesamten Kundenlebenszyklus bietet. Verwenden Sie Certona mit dem Connected Content Partner von Braze, um auf einfache Weise Inhaltsempfehlungen in Multichannel-Kampagnen einzufügen."
page_type: partner
search_tag: Partner

---

# Certona

> Die Plattform von Certona ermöglicht die Personalisierung über den gesamten Kundenlebenszyklus hinweg. Von hochgradig individualisierten E-Mail-Kampagnen bis hin zu Produktempfehlungen auf der Grundlage von maschinellem Lernen - Certona sorgt dafür, dass Sie sich die Kraft der Personalisierung zunutze machen.

Die Integration von Braze und Certona nutzt die Produktempfehlungen des maschinellen Lernens von Certona in Braze-Kampagnen und Canvases durch Connected Content.

## Voraussetzungen

| Anforderung| Beschreibung|
| ---| ---|
| [Certona-Konto](https://manage.certona.com/) | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Certona-Konto. |
| [Certona REST API Endpunkt](https://manage.certona.com/) | Dieser Endpunkt wird direkt in Ihrer Braze-Kampagnennachricht verwendet, um empfohlene Inhalte auf der Grundlage der Benutzer-ID abzurufen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Verwenden Sie die REST API von Certona, um personalisierte Inhalte in Ihre Nachrichten einzufügen. Dazu fügen Sie die folgende Vorlage für Connected Content in Ihren Braze Message Composer zusammen mit Ihrem Certona REST API Endpunkt ein.

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

Als Nächstes definieren Sie den Inhalt, den Sie aufrufen möchten, z. B. relevante Texte oder Bilder. Zum Beispiel: `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`.

{% endraw %}

![Ein Bild einer Push-Kampagne mit Certona-bezogenen Connected Content im Nachrichtentext.][1]

Sobald Sie diese Nachricht in den Body des Composers eingefügt haben, sehen Sie sich Ihren Aufruf von Connected Content in der Vorschau an, um sicherzustellen, dass Sie die richtigen Informationen angezeigt haben.

![Ein Bild, das die Registerkarte "Test" zeigt und die Benutzer dazu auffordert, ihre Nachricht vor dem Senden gründlich zu testen.][2]

[1]: {% image_buster /assets/img/certona.png %}
[2]: {% image_buster /assets/img/certona2.png %}