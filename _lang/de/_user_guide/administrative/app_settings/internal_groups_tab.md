---
nav_title: Interne Gruppen
article_title: Interne Gruppe
page_order: 10
page_type: reference
description: "Dieser referenzierte Artikel behandelt interne Gruppen, eine großartige Möglichkeit, um beim Testen der SDK-Integration Insights in die SDK- oder API-Protokolle Ihres Testgeräts zu erhalten."

---

# Interne Gruppen

> Interne Gruppen sind eine großartige Möglichkeit, interne oder externe Testgruppen zu bilden und zu organisieren. Sie bieten Insights in Ihre SDK- oder API-Protokolle und sind nützlich beim Testen Ihrer SDK-Integration. Sie können eine unbegrenzte Anzahl von angepassten internen Gruppen mit bis zu 1.000 Nutzer:innen erstellen.

{% alert tip %}
Wir empfehlen Ihnen auch unseren Braze-Lernkurs [Testen und Fehlerbehebung](https://learning.braze.com/path/developer/testing-and-troubleshooting), in dem Sie lernen, wie Sie interne Gruppen für Ihre eigene Fehlerbehebung und Fehlersuche verwenden.
{% endalert %}

## Voraussetzungen

Bevor Sie interne Gruppen erstellen und verwalten können, benötigen Sie die [Berechtigung Access Dev Console]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) für Ihren Workspace.

## Erstellen einer internen Gruppe

Um eine interne Gruppe zu erstellen, gehen Sie wie folgt vor: 

1. Gehen Sie zu **Einstellungen** > **Interne Gruppen**.
2. Wählen Sie **Interne Gruppe erstellen**.
3. Geben Sie Ihrer Gruppe einen Namen, z. B. "E-Mail-Testgruppe".
4. Wählen Sie eine oder mehrere Gruppenarten, wie in der folgenden Tabelle aufgeführt.

| Gruppe Typ         | Beschreibung                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| **Nutzer-Event-Gruppe**   | Dient zum Überprüfen von Ereignissen oder Protokollen von Ihrem Testgerät.                                    |
| **Content-Testgruppe** | Kann für Push-, E-Mail- und In-App-Nachrichten verwendet werden, um eine gerenderte Kopie der Nachricht zu versenden. |
| **Seed-Gruppe**         | Sendet beim Versenden automatisch eine Kopie der E-Mail an alle Mitglieder der Seed-Gruppe.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\![Eine interne Gruppe mit dem Namen "E-Mail-Testgruppe".]({% image_buster /assets/img_archive/internal_group.png %})

### Hinzufügen von Testnutzer:innen

Nachdem Sie Ihre interne Gruppe erstellt haben, können Sie Testnutzer:innen als Mitglieder dieser Gruppe hinzufügen. 

1. Wählen Sie auf der Verwaltungsseite Ihrer internen Gruppe **Testnutzer:in hinzufügen**.
2. Wählen Sie eine der folgenden Methoden zum Suchen und Auswählen Ihrer Testnutzer:innen.

| Methode                  | Beschreibung                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Identifizierte:n Nutzer:in hinzufügen** | Suchen Sie den Nutzer:innen anhand seiner externen ID, seiner E-Mail Adresse, seiner Telefonnummer oder seines Push-Tokens.                                                                                                                                                           |
| **Anonyme:n Nutzer:in hinzufügen**  | Suche nach IP-Adresse. Geben Sie dann für alle Testnutzer:innen einen Namen ein. Dies ist der Name, mit dem alle [Event-Benutzerprotokolle]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) auf der Seite [Event-Benutzerprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) verknüpft werden. |
| **Nutzer:innen per Masseneintrag hinzufügen**      | Kopieren Sie eine Liste von E-Mail-Adressen oder externen IDs und fügen Sie sie ein. Sie können nur Nutzer:innen hinzufügen, die bereits auf dem Dashboard bekannt sind. Weitere Informationen finden Sie unter [Nutzer:in importieren]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\![Interne Gruppe Einstellungen beim Erstellen einer neuen internen Gruppe]({% image_buster /assets/img_archive/internal_group_add_user.png %})

### Inhalt Testgruppen

Ähnlich wie beim Versenden eines Vorschautests einer Nachricht spart Ihnen die Inhaltstestgruppe Zeit und ermöglicht es Ihnen, Tests an eine vordefinierte Liste von Braze-Benutzern gleichzeitig zu senden. Diese Funktion ist für Push, In-App-Nachrichten, SMS, E-Mail und Content-Cards in Braze verfügbar. Nur Gruppen, die als Content-Test-Gruppen getaggt sind, sind in der Vorschau einer Nachricht verfügbar.

{% alert note %}
[SMS-Testnachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/) können nur an gültige Telefonnummern in der Datenbank gesendet werden.
{% endalert %}

Sie können einzelne Braze Nutzer:innen oder beliebig viele interne Gruppen auswählen, an die Sie die Nachricht senden möchten. Wenn Ihre Nachricht ein Liquid oder eine andere dynamische Personalisierung enthält, verwendet Braze die für jeden Nutzer:innen verfügbaren Attribute, um den Inhalt der Nachricht zu personalisieren. Für Nutzer:innen, die keine Attribute haben, verwendet Braze den eingestellten Standardwert.

Wenn Sie außerdem eine Vorschau der Nachricht als zufälliger Benutzer, angepasster Nutzer:innen oder bestehender Nutzer:innen anzeigen, können Sie stattdessen diese Vorschauversion versenden. Wenn Sie das Kontrollkästchen deaktivieren, können Sie den Versand auf der Grundlage der Attribute des jeweiligen Benutzers und nicht auf der Grundlage der Vorschauversion vornehmen.

Wenn Sie einen IP-Pool zum Versenden einer E-Mail verwenden, können Sie auswählen, von welchem IP-Pool die E-Mail versendet werden soll, indem Sie den Pool aus der verfügbaren Dropdown-Liste auswählen.

\![Der Bereich Test des In-App-Nachricht-Editors, um die Testgruppe für Inhalte auszuwählen.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Seed-Gruppen

Seed-Gruppen werden nur für den E-Mail-Kanal unterstützt. Sie können Nutzer:innen zu einer Seed-Gruppe hinzufügen, um Kopien jeder E-Mail Variante der Nachricht an alle Mitglieder der Gruppe zu senden.

Seed-Gruppen sind für API-Kampagnen nicht verfügbar, aber Sie können Seed-Gruppen über einen API-getriggerten Eingang in die Kampagne aufnehmen. Sie können damit Metriken zur Zustellbarkeit messen und Ihre E-Mail-Inhalte für historische und archivarische Zwecke aufbewahren. 

Nachdem Sie eine interne Gruppe erstellt und mit Tags versehen haben, um sie als Seed-Gruppe zu verwenden, können Sie sie im Schritt **Zielgruppen** des Kampagnen-Editors oder im Schritt **Sendeeinstellungen** in einem Canvas auswählen. 

Bei gesendeten E-Mails wird `[SEED]` an den Anfang der Betreffzeile der E-Mail angehängt. Beachten Sie, dass dies bei E-Mails **nicht der Fall ist**:

- Inkrement sendet im Dashboard Analytics.
- Auswirkungen auf E-Mail Analytics oder Retargeting. 
- Aktualisieren Sie die Liste der **empfangenen Kampagnen** eines Nutzerprofils.
- Frequency-Capping der Auswirkungen.
- Berücksichtigen Sie die Rate-Limits für die Zustellung oder beeinflussen Sie diese.

{% alert tip %}
Wenn die Mitglieder Ihrer Seed-Gruppe berichten, dass sie die Nachricht nicht in ihrem Posteingang sehen, überprüfen Sie, ob sie in der internen Gruppe aufgeführt sind, ob Ihre Betreffzeilen unterschiedlich sind und ob Google Mail die Nachrichten nicht gebündelt hat, oder lassen Sie sie ihre Spam-Ordner überprüfen.
{% endalert %}

#### Für Kampagnen

Wenn Sie eine E-Mail Kampagne erstellen, können Sie Ihre Seed-Gruppen im Bereich **Zielgruppen** des Editors bearbeiten.

Seed-Gruppen werden für jede E-Mail-Variante einmal versendet und werden zugestellt, wenn Ihr Benutzer diese bestimmte Variante zum ersten Mal erhält. Bei geplanten Nachrichten ist dies in der Regel der erste Zeitpunkt, an dem die Kampagne startet. Bei aktionsbasierten oder API-ausgelösten Kampagnen ist dies der Zeitpunkt, an dem der erste Nutzer eine Nachricht erhält.

Wenn Ihre Kampagne multivariat ist und Ihre Variante einen Sendeanteil von 0% hat, wird sie nicht an Seed-Gruppen gesendet. Wenn die Variante bereits versendet wurde und nicht unter **Seed-Gruppen bearbeiten** im Schritt **Ziel** aktualisiert wurde, wird sie außerdem standardmäßig nicht erneut versendet.

{% alert note %}
Wenn Sie eine wiederkehrende Kampagne haben und eine der Varianten aktualisiert wird, können Sie wählen, ob Sie nur an die aktualisierten Varianten oder an alle Varianten erneut senden möchten, oder ob Sie den Versand an die Seed-Gruppe beim Update deaktivieren möchten.
{% endalert %}

\![Die Seed-Gruppe "E-Mail-Seed-Test" wurde ausgewählt, um die E-Mail-Kampagne der Variante 1 zu erhalten.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Für Canvas

Seed-Gruppen in Canvas funktionieren ähnlich wie jede getriggerte Kampagne. Braze erkennt automatisch alle Schritte, die eine E-Mail-Nachricht enthalten, und sendet an diese, wenn Ihr Benutzer zum ersten Mal diesen bestimmten E-Mail-Schritt erreicht.

Wenn ein E-Mail-Schritt aktualisiert wurde, nachdem die Seed-Gruppe gemailt wurde, wird die Option angeboten, nur an aktualisierte Schritte zu senden, an alle Schritte oder die Seeds zu deaktivieren.

