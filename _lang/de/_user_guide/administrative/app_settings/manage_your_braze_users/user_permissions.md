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
{% tab Beispiel-Berechtigungssätze %}
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
{% tab Rollenbeispiele %}
| Rollenname | Arbeitsbereich | Berechtigungen  
----------- | ----------- | ---------
| Marketer - Modemarken | {::nomarkdown}[DEV] Modemarke, [QA] Modemarke, [PROD] Modemarke {:/} | "Zugriff auf Kampagnen, Leinwände, Karten, Feature-Flags, Segmente, Mediathek und Präferenzzentrum"<br>"Assets der Medienbibliothek verwalten" |
| Marketer – Hautpflegemarken | {::nomarkdown}[DEV] Hautpflegemarke, [QA] Hautpflegemarke, [PROD] Hautpflegemarke {:/} | "Zugriff auf Kampagnen, Canvase, Cards, Feature-Flags, Segmente, Mediathek und Einstellungen" <br>"Assets der Medienbibliothek verwalten" |
| Benutzerverwaltung - Alle Marken | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Dashboard-Benutzer verwalten"<br>"Teams verwalten" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## Wie unterscheiden sich die Berechtigungen und Rollen von Teams?

{% multi_lang_include permissions.md content="Unterschiede" %}

## Bearbeiten der Berechtigungen eines Benutzers

Um die aktuellen [Admin-](#admin), [Unternehmens-](#company) oder [Arbeitsbereichsberechtigungen](#workspace) eines Benutzers zu bearbeiten, gehen Sie zu **Einstellungen** > **Unternehmensbenutzer** und wählen Sie den Namen des Benutzers.

![Die Seite "Benutzer des Unternehmens" in Braze mit einem Benutzer in den Ergebnissen.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %}){: style="max-width:80%;"}

### Admin

Admins haben Zugriff auf alle Features und können alle Unternehmenseinstellungen ändern. Es gibt auch ein paar Dinge in Braze, die nur Administratoren können. 

Nur Administratoren können das:

- [Genehmigungseinstellungen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval) ändern
- Hinzufügen, Bearbeiten, Löschen, Suspendieren oder Aufheben der Suspendierung anderer [Braze-Benutzer]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)
- Braze-Benutzer als CSV-Datei exportieren

Um Admin-Rechte zu gewähren oder zu entfernen, wählen Sie **Dieser Benutzer ist ein Admin** und dann **Benutzer aktualisieren**.

![Die ausgewählten Nutzerdaten mit dem Kontrollkästchen "Admin" im Fokus.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:40%;"}

{% alert warning %}
Wenn Sie einem Benutzer die Administratorrechte entziehen, kann er erst wieder auf Braze zugreifen, wenn Sie ihm mindestens eine Berechtigung [auf Unternehmens-](#company) oder [Arbeitsbereichsebene](#workspace) zuweisen.
{% endalert %}

### Unternehmen

Um die folgenden Berechtigungen auf Unternehmensebene für einen Benutzer zu verwalten, aktivieren oder deaktivieren Sie das Kästchen neben der jeweiligen Berechtigung. Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

|Berechtigungsname|Beschreibung|
|----------|-----------|
|Unternehmenseinstellungen verwalten|Ermöglicht es Benutzern, jede Unternehmenseinstellung zu ändern.|
|Workspaces erstellen und löschen|Ermöglicht Benutzern das Erstellen und Löschen von Arbeitsbereichen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Workspace

Sie können individuell unterschiedliche Nutzerberechtigungen für jeden zugehörigen Braze-Workspace erteilen. Um deren Berechtigungen auf Arbeitsbereichsebene zu verwalten, wählen Sie **Arbeitsbereiche und Berechtigungen auswählen** und wählen Sie dann deren Berechtigungen manuell aus oder weisen Sie einen [zuvor erstellten](#creating-a-permission-set) Berechtigungssatz zu.

Um individuell unterschiedliche Nutzerberechtigungen für verschiedene Workspaces zu vergeben, wiederholen Sie diesen Vorgang so oft wie nötig. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen](#list-of-permissions).

{% tabs local %}
{% tab manuell auswählen %}
Wählen Sie unter **Arbeitsbereiche** einen oder mehrere Arbeitsbereiche aus der Dropdown-Liste. Wählen Sie dann unter **Berechtigungen** eine oder mehrere Berechtigungen aus der Dropdown-Liste. Sie erhalten diese Berechtigungen nur für die Arbeitsbereiche, die Sie ausgewählt haben. Optional können Sie **Admin-Zugriff aktivieren**, wenn Sie ihnen stattdessen volle Berechtigungen für diesen Arbeitsbereich geben möchten.

Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

![Workspace-Berechtigungen werden in Braze manuell ausgewählt.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})
{% endtab %}

{% tab Berechtigungspaket zuweisen %}
Wählen Sie unter **Arbeitsbereiche** einen oder mehrere Arbeitsbereiche aus der Dropdown-Liste. Wählen Sie dann unter **Berechtigungssätze** einen Berechtigungssatz aus. Sie erhalten diese Berechtigungen nur für die Arbeitsbereiche, die Sie ausgewählt haben.

Wenn Sie fertig sind, wählen Sie **Benutzer aktualisieren**.

![Workspace-Berechtigungen, die als Paket zugewiesen werden.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})
{% endtab %}
{% endtabs %}

## Benutzerberechtigungen exportieren

Um eine Liste Ihrer Benutzer und deren Berechtigungen herunterzuladen, gehen Sie zu **Einstellungen** > **Firmenbenutzer** und wählen Sie dann **Benutzer exportieren**. Eine CSV-Datei wird in Kürze an Ihre E-Mail-Adresse gesendet.

![Die Seite "Unternehmensbenutzer" in Braze mit der Option "Benutzer exportieren" im Fokus.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Liste der Berechtigungen

{% alert important %}
Ab April 2024 ist in Braze für die Erstellung und Aktualisierung von Listen mit Aktionscode die Berechtigung "Zugriff auf Kampagnen, Canvase, Cards, Segmente, Mediathek" erforderlich.
{% endalert %}

|Ebene|Name|Definition|
|---|---|---|
|Admin|Admin|Ermöglicht Benutzern den Zugriff auf alle verfügbaren Funktionen. Dies ist die Standardeinstellung für alle neuen Benutzer. Sie können die Firmeneinstellungen (Firmenname und Zeitzone) aktualisieren, was eingeschränkten Benutzern nicht möglich ist.|
|Unternehmen|Workspaces erstellen und löschen|Ermöglicht Benutzern das Erstellen und Löschen von Arbeitsbereichen.|
|Unternehmen|Unternehmenseinstellungen verwalten|Ermöglicht es Benutzern, jede Unternehmenseinstellung zu ändern.|
|Workspace|Greifen Sie auf Kampagnen, Leinwände, Karten, Inhaltsblöcke, Feature-Flags, Segmente, Medienbibliothek, Standorte, Promotion-Codes und Präferenzzentren zu.|Ermöglicht Benutzern die Anzeige von Kampagnen- und Canvas-Leistungskennzahlen, die Erstellung und Duplizierung von Entwürfen für Kampagnen und Canvases, die Bearbeitung von Kampagnen- und Canvas-Entwürfen und -Vorlagen, die Anzeige von Entwürfen für News Feed, Segmente, Vorlagen und Medien, die Erstellung von Vorlagen, das Hochladen von Medien, die Erstellung oder Aktualisierung von Aktionscodelisten, die Anzeige von Berichten über das Engagement und die Anzeige globaler Nachrichteneinstellungen im Dashboard. Benutzer mit dieser Berechtigung können jedoch keine bestehenden Live-Inhalte anhalten oder bearbeiten.|
|Workspace|Auf Entwicklungskonsole zugreifen|Ermöglicht den vollen Zugriff auf die folgenden Einstellungen und Protokolle:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>API-Schlüssel</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Interne Gruppen</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Nachrichten-Aktivitätsprotokoll</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Event-Nutzerprotokoll</a></li><li><a href='/docs/user_guide/data_and_analytics/cloud_ingestion/'>Datenaufnahme in die Cloud konfigurieren</a></li></ul>{:/}|
|Workspace|Kampagnen genehmigen und ablehnen|Ermöglicht es Benutzern, Kampagnen zu genehmigen oder abzulehnen. Der [Genehmigungsworkflow für Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) muss aktiviert sein, damit diese Berechtigung gilt. Diese Einstellung befindet sich derzeit in der Early Access-Phase. Wenden Sie sich an Ihren Account Manager, wenn Sie Interesse an einer Teilnahme haben.|
|Workspace|Canvase genehmigen und ablehnen|Ermöglicht es Benutzern, Leinwände zu genehmigen oder abzulehnen. Der [Genehmigungsworkflow für Canvase]({{site.baseurl}}/canvas_approval) muss aktiviert sein, damit diese Berechtigung gilt.|
|Workspace|Currents-Integrationen bearbeiten|Ermöglicht es Benutzern, eine Currents-Verbindung zu ändern, einschließlich der Zugangsdaten. Standardmäßig wird Benutzern, denen die Berechtigung "Externe Integrationen" zugewiesen wurde, auch diese Berechtigung zugewiesen.|
|Workspace|Segmente bearbeiten|Ermöglicht Benutzern das Erstellen und Bearbeiten von Segmenten. Sie können auch ohne diese Berechtigung Kampagnen mit bestehenden Segmenten und Filtern erstellen. Sie benötigen diese Berechtigung, um ein Segment aus den Benutzern in einer CSV-Datei zu erstellen oder die Gruppe der Benutzer in der CSV-Datei erneut anzusprechen.|
|Workspace|Nutzerdaten exportieren|Ermöglicht es Benutzern, ihre Benutzerdaten aus Segmenten, Kampagnen und Canvases zu exportieren. Diese Erlaubnis umfasst sensible Nutzer:innen-Daten wie Namen, E-Mail-Adressen und andere gesammelte persönliche Daten (PII). |
|Workspace|Benutzerdaten importieren und aktualisieren|Ermöglicht es Benutzern, CSV- und Update-Dateien von App-Benutzern zu importieren und die Seite Benutzerimport anzuzeigen. Hier können Sie auch den Abonnementstatus eines Benutzers und die Regeln für die An- und Abmeldung seiner Abonnementgruppe bearbeiten.|
|Workspace|Content-Blöcke starten|Ermöglicht es Benutzern, [Inhaltsblöcke]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/) zu starten.|
|Workspace|Präferenzzentren starten|Ermöglicht es Benutzern, [Einstellungszentren]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) zu starten.|
|Workspace|Apps verwalten|Ermöglicht Benutzern die Bearbeitung der **App-Einstellungen**.|
|Workspace|Dashboard-Berechtigungen zum Verwalten von Katalogen|Ermöglicht es Benutzern, Kataloge zu erstellen und zu verwalten.|
|Workspace|Dashboard-Nutzer:innen verwalten| Ermöglicht es Nicht-Administratoren, die Seite **Unternehmensbenutzer** anzuzeigen, zu bearbeiten und zu verwalten sowie die Nutzer:innen des Dashboards in ihrem Workspace zu verwalten, indem sie die Berechtigungen aller Nutzer:innen, einschließlich ihrer eigenen, ändern. Benutzer mit dieser Berechtigung können Nutzer:innen nicht löschen (nur Administratoren können Nutzer:innen löschen).|
|Workspace|E-Mail-Einstellungen verwalten|Ermöglicht es Benutzern, Änderungen an der E-Mail-Konfiguration zu speichern**(Einstellungen** > **E-Mail-Voreinstellungen**).|
|Workspace|Events, Attribute und Käufe verwalten|Ermöglicht es Benutzern, benutzerdefinierte Attribute zu bearbeiten (Benutzer ohne diese Funktion können benutzerdefinierte Attribute weiterhin anzeigen), Eigenschaften von benutzerdefinierten Ereignissen zu bearbeiten und anzuzeigen und Eigenschaften von Produkten unter **Dateneinstellungen** zu bearbeiten und anzuzeigen.|
|Workspace|Externe Integrationen verwalten|Ermöglicht den Zugriff auf alle Registerkarten unter **Technologiepartner** und die Möglichkeit, Braze mit anderen Plattformen zu synchronisieren.|
|Workspace|Feature-Flags verwalten|Erlaubt Nutzern:innen, [Feature-Flags]({{site.baseurl}}/developer_guide/feature_flags/) zu erstellen oder zu bearbeiten.|
|Workspace|Assets in Medienbibliothek verwalten|Ermöglicht Benutzern das Hinzufügen, Bearbeiten und Löschen von Medienbibliothek-Assets.|
|Workspace|Abo-Gruppen verwalten|Ermöglicht es Benutzern, Abonnementgruppen zu erstellen und zu verwalten.|
|Workspace|Tags verwalten|Ermöglicht Benutzern das Bearbeiten oder Löschen von Tags (unter **Tag Management**). Sie benötigen diese Berechtigung nicht, um Tags zu Kampagnen oder Segmenten hinzuzufügen.|
|Workspace|Teams verwalten|Ermöglicht Benutzern die Verwaltung **interner Teams**. Ob Sie diese Berechtigung auswählen können, hängt von Ihrem Vertrag mit Braze ab.|
|Workspace|Transformationen verwalten|Ermöglicht Benutzern das Erstellen und Verwalten von Datenumwandlungen.|
|Workspace|Cards veröffentlichen|Diese Berechtigung ist nur sichtbar, wenn Newsfeed noch in Ihrem Konto aktiviert ist. Newsfeed wird allerdings demnächst eingestellt. Dies betrifft nicht die Inhaltskarten. Ermöglicht es Benutzern, News Feed-Karten zu erstellen und zu bearbeiten. Sie können die News Feed-Karten auch ohne diese Berechtigung ansehen. Wenn Newsfeed bei Ihnen aktiviert ist, sind für den Launch von Content-Blöcken die beiden Berechtigungen "Cards veröffentlichen" und "Content-Blöcke starten" erforderlich.|
|Workspace|Kampagnen und Canvase senden|Ermöglicht es Benutzern, Kampagnen und Canvases zu bearbeiten, zu archivieren und zu beenden, Kampagnen zu erstellen und Canvases zu starten. |
|Workspace|Abrechnungsdetails anzeigen|Ermöglicht es Benutzern, Abonnements und Rechnungen einzusehen.|
|Workspace|Currents-Integration anzeigen|Ermöglicht Benutzern die Anzeige aller Informationen über eine Currents-Verbindung, mit Ausnahme der Anmeldedaten. Standardmäßig erhalten Benutzer, denen die Berechtigung "Zugriff auf Kampagnen, Leinwände, Karten, Inhaltsblöcke, Feature-Flags, Segmente, Mediathek, Standorte, Promotion-Codes und Präferenzzentren" zugewiesen wurde, auch diese Berechtigung.|
|Workspace|Als PII gekennzeichnete angepasste Attribute anzeigen|Erlaubt Nutzern:innen, die keine Administratoren sind, angepasste Attribute anzuzeigen, die sensible Informationen enthalten und als persönlich identifizierbare Informationen (PII) gekennzeichnet sind.|
|Workspace|PII anzeigen|Ermöglicht Nutzern:innen die Anzeige von Feldern mit personenbezogenen Daten (PII), wie von Ihrem Unternehmen im Dashboard definiert. Benutzer können PII-Felder auch auf der Registerkarte **Vorschau als Benutzer** der Nachrichtenvorschau sehen.|
|Workspace|Nutzerprofile PII-konform anzeigen|Ermöglicht Nutzern:innen die Anzeige von Nutzerprofilen, die Felder enthalten, die Ihr Unternehmen als personenbezogene Daten (PII) definiert hat, wobei die PII-Felder jedoch unkenntlich gemacht werden. |
|Workspace|Transformationen anzeigen|Ermöglicht es Benutzern, [Braze Data Transformations]({{site.baseurl}}/user_guide/data/data_transformation/overview/) anzuzeigen.|
|Workspace|Nutzungsdaten anzeigen|Ermöglicht Benutzern die Anzeige der App-Nutzung, einschließlich der Dashboards für die Kanalleistung.|
|Workspace|Doppelte Nutzer:innen zusammenführen|Ermöglicht es Benutzern, doppelte Benutzerprofile zusammenzuführen.|
|Workspace|Vorschau doppelter Nutzer:innen anzeigen|Ermöglicht Benutzern eine Vorschau, welche Benutzerprofile dupliziert sind.|
|Workspace|Canvas-Templates erstellen und bearbeiten|Ermöglicht es Benutzern, Canvas-Vorlagen zu erstellen und zu bearbeiten.|
|Workspace|Canvas-Templates anzeigen|Ermöglicht Benutzern die Ansicht von Canvas-Vorlagen.|
|Workspace|Canvas-Templates archivieren|Ermöglicht es Benutzern, Canvas-Vorlagen zu archivieren.|
|Workspace|Eigenschaftssegmentierung für angepasste Events verwalten|Erlaubt Nutzern:innen, Segmente auf der Grundlage der Eigenschaften Häufigkeit und Häufigkeit von Ereignissen zu erstellen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
