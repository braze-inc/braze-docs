---
nav_title: "Targeting von Nutzer:innen"
article_title: "Targeting von Nutzer:innen"
page_order: 4
tool: Campaigns
page_type: reference
description: "Dieser Referenzartikel behandelt die Targeting-Optionen, die Sie im Schritt Zielgruppen der Kampagnenerstellung finden."
---

# Targeting von Nutzer:innen

> Nachdem Sie [Ihre Kampagne zusammengestellt][1] und den [Zeitplan für die Zustellung][2] festgelegt haben, können Sie im Schritt **Zielgruppen** die Zielempfänger Ihrer Kampagne festlegen. 

## Targeting-Optionen

Unter dem Abschnitt **Zielgruppenoptionen** finden Sie einige Optionen, an wen Sie Ihre Kampagne senden können.

{% alert note %}
Nur die Benutzer, die den von Ihnen festgelegten Kriterien entsprechen, erhalten die Kampagne. Denken Sie daran, dass die genaue Segmentzugehörigkeit immer erst kurz vor dem Versand der Nachricht berechnet wird.
{% endalert %}

### Targeting von Nutzer:innen in einem bestehenden Segment {#existing-segment}

Um Mitglieder eines zuvor erstellten Segments anzusprechen, wählen Sie ein Segment aus der Dropdown-Liste unter **Benutzer ansprechen nach Segment**.

### Targeting von Nutzer:innen in mehreren bestehenden Segmenten {#multiple-existing-segment}

Um Benutzer anzusprechen, die in mehrere zuvor erstellte Segmente fallen, fügen Sie mehrere Segmente aus der Dropdown-Liste unter **Benutzer ansprechen nach Segment** hinzu. Die resultierende Zielgruppe besteht aus Nutzer:innen des ersten Segments, des zweiten Segments, des dritten Segments usw.

### Benutzer in mehreren bestehenden Segmenten und Filtern ansprechen {#existing_segment_filter}

Sie können auch Nutzer:innen aus einem oder mehreren zuvor erstellten Segmenten zusammenstellen, die ebenfalls unter zusätzliche Filter fallen. Nachdem Sie zunächst Ihre Segmente ausgewählt haben, können Sie Ihre Zielgruppe im Abschnitt **Zusätzliche Filter** weiter verfeinern. Dies wird im folgenden Screenshot veranschaulicht. Das Targeting zielt auf Nutzer:innen ab, die zum Segment Täglich aktive:r Nutzer:in gehören, E-Mails nicht öffnen und vor weniger als 30 Tagen einen Kauf getätigt haben.

![][25]

### Targeting Nutzer:innen ohne Segmentierung {#without-segment}

Um Nutzer:innen zusammenzustellen, ohne ein Segment hinzuzufügen, können Sie eine Reihe von Filtern verwenden. Das bedeutet, dass Sie eine Kampagne nicht auf ein bereits vorhandenes Segment ausrichten müssen. Sie können während der Kampagnenerstellung eine improvisierte Zielgruppe erstellen, indem Sie einfach die zusätzlichen Filter verwenden und keine Segmente unter **Zielbenutzer nach Segment** auswählen. Dies erlaubt es Ihnen, die Segmentierung zu überspringen, wenn Sie Kampagnen an einmalige Zielgruppen senden.

![][26]

## Targeting von Seed-Gruppen

Für E-Mail-Kampagnen können Sie Seed-Gruppen unter dem Abschnitt **Seed-Gruppen** gezielt ansprechen. Beachten Sie, dass Seed-Gruppen nicht für API-Kampagnen verfügbar sind, obwohl Sie Seed-Gruppen über einen API-getriggerten Entry in eine Kampagne aufnehmen können. Weitere Informationen finden Sie unter [Saatgutgruppen]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).

## Testen Sie Ihre Zielgruppe

Nachdem Sie Ihrer Zielgruppe Segmente und Filter hinzugefügt haben, können Sie testen, ob Ihre Zielgruppe wie erwartet eingerichtet ist, indem Sie [nach einem Benutzer suchen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), um zu überprüfen, ob er den Kriterien der Zielgruppe entspricht.

![]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:60%"}

## Zusammenfassung der Zielgruppe

Sobald Sie Segmente oder Filter zur Feinabstimmung Ihrer Zielgruppe hinzugefügt haben, zeigt Ihnen die **Publikumsübersicht** einen Überblick darüber, wer zu Ihrem Zielpublikum gehört. Hier können Sie die Zielgruppe Ihrer Kampagne weiter einschränken, indem Sie eine maximale Nutzerbegrenzung oder eine [Rate-Limiting-Zustellung][3] festlegen. Für E-Mail- und Push-Benachrichtigungs-Kampagnen können Sie auswählen, welcher Abo- und Opt-in-Status angestrebt werden soll.

![][27]

## A/B-Tests

Im Bereich **A/B-Tests** können Sie einen Test einrichten, um die Reaktionen der Nutzer auf mehrere Versionen derselben Marketingkampagne zu vergleichen. Diese Versionen haben ähnliche Marketingziele, unterscheiden sich aber in Wortlaut und Stil. Ziel ist es, die Version der Kampagne zu ermitteln, die Ihre Marketingziele am besten erreicht. 

Weitere Informationen und bewährte Verfahren finden Sie unter [Multivariate & A/B-Tests][4].

## Zielgruppe Statistik

Braze bietet in der Fußzeile detaillierte Statistiken zu den Zielgruppen der Kanäle. 

Je größer Ihre Nutzerbasis ist, desto wahrscheinlicher ist die Anzahl der **erreichbaren Nutzer** eine grobe Schätzung. Die Anzahl der erreichbaren Benutzer kann sich verringern, wenn Sie eine [globale Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) verwenden oder die Berechtigung für Nachrichten einrichten. Wählen Sie [Exakte Statistik berechnen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics), um eine genaue Zahl für Ihre erreichbaren Nutzer zu ermitteln, da dabei jeder Nutzer in Ihrer Nutzerbasis durchsucht wird. 

Beachten Sie Folgendes:

- Die Berechnung der genauen Statistiken kann einige Minuten in Anspruch nehmen. Diese Funktion berechnet die genauen Statistiken nur auf Segmentebene, nicht auf Filter- oder Filtergruppenebene.
- Bei großen Segmenten ist es normal, dass selbst bei der Berechnung exakter Statistiken leichte Abweichungen auftreten. Es wird erwartet, dass die Genauigkeit dieses Features 99,999 % oder mehr beträgt.

![][24]

Um zu sehen, welcher Prozentsatz Ihrer Nutzerbasis angesprochen wird oder wie hoch der Lifetime Value (LTV) für dieses Segment ist, wählen Sie **Zusätzliche Statistiken anzeigen**.

[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %}
[26]: {% image_buster /assets/img_archive/additional_filters.png %}
[27]: {% image_buster /assets/img_archive/audience_summary.png %}
