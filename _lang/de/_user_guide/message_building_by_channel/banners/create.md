---
nav_title: Ein Banner erstellen
article_title: Ein Banner erstellen
page_order: 1
description: "Dieser referenzierte Artikel beschreibt, wie Sie mit Kampagnen und Canvase von Braze Banner erstellen, zusammenstellen, konfigurieren und versenden."
tool:
  - Campaigns
channel:
  - banners
---

# Ein Banner erstellen

> Lernen Sie, wie Sie Banner erstellen, wenn Sie Kampagnen und Canvase in Braze erstellen. Weitere allgemeine Informationen finden Sie unter [Über Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

{% alert important %}
Das Erstellen einer Nachricht in Canvas als Banner ist noch im Anfangsstadium. Wenden Sie sich an Ihren Customer Success Manager, wenn Sie an einem Vorabzugang interessiert sind.
{% endalert %}

## Voraussetzungen

Bevor Sie Ihr Banner starten können, muss Ihr Entwickler:in-Team [die Platzierungen in Ihrer App oder Website einrichten]({{site.baseurl}}/developer_guide/banners/creating_placements/). Sie können Ihre Bannerkampagne in der Zwischenzeit immer noch entwerfen, aber Sie können die Kampagne erst starten, wenn die Platzierungen konfiguriert sind.

## Erstellen Sie eine Banner Nachricht

{% multi_lang_include banners/creating_placements.md section="user" %}

### Schritt 2: Wählen Sie, wo Sie Ihre Botschaft aufbauen möchten

Sie sind sich nicht sicher, ob Ihre Nachricht über eine Kampagne oder ein Canvas versendet werden soll? Kampagnen eignen sich besser für einzelne, gezielte Messaging-Kampagnen, während Canvase besser für mehrstufige Nutzer:innen geeignet sind.

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**.
2. **Banner** auswählen.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu. Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen. Wenn Sie zum Beispiel den Berichts-Builder verwenden, können Sie nach den entsprechenden Tags filtern.
5. Wählen Sie die Platzierung aus, die Sie zuvor erstellt haben, um sie mit Ihrer Kampagne zu verknüpfen.
6. Fügen Sie bei Bedarf Varianten hinzu. Sie können für jede Nachricht einen anderen Nachrichtentyp und ein anderes Layout wählen. Weitere Informationen zu Varianten finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).
7. Wählen Sie ein Startdatum und eine Startzeit für Ihre Banner Kampagne. Standardmäßig sind Banner unbegrenzt haltbar. Sie können dies ändern, indem Sie **Endzeit** auswählen und ein Enddatum und eine Endzeit angeben.

{% alert tip %}
Wenn alle Nachrichten in Ihrer Kampagne ähnlich sind oder den gleichen Inhalt haben, sollten Sie Ihre Nachricht verfassen, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann aus dem Dropdown-Menü **Variante hinzufügen** die Option **Aus Variante kopieren** auswählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) mit dem Canvas Composer.
2. Nachdem Sie Ihr Canvas eingerichtet haben, fügen Sie einen Nachrichtenschritt in den Canvas-Builder ein. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie **Banner** als Ihren Messaging-Kanal aus.
4. Wählen Sie eine Platzierung für das Banner aus.
5. Legen Sie die Priorität für das Banner fest. Die [Bannerpriorität]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) bestimmt die Reihenfolge, in der die Banner angezeigt werden, wenn sie dieselbe Platzierung haben.
6. Legen Sie ein Verfallsdatum für das Banner fest. Dies kann nach einer bestimmten Zeit geschehen, nachdem der Schritt verfügbar ist, oder zu einem bestimmten Datum und einer bestimmten Uhrzeit.

{% endtab %}
{% endtabs %}

### Schritt 3: Ein Banner zusammenstellen {#compose-a-banner}

Um Ihr Banner zu verfassen, können Sie Folgendes wählen:

- Beginnen Sie mit einem leeren Template
- Verwenden Sie eine Braze-Banner-Vorlage
- Eine gespeicherte Banner-Vorlage auswählen

![Sie haben die Möglichkeit, ein leeres Banner oder ein Template zu wählen.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Schritt 3.1: Gestalten Sie das Banner

Sie können Blöcke und Zeilen per Drag-and-Drop in den Canvas-Bereich ziehen, um mit der Erstellung Ihrer Nachricht zu beginnen.

Um die Eigenschaften des Hintergrunds Ihrer Nachricht, die Einstellungen für den Rahmen und mehr anzupassen, wählen Sie **Stile**. Wenn Sie nur den Stil für einen bestimmten Block oder eine bestimmte Zeile anpassen möchten, wählen Sie ihn aus, um Änderungen vorzunehmen.

![Style Panel des Banner Composers.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Schritt 3.2: Definieren Sie das Verhalten bei einem Klick (optional)

Wenn ein Nutzer:innen auf einen Link im Banner klickt, haben Sie die Wahl, ihn tiefer in Ihre App zu navigieren oder ihn auf eine andere Webseite umzuleiten. Zusätzlich können Sie [ein angepasstes Attribut oder Ereignis protokollieren]({{site.baseurl}}/developer_guide/analytics/), das das Profil Ihres Nutzers:in mit angepassten Daten aktualisiert, wenn er auf das Banner klickt.

{% alert important %}
{::nomarkdown}
Das Klickverhalten kann außer Kraft gesetzt werden, wenn ein bestimmtes Element (z.B. ein Button, ein Link oder ein Bild des Banners) sein eigenes Klickverhalten hat. Nehmen wir zum Beispiel das folgende Verhalten beim Klicken an:<br><ul><li>Ein Banner hat ein On-Click-Verhalten, das auf die Homepage einer Website umleitet.</li><li>Ein Bild im Banner hat ein On-Click-Verhalten, das auf die Produktseite einer Website weiterleitet.</li></ul>Wenn ein Nutzer:innen auf das Bild klickt, wird er auf die Seite mit dem Produkt weitergeleitet. Wenn Sie jedoch auf den umliegenden Bereich im Banner klicken, werden Sie auf die Homepage weitergeleitet.
{:/}
{% endalert %}

#### Schritt 3.3: Angepasste Eigenschaften hinzufügen (optional) {#custom-properties}

Sie können einem Banner angepasste Eigenschaften hinzufügen, um strukturierte Metadaten, wie Strings oder JSON-Objekte, anzuhängen. Diese Eigenschaften haben keinen Einfluss auf die Anzeige des Banners, können aber [über das Braze SDK aufgerufen]({{site.baseurl}}/developer_guide/banners/placements/) werden, um das Verhalten oder Aussehen Ihrer App zu ändern. Sie könnten zum Beispiel:

- Senden Sie Metadaten für Ihre Analytics oder Integrationen von Drittanbietern.
- Verwenden Sie Metadaten wie z.B. ein `timestamp` oder JSON-Objekt, um bedingte Logik zu triggern.
- Steuern Sie das Verhalten eines Banners anhand der enthaltenen Metadaten wie `ratio` oder `format`.

Um eine angepasste Eigenschaft hinzuzufügen, wählen Sie **Einstellungen** > **Eigenschaften** > **Eigenschaft hinzufügen**.

![Die Eigenschaftsseite mit der Möglichkeit, die erste angepasste Eigenschaft zu einer Banner-Kampagne hinzuzufügen.]({% image_buster /assets/img/banners/add_property.png %})

Füllen Sie für jede Eigenschaft, die Sie hinzufügen möchten, die folgenden Felder aus:

| Feld | Beschreibung | Beispiel |
|-------|-------------|---------|
| Eigenschaftstyp | Der Datentyp für die Eigenschaft. Unterstützt werden die Typen String, Boolean, Zahl, Zeitstempel, Bild-URL und JSON-Objekt. | String |
| Eigenschaftsschlüssel | Der eindeutige Bezeichner für die Eigenschaft. Dieser Schlüssel wird im SDK für den Zugriff auf die Eigenschaft verwendet. | `color` |
| Wert | Der Wert, der der Eigenschaft zugewiesen wurde. Muss mit dem ausgewählten Eigenschaftstyp übereinstimmen. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Wenn Sie fertig sind, wählen Sie **Fertig**.

![Die Eigenschaftsseite mit einer String-Eigenschaft mit dem Schlüssel color und dem Wert #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### Schritt 4: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas

{% tabs %}
{% tab Campaign %}

#### Banner-Priorität festlegen (optional)

Die [Bannerpriorität]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) bestimmt die Reihenfolge, in der die Banner angezeigt werden, wenn sie dieselbe Platzierung haben. Um die Priorität manuell einzustellen:

1. Wählen Sie **Exakte Priorität festlegen**.
2. Ziehen Sie die Kampagnen per Drag-and-Drop, um sie nach der richtigen Priorität zu ordnen.
3. Wählen Sie **Sortierung anwenden**.

{% alert tip %}
Wenn Sie mehrere Bannerkampagnen haben, die dieselbe ID verwenden, empfehlen wir Ihnen, die Prioritäten per Drag-and-Drop zu sortieren, um die genaue Priorität festzulegen.
{% endalert %}

#### Wählen Sie Ihre Zielgruppe

1. In **Zielgruppen** wählen Sie Segmente oder Filter, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Vorschau auf die ungefähre Größe der Segmente. Die genaue Segmentierung wird vor dem Versand der Nachricht berechnet.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2\. In **Conversions zuordnen** verfolgen Sie, wie oft Nutzer:innen nach dem Erhalt einer Kampagne bestimmte Aktionen durchführen, indem Sie Konversions-Events mit einem Zeitfenster von bis zu 30 Tagen definieren, um die Aktion als Konversion zu zählen.

{% multi_lang_include target_audiences.md %}

#### Wählen Sie Konversions-Events aus

Braze erlaubt Ihnen das Tracking von [Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), d.h. wie oft Nutzer:innen bestimmte Aktionen ausführen, nachdem sie eine Kampagne erhalten haben. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen zuzulassen, in dem eine Konversion gezählt wird, wenn der Nutzer:innen die angegebene Aktion durchführt.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, füllen Sie die restlichen Abschnitte der Canvas-Komponente aus. Weitere Einzelheiten zum Aufbau des restlichen Canvas, zur Implementierung von [multivariaten Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) und [intelligenter Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) und mehr finden Sie im Schritt [Aufbau Ihres Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) in unserer Canvas-Dokumentation.

{% endtab %}
{% endtabs %}

### Schritt 5: Testen Sie Ihre Nachricht (optional)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Schritt 6: Überprüfen und einsetzen

Nachdem Sie die Erstellung Ihrer Kampagne oder Ihres Canvas abgeschlossen haben, überprüfen Sie die Details, [testen Sie sie]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) und senden Sie sie, wenn Sie bereit sind.
