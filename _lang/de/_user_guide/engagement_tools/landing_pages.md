---
nav_title: Landing Pages
article_title: Startseiten
page_order: 31
guide_top_header: "Startseiten"
description: "Dieser Artikel enthält Ressourcen zum Erstellen und Anpassen von Braze-Landingpages."
alias: /landing_pages/
---

# Über Landing Pages

> Braze Landing Pages sind eigenständige Webseiten, die Ihre Strategie zur Gewinnung von Nutzer:innen und zum Engagement vorantreiben können.

Nutzen Sie Landing Pages, um Ihre Zielgruppe zu vergrößern, Nutzerdaten zu erfassen, Sonderangebote zu bewerben und Kampagnen über mehrere Kanäle zu unterstützen.

{% alert note %}
Die Verfügbarkeit von Landing Pages und angepassten Domains hängt von Ihrem Braze-Paket ab. Wenden Sie sich an Ihren Account Manager oder Customer-Success-Manager:in, um loszulegen.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## Voraussetzungen

Bevor Sie auf Landing Pages zugreifen, sie erstellen und veröffentlichen können, benötigen Sie entweder [Administratorrechte]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) oder alle der folgenden Rechte:

- Startseiten aufrufen
- Entwürfe für Startseite erstellen
- Startseiten veröffentlichen

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Planebenen

Die Anzahl der veröffentlichten Startseiten und angepassten Domains, die Sie nutzen können, hängt von der Art Ihres Tarifs ab: kostenlos oder kostenpflichtig (inkrementell).

| Feature                                                                                                   | Kostenlose Nutzung     | Kostenpflichtige Nutzung (inkrementell)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Veröffentlichte Startseiten                                                                 | Fünf pro Unternehmen | 20 zusätzlich |
| Angepasste Domains          | Eine pro Unternehmen | Fünf zusätzliche |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Hinzufügen von Google Tag Manager zu einer Landing Page

Um Google Tag Manager zu Ihren Landing Pages hinzuzufügen, fügen Sie Ihrer Landing Page im Drag-and-Drop-Editor einen **Custom Code-Block** hinzu und fügen dann den Tag Manager-Code in den Block ein. Stellen Sie sicher, dass Sie vor dem Code für den Tag Manager:in eine Datenebene einfügen, wie in diesem Beispiel:

```
<script>
window.dataLayer = window.dataLayer || [];
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
<!-- End Google Tag Manager -->
```

Einzelheiten zur Implementierung des Google Tag Managers finden Sie in [der Dokumentation von Google.](https://developers.google.com/tag-platform/tag-manager/datalayer#installation)

## Häufig gestellte Fragen

### Was ist die maximale Größe für Landing Pages?

Die Größe der Landing Page kann bis zu 500 KB betragen.

### Gibt es irgendwelche technischen Voraussetzungen für die Veröffentlichung einer Landing Page?

Nein, es gibt keine technischen Anforderungen.

### Gibt es einen HTML-Editor für Landing Pages?

Ja Verwenden Sie den Block **Angepasster Code** im Drag-and-Drop-Editor, um HTML hinzuzufügen oder zu bearbeiten.

### Kann ich einen Webhook innerhalb einer Landing Page erstellen?

Nein, dies wird derzeit nicht unterstützt.
