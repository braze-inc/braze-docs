---
nav_title: Teams
article_title: Teams
page_order: 4
page_type: reference
description: "Dieser referenzierte Artikel beschreibt, wie Sie Braze Teams im Dashboard verwenden können. Hier erfahren Sie, wie Sie Teams erstellen, Rollen zuweisen und Tags und Filter zuordnen können."

---

# Teams

> Als Braze-Administrator können Sie die Nutzer:innen Ihres Unternehmens in Teams mit unterschiedlichen Benutzerrollen und Berechtigungen gruppieren. Dies ermöglicht es Ihnen, mehrere, voneinander unabhängige Gruppen von Unternehmensnutzern:innen in einem Workspace zusammenarbeiten zu lassen, indem die Arten von Inhalten, die bearbeitet werden können, voneinander getrennt werden.

Teams können nach Standort, Sprache und angepassten Attributen eingerichtet werden, so dass Teammitglieder und Nicht-Teammitglieder unterschiedlichen Zugriff auf Messaging Features und Kundendaten haben. Team-Filter und Tags können über verschiedene Engagement-Tools zugewiesen werden. Es gibt keine Begrenzung hinsichtlich der Anzahl der Teams, die Sie in Ihrem Workspace erstellen können.

Teams sind nicht für alle Braze-Verträge verfügbar. Um auf dieses Feature zuzugreifen, wenden Sie sich bitte an Ihren Braze-Account Manager oder [kontaktieren Sie uns](mailto:success@braze.com) für eine Beratung.

## Wie unterscheiden sich Teams von Berechtigungsgruppen und Rollen?

{% multi_lang_include permissions.md content="Differences" %}

## Teams erstellen {#creating-teams}

Gehen Sie zu **Einstellungen** > **Interne Teams** und wählen Sie <i class="fas fa-plus"></i> **Team hinzufügen**.

![Fenster zum Hinzufügen eines neuen Teams.]({% image_buster /assets/img_archive/adding_a_team.png %})

Geben Sie den **Teamnamen** ein. Falls gewünscht, wählen Sie im Feld **Team definieren** ein angepasstes Attribut, einen Standort oder eine Sprache aus, um weiter zu definieren, auf welche Nutzerdaten das Team Zugriff hat. Ein möglicher Anwendungsfall ist z.B. das [Testen mit Teams](#test-with-teams), indem Sie ein Entwicklungsteam erstellen, das nur Zugriff auf Testnutzer:in hat, die durch ein angepasstes Attribut gekennzeichnet sind. Ein weiterer Anwendungsfall besteht darin, die Kommunikation mit Nutzern:innen auf der Grundlage des Produkts einzuschränken.

Wenn ein Team durch ein angepasstes Attribut, eine Sprache oder ein Land definiert ist, können Sie das Team verwenden, um Endnutzer nach Features wie Kampagnen, Canvase, Content-Cards, Segmenten und mehr zu filtern. Weitere Informationen finden Sie unter [Zuweisung von Team Tags](#tags-and-filters).

## Nutzer:innen Teams zuweisen

Braze-Manager:innen und eingeschränkte Nutzer:innen mit der Berechtigung „Unternehmenseinstellungen verwalten” auf Unternehmensebene können einem Unternehmensnutzer:in mit eingeschränktem Zugriff Berechtigungen auf Team-Ebene zuweisen. Wenn Nutzer:innen einem Team zugewiesen werden, können sie nur Daten lesen oder schreiben, die für ihr jeweiliges Team verfügbar sind, wie beispielsweise die Sprache des Nutzers, der Standort oder benutzerdefinierte Attribute, die bei der Erstellung des Teams festgelegt wurden.

Um einen Nutzer:innen einem Team zuzuordnen, navigieren Sie zu **Einstellungen** > **Unternehmensnutzer:innen** und wählen Sie einen Nutzer:innen aus, den Sie Ihrem Team hinzufügen möchten.

Führen Sie dann die folgenden Schritte aus:

1. Fügen Sie im Abschnitt **„Berechtigungen auf Workspace-Ebene**“ den Nutzer:in zum entsprechenden Workspace hinzu, falls er noch nicht enthalten ist.

![Berechtigungen auf Workspace-Ebene mit dem Berechtigungssatz „Banner-Template“.]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2\. Auswählen Sie **„+ Berechtigungen auf Teamebene hinzufügen**“ und anschließend das **Team** aus, dem Sie diesen Nutzer:in hinzufügen möchten.
3\. Weisen Sie im Abschnitt **„Team**-Berechtigungen“ spezifische Berechtigungen zu.

![Berechtigungen für Landingpage-Templates auf Team-Ebene.]({% image_buster /assets/img/teams.png %})

### Verfügbare Berechtigungen auf Team-Ebene

Im Folgenden finden Sie alle verfügbaren Berechtigungen, die Sie auf der Ebene Team vergeben können. Berechtigungen, die hier nicht aufgeführt sind, werden nur auf Workspace-Ebene gewährt und erscheinen als "--" in der Spalte **Team**-Berechtigungen.

{% tabs %}
{% tab Granular permissions %}

{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

- Kampagnen anzeigen
- Kampagnen bearbeiten
- Kampagnen archivieren
- Canvase anzeigen
- Canvase bearbeiten
- Canvase archivieren
- Frequency-Capping-Regeln anzeigen
- Frequency-Capping-Regeln bearbeiten
- Priorisierung von Nachrichten anzeigen
- Priorisierung von Nachrichten bearbeiten
- Content-Blöcke anzeigen
- Content-Blöcke bearbeiten
- Content-Blöcke archivieren
- Content-Blöcke starten
- Feature-Flags anzeigen
- Feature-Flags bearbeiten
- Feature-Flags archivieren
- Globale Kontrollgruppe anzeigen
- Segmente anzeigen
- Segmente bearbeiten
- IAM-Templates anzeigen
- IAM-Templates bearbeiten
- IAM-Templates archivieren
- E-Mail-Templates anzeigen
- E-Mail-Templates bearbeiten
- E-Mail Templates archivieren
- Webhook-Templates anzeigen
- Webhook-Templates bearbeiten
- Webhook-Templates archivieren
- Link-Templates anzeigen
- Link-Templates bearbeiten
- Mediathek Assets ansehen
- Assets der Medienbibliothek bearbeiten
- Assets der Medienbibliothek löschen
- Standorte anzeigen
- Standorte bearbeiten
- Standorte archivieren
- Aktionscodes anzeigen
- Aktionscodes bearbeiten
- Exportförderungsaktionscodes
- Präferenzzentren anzeigen
- Präferenzzentren bearbeiten
- Kampagnen starten
- Canvase starten
- Benutzerdaten exportieren
- Nutzerprofile PII-konform anzeigen
- Nutzer:innen des Dashboards anzeigen
- Dashboard-Nutzer:innen bearbeiten
- Kampagnen genehmigen
- Canvase genehmigen
- Canvas-Templates bearbeiten
- Canvas-Templates anzeigen
- Canvas-Templates archivieren
- Startseiten veröffentlichen
- Landing-Page-Templates bearbeiten
- Entwürfe für Landing-Pages bearbeiten
- Landing-Pages anzeigen
- Landing-Page-Templates archivieren
- Berichte anzeigen
- Erstellen Sie Berichte
- Berichte bearbeiten

{% endtab %}
{% tab Legacy permissions %}

- Greifen Sie auf Kampagnen, Leinwände, Karten, Inhaltsblöcke, Feature-Flags, Segmente, Mediathek und Präferenzzentren zu.
- Kampagnen versenden, Leinwände
- Content-Cards starten und verwalten
- Segmente bearbeiten
- Nutzerdaten exportieren
- Nutzerprofile PII-konform anzeigen
- Dashboard-Nutzer:innen verwalten
- Assets der Mediathek verwalten
- Kampagnen genehmigen und ablehnen
- Canvase genehmigen und ablehnen
- Canvas-Templates erstellen und bearbeiten
- Canvas-Templates anzeigen
- Canvas-Templates archivieren
- Landing-Page-Templates bearbeiten
- Landing-Page-Templates anzeigen
- Landing-Page-Templates archivieren

{% endtab %}
{% endtabs %}

Eine Beschreibung, was die einzelnen Benutzerrechte beinhalten und wie Sie sie verwenden können, finden Sie in unserem Abschnitt [Benutzerrechte]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Team-Tags zuweisen {#tags-and-filters}

Mit dem Filter **Team hinzufügen** können Sie Canvase, Kampagnen, Karten, Segmenten, E-Mail Templates und Medien Bibliothek Assets ein Team zuweisen.
 
![Hinzufügen eines Team-Tags zu einer Kampagne.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Basierend auf den bei der Erstellung des Teams angewendeten *Definitionen* wird die Zielgruppe dieses Engagement-Tools bei Zuweisung eines Team-Filters auf Nutzer:innen-Profile beschränkt, die der Definition entsprechen.
- Basierend auf den zugewiesenen *Berechtigungen* ist es Teammitgliedern nur zulässig, auf die Dashboard Engagement-Tools zuzugreifen, für die ihr Team-Filter gesetzt ist. Wenn sie nur über eingeschränkte oder gar keine Rechte für den Workspace verfügen, müssen sie bestimmten Objekten einen Team Filter hinzufügen, bevor sie diese speichern oder starten können. Teammitglieder können außerdem Canvase, Kampagnen, Karten und Segmente nach Teams filtern, um für sie relevante Inhalte zu identifizieren.

### Anwendungsfälle

Zwei Beispiele mit einem Braze-Marketer namens Michelle. Michelle ist Mitglied eines Teams namens "Entwicklung". Sie hat Zugriff auf alle Berechtigungen auf Teamebene für das Entwickler:in-Team.

{% tabs %}
{% tab Scenario 1 - Only Team permissions %}

In diesem Szenario ist Michelle eine eingeschränkte Nutzer:in, die keine Berechtigungen auf Workspace-Ebene besitzt. Ihre Berechtigungen sehen in etwa so aus:

![Angepasste Berechtigungen ohne Berechtigungen auf Workspace-Ebene und 16 teambezogene Berechtigungen.]({% image_buster /assets/img_archive/scenario1.png %})

Aufgrund der Michelle zugewiesenen Berechtigungen kann sie, wenn sie eine Kampagne erstellt, dieser Kampagne nur das Team "Entwicklung" zuweisen. Sie kann die Kampagne nur starten, wenn das Team zugewiesen ist, und sie kann keine anderen Tags des Teams sehen oder darauf zugreifen.

![Dropdown-Menü für Kampagnenteam-Tags, das ausschließlich das Team-Tag „Entwicklung“ anzeigt.]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Scenario 2 - Team permissions and workspace permissions %}

In diesem Szenario ist Michelle immer noch Mitglied des Entwicklungsteams, aber sie hat eine zusätzliche Berechtigung auf Workspace-Ebene.

![Benutzerdefinierte Berechtigungen mit einer Berechtigung auf Workspace-Ebene und 15 teambezogenen Berechtigungen.]({% image_buster /assets/img_archive/scenario2.png %})

Da Michelle auf Workspace-Ebene die Berechtigung "Zugriff auf Kampagnen, Canvase, Karten, Content-Blöcke, Feature-Flags, Segmente, Mediathek und Präferenzzentren" hat, kann sie andere Team-Filter für die von ihr erstellte Kampagne anzeigen und zuweisen.

![Dropdown-Menü „Kampagnenteam-Tag“ mit mehreren Team-Tags]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Ähnlich wie im ersten Szenario muss Michelle der Kampagne den Tag Entwicklungsteam hinzufügen, bevor sie sie einführen kann.

{% endtab %}
{% endtabs %}

## Test mit Teams

Ein möglicher Anwendungsfall für Teams ist die Schaffung eines Teams-basierten Genehmigungssystems für das Testen und Veröffentlichen von Inhalten in einer Produktionsumgebung.

Erstellen Sie dazu ein Team "Entwicklung", auf das nur Testnutzer:innen Zugriff haben. Sie können ein Team darauf beschränken, nur auf Testnutzer:innen zuzugreifen, wenn Ihre Testnutzer:innen durch ein angepasstes Attribut identifizierbar sind. Fügen Sie dann das angepasste Attribut als Definition hinzu, wenn Sie das Team erstellen oder bearbeiten (siehe den vorangehenden Abschnitt [Teams erstellen](#creating-Teams)). Ihre Genehmiger sollten Zugriff auf alle Benutzer haben.

Der allgemeine Prozess würde wie folgt ablaufen:

1. Das Entwickler:in Team erstellt eine Kampagne und fügt den Tag "Development" Team hinzu.
2. Das Entwickler Team startet die Kampagne, um Nutzer:innen zu testen.
3. Das Team der Genehmiger validiert das Design der lokalen Kampagne, bewirbt sie und startet sie. Zum Start ändert das Genehmigungsteam das Team-Tag von „Entwicklung“ in „[Alle Teams]“ und startet die Kampagne erneut.

Für Änderungen an aktiven Kampagnen:

1. Das Entwickler:in Team klont die laufende Kampagne, fügt den Tag "Entwicklung" Team hinzu und speichert.
2. Das Entwickler:in Team nimmt Bearbeitungen vor und gibt sie an das Team der Genehmigenden weiter.
3. Das Approver Team entfernt das Tag "Development" Team, pausiert die vorherige Kampagne und startet die neue Kampagne.

## Ein bestehendes Team archivieren

Sie können Teams über die Seite **Interne Teams** archivieren.

Wählen Sie ein oder mehrere Teams zum Archivieren aus. Wenn das Team mit keinem Objekt in Braze verknüpft ist, wird das Team sofort archiviert. Wenn das Team mit einem Objekt verknüpft ist, haben Sie die Möglichkeit, das Team nach dem Archivierungsprozess zu entfernen oder das Team zu ersetzen.

![Teams archivieren, die mit einem Braze-Objekt verbunden sind]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Braze-Administratoren können die Archivierung eines Teams aufheben, indem sie das archivierte Team auswählen und **Unarchive** wählen.