---
nav_title: LiftIgniter
article_title: LiftIgniter
alias: /partners/liftigniter/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und LiftIgniter, einer führenden Plattform für Personalisierung, die Unternehmen bei der Transformation ihrer Kundenerlebnisse unterstützt."
page_type: partner
search_tag: Partner

---

# Liftigniter

> LiftIgniter ist eine führende Personalisierungsplattform, die Unternehmen dabei hilft, ihre Kundenerlebnisse durch Realtime-Personalisierung an jedem Touchpoint zu transformieren.

_Diese Integration wird von Liftigniter gepflegt._

## Über die Integration

Die Integration von Liftigniter und Braze nutzt Connected-Content, damit Sie interessante Themen wie Nachrichtenartikel, Kleidung und andere Artikel und Videos aus dem Einzelhandel empfehlen können.

## Voraussetzungen

| Anforderung| Beschreibung|
| ---| ---|
| LiftIgniter Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Liftigniter-Konto](https://console.liftigniter.com/login). |
| LiftIgniter API Integration | Sie müssen LiftIgniter in Ihre Website oder App [integrieren](https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview), um Empfehlungen von dort abrufen zu können. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

Verwenden Sie [die REST API von LiftIgniter](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389), um personalisierte Inhalte in Ihre Nachrichten einzufügen. Nachdem Sie Ihr LiftIgniter-Konto eingerichtet haben und LiftIgniter in Ihre App integriert ist, fügen Sie das folgende Template in Ihren Nachrichten-Editor ein, um Inhalte in Ihren Nachrichten aufzurufen und Informationen nach Bedarf zu ersetzen (`x-api-key`, `theapikey`, etc.).

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {"x-api-key": "theapikey"} :body "UseActivity"=false :content_type application/json :save json %}
```

Als nächstes schreiben Sie Ihre Nachricht und definieren den Inhalt, den Sie mit JSON aufrufen möchten. Zum Beispiel: `{{json.items[0].title}}`.

{% endraw %}

![Ein Bild, das eine Push-Kampagne zeigt, die LiftIgniter-spezifische Connected-Content-Aufrufe enthält. Außerdem wurde dem Bildfeld eine Connected-Content-Logik hinzugefügt.]({% image_buster /assets/img/liftigniter.png %})

Sobald Sie diese Nachricht in den Body des Composers eingefügt haben, können Sie eine Vorschau Ihrer Nachricht anzeigen. Sie können sogar Bilder einfügen, wie im folgenden Beispiel gezeigt:

![Eine Vorschau darauf, wie die Nachricht nach dem Versenden aussehen wird.]({% image_buster /assets/img/liftigniter2.png %})


