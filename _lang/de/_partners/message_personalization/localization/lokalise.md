---
nav_title: Lokalise
article_title: Lokalise
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Lokalise, einem Übersetzungsmanagement-Service für agile Teams."
alias: /partners/lokalise/
page_type: partner
search_tag: Partner

---

# Lokalise

> [Lokalise](https://lokalise.com) ist ein Übersetzungsmanagement-Service für agile Teams.

Die Integration von Braze und Lokalise nutzt Connected Content, damit Sie auf der Grundlage der Spracheinstellungen des Benutzers problemlos übersetzte Inhalte in Ihre Braze-Kampagnen einfügen können.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Lokalise Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Lokalise-Konto. |
| Lokalise Übersetzungsprojekt | Bevor Sie diese Integration einrichten, sollten Sie ein Lokalise-Übersetzungsprojekt erstellen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erstellen Sie ein neues Lokalise Projekt

Um ein neues Übersetzungsprojekt zu erstellen, melden Sie sich bei Lokalise an und wählen Sie **Neues Projekt**. Als Nächstes benennen Sie Ihr Projekt, wählen eine **Basissprache** (die Sprache, aus der Sie übersetzen werden), fügen eine oder mehrere **Zielsprachen** hinzu und wählen den Projekttyp **Softwarelokalisierung**. Wenn Sie bereit sind, klicken Sie auf **Fortfahren**.

## Integration

In Lokalise erstellen Sie für jede der Connected Content-Variablen, die Sie in Braze definieren, einen Übersetzungsschlüssel. Wenn die Übersetzungen fertig sind, können Sie eine JSON-Datei pro Sprache erstellen und sie auf den URLs veröffentlichen, die Ihre Connected Content bereitstellen werden.

### Schritt 1: Benutzersprachen konfigurieren

Falls Sie dies noch nicht getan haben, öffnen Sie das Braze Dashboard und gehen Sie zu **Benutzer > Benutzerimport**. Hier können Sie Ihre Benutzer importieren. Wenn Sie eine CSV-Datei für den Import vorbereiten, stellen Sie sicher, dass Sie eine Sprachspalte mit den Sprachen der Benutzer einfügen. Dieses Sprachfeld wird später bei der Anzeige von Übersetzungen verwendet. 

{% alert important %}
Die verwendeten Sprachcodes müssen sowohl bei Braze als auch bei Lokalise übereinstimmen.
{% endalert %}
### Schritt 2: Vorbereitungen für Ihre Übersetzungen auf Lokalise

Um Ihre Übersetzungen auf Lokalise vorzubereiten, müssen Sie als Nächstes manuell die Übersetzungsschlüssel mit demselben Namen erstellen, den Sie auf Braze Connected Content variables verwenden. 

Lassen Sie uns zum Beispiel einen einfachen Übersetzungsschlüssel erstellen: `description`:
1. Öffnen Sie Ihr Lokalise Projekt, klicken Sie auf **Schlüssel hinzufügen** und geben Sie "Beschreibung" in das Feld **Schlüssel** ein.
2. Geben Sie "Demo-Beschreibung" in das Feld **Basis-Sprachwert** ein.
3. Fügen Sie "Web" in der Dropdown-Liste " **Plattformen** " hinzu. 
4. Wenn Sie fertig sind, klicken Sie auf **Speichern**.

![][1]{: style="max-width:60%"}

Ihr Übersetzungsschlüssel sollte im Projekteditor erscheinen:

![][2]{: style="max-width:90%"}

#### Bekannte Probleme

- Ihre Schlüssel müssen der **Webplattform** zugewiesen werden.
- Vermeiden Sie die Verwendung von Schlüsseln, die Punkte (`.`) oder die Zeichenfolge `_on` enthalten. Verwenden Sie beispielsweise `this_is_the_key` anstelle von `this.is.the.key` und `join_us_instagram` anstelle von `join_us_on_instagram`.

### Schritt 3: Konfigurieren der Braze-App auf der Lokalise

Öffnen Sie Ihr Lokalise-Projekt und klicken Sie auf **Apps**. Suchen und installieren Sie hier die Braze-App. Sie sehen dann den folgenden Bildschirm:

![Braze-Konfiguration auf Lokalise mit Angabe der Projekt-ID und der URL der Übersetzungsdateien.][3]

In der **URL der Übersetzungsdatei** veröffentlicht Lokalise eine JSON-Datei mit allen Übersetzungen für Ihre Schlüssel im Projekt. Sie erhalten so viele URLs von Übersetzungsdateien, wie Sie Zielsprachen in Ihrem Projekt haben. Aus diesem Grund bestehen die URLs der Übersetzungsdateien aus zwei Teilen:

1. Der erste Teil des URL-Pfads ist für alle Sprachen gleich.
2. Der JSON-Dateiname am Ende der URL basiert auf dem Sprachcode.

Die URL der Übersetzungsdatei ist die URL, die Sie benötigen, wenn Sie eine Braze-Kampagne konfigurieren. Sie können den Inhalt der JSON-Datei aktualisieren, indem Sie auf **Aktualisieren** klicken. Beachten Sie, dass die URL die gleiche bleibt und Sie Ihren Aufruf von Connected Content in Braze nicht ändern müssen.

### Test-URL

Um diese URL zu testen, kopieren Sie sie und ersetzen {% raw %}`{{${language}}}`{% endraw %} durch einen Sprachcode (z.B. `en`) und öffnen diese URL in Ihrem Browser. Sie werden eine JSON-Datei mit Ihren Schlüsseln und Übersetzungen sehen:

![][4]

### Schritt 4: Übersetzungen in der Braze-Kampagne verwenden

#### Aufruf Verbundene Inhalte einfügen

Wenn Sie fertig sind, kehren Sie zu Braze zurück und öffnen eine bestehende Kampagne oder erstellen eine neue. Für dieses Beispiel erstellen wir eine neue E-Mail-Kampagne mit Beispielinhalten. Klicken Sie auf **E-Mail-Text bearbeiten**.

Um Ihre Übersetzungen einzufügen, müssen Sie die Anfrage Connected Content in den HTML-Code einfügen, entweder am Anfang des Dokuments oder direkt vor der ersten Stelle, an der eine Übersetzung benötigt wird. Dies kann durch Einfügen der folgenden Markierung geschehen:

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

Ersetzen Sie die URL `https://exports.live.lokalise.cloud/...` durch die URL der Übersetzungsdatei, die Sie im vorherigen Schritt abgerufen haben.

{% raw %}

- `{{${language}}}` bedeutet "Benutzersprache an dieser Stelle einfügen". Alternativ können Sie Ihren Sprachcode auch fest codieren, zum Beispiel `en.json`.
  - Um sicherzustellen, dass für jeden Benutzer die passende übersetzte JSON-Datei abgerufen wird, müssen Sie entweder das Profilattribut `{{${language}}}` oder ein ähnliches benutzerdefiniertes Attribut, das die Sprache des Benutzers enthält, an das Ende der URL der Übersetzungsdateien setzen. (z.B. `/{{${language}}}.json`) Die in diesen Attributen enthaltenen Werte müssen mit dem Präfix jeder der übersetzten JSON-Dateien übereinstimmen. Dadurch wird sichergestellt, dass für jeden Benutzer die richtige Übersetzungsdatei zurückgegeben wird.
- `:save translations` speichert den JSON-Inhalt unter der Variablen translations.

#### Übersetzungen anzeigen

Verwenden Sie nun die Variable Übersetzungen, um die gewünschten Übersetzungen nach ihren Schlüsseln anzuzeigen.

Um zum Beispiel die Taste `description` anzuzeigen, verwenden Sie`{{ translations.description }}`.

{% endraw %}
![][6]

Zum Schluss speichern Sie die E-Mail-Vorlage und zeigen sie in der Vorschau an. Sie sollten sehen, dass Ihre Übersetzung angezeigt wird.

## Häufig gestellte Fragen

**Was passiert, wenn ich versehentlich einen Schlüssel aus Lokalise lösche?**<br>
Die entsprechende Zeichenkette auf Braze hat keine Übersetzung mehr.

**Wenn ich ein `en` Gebietsschema habe, es aber auf Lokalise mit `en-US` überschreibe, wird Braze es dann als `en-US` lesen?**<br>
Nein, die ISO-Codes der Länder müssen auf Braze und Lokalise übereinstimmen.

**Können wir die Flagge `:rerender` verwenden, wenn wir Lokalise-Inhalte verbinden?**<br>
Ja, sicher. Sie können die Braze-Dokumente konsultieren, um zu erfahren, wie Sie dieses Flag hinzufügen können.

**Warum sehe ich nach dem Aktualisieren der Übersetzungsdatei auf Lokalise keine Änderungen in den übersetzten Inhalten auf Braze?**<br>
Braze speichert übersetzte Inhalte im Cache. Die Aktualisierung kann einige Minuten dauern. Wenn Sie Ihre Kampagnen testen und die Ergebnisse der Übersetzungen sofort sehen möchten, können Sie den Parameter `:cache_max_age` verwenden, wie in diesem Referenzartikel beschrieben.

[1]: {% image_buster /assets/img/lokalise/1_add_key.png %}
[2]: {% image_buster /assets/img/lokalise/2_translation_key_added.png %}
[3]: {% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %}
[4]: {% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %}
[5]: {% image_buster /assets/img/lokalise/5_edit_email.png %}
[6]: {% image_buster /assets/img/lokalise/6_integration_usage_sample.png %}