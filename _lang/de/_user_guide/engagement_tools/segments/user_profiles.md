---
nav_title: Nutzerprofile
article_title: Nutzerprofile
page_order: 9
page_type: reference
tool: 
  - Dashboard
description: "Dieser Referenzartikel beschreibt, wie Sie im Dashboard auf das Profil von Nutzer:innen zugreifen können, welche Anwendungsfälle es gibt und was jedes Profil enthält."

---

# Nutzerprofile

> Nutzerprofile sind eine gute Möglichkeit, um Informationen über bestimmte Nutzer:innen zu finden. Alle persistenten Daten, die mit Nutzer:innen verknüpft sind, werden in deren Nutzerprofil gespeichert.

## Auf Profile zugreifen

Um auf das Profil von Nutzer:innen zuzugreifen, gehen Sie auf die Seite **Nutzer:innen suchen** und suchen Sie anhand einer der folgenden Möglichkeiten:

- Externe Nutzer-ID
- Braze-ID
- E-Mail
- Telefonnummer
- Push-Token
- Nutzer-Alias mit dem Format "[user_alias]:[alias_name]", wie z. B. "amplitude_id:user_123"

Wenn eine Übereinstimmung gefunden wird, können Sie die Informationen, die Sie für diese Nutzer:innen mit dem Braze SDK erfasst haben, einsehen. Andernfalls, wenn Ihre Suche mehrere Nutzerprofile ergibt, können Sie jedes Profil einzeln zusammenführen oder eine Massen-Zusammenführung von Nutzer:innen durchführen. Eine vollständige Anleitung finden Sie unter [Doppelte Nutzer:innen]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/).

{% alert important %}
Wenn eine Telefonnummer in der Suche verwendet wird, wird sie in das [`E.164`](https://en.wikipedia.org/wiki/e.164)-Format umgewandelt. Nutzer:innen, deren Telefonnummern nicht in das Format `E.164` umgewandelt werden können (z. B. weil die Telefonnummer eine ungültige Landesvorwahl oder Ortsvorwahl hat), können nicht nach der Telefonnummer gesucht werden.
{% endalert %}

![Suchergebnisse mit einem Banner, auf dem steht „Mehrere Nutzer:innen entsprechen Ihren Suchkriterien" und zwei Buttons mit der Aufschrift „Zurück" und „Weiter".]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Anwendungsfälle

Nutzerprofile sind eine großartige Ressource für die Fehlerbehebung und das Testen, da Sie ganz einfach auf Informationen über den Engagement-Verlauf, die Segmentzugehörigkeit, das Gerät und das Betriebssystem von Nutzer:innen zugreifen können.

Wenn zum Beispiel Nutzer:innen ein Problem melden und Sie nicht sicher sind, welches Gerät und Betriebssystem verwendet wird, können Sie den [Tab „Übersicht"](#overview-tab) verwenden, um diese Informationen zu finden (vorausgesetzt, Sie haben die E-Mail oder die Nutzer-ID). Sie können auch die Sprache von Nutzer:innen anzeigen, was bei der Fehlerbehebung einer [mehrsprachigen Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages), die sich nicht wie erwartet verhalten hat, hilfreich sein kann.

Auf dem [Tab „Engagement"](#engagement-tab) können Sie überprüfen, ob bestimmte Nutzer:innen eine Kampagne erhalten haben. Wenn diese Nutzer:innen die Kampagne erhalten haben, können Sie außerdem sehen, wann sie sie erhalten haben. Sie können auch überprüfen, ob Nutzer:innen in einem bestimmten Segment sind und ob sie für Push, E-Mail oder beides ein Opt-in haben. Diese Informationen sind für die Fehlerbehebung nützlich. Sie sollten diese Informationen zum Beispiel überprüfen, wenn Nutzer:innen eine Kampagne nicht erhalten, die Sie erwartet haben, oder eine Kampagne erhalten, die Sie nicht erwartet haben.

## Elemente des Nutzerprofils

Es gibt vier Hauptabschnitte im Profil von Nutzer:innen.

- **Übersicht:** Grundlegende Informationen über die Nutzer:innen, Sitzungsdaten, angepasste Attribute, angepasste Events, Käufe und das Gerät, bei dem sich die Nutzer:innen zuletzt angemeldet haben.
- **Engagement:** Informationen über die Kontakteinstellungen, erhaltene Kampagnen, Segmente, Kommunikationsstatistiken, Install-Attribution und zufällige Bucket-Nummer.
- **Nachrichtenverlauf:** Jüngste Messaging-bezogene Ereignisse für diese Nutzer:innen aus den letzten 30 Tagen.
- **Feature-Flags-Berechtigung:** Überprüfen Sie, für welche Feature-Flags Nutzer:innen bei Rollouts, Canvas-Schritten und Experimenten derzeit berechtigt sind.

### Tab „Übersicht" {#overview-tab}

Der Tab **Übersicht** enthält grundlegende Informationen über Nutzer:innen und deren Interaktionen mit Ihrer App oder Website.

| Übersichtskategorie | Enthält |
| --- | --- |
| Profil | Geschlecht, Altersgruppe, Standort, Sprache, Gebietsschema, Zeitzone und Geburtsdatum. |
| Sitzungsübersicht | Wie viele Sitzungen stattfanden, wann die erste und letzte Sitzung war und mit welchen Apps. |
| Angepasste Attribute | Welche angepassten Attribute diesen Nutzer:innen zugeordnet sind und ihr zugehöriger Wert, einschließlich verschachtelter angepasster Attribute. |
| Neueste Geräte | Auf wie vielen Geräten sich angemeldet wurde, Details zu jedem Gerät und die zugehörigen Werbe-IDs (falls vorhanden). |
| Angepasste Events | Welche angepassten Events durchgeführt wurden, wie oft und wann dies zuletzt geschehen ist. |
| Käufe | Lifetime-Umsatz, der diesen Nutzer:innen zugeschrieben wird, der letzte Kauf, die Gesamtzahl der Käufe und eine Liste der einzelnen Käufe. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Informationen zu diesen Daten finden Sie unter [SDK-Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/).

![Der Tab „Übersicht" eines Nutzerprofils.]({% image_buster /assets/img_archive/user_profile2.png %})

### Tab „Engagement" {#engagement-tab}

Der Tab **Engagement** enthält Informationen über die Interaktionen von Nutzer:innen mit den Nachrichten, die Sie ihnen über Braze gesendet haben.

| Engagement-Kategorie | Enthält |
| --- | --- |
| Kontakteinstellungen | Abo-Status für E-Mail, SMS und Push sowie die Abo-Gruppen, denen diese Nutzer:innen für diese drei Kanäle zugeordnet sind. Dieser Abschnitt enthält auch Changelog-Informationen für Push-Token. Unter [E-Mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) und [Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) finden Sie Informationen darüber, wie Abos und Opt-ins eingerichtet werden. |
| Erhaltene Kampagnen | Erhaltene Kampagnen werden markiert, wenn Nutzer:innen die Kampagne erhalten oder wenn erstmals Interaktionsdaten erkannt werden. Wählen Sie eine Kampagne aus der Liste, um sie anzuzeigen. |
| Segmente | Segmente, in denen diese Nutzer:innen enthalten sind. Wählen Sie ein Segment aus der Liste aus, um es anzuzeigen. |
| Kommunikationsstatistiken | Wann diese Nutzer:innen zuletzt Nachrichten von Ihnen aus den einzelnen Kanälen erhalten haben. |
| Install-Attribution | Informationen darüber, wie und wann Nutzer:innen Ihre App installiert haben. Mehr erfahren über das [Verständnis von Nutzerinstallationen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/install_attribution/). |
| Verschiedenes | Die [zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) der Nutzer:innen. |
| Empfangene Canvas-Nachrichten | Canvas-Nachrichten, die diese Nutzer:innen erhalten haben und wann. Wählen Sie eine Nachricht aus der Liste aus, um sie anzusehen. |
| Prognosen | Werte für die [Abwanderungsprognose]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) und die [Event-Prognose]({{site.baseurl}}/user_guide/brazeai/predictive_events/) für diese Nutzer:innen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Der Tab „Engagement" eines Nutzerprofils mit Kontakteinstellungen und Kommunikationsstatistiken.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Tab „Nachrichtenverlauf"

Der Tab **Nachrichtenverlauf** des Nutzerprofils zeigt die jüngsten Messaging-bezogenen Ereignisse (etwa 40) für einzelne Nutzer:innen aus den letzten 30 Tagen. Zu diesen Ereignissen gehören die Nachrichten, die gesendet, empfangen oder mit denen interagiert wurde, und mehr.

{% alert note %}
Die Daten in diesem Tab werden nach einer Nutzerzusammenführung nicht aktualisiert. Außerdem werden Ereignisse, die mit über die API gesendeten Nachrichten verknüpft sind (z. B. der [/messages/send-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#creating-new-users-with-api-sends)), in diesem Tab nicht angezeigt, wenn in diesen Sendungen keine Kampagnen-ID angegeben ist.
{% endalert %}

![Der Tab „Nachrichtenverlauf" zeigt an, welche Kampagnen und Canvase Nutzer:innen erhalten haben.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Events anzeigen und auswerten

Für jedes Ereignis in der Tabelle **Nachrichtenverlauf** können Sie den Messaging-Kanal, den Event-Typ, den Zeitstempel des Ereignisses, die zugehörige Kampagne oder Canvas-Nachricht und die Gerätedaten der Nutzer:innen sehen. Um nach bestimmten Ereignissen zu filtern, klicken Sie auf **Filter** und wählen Sie Ereignisse aus der Liste aus.

##### Nachrichtenengagement-Events

Die folgenden Nachrichtenengagement-Events sind für E-Mail, SMS, Push, In-App-Nachrichten, Content Cards und Webhooks verfügbar. Wenn Sie genauer wissen möchten, wie bestimmte Events getrackt werden, lesen Sie das [Glossar der Nachrichtenengagement-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

| Kanal | Verfügbare Engagement-Events |
| --- | --- |
| E-Mail | Absprung<br>Klick<br>Verzögerungsereignisse<br>Zustellung<br>Als Spam markieren<br>Öffnung (siehe [Hinweis zum E-Mail-Öffnungsereignis](#note-on-email-open-event))<br>Senden<br>Soft Bounce<br>Abmelden |
| SMS | Netzbetreiber-Sendung<br>Zustellung<br>Zustellfehler<br>Eingehende Nachricht empfangen<br>Zurückweisung<br>Senden |
| Push | Absprung<br>Beeinflusste Öffnung<br>iOS-Foreground<br>Öffnung<br>Senden |
| In-App-Nachricht | Klick<br>Impression |
| Content Cards | Klick<br>Ausblenden<br>Impression<br>Senden |
| Webhooks | Senden |
| WhatsApp | Abbrechen<br>Zustellung<br>Fehler<br>Frequency-Capping<br>Eingehende Nachricht empfangen<br>Gelesen<br>Senden |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Nachrichtenabbruch-Events

Nachrichtenabbruch-Events treten auf, wenn eine an Nutzer:innen gesendete Nachricht aufgrund von bedingter Logik in [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) oder [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content#aborting-messages) oder aufgrund von Liquid-Rendering-Zeitüberschreitungen abgebrochen wurde.

Abbruch-Events gibt es für die folgenden Kanäle:

- E-Mail
- SMS
- Push
- Webhooks

Abbruch-Events sind derzeit nicht für In-App-Nachrichten und Content Cards verfügbar.

##### Frequency-Capping-Events

Ein Frequency-Capping-Event tritt ein, wenn Nutzer:innen für den Empfang einer Nachricht qualifiziert sind, diese aber aufgrund der [Frequency-Capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)-Einstellungen nicht erhalten. Sie können die Frequency-Capping-Einstellungen unter **Einstellungen** > **Frequency-Capping-Regeln** anpassen.

##### Leere Ziele

Einige gesendete Nachrichten werden im Nachrichtenverlauf mit leeren Zielen angezeigt (gekennzeichnet durch „—"). Das liegt daran, dass einige Kanäle wie Content Cards und Webhooks beim Nachrichtenversand keine Gerätedaten erfassen.

Der Versand von Content Cards wird protokolliert, wenn die Karte zur Ansicht verfügbar ist. Da Content Cards auf mehreren Geräten angezeigt werden können, werden die Gerätedaten beim Versand nicht protokolliert. Stattdessen werden diese Informationen bei der Impression protokolliert (wenn die Karte tatsächlich angesehen wird). Webhooks werden an einen System-Endpunkt (nicht an ein Gerät) gesendet, sodass keine Gerätedaten vorliegen.

#### Hinweis zum E-Mail-Öffnungsereignis {#note-on-email-open-event}

Das Tracking von E-Mail-Öffnungen ist in jedem Tool fehleranfällig, auch in Braze. Da die verschiedenen E-Mail-Clients eine Vielzahl von Datenschutzfunktionen anbieten, die entweder das automatische Laden von Bildern blockieren oder sie proaktiv auf dem Server laden, sind E-Mail-Öffnungsereignisse sowohl für falsch positive als auch für falsch negative Ergebnisse anfällig.

Auch wenn Statistiken zu E-Mail-Öffnungen in ihrer Gesamtheit nützlich sein können, z. B. um die Effektivität verschiedener Betreffzeilen zu vergleichen, sollten Sie nicht davon ausgehen, dass ein einzelnes Öffnungsereignis für einzelne Nutzer:innen aussagekräftig ist.

#### Warum sind bestimmte Felder im Tab „Nachrichtenverlauf" leer?

In den folgenden Szenarien können einige Felder im Tab **Nachrichtenverlauf** von Nutzer:innen fehlen:

- Wenn bei einem Ereignis Daten für **Gesendete Nachricht** fehlen, bedeutet dies, dass die Kampagne keine Nachrichtenvarianten enthält.
- Wenn bei einem Ereignis Daten für **Kampagne/Canvas** und **Gesendete Nachricht** fehlen, bedeutet dies, dass diese Nachricht von einer API-Kampagne (nicht von API-getriggerten Kampagnen) gesendet wurde, die `campaign_id` und `message_variation_id` nicht angegeben hat. Diese Felder sind optional und können im Anfrage-Body weggelassen werden. Wenn diese Felder angegeben werden, werden die Informationen in die Nachrichtenverlauf-Protokolle aufgenommen.
   - Wenn eine bestimmte Nachricht im Nachrichtenverlauf fehlt, aber im Protokoll **Erhaltene Kampagnen** erscheint, haben die Nutzer:innen die Kampagne wahrscheinlich erhalten, bevor sie als aktuelle Nutzer:innen identifiziert wurden. Wenn ein bestehendes Profil verwaist ist, wird das Protokoll **Erhaltene Kampagnen** übertragen, der Nachrichtenverlauf jedoch nicht.
- Wenn Daten für **Kampagne/Canvas** fehlen, wurde möglicherweise ein manueller Test gesendet. Manuelle Tests werden im Tab **Nachrichtenverlauf** protokolliert, aber die Kampagne oder das Canvas, das gesendet wurde, wird nicht protokolliert.

## Verwandte Artikel

- [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
- [POST: Nutzerprofil nach Bezeichner exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)
- [POST: Nutzer:innen löschen]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)