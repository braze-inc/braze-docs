---
nav_title: Berechtigungen
article_title: Braze-Berechtigungen
page_order: 2
page_type: reference
description: "Dieser Artikel erläutert Nutzerberechtigungen in Braze. Hier erfahren Sie, wie Sie Benutzerberechtigungen bearbeiten und festlegen und damit bestimmen, wer auf Ihre Apps im Dashboard zugreifen darf."
tool: Dashboard

---

# Braze-Berechtigungen

> Lernen Sie, wie Sie Berechtigungssätze erstellen, Rollen erstellen, Benutzerberechtigungen bearbeiten und Benutzerberechtigungen exportieren, damit Sie sicherstellen können, dass Ihre Benutzer nur auf die Arbeitsbereiche und Funktionen zugreifen, die sie am meisten benötigen.

## Erstellen eines Berechtigungssatzes

Mit Berechtigungspaketen können Sie Berechtigungen für bestimmte Themenbereiche oder Aktionen bündeln. Sie können auf Dashboard-Benutzer angewendet werden, die in verschiedenen Arbeitsbereichen denselben Zugriff benötigen. Um einen Berechtigungssatz zu erstellen, gehen Sie zu **Einstellungen** > **Berechtigungseinstellungen** und wählen Sie dann **Berechtigungssatz erstellen**. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen](#list-of-permissions).

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

Rollen ermöglichen eine bessere Strukturierung durch die Bündelung Ihrer individuell angepassten Berechtigungen mit den Zugriffskontrollen für den Workspace. Das ist besonders nützlich, wenn Sie viele Marken oder regionale Workspaces in einem Dashboard haben. Mit Rollen können Sie Dashboard-Benutzer zu den richtigen Arbeitsbereichen hinzufügen und ihnen direkt die entsprechenden Berechtigungen erteilen. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen](#list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Rollenname | Arbeitsbereich | Berechtigungen  
----------- | ----------- | ---------
| Marketer - Modemarken | {::nomarkdown}[DEV] Modemarke, [QA] Modemarke, [PROD] Modemarke {:/} | "Zugriff auf Kampagnen, Canvase, Karten, Feature-Flags, Segmente, Mediathek und Präferenzzentrum"<br>"Assets der Medienbibliothek verwalten" |
| Marketer - Hautpflegemarken | {::nomarkdown}[DEV] Hautpflegemarke, [QA] Hautpflegemarke, [PROD] Hautpflegemarke {:/} | "Zugriff auf Kampagnen, Canvase, Karten, Feature-Flags, Segmente, Mediathek und Präferenzzentren" <br>"Assets der Medienbibliothek verwalten" |
| Benutzerverwaltung - Alle Marken | {::nomarkdown}[DEV] Modemarke, [QA] Modemarke, [PROD] Modemarke, [DEV] Hautpflegemarke, [QA] Hautpflegemarke, [PROD] Hautpflegemarke {:/} | "Dashboard Nutzer:innen verwalten"<br>"Teams verwalten" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## Wie unterscheiden sich die Berechtigungen und Rollen von Teams?

{% multi_lang_include permissions.md content="Differences" %}

### Überlegungen zum Hinzufügen von Nutzer:innen zu Teams

Es kann zu Schwierigkeiten kommen, wenn Sie versuchen, im Braze-Dashboard Berechtigungen zu speichern, insbesondere wenn Sie Nutzer:innen zu einem Workspace oder zu einem Team hinzufügen oder entfernen. Der Button **Nutzer:innen speichern/aktualisieren** kann ausgegraut werden, wenn die Berechtigungen für den Nutzer:innen mit denen identisch sind, die er bereits auf Workspace-Ebene hat. Diese Einschränkung besteht, weil es keinen Nutzen hat, ein Team zu haben, wenn alle Nutzer:innen die gleichen Berechtigungen wie der gesamte Workspace besitzen.

Um einen Nutzer:innen erfolgreich zu einem Team hinzuzufügen und dabei die gleichen Berechtigungen beizubehalten, vergeben Sie keine Berechtigungen auf der Ebene des Workspace. Vergeben Sie stattdessen Berechtigungen ausschließlich auf der Ebene des Teams.

## Eingeschränkte Nutzer:innen

Eingeschränkte Nutzer:innen verfügen über bestimmte Berechtigungen, die es ihnen erlauben, bestimmte Aspekte des Braze-Dashboards zu verwalten, während sie im Vergleich zu Unternehmensadministratoren und Workspace-Administratoren Einschränkungen haben.

| Berechtigungen | Eingeschränkte Nutzer:innen können die Berechtigungen anderer eingeschränkter Nutzer:innen bearbeiten, wenn sie die Berechtigung "Dashboard-Benutzer verwalten" aktiviert haben. Sie können auch neue eingeschränkte Nutzer:innen erstellen und deren Berechtigungen ändern. Sie können jedoch keine Firmenadministrationskonten erstellen oder verwalten. |
| Rollenbeschränkungen | Wenn ein Nutzer:innen über alle Rechte außer "App-Gruppen-Admin" verfügt, hat er dennoch Zugriff auf alle anderen Rechte, die normalerweise einem Workspace-Admin gewährt werden. |
| Sichtbarkeit von Berechtigungen | Wenn ein eingeschränkter Benutzer "Dashboard-Benutzer verwalten" für eine App-Gruppe (z.B. Dev), aber nicht für eine andere (z.B. Prod) aktiviert hat, sieht er in seinem Profil "Benutzer verwalten" die Berechtigungen der App-Gruppe Prod nicht. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Nutzer:innen mit Einschränkungen vergleichen

| Eingeschränkter Nutzertyp:in | Beschreibung |
| --- | --- |
| App-Gruppe verwalten | App-Gruppen-Admins verfügen über spezielle Berechtigungen für die Verwaltung von App-Gruppen, haben aber nicht die gleichen Befugnisse wie Unternehmens-Admins. Eingeschränkte Nutzer:innen können ähnliche Rechte wie App-Gruppen-Admins erben, wenn sie die erforderlichen Berechtigungen aktiviert haben. |
| Unternehmen admin | Unternehmensadministratoren haben umfassendere Berechtigungen, einschließlich der Möglichkeit, Nutzer:innen des Dashboards zu löschen. Sie können jedoch nicht ihre eigenen Konten löschen und müssen sich für diese Aktion an einen anderen Unternehmensadministrator wenden. |
| Grundlegende Nur-Lese-Erlaubnis | Für den Zugriff auf bestimmte Teile des Dashboards, wie z.B. die Technologie-Partnerseite, müssen Nutzer:innen über eine grundlegende Leseberechtigung verfügen. Dazu gehört, dass Sie "Externe Integrationen verwalten" aktiviert haben, zusammen mit den Berechtigungen für den Zugriff auf Kampagnen, Canvase, Karten, Segmente und die Mediathek. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Begrenzter Zugriffsfehler

Nutzer:innen erhalten möglicherweise Nachrichten wie "Eingeschränkter Zugang. Sie haben keine Berechtigung zum Zugriff auf diese Seite." In solchen Fällen sollte der Kontoverwalter prüfen, ob er das Problem durch Deaktivieren und Wiederaktivieren der Nutzer:innen-Berechtigungen lösen kann.

{% alert note %}
Es ist nicht möglich, Nutzer:innen von einem Dashboard-Benutzer zu einem anderen zusammenzuführen oder zu importieren.
{% endalert %}

## Bearbeiten der Berechtigungen eines Benutzers

Um die aktuellen Admin-, Unternehmens- oder Workspace-Berechtigungen eines Nutzers zu bearbeiten, gehen Sie zu **Einstellungen** > **Unternehmensnutzer:innen** und wählen Sie dann den Namen des Nutzers aus.

![Die Seite "Benutzer des Unternehmens" in Braze mit einem Nutzer:innen in der Ergebnisliste.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %}){: style="max-width:80%;"}

{% tabs local %}
{% tab Admin %}

### Admin

Admins haben Zugriff auf alle Features und können alle Unternehmenseinstellungen ändern. Sie können:

- [Genehmigungseinstellungen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval) ändern
- Hinzufügen, Bearbeiten, Löschen, Suspendieren oder Aufheben der Suspendierung anderer [Braze-Benutzer]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)
- Braze-Benutzer als CSV-Datei exportieren

Um Admin-Rechte zu gewähren oder zu entfernen, wählen Sie **Dieser Benutzer ist ein Admin** und dann **Benutzer aktualisieren**.

![Die Details des ausgewählten Nutzer:innen mit dem Kontrollkästchen admin im Fokus.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:40%;"}

{% alert warning %}
Wenn Sie einem Benutzer die Administratorrechte entziehen, kann er erst wieder auf Braze zugreifen, wenn Sie ihm mindestens eine Berechtigung [auf Unternehmens-](#company) oder [Arbeitsbereichsebene](#workspace) zuweisen.
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

Sie können individuell unterschiedliche Nutzerberechtigungen für jeden zugehörigen Braze-Workspace erteilen. Um die Berechtigungen auf Workspace-Ebene zu verwalten, wählen Sie **Workspaces und Berechtigungen auswählen** und wählen dann die Berechtigungen manuell aus, um einen [zuvor erstellten](#creating-a-permission-set) Berechtigungssatz auszuwählen oder zuzuweisen.

Um individuell unterschiedliche Nutzerberechtigungen für verschiedene Workspaces zu vergeben, wiederholen Sie diesen Vorgang so oft wie nötig. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen](#list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Wählen Sie unter **Arbeitsbereiche** einen oder mehrere Arbeitsbereiche aus der Dropdown-Liste. Wählen Sie dann unter **Berechtigungen** eine oder mehrere Berechtigungen aus der Dropdown-Liste. Sie erhalten diese Berechtigungen nur für die Arbeitsbereiche, die Sie ausgewählt haben. Optional können Sie **Admin-Zugriff aktivieren**, wenn Sie ihnen stattdessen volle Berechtigungen für diesen Arbeitsbereich geben möchten.

Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

![Berechtigungen auf Workspace-Ebene werden in Braze manuell ausgewählt.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Wählen Sie unter **Arbeitsbereiche** einen oder mehrere Arbeitsbereiche aus der Dropdown-Liste. Wählen Sie dann unter **Berechtigungssätze** einen Berechtigungssatz aus. Sie erhalten diese Berechtigungen nur für die Arbeitsbereiche, die Sie ausgewählt haben.

Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

![Berechtigungen auf Workspace-Ebene werden über eine Berechtigungsgruppe in Braze zugewiesen.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Benutzerberechtigungen exportieren

Um eine Liste Ihrer Nutzer:innen und deren Berechtigungen herunterzuladen, gehen Sie zu **Einstellungen** > **Firmennutzer:innen** und wählen Sie dann **Nutzer:innen exportieren**. Eine CSV-Datei wird in Kürze an Ihre E-Mail-Adresse gesendet.

![Die Seite "Unternehmen Nutzer:innen" in Braze mit der Option "Nutzer:innen exportieren" im Fokus.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

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
|Workspace|Nutzerdaten exportieren|Ermöglicht es Benutzern, ihre Benutzerdaten aus Segmenten, Kampagnen und Canvases zu exportieren. Diese Erlaubnis umfasst sensible Nutzer:innen-Daten wie Namen, E-Mail-Adressen und andere gesammelte persönliche Daten (PII). |
|Workspace|Benutzerdaten importieren und aktualisieren|Ermöglicht es Benutzern, CSV- und Update-Dateien von App-Benutzern zu importieren und die Seite Benutzerimport anzuzeigen. Hier können Sie auch den Abonnementstatus eines Benutzers und die Regeln für die An- und Abmeldung seiner Abonnementgruppe bearbeiten.|
|Workspace|Content-Blöcke starten und verwalten|Erlaubt es Nutzern:innen, [Content-Blöcke]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/) zu starten und zu verwalten.|
|Workspace|Präferenzzentren starten|Ermöglicht es Benutzern, [Einstellungszentren]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) zu starten.|
|Workspace|Apps verwalten|Ermöglicht Benutzern die Bearbeitung der **App-Einstellungen**.|
|Workspace|Dashboard-Berechtigungen zum Verwalten von Katalogen|Ermöglicht es Benutzern, Kataloge zu erstellen und zu verwalten.|
|Workspace|Dashboard-Nutzer:innen verwalten| Ermöglicht es Nicht-Administratoren, die Seite **Unternehmensbenutzer** anzuzeigen, zu bearbeiten und zu verwalten sowie die Nutzer:innen des Dashboards in ihrem Workspace zu verwalten, indem sie die Berechtigungen aller Nutzer:innen, einschließlich ihrer eigenen, ändern. Benutzer mit dieser Berechtigung können Nutzer:innen nicht löschen (nur Administratoren können Nutzer:innen löschen).|
|Workspace|E-Mail-Einstellungen verwalten|Ermöglicht es Benutzern, Änderungen an der E-Mail-Konfiguration zu speichern**(Einstellungen** > **E-Mail-Voreinstellungen**).|
|Workspace|Events, Attribute und Käufe verwalten|Ermöglicht es Benutzern, benutzerdefinierte Attribute zu bearbeiten (Benutzer ohne diese Funktion können benutzerdefinierte Attribute weiterhin anzeigen), Eigenschaften von benutzerdefinierten Ereignissen zu bearbeiten und anzuzeigen und Eigenschaften von Produkten unter **Dateneinstellungen** zu bearbeiten und anzuzeigen.|
|Workspace|Externe Integrationen verwalten|Erlaubt den Zugriff auf alle Tabs unter **Technologiepartner**, die Möglichkeit, Braze mit anderen Plattformen zu synchronisieren, und den Zugriff auf die Verwaltung der [Datenaufnahme in der Cloud]({{site.baseurl}}/user_guide/data/cloud_ingestion/).|
|Workspace|Feature-Flags verwalten|Erlaubt Nutzern:innen, [Feature-Flags]({{site.baseurl}}/developer_guide/feature_flags/) zu erstellen oder zu bearbeiten.|
|Workspace|Assets in Medienbibliothek verwalten|Ermöglicht Benutzern das Hinzufügen, Bearbeiten und Löschen von Medienbibliothek-Assets.|
|Workspace|Abo-Gruppen verwalten|Ermöglicht es Benutzern, Abonnementgruppen zu erstellen und zu verwalten.|
|Workspace|Tags verwalten|Ermöglicht Benutzern das Bearbeiten oder Löschen von Tags (unter **Tag Management**). Sie benötigen diese Berechtigung nicht, um Tags zu Kampagnen oder Segmenten hinzuzufügen.|
|Workspace|Teams verwalten|Ermöglicht Benutzern die Verwaltung **interner Teams**. Ob Sie diese Berechtigung auswählen können, hängt von Ihrem Vertrag mit Braze ab.|
|Workspace|Transformationen verwalten|Ermöglicht Benutzern das Erstellen und Verwalten von Datenumwandlungen.|
|Workspace|Kampagnen und Canvase senden|Ermöglicht es Benutzern, Kampagnen und Canvases zu bearbeiten, zu archivieren und zu beenden, Kampagnen zu erstellen und Canvases zu starten. |
|Workspace|Abrechnungsdetails anzeigen|Ermöglicht es Benutzern, Abonnements und Rechnungen einzusehen.|
|Workspace|Currents-Integration anzeigen|Ermöglicht Benutzern die Anzeige aller Informationen über eine Currents-Verbindung, mit Ausnahme der Anmeldedaten. Standardmäßig erhalten Benutzer, denen die Berechtigung "Zugriff auf Kampagnen, Leinwände, Karten, Inhaltsblöcke, Feature-Flags, Segmente, Mediathek, Standorte, Promotion-Codes und Präferenzzentren" zugewiesen wurde, auch diese Berechtigung.|
|Workspace|Als PII gekennzeichnete angepasste Attribute anzeigen|Erlaubt Nutzern:innen, die keine Administratoren sind, angepasste Attribute anzuzeigen, die sensible Informationen enthalten und als persönlich identifizierbare Informationen (PII) gekennzeichnet sind.|
|Workspace|PII anzeigen|Ermöglicht Nutzern:innen die Anzeige von Feldern mit personenbezogenen Daten (PII), wie von Ihrem Unternehmen im Dashboard definiert. Benutzer können PII-Felder auch auf der Registerkarte **Vorschau als Benutzer** der Nachrichtenvorschau sehen.<br><br>Sie benötigen diese Berechtigung, um den [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/) zu verwenden, da er direkten Zugriff auf einige Kundendaten erlaubt.|
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
|Workspace|Angepasste KI-Agenten anzeigen|Erlaubt Nutzern:innen, [angepasste KI-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/) anzuzeigen. Dieses Feature befindet sich derzeit in der Beta-Phase.|
|Workspace|Angepasste KI-Agenten erstellen|Erlaubt Nutzern:innen, angepasste KI-Agenten zu erstellen. Dieses Feature befindet sich derzeit in der Beta-Phase.|
|Workspace|Angepasste KI-Agenten bearbeiten|Erlaubt Nutzern:innen, angepasste KI-Agenten zu bearbeiten. Dieses Feature befindet sich derzeit in der Beta-Phase.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
