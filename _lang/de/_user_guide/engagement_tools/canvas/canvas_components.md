---
nav_title: Canvas-Komponenten
article_title: Canvas Komponenten
page_order: 2
alias: "/user_guide/engagement_tools/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "Canvas Komponenten"
guide_top_text: "Verbessern Sie Ihre Canvas-Reise mit Canvas-Komponenten. Canvas-Komponenten können verwendet werden, um den Prozess der Bestimmung der Effektivität Ihres Canvas zu vereinfachen, indem übermäßig viele Schritte durch nur einen ersetzt werden. Komponenten in Canvas beziehen sich auf die personalisierte Benutzerreise in Ihren Canvas-Zweigen."

page_type: landing
description: "Auf dieser Landing Page finden Sie Artikel zu Canvas-Komponenten, die Ihnen bei der Erstellung fortgeschrittener Canvases helfen. Einige dieser Komponenten sind der Nachrichtenschritt, der Verzögerungs-Schritt, der Decision-Split-Schritt und mehr."
tool: Canvas

guide_featured_title: "Abschnittsartikel"
guide_featured_list:
  - name: Nachrichtenschritt
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/message_step/
    image: /assets/img/braze_icons/message-square-02.svg
  - name: Delay-Schritt
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/delay_step/
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: Decision-Split-Schritt
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/decision_split/
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: Zielgruppenpfad-Schritt
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/audience_paths/
    image: /assets/img/braze_icons/users-01.svg 
  - name: Aktionspfadschritt  
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/action_paths/
    image: /assets/img/braze_icons/zap.svg
  - name: Experimentpfad-Schritt
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/experiment_step/
    image: /assets/img/braze_icons/columns-01.svg
  - name: Nutzeraktualisierungs-Schritt
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/user_update/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: Feature-Flags im Canvas
    link: /docs/developer_guide/feature_flags/canvas/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: Canvas-Zielgruppensynchronisierung
    link: /docs/partners/canvas_audience_sync/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
---

## Über Canvas-Komponenten

Mit Canvas-Komponenten können Sie neue Nutzer:innen ansprechen, um Ihren Prozess zu verbessern und die Effektivität Ihrer Zielgruppe zu erhöhen.

### Anpassen von Customer Journeys

![Beispiel einer Canvas-Benutzer:in mit einem Decision-Split-Schritt, gefolgt von Verzögerungsschritten und Nachrichten-Schritten.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

Verwenden Sie [Aktionspfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths), um Ihre Nutzer:innen auf der Grundlage von Aktionen und Engagement-Events, wie z. B. einem Kauf, aufzuteilen. Wenn Sie Ihre Zielgruppen filtern und gezielt ansprechen möchten, vereinfachen [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) Ihr User-Targeting, indem Sie Ihre Benutzer auf der Grundlage von Zielgruppenkriterien auf verschiedene Canvas-Pfade schicken.

[Decision Split-Komponenten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) verwenden eine einfache "Ja oder Nein"-Logik, um zwei sich gegenseitig ausschließende Pfade für Ihre User Journeys zu erstellen, die auf einer Aktion oder einem Benutzerattribut basieren. So können Sie Ihre Benutzergruppen identifizieren und gezielt ansprechen.

Mit [Verzögerungskomponenten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step) können Sie einen einzelnen Schritt in Ihrem Canvas verzögern. Dieser eigenständige Verzögerungsschritt in Ihrem Canvas eignet sich am besten für die Übermittlung von Nachrichten an Ihre Benutzer zu einem bestimmten Zeitpunkt. Darüber hinaus können Verzögerungskomponenten auch die Reichweite Ihrer Zielgruppe erhöhen, indem Sie ihr mehr Zeit geben, die Kriterien der Komponente zu erfüllen.

### Testen

Bei der Erstellung Ihrer Nutzer:innen sollten Sie auch testen, welcher Canvas-Pfad am effektivsten ist. Mit [Experimentpfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step) können Sie in jedem Schritt mehrere Canvas-Pfade testen. Sie können die Verbindungen zwischen den Schritten auch als Vorschau auf hoher Ebene verwenden. Orangefarbene Verbindungen zeigen an, dass der vorherige Schritt die Nutzer:innen sofort zum nächsten Schritt voranbringt.

### Integration

Möchten Sie mit den First-Party-Nutzerdaten Ihrer Marke synchronisieren? Nutzen Sie die verfügbaren Synchronisationsoptionen für [Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) und [Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).

