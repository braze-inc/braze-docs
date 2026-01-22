---
nav_title: Status
article_title: Kampagnen- und Canvas-Status
page_order: 1
description: "Lernen Sie die Status für Kampagnen und Canvase kennen und wie Sie sie im Dashboard verwenden können."
tool:
    - Campaigns
    - Canvas
---

# Kampagnen- und Canvas-Status

> Erfahren Sie mehr über Status für Kampagnen und Canvase und wie Sie sie im Dashboard verwenden können.

## Nach Status filtern

Um Ihre Kampagnen oder Canvase nach Status zu filtern, wählen Sie **Alle Status** und dann einen Status aus.

\![Das Dropdown-Menü 'Alle Status' im Braze-Dashboard.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Ändern des Status

Um den Status einer Kampagne oder eines Canvas zu ändern, wählen Sie das Menü <i class="fas fa-ellipsis-vertical"></i> und dann einen Status aus.

\![Eine Liste der Canvase im Braze-Dashboard, wobei das Menü für eine der Canvase geöffnet ist.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## Verfügbare Stati

Dies sind die verfügbaren Status für Kampagnen und Canvase:

| Status | Beschreibung |
| --- | --- |
| Aktiv | Aktive Kampagnen und Canvase werden gerade versendet. Standardmäßig sehen Sie aktive Kampagnen und Canvase auf den jeweiligen Seiten. |
| Entwurf | Entwürfe von Kampagnen und Canvase werden gespeichert, aber nicht eingeführt. Um die Bearbeitung fortzusetzen und mit dem Senden zu beginnen, können Sie den Entwurf auswählen, indem Sie im Braze-Dashboard auf **Messaging** gehen und **Canvas** oder **Kampagnen** auswählen. |
| Archiviert | Archivierte Kampagnen und Canvase sind Nachrichten, die nicht mehr gesendet werden. Diese Kampagnen und Canvase werden auch aus den statistischen Diagrammen auf der Website entfernt. [**Startseite**]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard) und [**Umsätze**]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report) Seiten entfernt.|
| Angehalten | Angehaltene Kampagnen und Canvase werden pausiert, können aber weiterhin bearbeitet werden. Um fortzufahren, wählen Sie das Menü <i class="fas fa-ellipsis-vertical"></i> und dann **Fortsetzen**. Weitere Informationen finden Sie unter [Gestopptes Canvas-Verhalten](#stopped-canvas-behavior). |
| Ruhend | Wenn eine Kampagne oder ein Canvas keine Nachrichten mehr versendet, weist Braze ihr/ihm einen Leerlaufstatus zu, um die Sortierung und Verwaltung Ihrer Liste von Kampagnen und Canvase zu erleichtern. Sie können sehen, welche Kampagnen oder Canvase automatisch gestoppt werden und das zugehörige Stoppdatum. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Canvas Verhalten gestoppt {#stopped-canvas-behavior}

Wenn ein Canvas angehalten wird, geschieht Folgendes:

- **Geplante Nachrichten:** Ihre geplanten Nachrichten werden nicht versendet, unabhängig von der Position eines Nutzers:innen im Canvas. Dazu gehören auch Nutzer:innen, die aufgrund von Rate-Limiting in der Warteschlange standen.
- **E-Mails senden:** Der Versand von E-Mails wird möglicherweise nicht sofort eingestellt, da Ihr Dienstanbieter (ESP) Ihre bestehenden Anfragen weiter bearbeitet.
- **Verzögerungsstufen:** Nutzer:innen, die sich in einem [Verzögerungsschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) befinden, verbleiben dort wie gewohnt, verlassen den Canvas jedoch, wenn der festgelegte Zeitraum endet.

Um den Canvas wieder aufzunehmen, wählen Sie das Menü <i class="fas fa-ellipsis-vertical"></i> und dann **Fortsetzen**. Wenn Sie die Funktion reaktivieren, werden alle zuvor gestoppten Nachrichten wie geplant gesendet - sofern der Zeitplan nicht bereits abgelaufen ist.

## Bewährte Praktiken

### Überwachen Sie Ihre Nachrichten nach Status

Sie können Ihre Nachrichten nach Status überwachen, um die Details der Performance zu überprüfen. Wenn Sie z.B. eine Reihe aktiver Kampagnen haben, können Sie die Performance der einzelnen Kampagnen anhand ihrer Engagement-Metriken auswerten und bei Bedarf Anpassungen vornehmen. Wenn Sie stattdessen ein paar gestoppte Canvase haben, können Sie überlegen, ob Sie diese für Messaging wieder aufnehmen oder ganz archivieren sollten.

{% alert tip %}
Suchen Sie nach weiteren Möglichkeiten, organisiert zu bleiben? Fügen Sie [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags) hinzu, um auf einen Blick mehr Kontext zu erhalten.
{% endalert %}

### Prüfen Sie Ihre aktiven Nachrichten

Indem Sie Ihre aktiven Kampagnen und Canvase überprüfen, können Sie die Relevanz und Performance bewerten und veraltete Kampagnen und Canvase entfernen oder aktualisieren, um Ihr Messaging frisch zu halten.
