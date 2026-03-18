{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

## Erstellen eines Berechtigungssatzes

Mit Berechtigungspaketen können Sie Berechtigungen für bestimmte Themenbereiche oder Aktionen bündeln. Sie können Berechtigungssätze auf Dashboard-Nutzer:innen anwenden, die in verschiedenen Workspaces denselben Zugriff benötigen. Um einen Berechtigungssatz zu erstellen, gehen Sie zu **Einstellungen** > **Berechtigungseinstellungen** und wählen Sie dann **Berechtigungssatz erstellen**. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Name|Berechtigungen|
\|-----------|----------------|
|Entwickler:in|„API-Schlüssel anzeigen“, „API-Schlüssel bearbeiten“, „Interne Gruppen anzeigen“, „Interne Gruppen bearbeiten“, „Nachrichtenaktivitätsprotokoll anzeigen“, „Event-Benutzerprotokoll anzeigen“, „API-Bezeichner anzeigen“, „API-Nutzungs-Dashboard anzeigen“, „API-Limits anzeigen“, „API-Nutzungswarnungen anzeigen“, „API-Nutzungswarnungen bearbeiten“, „SDK-Debugger anzeigen“, „SDK-Debugger bearbeiten“.|
|Marketer|„Kampagnen anzeigen“, „Kampagnen bearbeiten“, „Kampagnen archivieren“, „Canvases anzeigen“, „Canvases bearbeiten“, „Canvases archivieren“, „Frequency-Capping-Regeln anzeigen“, „Frequency-Capping-Regeln bearbeiten“, „Nachrichtenpriorisierung anzeigen“, „Nachrichtenpriorisierung bearbeiten“, „Content-Blöcke anzeigen“, „Feature-Flags anzeigen“, „Feature-Flags bearbeiten“, „Feature-Flags archivieren“, „Segmente anzeigen“, „Segmente bearbeiten“, „Globale Kontrollgruppe bearbeiten“, „IAM-Vorlagen anzeigen“, „IAM-Vorlagen bearbeiten“, „IAM-Vorlagen archivieren“, „E-Mail-Vorlagen anzeigen“, „E-Mail-Templates bearbeiten“, „E-Mail-Templates archivieren“, „Webhook-Templates anzeigen“, „Webhook-Templates bearbeiten“, „Webhook-Templates archivieren“, „Link-Templates anzeigen“, „Link-Templates bearbeiten“, „Medienbibliothek-Assets anzeigen“, „Standorte anzeigen“, „Standorte bearbeiten“, „Standorte archivieren“, „Aktionscodes anzeigen“, „Aktionscodes bearbeiten“, „Aktionscodes exportieren“, „Einstellungscenter anzeigen“, „Einstellungscenter bearbeiten“, „Berichte bearbeiten“, „Bannertemplates anzeigen“, „Mehrsprachige Einstellungen anzeigen“, „Operator verwenden“, „Decisioning Studio-Agenten anzeigen“, „Decisioning Studio-Konversions-Event anzeigen“.
|Benutzerverwaltung|„Dashboard-Nutzer:innen anzeigen“, „Dashboard-Nutzer:innen bearbeiten“, „Teams anzeigen“, „Teams bearbeiten“, „Teams archivieren“.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Eine Rolle erstellen

Rollen ermöglichen eine bessere Strukturierung durch die Bündelung Ihrer individuell angepassten Berechtigungen mit den Zugriffskontrollen für den Workspace. Das ist besonders nützlich, wenn Sie viele Marken oder regionale Workspaces in einem Dashboard haben. Mit Rollen können Sie Dashboard-Benutzer zu den richtigen Arbeitsbereichen hinzufügen und ihnen direkt die entsprechenden Berechtigungen erteilen. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Rollenname | Arbeitsbereich | Berechtigungen  
----------- | ----------- | ---------
| Marketer – Modemarken | {::nomarkdown}[DEV] Modemarke, [QA] Modemarke, [PROD] Modemarke{:/}| „Kampagnen anzeigen“, „Kampagnen bearbeiten“, „Kampagnen archivieren“, „Canvases anzeigen“, „Canvases bearbeiten“, „Canvases archivieren“, „Content-Blöcke anzeigen“, „Content-Blöcke bearbeiten“, „Content-Blöcke archivieren“, „Content-Blöcke starten“, „Feature-Flags anzeigen“, „Feature-Flags bearbeiten“, „Feature-Flags archivieren“, „Segmente anzeigen“, „Segmente bearbeiten“, „Banner-Templates anzeigen“, „Banner-Templates bearbeiten“, „E-Mail-Templates anzeigen“, „E-Mail-Templates bearbeiten“, „Medienbibliothek-Assets anzeigen“, „Medienbibliothek-Assets bearbeiten“, „Medienbibliothek-Assets löschen“, „Standorte anzeigen“, „Standorte bearbeiten“, „Standorte archivieren“, „Aktionscodes anzeigen“, „Aktionscodes bearbeiten“, „Aktionscodes exportieren“, „Einstellungscenter anzeigen“, „Einstellungscenter bearbeiten“. |
| Marketer – Hautpflegemarken | {::nomarkdown}[DEV] Hautpflegemarke, [QA] Hautpflegemarke, [PROD] Hautpflegemarke{:/}| „Kampagnen anzeigen“, „Kampagnen bearbeiten“, „Kampagnen archivieren“, „Canvases anzeigen“, „Canvases bearbeiten“, „Canvases archivieren“, „Content-Blöcke anzeigen“, „Content-Blöcke bearbeiten“, „Content-Blöcke archivieren“, „Content-Blöcke starten“, „Feature-Flags anzeigen“, „Feature-Flags bearbeiten“, „Feature-Flags archivieren“, „Segmente anzeigen“, „Segmente bearbeiten“, „Banner-Templates anzeigen“, „Banner-Templates bearbeiten“, „E-Mail-Templates anzeigen“, „E-Mail-Templates bearbeiten“, „Medienbibliothek-Assets anzeigen“, „Medienbibliothek-Assets bearbeiten“, „Medienbibliothek-Assets löschen“, „Standorte anzeigen“, „Standorte bearbeiten“, „Standorte archivieren“, „Aktionscodes anzeigen“, „Aktionscodes bearbeiten“, „Aktionscodes exportieren“, „Einstellungscenter anzeigen“, „Einstellungscenter bearbeiten“.
| Benutzerverwaltung – Alle Marken | {::nomarkdown}[DEV] Modemarke, [QA] Modemarke, [PROD] Modemarke, [DEV] Hautpflegemarke, [QA] Hautpflegemarke, [PROD] Hautpflegemarke{:/}| „Dashboard-Nutzer:innen anzeigen”, „Dashboard-Nutzer:innen bearbeiten”, „Teams anzeigen”, „Teams bearbeiten”, „Teams archivieren”|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## Wie unterscheiden sich die Berechtigungen und Rollen von Teams?

{% multi_lang_include permissions.md content="Differences" %}

### Überlegungen zum Hinzufügen von Benutzerberechtigungen zu Teams

Es kann zu Schwierigkeiten kommen, wenn Sie versuchen, Berechtigungen im Braze-Dashboard zu speichern, insbesondere beim Hinzufügen oder Entfernen von Nutzern aus einem Workspace oder beim Hinzufügen zu einem Team. Der Button **„Nutzer:innen speichern/Update“** kann ausgegraut sein, wenn die Berechtigungen für die Nutzer:innen mit denen identisch sind, die sie bereits auf Workspace-Ebene besitzen. Diese Einschränkung besteht, da es keinen Vorteil bietet, ein Team zu haben, wenn alle Nutzer:innen über dieselben Berechtigungen wie der gesamte Workspace verfügen.

Um einen Nutzer:in erfolgreich zu einem Team hinzuzufügen und dabei die gleichen Berechtigungen beizubehalten, weisen Sie bitte keine Berechtigungen auf Workspace-Ebene zu. Bitte weisen Sie Berechtigungen ausschließlich auf Team-Ebene zu.

## Eingeschränkte Nutzer:innen

Eingeschränkte Nutzer:innen verfügen über spezifische Berechtigungen, die es ihnen ermöglichen, bestimmte Aspekte des Braze-Dashboards zu verwalten, wobei sie im Vergleich zu Unternehmensadministratoren und Workspace-Administratoren Einschränkungen unterliegen.

| Geltungsbereich | Beschreibung |
| --- | --- |
| Berechtigungen | Nutzer:innen mit eingeschränkten Rechten können die Berechtigungen anderer Nutzer:innen mit eingeschränkten Rechten bearbeiten, wenn sie über die Berechtigungen „Dashboard-Nutzer:innen anzeigen“ und „Dashboard-Nutzer:innen bearbeiten“ verfügen. Sie können auch neue eingeschränkte Nutzer:innen anlegen und deren Berechtigungen ändern. Sie können jedoch keine Unternehmensadministratorkonten erstellen oder verwalten. |
| Rollenbeschränkungen | Wenn eine eingeschränkte Nutzer:in über alle Berechtigungen außer „Workspace-Administrator“ verfügt, hat sie dennoch Zugriff auf alle anderen Berechtigungen, die normalerweise einem Workspace-Administrator gewährt werden. |
| Sichtbarkeit von Berechtigungen | Wenn ein eingeschränkter Nutzer über die Berechtigungen „Dashboard-Nutzer anzeigen“ und „Dashboard-Nutzer bearbeiten“ für einen Workspace (z. B. Dev) verfügt, jedoch nicht für einen anderen (z. B. Prod), werden ihm die Berechtigungen für den Workspace Prod auf seiner Detailseite für Dashboard-Nutzer:innen nicht angezeigt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Vergleich eingeschränkter Nutzer:innen

| Eingeschränkter Nutzer:in | Beschreibung |
| --- | --- |
| Workspace-Administrator | Workspace-Administratoren verfügen über spezifische Berechtigungen für die Verwaltung von Workspaces, jedoch nicht über dieselben Befugnisse wie Unternehmensadministratoren. Eingeschränkte Nutzer:innen können ähnliche Berechtigungen wie Workspace-Administratoren erhalten, wenn die erforderlichen Berechtigungen aktiviert sind. |
| Administrator (Unternehmensadministrator) | Unternehmensadministratoren verfügen über umfassendere Berechtigungen, einschließlich der Möglichkeit, Dashboard-Nutzer:innen zu löschen. Sie können jedoch ihre eigenen Konten nicht löschen und müssen sich für diese Aktion an einen anderen Unternehmensadministrator wenden. |
| Nur-Lese-Zugriff | Um auf bestimmte Bereiche des Dashboards, wie beispielsweise die Seite „Kampagnen“, zugreifen zu können, müssen Nutzer:innen über die entsprechenden Anzeigeberechtigungen verfügen.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Fehler beim eingeschränkten Zugriff

Nutzer:innen können Nachrichten wie „Sie benötigen die Berechtigung „Landing Pages anzeigen“, um auf diese Seite zugreifen zu können“ erhalten. In solchen Fällen sollten der Nutzer:in und der Kontoadministrator überprüfen, dass die erforderlichen Berechtigungen erteilt wurden. Sollte dies der Fall sein, versuchen Sie bitte, das Problem zu beheben, indem Sie die Berechtigungen der Nutzer:innen deaktivieren und anschließend wieder aktivieren. 

{% alert note %}
Es ist nicht möglich, Benutzerberechtigungen von einem Dashboard-Nutzer:in auf einen anderen zu übertragen oder zu importieren.
{% endalert %}

## Bearbeiten der Berechtigungen eines Benutzers

Um die aktuellen Administrator-, Unternehmens- oder Workspace-Berechtigungen einer Nutzer:in zu bearbeiten, navigieren Sie bitte zu **„Einstellungen“** > **„Unternehmensbenutzer“** und wählen Sie den Namen der Nutzer:in aus.

![Die Seite „Unternehmensbenutzer“ in Braze zeigt eine Tabelle mit Dashboard-Nutzer:innen an.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Admin

Admins haben Zugriff auf alle Features und können alle Unternehmenseinstellungen ändern. Sie können:

- [Genehmigungseinstellungen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval) ändern
- Hinzufügen, Bearbeiten, Löschen, Suspendieren oder Aufheben der Suspendierung anderer [Braze-Benutzer]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)
- Braze-Benutzer als CSV-Datei exportieren

Um Admin-Rechte zu gewähren oder zu entfernen, wählen Sie **Dieser Benutzer ist ein Admin** und dann **Benutzer aktualisieren**.

![Die Details der ausgewählten Nutzer:in mit aktiviertem Admin-Kontrollkästchen.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Wenn Sie einem Nutzer:in die Administratorrechte entziehen, kann er nicht mehr auf Braze zugreifen, bis Sie ihm mindestens eine [Berechtigung auf Unternehmens- oder Workspace-Ebene]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions) zuweisen.
{% endalert %}

{% endtab %}
{% tab Company %}

### Unternehmen

Um die folgenden Berechtigungen auf Unternehmensebene für einen Benutzer zu verwalten, aktivieren oder deaktivieren Sie das Kästchen neben der jeweiligen Berechtigung. Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

|Berechtigungsname|Beschreibung|
|----------|-----------|
|Unternehmenseinstellungen verwalten|Ermöglicht es Nutzer:innen, Berechtigungseinstellungen und Überprüfungen des Absenders anzupassen.|
|Workspaces erstellen und löschen|Ermöglicht Benutzern das Erstellen und Löschen von Arbeitsbereichen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Workspace

Sie können individuell unterschiedliche Nutzerberechtigungen für jeden zugehörigen Braze-Workspace erteilen. Um die Berechtigungen auf Workspace-Ebene zu verwalten, wählen Sie **„Workspaces und Berechtigungen auswählen**“ und legen Sie dann die Berechtigungen manuell fest oder weisen Sie einen zuvor erstellten [Berechtigungssatz oder eine]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) zuvor erstellte [Rolle]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) zu. Um individuell unterschiedliche Nutzerberechtigungen für verschiedene Workspaces zu vergeben, wiederholen Sie diesen Vorgang so oft wie nötig. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Wählen Sie unter **Arbeitsbereiche** einen oder mehrere Arbeitsbereiche aus der Dropdown-Liste. Wählen Sie anschließend unter **„Berechtigungen“** eine oder mehrere Berechtigungen aus. Sie erhalten diese Berechtigungen nur für die Arbeitsbereiche, die Sie ausgewählt haben. Optional können Sie **„Workspace-Administratorzugriff auswählen“** auswählen, wenn Sie ihnen stattdessen vollständige Berechtigungen für diesen Workspace gewähren möchten.

Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

![Berechtigungen auf Workspace-Ebene, die manuell in Braze ausgewählt werden.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Wählen Sie unter **Arbeitsbereiche** einen oder mehrere Arbeitsbereiche aus der Dropdown-Liste. Wählen Sie dann unter **Berechtigungssätze** einen Berechtigungssatz aus. Sie erhalten diese Berechtigungen nur für die Arbeitsbereiche, die Sie ausgewählt haben.

Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

![Berechtigungen auf Workspace-Ebene, die über eine Berechtigungsgruppe in Braze zugewiesen werden.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Assign role %}

Wählen Sie unter **Arbeitsbereiche** einen oder mehrere Arbeitsbereiche aus der Dropdown-Liste. Wählen Sie anschließend unter **„Rolle“** eine Rolle aus. Sie erhalten diese Berechtigungen nur für die Arbeitsbereiche, die Sie ausgewählt haben.

Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

![Berechtigungen auf Workspace-Ebene, die über eine Rolle in Braze zugewiesen werden.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Benutzerberechtigungen exportieren

Um eine Liste Ihrer Nutzer:innen und deren Berechtigungen herunterzuladen, gehen Sie zu **Einstellungen** > **Firmennutzer:innen** und wählen Sie dann **Nutzer:innen exportieren**. Eine CSV-Datei wird in Kürze an Ihre E-Mail-Adresse gesendet.

![Die Seite „Unternehmensnutzer:innen“ in Braze mit der Option „Nutzer:innen exportieren“ im Fokus.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Liste der Berechtigungen

| Berechtigung | Definition |
|-------------------------------------------------|---------------------|
| Rechnungsdetails anzeigen                            | Rechnungsdetails anzeigen |
| Als PII gekennzeichnete angepasste Attribute anzeigen            | Als PII gekennzeichnete benutzerdefinierte Attribute anzeigen |
| PII anzeigen                                        | PII anzeigen |
| Nutzerprofile PII-konform anzeigen                | Zugriff auf die Nutzersuche und Anzeige von Nutzerprofilen mit unkenntlich gemachten PII-Daten |
| Nutzungsdaten anzeigen                                 | Nutzungsdaten anzeigen |
| Doppelte Nutzer:innen zusammenführen                           | Bitte führen Sie doppelte Nutzer:innen zu einem Nutzer:in zusammen. Duplikate werden nach dem Zusammenführen entfernt. |
| Vorschau doppelter Nutzer:innen anzeigen                         | Vorschau, welche Nutzerprofile doppelt vorhanden sind |
| Canvas-Templates anzeigen                           | Canvas-Vorlagen ansehen |
| Canvas-Templates archivieren                        | Verschieben Sie Canvas-Templates in das Archiv. |
| Content-Blöcke starten                           | Content-Blöcke starten |
| Präferenzzentren starten                       | Präferenzzentren starten |
| Benutzerdaten exportieren                                | Nutzer:innen vom Dashboard herunterladen |
| Currents-Integrationen bearbeiten                      | Currents-Integrationen erstellen, Update durchführen und löschen |
| Currents-Integration anzeigen                       | Currents-Integrationen anzeigen |
| Kampagnen anzeigen                                  | Kampagnen anzeigen |
| Kampagnen bearbeiten                                  | Erstellen und Update von Kampagnen |
| Kampagnen archivieren                               | Kampagnen in das Archiv verschieben |
| Kampagnen senden                                  | Kampagnen starten, stoppen, pausieren oder fortsetzen | 
| Canvases versenden                         		  | Canvases starten, stoppen, pausieren oder fortsetzen |
| Frequency-Capping-Regeln anzeigen                    | Frequency-Capping-Regeln anzeigen |
| Frequency-Capping-Regeln bearbeiten                    | Erstellen und Update von Frequency-Capping-Regeln |
| Canvase anzeigen                                   | Canvase anzeigen |
| Canvase bearbeiten                                   | Canvases erstellen und Updates durchführen |
| Canvase archivieren                                | Canvases in das Archiv verschieben |
| Content-Blöcke anzeigen                             | Content-Blöcke anzeigen |
| Content-Blöcke bearbeiten                             | Erstellen und Update von Content-Blöcken |
| Content-Blöcke archivieren                          | Content-Blöcke in das Archiv verschieben |
| Feature-Flags anzeigen                              | Feature-Flag anzeigen |
| Feature-Flags bearbeiten                              | Feature-Flag erstellen und Update durchführen |
| Feature-Flags archivieren                           | Feature-Flag-Einträge in das Archiv verschieben |
|  WhatsApp-Nachrichten-Templates anzeigen                | Ermöglicht es Nutzer:innen, [WhatsApp-Nachrichten-Templates]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/?tab=template%20messages#step-2-compose-your-whatsapp-message) anzuzeigen. |
| WhatsApp-Nachrichten-Templates bearbeiten | Ermöglicht es Nutzer:innen, WhatsApp-Nachrichten-Templates im Vorlagen-Generator zu erstellen. Dieses Feature befindet sich derzeit in der Early Access-Phase. |
| Segmente anzeigen                                   | Segmente anzeigen. Nutzer:innen müssen über die Berechtigung „Segmente anzeigen“ verfügen, um die Berechtigung „Segmente bearbeiten“ oder „Segmente archivieren“ zu erhalten. |
| Segmente archivieren                                | Segmente archivieren und aus dem Archiv entfernen. Nutzer:innen mit der Berechtigung „Segmente archivieren“ muss auch die Berechtigung „Segmente anzeigen“ erteilt werden. |
| Segmente bearbeiten                                   | Erstellen und Update von Segmenten. Nutzer:innen mit der Berechtigung „Segmente bearbeiten“ muss auch die Berechtigung „Segmente anzeigen“ erteilt werden. |
| Globale Kontrollgruppe anzeigen                       | Die Einrichtungsseite der globalen Kontrollgruppe anzeigen |
| Globale Kontrollgruppe bearbeiten                       | Erstellen und speichern Sie Änderungen an der globalen Kontrollgruppe. Nutzer:innen mit der Berechtigung „Globale Kontrollgruppe bearbeiten“ müssen auch die Berechtigungen „Kampagnen bearbeiten“ und „Canvases bearbeiten“ erhalten. Nutzer:innen mit der Berechtigung „Globale Kontrollgruppe bearbeiten“ erhalten auch die Berechtigung „Globale Kontrollgruppe anzeigen“. |
| Banner-Templates anzeigen                           | Banner-Templates anzeigen |
| Banner-Templates bearbeiten                           | Banner-Templates erstellen und aktualisieren |
| Banner-Templates archivieren                   	  | Banner-Templates ins Archiv verschieben |
| E-Mail-Templates anzeigen                            | E-Mail-Templates anzeigen |
| E-Mail-Templates bearbeiten                            | E-Mail-Templates erstellen und aktualisieren |
| E-Mail Templates archivieren                         | E-Mail-Templates in das Archiv verschieben |
| Link-Templates anzeigen   	                      | Link-Templates anzeigen |
| Link-Templates bearbeiten	                          | Erstellen und Update von Link-Templates |
| Startseiten veröffentlichen                           | Entwurf einer Landing Page aktivieren |
| Entwürfe für Landing-Pages bearbeiten                        | Entwürfe für Landing Pages erstellen und speichern |
| Landing-Pages anzeigen			                  | Landing Pages anzeigen |
| Landing-Page-Templates bearbeiten	                  |  Erstellen und Update von Landingpage-Templates |
| Landing-Page-Templates anzeigen	                  | Landingpage-Templates anzeigen |
| Archiv-Landingpage-Template 	              | Landingpage-Templates ins Archiv verschieben |
| Mediathek Assets ansehen                       | Medienbibliothek-Assets anzeigen |
| Assets der Medienbibliothek bearbeiten                       | Erstellen und Update von Ressourcen der Medienbibliothek |
| Assets der Medienbibliothek löschen                     | Medienbibliothek-Assets dauerhaft löschen |
| Standorte anzeigen                                  | Standorte anzeigen |
| Standorte bearbeiten                                  | Standorte erstellen und bearbeiten |
| Standorte archivieren                               | Standorte verschieben, um zu archivieren |
| Aktionscodes anzeigen                            | Promo-Codes anzeigen |
| Aktionscodes bearbeiten                            | Erstellen und Update von Aktionscodes |
| Exportförderungsaktionscodes                          | Bitte laden Sie eine Liste mit Aktionscodes vom Dashboard herunter. |
| Präferenzzentren anzeigen                         | Einstellungscenter anzeigen  |
| Präferenzzentren bearbeiten                         | Einstellungszentren erstellen und Updates durchführen |
| Präferenzzentren starten	                      | Einen Entwurf für das Präferenzcenter aktivieren oder ein Update für einen bestehenden durchführen |
| API-Schlüssel anzeigen                                   | API-Schlüssel anzeigen |
| API-Schlüssel bearbeiten                                   | API-Schlüssel erstellen und Update durchführen |
| Interne Gruppen anzeigen                            | Interne Gruppen anzeigen |
| Interne Gruppen bearbeiten                            | Interne Gruppen erstellen und ein Update durchführen |
| Nachrichten-Aktivitätsprotokoll anzeigen                       | Nachrichtenaktivitätsprotokolle anzeigen |
| Event-Nutzerprotokoll anzeigen                             | Event-Benutzerprotokolle anzeigen |
| API-Bezeichner anzeigen                            | API-Bezeichner und andere Bezeichner anzeigen |
| Dashboard zur API-Nutzung anzeigen                        | Das API-Nutzungs-Dashboard anzeigen |
| API-Limits anzeigen                                 | API-Rate-Limits anzeigen |
| API-Nutzungsmeldungen anzeigen                           | API-Nutzungswarnungen anzeigen |
| API-Nutzungsmeldungen bearbeiten                           | Erstellen und Update von API-Nutzungswarnungen |
| SDK-Debugger bearbeiten                               | Erstellen und Herunterladen von SDK-Debugger-Sitzungen |
| SDK Debugger anzeigen                               | SDK-Debugger anzeigen oder Debugging-Sitzungen |
| App-Einstellungen anzeigen                               | App-Einstellungen anzeigen |
| App-Einstellungen bearbeiten                               | Erstellen, bearbeiten und Update von Apps innerhalb der App-Einstellungen. |
| Kataloge anzeigen                                   | Kataloge und Auswahlen anzeigen |
| Kataloge bearbeiten                                   | Erstellen und Update von Katalogen und Auswahlen |
| Kataloge exportieren                                 | Laden Sie Kataloge über das Dashboard herunter. |
| Kataloge löschen                                 | Kataloge dauerhaft löschen |
| Nutzer:innen des Dashboards anzeigen                            | Unternehmensnutzer:innen anzeigen |
| Dashboard-Nutzer:innen bearbeiten                            | Unternehmensnutzer:innen erstellen und aktualisieren 
| E-Mail-Einstellungen anzeigen                             | E-Mail-Einstellungen anzeigen |
| E-Mail-Einstellungen bearbeiten                             | E-Mail-Einstellungen aktivieren und aktualisieren | 
| Verschlüsselung auf Bezeichner-Feldebene bearbeiten            | Aktivieren und Update der Einstellungen für die Verschlüsselung auf Feldebene. |
| Angepasste Attribute anzeigen                          | Angepasste Attribute und Nutzungsbericht anzeigen |
| Angepasste Attribute bearbeiten                          | Angepasste Attribute erstellen und aktualisieren |
| Sperrliste für angepasste Attribute                     | Fügen Sie einer Sperrliste angepasste Attribute hinzu, die die Verwendung im Dashboard einschränken. |
| Angepasste Attribute löschen                        | Angepasste Attribute dauerhaft löschen |
| Angepasste Attribute exportieren                        | Angepasste Attribute vom Dashboard herunterladen |
| Angepasste Events anzeigen                              | Angepasste Events und Nutzungsberichte anzeigen und angepasste Events zum Tagesbericht per E-Mail hinzufügen |
| Angepasste Events bearbeiten                              | Angepasste Events erstellen und aktualisieren |
| Sperrliste für angepasste Events                         | Fügen Sie angepasste Events zu einer Sperrliste hinzu, die die Verwendung im Dashboard einschränkt. |
| Angepasste Events löschen                            | Angepasste Events dauerhaft löschen |
| Angepasste Events exportieren                            | Angepasste Events vom Dashboard herunterladen |
| Segmentierung von angepassten Event-Eigenschaften bearbeiten         | Aktivieren und Deaktivieren der Segmentierung für benutzerdefinierte Event-Eigenschaften |
| Produkte anzeigen                                   | Produkte anzeigen |
| Produkte bearbeiten                                   | Produkte erstellen und Updates durchführen |
| Sperrliste für Produkte                              | Fügen Sie Produkte zu einer Sperrliste hinzu, die die Verwendung im Dashboard einschränkt. |
| Segmentierung von Kaufeigenschaften bearbeiten             | Segmentierung für Kauf-Event-Eigenschaften aktivieren und deaktivieren |
| Technologiepartner bearbeiten                        | Technologiepartner erstellen und ein Update durchführen |
| Cloud-Datenaufnahme bearbeiten                       | Erstellen, Update und Löschen von Quellen und Synchronisierungen |
| Mehrsprachige Einstellungen anzeigen                    | Mehrsprachige Einstellungen anzeigen |
| Mehrsprachige Ländereinstellungen für die Lokalisierung erstellen           | Erstellen und Update von mehrsprachigen Gebietsschemaeinstellungen für die Lokalisierung |
| Mehrsprachige Lokalisierung-Einstellungen löschen           | Mehrsprachige Lokalisierung-Einstellungen dauerhaft löschen |
| Abos bearbeiten                              | Erstellen und Update von Abo-Gruppen |
| Tags anzeigen                                       | Tags anzeigen |
| Tags bearbeiten                                       | Tags erstellen und Updates durchführen |
| Tags löschen                                     | Tags dauerhaft löschen |
| Teams anzeigen                                      | Teams anzeigen |
| Teams bearbeiten                                      | Teams erstellen und Updates durchführen |
| Teams archivieren                                   | Teams in das Archiv verschieben |
| Datentransformation anzeigen                        | Datentransformationen anzeigen |
| Datentransformation bearbeiten                        | Erstellen und Update von Datentransformationen |
| Kampagnen starten                                | Bestehende Kampagnen starten, stoppen, pausieren oder fortsetzen |
| Canvase starten                                 | Bestehende Canvases starten, stoppen, pausieren oder fortsetzen |
| Canvas-Templates bearbeiten                           | Canvas-Templates erstellen und aktualisieren |
| Kampagnen genehmigen                               | Kampagnen genehmigen oder ablehnen. Der [Genehmigungsworkflow für Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) muss aktiviert sein, damit diese Berechtigung gilt. Diese Einstellung befindet sich derzeit in der Early Access-Phase. Bitte wenden Sie sich an Ihren Account Manager, wenn Sie an einer Teilnahme am Early Access interessiert sind. |
| Canvase genehmigen                                | Canvases genehmigen oder ablehnen. Der [Genehmigungsworkflow für Canvase]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) muss aktiviert sein, damit diese Berechtigung gilt. Diese Einstellung befindet sich derzeit in der Early Access-Phase. Bitte wenden Sie sich an Ihren Account Manager, wenn Sie an einer Teilnahme am Early Access interessiert sind. |
| Platzierungen ansehen                                 | Bannerplatzierung anzeigen |
| Platzierungen bearbeiten                                 | Bannerplatzierungen anzeigen, ohne Änderungen vorzunehmen |
| Platzierungen archivieren                              | Bannerplatzierungen ins Archiv verschieben |
| Push-Einstellungen anzeigen                              | Push-Einstellungen anzeigen |
| Push-Einstellungen bearbeiten                              | Push-Einstellungen erstellen und ein Update durchführen |
| Berichte bearbeiten                                    | Erstellen und Update von Berichten |
| Importierte Nutzer:innen anzeigen                               | CSV-Nutzerimporte anzeigen |
| Nutzer:innen importieren                                    | Nutzer:innen in das Dashboard hochladen |
| Nutzerdaten bearbeiten                                  | Nutzerdaten erstellen und Update durchführen |
| Nutzer:innen zusammenführen anzeigen                                | Eine Liste der Zusammenführungsdatensätze für Nutzer:innen anzeigen |
| Zu löschende Nutzer-Datensätze anzeigen	            	  | Zu löschende Nutzerdatensätze anzeigen |
| Nutzer:innen aus Dashboard löschen	                  | Löschen Sie Nutzer:innen dauerhaft einzeln oder in großen Mengen aus dem Dashboard. |      
| Angepasste KI-Agenten anzeigen                           | Ermöglicht es Nutzer:innen, angepasste KI-Agenten anzuzeigen. |
| Angepasste KI-Agenten bearbeiten                           | Ermöglicht es Nutzer:innen, angepasste KI-Agenten zu erstellen und zu aktualisieren. |
| Archiv Angepasste KI-Agenten                        | Ermöglicht es Nutzer:innen, angepasste KI-Agenten zu archivieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }