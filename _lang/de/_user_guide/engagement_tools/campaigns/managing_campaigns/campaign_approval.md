---
nav_title: Kampagnen genehmigen
article_title: Kampagnen genehmigen
alias: "/campaign_approval/"
page_order: 0
page_type: reference
description: "Diese Seite bietet einen Überblick über den Prozess der Kampagnengenehmigung."
tool: Campaigns
---

# Kampagnen genehmigen

> Die Kampagnengenehmigung fügt Ihrem Workflow einen Überprüfungsprozess hinzu, bevor eine Kampagne gestartet wird. Diese Funktion fügt Zustände hinzu, die im Workflow-Schritt der Kampagnenbestätigung verfügbar sind. Sie können sicherstellen, dass jede Bestätigung für den Start der Kampagne genehmigt wird.

{% alert important %}
Die Genehmigung von Kampagnen wird im Erstellungsworkflow für API-Kampagnen und Transaktions-E-Mail-Kampagnen nicht unterstützt.
{% endalert %}

## Zustimmung zur Kampagne aktivieren

In der Standardeinstellung ist die Kampagnengenehmigung deaktiviert. Um diese Funktion zu aktivieren, gehen Sie zu **Einstellungen** > **Genehmigungs-Workflow**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie diese Seite unter **Einstellungen verwalten** > **Genehmigungsworkflow**.
{% endalert %}

## Genehmigungen verwenden

Nachdem die Kampagnengenehmigung aktiviert wurde, benötigen Sie die Berechtigung „Kampagnen genehmigen und ablehnen“. Diese Berechtigung steuert, wer den Genehmigungsstatus einer Kampagne aktualisieren kann. Diese Berechtigung kann auch auf Arbeitsbereiche oder [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) angewandt oder zu einer [Berechtigungsgruppe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets) hinzugefügt werden.

Im Schritt **Zusammenfassung überprüfen** des Kampagnenerstellungs-Workflows verwenden Sie die Genehmigungsoption, um die wichtigsten Komponenten Ihrer Kampagne zu genehmigen oder abzulehnen: **Nachrichten**, **Zustellung**, **Zielgruppen** und **Konversion-Events**. Der Standardstatus für die Kampagnengenehmigung lautet **Genehmigung ausstehend**. Beachten Sie, dass es möglich ist, Komponenten einer Kampagne selbst zu genehmigen.

![][1]

Sobald jeder Abschnitt genehmigt ist, wird die Schaltfläche **Starten** aktiviert, und Sie können Ihre Kampagne starten! 

[1]: {% image_buster /assets/img_archive/campaign_approval_example.png %} 
