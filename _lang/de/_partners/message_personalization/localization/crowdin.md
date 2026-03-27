---
nav_title: Crowdin
article_title: Crowdin
description: "Verwenden Sie die Crowdin-Integration, um Kampagnen, Canvas-Erlebnisse, E-Mail-Templates und Content-Blöcke mit Translation Memory, Glossaren und maschineller Übersetzung zu übersetzen."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> [Crowdin](https://crowdin.com/) ist eine KI-gestützte Plattform zur Verwaltung der Lokalisierung, die Teams dabei unterstützt, die Übersetzung ihrer Software, Apps und Marketing-Inhalte zu automatisieren.

Verbinden Sie Crowdin mit Braze, um Übersetzungen für Ihre Kampagnen und Canvas-Erlebnisse zu verwalten. Die automatische Synchronisierung arbeitet mit maschineller Übersetzung, Translation Memory und Glossaren, sodass manuelle und automatisierte Workflows konsistent bleiben.

_Diese Integration wird von Crowdin gepflegt._

## Über die Integration

Crowdin bietet zwei Apps für Braze: [Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) und [Braze Email Templates](https://store.crowdin.com/braze-app). Wählen Sie die App basierend auf den Braze-Features, die Sie lokalisieren möchten. Die folgende Tabelle vergleicht sie.

### Die richtige Crowdin-App auswählen

| Kanal oder Feature | Braze Campaigns & Canvas | Braze Email Templates |
| --- | --- | --- |
| **Kampagnen** | ✅ Unterstützt | ❌ Nicht unterstützt |
| **Canvas-Schritte** | ✅ Unterstützt | ❌ Nicht unterstützt |
| **E-Mail-Templates** | ❌ Nicht unterstützt | ✅ Unterstützt |
| **Content-Blöcke** | ❌ Nicht unterstützt | ✅ Unterstützt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| **Crowdin-Konto** | Ein [Crowdin.com-Konto](https://accounts.crowdin.com/register) oder ein [Crowdin-Enterprise-Konto](https://accounts.crowdin.com/workspace/create) ist erforderlich. |
| **Crowdin-Projekt** | Bevor Sie Braze verbinden, [erstellen Sie ein Übersetzungsprojekt](https://support.crowdin.com/creating-project/) in Crowdin oder Crowdin Enterprise. |
| **Braze REST-API-Schlüssel** | Ein Braze REST-API-Schlüssel mit Berechtigungen für Kampagnen, Canvas, Content-Blöcke, angepasste Attribute, E-Mail und Templates. |
| **Braze REST-Endpunkt** | Die spezifische URL Ihres Braze REST-Endpunkts (zum Beispiel `https://rest.iad-03.braze.com`). |
| **Braze-Mehrsprachigkeitseinstellungen** | Locales müssen in Ihrem Braze-Dashboard unter **Einstellungen** > **Lokalisierungseinstellungen** konfiguriert sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration von Braze Campaigns & Canvas

Wenn Sie Inhalte in aktiven Nachrichten lokalisieren, verwenden Sie die [Braze Campaigns & Canvas App](https://store.crowdin.com/braze-content-translation), um übersetzbare Strings aus Ihren Kampagnen- und Canvas-Entwürfen mit der Braze-Mehrsprachigkeitsunterstützung zu synchronisieren.

Eine Video-Anleitung finden Sie unter [Braze Campaigns & Canvas Integration](https://youtu.be/ahG1ET4VRKA).

### 1. Schritt: Mehrsprachigkeitseinstellungen in Braze einrichten

Bevor Sie Crowdin verbinden, fügen Sie Ihre Zielsprachen in Braze hinzu.

1. Gehen Sie in Braze zu **Einstellungen** > **Lokalisierungseinstellungen**.
2. Fügen Sie die Sprachen hinzu, die Sie unterstützen möchten.

![Braze-Seite „Locales" unter „Einstellungen" mit Locale-Namen, Locale-Schlüsseln und „Locale hinzufügen".]({% image_buster /assets/img/crowdin/braze_locales.png %})

{: start="3"}
3. Notieren Sie sich jeden **Locale-Schlüssel** (zum Beispiel `en-US`, `fr-FR`, `es-ES`). Sie verwenden diese Werte, wenn Sie Sprachen in Crowdin zuordnen.

### 2. Schritt: Das Braze-Projekt in Crowdin einrichten

1. Gehen Sie in Ihrem Crowdin-Enterprise- oder Crowdin.com-Konto zum **Store** im linken Menü.
2. Suchen Sie nach **Braze Campaigns & Canvas** und wählen Sie **Installieren**.

![Crowdin Store mit ausgewähltem „Braze Campaigns & Canvas" und hervorgehobenem „Installieren".]({% image_buster /assets/img/crowdin/crowdin_store_campaigns_canvas.png %})

{: start="3"}
3. Wählen Sie das Projekt (oder die Projekte) aus, in dem Sie diese Integration verwenden möchten.
4. Um die Integration zu öffnen, gehen Sie zu Ihrem Projekt **Integrationen** > **Braze Campaigns & Canvas**.

#### Braze mit Crowdin verbinden

Autorisieren Sie die Verbindung mit Ihren Braze-API-Zugangsdaten:

![Crowdin-Verbindungsformular für Braze Campaigns & Canvas mit REST-API-Schlüssel, REST-Endpunkt und „Mit Braze Campaigns & Canvas anmelden".]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_login.png %})

- **Braze REST-API-Schlüssel:** Erstellen Sie diesen in Braze unter **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**. Erteilen Sie die Berechtigungen, die diese Integration benötigt (Kampagnen, Canvas, Content-Blöcke und angepasste Attribute).
- **Braze REST-Endpunkt:** Geben Sie die URL für Ihre Braze-Instanz ein (zum Beispiel `https://rest.iad-03.braze.com`). Weitere Informationen finden Sie unter [REST-API-Endpunkte]({{site.baseurl}}/api/basics/#endpoints).

![Braze-Seite „REST-API-Schlüssel" mit „API-Schlüssel erstellen" und dem Kopiersteuerelement für den REST-Endpunkt.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

Wählen Sie **Mit Braze Campaigns & Canvas anmelden**.

### 3. Schritt: Sprachzuordnung in Crowdin konfigurieren

Nachdem Sie Ihr Konto verbunden haben, ordnen Sie jede Crowdin-Projektsprache dem entsprechenden Braze-Locale zu.

1. Wählen Sie im Integrations-Dashboard von **Braze Campaigns & Canvas** das **Zahnradsymbol** für Einstellungen in der oberen rechten Ecke.

![Integrationsbildschirm von Braze Campaigns & Canvas mit „Einstellungen" in der oberen Aktionsleiste.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_settings.png %})

{: start="2"}
2. Öffnen Sie den Tab **Allgemeine Einstellungen**.
3. Geben Sie die Locale-Schlüssel ein. Crowdin listet Ihre Projektsprachen auf (zum Beispiel Französisch, Italienisch). Geben Sie in jedem Feld den passenden **Braze-Locale-Schlüssel** ein.
   - Wenn Braze beispielsweise `it` für Italienisch verwendet, geben Sie `it` neben Italienisch in Crowdin ein.
   - Jeder Eintrag muss exakt mit dem **Locale-Schlüssel** für dieses Locale in den Braze-**Lokalisierungseinstellungen** übereinstimmen.

![Einstellungs-Modal auf dem Tab „Allgemeine Einstellungen" mit Dateifilterfeldern und Sprachzuordnungszeilen (zum Beispiel Französisch zugeordnet zu fr).]({% image_buster /assets/img/crowdin/crowdin_language_mapping_settings.png %})

{: start="4"}
4. Wählen Sie **Speichern**, um die Zuordnung zu bestätigen.

### 4. Schritt: Übersetzungs-Tags zu Ihrer Braze-Nachricht hinzufügen

Crowdin liest dieselben Liquid-**Übersetzungs-Tags**, die Braze für mehrsprachige Nachrichten verwendet. Fügen Sie {% raw %}`{% translation your_id_here %}` und `{% endtranslation %}`{% endraw %} um jeden Text, jede Bild-URL oder Link-URL hinzu, die übersetzt werden soll. Jeder Block benötigt eine eindeutige `id` (zum Beispiel `greeting` oder `welcome_header`).

**Beispiel:**

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

Für HTML, Liquid in Links und andere Muster befolgen Sie dieselben Regeln wie unter [Locales übersetzen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales) (zum Beispiel Tags um die kleinstmöglichen Segmente setzen und nur sprachspezifische Teile von URLs umschließen, wenn Sie Links lokalisieren).

Speichern Sie Ihre Braze-Nachricht als **Entwurf**, bevor Crowdin den Inhalt erkennen und abrufen kann.

### 5. Schritt: Übersetzungen in Crowdin verwalten

Der Integrationsbildschirm hat zwei Seiten:

- **Rechte Seite (Braze):** Ihre Kampagnen und Canvase.
- **Linke Seite (Crowdin):** Bereits zur Übersetzung synchronisierte Inhalte.

![Crowdin- und Braze-Campaigns-&-Canvas-Panels mit Ordnern für Kampagnen und Locales, „Mit Braze synchronisieren" und „Mit Crowdin synchronisieren".]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_sync_panels.png %})

#### Inhalte synchronisieren

1. Aktivieren Sie auf der **Braze-Seite (rechts)** das Kontrollkästchen für die Kampagne oder das Canvas, das Sie übersetzen möchten.
2. Wählen Sie **Mit Crowdin synchronisieren**.
3. Wenn die Synchronisierung abgeschlossen ist, erscheint die Datei auf der **Crowdin-Seite (links)**. Übersetzer:innen können die Strings im Crowdin-Editor öffnen.

#### Übersetzungen an Braze zurückgeben

1. Wenn die Übersetzungen in Crowdin zu 100 % abgeschlossen sind, kehren Sie zum Tab **Integrationen** zurück.
2. Wählen Sie den abgeschlossenen Inhalt auf der **Crowdin-Seite (links)** aus.
3. Wählen Sie **Mit Braze synchronisieren**. Dadurch werden die übersetzten Strings in die entsprechenden Sprachvarianten Ihrer Braze-Kampagne übertragen.

### 6. Schritt: Nachricht als mehrsprachige:r Nutzer:in in Braze in der Vorschau anzeigen

So bestätigen Sie die Integration:

1. Öffnen Sie Ihre Kampagne im **Braze-Nachrichten-Editor**.
2. Gehen Sie zum Tab **Test**.
3. Wählen Sie **Nachricht als Nutzer:in in der Vorschau anzeigen**.
4. Suchen Sie nach einem Nutzerprofil, das ein `language`-Attribut hat, das einem Ihrer übersetzten Locales entspricht.
5. Bestätigen Sie, dass der Inhalt von der Ausgangssprache zur übersetzten Version wechselt.

## Integration von Braze Email Templates

Wenn Sie E-Mails auf Template-Ebene lokalisieren, verwenden Sie die [Braze Email Templates App](https://store.crowdin.com/braze-app), um HTML aus Ihrer Braze-Medienbibliothek zu synchronisieren.

Eine Video-Anleitung finden Sie unter [Braze Email Templates Integration](https://youtu.be/g0YMKW3jEjk).

### 1. Schritt: App installieren

1. Gehen Sie in Ihrem Crowdin-Projekt zum Tab **Store**.
2. Suchen Sie nach **Braze Email Templates** und wählen Sie **Installieren**.

![Crowdin Store mit ausgewähltem „Braze Email Templates" und hervorgehobenem „Installieren".]({% image_buster /assets/img/crowdin/crowdin_store_email_templates.png %})

{: start="3"}
3. Wählen Sie das Projekt (oder die Projekte) aus, in dem Sie diese Integration verwenden möchten.
4. Um die Integration zu öffnen, gehen Sie zu Ihrem Projekt **Integrationen** > **Braze Email Templates**.

### 2. Schritt: Mit Braze verbinden

Autorisieren Sie die Verbindung mit Ihren Braze-API-Zugangsdaten:

![Crowdin-Verbindungsformular für Braze Email Templates mit REST-API-Schlüssel, REST-Endpunkt und „Mit Braze Email Templates anmelden".]({% image_buster /assets/img/crowdin/crowdin_email_templates_login.png %}){: style="max-width:85%;"}

1. **Braze REST-API-Schlüssel:** Erteilen Sie `templates.email` und `content_blocks` (Lesen und Schreiben). Erstellen Sie den Schlüssel in Braze unter **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**.

![Braze-Seite „REST-API-Schlüssel" mit „API-Schlüssel erstellen" und dem Kopiersteuerelement für den REST-Endpunkt.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

{: start="2"}
2. Geben Sie für den **Braze REST-Endpunkt** Ihre instanzspezifische URL ein (zum Beispiel `https://rest.iad-03.braze.com`).
3. Wählen Sie **Mit Braze Email Templates anmelden**.

### 3. Schritt: Inhalte zur Übersetzung synchronisieren

Der Integrationsbildschirm zeigt Ihre Braze-Bibliothek:

- **Rechte Seite (Braze):** **E-Mail-Templates** und **Content-Blöcke**, die Sie synchronisieren können.
- **Linke Seite (Crowdin):** Inhalte in der Übersetzung.

1. Aktivieren Sie auf der **Braze-Seite (rechts)** das Kontrollkästchen neben den Templates oder Blöcken, die Sie lokalisieren möchten.
2. Wählen Sie **Mit Crowdin synchronisieren**.
3. Crowdin ruft den HTML-Quellcode ab. Übersetzer:innen arbeiten im Crowdin-Editor mit einer Live-**WYSIWYG-Vorschau**, sodass das Layout erhalten bleibt.

![Crowdin-Editor-Vorschau-Tab mit lokalisiertem E-Mail-HTML und übersetzbaren Strings.]({% image_buster /assets/img/crowdin/crowdin_editor_wysiwyg_preview.png %}){: style="max-width:85%;"}

### 4. Schritt: Übersetzte Templates bereitstellen

Wenn die Übersetzungen 100 % Fertigstellung erreichen:

1. Wählen Sie die abgeschlossenen Dateien auf der **Crowdin-Seite (links)** aus.
2. Wählen Sie **Mit Braze synchronisieren**.
3. Crowdin erstellt automatisch lokalisierte Versionen dieser Assets in Ihrer Braze-Medienbibliothek (zum Beispiel `Template_Name_fr`).

![Crowdin- und Braze-Email-Templates-Panels mit E-Mail-Templates und Content-Blöcken, mit „Mit Braze synchronisieren" und „Mit Crowdin synchronisieren".]({% image_buster /assets/img/crowdin/crowdin_email_templates_sync_panels.png %})