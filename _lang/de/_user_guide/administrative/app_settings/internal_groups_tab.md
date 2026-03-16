---
nav_title: Interne Gruppen
article_title: Interne Gruppe
page_order: 10
page_type: reference
description: "Dieser Referenzartikel beschreibt interne Gruppen, eine hervorragende Möglichkeit, um beim Testen der SDK-Integration Einblicke in die SDK- oder API-Protokolle Ihres Geräts zu erhalten."

---

# Interne Gruppen

> Interne Gruppen sind eine großartige Möglichkeit, interne oder externe Testgruppen zu bilden und zu organisieren. Sie bieten Insights in Ihre SDK- oder API-Protokolle und sind nützlich beim Testen Ihrer SDK-Integration. Sie können eine unbegrenzte Anzahl von angepassten internen Gruppen mit bis zu 1.000 Nutzer:innen erstellen.

{% alert tip %}
Wir empfehlen Ihnen auch unseren Braze-Lernkurs [Testen und Fehlerbehebung](https://learning.braze.com/path/developer/testing-and-troubleshooting), in dem Sie lernen, wie Sie interne Gruppen für Ihre eigene Fehlerbehebung und Fehlersuche verwenden.
{% endalert %}

## Voraussetzungen

Um interne Gruppen zu erstellen und zu verwalten, benötigen Sie die [alte Berechtigung „Access Dev Console“]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions) oder die folgenden [detaillierten Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions):

- API-Schlüssel anzeigen
- API-Schlüssel bearbeiten
- Interne Gruppen anzeigen
- Interne Gruppen bearbeiten
- Nachrichten-Aktivitätsprotokoll anzeigen
- Event-Nutzerprotokoll anzeigen
- API-Bezeichner anzeigen
- Dashboard zur API-Nutzung anzeigen
- API-Limits anzeigen
- API-Nutzungsmeldungen anzeigen
- API-Nutzungsmeldungen bearbeiten
- SDK-Debugger bearbeiten
- SDK Debugger anzeigen

{% multi_lang_include deprecations/user_permissions.md %}

## Erstellen einer internen Gruppe

Um eine interne Gruppe zu erstellen: 

1. Gehen Sie zu **Einstellungen** > **Interne Gruppen**.
2. Wählen Sie **Interne Gruppe erstellen**.
3. Geben Sie Ihrer Gruppe einen Namen, z. B. "E-Mail-Testgruppe".
4. Wählen Sie eine oder mehrere Gruppenarten, wie in der folgenden Tabelle aufgeführt.

| Gruppe Typ         | Beschreibung                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| **Nutzer-Event-Gruppe**   | Verwenden Sie diese Option, um Ereignisse oder Protokolle von Ihrem Testgerät zu überprüfen.                                    |
| **Content-Testgruppe** | Verwenden Sie dies für Push-Benachrichtigungen, E-Mails und In-App-Nachrichten, um eine gerenderte Kopie der Nachricht zu versenden. |
| **Seed-Gruppe**         | Versendet beim Absenden automatisch eine Kopie der E-Mail an alle Mitglieder der Seed-Gruppe.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Eine interne Gruppe mit dem Namen „E-Mail-Testgruppe”.]({% image_buster /assets/img_archive/internal_group.png %})

### Hinzufügen von Testnutzer:innen

Nachdem Sie Ihre interne Gruppe erstellt haben, fügen Sie Testnutzer:innen als Mitglieder dieser Gruppe hinzu. 

1. Wählen Sie auf der Verwaltungsseite Ihrer internen Gruppe **Testnutzer:in hinzufügen**.
2. Wählen Sie eine der folgenden Methoden zum Suchen und Auswählen Ihrer Testnutzer:innen.

| Methode                  | Beschreibung                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Identifizierte:n Nutzer:in hinzufügen** | Suchen Sie den Nutzer:innen anhand seiner externen ID, seiner E-Mail Adresse, seiner Telefonnummer oder seines Push-Tokens.                                                                                                                                                           |
| **Anonyme:n Nutzer:in hinzufügen**  | Suche nach IP-Adresse. Bitte geben Sie anschließend für jeden hinzugefügten Testnutzer:in einen Namen an. Dies ist der Name, mit dem alle Ereignisprotokolle auf der Seite [„Event-Benutzerprotokoll“]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) verknüpft sind. |
| **Nutzer:innen per Masseneintrag hinzufügen**      | Kopieren Sie eine Liste von E-Mail-Adressen oder externen IDs und fügen Sie sie ein. Es können nur Nutzer:innen hinzugefügt werden, die bereits im Dashboard bekannt sind. Weitere Informationen finden Sie unter [Nutzer:in importieren]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Interne Gruppeneinstellungen beim Erstellen einer neuen internen Gruppe]({% image_buster /assets/img_archive/internal_group_add_user.png %})

### Inhalt Testgruppen

Ähnlich wie beim Versenden eines Vorschau-Tests einer Nachricht spart Ihnen die Content Test Group Zeit und ermöglicht es Ihnen, Tests für eine vordefinierte Liste von Braze-Nutzer:innen gleichzeitig zu starten. Diese Funktion ist für Push, In-App-Nachrichten, SMS, E-Mail und Content-Cards in Braze verfügbar. In der Vorschau einer Nachricht sind nur Gruppen verfügbar, die als „Content Test Groups“ gekennzeichnet sind.

{% alert note %}
[SMS-Testnachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/) können nur an gültige Telefonnummern in der Datenbank gesendet werden.
{% endalert %}

Bitte wählen Sie einzelne Braze-Nutzer:innen oder eine beliebige Anzahl interner Gruppen aus, an die die Nachricht gesendet werden soll. Wenn Ihre Nachricht Liquid oder andere dynamische Personalisierungen enthält, verwendet Braze die für jeden Nutzer:in verfügbaren Attribute, um den Inhalt der Nachricht zu personalisieren. Für Nutzer:innen, die keine Attribute haben, verwendet Braze den Standard-Wert.

Wenn Sie die Nachricht als zufällige Nutzer:in, angepasste Nutzer:in oder bestehende Nutzer:in in der Vorschau anzeigen, können Sie stattdessen diese in der Vorschau angezeigte Version versenden. Wenn Sie das Kontrollkästchen deaktivieren, können Sie die E-Mail basierend auf den Attributen jeder Nutzer:in anstatt der Vorschau-Version versenden.

Wenn Sie einen IP-Pool zum Versenden einer E-Mail verwenden, wählen Sie bitte den gewünschten IP-Pool aus der Dropdown-Liste aus, um festzulegen, von welchem Pool die E-Mail versendet werden soll.

![Der Testbereich des In-App-Nachrichteneditors zum Auswählen der Content-Testgruppe.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Seed-Gruppen

Seed-Gruppen werden nur für den E-Mail-Kanal unterstützt. Fügen Sie Nutzer:innen zu einer Seed-Gruppe hinzu, um Kopien jeder E-Mail-Variante an alle Mitglieder der Gruppe zu senden.

Seed-Gruppen sind für API-Kampagnen nicht verfügbar, aber Sie können Seed-Gruppen über einen API-getriggerten Eingang in die Kampagne aufnehmen. Verwenden Sie diese Funktion, um Metriken zur Zustellbarkeit zu messen und Ihre E-Mail-Inhalte für historische und Archivierungszwecke zu dokumentieren. 

Nachdem Sie eine interne Gruppe erstellt und diese als Seed-Gruppe gekennzeichnet haben, wählen Sie sie im Schritt **„Zielgruppen“** des Kampagneneditors oder im Schritt **„Sendeeinstellungen“** in einem Canvas aus. 

Bei gesendeten E-Mails wird `[SEED]` an den Anfang der Betreffzeile der E-Mail angehängt. Beachten Sie, dass dies bei E-Mails **nicht der Fall ist**:

- Inkrement sendet die Dashboard-Analytics.
- Auswirkungen auf E-Mail Analytics oder Retargeting. 
- Aktualisieren Sie die Liste der **empfangenen Kampagnen** eines Nutzerprofils.
- Frequency-Capping der Auswirkungen.
- Berücksichtigen Sie die Rate-Limits für die Zustellung oder beeinflussen Sie diese.

#### Abo-Verhalten

Seed-Sendungen sind für die interne Qualitätssicherung und Überprüfung vorgesehen, daher umgehen sie mit Absicht die Abonnementprüfungen für die Nutzer:innen des Unternehmens, an das die Sendung gerichtet ist. Dies bedeutet, dass Nutzer:innen mit gültigen E-Mail-Adressen, die Teil einer Seed-Gruppe sind, die Nachricht auch dann erhalten, wenn sie nicht abonniert sind. Die Nachricht muss jedoch so konfiguriert werden, dass Seed-Kopien an diese Gruppe gesendet werden.

{% alert tip %}
Wenn die Mitglieder Ihrer Seed-Gruppe berichten, dass sie die Nachricht nicht in ihrem Posteingang sehen, überprüfen Sie, ob sie in der internen Gruppe aufgeführt sind, ob Ihre Betreffzeilen unterschiedlich sind und ob Google Mail die Nachrichten nicht gebündelt hat, oder lassen Sie sie ihre Spam-Ordner überprüfen.
{% endalert %}

#### Für Kampagnen

Wenn Sie eine E-Mail-Kampagne erstellen, bearbeiten Sie bitte Ihre Seed-Gruppen im Abschnitt **„Zielgruppen“** des Editors.

{% alert important %}
Wenn Sie eine Seed-Gruppe so konfigurieren, dass sie automatisch an alle Kampagnen angehängt wird, gilt dies nur für neue Kampagnen. Dies gilt nicht, wenn Sie bereits vorhandene Kampagnen kopieren. Bitte wenden Sie die gewünschten Seed-Gruppen manuell auf die kopierte Kampagne im Abschnitt **„Zielgruppen“** an.
{% endalert %}

Seed-Gruppen werden für jede E-Mail-Variante einmal versendet und werden zugestellt, wenn Ihr Benutzer diese bestimmte Variante zum ersten Mal erhält. Bei geplanten Nachrichten ist dies in der Regel der erste Zeitpunkt, an dem die Kampagne startet. Bei aktionsbasierten oder API-ausgelösten Kampagnen ist dies der Zeitpunkt, zu dem der erste Nutzer eine Nachricht erhält.

Wenn Ihre Kampagne multivariat ist und Ihre Variante einen Versandanteil von 0 % aufweist, wird sie nicht an Seed-Gruppen versendet. Darüber hinaus wird die Variante standardmäßig nicht erneut versendet, wenn sie bereits versendet und im Schritt **„Ziel“** unter **„Seed-Gruppen bearbeiten**“ nicht für einen erneuten Versand aktualisiert wurde.

{% alert note %}
Wenn Sie eine wiederkehrende Kampagne haben und eine der Varianten aktualisiert wird, können Sie wählen, ob Sie nur an die aktualisierten Varianten oder an alle Varianten erneut senden möchten, oder ob Sie den Versand an die Seed-Gruppe beim Update deaktivieren möchten.
{% endalert %}

![Die Seed-Gruppe „E-Mail-Seed-Test“ wurde ausgewählt, um die E-Mail-Kampagne der Variante 1 zu erhalten.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Für Canvas

Seed-Gruppen in Canvas funktionieren ähnlich wie jede andere ausgelöste Kampagne. Braze erkennt automatisch alle Schritte, die eine E-Mail-Nachricht enthalten, und sendet diese, sobald Ihre Nutzer:in diesen bestimmten E-Mail-Schritt zum ersten Mal erreicht.

Wenn ein E-Mail-Schritt nach dem Versand der Seed-Gruppe aktualisiert wurde, bietet Braze die Option, nur aktualisierte Schritte zu versenden, alle Schritte zu versenden oder Seeds zu deaktivieren.