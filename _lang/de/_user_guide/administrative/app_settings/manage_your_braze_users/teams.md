---
nav_title: Teams
article_title: Teams
page_order: 4
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie Braze-Teams im Dashboard verwenden können. Hier erfahren Sie, wie Sie Teams erstellen, Rollen zuweisen und Tags und Filter zuordnen können."

---

# Teams

> Als Braze-Administrator können Sie Ihre Dashboard-Benutzer in Teams mit unterschiedlichen Benutzerrollen und Berechtigungen einteilen. So können Sie mehrere Gruppen von Dashboard-Benutzern, die nicht miteinander verbunden sind, in einem Arbeitsbereich zusammenarbeiten lassen, indem Sie die Arten von Inhalten, die bearbeitet werden können, voneinander trennen.

Teams können nach Kundenstandort, Sprache und benutzerdefinierten Attributen eingerichtet werden, so dass Teammitglieder und Nicht-Teammitglieder unterschiedlichen Zugriff auf Messaging-Funktionen und Kundendaten haben. Team-Filter und Tags können über verschiedene Engagement-Tools zugewiesen werden.

Teams sind nicht für alle Braze-Verträge verfügbar. Wenn Sie diese Funktion nutzen möchten, wenden Sie sich an Ihren Braze-Kundenbetreuer oder [kontaktieren Sie uns](mailto:success@braze.com) für ein Beratungsgespräch.

## Wie unterscheiden sich Teams von Berechtigungsgruppen und Rollen?

{% multi_lang_include permissions.md content="Unterschiede" %}

## Teams bilden

Gehen Sie zu **Einstellungen** > **Interne Teams** und wählen Sie <i class="fas fa-plus"></i> **Team hinzufügen**.

![Ein neues Team hinzufügen][68]

Geben Sie den **Teamnamen** ein. Falls gewünscht, verwenden Sie das Feld **Team definieren**, um ein benutzerdefiniertes Attribut, einen Standort oder eine Sprache auszuwählen, um weiter zu definieren, auf welche Benutzerdaten das Team Zugriff hat. Ein möglicher Anwendungsfall ist beispielsweise die Durchführung von [Tests mit Teams](#testing-with-teams), indem Sie ein Entwicklungsteam erstellen, das nur Zugriff auf Testbenutzer hat, die durch ein benutzerdefiniertes Attribut identifiziert werden. Ein weiterer Anwendungsfall ist die Einschränkung der Benutzerkommunikation nach Produkt.

Wenn ein Team durch ein benutzerdefiniertes Attribut, eine Sprache oder ein Land definiert ist, können Sie das Team verwenden, um Endbenutzer für Funktionen wie Kampagnen, Canvases, Content Cards, Segmente und mehr zu filtern. Mehr dazu finden Sie unter [Zuweisen von Team-Tags](#tags-and-filters).

## Benutzern Teams zuweisen

Braze-Administratoren und eingeschränkte Benutzer mit der Unternehmensberechtigung "Kann Unternehmenseinstellungen verwalten" können einem Dashboard-Benutzer mit eingeschränktem Zugriff Berechtigungen auf Teamebene zuweisen. Wenn Sie einem Team zugewiesen sind, können Dashboard-Benutzer nur die Daten lesen oder schreiben, die für ihr jeweiliges Team verfügbar sind, z. B. Benutzersprache, Standort oder benutzerdefinierte Attribute, die bei der Erstellung des Teams festgelegt wurden.

Um einen Benutzer einem Team zuzuweisen, navigieren Sie zu **Einstellungen** > **Unternehmensbenutzer** und wählen einen Benutzer aus, den Sie Ihrem Team hinzufügen möchten.

Führen Sie dann die folgenden Schritte aus:

1. Wählen Sie **Bearbeiten**.
2. Setzen Sie ihre Benutzerrolle auf **Eingeschränkt**.
3. Fügen Sie sie dem entsprechenden Arbeitsbereich hinzu. 
4. Wählen Sie das **Team** aus, dem Sie diesen Benutzer hinzufügen möchten, und weisen Sie ihm in der Spalte **Teamberechtigungen** bestimmte Berechtigungen zu.

![][2]

### Verfügbare Berechtigungen auf Teamebene

Hier alle verfügbaren Berechtigungen, die Sie auf Teamebene vergeben können. Berechtigungen, die hier nicht aufgeführt sind, werden nur auf Workspace-Ebene gewährt und erscheinen als "--" in der Spalte **Team**-Berechtigungen.

- Greifen Sie auf Kampagnen, Leinwände, Karten, Inhaltsblöcke, Feature-Flags, Segmente, Mediathek und Präferenzzentren zu.
- Kampagnen und Canvase senden
- Cards veröffentlichen
- Segmente bearbeiten
- Nutzerdaten exportieren
- Nutzerprofile PII-konform anzeigen
- Dashboard-Nutzer:innen verwalten
- Assets in Medienbibliothek verwalten

Eine Beschreibung, was die einzelnen Benutzerrechte beinhalten und wie Sie sie verwenden können, finden Sie in unserem Abschnitt [Benutzerrechte]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Team-Tags zuweisen {#tags-and-filters}

Mit dem Filter **Team hinzufügen** können Sie Canvases, Kampagnen, Karten, Segmenten, E-Mail-Vorlagen und Medienbibliothek-Assets ein Team zuweisen.
 
![Team-Tag zu einer Kampagne hinzufügen][3]{: style="max-width:70%;"}

- Basierend auf den *Definitionen*, die bei der Erstellung des Teams angewendet wurden, wird die Zielgruppe dieses Engagement-Tools auf Benutzerprofile beschränkt, die der Definition entsprechen, wenn ein Teamfilter zugewiesen wird.
- Basierend auf den zugewiesenen *Berechtigungen* können Teammitglieder nur auf die Dashboard-Tools zugreifen, für die ihr Teamfilter eingestellt ist. Wenn sie nur über eingeschränkte oder gar keine Rechte für den Arbeitsbereich verfügen, müssen sie bestimmten Objekten einen Teamfilter hinzufügen, bevor sie diese speichern oder starten können. Teammitglieder können Canvases, Kampagnen, Karten und Segmente auch nach Teams filtern, um für sie relevante Inhalte zu identifizieren.

### Anwendungsfälle

Zwei Beispiele mit einem Braze-Marketer namens Michelle. Michelle gehört zu dem Team "Entwicklung". Sie hat Zugriff auf alle Berechtigungen auf Teamebene für das Entwicklungsteam.

{% tabs %}
{% tab Szenario 1 - Nur Team-Berechtigungen %}

In diesem Szenario ist Michelle ein eingeschränkter Benutzer, der keine Berechtigungen auf Arbeitsbereichsebene hat. Ihre Berechtigungen sehen in etwa so aus:

![]({% image_buster /assets/img_archive/scenario1.png %})

Wenn Michelle eine Kampagne erstellt, kann sie aufgrund der ihr zugewiesenen Berechtigungen nur das Team "Entwicklung" dieser Kampagne zuweisen. Sie kann die Kampagne nur starten, wenn das Team zugewiesen ist, und sie kann keine anderen Team-Tags anzeigen oder darauf zugreifen.

![]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Szenario 2 - Team-Berechtigungen und Arbeitsbereich-Berechtigungen %}

In diesem Beispiel ist Michelle weiterhin Mitglied des Entwicklungsteams, hat aber auch eine zusätzliche Berechtigung auf Workspace-Ebene.

![]({% image_buster /assets/img_archive/scenario2.png %})

Da Michelle auf Arbeitsbereichsebene die Berechtigung "Zugriff auf Kampagnen, Leinwände, Karten, Inhaltsblöcke, Feature-Flags, Segmente, Mediathek und Präferenzzentren" hat, kann sie die von ihr erstellte Kampagne anzeigen und andere Teamfilter zuweisen.

![]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Ähnlich wie im ersten Szenario muss Michelle der Kampagne das Tag Entwicklungsteam hinzufügen, bevor sie sie starten kann.

{% endtab %}
{% endtabs %}

## Testen mit Teams

Ein möglicher Anwendungsfall für Teams ist die Schaffung eines teamabhängigen Genehmigungssystems für die Erprobung und Aufnahme von Inhalten in eine Produktionsumgebung.

Erstellen Sie dazu ein "Entwicklungsteam", das nur Zugriff auf Testbenutzer hat. Sie können ein Team so beschränken, dass es nur auf Testbenutzer zugreifen kann, wenn diese durch ein benutzerdefiniertes Attribut identifiziert werden können. Fügen Sie dann das benutzerdefinierte Attribut als Definition hinzu, wenn Sie das Team erstellen oder bearbeiten (siehe den vorangehenden Abschnitt [Teams erstellen](#creating-teams)). Ihre Genehmiger sollten Zugriff auf alle Benutzer haben.

Der allgemeine Prozess würde wie folgt ablaufen:

1. Das Entwicklungsteam erstellt eine Kampagne und fügt das Team-Tag "Entwicklung" hinzu.
2. Das Entwicklungsteam startet die Kampagne für Testbenutzer.
3. Das Genehmigungsteam überprüft das Design der lokalen Kampagne, bewirbt sie und startet sie. Um die Kampagne zu starten, ändert das Genehmigungsteam das Team-Tag von "Entwicklung" in "[Alle Teams]" und startet die Kampagne neu.

Für Änderungen an aktiven Kampagnen:

1. Das Entwicklungsteam klont die laufende Kampagne, fügt das Team-Tag "Entwicklung" hinzu und speichert sie.
2. Das Entwicklungsteam nimmt Bearbeitungen vor und gibt sie an das Team der Genehmiger weiter.
3. Das Genehmigungsteam entfernt das Team-Tag "Entwicklung", pausiert die vorherige Kampagne und startet die neue Kampagne.

## Ein bestehendes Team archivieren

Sie können Teams auf der Seite **Interne Teams** archivieren.

Wählen Sie ein oder mehrere Teams zum Archivieren aus. Wenn das Team mit keinem Braze-Objekt verknüpft ist, wird es sofort archiviert. Wenn das Team mit einem Objekt verknüpft ist, können Sie es nach der Archivierung entfernen oder ersetzen.

![Teams archivieren, die mit einem Braze-Objekt verbunden sind][86]{: style="max-width:70%;"}

Braze-Administratoren können die Archivierung eines Teams aufheben, indem sie das archivierte Team auswählen und die Option **Archivierung aufheben** wählen.

[2]: {% image_buster /assets/img/teams.png %}
[3]: {% image_buster /assets/img/teams1.png %}
[68]: {% image_buster /assets/img_archive/adding_a_team.png %}
[86]: {% image_buster /assets/img_archive/archive_a_team.png %}
