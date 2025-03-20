---
nav_title: Canvas-Zulassung und Berechtigungen
article_title: Canvas-Zulassung und Berechtigungen 
page_order: 0.5
alias: "/canvas_approval/"
description: "In diesem Referenzartikel erfahren Sie, wie Sie Canvase vor dem Start genehmigen können und welche Nutzer:innen dazu berechtigt sind."
tool: Canvas
---

# Canvas Genehmigung und Berechtigungen

> Die Canvas-Genehmigung fügt Ihrem Arbeitsablauf einen Überprüfungsprozess vor dem Start hinzu. Auf diese Weise können Sie überprüfen, ob jede Bestätigung genehmigt wurde, um das Canvas zu starten.

## Einschalten der Canvas-Freigabe

Um den Genehmigungsworkflow für Canvas zu aktivieren, gehen Sie zu **Einstellungen** > **Genehmigungsworkflow** unter **Arbeitsplatzeinstellungen**. In der Standardeinstellung ist diese Funktion ausgeschaltet.

![Die Einstellungen für den Genehmigungs-Workflow, in denen die Option zur Verwendung des Genehmigungs-Workflows für Kampagnen und Canvases aktiviert ist.][1]

{% alert tip %}
Vergewissern Sie sich, dass Sie über die richtigen [Nutzer]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions):innen verfügen, um Canvase zu genehmigen.
{% endalert %}

### Benutzerberechtigungen festlegen

Nachdem der Genehmigungs-Workflow für Canvas aktiviert wurde, gehen Sie zu **Einstellungen** > **Unternehmensbenutzer** und wählen Sie **Canvases genehmigen und ablehnen**, damit bestimmte Benutzer Canvases sofort genehmigen und ablehnen können. Diese Berechtigung kann auch auf Arbeitsbereiche oder [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) angewandt oder zu einer [Berechtigungsgruppe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets) hinzugefügt werden.

Ein Benutzer mit dieser Berechtigung kann jede der folgenden Aktionen im Canvas-Workflow ausführen:
- Genehmigen Sie das Canvas, aber starten Sie es nicht
- Starten, aber nicht genehmigen des Canvas
- Genehmigen und starten Sie das Canvas
- Weder genehmigen noch starten Sie den Canvas

![Ein Beispiel für ein nicht markiertes Kontrollkästchen für die Berechtigung Canvase genehmigen und ablehnen, d. h. dieser Nutzer:innen hat nicht die Berechtigung, Canvase zu genehmigen oder abzulehnen.][3]{: style="max-width:70%" }

{% alert important %}
Um eine Live-Kampagne zu bearbeiten, benötigen Sie die Berechtigung "Kampagnen genehmigen und ablehnen". Ein Benutzer muss seine Änderungen genehmigen, da eine Entwurfsversion von Kampagnen noch nicht verfügbar ist. Dies ist bei Canvases nicht der Fall, da ein Benutzer Änderungen vornehmen und als Entwurf speichern kann, und ein anderer Benutzer kann das Canvas genehmigen und starten.
{% endalert %}

## Genehmigungen verwenden

Wenn Sie die Berechtigung "Canvases genehmigen und ablehnen" besitzen, haben Sie Zugriff auf den Schritt **Zusammenfassung** des Canvas-Erstellers. Auf dieser Seite finden Sie eine Zusammenfassung der wichtigsten Canvas-Details mit der Möglichkeit, diese Details zu genehmigen oder abzulehnen, einschließlich Konversions-Events, Zeitplan für den Entry sowie Art und Anzahl der Komponenten in Ihrem Canvas. Beachten Sie, dass der Standardstatus für die Canvas-Genehmigung **Pending Approval** lautet.

Sobald der Genehmigungsstatus im Schritt **Zusammenfassung** festgelegt wurde, werden alle nachfolgenden Änderungen am Canvas beim Speichern alle Genehmigungsstatus zurückgesetzt. Dies gilt für alle Änderungen, die entweder in einem Entwurf des Canvas oder in einem Canvas nach dem Start vorgenommen werden. Wenn Sie zum Beispiel nur Änderungen an der Zielgruppe vornehmen, setzt der Schritt **Zusammenfassung** den Genehmigungsstatus für alle Abschnitte auf den Standardstatus "Ausstehend" zurück.

![Ein Beispiel für den Canvas-Genehmigungsworkflow, bei dem die Details der Konversions-Events und des Zeitplans für den Entry als genehmigt markiert wurden.][2]{: style="max-width:85%" }

Sobald jeder Abschnitt genehmigt ist, steht die Schaltfläche **Starten** zur Verfügung und Sie können Ihr Canvas starten.

[1]: {% image_buster /assets/img_archive/canvas_approval.png %}
[2]: {% image_buster /assets/img_archive/canvas_approval_summary.png %}
[3]: {% image_buster /assets/img_archive/canvas_approval_user_permissions.png %}