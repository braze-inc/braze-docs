---
nav_title: Teams
article_title: Teams
page_order: 4
page_type: reference
description: "Dieser referenzierte Artikel beschreibt, wie Sie Braze Teams im Dashboard verwenden können. Hier erfahren Sie, wie Sie Teams erstellen, Rollen zuweisen und Tags und Filter zuordnen können."

---

# Teams

> Als Braze-Administrator können Sie Ihre Nutzer:innen des Dashboards in Teams mit unterschiedlichen Nutzer:innenrollen und Berechtigungen gruppieren. So können Sie mehrere Gruppen von Dashboard-Benutzern, die nicht miteinander verbunden sind, in einem Arbeitsbereich zusammenarbeiten lassen, indem Sie die Arten von Inhalten, die bearbeitet werden können, voneinander trennen.

Teams können nach Standort, Sprache und angepassten Attributen eingerichtet werden, so dass Teammitglieder und Nicht-Teammitglieder unterschiedlichen Zugriff auf Messaging Features und Kundendaten haben. Team-Filter und Tags können über verschiedene Engagement-Tools zugewiesen werden.

Teams sind nicht für alle Braze-Verträge verfügbar. Wenn Sie diese Funktion nutzen möchten, wenden Sie sich an Ihren Braze-Kundenbetreuer oder [kontaktieren Sie uns](mailto:success@braze.com) für ein Beratungsgespräch.

## Wie unterscheiden sich Teams von Berechtigungsgruppen und Rollen?

{% multi_lang_include permissions.md content="Differences" %}

## Teams erstellen

Gehen Sie zu **Einstellungen** > **Interne Teams** und wählen Sie <i class="fas fa-plus"></i> **Team hinzufügen**.

![Fenster zum Hinzufügen eines neuen Teams.]({% image_buster /assets/img_archive/adding_a_team.png %}){: style="max-width:70%;"}

Geben Sie den **Teamnamen** ein. Falls gewünscht, wählen Sie im Feld **Team definieren** ein angepasstes Attribut, einen Standort oder eine Sprache aus, um weiter zu definieren, auf welche Nutzerdaten das Team Zugriff hat. Ein möglicher Anwendungsfall ist z.B. das [Testen mit Teams](#testing-with-Teams), indem Sie ein Entwicklungsteam erstellen, das nur Zugriff auf Testnutzer:in hat, die durch ein angepasstes Attribut gekennzeichnet sind. Ein weiterer Anwendungsfall ist die Einschränkung der Benutzerkommunikation nach Produkt.

Wenn ein Team durch ein angepasstes Attribut, eine Sprache oder ein Land definiert ist, können Sie das Team verwenden, um Endnutzer nach Features wie Kampagnen, Canvase, Content-Cards, Segmenten und mehr zu filtern. Weitere Informationen finden Sie unter [Zuweisung von Team Tags](#tags-and-filters).

## Zuweisung von Nutzer:innen zu Teams

Braze-Administratoren und eingeschränkte Nutzer:innen mit der Berechtigung "Kann Firmeneinstellungen verwalten" können einem Dashboard-Benutzer mit eingeschränktem Zugriff Berechtigungen auf Teamebene zuweisen. Wenn Sie einem Team zugewiesen sind, können Nutzer:innen des Dashboards nur die Daten lesen oder schreiben, die für ihr jeweiliges Team verfügbar sind, z.B. Benutzersprache, Standort oder angepasste Attribute, wie sie bei der Erstellung des Teams definiert wurden.

Um einen Nutzer:innen einem Team zuzuordnen, navigieren Sie zu **Einstellungen** > **Unternehmensnutzer:innen** und wählen Sie einen Nutzer:innen aus, den Sie Ihrem Team hinzufügen möchten.

Führen Sie dann die folgenden Schritte aus:

1. Fügen Sie im Abschnitt **Berechtigungen auf Workspace-Ebene** den Nutzer:innen dem entsprechenden Workspace hinzu, wenn er nicht bereits enthalten ist.

![Ein Berechtigungssatz für den Workspace "Swifty & Droidboy".]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2\. Wählen Sie **\+ Berechtigungen auf Teamebene hinzufügen** und wählen Sie dann das **Team** aus, dem Sie diesen Nutzer:innen hinzufügen möchten.
3\. Weisen Sie bestimmte Berechtigungen aus der Spalte **Team-Berechtigungen** zu.

![Ein Bereich zum Auswählen von Berechtigungen für das Team "Kundensupport".]({% image_buster /assets/img/teams.png %})

### Verfügbare Berechtigungen auf Team-Ebene

Im Folgenden finden Sie alle verfügbaren Berechtigungen, die Sie auf der Ebene Team vergeben können. Berechtigungen, die hier nicht aufgeführt sind, werden nur auf Workspace-Ebene gewährt und erscheinen als "--" in der Spalte **Team**-Berechtigungen.

- Greifen Sie auf Kampagnen, Leinwände, Karten, Inhaltsblöcke, Feature-Flags, Segmente, Mediathek und Präferenzzentren zu.
- Kampagnen versenden, Leinwände
- Starten und Verwalten von Content-Cards
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
- Landing-Page-Templates erstellen und bearbeiten
- Landing-Page-Templates anzeigen
- Landing-Page-Templates archivieren

Eine Beschreibung, was die einzelnen Benutzerrechte beinhalten und wie Sie sie verwenden können, finden Sie in unserem Abschnitt [Benutzerrechte]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Team Tags zuweisen {#tags-and-filters}

Mit dem Filter **Team hinzufügen** können Sie Canvase, Kampagnen, Karten, Segmenten, E-Mail Templates und Medien Bibliothek Assets ein Team zuweisen.
 
![Hinzufügen eines Team Tags zu einer Kampagne.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Basierend auf den bei der Erstellung des Teams angewendeten *Definitionen* wird die Zielgruppe dieses Engagement-Tools bei Zuweisung eines Team-Filters auf Nutzer:innen-Profile beschränkt, die der Definition entsprechen.
- Basierend auf den zugewiesenen *Berechtigungen* ist es Teammitgliedern nur zulässig, auf die Dashboard Engagement-Tools zuzugreifen, für die ihr Team-Filter gesetzt ist. Wenn sie nur über eingeschränkte oder gar keine Rechte für den Workspace verfügen, müssen sie bestimmten Objekten einen Team Filter hinzufügen, bevor sie diese speichern oder starten können. Teammitglieder können außerdem Canvase, Kampagnen, Karten und Segmente nach Teams filtern, um für sie relevante Inhalte zu identifizieren.

### Anwendungsfälle

Zwei Beispiele mit einem Braze-Marketer namens Michelle. Michelle ist Mitglied eines Teams namens "Entwicklung". Sie hat Zugriff auf alle Berechtigungen auf Teamebene für das Entwickler:in-Team.

{% tabs %}
{% tab Scenario 1 - Only Team permissions %}

In diesem Szenario ist Michelle ein eingeschränkter Nutzer:in, der keine Berechtigungen auf Workspace-Ebene hat. Ihre Berechtigungen sehen in etwa so aus:

![Angepasste Berechtigungen ohne Berechtigungen auf Workspace-Ebene und 16 teambasierte Berechtigungen.]({% image_buster /assets/img_archive/scenario1.png %})

Aufgrund der Michelle zugewiesenen Berechtigungen kann sie, wenn sie eine Kampagne erstellt, dieser Kampagne nur das Team "Entwicklung" zuweisen. Sie kann die Kampagne nur starten, wenn das Team zugewiesen ist, und sie kann keine anderen Tags des Teams sehen oder darauf zugreifen.

![Dropdown-Menü für Kampagnenteams, das nur das Tag "Entwicklungsteam" anzeigt.]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Scenario 2 - Team permissions and workspace permissions %}

In diesem Szenario ist Michelle immer noch Mitglied des Entwicklungsteams, aber sie hat eine zusätzliche Berechtigung auf Workspace-Ebene.

![Angepasste Berechtigungen mit einer Berechtigung auf Workspace-Ebene und 15 teambasierten Berechtigungen.]({% image_buster /assets/img_archive/scenario2.png %})

Da Michelle auf Workspace-Ebene die Berechtigung "Zugriff auf Kampagnen, Canvase, Karten, Content-Blöcke, Feature-Flags, Segmente, Mediathek und Präferenzzentren" hat, kann sie andere Team-Filter für die von ihr erstellte Kampagne anzeigen und zuweisen.

![Kampagnen Team Tag Dropdown mit mehreren Team Tags]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Ähnlich wie im ersten Szenario muss Michelle der Kampagne den Tag Entwicklungsteam hinzufügen, bevor sie sie einführen kann.

{% endtab %}
{% endtabs %}

## Testen mit Teams

Ein möglicher Anwendungsfall für Teams ist die Schaffung eines Teams-basierten Genehmigungssystems für das Testen und Veröffentlichen von Inhalten in einer Produktionsumgebung.

Erstellen Sie dazu ein Team "Entwicklung", auf das nur Testnutzer:innen Zugriff haben. Sie können ein Team darauf beschränken, nur auf Testnutzer:innen zuzugreifen, wenn Ihre Testnutzer:innen durch ein angepasstes Attribut identifizierbar sind. Fügen Sie dann das angepasste Attribut als Definition hinzu, wenn Sie das Team erstellen oder bearbeiten (siehe den vorangehenden Abschnitt [Teams erstellen](#creating-Teams)). Ihre Genehmiger sollten Zugriff auf alle Benutzer haben.

Der allgemeine Prozess würde wie folgt ablaufen:

1. Das Entwickler:in Team erstellt eine Kampagne und fügt den Tag "Development" Team hinzu.
2. Das Entwickler Team startet die Kampagne, um Nutzer:innen zu testen.
3. Das Team der Genehmiger validiert das Design der lokalen Kampagne, bewirbt sie und startet sie. Um die Kampagne einzuführen, ändert das Approver Team den Tag des Teams von "Entwicklung" in "[Alle Teams]" und startet die Kampagne neu.

Für Änderungen an aktiven Kampagnen:

1. Das Entwickler:in Team klont die laufende Kampagne, fügt den Tag "Entwicklung" Team hinzu und speichert.
2. Das Entwickler:in Team nimmt Bearbeitungen vor und gibt sie an das Team der Genehmigenden weiter.
3. Das Approver Team entfernt das Tag "Development" Team, pausiert die vorherige Kampagne und startet die neue Kampagne.

## Ein bestehendes Team archivieren

Sie können Teams über die Seite **Interne Teams** archivieren.

Wählen Sie ein oder mehrere Teams zum Archivieren aus. Wenn das Team mit keinem Objekt in Braze verknüpft ist, wird das Team sofort archiviert. Wenn das Team mit einem Objekt verknüpft ist, haben Sie die Möglichkeit, das Team nach dem Archivierungsprozess zu entfernen oder das Team zu ersetzen.

![Archivierung eines Teams, das mit einem Objekt in Braze verbunden ist]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Braze-Administratoren können die Archivierung eines Teams aufheben, indem sie das archivierte Team auswählen und **Unarchive** wählen.

