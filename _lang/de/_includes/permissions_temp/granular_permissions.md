{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

## Erstellen eines Berechtigungssatzes

Mit Berechtigungssätzen können Sie Berechtigungen für bestimmte Themenbereiche oder Aktionen bündeln. Sie können Berechtigungssätze auf Dashboard-Nutzer:innen anwenden, die in verschiedenen Workspaces denselben Zugriff benötigen. Um einen Berechtigungssatz zu erstellen, gehen Sie zu **Einstellungen** > **Berechtigungseinstellungen** und wählen Sie dann **Berechtigungssatz erstellen**. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Name|Berechtigungen|
|-----------|----------------|
|Entwickler:innen|„API-Schlüssel anzeigen", „API-Schlüssel bearbeiten", „Interne Gruppen anzeigen", „Interne Gruppen bearbeiten", „Nachrichtenaktivitätsprotokoll anzeigen", „Event-Benutzerprotokoll anzeigen", „API-Bezeichner anzeigen", „API-Nutzungs-Dashboard anzeigen", „API-Limits anzeigen", „API-Nutzungswarnungen anzeigen", „API-Nutzungswarnungen bearbeiten", „SDK-Debugger anzeigen", „SDK-Debugger bearbeiten".|
|Marketer|„Kampagnen anzeigen", „Kampagnen bearbeiten", „Kampagnen archivieren", „Canvase anzeigen", „Canvase bearbeiten", „Canvase archivieren", „Frequency-Capping-Regeln anzeigen", „Frequency-Capping-Regeln bearbeiten", „Nachrichtenpriorisierung anzeigen", „Nachrichtenpriorisierung bearbeiten", „Content-Blöcke anzeigen", „Feature-Flags anzeigen", „Feature-Flags bearbeiten", „Feature-Flags archivieren", „Segmente anzeigen", „Segmente bearbeiten", „Globale Kontrollgruppe bearbeiten", „IAM-Templates anzeigen", „IAM-Templates bearbeiten", „IAM-Templates archivieren", „E-Mail-Templates anzeigen", „E-Mail-Templates bearbeiten", „E-Mail-Templates archivieren", „Webhook-Templates anzeigen", „Webhook-Templates bearbeiten", „Webhook-Templates archivieren", „Link-Templates anzeigen", „Link-Templates bearbeiten", „Medienbibliothek-Assets anzeigen", „Standorte anzeigen", „Standorte bearbeiten", „Standorte archivieren", „Aktionscodes anzeigen", „Aktionscodes bearbeiten", „Aktionscodes exportieren", „Einstellungscenter anzeigen", „Einstellungscenter bearbeiten", „Dashboard-Berichte bearbeiten", „Banner-Templates anzeigen", „Lokalisierungseinstellungen anzeigen", „Operator verwenden", „Decisioning Studio-Agenten anzeigen", „Decisioning Studio-Konversions-Event anzeigen".|
|Benutzerverwaltung|„Dashboard-Nutzer:innen bearbeiten", „Teams anzeigen", „Teams bearbeiten", „Teams archivieren".|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Eine Rolle erstellen

Rollen ermöglichen eine bessere Strukturierung durch die Bündelung Ihrer individuell angepassten Berechtigungen mit den Zugriffskontrollen für den Workspace. Das ist besonders nützlich, wenn Sie viele Marken oder regionale Workspaces in einem Dashboard haben. Mit Rollen können Sie Dashboard-Nutzer:innen zu den richtigen Workspaces hinzufügen und ihnen direkt die entsprechenden Berechtigungen erteilen. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Rollenname    | Workspace | Berechtigungen  
----------- | ----------- | ---------
| Marketer – Modemarken | {::nomarkdown}[DEV] Modemarke, [QA] Modemarke, [PROD] Modemarke {:/} | „Kampagnen anzeigen", „Kampagnen bearbeiten", „Kampagnen archivieren", „Canvase anzeigen", „Canvase bearbeiten", „Canvase archivieren", „Content-Blöcke anzeigen", „Content-Blöcke bearbeiten", „Content-Blöcke archivieren", „Content-Blöcke starten", „Feature-Flags anzeigen", „Feature-Flags bearbeiten", „Feature-Flags archivieren", „Segmente anzeigen", „Segmente bearbeiten", „Banner-Templates anzeigen", „Banner-Templates bearbeiten", „E-Mail-Templates anzeigen", „E-Mail-Templates bearbeiten", „Medienbibliothek-Assets anzeigen", „Medienbibliothek-Assets bearbeiten", „Medienbibliothek-Assets löschen", „Standorte anzeigen", „Standorte bearbeiten", „Standorte archivieren", „Aktionscodes anzeigen", „Aktionscodes bearbeiten", „Aktionscodes exportieren", „Einstellungscenter anzeigen", „Einstellungscenter bearbeiten". |
| Marketer – Hautpflegemarken | {::nomarkdown}[DEV] Hautpflegemarke, [QA] Hautpflegemarke, [PROD] Hautpflegemarke {:/} |„Kampagnen anzeigen", „Kampagnen bearbeiten", „Kampagnen archivieren", „Canvase anzeigen", „Canvase bearbeiten", „Canvase archivieren", „Content-Blöcke anzeigen", „Content-Blöcke bearbeiten", „Content-Blöcke archivieren", „Content-Blöcke starten", „Feature-Flags anzeigen", „Feature-Flags bearbeiten", „Feature-Flags archivieren", „Segmente anzeigen", „Segmente bearbeiten", „Banner-Templates anzeigen", „Banner-Templates bearbeiten", „E-Mail-Templates anzeigen", „E-Mail-Templates bearbeiten", „Medienbibliothek-Assets anzeigen", „Medienbibliothek-Assets bearbeiten", „Medienbibliothek-Assets löschen", „Standorte anzeigen", „Standorte bearbeiten", „Standorte archivieren", „Aktionscodes anzeigen", „Aktionscodes bearbeiten", „Aktionscodes exportieren", „Einstellungscenter anzeigen", „Einstellungscenter bearbeiten".|
| Benutzerverwaltung – Alle Marken | {::nomarkdown}[DEV] Modemarke, [QA] Modemarke, [PROD] Modemarke, [DEV] Hautpflegemarke, [QA] Hautpflegemarke, [PROD] Hautpflegemarke {:/} | „Dashboard-Nutzer:innen bearbeiten", „Teams anzeigen", „Teams bearbeiten", „Teams archivieren"|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## Wie unterscheiden sich Berechtigungssätze und Rollen von Teams?

{% multi_lang_include permissions.md content="Differences" %}

### Überlegungen zum Hinzufügen von Benutzerberechtigungen zu Teams

Es kann zu Schwierigkeiten kommen, wenn Sie versuchen, Berechtigungen im Braze-Dashboard zu speichern – insbesondere beim Hinzufügen oder Entfernen von Nutzer:innen aus einem Workspace oder beim Hinzufügen zu einem Team. Der Button **Nutzer:innen speichern/aktualisieren** kann ausgegraut sein, wenn die Berechtigungen der Nutzer:innen mit denen identisch sind, die sie bereits auf Workspace-Ebene besitzen. Diese Einschränkung besteht, da es keinen Vorteil bietet, ein Team zu haben, wenn alle Nutzer:innen über dieselben Berechtigungen wie der gesamte Workspace verfügen.

Um Nutzer:innen erfolgreich zu einem Team hinzuzufügen und dabei die gleichen Berechtigungen beizubehalten, weisen Sie keine Berechtigungen auf Workspace-Ebene zu. Weisen Sie Berechtigungen stattdessen ausschließlich auf Team-Ebene zu.

## Eingeschränkte Nutzer:innen

Eingeschränkte Nutzer:innen verfügen über spezifische Berechtigungen, die es ihnen ermöglichen, bestimmte Aspekte des Braze-Dashboards zu verwalten, wobei sie im Vergleich zu Unternehmensadministratoren und Workspace-Administratoren Einschränkungen unterliegen.

| Geltungsbereich | Beschreibung |
| --- | --- |
| Berechtigungen | Eingeschränkte Nutzer:innen können die Berechtigungen anderer eingeschränkter Nutzer:innen bearbeiten, wenn sie über die Berechtigung „Dashboard-Nutzer:innen bearbeiten" verfügen. Sie können auch neue eingeschränkte Nutzer:innen anlegen und deren Berechtigungssätze ändern. Sie können jedoch keine Unternehmensadministratorkonten erstellen oder verwalten. |
| Rollenbeschränkungen | Wenn eingeschränkte Nutzer:innen über alle Berechtigungen außer „Workspace-Administrator" verfügen, haben sie dennoch Zugriff auf alle anderen Berechtigungen, die normalerweise einem Workspace-Administrator gewährt werden. |
| Sichtbarkeit von Berechtigungen | Wenn eingeschränkte Nutzer:innen die Berechtigung „Dashboard-Nutzer:innen bearbeiten" für einen Workspace (z. B. Dev) besitzen, jedoch nicht für einen anderen (z. B. Prod), werden die Berechtigungen für den Workspace Prod auf der Detailseite für Dashboard-Nutzer:innen nicht angezeigt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Vergleich eingeschränkter Nutzer:innen

| Eingeschränkter Nutzertyp | Beschreibung |
| --- | --- |
| Workspace-Administrator | Workspace-Administratoren verfügen über spezifische Berechtigungen für die Verwaltung von Workspaces, jedoch nicht über dieselben Befugnisse wie Unternehmensadministratoren. Eingeschränkte Nutzer:innen können ähnliche Berechtigungen wie Workspace-Administratoren erhalten, wenn die erforderlichen Berechtigungen aktiviert sind. |
| Administrator (Unternehmensadministrator) | Unternehmensadministratoren verfügen über umfassendere Berechtigungen, einschließlich der Möglichkeit, Dashboard-Nutzer:innen zu löschen. Sie können jedoch ihre eigenen Konten nicht löschen und müssen sich für diese Aktion an einen anderen Unternehmensadministrator wenden. |
| Nur-Lese-Zugriff | Um auf bestimmte Bereiche des Dashboards zugreifen zu können, wie beispielsweise die Seite „Kampagnen", müssen Nutzer:innen über die entsprechenden Anzeigeberechtigungen verfügen.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Fehler bei eingeschränktem Zugriff

Nutzer:innen können Nachrichten wie „Sie benötigen die Berechtigung ‚Landing Pages anzeigen', um auf diese Seite zugreifen zu können" erhalten. In solchen Fällen sollten die Nutzer:innen und der Kontoadministrator überprüfen, ob die erforderlichen Berechtigungen erteilt wurden. Ist dies der Fall, versuchen Sie, das Problem zu beheben, indem Sie die Berechtigungen der Nutzer:innen deaktivieren und anschließend wieder aktivieren. 

{% alert note %}
Es ist nicht möglich, Benutzerberechtigungen von einer Dashboard-Nutzer:in auf eine andere zu übertragen oder zu importieren.
{% endalert %}

## Bearbeiten der Berechtigungen von Nutzer:innen

Um die aktuellen Administrator-, Unternehmens- oder Workspace-Berechtigungen von Nutzer:innen zu bearbeiten, navigieren Sie zu **Einstellungen** > **Unternehmensbenutzer** und wählen Sie den entsprechenden Namen aus.

![Die Seite „Unternehmensbenutzer" in Braze zeigt eine Tabelle mit Dashboard-Nutzer:innen an.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Admin

Admins haben Zugriff auf alle Features und können alle Unternehmenseinstellungen ändern. Sie können:

- [Genehmigungseinstellungen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval) ändern
- Andere [Braze-Nutzer:innen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users) hinzufügen, bearbeiten, löschen, suspendieren oder die Suspendierung aufheben
- Braze-Nutzer:innen als CSV-Datei exportieren

Um Admin-Rechte zu gewähren oder zu entfernen, wählen Sie **Dieser Benutzer ist ein Admin** und dann **Benutzer aktualisieren**.

![Die Details der ausgewählten Nutzer:in mit aktiviertem Admin-Kontrollkästchen.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Wenn Sie Nutzer:innen die Administratorrechte entziehen, können diese nicht mehr auf Braze zugreifen, bis Sie ihnen mindestens eine [Berechtigung auf Unternehmens- oder Workspace-Ebene]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions) zuweisen.
{% endalert %}

{% endtab %}
{% tab Company %}

### Unternehmen

Um die folgenden Berechtigungen auf Unternehmensebene für Nutzer:innen zu verwalten, aktivieren oder deaktivieren Sie das Kästchen neben der jeweiligen Berechtigung. Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

|Berechtigungsname|Beschreibung|
|----------|-----------|
|Unternehmenseinstellungen verwalten|Ermöglicht es Nutzer:innen, Berechtigungseinstellungen und die Absenderverifizierung anzupassen.|
|Workspaces erstellen und löschen|Ermöglicht es Nutzer:innen, Workspaces zu erstellen und zu löschen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Workspace

Sie können Nutzer:innen unterschiedliche Berechtigungen für jeden Workspace erteilen, dem sie in Braze angehören. Um die Berechtigungen auf Workspace-Ebene zu verwalten, wählen Sie **Workspaces und Berechtigungen auswählen** und legen Sie dann die Berechtigungen manuell fest oder weisen Sie einen zuvor erstellten [Berechtigungssatz oder eine Rolle]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) zu. Um Nutzer:innen unterschiedliche Berechtigungen für verschiedene Workspaces zu vergeben, wiederholen Sie diesen Vorgang so oft wie nötig. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus der Dropdown-Liste. Wählen Sie anschließend unter **Berechtigungen** eine oder mehrere Berechtigungen aus. Diese Berechtigungen gelten nur für die von Ihnen ausgewählten Workspaces. Optional können Sie **Workspace-Administratorzugriff zuweisen** auswählen, wenn Sie den Nutzer:innen stattdessen vollständige Berechtigungen für diesen Workspace gewähren möchten.

Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

![Berechtigungen auf Workspace-Ebene, die manuell in Braze ausgewählt werden.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus der Dropdown-Liste. Wählen Sie dann unter **Berechtigungssätze** einen Berechtigungssatz aus. Diese Berechtigungen gelten nur für die von Ihnen ausgewählten Workspaces.

Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

![Berechtigungen auf Workspace-Ebene, die über einen Berechtigungssatz in Braze zugewiesen werden.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Assign role %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus der Dropdown-Liste. Wählen Sie anschließend unter **Rolle** eine Rolle aus. Diese Berechtigungen gelten nur für die von Ihnen ausgewählten Workspaces.

Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

![Berechtigungen auf Workspace-Ebene, die über eine Rolle in Braze zugewiesen werden.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Benutzerberechtigungen exportieren

Um eine Liste Ihrer Nutzer:innen und deren Berechtigungen herunterzuladen, gehen Sie zu **Einstellungen** > **Unternehmensbenutzer** und wählen Sie dann **Nutzer:innen exportieren**. Eine CSV-Datei wird in Kürze an Ihre E-Mail-Adresse gesendet.

![Die Seite „Unternehmensbenutzer" in Braze mit der Option „Nutzer:innen exportieren" im Fokus.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Liste der Berechtigungen

| Berechtigung | Definition |
|-------------------------------------------------|---------------------|
| Rechnungsdetails anzeigen                            | Rechnungsdetails anzeigen |
| Als PII gekennzeichnete angepasste Attribute anzeigen            | Als PII gekennzeichnete angepasste Attribute anzeigen |
| PII anzeigen                                        | PII anzeigen |
| Nutzerprofile PII-konform anzeigen               | Zugriff auf die Nutzersuche und Anzeige von Nutzerprofilen mit unkenntlich gemachten PII-Daten |
| Nutzungsdaten anzeigen                                 | Nutzungsdaten anzeigen |
| Doppelte Nutzer:innen zusammenführen                           | Vorschau anzeigen und doppelte Nutzer:innen zu einer Nutzer:in zusammenführen. Duplikate werden nach dem Zusammenführen entfernt. |
| Canvas-Templates anzeigen                           | Canvas-Templates anzeigen |
| Canvas-Templates archivieren                        | Canvas-Templates in das Archiv verschieben |
| Content-Blöcke starten                           | Content-Blöcke starten |
| Präferenzzentren starten                       | Präferenzzentren starten |
| Currents-Integrationen bearbeiten                      | Currents-Integrationen erstellen, aktualisieren und löschen |
| Currents-Integrationen anzeigen                       | Currents-Integrationen anzeigen |
| Kampagnen anzeigen                                  | Kampagnen anzeigen |
| Kampagnen bearbeiten                                  | Kampagnen erstellen und aktualisieren |
| Kampagnen archivieren                               | Kampagnen in das Archiv verschieben |
| Kampagnen starten                                | Bestehende Kampagnen starten, stoppen, pausieren oder fortsetzen |
| Frequency-Capping-Regeln anzeigen                    | Frequency-Capping-Regeln anzeigen |
| Frequency-Capping-Regeln bearbeiten                    | Frequency-Capping-Regeln erstellen und aktualisieren |
| Canvase anzeigen                                   | Canvase anzeigen |
| Canvase bearbeiten                                   | Canvase erstellen und aktualisieren |
| Canvase archivieren                                | Canvase in das Archiv verschieben |
| Canvase starten                                 | Bestehende Canvase starten, stoppen, pausieren oder fortsetzen |
| Content-Blöcke anzeigen                             | Content-Blöcke anzeigen |
| Content-Blöcke bearbeiten                             | Content-Blöcke erstellen und aktualisieren |
| Content-Blöcke archivieren                          | Content-Blöcke in das Archiv verschieben |
| Feature-Flags anzeigen                              | Feature-Flags anzeigen |
| Feature-Flags bearbeiten                              | Feature-Flags erstellen und aktualisieren |
| Feature-Flags archivieren                           | Feature-Flags in das Archiv verschieben |
| WhatsApp-Nachrichten-Templates anzeigen                 | Ermöglicht es Nutzer:innen, [WhatsApp-Nachrichten-Templates]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/?tab=template%20messages#step-2-compose-your-whatsapp-message) anzuzeigen. |
| WhatsApp-Nachrichten-Templates bearbeiten | Ermöglicht es Nutzer:innen, WhatsApp-Nachrichten-Templates im Template-Builder zu erstellen. Dieses Feature befindet sich derzeit in der Early-Access-Phase. |
| Segmente anzeigen                                   | Segmente anzeigen. Nutzer:innen müssen über die Berechtigung „Segmente anzeigen" verfügen, um die Berechtigung „Segmente bearbeiten" oder „Segmente archivieren" zu erhalten. |
| Segmente archivieren                                | Segmente archivieren und aus dem Archiv entfernen. Nutzer:innen mit der Berechtigung „Segmente archivieren" muss auch die Berechtigung „Segmente anzeigen" erteilt werden. |
| Segmente bearbeiten                                   | Segmente erstellen und aktualisieren. Nutzer:innen mit der Berechtigung „Segmente bearbeiten" muss auch die Berechtigung „Segmente anzeigen" erteilt werden. |
| Globale Kontrollgruppe anzeigen                       | Die Einrichtungsseite der globalen Kontrollgruppe anzeigen |
| Globale Kontrollgruppe bearbeiten                       | Änderungen an der globalen Kontrollgruppe erstellen und speichern. Nutzer:innen mit der Berechtigung „Globale Kontrollgruppe bearbeiten" müssen auch die Berechtigungen „Kampagnen bearbeiten" und „Canvase bearbeiten" erhalten. Nutzer:innen mit der Berechtigung „Globale Kontrollgruppe bearbeiten" erhalten auch die Berechtigung „Globale Kontrollgruppe anzeigen". |
| Banner-Templates anzeigen                           | Banner-Templates anzeigen |
| Banner-Templates bearbeiten                           | Banner-Templates erstellen und aktualisieren |
| Banner-Templates archivieren                   	  | Banner-Templates in das Archiv verschieben |
| E-Mail-Templates anzeigen                            | E-Mail-Templates anzeigen |
| E-Mail-Templates bearbeiten                            | E-Mail-Templates erstellen und aktualisieren |
| E-Mail-Templates archivieren                         | E-Mail-Templates in das Archiv verschieben |
| Link-Templates anzeigen   	                  | Link-Templates anzeigen, ohne Änderungen vorzunehmen |
| Link-Templates bearbeiten	                      | Link-Templates erstellen und aktualisieren |
| Landing-Pages veröffentlichen                           | Einen Landing-Page-Entwurf aktivieren |
| Landing-Page-Entwürfe bearbeiten                        | Landing-Page-Entwürfe erstellen und speichern |
| Landing-Pages anzeigen			                  | Landing-Pages anzeigen |
| Landing-Page-Templates bearbeiten	                  | Landing-Page-Templates erstellen und aktualisieren |
| Landing-Page-Templates anzeigen	                  | Landing-Page-Templates anzeigen |
| Landing-Page-Templates archivieren 	              | Landing-Page-Templates in das Archiv verschieben |
| Medienbibliothek-Assets anzeigen                       | Medienbibliothek-Assets anzeigen |
| Medienbibliothek-Assets bearbeiten                       | Medienbibliothek-Assets erstellen und aktualisieren |
| Medienbibliothek-Assets löschen                     | Medienbibliothek-Assets dauerhaft löschen |
| Standorte anzeigen                                  | Standorte anzeigen |
| Standorte bearbeiten                                  | Standorte erstellen und bearbeiten |
| Standorte archivieren                               | Standorte in das Archiv verschieben |
| Aktionscodes anzeigen                            | Aktionscodes anzeigen |
| Aktionscodes bearbeiten                            | Aktionscodes erstellen und aktualisieren |
| Aktionscodes exportieren                          | Eine Liste mit Aktionscodes vom Dashboard herunterladen |
| Einstellungscenter anzeigen                         | Einstellungscenter anzeigen  |
| Einstellungscenter bearbeiten                         | Einstellungscenter erstellen und aktualisieren |
| Einstellungscenter starten	                      | Einen Entwurf für das Einstellungscenter aktivieren oder ein bestehendes aktualisieren |
| API-Schlüssel anzeigen                                   | API-Schlüssel anzeigen |
| API-Schlüssel bearbeiten                                   | API-Schlüssel erstellen und aktualisieren |
| Interne Gruppen anzeigen                            | Interne Gruppen anzeigen |
| Interne Gruppen bearbeiten                            | Interne Gruppen erstellen und aktualisieren |
| Interne Gruppen löschen                          | Interne Gruppen löschen |
| Nachrichtenaktivitätsprotokoll anzeigen                       | Nachrichtenaktivitätsprotokolle anzeigen |
| Event-Benutzerprotokoll anzeigen                             | Event-Benutzerprotokolle anzeigen |
| API-Bezeichner anzeigen                            | API-Bezeichner und andere Bezeichner anzeigen |
| API-Nutzungs-Dashboard anzeigen                        | Das API-Nutzungs-Dashboard anzeigen |
| API-Limits anzeigen                                 | API-Rate-Limits anzeigen |
| API-Nutzungswarnungen anzeigen                           | API-Nutzungswarnungen anzeigen |
| API-Nutzungswarnungen bearbeiten                           | API-Nutzungswarnungen erstellen und aktualisieren |
| SDK-Debugger bearbeiten                               | SDK-Debugger-Sitzungen erstellen und herunterladen |
| SDK-Debugger anzeigen                               | SDK-Debugger oder Debugging-Sitzungen anzeigen |
| App-Einstellungen anzeigen                               | Die Seite „App-Einstellungen" anzeigen |
| App-Einstellungen bearbeiten                               | Apps innerhalb der App-Einstellungen erstellen, bearbeiten und aktualisieren |
| Kataloge anzeigen                                   | Kataloge und Auswahlen anzeigen |
| Kataloge bearbeiten                                   | Kataloge und Auswahlen erstellen und aktualisieren |
| Kataloge exportieren                                 | Kataloge vom Dashboard herunterladen |
| Kataloge löschen                                 | Kataloge dauerhaft löschen |
| Dashboard-Nutzer:innen bearbeiten                            | Unternehmensnutzer:innen anzeigen, erstellen und bearbeiten |
| E-Mail-Einstellungen anzeigen                             | E-Mail-Einstellungen anzeigen |
| E-Mail-Einstellungen bearbeiten                             | E-Mail-Einstellungen aktivieren und aktualisieren | 
| Verschlüsselung auf Bezeichner-Feldebene bearbeiten            | Einstellungen für die Verschlüsselung auf Feldebene aktivieren und aktualisieren |
| Angepasste Attribute anzeigen                          | Angepasste Attribute und Nutzungsbericht anzeigen |
| Angepasste Attribute bearbeiten                          | Angepasste Attribute erstellen und aktualisieren |
| Sperrliste für angepasste Attribute                     | Angepasste Attribute zu einer Sperrliste hinzufügen, die die Verwendung im Dashboard einschränkt |
| Angepasste Attribute löschen                        | Angepasste Attribute dauerhaft löschen |
| Angepasste Attribute exportieren                        | Angepasste Attribute vom Dashboard herunterladen |
| Angepasste Events anzeigen                              | Angepasste Events und Nutzungsberichte anzeigen und angepasste Events zum täglichen Analytics-Bericht per E-Mail hinzufügen |
| Angepasste Events bearbeiten                              | Angepasste Events erstellen und aktualisieren |
| Sperrliste für angepasste Events                         | Angepasste Events zu einer Sperrliste hinzufügen, die die Verwendung im Dashboard einschränkt |
| Angepasste Events löschen                            | Angepasste Events dauerhaft löschen |
| Angepasste Events exportieren                            | Angepasste Events vom Dashboard herunterladen |
| Segmentierung von angepassten Event-Eigenschaften bearbeiten         | Segmentierung für angepasste Event-Eigenschaften aktivieren und deaktivieren |
| Produkte anzeigen                                   | Produkte anzeigen |
| Produkte bearbeiten                                   | Produkte erstellen und aktualisieren |
| Sperrliste für Produkte                              | Produkte zu einer Sperrliste hinzufügen, die die Verwendung im Dashboard einschränkt |
| Segmentierung von Kaufeigenschaften bearbeiten             | Segmentierung für Kauf-Event-Eigenschaften aktivieren und deaktivieren |
| Technologiepartner bearbeiten                        | Technologiepartner erstellen und aktualisieren |
| Cloud-Datenaufnahme bearbeiten                       | Quellen und Synchronisierungen erstellen, aktualisieren und löschen |
| Lokalisierungseinstellungen anzeigen                      | Die Seite für mehrsprachige Gebietsschemaeinstellungen anzeigen |
| Lokalisierungseinstellungen bearbeiten                      | Mehrsprachige Gebietsschemaeinstellungen erstellen |
| Lokalisierungseinstellungen löschen                    | Mehrsprachige Gebietsschemaeinstellungen löschen |
| Abos bearbeiten                              | Abo-Gruppen erstellen und aktualisieren |
| Tags anzeigen                                       | Tags anzeigen |
| Tags bearbeiten                                       | Tags erstellen und aktualisieren |
| Tags löschen                                     | Tags dauerhaft löschen |
| Teams anzeigen                                      | Teams anzeigen |
| Teams bearbeiten                                      | Teams erstellen und aktualisieren |
| Teams archivieren                                   | Teams in das Archiv verschieben |
| Datentransformationen anzeigen                        | Datentransformationen anzeigen |
| Datentransformationen bearbeiten                        | Datentransformationen erstellen und aktualisieren |
| Canvas-Templates bearbeiten                           | Canvas-Templates erstellen und aktualisieren |
| Kampagnen genehmigen                               | Kampagnen genehmigen oder ablehnen. Der [Genehmigungsworkflow für Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) muss aktiviert sein, damit diese Berechtigung gilt. Diese Einstellung befindet sich derzeit in der Early-Access-Phase. Wenden Sie sich an Ihren Account Manager, wenn Sie an einer Teilnahme am Early Access interessiert sind. |
| Canvase genehmigen                                | Canvase genehmigen oder ablehnen. Der [Genehmigungsworkflow für Canvase]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) muss aktiviert sein, damit diese Berechtigung gilt. Diese Einstellung befindet sich derzeit in der Early-Access-Phase. Wenden Sie sich an Ihren Account Manager, wenn Sie an einer Teilnahme am Early Access interessiert sind. |
| Platzierungen anzeigen                                 | Bannerplatzierungen anzeigen |
| Platzierungen bearbeiten                                 | Bannerplatzierungen anzeigen, ohne Änderungen vorzunehmen |
| Platzierungen archivieren                              | Bannerplatzierungen in das Archiv verschieben |
| Push-Einstellungen anzeigen                              | Push-Einstellungen anzeigen |
| Push-Einstellungen bearbeiten                              | Push-Einstellungen erstellen und aktualisieren |
| Dashboard-Berichte bearbeiten                          | Berichte erstellen und aktualisieren |
| Importierte Nutzer:innen anzeigen                               | CSV-Nutzerimporte anzeigen, ohne Änderungen vorzunehmen |
| Nutzer:innen importieren                                    | Nutzer:innen in das Dashboard hochladen |
| Nutzerdaten exportieren                                | Nutzer:innen vom Dashboard herunterladen |
| Nutzerdaten bearbeiten                                  | Nutzerdaten erstellen und aktualisieren |
| Zusammengeführte Nutzer:innen anzeigen                                | Eine Liste der Zusammenführungsdatensätze für Nutzer:innen anzeigen |
| Angepasste KI-Agenten anzeigen                           | Ermöglicht es Nutzer:innen, angepasste KI-Agenten anzuzeigen. |
| Angepasste KI-Agenten bearbeiten                           | Ermöglicht es Nutzer:innen, angepasste KI-Agenten zu erstellen und zu aktualisieren. |
| Angepasste KI-Agenten archivieren                        | Ermöglicht es Nutzer:innen, angepasste KI-Agenten zu archivieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }