---
nav_title: "Targeting von Nutzer:innen"
article_title: "Targeting von Nutzer:innen"
page_order: 9
page_type: reference
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Ihre Zielgruppe in Ihrer Kampagne und in den Canvas-Editoren ansprechen können."
tool:
    - Campaigns
    - Canvas
---

# Targeting von Nutzer:innen

> Die Festlegung des Targetings für Ihre Nutzer:innen ist einer der wichtigsten Schritte bei der Erstellung einer Kampagne oder eines Canvas. Wenn Sie verstehen, wie Sie Ihre Zielgruppe auf der Grundlage ihres Verhaltens, ihrer Vorlieben und ihrer demografischen Daten segmentieren können, können Sie Ihr Messaging maßgeschneidert und personalisiert gestalten.

## Erstellen einer Zielgruppe

### Schritt 1: Nutzer:innen auswählen

Unter **Targeting-Optionen** können Sie mit den folgenden Optionen auswählen, welche Nutzer:innen Sie für Ihre Kampagne oder Ihr Canvas ansprechen möchten. Nur die Nutzer:innen, die den von Ihnen festgelegten Kriterien entsprechen, erhalten die Nachricht. Denken Sie daran, dass die genaue Segmentzugehörigkeit immer erst kurz vor dem Versand der Nachricht berechnet wird.

{% tabs local %}
{% tab einzelnes Segment %}
Um Mitglieder eines zuvor erstellten Segments anzusprechen, wählen Sie ein Segment aus der Dropdown-Liste unter **Benutzer ansprechen nach Segment**.
{% endtab %}

{% tab mehrere Segmente %}
Um Benutzer anzusprechen, die in mehrere zuvor erstellte Segmente fallen, fügen Sie mehrere Segmente aus der Dropdown-Liste unter **Benutzer ansprechen nach Segment** hinzu. Die resultierende Zielgruppe besteht aus Nutzer:innen des ersten Segments, des zweiten Segments, des dritten Segments usw.
{% endtab %}

{% tab mehrere Filter %}
Um Nutzer:innen zusammenzustellen, ohne ein Segment hinzuzufügen, können Sie eine Reihe von Filtern verwenden. Dies ist eine improvisierte Zielgruppe bei der Erstellung von Nachrichten und erlaubt es Ihnen, die Segmentierung zu überspringen, wenn Sie an einmalige Zielgruppen senden.

![Zusätzliche Filter für eine Nachricht, die auf Nutzer:innen abzielt, die eine App zuletzt innerhalb eines Tages geöffnet haben, noch nie eine Kampagne oder einen Canvas-Schritt erhalten haben und die vor weniger als 30 Tagen einen Kauf getätigt haben.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:70%;"}
{% endtab %}

{% tab Segmente & Filter %}
Sie können auch Nutzer:innen aus einem oder mehreren zuvor erstellten Segmenten zusammenstellen, die ebenfalls unter zusätzliche Filter fallen. Nachdem Sie zunächst Ihre Segmente ausgewählt haben, können Sie Ihre Zielgruppe im Abschnitt **Zusätzliche Filter** weiter verfeinern. Dies wird im folgenden Screenshot veranschaulicht. Das Targeting zielt auf Nutzer:innen ab, die im Segment "Täglich aktive:r Nutzer:in" sind, im Segment "Niemals geöffnete E-Mail" und vor mehr als 30 Tagen einen Kauf getätigt haben.

![Targeting-Optionen für eine Nachricht, die zwei Segmente umfassen und einen zusätzlichen Filter für einen letzten Kauf, der weniger als 30 Tage zurückliegt, haben.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:70%;"}
{% endtab %}
{% endtabs %}

{% alert tip %}
Für E-Mail-Kampagnen können Sie Seed-Gruppen unter dem Abschnitt **Seed-Gruppen** gezielt ansprechen. Beachten Sie, dass Seed-Gruppen nicht für API-Kampagnen verfügbar sind, obwohl Sie Seed-Gruppen über einen API-getriggerten Entry in eine Kampagne aufnehmen können. Weitere Informationen finden Sie unter [Saatgutgruppen]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).
{% endalert %}

### Schritt 2: Testen Sie Ihre Zielgruppe

Nachdem Sie Ihrer Zielgruppe Segmente und Filter hinzugefügt haben, können Sie testen, ob Ihre Zielgruppe wie erwartet eingerichtet ist, indem Sie [nach einem Benutzer suchen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), um zu überprüfen, ob er den Kriterien der Zielgruppe entspricht.

![Der Bereich "Nutzer:innen" mit einem Button "Nutzer:innen suchen".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%"}

#### Zusammenfassung der Zielgruppe

Die **Zielgruppenübersicht** gibt Ihnen eine Übersicht über die Personen, die zu Ihrer Zielgruppe gehören. Hier können Sie Ihre Zielgruppe weiter einschränken, indem Sie eine maximale Nutzer:innen-Begrenzung oder eine [Rate-Limiting-Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) festlegen.

![Der Abschnitt "Zusammenfassung der Zielgruppe" mit Optionen zum Festlegen einer maximalen Nutzer:innen oder Rate-Limits für die Zustellung.]({% image_buster /assets/img_archive/audience_summary.png %})

#### A/B-Tests

Im Bereich **A/B-Tests** können Sie einen Test einrichten, um die Reaktionen der Nutzer:innen auf mehrere Versionen der gleichen Marketing-Kampagne zu vergleichen. Diese Versionen haben ähnliche Marketingziele, unterscheiden sich aber in Wortlaut und Stil. Ziel ist es, die Version der Kampagne zu ermitteln, die Ihre Marketingziele am besten erreicht. 

Weitere Informationen und bewährte Verfahren finden Sie unter [Multivariate & A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

#### Zielgruppe Statistik

Braze bietet in der Fußzeile detaillierte Statistiken zu den Zielgruppen der Kanäle. Je größer Ihre Nutzerbasis ist, desto wahrscheinlicher ist die Anzahl der **erreichbaren Nutzer** eine grobe Schätzung. Die Anzahl der erreichbaren Benutzer kann sich verringern, wenn Sie eine [globale Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) verwenden oder die Berechtigung für Nachrichten einrichten. 

- Um eine genaue Zahl für Ihre erreichbaren Nutzer zu ermitteln, wählen Sie [Exakte Statistik berechnen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics) aus, denn damit werden alle Nutzer:in Ihrer Nutzerbasis durchsucht.
- Um zu sehen, welcher Prozentsatz Ihrer Nutzerbasis angesprochen wird oder wie hoch der Lifetime Value (LTV) für dieses Segment ist, wählen Sie **Zusätzliche Statistiken anzeigen**.
- Um zu sehen, welcher Prozentsatz Ihrer Nutzerbasis angesprochen wird oder wie hoch der Lifetime Value (LTV) für dieses Segment ist, wählen Sie **Zusätzliche Statistiken anzeigen**.

![Der Abschnitt "Gesamtbevölkerung" mit geschätzten Zahlen für erreichbare Nutzer:innen in jedem Targeting-Kanal.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
Die Berechnung der genauen Statistiken kann einige Minuten in Anspruch nehmen. Diese Funktion berechnet die genauen Statistiken nur auf Segmentebene, nicht auf Filter- oder Filtergruppenebene.<br><br>
Bei großen Segmenten ist es normal, dass selbst bei der Berechnung exakter Statistiken leichte Abweichungen auftreten. Es wird erwartet, dass die Genauigkeit dieses Features 99,999 % oder mehr beträgt.
{% endalert %}

