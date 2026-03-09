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

> Nutzen Sie Freigaben, um Ihren Kampagnen und Canvases vor dem Start eine abschließende Kontrollinstanz hinzuzufügen. Mit diesem Arbeitsablauf können Sie den Inhalt in allen erforderlichen Abschnitten Ihrer Nachricht überprüfen und genehmigen.

## Funktionsweise

Im letzten Schritt der Bearbeitung können Sie die Details Ihrer Kampagne oder Ihres Canvas überprüfen. 

Sowohl bei Canvases als auch bei Kampagnen müssen Sie alle Änderungen vor der Freigabe speichern, auch wenn es sich um Ihre eigenen Änderungen handelt. Eine Nutzer:in mit den entsprechenden Berechtigungen muss jeden Abschnitt der Zusammenfassung genehmigen, bevor die Nachricht versendet werden kann. Der Standard-Status für jeden Abschnitt ist " **Pending Approval"**.

{% tabs %}
{% tab campaign %}
Um eine Kampagne zu starten, müssen Sie die folgenden Komponenten genehmigen:

- **Nachrichten:** Dies ist die Nachricht der Kampagne.
- **Lieferung:** Dies ist die Art der Zustellung und bestimmt, wann die Nutzer:innen die Kampagne erhalten.
- **Zielgruppen:** Dies bestimmt, wer die Kampagne erhalten wird.
- **Konversions-Events:** Dies ist die Metrik, die Sie für das Engagement und die Berichterstattung tracken.
{% endtab %}

{% tab canvas %}
Um ein Canvas zu starten, müssen Sie diese Schlüsselkomponenten genehmigen:

- **Konversions-Events:** Dies ist die Metrik, die Sie für das Engagement und die Berichterstattung tracken.
- **Zeitplan für den Eingang:** Dies umfasst die Art des Zeitplans für den Eingang und den Zeitpunkt, zu dem Nutzer:innen das Canvas betreten.
- **Zielgruppen:** Damit legen Sie fest, wer dieses Canvas betreten wird.
- **Einstellungen senden:** Dies sind die Sendeoptionen für alle Schritte im Canvas. 
- **Canvas bauen:** Dies ist die Reise der Nutzer:innen von Canvas.
{% endtab %}
{% endtabs %}

## Einschalten des Genehmigungs-Workflows

Standardmäßig ist die Genehmigungs-Workflow-Einstellung für Kampagnen und Canvases deaktiviert. Um dieses Feature zu aktivieren, gehen Sie zu **Einstellungen** > **Genehmigungs-Workflow** und wählen Sie das entsprechende Umschalten aus:

- **Bitte verwenden Sie den Genehmigungs-Workflow für alle Kampagnen in [Ihrem Workspace].**
- **Bitte verwenden Sie den Genehmigungs-Workflow für alle Canvases in [Ihrem Workspace].**

{% alert important %}
Die Genehmigung von Kampagnen wird für [API-Kampagnen]({{site.baseurl}}/api/api_campaigns) und [Transaktions-E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign) nicht unterstützt.
{% endalert %}

## Benutzerberechtigungen festlegen

Nachdem Sie den Genehmigungsworkflow aktiviert haben, müssen Sie Berechtigungen für Nutzer:innen festlegen, damit die Nutzer:innen Ihres Unternehmens Kampagnen und Canvases genehmigen oder ablehnen können. Beide Berechtigungen können auch auf Workspaces oder [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) angewendet oder zu einer [Berechtigungsgruppe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets) hinzugefügt werden.

{% tabs %}
{% tab campaign %}
Sie müssen über die [ Berechtigung "Kampagnen genehmigen und ablehnen"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) verfügen. Diese Berechtigung steuert, wer den Genehmigungsstatus einer Kampagne aktualisieren kann. Mit dieser Berechtigung können Sie Folgendes tun:

- Die Kampagne selbst genehmigen
- Die Kampagne genehmigen und starten
- Die Kampagne genehmigen, jedoch nicht starten (ein anderer Nutzer:in mit der Berechtigung „Kampagnen, Canvases senden“ kann die Kampagne starten).
- Die Kampagne weder genehmigen noch starten

Nachdem die Genehmigungsstatus im Schritt **„Zusammenfassung“** festgelegt wurden, werden alle nachfolgenden Änderungen an den Kampagnen beim Speichern alle Genehmigungsstatus zurücksetzen. Dies gilt für alle Änderungen, die entweder in einem Kampagnenentwurf oder in einer bereits gestarteten Kampagne vorgenommen werden. Wenn Sie beispielsweise nur Änderungen an den Zielgruppen vornehmen, werden im Schritt **„Zusammenfassung“** die Genehmigungsstatus für alle Abschnitte auf den Standardstatus **„Zur Genehmigung ausstehend**“ zurückgesetzt.

{% endtab %}

{% tab canvas %}
Sie müssen über die [ Berechtigung "Canvase genehmigen und ablehnen"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) verfügen. Diese Berechtigung regelt, wer den Genehmigungsstatus eines Canvas updaten darf. Mit dieser Berechtigung können Sie Folgendes tun:

- Die Canvas selbst genehmigen
- Genehmigen und starten Sie das Canvas
- Genehmigen Sie die Canvas, jedoch nicht starten (eine andere Nutzer:in mit der Berechtigung „Kampagnen, Canvases senden“ kann die Canvas starten).
- Bitte genehmigen Sie das Canvas nicht und starten Sie es auch nicht.

Nachdem die Genehmigungsstatus im Schritt **„Zusammenfassung“** festgelegt wurden, werden alle nachfolgenden Änderungen am Canvas beim Speichern alle Genehmigungsstatus zurücksetzen. Dies gilt für alle Änderungen, die entweder in einem Entwurf des Canvas oder in einem Canvas nach dem Start vorgenommen werden. Wenn Sie beispielsweise nur Änderungen an den Zielgruppen vornehmen, werden im Schritt **„Zusammenfassung“** die Genehmigungsstatus aller Abschnitte auf den Standardstatus **„Zur Genehmigung ausstehend**“ zurückgesetzt.

{% alert note %}
**Genehmigungsstatus und Speichern**

- Wenn Sie im Schritt **„Zusammenfassung“** einen Klick auf **„Genehmigen“** für einen Abschnitt machen, wird diese Genehmigung sofort gespeichert.
- Mit dem Button **„Speichern“** werden Änderungen am Canvas-Inhalt und an den Einstellungen gespeichert, nicht jedoch der Genehmigungsstatus.

Um den Verlust von Genehmigungen zu vermeiden:

1. Nehmen Sie die erforderlichen Änderungen in Canvas vor und klicken Sie anschließend auf **„Speichern**“.
2. Nachdem Canvas den Speichervorgang abgeschlossen hat, genehmigen Sie bitte die entsprechenden Abschnitte im Schritt **„Zusammenfassung**“.
3. Bitte klicken Sie nur dann erneut auf **„Speichern“,** wenn Sie nach der Genehmigung zusätzliche Änderungen an der Canvas vornehmen. Wenn Sie die Canvas ändern und speichern, werden alle Genehmigungsstatus auf **„Zur Genehmigung ausstehend“** zurückgesetzt.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
Um eine aktive Kampagne zu bearbeiten, benötigen Sie die Berechtigung „Kampagnen genehmigen und ablehnen“. Ein Nutzer:in muss seine Änderungen genehmigen, da noch keine Entwurfsversion von Kampagnen verfügbar ist. Dies ist bei Canvases nicht der Fall, da ein Benutzer Änderungen vornehmen und als Entwurf speichern kann, und ein anderer Benutzer kann das Canvas genehmigen und starten.
{% endalert %}