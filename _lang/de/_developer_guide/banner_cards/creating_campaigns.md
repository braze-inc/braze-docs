---
nav_title: Kampagnen erstellen
article_title: Erstellen von Banner Card Kampagnen
alias: "/create_banner_card/"
description: "Dieser referenzierte Artikel beschreibt, wie Sie mit Kampagnen von Braze Bannerkarten erstellen und versenden können."
page_type: reference
---

# Erstellen von Banner Card Kampagnen

> Lernen Sie, wie Sie Bannerkarten erstellen, wenn Sie eine Kampagne in Braze erstellen. Weitere allgemeine Informationen finden Sie unter [Über Bannerkarten]({{site.baseurl}}/developer_guide/banners/).

{% alert important %}
Banner-Cards befinden sich derzeit in der Early Access-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Early-Access-Phase teilnehmen möchten.
{% endalert %}

## Voraussetzungen {#prerequisite-determine-placement}

Das sind die Mindestversionen des SDK, um Banner Cards zu verwenden:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Erstellen einer Banner Card Kampagne

{% multi_lang_include banners/creating_placements.md %}

### Schritt 2: Eine Kampagne erstellen

1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**.
2. Wählen Sie die **Bannerkarte** aus.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie Teams und Tags nach Bedarf hinzu. Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen. Wenn Sie zum Beispiel den Berichts-Builder verwenden, können Sie nach den entsprechenden Tags filtern.
5. Wählen Sie die Platzierung aus, die Sie zuvor erstellt haben, um sie mit Ihrer Kampagne zu verknüpfen.
6. Fügen Sie bei Bedarf Varianten hinzu. Sie können für jede Nachricht einen anderen Nachrichtentyp und ein anderes Layout wählen. Weitere Informationen zu Varianten finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

### Schritt 2: Verfassen Sie eine Nachricht

Um Ihre Bannerkarte zu verfassen, wählen Sie **Nachricht bearbeiten**. Hier können Sie die Karte gestalten und das Verhalten bei einem Klick festlegen.

#### Schritt 2.1: Gestalten Sie die Karte {#styles}

Sie können Blöcke und Zeilen per Drag-and-Drop in den Canvas-Bereich ziehen, um mit der Erstellung Ihrer Nachricht zu beginnen. Um die Eigenschaften des Hintergrunds Ihrer Nachricht, die Einstellungen für den Rahmen und mehr anzupassen, wählen Sie **Stile**. Wenn Sie nur den Stil für einen bestimmten Block oder eine bestimmte Zeile anpassen möchten, wählen Sie ihn aus, um Änderungen vorzunehmen.

![Style Panel des Banner Card Composers.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Schritt 2.2: Verhalten beim Klicken definieren

Wenn ein Kunde auf einen Link in der Bannerkarte klickt, haben Sie die Wahl, ihn tiefer in Ihre App zu navigieren oder ihn auf eine andere Webseite umzuleiten. Zusätzlich können Sie [ein angepasstes Attribut oder Ereignis protokollieren]({{site.baseurl}}/developer_guide/analytics/), das das Profil Ihrer Kund:in mit den angepassten Daten aktualisiert, wenn diese auf die Bannerkarte klicken.

### Schritt 3: Kartenpriorität festlegen {#set-card-priority}

Wenn mehrere Kampagnen auf dieselbe ID referenzieren, werden die Karten in der Reihenfolge ihrer Priorität angezeigt. Standardmäßig sind neu erstellte Bannerkarten auf mittel eingestellt, aber Sie können die Priorität manuell auf hoch, mittel oder niedrig setzen. Wenn mehrere Karten die gleiche Prioritätsstufe haben, wird die neueste Karte zuerst angezeigt.

So legen Sie die Kartenpriorität für eine Karte fest:

1. Wählen Sie **Prioritätssortierer** aus.
2. Ziehen Sie die Kampagnen per Drag-and-Drop, um sie nach der richtigen Priorität zu ordnen.
3. Wählen Sie **Sortierung anwenden**.

### Schritt 3: Beenden Sie die Erstellung der Kampagne

Beenden Sie den Aufbau Ihrer Kampagne, indem Sie die folgenden Aufgaben erledigen:

| Option                    | Beschreibung |
|---------------------------|-------------|
| **Kampagnendauer** | Wählen Sie ein Startdatum und eine Startzeit für Ihre Banner Card Kampagne. Standardmäßig sind die Bannerkarten unbegrenzt gültig. Sie können dies ändern, indem Sie **Endzeit** auswählen und ein Enddatum und eine Endzeit angeben. |
| **Adressierte Nutzer:innen** | Stellen Sie Nutzer:innen durch die Auswahl von Segmenten oder Filtern gezielt zusammen, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Momentaufnahme der ungefähren Segmente. Die genaue Segmentierung wird kurz vor dem Versand der Nachricht berechnet. |
| **Konversions-Events** | Verfolgen Sie, wie oft Nutzer:innen nach Erhalt einer Kampagne bestimmte Aktionen ausführen. Sie können Konversions-Events mit einem Zeitfenster von bis zu 30 Tagen definieren, um die Aktion als Konversion zu zählen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Schritt 4: Test und Start

Nachdem Sie Ihre Kampagne erstellt haben, testen und überprüfen Sie sie, um sicherzustellen, dass Ihre Kampagne wie erwartet funktioniert. Wenn Sie bereit sind, starten Sie Ihre Banner Card Kampagne!
