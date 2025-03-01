---
nav_title: Überlappung der Bildlaufleiste
article_title: Überlappung der Bildlaufleiste
page_order: 0

page_type: solution
description: "Dieser Hilfe-Artikel zeigt Mac-Benutzern, wie Sie Rollbalken, die den Inhalt von Braze-Dokumenten überlagern, beseitigen können."
---

# Überlappung der Bildlaufleiste

Verwenden Sie einen Mac und stellen fest, dass Ihre Bildlaufleisten den Inhalt von Braze Docs überlagern, wie im folgenden Beispiel?

![Beispiel für die Überlappung der Bildlaufleiste][1]

Prüfen Sie, ob Ihre Bildlaufleiste den folgenden Codeblock überlappt:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.S3.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.S3.integration.<integration-id>+<partition>+<offset>.avro
```

Wenn Ihre Bildlaufleiste den Codeblock überlappt, empfehlen wir Ihnen, die Einstellung **Bildlaufleisten anzeigen:** in Ihren **Allgemeinen Einstellungen** auf **Immer** zu ändern. Dadurch werden Funktionen in Docs (wie z.B. Codeblöcke) so erweitert, dass die Bildlaufleiste immer angezeigt wird und die Unlesbarkeit verhindert wird.

![MacOS Allgemeine Einstellungen][2]

So sollte Ihre aktualisierte Bildlaufleiste jetzt aussehen:

![Beispiel einer festen Bildlaufleiste ohne Überlappung][3]

_Zuletzt aktualisiert am 27\. März 2019_

{% comment %}
Fügen Sie dies dort ein, wo eine einzelne lange Codezeile Probleme verursachen könnte:
_Sie können den Code wegen der Bildlaufleiste nicht sehen? Sehen Sie [hier]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/), wie Sie das beheben können._
{% endcomment %}

[1]: {% image_buster /assets/img/scroll-overlap.png %}
[2]: {% image_buster /assets/img/general-on-mac.png %}
[3]: {% image_buster /assets/img/scroll-bar-on.png %}
