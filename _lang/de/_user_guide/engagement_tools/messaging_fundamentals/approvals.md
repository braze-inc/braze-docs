---
nav_title: Genehmigungen
article_title: Genehmigungen
page_order: 1
page_type: reference
description: "Dieser referenzierte Artikel gibt eine Übersicht über die verschiedenen Status, die eine Kampagne und Canvas haben können und was sie bedeuten."
tool:
    - Campaigns
    - Canvas
---

# Genehmigungen für Kampagnen und Canvase

> Verwenden Sie Genehmigungen, um Ihren Kampagnen und Canvase vor dem Start einen letzten Kontrollpunkt hinzuzufügen. Mit diesem Workflow können Sie den Inhalt in allen erforderlichen Abschnitten Ihrer Nachricht überprüfen und genehmigen.

## Funktionsweise

Sie können die Details Ihrer Kampagne oder Ihres Canvas im letzten Schritt der Bearbeitung überprüfen. 

Sowohl bei Canvase als auch bei Kampagnen müssen Sie alle Änderungen vor der Freigabe speichern, auch wenn es sich um Ihre eigenen Änderungen handelt. Ein Nutzer:innen mit den entsprechenden Rechten muss jeden Abschnitt der Zusammenfassung genehmigen, bevor die Nachricht gestartet werden kann. Der Standard-Status für jeden Abschnitt ist " **Pending Approval"**.

{% tabs %}
{% tab campaign %}
Um eine Kampagne einzuführen, müssen Sie diese Komponenten genehmigen:

- **Nachrichten:** Dies ist die Nachricht der Kampagne.
- **Lieferung:** Dies ist die Art der Zustellung und bestimmt, wann Nutzer:innen die Kampagne erhalten.
- **Zielgruppen:** Damit wird festgelegt, wer die Kampagne erhält.
- **Konversions-Events:** Dies ist die Metrik, die Sie für das Engagement und die Berichterstattung tracken.
{% endtab %}

{% tab canvas %}
Um ein Canvas zu starten, müssen Sie diese Schlüsselkomponenten genehmigen:

- **Konversions-Events:** Dies ist die Metrik, die Sie für das Engagement und die Berichterstattung tracken.
- **Zeitplan für den Eingang:** Dazu gehört die Art des Zeitplans für den Eingang und wann Nutzer:innen den Canvas betreten.
- **Zielgruppen:** Damit legen Sie fest, wer dieses Canvas betreten wird.
- **Einstellungen senden:** Dies sind die Sendeoptionen für alle Schritte im Canvas. 
- **Canvas bauen:** Dies ist die Reise der Nutzer:innen von Canvas.
{% endtab %}
{% endtabs %}

## Einschalten des Genehmigungs-Workflows

Standardmäßig ist der Genehmigungs-Workflow für Kampagnen und Canvase deaktiviert. Um dieses Feature zu aktivieren, gehen Sie zu **Einstellungen** > **Genehmigungs-Workflow** und wählen Sie das entsprechende Umschalten aus:

- **Genehmigungsworkflow für alle Kampagnen in [Ihrem Workspace] verwenden**
- **Genehmigungs-Workflow für alle Canvase in [Ihrem Workspace] verwenden**

{% alert important %}
Die Genehmigung von Kampagnen wird für [API-Kampagnen]({{site.baseurl}}/api/api_campaigns) und [Transaktions-E-Mail-Kampagnen]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign) nicht unterstützt.
{% endalert %}

## Benutzerberechtigungen festlegen

Nachdem Sie den Genehmigungs-Workflow aktiviert haben, müssen Sie die Nutzer:innen Ihres Unternehmens dazu berechtigen, Kampagnen und Canvase zu genehmigen oder abzulehnen. Beide Berechtigungen können auch auf Workspaces oder [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) angewendet oder zu einem [Berechtigungssatz]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets) hinzugefügt werden.

{% tabs %}
{% tab campaign %}
Sie müssen über die [ Berechtigung "Kampagnen genehmigen und ablehnen"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) verfügen. Diese Berechtigung steuert, wer den Genehmigungsstatus einer Kampagne aktualisieren kann. Mit dieser Genehmigung können Sie Folgendes tun:

- Die Kampagne selbst genehmigen
- Genehmigen Sie die Kampagne und starten Sie sie
- Genehmigen Sie die Kampagne, aber starten Sie sie nicht (ein anderer Nutzer:innen mit der Berechtigung "Kampagnen, Canvase senden" kann die Kampagne starten)
- Die Kampagne weder genehmigen noch einführen

Nachdem der Genehmigungsstatus im Schritt **Zusammenfassung** festgelegt wurde, setzen alle nachfolgenden Änderungen an der Kampagne beim Speichern alle Genehmigungsstatus zurück. Dies gilt für alle Änderungen, die entweder in einem Kampagnenentwurf oder in einer nach dem Start der Kampagne durchgeführten Kampagne vorgenommen werden. Wenn Sie beispielsweise nur Änderungen an der Zielgruppe vornehmen, setzt der Schritt **Zusammenfassung** den Genehmigungsstatus für alle Abschnitte auf den Standardstatus " **Ausstehend"** zurück.

{% endtab %}

{% tab canvas %}
Sie müssen über die [ Berechtigung "Canvase genehmigen und ablehnen"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) verfügen. Diese Berechtigung steuert, wer den Genehmigungsstatus eines Canvas aktualisieren darf. Mit dieser Genehmigung können Sie Folgendes tun:

- Das Canvas selbst freigeben
- Genehmigen und starten Sie das Canvas
- Genehmigen Sie das Canvas, aber starten Sie es nicht (ein anderer Nutzer:innen mit der Berechtigung "Kampagnen, Canvase senden" kann das Canvas starten)
- Weder genehmigen noch starten Sie den Canvas

Nachdem der Genehmigungsstatus im Schritt **Zusammenfassung** festgelegt wurde, setzen alle nachfolgenden Änderungen am Canvas beim Speichern alle Genehmigungsstatus zurück. Dies gilt für alle Änderungen, die entweder in einem Entwurf des Canvas oder in einem Canvas nach dem Start vorgenommen werden. Wenn Sie beispielsweise nur Änderungen an der Zielgruppe vornehmen, setzt der Schritt **Zusammenfassung** den Genehmigungsstatus für alle Abschnitte auf den Standardstatus " **Ausstehend"** zurück.

{% alert note %}
**Genehmigungsstatus und Speichern**

- Wenn Sie im Schritt **Zusammenfassung** auf **Genehmigen** für einen Abschnitt klicken, wird diese Genehmigung sofort gespeichert.
- Der Button **Speichern** speichert Änderungen am Canvas-Inhalt und den Einstellungen, nicht aber den Genehmigungsstatus.

Um den Verlust von Genehmigungen zu vermeiden:

1. Nehmen Sie alle erforderlichen Canvas-Bearbeitungen vor und klicken Sie dann auf **Speichern**.
2. Nachdem der Canvas gespeichert wurde, genehmigen Sie die entsprechenden Abschnitte im Schritt **Zusammenfassung**.
3. Klicken Sie nur dann erneut auf **Speichern**, wenn Sie nach der Genehmigung weitere Änderungen am Canvas vornehmen. Wenn Sie den Canvas ändern und speichern, werden alle Genehmigungsstatus auf **Ausstehende Genehmigung** zurückgesetzt.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
Um eine Live-Kampagne zu bearbeiten, benötigen Sie die Berechtigung "Kampagnen genehmigen und ablehnen". Ein Nutzer:innen muss seine Änderungen genehmigen, da eine Entwurfsversion von Kampagnen noch nicht verfügbar ist. Dies ist bei Canvases nicht der Fall, da ein Benutzer Änderungen vornehmen und als Entwurf speichern kann, und ein anderer Benutzer kann das Canvas genehmigen und starten.
{% endalert %}