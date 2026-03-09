{% alert important %}
Braze führt [detaillierte Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions) ein, eine flexiblere Methode zur Verwaltung des Zugriffs der Nutzer:innen. Weitere Informationen zum Migrationsprozess, einschließlich der Abbildung von alten Berechtigungen auf granularen Berechtigungen, finden Sie unter [Migration zu granularen Berechtigungen]({{site.baseurl}}/granular_permissions_migration/).
{% endalert %}

## Erstellen eines Berechtigungssatzes

Mit Berechtigungspaketen können Sie Berechtigungen für bestimmte Themenbereiche oder Aktionen bündeln. Sie können Berechtigungssätze auf Dashboard-Nutzer:innen anwenden, die in verschiedenen Workspaces denselben Zugriff benötigen. Um einen Berechtigungssatz zu erstellen, gehen Sie zu **Einstellungen** > **Berechtigungseinstellungen** und wählen Sie dann **Berechtigungssatz erstellen**. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Name|Berechtigungen|
\|-----------|----------------|
|Entwickler| "Zugriff auf Entwicklungskonsole"|.
|Marketer| "Zugriff auf Kampagnen, Canvase, Cards, Feature-Flags, Segmente, Mediathek und Einstellungen" <br> "Assets der Medienbibliothek verwalten"|.
|Benutzerverwaltung|"Dashboard-Benutzer verwalten" <br> "Teams verwalten"|.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Eine Rolle erstellen

Rollen ermöglichen eine bessere Strukturierung durch die Bündelung Ihrer individuell angepassten Berechtigungen mit den Zugriffskontrollen für den Workspace. Das ist besonders nützlich, wenn Sie viele Marken oder regionale Workspaces in einem Dashboard haben. Mit Rollen können Sie Dashboard-Benutzer zu den richtigen Arbeitsbereichen hinzufügen und ihnen direkt die entsprechenden Berechtigungen erteilen. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Rollenname | Arbeitsbereich | Berechtigungen  
----------- | ----------- | ---------
| Marketer – Modemarken | {::nomarkdown}[DEV] Modemarke, [QA] Modemarke, [PROD] Modemarke{:/}| „Zugriff auf Kampagnen, Canvases, Karten, Feature-Flags, Segmente, Medienbibliothek und Präferenzcenter“<br>"Assets der Medienbibliothek verwalten" |
| Marketer – Hautpflegemarken | {::nomarkdown}[DEV] Hautpflegemarke, [QA] Hautpflegemarke, [PROD] Hautpflegemarke{:/}| „Zugriff auf Kampagnen, Canvases, Karten, Feature-Flags, Segmente, Medienbibliothek und Präferenzzentren“ <br>"Assets der Medienbibliothek verwalten" |
| Benutzerverwaltung – Alle Marken | {::nomarkdown}[DEV] Modemarke, [QA] Modemarke, [PROD] Modemarke, [DEV] Hautpflegemarke, [QA] Hautpflegemarke, [PROD] Hautpflegemarke{:/}| „Dashboard-Nutzer:innen verwalten”<br>"Teams verwalten" |
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

| Berechtigungen | Nutzer:innen mit eingeschränkten Rechten können die Berechtigungen anderer Nutzer:innen mit eingeschränkten Rechten bearbeiten, wenn sie die Berechtigung „Dashboard-Nutzer:innen verwalten” aktiviert haben. Sie können auch neue eingeschränkte Nutzer:innen anlegen und deren Berechtigungen ändern. Allerdings können sie keine Unternehmensadministratorkonten erstellen oder verwalten.
| Rollenbeschränkungen | Wenn ein eingeschränkter Nutzer:in über alle Berechtigungen außer „Administrator der App-Gruppe“ verfügt, hat er dennoch Zugriff auf alle anderen Berechtigungen, die normalerweise einem Workspace-Administrator gewährt werden. |
| Sichtbarkeit von Berechtigungen | Wenn für einen eingeschränkten Nutzer die Option „Dashboard-Benutzer verwalten” für eine App-Gruppe (z. B. „Dev”) aktiviert ist, jedoch nicht für eine andere (z. B. „Prod”), werden ihm die Berechtigungen für die App-Gruppe „Prod” in seinem Profil „Benutzer verwalten” nicht angezeigt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Vergleich eingeschränkter Nutzer:innen

| Eingeschränkter Nutzer:in | Beschreibung |
| --- | --- |
| App-Gruppenadministrator | App-Gruppenadministratoren verfügen über Berechtigungen, die speziell für die Verwaltung von App-Gruppen gelten, jedoch nicht über dieselben Befugnisse wie Unternehmensadministratoren. Eingeschränkte Nutzer:innen können Berechtigungen ähnlich denen von Administratoren der App-Gruppen erhalten, wenn sie über die erforderlichen Berechtigungen verfügen. |
| Unternehmensverwaltung | Unternehmensadministratoren verfügen über umfassendere Berechtigungen, einschließlich der Möglichkeit, Dashboard-Nutzer:innen zu löschen. Sie können jedoch ihre eigenen Konten nicht löschen und müssen sich für diese Aktion an einen anderen Unternehmensadministrator wenden. |
| Grundlegende Leseberechtigung | Um auf bestimmte Bereiche des Dashboards, wie beispielsweise die Technologie-Partnerseite, zugreifen zu können, benötigen Nutzer:innen eine grundlegende Leseberechtigung. Dazu gehört, dass „Externe Integrationen verwalten” aktiviert ist und Sie über Berechtigungen für Kampagnen, Canvases, Karten, Segmente und die Medienbibliothek verfügen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Fehler beim eingeschränkten Zugriff

Nutzer:innen können Nachrichten wie „Eingeschränkter Zugriff“ erhalten. Sie verfügen nicht über die erforderlichen Berechtigungen, um auf diese Seite zuzugreifen. In solchen Fällen sollte der Kontoadministrator überprüfen, ob das Problem durch Deaktivieren und erneutes Aktivieren der Berechtigungen der Nutzer:innen behoben werden kann.

{% alert note %}
Es ist nicht möglich, Benutzerberechtigungen von einem Dashboard-Nutzer:in auf einen anderen zu übertragen oder zu importieren.
{% endalert %}

## Bearbeiten der Berechtigungen eines Benutzers

Um die aktuellen Administrator-, Unternehmens- oder Workspace-Berechtigungen einer Nutzer:in zu bearbeiten, navigieren Sie bitte zu **„Einstellungen“** > **„Unternehmensbenutzer“** und wählen Sie den Namen der Nutzer:in aus.

![Die Seite „Unternehmensnutzer:innen“ in Braze mit einer Nutzer:in in den Ergebnissen.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Admin

Admins haben Zugriff auf alle Features und können alle Unternehmenseinstellungen ändern. Sie können:

- [Genehmigungseinstellungen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval) ändern
- Hinzufügen, Bearbeiten, Löschen, Suspendieren oder Aufheben der Suspendierung anderer [Braze-Benutzer]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)
- Braze-Benutzer als CSV-Datei exportieren

Um Admin-Rechte zu gewähren oder zu entfernen, wählen Sie **Dieser Benutzer ist ein Admin** und dann **Benutzer aktualisieren**.

![Die Details der ausgewählten Nutzer:in mit aktiviertem Admin-Kontrollkästchen.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Wenn Sie einem Nutzer:in die Administratorrechte entziehen, kann er nicht mehr auf Braze zugreifen, bis Sie ihm mindestens eine Berechtigung [auf Unternehmens- oder Workspace-Ebene]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions&tab=company#legacypermissions_editing-a-users-permissions) zuweisen.
{% endalert %}

{% endtab %}
{% tab Company %}

### Unternehmen

Um die folgenden Berechtigungen auf Unternehmensebene für einen Benutzer zu verwalten, aktivieren oder deaktivieren Sie das Kästchen neben der jeweiligen Berechtigung. Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

|Berechtigungsname|Beschreibung|
|----------|-----------|
|Unternehmenseinstellungen verwalten|Ermöglicht es Benutzern, jede Unternehmenseinstellung zu ändern.|
|Workspaces erstellen und löschen|Ermöglicht Benutzern das Erstellen und Löschen von Arbeitsbereichen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Workspace

Sie können individuell unterschiedliche Nutzerberechtigungen für jeden zugehörigen Braze-Workspace erteilen. Um die Berechtigungen auf Workspace-Ebene zu verwalten, wählen Sie **Workspaces und Berechtigungen auswählen** und wählen dann die Berechtigungen manuell aus, um einen [zuvor erstellten]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_creating-a-permission-set) Berechtigungssatz auszuwählen oder zuzuweisen.

Um individuell unterschiedliche Nutzerberechtigungen für verschiedene Workspaces zu vergeben, wiederholen Sie diesen Vorgang so oft wie nötig. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Wählen Sie unter **Arbeitsbereiche** einen oder mehrere Arbeitsbereiche aus der Dropdown-Liste. Wählen Sie dann unter **Berechtigungen** eine oder mehrere Berechtigungen aus der Dropdown-Liste. Braze erteilt diese Berechtigungen ausschließlich für die von Ihnen ausgewählten Workspaces. Optional können Sie **Admin-Zugriff aktivieren**, wenn Sie ihnen stattdessen volle Berechtigungen für diesen Arbeitsbereich geben möchten.

Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

![Berechtigungen auf Workspace-Ebene, die manuell in Braze ausgewählt werden.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual_legacy.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Wählen Sie unter **Arbeitsbereiche** einen oder mehrere Arbeitsbereiche aus der Dropdown-Liste. Wählen Sie dann unter **Berechtigungssätze** einen Berechtigungssatz aus. Braze erteilt diese Berechtigungen ausschließlich für die von Ihnen ausgewählten Workspaces.

Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

![Berechtigungen auf Workspace-Ebene, die über eine Berechtigungsgruppe in Braze zugewiesen werden.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set_legacy.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Benutzerberechtigungen exportieren

Um eine Liste Ihrer Nutzer:innen und deren Berechtigungen herunterzuladen, gehen Sie zu **Einstellungen** > **Firmennutzer:innen** und wählen Sie dann **Nutzer:innen exportieren**. Eine CSV-Datei wird in Kürze an Ihre E-Mail-Adresse gesendet.

![Die Seite „Unternehmensnutzer:innen“ in Braze mit der Option „Nutzer:innen exportieren“ im Fokus.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Liste der Berechtigungen

{% alert important %}
Ab April 2024 ist in Braze für die Erstellung und Aktualisierung von Listen mit Aktionscode die Berechtigung "Zugriff auf Kampagnen, Canvase, Cards, Segmente, Mediathek" erforderlich.
{% endalert %}

|Ebene|Name|Definition|
|---|---|---|
|Admin|Admin|Ermöglicht Benutzern den Zugriff auf alle verfügbaren Funktionen. Dies ist die Standardeinstellung für alle neuen Benutzer. Sie können die Firmeneinstellungen (Firmenname und Zeitzone) aktualisieren, was eingeschränkten Benutzern nicht möglich ist.|
|Unternehmen|Workspaces erstellen und löschen|Ermöglicht Benutzern das Erstellen und Löschen von Arbeitsbereichen.|
|Unternehmen|Unternehmenseinstellungen verwalten|Ermöglicht es Benutzern, jede Unternehmenseinstellung zu ändern.|
|Workspace|Greifen Sie auf Kampagnen, Leinwände, Karten, Inhaltsblöcke, Feature-Flags, Segmente, Medienbibliothek, Standorte, Promotion-Codes und Präferenzzentren zu.|Erlaubt Benutzern die Anzeige von Metriken zur Performance von Kampagnen und Canvas, die Erstellung und Duplizierung von Entwürfen für Kampagnen und Canvase, die Bearbeitung von Kampagnen- und Canvas-Entwürfen und -Vorlagen, die Anzeige von Entwürfen für Segmente, Vorlagen und Medien, die Erstellung von Vorlagen, den Upload von Medien, die Erstellung oder Aktualisierung von Code-Listen für Aktionen, die Anzeige von Engagement-Berichten und die Anzeige globaler Einstellungen für Nachrichten im Dashboard. Benutzer mit dieser Berechtigung können jedoch keine bestehenden Live-Inhalte anhalten oder bearbeiten.|
|Workspace|Auf Entwicklungskonsole zugreifen|Ermöglicht den vollen Zugriff auf die folgenden Einstellungen und Protokolle:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>API-Schlüssel</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Interne Gruppen</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Nachrichten-Aktivitätsprotokoll</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Event-Nutzerprotokoll</a></li></ul>{:/}|
|Workspace|Kampagnen genehmigen und ablehnen|Ermöglicht es Benutzern, Kampagnen zu genehmigen oder abzulehnen. Der [Genehmigungsworkflow für Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) muss aktiviert sein, damit diese Berechtigung gilt. Diese Einstellung befindet sich derzeit in der Early Access-Phase. Wenden Sie sich an Ihren Account Manager, wenn Sie Interesse an einer Teilnahme haben.|
|Workspace|Canvase genehmigen und ablehnen|Ermöglicht es Benutzern, Leinwände zu genehmigen oder abzulehnen. Der [Genehmigungsworkflow für Canvase]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) muss aktiviert sein, damit diese Berechtigung gilt.|
|Workspace|Currents-Integrationen bearbeiten|Ermöglicht es Benutzern, eine Currents-Verbindung zu ändern, einschließlich der Zugangsdaten. Standardmäßig wird Benutzern, denen die Berechtigung "Externe Integrationen" zugewiesen wurde, auch diese Berechtigung zugewiesen.|
|Workspace|Segmente bearbeiten|Ermöglicht Benutzern das Erstellen und Bearbeiten von Segmenten. Sie können auch ohne diese Berechtigung Kampagnen mit bestehenden Segmenten und Filtern erstellen. Sie benötigen diese Berechtigung, um ein Segment aus den Benutzern in einer CSV-Datei zu erstellen oder die Gruppe der Benutzer in der CSV-Datei erneut anzusprechen.|
|Workspace|Nutzerdaten exportieren|Ermöglicht es Benutzern, ihre Benutzerdaten aus Segmenten, Kampagnen und Canvases zu exportieren. Diese Erlaubnis umfasst sensible Nutzer:innen-Daten wie Namen, E-Mail-Adressen und andere gesammelte persönliche Daten (PII). Um CSV-Dateien aus dem Dashboard zu exportieren, benötigen Sie diese Berechtigung sowie die Berechtigung „PII anzeigen“.|
|Workspace|Benutzerdaten importieren und aktualisieren|Ermöglicht es Benutzern, CSV- und Update-Dateien von App-Benutzern zu importieren und die Seite Benutzerimport anzuzeigen. Hier können Sie auch den Abonnementstatus eines Benutzers und die Regeln für die An- und Abmeldung seiner Abonnementgruppe bearbeiten.|
|Workspace|Content-Blöcke starten und verwalten|Ermöglicht es Nutzer:innen[, Content-Blöcke]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/) zu starten und zu verwalten.|
|Workspace|Präferenzzentren starten|Ermöglicht es Benutzern, [Einstellungszentren]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) zu starten.|
|Workspace|Apps verwalten|Ermöglicht Benutzern die Bearbeitung der **App-Einstellungen**.|
|Workspace|Dashboard-Berechtigungen zum Verwalten von Katalogen|Ermöglicht es Benutzern, Kataloge zu erstellen und zu verwalten.|
|Workspace|Dashboard-Nutzer:innen verwalten| Ermöglicht es Nicht-Administratoren, die Seite **Unternehmensbenutzer** anzuzeigen, zu bearbeiten und zu verwalten sowie die Nutzer:innen des Dashboards in ihrem Workspace zu verwalten, indem sie die Berechtigungen aller Nutzer:innen, einschließlich ihrer eigenen, ändern. Benutzer mit dieser Berechtigung können Nutzer:innen nicht löschen (nur Administratoren können Nutzer:innen löschen).<br><br>Dies entspricht der bisherigen Berechtigung`MANAGE_DEVELOPERS_AND_PERMISSIONS`.|
|Workspace|E-Mail-Einstellungen verwalten|Ermöglicht es Benutzern, Änderungen an der E-Mail-Konfiguration zu speichern**(Einstellungen** > **E-Mail-Voreinstellungen**).|
|Workspace|Events, Attribute und Käufe verwalten|Ermöglicht es Benutzern, benutzerdefinierte Attribute zu bearbeiten (Benutzer ohne diese Funktion können benutzerdefinierte Attribute weiterhin anzeigen), Eigenschaften von benutzerdefinierten Ereignissen zu bearbeiten und anzuzeigen und Eigenschaften von Produkten unter **Dateneinstellungen** zu bearbeiten und anzuzeigen.|
|Workspace|Externe Integrationen verwalten|Erlaubt den Zugriff auf alle Tabs unter **Technologiepartner**, die Möglichkeit, Braze mit anderen Plattformen zu synchronisieren, und den Zugriff auf die Verwaltung der [Datenaufnahme in der Cloud]({{site.baseurl}}/user_guide/data/cloud_ingestion/).|
|Workspace|Feature-Flags verwalten|Erlaubt Nutzern:innen, [Feature-Flags]({{site.baseurl}}/developer_guide/feature_flags/) zu erstellen oder zu bearbeiten.|
|Workspace|Assets in Medienbibliothek verwalten|Ermöglicht Benutzern das Hinzufügen, Bearbeiten und Löschen von Medienbibliothek-Assets.|
|Workspace|Abo-Gruppen verwalten|Ermöglicht es Benutzern, Abonnementgruppen zu erstellen und zu verwalten.|
|Workspace|Tags verwalten|Ermöglicht Benutzern das Bearbeiten oder Löschen von Tags (unter **Tag Management**). Sie benötigen diese Berechtigung nicht, um Tags zu Kampagnen oder Segmenten hinzuzufügen.|
|Workspace|Teams verwalten|Ermöglicht Benutzern die Verwaltung **interner Teams**. Ob Sie diese Berechtigung auswählen können, hängt von Ihrem Vertrag mit Braze ab.<br><br>Dies entspricht der bisherigen Berechtigung`MANAGE_TERRITORIES`.|
|Workspace|Transformationen verwalten|Ermöglicht Benutzern das Erstellen und Verwalten von Datenumwandlungen.|
|Workspace|Kampagnen und Canvase senden|Ermöglicht es Benutzern, Kampagnen und Canvases zu bearbeiten, zu archivieren und zu beenden, Kampagnen zu erstellen und Canvases zu starten. |
|Workspace|Abrechnungsdetails anzeigen|Ermöglicht es Benutzern, Abonnements und Rechnungen einzusehen.|
|Workspace|Currents-Integration anzeigen|Ermöglicht Benutzern die Anzeige aller Informationen über eine Currents-Verbindung, mit Ausnahme der Anmeldedaten. Standardmäßig erhalten Benutzer, denen die Berechtigung "Zugriff auf Kampagnen, Leinwände, Karten, Inhaltsblöcke, Feature-Flags, Segmente, Mediathek, Standorte, Promotion-Codes und Präferenzzentren" zugewiesen wurde, auch diese Berechtigung.|
|Workspace|Als PII gekennzeichnete angepasste Attribute anzeigen|Erlaubt Nutzern:innen, die keine Administratoren sind, angepasste Attribute anzuzeigen, die sensible Informationen enthalten und als persönlich identifizierbare Informationen (PII) gekennzeichnet sind.|
|Workspace|PII anzeigen|Ermöglicht Nutzern:innen die Anzeige von Feldern mit personenbezogenen Daten (PII), wie von Ihrem Unternehmen im Dashboard definiert. Benutzer können PII-Felder auch auf der Registerkarte **Vorschau als Benutzer** der Nachrichtenvorschau sehen.<br><br>Sie benötigen diese Berechtigung, um den [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/) zu verwenden, da er direkten Zugriff auf einige Kundendaten erlaubt. Um CSV-Dateien aus dem Dashboard zu exportieren, benötigen Nutzer:innen sowohl diese Berechtigung als auch die Berechtigung „Nutzerdaten exportieren“.|
|Workspace|Nutzerprofile PII-konform anzeigen|Ermöglicht Nutzern:innen die Anzeige von Nutzerprofilen, die Felder enthalten, die Ihr Unternehmen als personenbezogene Daten (PII) definiert hat, wobei die PII-Felder jedoch unkenntlich gemacht werden.<br><br>Sie benötigen diese Berechtigung, um die Nutzersuche zu verwenden. |
|Workspace|Transformationen anzeigen|Ermöglicht es Benutzern, [Braze Data Transformations]({{site.baseurl}}/user_guide/data/data_transformation/overview/) anzuzeigen.|
|Workspace|Nutzungsdaten anzeigen|Ermöglicht Benutzern die Anzeige der App-Nutzung, einschließlich der Dashboards für die Kanalleistung.|
|Workspace|Doppelte Nutzer:innen zusammenführen|Ermöglicht es Benutzern, doppelte Benutzerprofile zusammenzuführen.|
|Workspace|Vorschau doppelter Nutzer:innen anzeigen|Ermöglicht Benutzern eine Vorschau, welche Benutzerprofile dupliziert sind.|
|Workspace|Canvas-Templates erstellen und bearbeiten|Ermöglicht es Benutzern, Canvas-Vorlagen zu erstellen und zu bearbeiten.|
|Workspace|Canvas-Templates anzeigen|Ermöglicht Benutzern die Ansicht von Canvas-Vorlagen.|
|Workspace|Canvas-Templates archivieren|Ermöglicht es Benutzern, Canvas-Vorlagen zu archivieren.|
|Workspace|Eigenschaftssegmentierung für angepasste Events verwalten|Erlaubt Nutzern:innen, Segmente auf der Grundlage der Eigenschaften Häufigkeit und Häufigkeit von Ereignissen zu erstellen.|
|Workspace|Startseiten veröffentlichen|Erlaubt es Nutzer:innen, [Landing Pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/) zu veröffentlichen.|
|Workspace|Entwürfe für Startseite erstellen|Erlaubt Nutzern:innen, Entwürfe für Landing Pages zu erstellen und zu speichern.|
|Workspace|Startseiten aufrufen|Erlaubt Nutzern:innen den Zugriff auf die Seite **Landing Pages**.|
|Workspace|Landing-Page-Templates erstellen und bearbeiten|Erlaubt Nutzern:innen die Erstellung und Bearbeitung von Landing Page Templates.|
|Workspace|Landing-Page-Templates anzeigen|Erlaubt Nutzern:innen die Anzeige von Landing Page Templates.|
|Workspace|Landing-Page-Templates archivieren|Erlaubt Nutzern:innen die Archivierung von Landing Page Templates.|
|Workspace|Angepasste KI-Agenten anzeigen|Ermöglicht es Nutzer:innen, [benutzerdefinierte KI-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/) anzuzeigen. Dieses Feature befindet sich derzeit in der Beta-Phase.|
|Workspace|Angepasste KI-Agenten erstellen|Es ist zulässig, dass Nutzer:innen benutzerdefinierte KI-Agenten erstellen. Dieses Feature befindet sich derzeit in der Beta-Phase.|
|Workspace|Angepasste KI-Agenten bearbeiten|Es ist zulässig, dass Nutzer:innen benutzerdefinierte KI-Agenten bearbeiten. Dieses Feature befindet sich derzeit in der Beta-Phase.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
