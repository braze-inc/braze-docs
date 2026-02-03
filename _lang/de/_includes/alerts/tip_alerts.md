{% if include.alert == "Liquid email display name and reply-to address" %}

{% alert tip %}
Sie können [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) in den Feldern **Absender-Anzeigename + Adresse** und **Antwort-Annahme-Adresse** verwenden, um diese auf der Grundlage angepasster Attribute dynamisch anzupassen. So können Sie mit einer einzigen E-Mail-Kampagne oder einem einzigen Canvas-Schritt von verschiedenen Marken, Regionen oder Abteilungen aus versenden.
{% endalert %}

{% endif %}

{% if include.alert == "Reference properties from triggering event" %}

{% alert tip %}
Sie benötigen keinen Kontextschritt, um Eigenschaften des triggernden Ereignisses in [Zielgruppen-Pfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) oder [Decision-Split-Schritten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) zu referenzieren. Sie können die Eigenschaften direkt in den Filtergruppen mit dem Filter **Kontextvariable** referenzieren. Stellen Sie sicher, dass Sie den richtigen Datentyp auswählen.
{% endalert %}

{% endif %}

{% if include.alert == 'catalog data images' %}

{% alert tip %}
Um Bilder für triggernde Artikel im Katalog zu verwenden, muss Ihr Katalog ein Feld namens `image_url` enthalten. Sie können sie dann mit {%raw%}``{{ items[0].image_url }}``{%endraw%} referenzieren.
{% endalert %}

{% endif %}