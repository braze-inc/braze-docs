---
nav_title: Segment-Insights
article_title: Segment-Insights
page_order: 4
page_type: tutorial
tool: 
  - Segments
  - Reports
description: "In diesem Artikel erfahren Sie, wie Sie Segment-Insights verwenden, interpretieren und weitergeben können."
---

# [![Braze-Lernkurse]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Segment-Insights

> Lernen Sie, wie Sie Segment-Insights verwenden, interpretieren und weitergeben können. 

Segment Insights zeigt Ihnen, wie sich ein Segment im Vergleich zu einem anderen in einer Reihe von vorher ausgewählten KPIs verhält.

## Segmenteinblicke anzeigen

Gehen Sie auf die Seite **Segment Insights** in Ihrem Dashboard unter **Analytics** und klicken Sie auf <i class="fas fa-plus"></i> **Segment hinzufügen**, um bis zu vier verschiedene Segmente im Vergleich zu einer Baseline anzuzeigen.

![Segment Insights Dashboard.][1]

Das Basissegment kann entweder ein bestimmtes Segment sein, das Sie auswählen, oder ein Segment, das alle Ihre Nutzer enthält. Sie können die folgenden Statistiken mit Segment Insights vergleichen:

| Messung | Beschreibung | Formel |
| --------------------- | ------------- | ------------- |
| Sitzungs-Häufigkeit | Durchschnittliche Anzahl der Sitzungen der Segmentbenutzer pro Tag | (Gesamtzahl der Sitzungen) / (Anzahl der Tage seit der ersten Sitzung) |
| Zeit seit der ersten Sitzung | Durchschnittliche Zeit zwischen der ersten Sitzung von Nutzer:innen im Segment und jetzt | heute – Datum der ersten Sitzung |
| Zeit seit der letzten Sitzung | Durchschnittliche Zeit zwischen der letzten Sitzung von Nutzer:innen im Segment und jetzt | heute – Datum der letzten Sitzung |
| Lifetime-Umsatz | Durchschnittlicher Lifetime-Umsatz von Nutzer:innen im Segment | Nutzerausgaben über die gesamte Lifetime |
| Zeit bis zum ersten Kauf | Durchschnittliche Zeit zwischen der ersten Sitzung von Nutzer:innen im Segment und dem ersten Kauf | Datum des ersten Kaufs – Datum der ersten Sitzung |
| Zeit seit dem letzten Kauf | Durchschnittliche Zeit zwischen dem letzten Kauf von Nutzer:innen im Segment und jetzt | heute - Datum des letzten Kaufs |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Über die eindeutige URL der Seite können Sie bestimmte Vergleiche ganz einfach mit Ihren Teamkollegen teilen, und Sie können auch unter jedes Segment klicken, um weitere Informationen über dieses Segment zu erhalten. Diese Vergleiche werden zurückgesetzt, wenn Sie zwischen Workspaces wechseln.

![][2]

## Segment Details Seite

Die Segmenteinblicke wurden auch direkt in die Ansicht **Segmentdetails** integriert. Wenn Sie sich ein bestimmtes Segment ansehen, das Sie zuvor eingerichtet haben, finden Sie dieselben sechs Statistiken, die im dynamischen, grauen Feld Segmentstatistik aufgeführt sind. Von hier aus können Sie schnell das Tool Segment Insights starten, um dieses bestimmte Segment mit allen anderen zu vergleichen, die Sie zuvor eingerichtet haben. Beachten Sie jedoch, dass dadurch alle Segmente überschrieben werden, die Sie zuvor im Tool Segment Insights ausgewählt haben.

![][3]

## Anwendungsfälle {#insights-use-cases}

### Vergleich der demografischen Nutzungs- und Kaufmuster

Einer der besten Einsatzbereiche von Segment-Insights ist die Beantwortung von Fragen zu den Auswirkungen von Nutzer:innen auf die Nutzung von Apps und die Effektivität von Kampagnen, z. B:

- Sind bestimmte Nutzerdemografien deutlich besser oder schlechter als der Durchschnitt?
- Sollte ich die Lokalisierung einer bestimmten Kampagne noch einmal überdenken?
- Spricht eine Kampagne eine bestimmte Bevölkerungsgruppe an?
- Welche Ziele sollte ich mir für eine Kampagne setzen, die sich an eine bestimmte Bevölkerungsgruppe richtet?

Segment-Insights können helfen, Unterschiede zwischen Nutzer:innen aufzudecken. Das folgende Beispiel zeigt einen Vergleich der Nutzerbasis einer App nach Sprache. Es veranschaulicht, dass Englischsprachige tendenziell einen höheren LTV und ein höheres Aktivitätsniveau haben als Sprecher anderer Sprachen.

![][5]

In diesem Beispiel haben sich die deutschsprachigen Nutzer im Durchschnitt vor längerer Zeit angemeldet, was erklären könnte, warum sie nicht mehr so aktiv sind. Dies könnte auf eine Vielzahl von Faktoren zurückzuführen sein. Zum Beispiel, wenn die App zuerst in Europa eingeführt wurde, aber jetzt in den USA beliebter ist, wo die meisten Menschen Englisch oder Spanisch sprechen. Um solidere Ergebnisse zu erhalten, ist es sinnvoll, bei der Analyse von KPIs nach demografischen Gesichtspunkten die Ergebnisse einer allgemeinen Studie über demografische Merkmale zu testen (z. B. ob sich die Sprache bei allen Nutzern auf den LTV auswirkt), indem man eine kleinere, ähnlichere Population betrachtet und prüft, ob die Ergebnisse bestehen bleiben.

Um die Konversionsrate bei Sprechern anderer Sprachen als Englisch zu verbessern, wäre ein guter erster Schritt die [Lokalisierung von Kampagnen][10] auf die Gerätesprache des Benutzers und die Sicherstellung, dass die Texte dieser Nachrichten die Benutzer ansprechen, indem eine [multivariate Kampagne][11] verwendet wird, um verschiedene Versionen der fremdsprachigen Texte zu testen.

### Indikatoren für höhere Einnahmen verstehen

Es kann schwierig sein, Nutzer:innen zu Käufern und Käuferinnen umzuwandeln, und der Versuch, neue, inaktive oder uninteressierte Nutzer:innen direkt zum Kauf zu drängen, kann dazu führen, dass sie Ihre App deinstallieren. Segment-Insights können Ihnen helfen, Aktionen zu entdecken, die Nutzer:innen weiter in den Funnel führen, ohne dass sie gleich kaufen müssen, z. B. das Hinzufügen von Artikeln zu ihrer Wunschliste, das Teilen in Social Media oder das Favorisieren von Content. So können Sie zum Beispiel die Auswirkungen verschiedener Verhaltensweisen innerhalb einer E-Commerce App auf die Käufe in einem Chart darstellen.

![][7]

In diesem Fall sind derzeit relativ wenige Nutzer:innen für den Newsletter registriert, aber diese Nutzer:innen sind im Allgemeinen aktiver. Um das Interesse neuer Nutzer:innen aufrechtzuerhalten, wäre es eine gute Idee, in Onboarding Kampagnen eine Einladung zur Bestellung des Newsletters einzubauen. Um ehemalige Nutzer:innen erneut zu gewinnen, wäre es ein guter Plan, eine typische [Kampagne für ehemalige Nutzer:innen][9] zu versenden und die Zielgruppe [Nutzer:innen, die konvertiert sind][12] mit einer nachfolgenden Kampagne zusammenzustellen, um sich für den Newsletter zu registrieren.

[1]: {% image_buster /assets/img_archive/segment_insights.png %}
[2]: {% image_buster /assets/img_archive/Segment_Insights_Info.png %}
[3]: {% image_buster /assets/img_archive/Segment_Segment_Insights.png %}
[5]: {% image_buster /assets/img_archive/Segment_Language_Insights.png %}
[7]: {% image_buster /assets/img_archive/Segment_Insights_Events1.png %}
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
[10]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[11]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#creating-tests
[12]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter
