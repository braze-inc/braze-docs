---
nav_title: Segment-Insights
article_title: Segment-Insights
page_order: 8
page_type: tutorial
tool: 
  - Segments
  - Reports
description: "In diesem Artikel erfahren Sie, wie Sie Segment-Insights verwenden, interpretieren und weitergeben können."
---

# [![Braze Lernkurse]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"} Segmente Insights

> Lernen Sie, wie Sie Segment-Insights verwenden, interpretieren und weitergeben können. 

Segment Insights zeigt Ihnen, wie sich ein Segment im Vergleich zu einem anderen in einer Reihe von vorher ausgewählten KPIs verhält.

## Segmenteinblicke anzeigen

Gehen Sie auf die Seite **Segment-Insights** auf Ihrem Dashboard unter **Analytics**, um bis zu 10 verschiedene Segmente im Vergleich zu einer Baseline zu sehen.

![Segment-Insights Dashboard, das die drei Segmente "Nutzer:innen aus Großbritannien", "Nutzer:innen aus Frankreich" und "Nutzer:innen aus Kanada" mit einem Basissegment "Alle Nutzer:innen" vergleicht.]({% image_buster /assets/img_archive/segment_insights.png %})

Das Basissegment kann entweder ein bestimmtes Segment sein, das Sie auswählen, oder ein Segment, das alle Ihre Nutzer enthält. Sie können die folgenden Statistiken mit Segment Insights vergleichen:

| Messung | Beschreibung | Formel |
| --------------------- | ------------- | ------------- |
| Sitzungen pro Tag | Durchschnittliche Anzahl der Sitzungen der Segmentbenutzer pro Tag | (Gesamtzahl der Sitzungen) / (Anzahl der Tage seit der ersten Sitzung) |
| Tage seit erster Sitzung | Durchschnittliche Anzahl von Tagen zwischen der ersten Sitzung der Nutzer:innen des Segments und jetzt | heute – Datum der ersten Sitzung |
| Tage seit letzter Sitzung | Durchschnittliche Anzahl von Tagen zwischen der letzten Sitzung der Nutzer:innen des Segments und jetzt | heute – Datum der letzten Sitzung |
| Lifetime-Umsatz in Dollar | Durchschnittlicher Lifetime-Umsatz in Dollar für Nutzer:innen des Segments | Nutzerausgaben über die gesamte Lifetime |
| Tage seit erstem Kauf | Durchschnittliche Anzahl von Tagen zwischen der ersten Sitzung der Nutzer:innen des Segments und dem ersten Kauf | Datum des ersten Kaufs – Datum der ersten Sitzung |
| Tage seit letztem Kauf | Durchschnittliche Anzahl von Tagen zwischen dem letzten Kauf der Nutzer:innen des Segments und jetzt | heute - Datum des letzten Kaufs |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Über die eindeutige URL der Seite können Sie bestimmte Vergleiche ganz einfach mit Ihren Teamkollegen teilen. Außerdem können Sie das Augensymbol neben jedem Segment auswählen, um weitere Informationen über dieses Segment zu erhalten. Diese Vergleiche werden zurückgesetzt, wenn Sie zwischen Workspaces wechseln.

![Details für das Segment "Premium Nutzer:innen (iOS VideoApp)" mit einem Diagramm, das die historischen Mitgliederzahlen anzeigt, und einem Chart, das die geschätzte Größe für verschiedene Messaging-Kanäle aufschlüsselt.]({% image_buster /assets/img_archive/Segment_Insights_Info.png %}){: style="max-width:50%;"}

## Segment Details Seite

Die Segmenteinblicke wurden auch direkt in die Ansicht **Segmentdetails** integriert. Wenn Sie sich ein bestimmtes Segment ansehen, das Sie zuvor eingerichtet haben, finden Sie dieselben sechs Statistiken, die im dynamischen, grauen Feld Segmentstatistik aufgeführt sind. Von hier aus können Sie schnell das Tool Segment Insights starten, um dieses bestimmte Segment mit allen anderen zu vergleichen, die Sie zuvor eingerichtet haben. Beachten Sie jedoch, dass dadurch alle Segmente überschrieben werden, die Sie zuvor im Tool Segment Insights ausgewählt haben.

![]({% image_buster /assets/img_archive/Segment_Segment_Insights.png %})

## Anwendungsfälle {#insights-use-cases}

### Vergleich der demografischen Nutzungs- und Kaufmuster

Einer der besten Einsatzbereiche von Segment-Insights ist die Beantwortung von Fragen zu den Auswirkungen von Nutzer:innen auf die Nutzung von Apps und die Effektivität von Kampagnen, z. B:

- Sind bestimmte Nutzerdemografien deutlich besser oder schlechter als der Durchschnitt?
- Sollte ich die Lokalisierung einer bestimmten Kampagne noch einmal überdenken?
- Spricht eine Kampagne eine bestimmte Bevölkerungsgruppe an?
- Welche Ziele sollte ich mir für eine Kampagne setzen, die sich an eine bestimmte Bevölkerungsgruppe richtet?

Segment-Insights können helfen, Unterschiede zwischen Nutzer:innen aufzudecken. Das folgende Beispiel zeigt einen Vergleich der Nutzerbasis einer App nach Sprache. Es veranschaulicht, dass Englischsprachige tendenziell einen höheren LTV und ein höheres Aktivitätsniveau haben als Sprecher anderer Sprachen.

![Segment-Insights Aufschlüsselung für die Segmente Englisch, Deutsch, Französisch und Spanisch.]({% image_buster /assets/img_archive/Segment_Language_Insights.png %})

In diesem Beispiel haben sich die deutschsprachigen Nutzer im Durchschnitt vor längerer Zeit angemeldet, was erklären könnte, warum sie nicht mehr so aktiv sind. Dies könnte auf eine Vielzahl von Faktoren zurückzuführen sein. Zum Beispiel, wenn die App zuerst in Europa eingeführt wurde, aber jetzt in den USA beliebter ist, wo die meisten Menschen Englisch oder Spanisch sprechen. Um solidere Ergebnisse zu erhalten, ist es sinnvoll, bei der Analyse von KPIs nach demografischen Gesichtspunkten die Ergebnisse einer allgemeinen Studie über demografische Merkmale zu testen (z. B. ob sich die Sprache bei allen Nutzern auf den LTV auswirkt), indem man eine kleinere, ähnlichere Population betrachtet und prüft, ob die Ergebnisse bestehen bleiben.

Um die Konversionen bei Sprechern anderer Sprachen als Englisch zu verbessern, wäre es ein guter erster Schritt, Kampagnen auf die Sprache des Geräts des Nutzers [zu lokalisieren]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) und sicherzustellen, dass die Texte dieser Nachrichten die Nutzer:innen ansprechen, indem Sie eine [multivariate Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#creating-tests) durchführen, um verschiedene Versionen der fremdsprachigen Texte zu testen.

### Indikatoren für höhere Einnahmen verstehen

Es kann schwierig sein, Nutzer:innen zu Käufern und Käuferinnen umzuwandeln, und der Versuch, neue, inaktive oder uninteressierte Nutzer:innen direkt zum Kauf zu drängen, kann dazu führen, dass sie Ihre App deinstallieren. Segment-Insights können Ihnen helfen, Aktionen zu entdecken, die Nutzer:innen weiter in den Funnel führen, ohne dass sie gleich kaufen müssen, z.B. das Abonnieren Ihres Newsletters, das Teilen in Social Media oder das Abonnieren von Nachrichten zu Werbezwecken. So können Sie zum Beispiel die Auswirkungen verschiedener Verhaltensweisen innerhalb einer E-Commerce App auf die Käufe in einem Chart darstellen.

Segment-Insights Aufschlüsselung für Nutzer:innen, die in Social Media geteilt, sich für Aktionen registriert und sich für den Newsletter angemeldet haben.]({% image_buster /assets/img_archive/Segment_Insights_Events1.png %})

In diesem Fall sind relativ wenige Nutzer:innen für Nachrichten zu Werbezwecken registriert und nicht so aktiv, aber diese Nutzer:innen generieren einen höheren Lifetime-Umsatz. Um den Umsatz zu steigern, kann es eine gute Idee sein, in Onboarding-Kampagnen eine Einladung zur Registrierung für Werbenachrichten aufzunehmen. Um verfallene Nutzer:innen wieder zu engagieren, bietet es sich an, eine typische [Kampagne für verfallene Nutzer:innen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) zu versenden und die [Nutzer:innen, die konvertiert sind]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter), mit einer nachfolgenden Kampagne anzusprechen, damit sie sich für Werbebotschaften anmelden.

