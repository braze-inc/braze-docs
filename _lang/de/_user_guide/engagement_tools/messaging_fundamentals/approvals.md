---
nav_title: Genehmigungen
article_title: Genehmigungen
page_order: 2
page_type: reference
description: "Dieser referenzierte Artikel gibt eine Übersicht über die verschiedenen Status, die eine Kampagne und Canvas haben können und was sie bedeuten."
tool:
    - Campaigns
    - Canvas
---

# Genehmigungen für Kampagnen und Canvase

> Der Genehmigungsprozess für Kampagnen und Canvase fügt Ihrem Workflow vor dem Start einen Überprüfungsprozess hinzu. Auf diese Weise können Sie überprüfen, ob jeder Abschnitt im Finale der Kampagne oder des Canvas-Editors genehmigt ist, um zu starten.

## Funktionsweise

Sie können die Details Ihrer Kampagne oder Ihres Canvas im letzten Schritt Ihres Editors überprüfen. Bei Kampagnen ist dies die **Zusammenfassung der Überprüfung**, bei Canvase die **Zusammenfassung**. 

Wenn Ihr Administrator den Genehmigungs-Workflow aktiviert hat, muss jeder Abschnitt der Zusammenfassung von einem Nutzer:innen mit den entsprechenden Rechten genehmigt werden, bevor die Nachricht gestartet werden kann. Der Standard-Status für jeden Abschnitt ist " **Pending Approval"**.

{% tabs %}
{% tab campaign %}
Um eine Kampagne einführen zu können, müssen Sie diese Schlüsselkomponenten genehmigen:

- **Nachrichten:** Dies ist die Nachricht der Kampagne.
- **Lieferung:** Dies ist die Art der Zustellung und bestimmt, wann die Nutzer:innen die Kampagne erhalten.
- **Zielgruppen:** Damit wird festgelegt, wer die Kampagne erhält.
- **Konversions-Events:** Dies ist die Metrik, die Sie für das Engagement und die Berichterstattung tracken.
{% endtab %}

{% tab canvas %}
Um ein Canvas zu starten, müssen Sie diese Schlüsselkomponenten genehmigen:

- **Konversions-Events:** Dies ist die Metrik, die Sie für das Engagement und die Berichterstattung tracken.
- **Zeitplan für den Eingang:** Dazu gehört die Art des Zeitplans für den Eingang und wann Nutzer:innen den Canvas betreten sollen.
- **Zielgruppen:** Damit legen Sie fest, wer dieses Canvas betreten wird.
- **Einstellungen senden:** Dies sind die Sendeoptionen für alle Schritte im Canvas. 
- **Canvas bauen:** Dies ist die Reise der Nutzer:innen von Canvas.
{% endtab %}
{% endtabs %}

## Einschalten des Genehmigungs-Workflows

Standardmäßig ist die Einstellung für den Genehmigungs-Workflow für Kampagnen und Canvase deaktiviert. Um dieses Feature zu aktivieren, gehen Sie zu **Einstellungen** > **Genehmigungs-Workflow** und wählen Sie das entsprechende Umschalten aus:
- **Genehmigungsworkflow für alle Kampagnen in [Ihrem Workspace] verwenden**
- **Genehmigungs-Workflow für alle Canvase in [Ihrem Workspace] verwenden**

{% alert important %}
Die Genehmigung von Kampagnen wird im Erstellungsworkflow für [API-Kampagnen]({{site.baseurl}}/api/api_campaigns) und [Transaktions-E-Mail-Kampagnen]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign) nicht unterstützt.
{% endalert %}

## Benutzerberechtigungen festlegen

Nachdem der Genehmigungs-Workflow aktiviert wurde, müssen Sie die Nutzer:innen des Dashboards dazu berechtigen, die Kampagnen und Canvase sofort zu genehmigen oder abzulehnen. Beide Berechtigungen können auch auf Workspaces oder [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) angewendet oder zu einem [Berechtigungssatz]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets) hinzugefügt werden.

{% tabs %}
{% tab campaign %}
Sie müssen über die [ Berechtigung "Kampagnen genehmigen und ablehnen"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) verfügen. Diese Berechtigung steuert, wer den Genehmigungsstatus einer Kampagne aktualisieren kann. Es ist möglich, Komponenten einer Kampagne selbst zu genehmigen.
{% endtab %}

{% tab canvas %}
Sie müssen über die [ Berechtigung "Canvase genehmigen und ablehnen"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) verfügen. Ein Benutzer mit dieser Berechtigung kann jede der folgenden Aktionen im Canvas-Workflow ausführen:

- Genehmigen Sie das Canvas, aber starten Sie es nicht
- Starten, aber nicht genehmigen des Canvas
- Genehmigen und starten Sie das Canvas
- Weder genehmigen noch starten Sie den Canvas

Nachdem der Genehmigungsstatus im Schritt **Zusammenfassung** festgelegt wurde, werden alle nachfolgenden Änderungen am Canvas beim Speichern alle Genehmigungsstatus zurückgesetzt. Dies gilt für alle Änderungen, die entweder in einem Entwurf des Canvas oder in einem Canvas nach dem Start vorgenommen werden. Wenn Sie zum Beispiel nur Änderungen an der Zielgruppe vornehmen, setzt der Schritt **Zusammenfassung** den Genehmigungsstatus für alle Abschnitte auf den Standardstatus "Ausstehend" zurück.
{% endtab %}
{% endtabs %}

{% alert important %}
Um eine Live-Kampagne zu bearbeiten, benötigen Sie die Berechtigung "Kampagnen genehmigen und ablehnen". Ein Benutzer muss seine Änderungen genehmigen, da eine Entwurfsversion von Kampagnen noch nicht verfügbar ist. Dies ist bei Canvases nicht der Fall, da ein Benutzer Änderungen vornehmen und als Entwurf speichern kann, und ein anderer Benutzer kann das Canvas genehmigen und starten.
{% endalert %}
