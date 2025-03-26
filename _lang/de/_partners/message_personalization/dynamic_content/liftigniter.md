---
nav_title: LiftIgniter
article_title: LiftIgniter
alias: /partners/liftigniter/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und LiftIgniter, einer führenden Personalisierungsplattform, die Unternehmen dabei hilft, ihr Kundenerlebnis zu verbessern."
page_type: partner
search_tag: Partner

---

# Liftigniter

> LiftIgniter ist eine führende Personalisierungsplattform, die Unternehmen dabei hilft, ihre Kundenerlebnisse durch Echtzeit-Personalisierung an jedem Berührungspunkt zu verbessern.

Die LiftIgniter- und Braze-Integration nutzt Connected Content, damit Sie interessante Themen wie Nachrichtenartikel, Kleidung und andere Einzelhandelsartikel und Videos empfehlen können.

## Voraussetzungen

| Anforderung| Beschreibung|
| ---| ---|
| LiftIgniter Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [LiftIgniter-Konto](https://console.liftigniter.com/login). |
| LiftIgniter API-Integration | Sie müssen LiftIgniter in Ihre Website oder App [integrieren](https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview), um Empfehlungen von dort beziehen zu können. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

Verwenden Sie [die REST-API von LiftIgniter](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389), um personalisierte Inhalte in Ihre Nachrichten einzufügen. Nachdem Sie Ihr LiftIgniter-Konto eingerichtet haben und LiftIgniter in Ihre App integriert ist, fügen Sie die folgende Vorlage in Ihren Message Composer ein, um Inhalte in Ihren Nachrichten aufzurufen, wobei Sie die Informationen nach Bedarf ersetzen (`x-api-key`, `theapikey`, etc.).

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {"x-api-key": "theapikey"} :body "UseActivity"=false :content_type application/json :save json %}
```

Als nächstes schreiben Sie Ihre Nachricht und definieren den Inhalt, den Sie mit JSON aufrufen möchten. Zum Beispiel: `{{json.items[0].title}}`.

{% endraw %}

![Ein Bild mit einer Push-Kampagne, die LiftIgniter-spezifische Connected Content-Aufrufe enthält. Außerdem wurde dem Bildfeld eine Logik für verbundene Inhalte hinzugefügt.][1]

Sobald Sie diese Nachricht in den Body des Composers eingefügt haben, können Sie eine Vorschau Ihrer Nachricht anzeigen. Sie können sogar Bilder einfügen, wie im folgenden Beispiel gezeigt:

![Ein Vorschaubild, wie die Nachricht nach dem Versenden aussehen wird.][2]

[1]: {% image_buster /assets/img/liftigniter.png %}
[2]: {% image_buster /assets/img/liftigniter2.png %}