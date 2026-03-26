---
nav_title: Erstellen Sie ein Banner
article_title: Erstellen Sie ein Banner
page_order: 1
description: "Dieser Referenzartikel behandelt die Erstellung, Gestaltung, Konfiguration und den Versand von Bannern mithilfe von Braze-Kampagnen und Canvases."
tool:
  - Campaigns
channel:
  - banners
---

# Erstellen Sie ein Banner

> Erfahren Sie, wie Sie Banner erstellen, wenn Sie Kampagnen und Canvases in Braze erstellen. Weitere allgemeine Informationen finden Sie unter [Über Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

{% alert important %}
Die Erstellung einer Banner-Nachricht in Canvas befindet sich derzeit in der Early-Access-Phase. Wenden Sie sich an Ihren Customer Success Manager, wenn Sie an einem Vorabzugang interessiert sind.
{% endalert %}

## Voraussetzungen

Bevor Sie Ihr Banner starten können, muss Ihr Entwicklungsteam [Platzierungen in Ihrer App oder Website einrichten]({{site.baseurl}}/developer_guide/banners/creating_placements/). Sie können Ihre Banner-Kampagne in der Zwischenzeit weiterhin entwerfen, jedoch können Sie die Kampagne erst starten, wenn die Platzierungen konfiguriert sind.

## Erstellen Sie eine Banner-Nachricht

{% multi_lang_include banners/creating_placements.md section="user" %}

### Schritt 2: Wählen Sie, wo Sie Ihre Botschaft aufbauen möchten

Sie sind sich nicht sicher, ob Ihre Nachricht über eine Kampagne oder ein Canvas versendet werden soll? Kampagnen eignen sich besser für einzelne, zielgerichtete Messaging-Kampagnen, während Canvases besser für mehrstufige User Journeys geeignet sind.

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
3. Bitte wählen Sie **Banner** als Ihren Messaging-Kanal.
4. Bitte wählen Sie eine Position für das Banner aus.
5. Legen Sie bitte die Priorität für das Banner fest. Die [Bannerpriorität]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) bestimmt die Reihenfolge, in der die Banner angezeigt werden, wenn sie dieselbe Platzierung haben.
6. Legen Sie bitte ein Ablaufdatum für das Banner fest. Dies kann nach einer bestimmten Zeitspanne, nachdem der Schritt verfügbar ist, oder zu einem bestimmten Datum und einer bestimmten Uhrzeit erfolgen.

{% endtab %}
{% endtabs %}

### Schritt 3: Ein Banner zusammenstellen {#compose-a-banner}

Um Ihr Banner zu gestalten, haben Sie folgende Möglichkeiten:

- Beginnen Sie mit einem leeren Template.
- Verwenden Sie ein Braze-Banner-Template
- Bitte wählen Sie ein gespeichertes Banner-Template aus.

![Es besteht die Möglichkeit, zwischen einem leeren Banner und einem Template zu wählen.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Schritt 3.1: Gestalten Sie das Banner

Sie können Blöcke und Zeilen per Drag-and-Drop in den Canvas-Bereich ziehen, um mit der Erstellung Ihrer Nachricht zu beginnen.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Um die Eigenschaften des Hintergrunds Ihrer Nachricht, die Einstellungen für den Rahmen und mehr anzupassen, wählen Sie **Stile**. Wenn Sie nur den Stil für einen bestimmten Block oder eine bestimmte Zeile anpassen möchten, wählen Sie ihn aus, um Änderungen vorzunehmen.

![Stil-Panel des Banner-Composers.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Schritt 3.2: Klickverhalten definieren (optional)

Wenn ein Nutzer:innen auf einen Link im Banner klickt, haben Sie die Wahl, ihn tiefer in Ihre App zu navigieren oder ihn auf eine andere Webseite umzuleiten. Darüber hinaus haben Sie die Möglichkeit, [ein benutzerdefiniertes Attribut oder Ereignis]({{site.baseurl}}/developer_guide/analytics/) zu [protokollieren]({{site.baseurl}}/developer_guide/analytics/), wodurch das Profil Ihres Benutzers mit benutzerdefinierten Daten aktualisiert wird, wenn er auf das Banner klickt.

{% alert important %}
{::nomarkdown}
Das Klickverhalten kann außer Kraft gesetzt werden, wenn ein bestimmtes Element (z.B. ein Button, ein Link oder ein Bild des Banners) sein eigenes Klickverhalten hat. Nehmen wir zum Beispiel das folgende Verhalten beim Klicken an:<br><ul><li>Ein Banner hat ein On-Click-Verhalten, das auf die Homepage einer Website umleitet.</li><li>Ein Bild im Banner hat ein On-Click-Verhalten, das auf die Produktseite einer Website weiterleitet.</li></ul>Wenn eine Nutzer:in auf das Bild klickt, wird sie zur Seite des Produkts weitergeleitet. Wenn man jedoch einen Klick auf den Bereich um das Banner herum macht, wird man zur Startseite weitergeleitet.
{:/}
{% endalert %}

#### Schritt 3.3: Benutzerdefinierte Eigenschaften hinzufügen (optional) {#custom-properties}

Sie können einem Banner angepasste Eigenschaften hinzufügen, um strukturierte Metadaten wie Strings oder JSON-Objekte anzuhängen. Diese Eigenschaften haben keinen Einfluss auf die Darstellung des Banners, können jedoch [über das Braze SDK abgerufen]({{site.baseurl}}/developer_guide/banners/placements/) werden, um das Verhalten oder das Erscheinungsbild Ihrer App anzupassen. Beispielsweise könnten Sie:

- Bitte senden Sie Metadaten für Ihre Analytics oder Integrationen von Drittanbietern.
- Verwenden Sie Metadaten wie ein `timestamp`JSON-Objekt, um bedingte Logik zu triggern.
- Steuern Sie das Verhalten eines Banners basierend auf enthaltenen Metadaten wie`ratio`oder`format`.

Um eine angepasste Eigenschaft hinzuzufügen, wählen Sie **bitte Einstellungen** > **Eigenschaften** > **Eigenschaft hinzufügen**.

![Die Eigenschaftenseite, auf der die Option zum Hinzufügen der ersten angepassten Eigenschaft zu einer Banner-Kampagne angezeigt wird.]({% image_buster /assets/img/banners/add_property.png %})

Bitte füllen Sie für jede Eigenschaft, die Sie hinzufügen möchten, die folgenden Angaben aus:

| Feld | Beschreibung | Beispiel |
|-------|-------------|---------|
| Eigenschaftstyp | Der Datentyp für die Eigenschaft. Unterstützte Typen umfassen Strings, Boolesche Werte, Zahlen, Zeitstempel, Bild-URLs und JSON-Objekte. | String |
| Eigenschaftsschlüssel | Der eindeutige Bezeichner für die Immobilie. Dieser Schlüssel wird im SDK verwendet, um auf die Eigenschaft zuzugreifen. | `color` |
| Wert | Die Wertzuweisung für die Eigenschaft. Muss mit der ausgewählten Eigenschaft übereinstimmen. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Wenn Sie fertig sind, wählen Sie **Fertig**.

![Die Eigenschaftenseite mit einer String-Eigenschaft mit dem Schlüssel „Farbe“ und dem String-Wert „#FF0000.]({% image_buster /assets/img/banners/example_property.png %})

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

#### Bitte wählen Sie Ihre Zielgruppe aus.

1. Wählen Sie unter **„Zielgruppen“** Segmente oder Filter aus, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Vorschau der ungefähren Segmentpopulation. Die genaue Segmentzugehörigkeit wird vor dem Versand der Nachricht berechnet.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2\. Verfolgen Sie in **„Assign Conversions“** (**Konversionen** zuweisen), wie oft Nutzer:innen bestimmte Aktionen ausführen, nachdem sie eine Kampagne erhalten haben, indem Sie Konversions-Events mit einem Zeitfenster von bis zu 30 Tagen definieren, um die Aktion als Konversion zu zählen.

{% multi_lang_include target_audiences.md %}

#### Wählen Sie Konversions-Events aus

Mit Braze können Sie [Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) nachverfolgen, d. h. wie oft Nutzer:innen bestimmte Aktionen ausführen, nachdem sie eine Kampagne erhalten haben. Es ist zulässig, einen Zeitraum von bis zu 30 Tagen festzulegen, in dem eine Konversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, füllen Sie die restlichen Abschnitte der Canvas-Komponente aus. Weitere Einzelheiten zum Aufbau des restlichen Canvas, zur Implementierung von [multivariaten Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) und [intelligenter Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) und mehr finden Sie im Schritt [Aufbau Ihres Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) in unserer Canvas-Dokumentation.

{% endtab %}
{% endtabs %}

### Schritt 5: Testen Sie Ihre Nachricht (optional)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Schritt 6: Überprüfen und einsetzen

Nachdem Sie Ihre Kampagne oder Ihr Canvas fertiggestellt haben, überprüfen Sie bitte die Details, [testen Sie es]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) und versenden Sie es, sobald Sie bereit sind.
