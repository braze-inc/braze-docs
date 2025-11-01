### Voraussetzungen

Bevor Sie diese Methode der Integration nutzen können, müssen Sie [ein Konto und einen Container für Google Tag Manager:in erstellen](https://support.google.com/tagmanager/answer/14842164).

### Schritt 1: Öffnen Sie die Galerie der Tags-Vorlagen

Wählen Sie in [Google Tag Manager:](https://tagmanager.google.com/)in Ihren Workspace und wählen Sie dann **Templates** aus. Wählen Sie im Bereich **Tag-Vorlage** die Option **Galerie suchen** aus.

![Die Templates-Seite für einen beispielhaften Workspace in Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### Schritt 2: Fügen Sie das Template für den Tag der Initialisierung hinzu

Suchen Sie in der Galerie der Templates nach `braze-inc` und wählen Sie **Braze Initialization Tag** aus.

![Die Template-Galerie mit den verschiedenen 'braze-inc' Templates.]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

Wählen Sie **Zum Workspace hinzufügen** > **Hinzufügen**.

![Die Seite 'Braze Initialization Tag' im Google Tag Manager.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### Schritt 3: Konfigurieren Sie den Tag

Wählen Sie im Bereich **Templates** Ihre neu hinzugefügte Vorlage aus.

![Die Seite "Templates" im Google Tag Manager zeigt das Braze Initialization Tag Template.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

Wählen Sie das Bleistiftsymbol aus, um das Dropdown-Menü **Tag-Konfiguration** zu öffnen.

![Die Kachel "Tag-Konfiguration" mit dem Bleistift-Symbol.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

Geben Sie die erforderlichen Mindestinformationen ein:

| Feld         | Beschreibung |
| ------------- | ----------- |
| **API-Schlüssel**   | Ihren [Braze API-Schlüssel]({{site.baseurl}}/api/basics/#about-rest-api-keys), den Sie auf dem Braze-Dashboard unter **Einstellungen** > **App-Einstellungen** finden. |
| **API-Endpunkt** | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
| **SDK Version**  | Die aktuellste `MAJOR.MINOR` Version des Internet Braze SDK, die im [Changelog]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web) aufgeführt ist. Wenn die neueste Version beispielsweise `4.1.2` ist, geben Sie `4.1` ein. Weitere Informationen finden Sie unter [Über SDK-Versionsverwaltung]({{site.baseurl}}/developer_guide/sdk_integration/version_management/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Für zusätzliche Initialisierungseinstellungen wählen Sie **Braze Initialisierungsoptionen** und wählen Sie die gewünschten Optionen.

![Die Liste der Braze-Initialisierungsoptionen finden Sie unter 'Tag-Konfiguration'.]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### Schritt 4: Auf *allen Seiten* triggern

Der Tag zur Initialisierung sollte auf allen Seiten Ihrer Website ausgeführt werden. Dies erlaubt Ihnen die Verwendung von Braze SDK-Methoden und die Aufzeichnung von Web-Push-Analytics.

### Schritt 5: Überprüfen Sie Ihre Integration

Sie können Ihre Integration mit einer der folgenden Optionen überprüfen:

- **Option 1:** Mit dem [Debugging-Tool](https://support.google.com/tagmanager/answer/6107056?hl=en) des Google Tag Managers können Sie überprüfen, ob das Braze Initialization Tag auf Ihren konfigurierten Seiten oder Ereignissen korrekt triggert.
- **Option 2:** Prüfen Sie, ob von Ihrer Webseite aus Netzwerkanfragen an Braze gestellt wurden. Außerdem sollte jetzt die globale Bibliothek `window.braze` definiert werden.
