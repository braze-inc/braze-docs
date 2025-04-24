---
nav_title: Benutzerprofile
article_title: Benutzerprofile
page_order: 5
page_type: reference
tool: 
  - Dashboard
description: "Dieser Referenzartikel beschreibt, wie Sie im Dashboard auf das Profil eines Benutzers zugreifen können, welche Anwendungsfälle es gibt und was jedes Profil enthält."

---

# Benutzerprofile

> Nutzerprofile sind eine gute Möglichkeit, um Informationen über bestimmte Nutzer:innen zu finden. Alle persistenten Daten, die mit einem Benutzer verbunden sind, werden in dessen Benutzerprofil gespeichert.

## Zugangsprofile

Um auf das Profil eines Benutzers zuzugreifen, gehen Sie auf die Seite **Benutzer suchen** und suchen Sie nach einem Benutzer anhand einer der folgenden Möglichkeiten:

- Externe Benutzer-ID
- Braze-ID
- E-Mail
- Telefonnummer
- Push-Token
- Benutzer-Alias mit dem Format "[user_alias]:[alias_name]", wie z.B. "amplitude_id:user_123"

Wenn eine Übereinstimmung gefunden wird, können Sie die Informationen, die Sie für diese Nutzer:innen erfasst haben, mit dem Braze SDK einsehen. Andernfalls, wenn Ihre Suche mehrere Nutzerprofile ergibt, können Sie jedes Profil einzeln zusammenführen oder eine Massen-Zusammenführung von Nutzer:innen durchführen. Eine vollständige Anleitung finden Sie unter [Doppelte Benutzer]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/).

![Suchergebnisse mit einem Banner mit der Aufschrift "Mehrere Nutzer:innen entsprechen Ihren Suchkriterien" und zwei Buttons mit der Aufschrift Zurück und Weiter.][1]

## Anwendungsfälle

Benutzerprofile sind eine großartige Ressource für die Fehlersuche und das Testen, da Sie ganz einfach auf Informationen über den Engagementverlauf eines Benutzers, seine Segmentzugehörigkeit, sein Gerät und sein Betriebssystem zugreifen können.

Wenn zum Beispiel ein Benutzer ein Problem meldet und Sie nicht sicher sind, welches Gerät und Betriebssystem er verwendet, können Sie die [Registerkarte Übersicht](#overview-tab) verwenden, um diese Informationen zu finden (vorausgesetzt, Sie haben die E-Mail oder die Benutzer-ID des Benutzers). Sie können auch die Sprache eines Benutzers anzeigen, was bei der Fehlersuche in einer [mehrsprachigen Kampagne][13] ], die sich nicht wie erwartet verhalten hat, hilfreich sein kann.

Auf der [Registerkarte Engagement](#engagement-tab) können Sie überprüfen, ob ein bestimmter Benutzer eine Kampagne erhalten hat. Wenn dieser Nutzer die Kampagne erhalten hat, können Sie außerdem sehen, wann er sie erhalten hat. Sie können auch überprüfen, ob ein Nutzer:in einem bestimmten Segment ist und ob ein Nutzer:in für Push, E-Mail oder beides opt-in ist. Diese Informationen sind für die Fehlersuche nützlich. Sie sollten diese Informationen zum Beispiel überprüfen, wenn ein Benutzer eine Kampagne nicht erhält, die Sie erwartet haben, oder eine Kampagne erhält, die Sie nicht erwartet haben.

## Elemente des Benutzerprofils

Es gibt vier Hauptabschnitte im Profil eines Benutzers.

- **Überblick:** Grundlegende Informationen über den Benutzer, Sitzungsdaten, benutzerdefinierte Attribute, benutzerdefinierte Ereignisse, Einkäufe und das Gerät, bei dem sich der Benutzer zuletzt angemeldet hat.
- **Engagement:** Informationen über die Kontakteinstellungen des Benutzers, erhaltene Kampagnen, Segmente, Kommunikationsstatistiken, Installationszuordnung und zufällige Bucket-Nummer.
- **Nachrichtenverlauf:** Jüngste Ereignisse im Zusammenhang mit Messaging für diesen Nutzer:innen aus den letzten 30 Tagen.

### Registerkarte Übersicht {#overview-tab}

Die Registerkarte **Übersicht** enthält grundlegende Informationen über einen Benutzer und seine Interaktionen mit Ihrer App oder Website.

| Kategorie Übersicht | Enthält |
| --- | --- |
| Profil | Geschlecht, Altersgruppe, Standort, Sprache, Gebietsschema, Zeitzone und Geburtsdatum. |
| Sitzungsübersicht | Anzahl der Sitzungen, Zeitpunkt der ersten und letzten Sitzung und verwendete Apps. |
| Angepasste Attribute | Welche benutzerdefinierten Attribute diesem Benutzer zugeordnet sind und ihr zugehöriger Wert, einschließlich verschachtelter benutzerdefinierter Attribute. |
| Neueste Geräte | Auf wie vielen Geräten sie sich eingeloggt haben, Details zu jedem Gerät und die zugehörigen Werbe-IDs (falls vorhanden). |
| Angepasste Events | Welche angepassten Events durchgeführt wurden und wie oft und wann dies zuletzt geschehen ist. |
| Käufe | Lebenszeitumsatz, der diesem Benutzer zugeschrieben wird, sein letzter Kauf, die Gesamtzahl der Käufe und eine Liste der einzelnen Käufe. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Informationen zu diesen Daten finden Sie unter [Sammlung von Benutzerdaten][12].

![Die Registerkarte Übersicht eines Benutzerprofils.][2]

### Engagement-Tab {#engagement-tab}

Die Registerkarte **Engagement** enthält Informationen über die Interaktionen eines Benutzers mit den Nachrichten, die Sie ihm mit Braze geschickt haben.

| Kategorie Engagement | Enthält |
| --- | --- |
| Kontakt-Einstellungen | Abonnementstatus für E-Mail, SMS und Push und die Abonnementgruppen, denen dieser Benutzer für diese drei Kanäle zugeordnet ist. Dieser Abschnitt enthält auch Informationen zum Änderungsprotokoll für Push-Tokens. Unter [E-Mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) und [Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) finden Sie Informationen darüber, wie Abonnements und Opt-Ins eingerichtet werden. |
| Erhaltene Kampagnen | Empfangene Kampagnen werden markiert, wenn der Benutzer die Kampagne erhält oder wenn wir zum ersten Mal Interaktionsdaten für einen Benutzer erkennen. Wählen Sie eine Kampagne aus der Liste, um sie anzuzeigen. |
| Segmente | Segmente, in denen dieser Benutzer enthalten ist. Wählen Sie ein Segment aus der Liste aus, um es anzuzeigen. |
| Kommunikationsstatistiken | Wann dieser Benutzer zuletzt Nachrichten von Ihnen aus jedem Kanal erhalten hat. |
| Install-Attribution | Informationen darüber, wie und wann ein Benutzer Ihre App installiert hat. Erfahren Sie mehr über das [Verständnis von Benutzerinstallationen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/install_attribution/). |
| Verschiedenes | Die zufällig generierte nutzerspezifische [Bucket-Nummer]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) |
| Empfangene Canvas-Nachrichten | Canvas-Nachrichten, die dieser Benutzer erhalten hat und wann. Wählen Sie eine Nachricht aus der Liste aus, um sie anzusehen. |
| Prognosen | Werte für die [Abwanderungsvorhersage]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/) und die [Ereignisvorhersage]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/) für diesen Benutzer. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Die Registerkarte Engagement eines Benutzerprofils, auf der die Kontakteinstellungen und Kommunikationsstatistiken angezeigt werden.][3]

### Registerkarte Nachrichtenverlauf

Der Tab **Nachrichtenverlauf** des Nutzerprofils zeigt die jüngsten Ereignisse im Zusammenhang mit Messaging (etwa 40) für einen einzelnen Nutzer:innen aus den letzten 30 Tagen. Zu diesen Ereignissen gehören die Nachrichten, die der Benutzer gesendet oder empfangen hat, mit denen er interagiert hat, und vieles mehr. Beachten Sie, dass die Daten in diesem Tab bei einer Nutzerzusammenführung nicht aktualisiert werden.

{% alert note %}
Wenn Sie Feedback zu dieser Tabelle haben oder bestimmte Ereignisse sehen möchten, mailen Sie bitte [user-targeting@braze.com](mailto:user-targeting@braze.com?subject=Messaging%20History%20Tab%20Feedback) mit der Betreffzeile "Messaging History Tab Feedback".
{% endalert %}

![Die Registerkarte Nachrichtenverlauf zeigt an, welche Kampagnen und Canvases ein Benutzer erhalten hat.][5]

#### Events anzeigen und auswerten

Für jedes Ereignis in der Tabelle **Nachrichtenverlauf** können Sie den Nachrichtenkanal, den Ereignistyp, den Zeitstempel des Ereignisses, die zugehörige Kampagne oder Canvas-Nachricht und die Gerätedaten des Benutzers sehen. Um nach bestimmten Ereignissen zu filtern, klicken Sie auf **Filter** und wählen Sie Ereignisse aus der Liste aus.

##### Nachrichtenengagement-Events

Die folgenden Ereignisse zum Nachrichtenengagement sind bei E-Mail, SMS, Push-Benachrichtigungen, In-App-Nachrichten, Content-Cards und Webhooks verfügbar. Wenn Sie genauer wissen möchten, wie bestimmte Ereignisse verfolgt werden, lesen Sie bitte das [Glossar Nachrichten-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

| Kanal | Engagement-Events verfügbar |
| --- | --- |
| E-Mail | Absprung<br>Klick<br>Zustellung<br>Als Spam markieren<br>Öffnen (siehe [Ereignis E-Mail öffnen](#note-on-email-open-event))<br>Senden<br>Zustellfehler (Soft Bounce)<br>Abmelden |
| SMS | Netzbetreiber-Sendung<br>Zustellung<br>Zustellfehler<br>Eingehende Nachricht empfangen<br>Zurückweisung<br>Senden |
| Push | Absprung<br>Beeinflusste Öffnung<br>iOS-Foreground<br>Öffnung<br>Senden |
| In-App-Nachricht | Klick<br>Impression |
| Content-Cards | Klick<br>Ausblenden<br>Impression<br>Senden |
| Webhooks | Senden |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Abbruch von Nachrichten

Nachrichtenabbruch-Ereignisse treten auf, wenn eine an einen Benutzer gesendete Nachricht aufgrund von bedingter Logik in [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) oder [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content#aborting-messages) oder aufgrund von Liquid-Rendering-Zeitüberschreitungen abgebrochen wurde.

Abbruchereignisse gibt es für die folgenden Kanäle:

- E-Mail
- SMS
- Push
- Webhooks

Abbruchereignisse sind derzeit nicht für In-App-Nachrichten und Inhaltskarten verfügbar.

##### Frequency-Capping-Ereignisse

Ein Frequency-Capping-Ereignis tritt ein, wenn ein Nutzer:innen für den Empfang einer Nachricht qualifiziert ist, diese aber aufgrund der [Frequency-Capping-Einstellungen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) nicht erhält. Sie können die Einstellungen für die Frequenzbegrenzung unter **Einstellungen** > **Frequenzbegrenzungsregeln** anpassen.

##### Leere Ziele

Einige gesendete Nachrichten werden im Nachrichtenverlauf mit leeren Zielen angezeigt (gekennzeichnet durch "-"). Das liegt daran, dass einige Kanäle wie Content-Cards und Webhooks beim Nachrichtenversand keine Gerätedaten erfassen.

Der Versand von Content-Cards wird protokolliert, wenn die Karte zur Ansicht verfügbar ist. Da Content-Cards auf mehreren Geräten angezeigt werden können, werden die Gerätedaten beim Versand nicht protokolliert. Stattdessen werden diese Informationen beim Abdruck protokolliert (wenn die Karte tatsächlich angesehen wird). Webhooks werden an einen Endpunkt des Systems (nicht an ein Gerät) gesendet, sodass keine Gerätedaten vorliegen.

#### Ereignis E-Mail öffnen {#note-on-email-open-event}

Das Tracking der Öffnung von E-Mails ist in jedem Tool fehleranfällig, auch in Braze. Da die verschiedenen E-Mail-Clients eine Vielzahl von Datenschutzfunktionen anbieten, die entweder das automatische Laden von Bildern blockieren oder sie proaktiv auf den Server laden, sind Ereignisse beim Öffnen von E-Mails sowohl für falsch positive als auch für falsch negative Ergebnisse anfällig.

Auch wenn Statistiken über die Öffnung von E-Mails in ihrer Gesamtheit nützlich sein können, z.B. um die Effektivität verschiedener Betreffzeilen zu vergleichen, sollten Sie nicht davon ausgehen, dass ein einzelnes Öffnungsereignis für einen einzelnen Nutzer:innen aussagekräftig ist.


[1]: {% image_buster /assets/img_archive/User_Search_Nonunique.png %}
[2]: {% image_buster /assets/img_archive/user_profile2.png %}
[3]: {% image_buster /assets/img_archive/profiles_engagement_tab.png %}
[5]: {% image_buster /assets/img_archive/profiles_messaging_history_tab.png %}
[12]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[13]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
