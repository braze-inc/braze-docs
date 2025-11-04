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

Bevor Sie beginnen, stellen Sie sicher, dass Sie mit Ihrem Team und Ihrem Braze Onboarding Manager zusammenarbeiten, um die beste Workspace-Konfiguration für Ihren Anwendungsfall zu bestimmen. To learn more about planning your workspaces in Braze, check out our [Getting Started: Workspaces]({{site.baseurl}}/user_guide/getting_started/workspaces/) guide.

### Schritt 2: Ihren Arbeitsbereich hinzufügen

Sie können über das Dropdown-Menü Arbeitsbereich in der globalen Kopfzeile neue Arbeitsbereiche erstellen oder zwischen bestehenden Arbeitsbereichen wechseln.

1. Wählen Sie das Dropdown-Menü Workspace und dann <i class="fa-solid fa-square-plus" style="color: #0b8294;"></i> **Workspace erstellen**.

\![Das Workspace-Dropdown mit dem Button "Workspace erstellen".]({% image_buster /assets/img/workspaces/workspace_create.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Geben Sie Ihrem Arbeitsbereich einen Namen.

{% alert tip %}
Vielleicht möchten Sie eine Namenskonvention festlegen, damit andere in Ihrem Unternehmen Ihren Arbeitsbereich leicht finden können. Zum Beispiel: "Upon Voyage US - Produktion" und "Upon Voyage US - Inszenierung".
{% endalert %}

{:start="3"}
3\. Wählen Sie **Erstellen**. Es kann ein paar Sekunden dauern, bis Braze Ihren Arbeitsbereich erstellt hat.

\!["Workspace erstellen"-Modal mit dem Namen "Upon Voyage US - Staging".]({% image_buster /assets/img/workspaces/workspace_name.png %}){: style="max-width:60%" }

Sie werden zur Seite **App-Einstellungen** weitergeleitet, auf der Sie Ihre App-Instanzen hinzufügen können. Sie können diese Seite jederzeit über **Einstellungen** > **App-Einstellungen** aufrufen.

\!["App-Einstellungen"-Seite für den Upon Voyage US - Staging Workspace mit einem Button zum Hinzufügen einer App.]({% image_buster /assets/img/workspaces/workspace_empty_state.png %})

### Schritt 3: Fügen Sie Ihre App-Instanzen hinzu

Wir bezeichnen die verschiedenen Websites und Apps, die innerhalb eines Workspace gesammelt werden, als "App-Instanzen".

1. Wählen Sie auf der Seite mit **den App-Einstellungen** **\+ App hinzufügen**.
2. Geben Sie Ihrer App-Instanz einen Namen und wählen Sie aus, auf welcher Plattform oder welchen Plattformen diese App-Instanz läuft. Wenn Sie mehrere Plattformen auswählen, wird Braze eine App-Instanz für jede Plattform erstellen.

\!["Neue App zu Upon Voyage US - Staging hinzufügen"-Modal mit Optionen zum Auswählen von App-Details.]({% image_buster /assets/img/workspaces/workspace_add_app.png %}){: style="max-width:60%" }

{:start="3"}
3\. Wählen Sie zur Bestätigung **App hinzufügen**.

#### App API-Schlüssel

Nachdem Sie Ihre App-Instanz hinzugefügt haben, haben Sie Zugang zu ihrem API-Schlüssel. Der API-Schlüssel wird verwendet, wenn Sie Anfragen zwischen Ihrer App-Instanz und der Braze API stellen. Der API-Schlüssel ist auch wichtig für die Integration des Braze SDK mit Ihrer App oder Website.

\![Einstellungsseite für die Upon Voyage iOS App mit Feldern für den API-Schlüssel und den SDK-Endpunkt.]({% image_buster /assets/img/workspaces/app_api_key.png %})

{% alert note %}
Sie müssen für jede Version Ihrer App auf jeder Plattform separate App-Instanzen erstellen. Wenn Sie zum Beispiel eine kostenlose und eine Pro-Version Ihrer App für iOS und Android haben, erstellen Sie vier App-Instanzen in Ihrem Arbeitsbereich (kostenlose iOS-App, kostenlose Android-App, Pro-iOS-App und Pro-Android-App). So erhalten Sie vier API-Schlüssel, die Sie verwenden können, einen für jede App-Instanz.
{% endalert %}

#### Live SDK Version

Die Live-SDK-Version, die auf der Seite App-Einstellungen für eine bestimmte App angezeigt wird, ist die höchste App-Version mit mindestens 5 % Ihrer täglichen Gesamtsitzungen und mindestens 500 Sitzungen am vergangenen Tag.

Dieses Feld erscheint, nachdem Sie das Braze SDK in Ihre App oder Website integriert haben. Wenn eine neuere Version des Braze SDK für Ihre Plattform verfügbar ist, wird dies hier mit dem Tag "Neuere Version verfügbar" vermerkt.

\!["Live SDK Version"-Abschnitt mit dem Feldwert "5.4.0" und einem Symbol, das besagt, dass eine neue Version verfügbar ist.]({% image_buster /assets/img/workspaces/app_live_sdk_version.png %})

### Schritt 4: Wiederholen Sie den Vorgang nach Bedarf

Wiederholen Sie die Schritte 2 und 3, um so viele Workspaces einzurichten, wie Ihr Plan erfordert. Wir empfehlen Ihnen, einen Test-Workspace für Integrationstests und Kampagnentests zu erstellen.

{% alert tip %}
**Einen Workspace zum Testen hinzufügen**<br>Sie können App-Tests durchführen, indem Sie bestimmte Nutzer:innen komplett von Ihrer Produktionsinstanz fernhalten. Erstellen Sie einen neuen Workspace, und wenn Sie Ihre Anwendung veröffentlichen, stellen Sie sicher, dass der API-Schlüssel, den Braze verwendet, mit dem Ihres Produktions-Workspace übereinstimmt und nicht mit dem Ihres Test-Workspace.
{% endalert %}

## Arbeitsbereiche verwalten

### Hinzufügen von Favoriten

Sie können bevorzugte Workspaces hinzufügen, um noch schneller auf die Workspaces zuzugreifen, die Sie am häufigsten verwenden.

\![Workspace-Dropdown mit dem Tab für "Favorisierte Workspaces".]({% image_buster /assets/img/workspaces/workspace_favorites.png %}){: style="max-width:50%;"}

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

\![Das Bleistift-Symbol erscheint neben dem Namen des Workspace.]({% image_buster /assets/img/workspaces/workspace_rename.gif %}){: style="max-width:50%;"}

### Löschen von Workspaces und App-Instanzen

So löschen Sie Ihren Workspace oder Ihre App-Instanz:

1. Gehen Sie zu **Einstellungen** > **App-Einstellungen**.
2. Wählen Sie **Workspace löschen**, um den jeweiligen Workspace zu löschen, oder wählen Sie das Mülleimer-Symbol neben der jeweiligen App-Instanz.

Sie können keine App-Instanzen oder Workspaces löschen, die derzeit für das Targeting von Nutzern:innen verwendet werden oder die mehr als 1.000 Nutzer:innen haben. Wenn Sie dies versuchen, erhalten Sie eine Fehlermeldung. Um fortzufahren und sie zu löschen, [erstellen Sie einen Support-Fall]({{site.baseurl}}/user_guide/administrative/access_braze/support/), der einen Dashboard-Link und den Namen der zu löschenden App-Instanz oder des Workspace enthält.

{% alert warning %}
Seien Sie vorsichtig beim Löschen von Arbeitsbereichen! Nachdem ein Workspace gelöscht wurde, kann er nicht wiederhergestellt werden.
{% endalert %}

\![Die Seite App-Einstellungen mit einem Button zum Löschen eines Workspace und einem Mülleimer-Symbol zum Löschen einer App.]({% image_buster /assets/img/workspaces/workspace_delete.png %})

## Häufig gestellte Fragen

### Sollte ich einen neuen Workspace erstellen, wenn ich eine aktualisierte App veröffentliche?

This depends on whether you're updating your app or creating an entirely new one.

#### Updating your app

If you're updating your app, you should separate the old and new versions by creating a new app instance within the same workspace. Auf diese Weise können Sie effektiv Zielgruppen aus Nutzer:innen der neuen Version ansprechen, wenn Sie diese App bei der Segmentierung auswählen. Wenn Sie Nutzern, die eine alte Version verwenden, eine Nachricht zukommen lassen möchten, können Sie Filter verwenden, die [auf die vorherige App-Version abzielen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

If you create a new workspace, your users will exist in two places: the old workspace and the new workspace. They could also potentially have the same push token. This can lead to users receiving a marketing message intended for only old workspace users, even if they’ve already upgraded.

#### Releasing a new app

If you're releasing an entirely new app to the app store, you should create a new workspace. Wenn Sie einen neuen Arbeitsbereich erstellen, werden alle historischen Daten und Benutzerprofile aus der älteren App-Version in diesem neuen Arbeitsbereich nicht mehr vorhanden sein. Wenn Sie also ein Upgrade auf die neue App-Version durchführen, wird ein neues Profil ohne die Verhaltensdaten aus der alten App erstellt.

### Ich habe mehrere App-Instanzen in einem Workspace. Wie kann ich sicherstellen, dass ich mit meiner Nachricht nur eine einzige App anspreche? {#singular-app}

Um sicherzustellen, dass Ihre Nachricht nur auf eine bestimmte App abzielt, fügen Sie ein Segment hinzu, das nur Nutzer:innen der von Ihnen gewählten App-Instanzen anspricht. Dies ist besonders wichtig, wenn ein Benutzer möglicherweise zwei Push-Token für verschiedene App-Instanzen im selben Arbeitsbereich hat. In diesem Szenario könnten Benutzer eine Benachrichtigung für eine andere App erhalten als die, in der sie sich gerade befinden. Nicht gerade eine ideale Erfahrung!

Standardmäßig zielt ein Segment auf alle Apps und Websites im Workspace ab. So richten Sie ein Segment ein, das nur auf eine App oder Website abzielt:

1. Erstellen Sie ein Segment mit einem aussagekräftigen Namen. Bei Braze verwenden wir das Format "Alle Benutzer ({Name} {Plattform})". Zum Beispiel: "Alle Benutzer (auf Voyage iOS)".
2. Für **gezielte Apps und Websites** wählen Sie **Benutzer aus bestimmten Apps**.
3. Wählen Sie in der Dropdown-Liste **Spezifische Apps** Ihre App oder Website aus.

Segment, das Nutzer:innen aus bestimmten Apps zusammenstellt.]({% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %})

Sie können dieses Segment dann zu Ihrer Nachricht hinzufügen und Ihre Zielgruppe bei Bedarf mit zusätzlichen Segmenten und Filtern weiter verfeinern.

#### Kampagnen

For campaigns, add your segment to the **Target Audiences** step of the composer.

#### Canvas

In Canvas, add your segment to your Message steps, in the **Delivery Validations** section. Zustellungsvalidierungen überprüfen nochmals, dass Ihre Zielgruppe die Zustellungskriterien beim Senden der Nachrichten erfüllt. Denken Sie daran, für jeden Nachrichtenschritt Zustellungsvalidierungen festzulegen, um sicherzustellen, dass die Nachricht an die richtige App zugestellt wird. Eine Segmentierung auf der Einstiegsebene ist nicht erforderlich.

{% details Expand for steps in the original Canvas workflow %}

Im ursprünglichen Canvas-Workflow fügen Sie Ihr Segment auf der Canvas-Komponentenebene im Bereich **Zielgruppe** hinzu. Eine Segmentierung auf der Einstiegsebene ist nicht erforderlich.

{% enddetails %}


