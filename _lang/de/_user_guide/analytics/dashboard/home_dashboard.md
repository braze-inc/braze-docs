---
nav_title: Home Dashboard
article_title: Home Dashboard (zuvor Übersicht)
page_order: 1
page_type: reference
description: "Dieser referenzierte Artikel beschreibt Ihr Home Dashboard und enthält Definitionen für die auf dieser Seite verfügbaren Statistiken."
tool: 
  - Reports

---

# Home Dashboard

> Auf der **Startseite** des Dashboards finden Sie die wichtigsten Metriken, mit denen Sie die Performance Ihrer App oder Website tracken und verstehen können, und Sie erhalten auf einen Blick einen Überblick über Ihre Nutzerbasis.

Die **Startseite** hat zwei Hauptbereiche:
- [Machen Sie dort weiter, wo Sie aufgehört haben.](#pick-up-where-you-left-off)
- [Performance-Übersicht](#peformance-overview)

![Home-Dashboard in Braze.]({% image_buster /assets/img_archive/home_dashboard.png %})

## Machen Sie dort weiter, wo Sie aufgehört haben.

Sie können dort weitermachen, wo Sie im Braze-Dashboard aufgehört haben, mit direktem Zugriff auf Dateien, die Sie kürzlich bearbeitet oder erstellt haben. Dieser Abschnitt erscheint oben auf der **Startseite** des Braze-Dashboards.

Sie können die zuletzt bearbeiteten oder erstellten Kampagnen, Canvase und Segmente erneut aufrufen. Jede Karte ist mit Tags versehen, die den Content-Typ (Kampagne, Canvas, Segment) und den Status (aktiv, Entwurf, archiviert, gestoppt) angeben.

{% alert note %}
Der Abschnitt **Weitermachen, wo Sie aufgehört haben** erscheint, nachdem Sie eine Kampagne, ein Canvas oder ein Segment erstellt oder bearbeitet haben.
{% endalert %}

![Ein Canvas-Entwurf, ein aktives Segment und ein Entwurf für eine Kampagne im Abschnitt "Weitermachen, wo Sie aufgehört haben".]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

## Performance-Übersicht

Standardmäßig zeigt die **Übersicht über die Performance** die Daten der letzten 30 Tage für alle Apps und Websites. Ihre Metriken werden alle auf der Grundlage des ausgewählten Datumsbereichs berechnet.

![Datumsbereich und App-Felder auf dem Home Dashboard.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

Die Prozentsätze werden auf der Grundlage des aktuellen Datumsbereichs im Vergleich zum vorherigen Datumsbereich berechnet, mit Ausnahme der *monatlich aktiven Nutzer*:in (MAU), die den letzten Tag des vorherigen Zeitraums anstelle eines Bereichs verwenden. 

Wenn Sie beispielsweise den Datumsbereich auf **Letzte 7 Tage** einstellen und Ihre *täglich aktiven Nutzer:innen* einen prozentualen Anstieg von 1,8% aufweisen, bedeutet dies, dass Sie in dieser Woche 1,8% mehr täglich aktive:r Nutzer:innen hatten als in der vergangenen Woche.

![]({% image_buster /assets/img_archive/home_dashboard_metric_tile.png %}){: style="max-width:60%;"}

### Aufschlüsselung anzeigen

Wählen Sie **Aufschlüsselung anzeigen** für jede Zeile der Performance-Übersichtsstatistik aus, um den Wert jeder Statistik pro Tag für den angegebenen Datumsbereich anzuzeigen.

![Erweitern]({% image_buster /assets/img_archive/home_dashboard_breakdown.png %})

## Verfügbare Statistiken

Im Folgenden finden Sie die Definitionen der Ihnen zur Verfügung stehenden Statistiken, wie wir sie berechnen und warum sie für Sie wichtig sein sollten.

### Nutzer:innen

*Nutzer:in* ist die Gesamtzahl der Nutzer:innen, die in diesem Workspace angelegt wurden. Dies schließt alle Nutzer:innen ein, die Ihre App oder Website zu einem bestimmten Zeitpunkt genutzt haben, und auch solche, die nicht mit einer bestimmten App oder Website in Verbindung gebracht werden können. Diese Zahl gibt an, wie viele Ihrer Lifetime-Nutzer als *monatlich aktive Nutzer*:innen (MAU) vertreten sind. Diese Zahl ist nützlich, um die Bindung der Nutzer:innen über einen längeren Zeitraum hinweg zu sehen.

Ein niedriges MAU-zu-Nutzer-Verhältnis kann darauf hinweisen, dass Sie Ihre Messaging-Kanäle diversifizieren oder Ihre Bemühungen verstärken müssen, um passive Nutzer:innen zu erreichen. Weitere Informationen finden Sie in unserem Quick Win zur [Erfassung von passiven Nutzer:innen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users). Im Allgemeinen wird das Verhältnis von MAU zu Lifetime im Laufe der Zeit unweigerlich sinken, weil Nutzer:innen abwandern. Mit den Tools von Braze können Sie diesen Effekt jedoch minimieren, indem Sie die Nutzer:innen länger binden.

### Lifetime-Sitzungen

*Lifetime-Sitzungen* ist die Gesamtzahl der Sitzungen, die Braze seit der Integration aufgezeichnet hat. Einfach ausgedrückt: Eine Sitzung findet jedes Mal statt, wenn ein Nutzer:innen die App verwendet oder Ihre Website besucht. Eine genauere Definition, wie Sitzungen nach Plattform definiert werden, finden Sie in der entsprechenden
[iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Android und FireOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), oder [Internet]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web) Session Tracking Entwickler:in Artikel.

### Monatlich aktive Nutzer:innen

*Monatlich aktive Nutzer:* in (MAU) ist die Anzahl der Nutzer:innen, die in den letzten 30 Tagen eine Sitzung in Ihrer App oder Website aufgezeichnet haben. MAU werden nachts mit einem rollenden 30-Tage-Fenster berechnet. MAU bietet Ihnen ein gutes Verständnis für den Zustand einer App oder Website über einen längeren Zeitraum, da es die Unstimmigkeiten zwischen Tagen mit unterschiedlicher Nutzungsintensität ausgleicht.

Der Prozentsatz neben der MAU-Zahl zeigt die Veränderung der MAU für diesen Zeitraum im Vergleich zum vorherigen Zeitraum.

$$\text{Change in MAU} = \frac{\text{MAU of last date in range} - \text{MAU of day before start date}}{\text{MAU of day before start date}}$$

{% alert note %}
Anonyme Nutzer:innen zählen ebenfalls zu Ihren MAU. Bei mobilen Geräten sind anonyme Nutzer:innen geräteabhängig. Für Internet-Nutzer:innen sind anonyme Nutzer:innen vom Browser-Cache abhängig.
{% endalert %}

### Täglich aktive Nutzer:innen

*Täglich aktive Nutzer*:in (DAU) zeigt die Anzahl eindeutiger Nutzer:innen an, die an einem bestimmten Tag mindestens eine Sitzung in Ihrer App oder Website aufzeichnen. DAU kann eine nützliche Statistik sein, um die täglichen Schwankungen bei der Nutzung Ihrer App oder Website zu untersuchen und Ihre Messaging-Kampagnen so effektiv wie möglich zu gestalten. Zum Beispiel kann die Nutzung Ihrer App an Wochenenden deutlich ansteigen. Das würde Ihnen zeigen, dass Sie an diesen Tagen mehr Nutzer:innen mit In-App-Nachrichten erreichen können als an Wochentagen.

### Neue Nutzer:innen

*Neue Nutzer:innen* zeigt Ihnen, wie viele Nutzer:innen, die noch nie eine Sitzung aufgezeichnet haben, nun Ihre App oder Website nutzen. Diese Zahl ist die Gesamtzahl der neuen Nutzer:innen in dem angegebenen Zeitraum. Diese Statistik kann für das Tracking der Effektivität Ihrer Werbemaßnahmen sehr wertvoll sein.

{% alert note %}
Wenn Sie Braze zum ersten Mal integrieren, sehen alle Nutzer:innen wie neue Nutzer:innen aus, da Braze noch nie eine Sitzung für sie aufgezeichnet hat.
{% endalert %}

### Kundenbindung

Der *Stickiness-Wert* ist ein Verhältnis zwischen DAU und MAU einer bestimmten Periode. Im Wesentlichen misst die Stickiness den Prozentsatz Ihrer MAU, die täglich wiederkommen.

Wenn der Datumsbereich beispielsweise auf 30 Tage festgelegt ist, bedeutet ein Verhältnis von 50 %, dass ein aktiver Nutzer:innen die App oder Website im Durchschnitt 15 von 30 Tagen nutzt oder dass etwa die Hälfte Ihrer aktiven Nutzer:innen täglich wiederkommt. Stickiness ist eine wichtige Metrik für den Erfolg, denn die meisten Nutzer:innen hören nicht auf, eine App zu benutzen, weil sie sie aktiv hassen, sondern weil sie nicht Teil ihrer täglichen Routine geworden ist. Daher können Sie die Klebrigkeit als Indikator dafür verwenden, wie gut Sie Ihre Nutzer:innen einbinden.

Der Prozentsatz neben dem Klebrigkeitsverhältnis zeigt die Veränderung der Klebrigkeit in diesem Zeitraum im Vergleich zum vorherigen Zeitraum.

$$\text{Change in stickiness} = \frac{\text{Stickiness of last period} - \text{Stickiness of this period}}{\text{Stickiness of last period}}$$

Die Zeitrahmen für "letzter Zeitraum" und "dieser Zeitraum" werden durch den von Ihnen ausgewählten Datumsbereich bestimmt.

{% alert important %}
Der MAU-Wert wird jede Nacht berechnet und erst am nächsten Tag aktualisiert.
{% endalert %}

### Tägliche Sitzungen

*Tägliche Sitzungen* ist die Anzahl der Sitzungen, die an einem bestimmten Tag aufgezeichnet wurden. Wenn Sie diesen Wert mit Ihrer DAU-Zahl vergleichen, können Sie feststellen, wie oft Ihre Nutzer:innen die App öffnen oder Ihre Website an Tagen besuchen, an denen sie mindestens eine Sitzung aufzeichnen.

### Tägliche Sitzungen pro MAU

*Tägliche Sitzungen pro MAU* ist das Verhältnis von *täglichen Sitzungen* zu MAU an einem bestimmten Tag. Diese Statistik zeigt Ihnen, wie viele Sitzungen Sie pro Tag und MAU erwarten können. Zusammengefasst und gemittelt können Sie so eine Idee davon bekommen, wie häufig Ihre Nutzer:innen Ihre App oder Website verwenden. Das heißt, wenn Ihre *täglichen Sitzungen pro MAU* im Durchschnitt 0,5 betragen, können Sie davon ausgehen, dass jede MAU etwa alle 2 Tage eine Sitzung aufzeichnet.  

