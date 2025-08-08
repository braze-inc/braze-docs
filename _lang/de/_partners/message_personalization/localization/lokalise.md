---
nav_title: Lokalise
article_title: Lokalise
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Lokalise, einem Dienst für Übersetzungsmanagement für agile Teams."
alias: /partners/lokalise/
page_type: partner
search_tag: Partner

---

# Lokalise

> [Lokalise](https://lokalise.com) ist ein Dienst für das Übersetzungsmanagement agiler Teams.

_Diese Integration wird von Lokalise gepflegt._

## Über die Integration

Die Integration von Braze und Lokalise nutzt Connected-Content, um Ihnen das einfache Einfügen übersetzter Inhalte in Ihre Braze Kampagnen auf der Grundlage der Nutzer:innen-Einstellungen zu ermöglichen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Lokalise Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Lokalise-Konto. |
| Lokalise Übersetzungsprojekt | Bevor Sie diese Integration einrichten, sollten Sie ein Lokalise-Übersetzungsprojekt erstellen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erstellen Sie ein neues Lokalise Projekt

Um ein neues Übersetzungsprojekt zu erstellen, melden Sie sich bei Lokalise an und wählen Sie **Neues Projekt**. Als Nächstes benennen Sie Ihr Projekt, wählen eine **Basissprache** (die Sprache, aus der Sie übersetzen werden), fügen eine oder mehrere **Zielsprachen** hinzu und wählen den Projekttyp **Softwarelokalisierung**. Wenn Sie bereit sind, klicken Sie auf **Fortfahren**.

## Integration

In Lokalise erstellen Sie für jede der Connected-Content-Variablen, die Sie in Braze definieren, einen Übersetzungsschlüssel. Wenn die Übersetzungen fertig sind, können Sie eine JSON-Datei pro Sprache generieren und sie auf den URLs veröffentlichen, die Ihre Connected-Content-Inhalte bereitstellen werden.

### Schritt 1: Konfiguration der Nutzer:innen Sprachen

Falls Sie es noch nicht getan haben, öffnen Sie das Braze-Dashboard und gehen Sie zu **Nutzer:innen > Nutzerimport.** Hier können Sie Ihre Nutzer:innen importieren. Wenn Sie eine CSV-Datei für den Import vorbereiten, stellen Sie sicher, dass Sie eine Sprachspalte mit den Sprachen der Nutzer:innen einfügen. Dieses Sprachfeld wird später bei der Anzeige von Übersetzungen verwendet. 

{% alert important %}
Die verwendeten Sprachcodes müssen sowohl in Braze als auch in Lokalise übereinstimmen.
{% endalert %}
### Schritt 2: Vorbereitungen für Ihre Übersetzungen auf Lokalise

Um Ihre Übersetzungen in Lokalise vorzubereiten, müssen Sie als Nächstes manuell die Übersetzungsschlüssel mit demselben Namen erstellen, den Sie in den Variablen von Braze Connected-Content verwenden. 

Lassen Sie uns zum Beispiel einen einfachen Übersetzungsschlüssel erstellen: `description`:
1. Öffnen Sie Ihr Lokalise Projekt, klicken Sie auf **Schlüssel hinzufügen** und geben Sie "Beschreibung" in das Feld **Schlüssel** ein.
2. Geben Sie "Demo-Beschreibung" in das Feld **Basis-Sprachwert** ein.
3. Fügen Sie "Internet" in der Dropdown-Liste " **Plattformen** " hinzu. 
4. Wenn Sie fertig sind, klicken Sie auf **Speichern**.

![]({% image_buster /assets/img/lokalise/1_add_key.png %}){: style="max-width:60%"}

Ihr Übersetzungsschlüssel sollte im Projekteditor erscheinen:

![]({% image_buster /assets/img/lokalise/2_translation_key_added.png %}){: style="max-width:90%"}

#### Bekannte Probleme

- Ihre Schlüssel müssen der **Internet-Plattform** zugewiesen sein.
- Vermeiden Sie die Verwendung von Schlüsseln, die Punkte (`.`) oder den String `_on` enthalten. Verwenden Sie zum Beispiel `this_is_the_key` anstelle von `this.is.the.key` und `join_us_instagram` anstelle von `join_us_on_instagram`.

### Schritt 3: Konfigurieren der Braze App auf der Lokalise

Öffnen Sie Ihr Lokalise Projekt, und klicken Sie auf **Apps**. Suchen und installieren Sie hier die App Braze. Sie sehen dann den folgenden Bildschirm:

![Braze-Konfiguration auf Lokalise mit Angabe der Projekt ID und der URL der Übersetzungsdateien.]({% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %})

In der **URL der Übersetzungsdatei** veröffentlicht Lokalise eine JSON-Datei mit allen Übersetzungen für Ihre Schlüssel im Projekt. Sie erhalten so viele URLs von Übersetzungsdateien, wie Sie Zielsprachen in Ihrem Projekt haben. Aus diesem Grund bestehen die URLs der Übersetzungsdateien aus zwei Teilen:

1. Der erste Teil des URL-Pfads ist für alle Sprachen gleich.
2. Der JSON-Dateiname am Ende der URL basiert auf dem Code der Sprache.

Die URL der Übersetzungsdatei ist die URL, die Sie benötigen, wenn Sie eine Kampagne von Braze konfigurieren. Sie können den Inhalt der JSON-Datei aktualisieren, indem Sie auf **Aktualisieren** klicken. Beachten Sie, dass die URL gleich bleibt und Sie Ihren Connected-Content-Aufruf in Braze nicht ändern müssen.

### Test-URL

Um diese URL zu testen, kopieren Sie sie und ersetzen Sie {% raw %}`{{${language}}}`{% endraw %} durch einen Sprachcode (z.B. `en`) und öffnen Sie diese URL in Ihrem Browser. Sie sehen dann eine JSON-Datei mit Ihren Schlüsseln und Übersetzungen:

![]({% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %})

### Schritt 4: Übersetzungen in der Braze Kampagne verwenden

#### Connected-Content-Aufruf einfügen

Wenn Sie fertig sind, kehren Sie zu Braze zurück und öffnen eine bestehende Kampagne oder erstellen eine neue Kampagne. Für dieses Beispiel erstellen wir eine neue E-Mail Kampagne mit Beispielinhalten. Klicken Sie auf **E-Mail-Text bearbeiten**.

Um Ihre Übersetzungen einzufügen, müssen Sie die Anfrage für Connected-Content in den HTML-Code einfügen, entweder am Anfang des Dokuments oder direkt vor der ersten Stelle, an der eine Übersetzung benötigt wird. Dies kann durch Einfügen der folgenden Markierung geschehen:

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

Ersetzen Sie die URL `https://exports.live.lokalise.cloud/...` durch die URL der Übersetzungsdatei, die Sie im vorherigen Schritt abgerufen haben.

{% raw %}

- `{{${language}}}` bedeutet "Nutzersprache an dieser Stelle einfügen". Alternativ können Sie den Code Ihrer Sprache auch fest codieren, z.B. `en.json`.
  - Um sicherzustellen, dass für jeden Nutzer die passende übersetzte JSON-Datei abgerufen wird, müssen Sie entweder das Attribut `{{${language}}}` oder ein ähnliches angepasstes Attribut, das die Sprache des Nutzers enthält, an das Ende der URL der Übersetzungsdateien setzen. (z.B. `/{{${language}}}.json`) Die in diesen Attributen enthaltenen Werte müssen mit dem Präfix jeder der übersetzten JSON-Dateien übereinstimmen. So wird sichergestellt, dass für jeden Nutzer:innen die richtige Übersetzungsdatei zurückgegeben wird.
- `:save translations` speichert den JSON-Inhalt unter der Variablen translations.

#### Übersetzungen anzeigen

Verwenden Sie nun die Variable Übersetzungen, um die gewünschten Übersetzungen nach ihren Schlüsseln anzuzeigen.

Um zum Beispiel die Taste `description` anzuzeigen, verwenden Sie`{{ translations.description }}`.

{% endraw %}
![]({% image_buster /assets/img/lokalise/6_integration_usage_sample.png %})

Zum Schluss speichern Sie das Template für die E-Mail und zeigen es in der Vorschau an. Sie sollten sehen, dass Ihre Übersetzung angezeigt wird.

## Häufig gestellte Fragen

**Was passiert, wenn ich versehentlich einen Schlüssel aus Lokalise lösche?**<br>
Für den entsprechenden String auf Braze gibt es keine Übersetzung mehr.

**Wenn ich eine `en` Lokalisierung habe, diese aber mit `en-US` auf Lokalise überschreibe, wird Braze sie dann als `en-US` lesen?**<br>
Nein, die ISO-Codes der Lokalisierung müssen auf Braze und Lokalise übereinstimmen.

**Können wir die Flagge `:rerender` verwenden, wenn wir Lokalise-Inhalte verbinden?**<br>
Ja, sicher. Sie können in den Braze-Dokumenten nachlesen, wie Sie dieses Flag hinzufügen können.

**Warum kann ich nach dem Aktualisieren der Übersetzungsdatei auf Lokalise keine Änderungen in den übersetzten Inhalten auf Braze sehen?**<br>
Braze speichert übersetzte Inhalte im Cache. Die Aktualisierung kann einige Minuten dauern. Wenn Sie Ihre Kampagnen testen und die Ergebnisse der Übersetzungen sofort sehen müssen, können Sie den Parameter `:cache_max_age` verwenden, wie in diesem Artikel referenzieren.


