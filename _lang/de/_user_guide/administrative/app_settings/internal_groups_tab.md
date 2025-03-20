---
nav_title: Interne Gruppen
article_title: Interne Gruppe
page_order: 10
page_type: reference
description: "Dieser Referenzartikel behandelt interne Gruppen, eine großartige Möglichkeit, um beim Testen der SDK-Integration Insights in die SDK- oder API-Protokolle Ihres Testgeräts zu erhalten."

---

# Interne Gruppen

> Interne Gruppen sind eine hervorragende Möglichkeit, interne oder externe Testgruppen zu erstellen und zu organisieren. Sie bieten Insights in Ihre SDK- oder API-Protokolle und sind nützlich beim Testen Ihrer SDK-Integration. Sie können eine unbegrenzte Anzahl von benutzerdefinierten internen Gruppen mit bis zu 1.000 Mitgliedern erstellen.

Sie benötigen die [Berechtigung]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) **Access Dev Console** für Ihren Arbeitsbereich, um interne Gruppen zu erstellen und zu verwalten.

{% alert tip %}
Zusätzlich zu diesem Artikel empfehlen wir Ihnen auch unseren Braze Learning-Kurs [Qualitätssicherung und Debugging-Tools](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), in dem Sie lernen, wie Sie interne Gruppen für Ihre eigene Fehlersuche und -behebung nutzen können.
{% endalert %}

## Eine Gruppe erstellen

Um eine interne Gruppe zu erstellen, führen Sie die folgenden Schritte aus: 

1. Gehen Sie zu **Einstellungen** > **Interne Gruppen**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie diese Seite unter **Einstellungen** > **Entwicklerkonsole** > **Interne Gruppen**.
{% endalert %}

{:start="2"}
2\. Klicken Sie auf **Interne Gruppe erstellen**.
3\. Geben Sie Ihrer Gruppe einen aussagekräftigen Namen.
4\. Wählen Sie eine oder mehrere Gruppenarten, wie in der folgenden Tabelle aufgeführt.

![Erstellen einer internen Gruppe in Braze][7]

| Gruppentyp     | Anwendungsfall     |
| :------------- | :------------- |
| Nutzer-Event-Gruppe| Dient zum Überprüfen von Ereignissen oder Protokollen von Ihrem Testgerät.|
| Content-Testgruppe | Ein ähnliches Konzept wie bei Testlisten. Kann für Push-, E-Mail- und In-App-Nachrichten verwendet werden, um eine gerenderte Kopie der Nachricht zu versenden.|
| Seed-Gruppe | Sendet beim Senden automatisch eine Kopie der E-Mail an alle Mitglieder der Seed-Gruppe.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Hinzufügen von Testnutzer:innen

Nachdem Sie Ihre interne Gruppe erstellt haben, können Sie Testnutzer:innen als Mitglieder dieser Gruppe hinzufügen. Klicken Sie auf der Verwaltungsseite Ihrer internen Gruppe auf **Testbenutzer hinzufügen** und fügen Sie sie entweder als identifizierte oder als anonyme Benutzer in der Masse hinzu.

![Interne Gruppeneinstellungen bei der Erstellung einer neuen internen Gruppe][8]

| Additionsmethode | Beschreibung |
| :------------- | :------------- |
| Identifizierte Nutzer:innen |Suchen Sie den Nutzer:innen anhand seiner externen ID oder seiner E-Mail Adresse.|
|Anonyme Benutzer| Suche nach IP-Adresse. Geben Sie dann für alle Testnutzer:innen einen Namen ein. Dies ist der Name, mit dem alle [Event-Benutzerprotokolle]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/) auf der Seite [Event-Benutzerprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/) verknüpft werden.|
|Nutzer:innen per Masseneintrag hinzufügen|Kopieren Sie eine Liste von E-Mail-Adressen oder externen IDs und fügen Sie sie in den vorgesehenen Bereich ein. Sie können nur Nutzer:innen hinzufügen, die bereits auf dem Dashboard bekannt sind. Weitere Informationen finden Sie unter [Benutzerimport]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Inhalt Testgruppen

Ähnlich wie beim Versenden eines Vorschautests einer Nachricht spart Ihnen die Inhaltstestgruppe Zeit und ermöglicht es Ihnen, Tests an eine vordefinierte Liste von Braze-Benutzern gleichzeitig zu senden. Diese Funktion ist für Push-Nachrichten, In-App-Nachrichten, SMS, E-Mails und Content Cards in Braze verfügbar.

{% alert note %}
[SMS-Testnachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) können nur an gültige Telefonnummern in der Datenbank gesendet werden.
{% endalert %}

Sie können einzelne Braze-Benutzer oder beliebig viele interne Gruppen auswählen, an die Sie die Nachricht senden möchten. Wenn Ihre Nachricht ein Liquid oder eine andere dynamische Personalisierung enthält, verwendet Braze die für jeden Nutzer:innen verfügbaren Attribute, um den Inhalt der Nachricht zu personalisieren. Für Nutzer:innen, die keine Attribute haben, verwendet Braze den eingestellten Standardwert.

Wenn Sie außerdem eine Vorschau der Nachricht als zufälliger Benutzer, angepasster Nutzer:innen oder bereits vorhandener Nutzer:innen anzeigen, können Sie stattdessen diese Vorschauversion versenden. Wenn Sie das Kontrollkästchen deaktivieren, können Sie den Versand auf der Grundlage der Attribute des jeweiligen Benutzers und nicht auf der Grundlage der Vorschauversion vornehmen.

Wenn Sie schließlich einen IP-Pool zum Versenden einer E-Mail verwenden, können Sie auswählen, von welchem IP-Pool die E-Mail versendet werden soll, indem Sie den Pool aus der Dropdown-Liste auswählen.

Nur Gruppen, die als Content-Test-Gruppen getaggt sind, sind in der Vorschau einer Nachricht verfügbar.

![Test an Content-Test-Gruppen senden][9]{: style="max-width:50%" }

### Seed-Gruppen

Seed Groups sind nur für den E-Mail-Kanal gedacht und ermöglichen es Ihnen, eine Kopie jeder E-Mail-Variante an die Mitglieder dieser Gruppe zu senden. Seed-Gruppen sind für API-Kampagnen nicht verfügbar, obwohl Sie Seed-Gruppen über einen API-getriggerten Entry in die Kampagne aufnehmen können. Dieses Feature wird in der Regel mit Partnern wie Return Path oder 250OK verwendet, um Metriken zur Zustellbarkeit zu messen. Es kann dazu verwendet werden, den Content von E-Mails für historische und archivarische Zwecke aufzuzeichnen. 

Nachdem Sie eine interne Gruppe erstellt und für die Verwendung als Seed-Gruppe markiert haben, können Sie sie im Schritt **Zielbenutzer** des Kampagnen-Composers oder im Schritt **Sendeeinstellungen** in einem Canvas auswählen. Bei gesendeten E-Mails wird der Bezeichner `[SEED]` an den Anfang der Betreffzeile der E-Mail angehängt. Beachten Sie, dass gesendete Seed-E-Mails in Dashboard Analytics nicht inkrementiert werden und keinen Einfluss auf E-Mail Analytics oder Retargeting haben. Sie aktualisieren auch nicht die Liste der **empfangenen Kampagnen** eines Benutzerprofils.

{% alert tip %}
Wenn Ihre Seed Group-Mitglieder berichten, dass sie die Nachricht nicht in ihrem Posteingang sehen, vergewissern Sie sich, dass sie in der Internen Gruppe aufgeführt sind, stellen Sie sicher, dass Ihre Betreffzeilen unterschiedlich sind und dass Google Mail die E-Mails nicht gebündelt hat, oder lassen Sie sie ihre SPAM-Ordner überprüfen.
{% endalert %}

#### Für Kampagnen

Seed-Gruppen können bei der Erstellung einer E-Mail-Kampagne auf der Seite **Targeting** bearbeitet werden.

Seed-Gruppen werden für jede E-Mail-Variante einmal versendet und werden zugestellt, wenn Ihr Benutzer diese bestimmte Variante zum ersten Mal erhält. Bei geplanten Nachrichten ist dies in der Regel der erste Zeitpunkt, an dem die Kampagne startet. Bei aktionsbasierten oder API-ausgelösten Kampagnen ist dies der Zeitpunkt, an dem der erste Nutzer eine Nachricht erhält.

Wenn Ihre Kampagne multivariat ist und Ihre Variante eine Versandrate von 0 % hat, wird sie nicht an Seed-Gruppen gesendet. Wenn die Variante bereits versendet wurde und im Schritt **Ziel** unter **Saatgutgruppen bearbeiten** nicht für den erneuten Versand aktualisiert wurde, wird sie außerdem standardmäßig nicht erneut versendet.

{% alert note %}
Wenn es sich um eine wiederkehrende Kampagne handelt und eine der Varianten aktualisiert wird, haben Sie die Möglichkeit, nur an die aktualisierten Varianten oder an alle Varianten erneut zu senden oder den Versand an die Seed-Gruppe beim Update zu deaktivieren.
{% endalert %}

![Seed-Gruppen-Vorschau für eine Kampagne][11]

#### Für Canvas

Seed-Gruppen in Canvas funktionieren ähnlich wie bei jeder getriggerten Kampagne. Braze erkennt automatisch alle Schritte, die eine E-Mail-Nachricht enthalten, und sendet an diese, wenn Ihr Benutzer zum ersten Mal diesen bestimmten E-Mail-Schritt erreicht.

Wenn ein E-Mail-Schritt aktualisiert wurde, nachdem die Seed-Gruppe gemailt wurde, wird die Option angeboten, nur an aktualisierte Schritte zu senden, an alle Schritte oder die Seeds zu deaktivieren.


[7]: {% image_buster /assets/img_archive/internal_group.png %}
[8]: {% image_buster /assets/img_archive/UserLogs1.png %}
[9]: {% image_buster /assets/img_archive/content_test_preview.png %}
[11]: {% image_buster /assets/img_archive/seed_group_campaign.png %}
