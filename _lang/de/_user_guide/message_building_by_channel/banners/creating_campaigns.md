---
nav_title: Kampagnen erstellen
article_title: Erstellen von Bannerkampagnen in Braze
page_order: 1
description: "Dieser referenzierte Artikel beschreibt, wie Sie mit Kampagnen von Braze Banner erstellen, zusammenstellen, konfigurieren und versenden."
tool:
  - Campaigns
channel:
  - banners
---

# Erstellen von Banner-Kampagnen

> Lernen Sie, wie Sie Banner erstellen, wenn Sie eine Kampagne in Braze erstellen. Weitere allgemeine Informationen finden Sie unter [Über Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

## Voraussetzungen

Bevor Sie Ihre Kampagne einführen können, muss Ihr Entwickler: [in Ihre App oder Website einbinden]({{site.baseurl}}/developer_guide/banners/creating_placements/). Sie können Ihre Bannerkampagne in der Zwischenzeit immer noch entwerfen - Sie können die Kampagne dann nur nicht mehr starten.

## Erstellen einer Banner-Kampagne

{% multi_lang_include banners/creating_placements.md section="user" %}

### Schritt 2: Eine Kampagne erstellen

1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**.
2. **Banner** auswählen.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie Teams und Tags nach Bedarf hinzu. Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen. Wenn Sie zum Beispiel den Berichts-Builder verwenden, können Sie nach den entsprechenden Tags filtern.
5. Wählen Sie die Platzierung aus, die Sie zuvor erstellt haben, um sie mit Ihrer Kampagne zu verknüpfen.
6. Fügen Sie bei Bedarf Varianten hinzu. Sie können für jede Nachricht einen anderen Nachrichtentyp und ein anderes Layout wählen. Weitere Informationen zu Varianten finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).

### Schritt 3: Ein Banner zusammenstellen {#compose-a-banner}

Um Ihr Banner zu verfassen, können Sie Folgendes wählen:

- Beginnen Sie mit einem leeren Template
- Verwenden Sie eine Braze-Banner-Vorlage
- Eine gespeicherte Banner-Vorlage auswählen

![Option zur Auswahl eines leeren Banners oder eines Templates.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Schritt 3.1: Gestalten Sie das Banner

Sie können Blöcke und Zeilen per Drag-and-Drop in den Canvas-Bereich ziehen, um mit der Erstellung Ihrer Nachricht zu beginnen.

Um die Eigenschaften des Hintergrunds Ihrer Nachricht, die Einstellungen für den Rahmen und mehr anzupassen, wählen Sie **Stile**. Wenn Sie nur den Stil für einen bestimmten Block oder eine bestimmte Zeile anpassen möchten, wählen Sie ihn aus, um Änderungen vorzunehmen.

![Style Panel des Banner Composers.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Schritt 3.2: Definieren Sie das Verhalten bei einem Klick (optional)

Wenn ein Nutzer:innen auf einen Link im Banner klickt, haben Sie die Wahl, ihn tiefer in Ihre App zu navigieren oder ihn auf eine andere Webseite umzuleiten. Darüber hinaus können Sie [ein angepasstes Attribut oder Ereignis protokollieren]({{site.baseurl}}/developer_guide/analytics/), wodurch das Profil Ihres Nutzers:in beim Klick auf das Banner mit den angepassten Daten aktualisiert wird.

{% alert important %}
{::nomarkdown}
Das Klickverhalten kann außer Kraft gesetzt werden, wenn ein bestimmtes Element (z.B. ein Button, ein Link oder ein Bild des Banners) sein eigenes Klickverhalten hat. Nehmen wir zum Beispiel das folgende Verhalten beim Klicken an:<br><ul><li>Ein Banner hat ein On-Click-Verhalten, das auf die Homepage einer Website umleitet.</li><li>Ein Bild im Banner hat ein On-Click-Verhalten, das auf die Produktseite einer Website weiterleitet.</li></ul>Wenn ein Nutzer:innen auf das Bild klickt, wird er auf die Seite des Produkts weitergeleitet. Wenn Sie jedoch auf den umliegenden Bereich im Banner klicken, werden Sie auf die Homepage weitergeleitet.
{:/}
{% endalert %}

#### Schritt 3.3: Angepasste Eigenschaften hinzufügen (optional) {#custom-properties}

Sie können einem Banner angepasste Eigenschaften hinzufügen, um strukturierte Metadaten, wie Strings oder JSON-Objekte, anzuhängen. Diese Eigenschaften haben keinen Einfluss auf die Anzeige des Banners, können aber [über das Braze SDK aufgerufen]({{site.baseurl}}/developer_guide/banners/placements/) werden, um das Verhalten oder Aussehen Ihrer App zu ändern. Sie könnten zum Beispiel:

- Senden Sie Metadaten für Ihre Analytics oder Integrationen von Drittanbietern.
- Verwenden Sie Metadaten wie z.B. ein `timestamp` oder JSON-Objekt, um bedingte Logik zu triggern.
- Steuern Sie das Verhalten eines Banners anhand der enthaltenen Metadaten wie `ratio` oder `format`.

Um eine angepasste Eigenschaft hinzuzufügen, wählen Sie **Einstellungen** > **Eigenschaften** > **Eigenschaft hinzufügen**.

![Die Eigenschaftsseite mit der Option, die erste angepasste Eigenschaft zu einer Banner Kampagne hinzuzufügen.]({% image_buster /assets/img/banners/add_property.png %})

Füllen Sie für jede Eigenschaft, die Sie hinzufügen möchten, die folgenden Felder aus:

| Feld | Beschreibung | Beispiel |
|-------|-------------|---------|
| Eigenschaftstyp | Der Datentyp für die Eigenschaft. Unterstützt werden die Typen String, Boolean, Zahl, Zeitstempel, Bild-URL und JSON-Objekt. | String |
| Eigenschaftsschlüssel | Der eindeutige Bezeichner für die Eigenschaft. Dieser Schlüssel wird im SDK für den Zugriff auf die Eigenschaft verwendet. | `color` |
| Wert | Der Wert, der der Eigenschaft zugewiesen wurde. Muss mit dem ausgewählten Eigenschaftstyp übereinstimmen. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Wenn Sie fertig sind, wählen Sie **Fertig**.

![Die Eigenschaftsseite mit einer String-Eigenschaft mit einem Schlüssel von color und einem Wert von #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### Schritt 4: Dauer der Kampagne festlegen

Wählen Sie ein Startdatum und eine Startzeit für Ihre Banner Kampagne. Standardmäßig sind Banner unbegrenzt haltbar. Sie können dies ändern, indem Sie **Endzeit** auswählen und ein Enddatum und eine Endzeit angeben.

### Schritt 5: Banner-Priorität festlegen (optional)

Die [Bannerpriorität]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) bestimmt die Reihenfolge, in der die Banner angezeigt werden, wenn sie dieselbe Platzierung haben. Um die Priorität manuell einzustellen:

1. Wählen Sie **Exakte Priorität festlegen**.
2. Ziehen Sie die Kampagnen per Drag-and-Drop, um sie nach der richtigen Priorität zu ordnen.
3. Wählen Sie **Sortierung anwenden**.

{% alert tip %}
Wenn Sie mehrere Bannerkampagnen haben, die dieselbe ID verwenden, empfehlen wir Ihnen, die Prioritäten per Drag-and-Drop zu sortieren, um die genaue Priorität festzulegen.
{% endalert %}

### Schritt 6: Testen Sie Ihre Nachricht (optional)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Schritt 7: Beenden Sie die Erstellung der Kampagne

Beenden Sie den Aufbau Ihrer Kampagne, indem Sie die folgenden Aufgaben erledigen:

1. In **Zielgruppen** wählen Sie Segmente oder Filter, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Vorschau auf die ungefähre Größe der Segmente. Die genaue Segmentierung wird kurz vor dem Versand der Nachricht berechnet.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2\. In **Conversions zuordnen** verfolgen Sie, wie oft Nutzer:innen nach dem Erhalt einer Kampagne bestimmte Aktionen durchführen, indem Sie Konversions-Events mit einem Zeitfenster von bis zu 30 Tagen definieren, um die Aktion als Konversion zu zählen.

### Schritt 8: Starten Sie Ihre Kampagne

Nachdem Sie Ihre Bannerkampagne erstellt und getestet haben, können Sie sie starten!
