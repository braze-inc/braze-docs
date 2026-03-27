---
nav_title: Teams
article_title: Teams
page_order: 4
page_type: reference
alias: /teams/
description: "Dieser Referenzartikel beschreibt, wie Sie Braze Teams im Dashboard verwenden können. Hier erfahren Sie, wie Sie Teams erstellen, Rollen zuweisen und Tags und Filter zuordnen können."

---

# Teams

> Als Braze-Administrator:in können Sie die Nutzer:innen Ihres Unternehmens in Teams mit unterschiedlichen Rollen und Berechtigungen gruppieren. Dies ermöglicht es Ihnen, mehrere, voneinander unabhängige Gruppen von Unternehmensnutzer:innen in einem Workspace zusammenarbeiten zu lassen, indem die Arten von Inhalten, die bearbeitet werden können, voneinander getrennt werden.

Teams können nach Standort der Kundenbasis, Sprache und angepassten Attributen eingerichtet werden, sodass Teammitglieder und Nicht-Teammitglieder unterschiedlichen Zugriff auf Messaging-Features und Kundendaten haben. Team-Filter und Tags können über verschiedene Engagement-Tools zugewiesen werden. Es gibt keine Begrenzung hinsichtlich der Anzahl der Teams, die Sie in Ihrem Workspace erstellen können.

Teams sind nicht in allen Braze-Verträgen enthalten. Um auf dieses Feature zuzugreifen, wenden Sie sich bitte an Ihren Braze Account Manager oder [kontaktieren Sie uns](mailto:success@braze.com) für eine Beratung.

## Wie unterscheiden sich Teams von Berechtigungsgruppen und Rollen?

{% multi_lang_include permissions.md content="Differences" %}

## Teams erstellen {#creating-teams}

Gehen Sie zu **Einstellungen** > **Interne Teams** und wählen Sie <i class="fas fa-plus"></i> **Team hinzufügen**.

![Fenster zum Hinzufügen eines neuen Teams.]({% image_buster /assets/img_archive/adding_a_team.png %})

Geben Sie den **Teamnamen** ein. Falls gewünscht, wählen Sie im Feld **Team definieren (Optional)** ein angepasstes Attribut, einen Standort oder eine Sprache aus, um genauer zu definieren, auf welche Nutzerdaten das Team Zugriff hat. Ein möglicher Anwendungsfall ist z. B. das [Testen mit Teams](#test-with-teams), indem Sie ein Entwicklungsteam erstellen, das nur Zugriff auf Testnutzer:innen hat, die durch ein angepasstes Attribut gekennzeichnet sind. Ein weiterer Anwendungsfall besteht darin, die Kommunikation mit Nutzer:innen auf der Grundlage des Produkts einzuschränken.

Wenn ein Team durch ein angepasstes Attribut, eine Sprache oder ein Land definiert ist, können Sie das Team verwenden, um Endnutzer:innen nach Features wie Kampagnen, Canvase, Content-Cards, Segmenten und mehr zu filtern. Weitere Informationen finden Sie unter [Team-Tags zuweisen](#tags-and-filters).

## Nutzer:innen Teams zuweisen

Braze-Administrator:innen und eingeschränkte Nutzer:innen mit der Berechtigung „Unternehmenseinstellungen verwalten" auf Unternehmensebene können einem/einer Unternehmensnutzer:in mit eingeschränktem Zugriff Berechtigungen auf Team-Ebene zuweisen. Wenn Nutzer:innen einem Team zugewiesen werden, können sie nur Daten lesen oder schreiben, die für ihr jeweiliges Team verfügbar sind, wie beispielsweise die Sprache, der Standort oder angepasste Attribute, die bei der Erstellung des Teams festgelegt wurden.

Um eine:n Nutzer:in einem Team zuzuordnen, navigieren Sie zu **Einstellungen** > **Unternehmensnutzer:innen** und wählen Sie eine:n Nutzer:in aus, den/die Sie Ihrem Team hinzufügen möchten.

Führen Sie dann die folgenden Schritte aus:

1. Fügen Sie im Abschnitt **Berechtigungen auf Workspace-Ebene** den/die Nutzer:in zum entsprechenden Workspace hinzu, falls er/sie noch nicht enthalten ist.

![Berechtigungen auf Workspace-Ebene mit dem Berechtigungssatz „Banner-Template".]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2. Wählen Sie **+ Berechtigungen auf Teamebene hinzufügen** und anschließend das **Team** aus, dem Sie diese:n Nutzer:in hinzufügen möchten.
3. Weisen Sie im Abschnitt **Team**-Berechtigungen spezifische Berechtigungen zu.

![Berechtigungen für Landing-Page-Templates auf Team-Ebene.]({% image_buster /assets/img/teams.png %})

### Verfügbare Berechtigungen auf Team-Ebene

Im Folgenden finden Sie alle verfügbaren Berechtigungen, die Sie auf Team-Ebene vergeben können. Berechtigungen, die hier nicht aufgeführt sind, werden nur auf Workspace-Ebene gewährt und erscheinen als „--" in der Spalte **Team**-Berechtigungen.

{% tabs %}
{% tab Granular permissions %}

{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

- Kampagnen anzeigen
- Kampagnen bearbeiten
- Kampagnen archivieren
- Canvase anzeigen
- Canvase bearbeiten
- Canvase archivieren
- Content-Blöcke anzeigen
- Content-Blöcke bearbeiten
- Content-Blöcke archivieren
- Content-Blöcke starten
- Feature-Flags anzeigen
- Feature-Flags bearbeiten
- Feature-Flags archivieren
- Segmente anzeigen
- Segmente bearbeiten
- E-Mail-Templates anzeigen
- E-Mail-Templates bearbeiten
- E-Mail-Templates archivieren
- Webhook-Templates anzeigen
- Webhook-Templates bearbeiten
- Webhook-Templates archivieren
- E-Mail-Link-Templates anzeigen
- E-Mail-Link-Templates bearbeiten
- Mediathek-Assets anzeigen
- Mediathek-Assets bearbeiten
- Mediathek-Assets löschen
- Kampagnen starten
- Canvase starten
- Nutzerdaten exportieren
- Nutzerprofile anzeigen (PII geschwärzt)
- Dashboard-Nutzer:innen bearbeiten
- Kampagnen genehmigen
- Canvase genehmigen
- Canvas-Templates bearbeiten
- Canvas-Templates anzeigen
- Canvas-Templates archivieren
- Dashboard-Berichte anzeigen
- Dashboard-Berichte bearbeiten
- Dashboard-Berichte löschen
- PII anzeigen

{% endtab %}
{% tab Legacy permissions %}

- Zugriff auf Kampagnen, Canvase, Karten, Content-Blöcke, Feature-Flags, Segmente, Mediathek und Präferenzzentren
- Kampagnen und Canvase versenden
- Content-Cards starten und verwalten
- Segmente bearbeiten
- Nutzerdaten exportieren
- Nutzerprofile PII-konform anzeigen
- Dashboard-Nutzer:innen verwalten
- Mediathek-Assets verwalten
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

Eine Beschreibung, was die einzelnen Berechtigungen beinhalten und wie Sie sie verwenden können, finden Sie in unserem Abschnitt [Berechtigungen]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Team-Tags zuweisen {#tags-and-filters}

Mit dem Filter **Team hinzufügen** können Sie Canvasen, Kampagnen, Content-Cards, Segmenten, E-Mail-Templates, Webhook-Templates, Content-Blöcken und Mediathek-Assets ein Team zuweisen.
 
![Hinzufügen eines Team-Tags zu einer Kampagne.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Basierend auf den bei der Erstellung des Teams angewendeten *Definitionen* wird die Zielgruppe dieses Engagement-Tools bei Zuweisung eines Team-Filters auf Nutzerprofile beschränkt, die der Definition entsprechen.
- Basierend auf den zugewiesenen *Berechtigungen* ist es Teammitgliedern nur erlaubt, auf die Dashboard-Engagement-Tools zuzugreifen, für die ihr Team-Filter gesetzt ist. Wenn sie nur über eingeschränkte oder gar keine Berechtigungen auf Workspace-Ebene verfügen, müssen sie bestimmten Objekten einen Team-Filter hinzufügen, bevor sie diese speichern oder starten können. Teammitglieder können außerdem Canvase, Kampagnen, Content-Cards und Segmente nach Teams filtern, um für sie relevante Inhalte zu identifizieren.

### Anwendungsfälle

Betrachten Sie die folgenden zwei Szenarien für eine Marketerin bei Braze namens Michelle. Michelle ist Mitglied eines Teams namens „Entwicklung". Sie hat Zugriff auf alle Berechtigungen auf Teamebene für das Entwicklungsteam.

{% tabs %}
{% tab Scenario 1 - Only Team permissions %}

In diesem Szenario ist Michelle eine eingeschränkte Nutzerin, die keine Berechtigungen auf Workspace-Ebene besitzt. Ihre Berechtigungen sehen in etwa so aus:

![Angepasste Berechtigungen ohne Berechtigungen auf Workspace-Ebene und 16 teambezogene Berechtigungen.]({% image_buster /assets/img_archive/scenario1.png %})

Aufgrund der Michelle zugewiesenen Berechtigungen kann sie beim Erstellen einer Kampagne dieser nur das Team „Entwicklung" zuweisen. Sie kann die Kampagne nur starten, wenn das Team zugewiesen ist, und sie kann keine anderen Team-Tags sehen oder darauf zugreifen.

![Dropdown-Menü für Kampagnen-Team-Tags, das ausschließlich das Team-Tag „Entwicklung" anzeigt.]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Scenario 2 - Team permissions and workspace permissions %}

In diesem Szenario ist Michelle immer noch Mitglied des Entwicklungsteams, verfügt aber zusätzlich über eine Berechtigung auf Workspace-Ebene.

![Angepasste Berechtigungen mit einer Berechtigung auf Workspace-Ebene und 15 teambezogenen Berechtigungen.]({% image_buster /assets/img_archive/scenario2.png %})

Da Michelle auf Workspace-Ebene die Berechtigung „Zugriff auf Kampagnen, Canvase, Karten, Content-Blöcke, Feature-Flags, Segmente, Mediathek und Präferenzzentren" hat, kann sie andere Team-Filter für die von ihr erstellte Kampagne anzeigen und zuweisen.

![Dropdown-Menü für Kampagnen-Team-Tags mit mehreren Team-Tags]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Ähnlich wie im ersten Szenario muss Michelle der Kampagne den Tag des Entwicklungsteams hinzufügen, bevor sie sie starten kann.

{% endtab %}
{% endtabs %}

## Testen mit Teams

Ein möglicher Anwendungsfall für Teams ist die Einrichtung eines teambasierten Genehmigungssystems für das Testen und Veröffentlichen von Inhalten in einer Produktionsumgebung.

Erstellen Sie dazu ein Team „Entwicklung", das nur Zugriff auf Testnutzer:innen hat. Sie können ein Team darauf beschränken, nur auf Testnutzer:innen zuzugreifen, wenn Ihre Testnutzer:innen durch ein angepasstes Attribut identifizierbar sind. Fügen Sie dann das angepasste Attribut als Definition hinzu, wenn Sie das Team erstellen oder bearbeiten (siehe den vorangehenden Abschnitt [Teams erstellen](#creating-Teams)). Ihre Genehmiger:innen sollten Zugriff auf alle Nutzer:innen haben.

Der allgemeine Prozess würde wie folgt ablaufen:

1. Das Entwicklungsteam erstellt eine Kampagne und fügt den Tag „Entwicklung" hinzu.
2. Das Entwicklungsteam startet die Kampagne für Testnutzer:innen.
3. Das Genehmigungsteam validiert das lokale Kampagnendesign, bewirbt es und startet es. Zum Starten ändert das Genehmigungsteam das Team-Tag von „Entwicklung" in „[Alle Teams]" und startet die Kampagne erneut.

Für Änderungen an aktiven Kampagnen:

1. Das Entwicklungsteam klont die laufende Kampagne, fügt den Tag „Entwicklung" hinzu und speichert.
2. Das Entwicklungsteam nimmt Bearbeitungen vor und gibt sie an das Genehmigungsteam weiter.
3. Das Genehmigungsteam entfernt den Tag „Entwicklung", pausiert die vorherige Kampagne und startet die neue Kampagne.

## Ein bestehendes Team archivieren

Sie können Teams über die Seite **Interne Teams** archivieren.

Wählen Sie ein oder mehrere Teams zum Archivieren aus. Wenn das Team mit keinem Objekt in Braze verknüpft ist, wird es sofort archiviert. Wenn das Team mit einem Objekt verknüpft ist, haben Sie die Möglichkeit, das Team nach dem Archivierungsprozess zu entfernen oder zu ersetzen.

![Archivieren eines Teams, das mit einem Objekt in Braze verknüpft ist]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Braze-Administrator:innen können die Archivierung eines Teams aufheben, indem sie das archivierte Team auswählen und **Archivierung aufheben** wählen.