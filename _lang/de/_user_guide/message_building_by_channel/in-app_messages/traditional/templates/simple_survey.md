---
nav_title: "Einfache Umfrage"
article_title: Einfache Umfrage In-App-Nachricht
page_order: 1.5
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie mit Hilfe der Umfragen für In-App-Nachrichten Benutzerattribute, Erkenntnisse und Vorlieben sammeln, um Ihre Kampagnenstrategie zu unterstützen."
channel:
  - in-app messages
tool:
  - Templates
---

# Einfache Umfrage

> Verwenden Sie die In-App-Nachrichtenvorlage **Simple Survey**, um Benutzerattribute, Erkenntnisse und Vorlieben zu sammeln, die Ihre Kampagnenstrategie unterstützen. 

Fragen Sie die Nutzer zum Beispiel, wie sie Ihre App verwenden möchten, erfahren Sie mehr über ihre persönlichen Vorlieben oder fragen Sie sie nach ihrer Zufriedenheit mit einer bestimmten Funktion.

![Drei einfache Nachrichten für Umfragen: Benachrichtigungspräferenzen, Ernährungspräferenzen und eine Umfrage zur Kundenzufriedenheit. Die ausgewählten Optionen in den Umfragen entsprechen den benutzerdefinierten Attributen, die für diesen Benutzer protokolliert werden.]({% image_buster /assets/img/iam/iam-survey.png %})

## SDK-Anforderungen {#supported-sdk-versions}

Diese In-App-Nachricht wird nur an Geräte ausgeliefert, die [Flex CSS](https://caniuse.com/flexbox) unterstützen und mindestens die folgenden [SDK-Versionen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) haben müssen. 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Um In-App-Nachrichten im HTML-Format über das Internet SDK zu aktivieren, müssen Sie Braze die Initialisierungsoption `allowUserSuppliedJavascript` zur Verfügung stellen.
{% endalert %}

## Eine Umfrage erstellen {#create}

Wenn Sie eine [In-App-Nachricht][1] erstellen, wählen Sie **Einfache Umfrage** als **Nachrichtentyp**.

![]({% image_buster /assets/img/iam/survey-message-type.png %}){: style="max-width:80%"}

Diese Umfragevorlage wird sowohl für mobile Apps als auch für Webbrowser unterstützt. Vergewissern Sie sich, dass Ihre SDKs über die für dieses Feature erforderlichen [Mindestversionen](#supported-sdk-versions) verfügen.

### Schritt 1: Ihre Umfragefrage hinzufügen

Um mit der Erstellung Ihrer Umfrage zu beginnen, fügen Sie Ihre Frage in das Feld **Überschrift der** Umfrage ein. Falls gewünscht, können Sie eine optionale **Nachricht** hinzufügen, die unter der Frage Ihrer Umfrage erscheint.

![Tab des einfachen Umfragen-Editors mit Feldern für eine Überschrift, einen optionalen Hauptteil und einen optionalen Hilfstext.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:80%"}

{% alert tip %}
Diese Felder können sowohl Liquid als auch Emojis enthalten, also lassen Sie sich etwas einfallen!
{% endalert %}

### Schritt 2: Wählen Sie zwischen Single- und Multiple-Choice-Verfahren {#single-multiple-choice}

Verwenden Sie **Einzelauswahl** oder **Mehrfachauswahl**, um festzulegen, ob ein Benutzer nur eine Auswahl oder mehrere Auswahlmöglichkeiten auswählen kann. Sie können bis zu 12 Auswahlmöglichkeiten in einer Umfrage hinzufügen.

![Dropdown-Auswahlmöglichkeiten mit ausgewählter "Multiple-Choice-Auswahl".]({% image_buster /assets/img/iam/single-multiple-choice.png %}){: style="max-width:60%"}

{% alert tip %}
Ihr **Hilfstext** wird automatisch aktualisiert, wenn Sie zwischen **Einzelauswahl** und **Mehrfachauswahl** wechseln, um den Benutzern mitzuteilen, wie viele Auswahlmöglichkeiten sie haben.
{% endalert %}

### Schritt 3: Angepasste Attribute sammeln {#custom-attributes}

Wählen Sie **Attribute bei der Einreichung protokollieren** auswählen, um Attribute basierend auf der Übermittlung der Nutzerin oder des Nutzers zu sammeln. Mit dieser Option können Sie neue Segmente und Retargeting Kampagnen erstellen. Bei einer Zufriedenheitsumfrage könnten Sie zum Beispiel eine Folge-E-Mail an alle Nutzer senden, die nicht zufrieden waren.

![Wählen Sie das Dropdown-Menü mit der Auswahl "Attribute bei der Einreichung protokollieren".]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

Um jeder Auswahl ein benutzerdefiniertes Attribut hinzuzufügen, wählen Sie den Namen eines benutzerdefinierten Attributs aus dem Dropdown-Menü (oder erstellen Sie ein neues) und geben Sie dann den Wert ein, der bei der Übermittlung dieser Auswahl gesetzt werden soll. Sie können ein neues benutzerdefiniertes Attribut auf Ihrer [Einstellungsseite][5] erstellen.

In einer Umfrage zu den Benachrichtigungspräferenzen könnten Sie zum Beispiel jede Auswahl mit einem booleschen (wahr/falsch) Attribut versehen, damit die Benutzer auswählen können, welche Themen sie interessieren. Wenn ein Benutzer die Option "Sonderangebote" ankreuzt, wird sein [Benutzerprofil][3] aktualisiert und das benutzerdefinierte Attribut `Promotions Topic` auf `true` gesetzt. Wenn Sie die Option nicht markieren, bleibt dasselbe Attribut unverändert.

![]({% image_buster /assets/img/iam/iam-survey3.png %}){: style="max-width:60%"}

Sie können dann mit `Promotions Topic = true` ein Segment für Nutzer:innen erstellen, um sicherzustellen, dass nur Nutzer:innen, die an Ihren Aktionen interessiert sind, die entsprechenden Kampagnen erhalten.

{% alert important %}
Wenn die Sammlung von benutzerdefinierten Attributen aktiviert ist, werden Auswahlmöglichkeiten, die denselben benutzerdefinierten Attributnamen haben, in einem Array zusammengefasst.
{% endalert %}

#### Benutzerdefinierte Attribut-Datentypen

Der Datentyp Ihrer benutzerdefinierten Attribute hängt davon ab, wie Sie Ihre Umfrage eingerichtet haben.

- **Auswahl im Multiple-Choice-Verfahren:** Der Datentyp des benutzerdefinierten Attributs muss ein Array sein. Wenn das angepasste Attribut auf einen anderen Datentyp eingestellt ist, werden die Antworten nicht protokolliert.
- **Einzelne Auswahlmöglichkeiten:** Der Datentyp des angepassten Attributs _darf kein_ Array sein. Die Antworten werden nicht protokolliert, wenn das Attribut ein Array ist.

#### Nur Antworten protokollieren

Alternativ können Sie auch **nur die Antworten protokollieren (ohne Attribute)**. Wenn diese Option ausgewählt ist, werden Umfragebeantwortungen als Schaltflächenklicks protokolliert, aber benutzerdefinierte Attribute werden nicht im Profil eines Benutzers gespeichert. Das bedeutet, dass Sie weiterhin die Klick-Metriken für jede Umfrageoption sehen können (siehe [Analytics](#analytics)), aber diese Auswahl wird nicht in ihrem Benutzerprofil angezeigt.

Diese Klick-Metriken sind für Retargeting nicht verfügbar.

### Schritt 4: Einreichungsverhalten wählen

Sobald ein Benutzer seine Antwort abgeschickt hat, können Sie optional eine Bestätigungsseite anzeigen oder die Nachricht einfach schließen.

Eine Bestätigungsseite ist ein guter Ort, um sich bei den Nutzern für ihre Zeit zu bedanken oder zusätzliche Informationen bereitzustellen. Sie können den Aktionsaufruf auf dieser Seite anpassen, um den Benutzer auf eine andere Seite Ihrer App oder Website zu leiten.

Bearbeiten Sie den Text der Schaltfläche und das On-Click-Verhalten im Abschnitt **Schaltfläche einreichen** unten auf der Registerkarte **Umfrage**:

![On-Click-Verhalten auf "Antworten einreichen und Bestätigungsseite anzeigen" eingestellt.]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Wenn Sie eine Bestätigungsseite hinzufügen möchten, wechseln Sie zur Registerkarte **Bestätigungsseite**, um Ihre Nachricht anzupassen:

![Registerkarte Bestätigungsseite des einfachen Umfrage-Editors. Die verfügbaren Felder sind Überschrift, optionaler Textkörper, Button-Text und das On-Click-Verhalten des Buttons.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:80%"}

Wenn Sie Benutzer auf eine andere Seite Ihrer App oder Website leiten möchten, ändern Sie das **On-Click-Verhalten** des Buttons.

### Schritt 5: Gestalten Sie Ihre Nachricht (optional) {#styling}

Sie können die Schriftfarbe und die Akzentfarbe der Nachricht mit dem **Farbthema-Picker** anpassen.

![Tab des einfachen Umfragen-Editors mit der erweiterten Farbauswahl, nachdem ein:e Nutzer:in auf die Farbpalette geklickt hat.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analysieren Sie die Ergebnisse {#analytics}

Sobald Ihre Kampagne gestartet ist, können Sie die Ergebnisse in Echtzeit analysieren, um die Aufschlüsselung jeder ausgewählten Wahl zu sehen. Wenn Sie die [Erfassung von benutzerdefinierten Attributen](#custom-attributes) aktiviert haben, können Sie auch neue Segmente oder Folgekampagnen für Benutzer erstellen, die die Umfrage eingereicht haben.

{% alert note %}
Gelöschte Umfrageoptionen erscheinen weiterhin in der Analyse, werden aber neuen Benutzern nicht mehr als Auswahlmöglichkeit angezeigt.
{% endalert %}

Definitionen der Umfragemetriken finden Sie im [Glossar der Berichtsmetriken][11] und filtern Sie nach "In-App-Nachricht".

![In-App-Nachricht Performance Panel mit Klick-Analytics für jede Auswahl und jeden Button in der Umfrage.]({% image_buster /assets/img/iam/iam-survey-analytics.png %}){: style="max-width:95%"}

Sehen Sie sich die [In-App-Nachrichtenberichte][4] an, um eine Aufschlüsselung Ihrer Kampagnenmetriken zu erhalten.

### Currents {#currents}

Die ausgewählten Optionen fließen automatisch in Currents ein, und zwar unter dem Menüpunkt [**In-App-Nachricht Klick-Events**][6] `button_id` Feld. Jede Auswahl wird mit ihrem universell eindeutigen Identifikator (UUID) gesendet.

## Anwendungsfälle

### Zufriedenheit der Nutzer:innen

**Das Ziel:** Messen Sie die Kundenzufriedenheit und senden Sie Win-Back-Kampagnen an Nutzer, die schlechte Bewertungen hinterlassen haben.

Verwenden Sie für diesen Anwendungsfall die Single-Choice-Auswahl, wobei die Auswahlmöglichkeiten von "Sehr unzufrieden" bis "Sehr zufrieden" reichen. Für jede Auswahl ist das benutzerdefinierte Attribut `customer_satisfaction` auf eine Zahl von 1 bis 5 eingestellt, wobei 1 die geringste Zufriedenheit und 5 die höchste Zufriedenheit bedeutet.

Nachdem Sie Ihre Umfrage gestartet haben, können Sie Ihre Kampagnen zur Rückgewinnung auf Nutzer:innen abstimmen, die angegeben haben, "sehr unzufrieden" oder "unzufrieden" zu sein. Das sind Nutzer:innen, deren `customer_satisfaction` auf 1 oder 2 eingestellt ist.

![][7]

### Ziele der Kund:in identifizieren

**Das Ziel:** Ermitteln Sie die Hauptgründe, warum Benutzer Ihre App besuchen.

Verwenden Sie für diesen Anwendungsfall die Single-Choice-Auswahl, wobei jede Auswahl für einen häufigen Grund steht, aus dem ein:e Nutzer:in Ihre App besuchen könnte. Bei jeder Auswahl ist das benutzerdefinierte Attribut `product_goal` auf das Thema des Anwendungsfalls eingestellt. 

Wenn die:der Nutzer:in zum Beispiel "Mein Konto upgraden" auswählt, wird `product_goal = upgrade` im Nutzerprofil gesetzt.

![][8]

### Verbessern Sie die Konversionsraten

**Das Ziel:** Verstehen Sie, warum Kunden nicht upgraden oder kaufen.

Verwenden Sie für diesen Anwendungsfall die Single-Choice-Auswahl, wobei jede Auswahl einen häufigen Grund darstellt, warum ein:e Nutzer:in nicht auf ein Premium-Konto upgraden kann. Bei jeder Auswahl ist das angepasste Attribut `upgrade_reason` auf die Auswahl der Nutzerin oder des Nutzers eingestellt. 

Wenn die:der Nutzer:in zum Beispiel "Zu teuer" auswählt, wird `upgrade_reason = expensive` im Nutzerprofil gesetzt. Sie können diese Benutzer für Werbeaktionen wie Rabatte oder kostenlose Testversionen ansprechen.

![][9]

### Bevorzugte Features

**Das Ziel:** Verstehen Sie, welche Funktionen Kunden gerne nutzen.

Verwenden Sie für diesen Anwendungsfall die Multiple-Choice-Auswahl, wobei jede Auswahl ein Feature der App darstellt. Bei jeder Auswahl ist das angepasste Attribut `favorite_features` auf die Auswahl der Nutzerin oder des Nutzers eingestellt. Da es sich bei diesem Anwendungsfall um eine Multiple-Choice-Umfrage handelt, wird das Profil des Benutzers nach Abschluss der Umfrage aktualisiert und das Attribut `favorite_features` auf ein Array mit allen ausgewählten Optionen gesetzt.

![][10]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[3]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/managing_custom_data
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe

[7]: {% image_buster /assets/img_archive/simple_survey_use_case_1.png %}
[8]: {% image_buster /assets/img_archive/simple_survey_use_case_2.png %}
[9]: {% image_buster /assets/img_archive/simple_survey_use_case_3.png %}
[10]: {% image_buster /assets/img_archive/simple_survey_use_case_4.png %}

[11]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
