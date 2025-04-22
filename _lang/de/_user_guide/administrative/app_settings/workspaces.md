---
nav_title: Arbeitsbereiche erstellen und verwalten
article_title: Arbeitsbereiche erstellen und verwalten
page_order: 0
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie Ihre Arbeitsbereiche erstellen, einrichten und verwalten."

---

# Arbeitsbereiche erstellen und verwalten

> Dieser Artikel beschreibt, wie Sie Ihre Arbeitsbereiche erstellen, einrichten und verwalten. 

## Was ist ein Arbeitsbereich?

Alles, was Sie in Braze tun, geschieht innerhalb eines Workspace. Workspaces sind gemeinsam genutzte Umgebungen, in der Sie das Engagement für verwandte mobile Apps oder Websites verfolgen und verwalten können. Arbeitsbereiche fassen gleiche oder sehr ähnliche Apps zusammen: zum Beispiel die Android- und iOS-Versionen Ihrer mobilen App. 

## Einen Workspace erstellen

### Schritt 1: Haben Sie einen Plan

Bevor Sie beginnen, stellen Sie sicher, dass Sie mit Ihrem Team und Ihrem Braze Onboarding Manager zusammenarbeiten, um die beste Workspace-Konfiguration für Ihren Anwendungsfall zu bestimmen. Wenn Sie mehr über die Planung Ihrer Workspaces in Braze erfahren möchten, lesen Sie unseren Artikel [Erste Schritte]: Workspaces][link] Leitfaden.

### Schritt 2: Ihren Arbeitsbereich hinzufügen

Sie können über das Dropdown-Menü Arbeitsbereich in der globalen Kopfzeile neue Arbeitsbereiche erstellen oder zwischen bestehenden Arbeitsbereichen wechseln.

1. Wählen Sie das Dropdown-Menü Workspace und dann <i class="fa-solid fa-square-plus" style="color: #0b8294;"></i> **Workspace erstellen**.

![Das Workspace-Dropdown mit dem Button "Workspace erstellen".][1]{: style="max-width:60%;"}

{:start="2"}
2\. Geben Sie Ihrem Arbeitsbereich einen Namen.

{% alert tip %}
Vielleicht möchten Sie eine Namenskonvention festlegen, damit andere in Ihrem Unternehmen Ihren Arbeitsbereich leicht finden können. Zum Beispiel: "Upon Voyage US - Produktion" und "Upon Voyage US - Inszenierung".
{% endalert %}

{:start="3"}
3\. Wählen Sie **Erstellen**. Es kann ein paar Sekunden dauern, bis Braze Ihren Arbeitsbereich erstellt hat.

![Modal "Workspace erstellen" mit dem Namen "Upon Voyage US - Staging".][2]{: style="max-width:60%" }

Sie werden zur Seite **App-Einstellungen** weitergeleitet, auf der Sie Ihre App-Instanzen hinzufügen können. Sie können diese Seite jederzeit über **Einstellungen** > **App-Einstellungen** aufrufen.

![Seite "App-Einstellungen" für den Upon Voyage US - Staging Workspace mit einem Button zum Hinzufügen einer App.][3]

### Schritt 3: Fügen Sie Ihre App-Instanzen hinzu

Wir bezeichnen die verschiedenen Websites und Apps, die innerhalb eines Workspace gesammelt werden, als "App-Instanzen".

1. Wählen Sie auf der Seite mit **den App-Einstellungen** **\+ App hinzufügen**.
2. Geben Sie Ihrer App-Instanz einen Namen und wählen Sie aus, auf welcher Plattform oder welchen Plattformen diese App-Instanz läuft. Wenn Sie mehrere Plattformen auswählen, wird Braze eine App-Instanz für jede Plattform erstellen.

![Modal "Neue App zu Upon Voyage US - Staging hinzufügen" mit Optionen zum Auswählen der App-Details.][4]{: style="max-width:60%" }

{:start="3"}
3\. Wählen Sie zur Bestätigung **App hinzufügen**.

#### App API-Schlüssel

Nachdem Sie Ihre App-Instanz hinzugefügt haben, haben Sie Zugang zu ihrem API-Schlüssel. Der API-Schlüssel wird verwendet, wenn Sie Anfragen zwischen Ihrer App-Instanz und der Braze API stellen. Der API-Schlüssel ist auch wichtig für die Integration des Braze SDK mit Ihrer App oder Website.

![Einstellungsseite für die Upon Voyage iOS App mit Feldern für den API-Schlüssel und den SDK-Endpunkt.][5]

{% alert note %}
Sie müssen für jede Version Ihrer App auf jeder Plattform separate App-Instanzen erstellen. Wenn Sie zum Beispiel eine kostenlose und eine Pro-Version Ihrer App für iOS und Android haben, erstellen Sie vier App-Instanzen in Ihrem Arbeitsbereich (kostenlose iOS-App, kostenlose Android-App, Pro-iOS-App und Pro-Android-App). So erhalten Sie vier API-Schlüssel, die Sie verwenden können, einen für jede App-Instanz.
{% endalert %}

#### Live SDK Version

Die Live-SDK-Version, die auf der Seite App-Einstellungen für eine bestimmte App angezeigt wird, ist die höchste App-Version mit mindestens 5 % Ihrer täglichen Gesamtsitzungen und mindestens 500 Sitzungen am vergangenen Tag.

Dieses Feld erscheint, nachdem Sie das Braze SDK in Ihre App oder Website integriert haben. Wenn eine neuere Version des Braze SDK für Ihre Plattform verfügbar ist, wird dies hier mit dem Tag "Neuere Version verfügbar" vermerkt.

![Abschnitt "Live SDK Version" mit dem Feldwert "5.4.0" und einem Symbol, das besagt, dass eine neue Version verfügbar ist.][6]

### Schritt 4: Wiederholen Sie den Vorgang nach Bedarf

Wiederholen Sie die Schritte 2 und 3, um so viele Workspaces einzurichten, wie Ihr Plan erfordert. Wir empfehlen Ihnen, einen Test-Workspace für Integrationstests und Kampagnentests zu erstellen.

{% alert tip %}
**Einen Workspace zum Testen hinzufügen**<br>Sie können App-Tests durchführen, indem Sie bestimmte Nutzer:innen komplett von Ihrer Produktionsinstanz fernhalten. Erstellen Sie einen neuen Workspace, und wenn Sie Ihre Anwendung veröffentlichen, stellen Sie sicher, dass der API-Schlüssel, den Braze verwendet, mit dem Ihres Produktions-Workspace übereinstimmt und nicht mit dem Ihres Test-Workspace.
{% endalert %}

## Arbeitsbereiche verwalten

### Hinzufügen von Favoriten

Sie können bevorzugte Workspaces hinzufügen, um noch schneller auf die Workspaces zuzugreifen, die Sie am häufigsten verwenden.

![Workspace-Dropdown mit dem Tab für "Favorisierte Workspaces".][7]{: style="max-width:50%;"}

So fügen Sie bevorzugte Arbeitsbereiche hinzu:

1. Wählen Sie das Dropdown-Menü Ihres Profils und dann die Option **Ihr Konto verwalten**.
2. Suchen Sie im Bereich **Kontoprofil** das Feld **Bevorzugte Arbeitsbereiche**.
3. Wählen Sie Ihre Arbeitsbereiche aus der Liste aus.
4. Wählen Sie **Änderungen speichern**.

Die Anzahl der Workspaces, die Sie favorisieren können, ist unbegrenzt, aber wir empfehlen Ihnen, diese Liste der Einfachheit halber kurz zu halten.

### Workspaces umbenennen

So benennen Sie Ihren Arbeitsbereich um:

1. Gehen Sie zu **Einstellungen** > **App-Einstellungen**.
2. Bewegen Sie den Mauszeiger über den Namen Ihres Arbeitsbereichs und wählen Sie <i class="image: /assets/img/braze_icons/pencil-01.svg" style="color: #0b8294;"></i>.
3. Geben Sie Ihrem Arbeitsbereich einen neuen Namen und wählen Sie dann <i class="fa-solid fa-square-check" style="color: #0b8294;"></i> **Speichern**.

![Das Bleistiftsymbol neben dem Namen des Workspaces.][8]{: style="max-width:50%;"}

### Löschen von Workspaces und App-Instanzen

So löschen Sie Ihren Workspace oder Ihre App-Instanz:

1. Gehen Sie zu **Einstellungen** > **App-Einstellungen**.
2. Wählen Sie **Workspace löschen**, um den jeweiligen Workspace zu löschen, oder wählen Sie das Mülleimer-Symbol neben der jeweiligen App-Instanz.

Sie können keine App-Instanzen oder Workspaces löschen, die derzeit für das Targeting von Nutzern:innen verwendet werden oder die mehr als 1.000 Nutzer:innen haben. Wenn Sie dies versuchen, erhalten Sie eine Fehlermeldung. Um fortzufahren und sie zu löschen, [erstellen Sie einen Support-Fall]({{site.baseurl}}/user_guide/administrative/access_braze/support/), der einen Dashboard-Link und den Namen der zu löschenden App-Instanz oder des Workspace enthält.

{% alert warning %}
Seien Sie vorsichtig beim Löschen von Arbeitsbereichen! Nachdem ein Workspace gelöscht wurde, kann er nicht wiederhergestellt werden.
{% endalert %}

![Die Seite App-Einstellungen mit einem Button zum Löschen eines Workspace und einem Mülleimer-Symbol zum Löschen einer App.][9]

## Häufig gestellte Fragen

### Sollte ich einen neuen Workspace erstellen, wenn ich eine aktualisierte App veröffentliche?

Wenn Benutzer nur ihre App aktualisieren müssen und Sie keine völlig neue App im App Store veröffentlichen, sollten Sie keinen neuen Arbeitsbereich erstellen, es sei denn, Sie haben nicht vor, die Benutzer der älteren Version nicht mehr zu benachrichtigen.

Wenn Sie einen neuen Arbeitsbereich erstellen, werden alle historischen Daten und Benutzerprofile aus der älteren App-Version in diesem neuen Arbeitsbereich nicht mehr vorhanden sein. Wenn Sie also ein Upgrade auf die neue App-Version durchführen, wird ein neues Profil ohne die Verhaltensdaten aus der alten App erstellt.

Außerdem würden Ihre Nutzer:innen an zwei Orten existieren: im alten Workspace und im neuen Workspace. Sie können auch potenziell denselben Push-Token haben. Dies kann dazu führen, dass Nutzer:innen eine Marketing-Nachricht erhalten, die sich nur an Nutzer:innen des alten Workspace richtet, auch wenn sie bereits aktualisiert haben.

#### Was sollte ich stattdessen tun?

Um alte und neue Apps zu trennen, erstellen Sie eine neue App-Instanz innerhalb desselben Workspace. Auf diese Weise können Sie effektiv Zielgruppen aus Nutzer:innen der neuen Version ansprechen, wenn Sie diese App bei der Segmentierung auswählen. Wenn Sie Nutzern, die eine alte Version verwenden, eine Nachricht zukommen lassen möchten, können Sie Filter verwenden, die [auf die vorherige App-Version abzielen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

### Ich habe mehrere App-Instanzen in einem Workspace. Wie kann ich sicherstellen, dass ich mit meiner Nachricht nur eine einzige App anspreche? {#singular-app}

Um sicherzustellen, dass Ihre Nachricht nur auf eine bestimmte App abzielt, fügen Sie ein Segment hinzu, das nur Nutzer:innen der von Ihnen gewählten App-Instanzen anspricht. Dies ist besonders wichtig, wenn ein Benutzer möglicherweise zwei Push-Token für verschiedene App-Instanzen im selben Arbeitsbereich hat. In diesem Szenario könnten Benutzer eine Benachrichtigung für eine andere App erhalten als die, in der sie sich gerade befinden. Nicht gerade eine ideale Erfahrung!

Standardmäßig zielt ein Segment auf alle Apps und Websites im Workspace ab. So richten Sie ein Segment ein, das nur auf eine App oder Website abzielt:

1. Erstellen Sie ein Segment mit einem aussagekräftigen Namen. Bei Braze verwenden wir das Format "Alle Benutzer ({Name} {Plattform})". Zum Beispiel: "Alle Benutzer (auf Voyage iOS)".
2. Für **gezielte Apps und Websites** wählen Sie **Benutzer aus bestimmten Apps**.
3. Wählen Sie in der Dropdown-Liste **Spezifische Apps** Ihre App oder Website aus.

![Segmente, die Nutzer:innen aus bestimmten Apps zusammenstellen.][10]

Sie können dieses Segment dann zu Ihrer Nachricht hinzufügen und Ihre Zielgruppe bei Bedarf mit zusätzlichen Segmenten und Filtern weiter verfeinern.

#### Kampagnen

Für Kampagnen fügen Sie Ihr Segment im Schritt **Zielbenutzer** des Composers hinzu.

#### Canvas Flow

In Canvas Flow fügen Sie Ihr Segment zu Ihren Nachrichtenschritten hinzu, und zwar im Abschnitt **Zustellungsvalidierungen**. Zustellungsvalidierungen überprüfen nochmals, dass Ihre Zielgruppe die Zustellungskriterien beim Senden der Nachrichten erfüllt. Denken Sie daran, für jeden Nachrichtenschritt Zustellungsvalidierungen festzulegen, um sicherzustellen, dass die Nachricht an die richtige App zugestellt wird. Eine Segmentierung auf der Einstiegsebene ist nicht erforderlich.

{% details Erweitern für Schritte im ursprünglichen Canvas-Workflow %}

{% alert important %}
Ab dem 28\. Februar 2023 können Sie keine Canvase mehr mit dem Original-Editor erstellen oder duplizieren. Dieser Inhalt ist als Referenz verfügbar, um Segmente und Targeting im Original-Editor zu verstehen.<br><br>Braze empfiehlt Kund:innen, die die ursprüngliche Canvas-Umgebung nutzen, den Wechsel zu Canvas Flow. Es handelt sich um eine verbesserte Bearbeitungsfunktion, mit der Sie Canvases besser erstellen und verwalten können. Erfahren Sie mehr über das [Klonen Ihrer Canvases in Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

Im ursprünglichen Canvas-Workflow fügen Sie Ihr Segment auf der Canvas-Komponentenebene im Bereich **Zielgruppe** hinzu. Eine Segmentierung auf der Einstiegsebene ist nicht erforderlich.
{% enddetails %}


[1]: {% image_buster /assets/img/workspaces/workspace_create.png %}
[2]: {% image_buster /assets/img/workspaces/workspace_name.png %}
[3]: {% image_buster /assets/img/workspaces/workspace_empty_state.png %}
[4]: {% image_buster /assets/img/workspaces/workspace_add_app.png %}
[5]: {% image_buster /assets/img/workspaces/app_api_key.png %}
[6]: {% image_buster /assets/img/workspaces/app_live_sdk_version.png %}
[7]: {% image_buster /assets/img/workspaces/workspace_favorites.png %}
[8]: {% image_buster /assets/img/workspaces/workspace_rename.gif %}
[9]: {% image_buster /assets/img/workspaces/workspace_delete.png %}
[10]: {% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %}
[Link]: {{site.baseurl}}/user_guide/getting_started/workspaces/
