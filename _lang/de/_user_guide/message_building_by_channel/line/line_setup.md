---
nav_title: LINE-Einstellung
article_title: LINE-Einstellung
description: "In diesem Artikel erfahren Sie, wie Sie den Braze LINE-Kanal einrichten, einschließlich der Voraussetzungen und der vorgeschlagenen nächsten Schritte."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# LINE-Einstellung

> In diesem Artikel erfahren Sie, wie Sie den LINE-Kanal in Braze einrichten, Nutzer:innen einrichten, IDs abgleichen und LINE-Testnutzer:innen in Braze erstellen.

## Voraussetzungen

Für die Integration von LINE mit Braze benötigen Sie Folgendes:

- [LINE Geschäftskonto](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- Premium- oder verifizierter Kontostatus (notwendig für die Synchronisierung bestehender Follower)
   - [LINE-Kontorichtlinien](https://terms2.line.me/official_account_guideline_oth) ansehen
- [LINE Entwickler-Konto](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE-Messaging-API-Kanal](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

Wenn Sie LINE-Nachrichten von Braze aus versenden, wird das Nachrichtenguthaben Ihres Kontos verbraucht.

## Arten von LINE-Konten

| Kontotyp | Beschreibung |
| --- | --- |
| Unverifiziertes Konto | Ein ungeprüftes Konto, das von jedermann (Privatperson oder Unternehmen) erhalten werden kann. Dieses Konto wird mit einem grauen Abzeichen dargestellt und erscheint nicht in den Suchergebnissen der LINE-App. |
| Verifiziertes Konto | Ein Konto, das die Überprüfung von LINE Yahoo bestanden hat. Dieses Konto wird mit einem blauen Abzeichen dargestellt und erscheint in den Suchergebnissen der LINE-App.<br><br>Dieses Konto ist nur für Konten mit Sitz in Japan, Taiwan, Thailand und Indonesien verfügbar.  |
| Premium-Konto | Ein Konto, das die Überprüfung von LINE Yahoo bestanden hat. Dieses Konto ist mit einem grünen Abzeichen gekennzeichnet und wird in den Suchergebnissen der LINE-App angezeigt. Dieser Kontotyp wird während des Screenings nach dem Ermessen von LINE automatisch gewährt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erforderlicher Kontotyp

Um Follower mit Braze zu synchronisieren, muss Ihr LINE-Konto überprüft werden oder Premium sein. Wenn Sie ein Konto erstellen, ist sein Standardstatus ungeprüft. Sie müssen eine Kontoverifizierung beantragen.

### Beantragung eines verifizierten LINE-Kontos

{% alert important %}
Verifizierte Konten sind nur für Konten mit Sitz in Japan, Taiwan, Thailand und Indonesien verfügbar.
{% endalert %}

1. Auf der Seite LINE **Offizielles Konto** wählen Sie **Einstellungen**.
2. Wählen Sie unter **Status der Offenlegung von Informationen** die Option **Kontoüberprüfung anfordern**.
3. Geben Sie die erforderlichen Informationen ein.
4. Warten Sie auf eine Benachrichtigung mit den Ergebnissen der Überprüfung.

## Integration von LINE

Um konsistente Benutzeraktualisierungen einzurichten, übernehmen Sie die LINE-IDs bestehender Benutzer und synchronisieren Sie sie alle mit dem Abonnementstatus von LINE:

1. [Importieren oder aktualisieren Sie bekannte Nutzer:innen](#step-1-import-or-update-existing-line-users)
2. [Integration des LINE-Kanals](#step-2-integrate-line-channel)
3. [Nutzer-IDs abgleichen](#step-3-reconcile-user-ids)
4. [Update-Methoden für Nutzer:innen ändern](#step-4-change-your-user-update-methods)
5. [(Optional) Nutzerprofile zusammenführen](#step-5-merge-profiles-optional)

## Schritt 1: Importieren oder aktualisieren Sie bestehende LINE-Benutzer

Dieser Schritt ist notwendig, wenn Sie einen bestehenden und identifizierten LINE-Benutzer haben, da Braze später automatisch dessen Abonnementstatus abruft und das richtige Benutzerprofil aktualisiert. Wenn Sie die Nutzer:innen noch nicht mit ihrer LINE ID abgeglichen haben, überspringen Sie diesen Schritt. 

Sie können Benutzer mit einer der von Braze unterstützten Methoden importieren oder aktualisieren, einschließlich dem [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Endpunkt, [CSV-Import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) oder [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/). 

Unabhängig von der Methode, die Sie verwenden, aktualisieren Sie die `native_line_id`, um die LINE ID des Nutzers:innen anzugeben. Weitere Informationen zu `native_line_id` finden Sie unter [Benutzereinrichtung](#user-setup).

{% alert note %}
Der Status der Abonnementgruppe sollte nicht angegeben werden und wird ignoriert. LINE ist die Quelle der Wahrheit für den Status des Nutzer:innen-Abos, das entweder über das Abo-Synchronisierungstool oder durch Ereignis-Updates mit Braze synchronisiert wird.
{% endalert %}

## Schritt 2: LINE-Kanal integrieren

Nachdem der Integrationsprozess abgeschlossen ist, zieht Braze automatisch die LINE-Follower dieses Kanals in Braze ein. Für alle LINE IDs, die bereits mit einem Braze-Benutzerprofil verbunden sind, wird jedes Profil mit dem Status "abonniert" aktualisiert, und alle verbleibenden LINE IDs werden zu anonymen Benutzern. Außerdem werden für neue Follower Ihres LINE-Kanals nicht identifizierbare Benutzerprofile erstellt, wenn sie dem Kanal folgen.

### Schritt 2.1: Webhook-Einstellungen bearbeiten

1. Gehen Sie in LINE auf die Registerkarte **Messaging API** und bearbeiten Sie Ihre **Webhook-Einstellungen**:
   - Setzen Sie die **Webhook-URL** auf `https://anna.braze.com/line/events`.
      - Braze ändert diese URL bei der Integration automatisch in eine andere URL, die auf Ihrem Dashboard-Cluster basiert.
   - Aktivieren Sie **Webhook verwenden** und **Webhook-Zustellung**. <br><br> ![Webhook-Einstellungsseite, um die Webhook-URL zu überprüfen oder zu bearbeiten, "Webhook verwenden", "Webhook-Wiederzustellung" und "Fehlerstatistiken aggregieren" ein- oder auszuschalten.]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. Beachten Sie die folgenden Informationen auf der Registerkarte **Provider**:

| Informationstyp | Standort |
| --- | --- |
| Anbieter-ID | Wählen Sie Ihren Anbieter und gehen Sie dann zu **\*Einstellungen** > **Grundlegende Informationen** |
| Kanal-ID | Wählen Sie Ihren Anbieter und gehen Sie dann zu **Kanäle** > Ihr Kanal > **Grundeinstellungen** |
| Kanalgeheimnis | Wählen Sie Ihren Anbieter aus und gehen Sie dann zu **Kanäle** > Ihr Kanal > **Grundeinstellungen**. |
| Kanalzugriffs-Token | Wählen Sie Ihren Anbieter aus und gehen Sie dann zu **Kanäle** > Ihr Kanal > **Messaging-API**. Wenn es kein Token für den Kanalzugang gibt, wählen Sie **Fehler** aus. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="3"}
3\. Gehen Sie zu Ihrer Seite **Einstellungen** > **Antworteinstellungen** und führen Sie folgende Schritte aus:
   - Schalten Sie die **Begrüßungsnachricht** aus. Dies kann in Braze über Follow-Trigger gehandhabt werden.
   - Schalten Sie **Automatische Antwortnachrichten** aus. Alle ausgelösten Benachrichtigungen sollten über Braze erfolgen. Das hindert Sie nicht daran, direkt von der LINE-Konsole aus zu senden.
   - Aktivieren Sie **Webhooks**.

![Einstellungsseite für die Antwort mit Umschaltmöglichkeiten, wie Ihr Konto Chats behandeln soll.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### Schritt 2.2: Erzeugen von LINE-Abonnementgruppen in Braze

1. Rufen Sie die Seite Braze Technology Partners für LINE auf und geben Sie die Informationen ein, die Sie auf der Registerkarte LINE **Providers** notiert haben:
   - Anbieter-ID
   - Kanal-ID
   - Kanalgeheimnis
   - Kanalzugriffs-Token

Wenn Sie in Ihrem LINE-Konto ein IP-Whitelisting hinzufügen möchten, fügen Sie alle IP-Adressen, die für Ihren Cluster in der [IP-Zulassungsliste]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-allowlisting) aufgeführt sind, zu Ihrer Zulassungsliste hinzu.

{% alert important %}
Vergewissern Sie sich während der Integration, dass Ihr Kanalgeheimnis korrekt ist. Wenn sie nicht korrekt ist, gibt es möglicherweise Unstimmigkeiten im Abo-Status.
{% endalert %}

![LINE Messaging Integration Seite mit LINE Integration Abschnitt.]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Nach der Verbindung erstellt Braze automatisch eine Braze-Abonnementgruppe für jede LINE-Integration, die erfolgreich zu Ihrem Arbeitsbereich hinzugefügt wurde. <br><br> Alle Änderungen an Ihrer Follower-Liste (z.B. neue Follower oder Unfollower) werden automatisch in Braze übertragen.

![Abschnitt LINE Abo-Gruppen, der eine Abo-Gruppe für den Kanal "LINE" anzeigt.]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## Schritt 3: Nutzer-IDs abgleichen

Kombinieren Sie die LINE-IDs Ihrer Benutzer mit ihren bestehenden Braze-Benutzerprofilen, indem Sie die Schritte unter [Abgleich der Benutzer-IDs](#user-id-reconciliation) ausführen.

## Schritt 4: Nutzeraktualisierungsmethoden ändern 

Angenommen, Sie haben bereits eine Methode, um Benutzeraktualisierungen an Braze zu übermitteln, dann müssen Sie diese aktualisieren, um das neue Feld `native_line_id` einzubeziehen, damit nachfolgende Benutzeraktualisierungen, die an Braze gesendet werden, dieses Feld enthalten.

Es kann sein, dass in Braze nicht identifizierte Benutzerprofile mit `native_line_id` existieren, die im Rahmen der Synchronisierung des Abonnementstatus erstellt wurden, oder wenn ein neuer Follower Ihrem Kanal gefolgt ist. 

Wenn ein:e LINE-Nutzer:in in Ihrer Anwendung durch einen [Nutzerabgleich](#user-id-reconciliation) oder auf andere Weise identifiziert wird, können Sie ein potenziell nicht identifiziertes Nutzerprofil in Braze mit dem [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)-Endpunkt als Ziel auswählen. Jedes nicht identifizierte Nutzerprofil mit einem `native_line_id` hat auch einen Nutzer-Alias `line_id`, der zum Targeting des zu identifizierenden Nutzerprofils verwendet werden kann.

Hier ist ein Beispiel für eine Nutzlast für `/users/identify`, die auf ein nicht identifiziertes Nutzerprofil des Nutzer-Alias `line_id` abzielt: 

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

Wenn für das von Ihnen angegebene `external_id` kein Benutzerprofil vorhanden ist, wird es dem nicht identifizierten Benutzerprofil hinzugefügt, so dass es identifiziert wird. Wenn für `external_id` ein Benutzerprofil existiert, werden alle Attribute, die ausschließlich auf dem nicht identifizierten Benutzerprofil vorhanden sind, in das bekannte Benutzerprofil kopiert, einschließlich `native_line_id` und dem Abonnementstatus des Benutzers.

Sie können Nutzer:innen, die in Ihrer Anwendung bekannt sind, über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Endpunkt aktualisieren, indem Sie ihre externen Bezeichner und `native_line_id` übergeben. Wenn für einen Benutzer bereits ein nicht identifiziertes Benutzerprofil existiert und derselbe `native_line_id` über `/users/track` zu einem anderen Benutzerprofil hinzugefügt wird, erbt er alle Abonnementstatus des nicht identifizierten Benutzerprofils. Es gibt jedoch doppelte Benutzerprofile mit demselben `native_line_id`. Alle nachfolgenden Updates von Abos durch Event-Aktualisierungen werden alle Profile entsprechend aktualisieren. 

Hier ist ein Beispiel für eine Nutzlast für `/users/track`, die ein Nutzerprofil anhand der externen Nutzer-ID aktualisiert, um eine `native_line_id` hinzuzufügen. 

{% raw %}
```json
{
   "attributes": [
       {
           "external_id": "known_external_id_from_your_application",
           "native_line_id": "U89f4a626548ccd48482f529a482f138b",
           "other": "attribute"
       }
   ]
}
```
{% endraw %}

## Schritt 5: Profile zusammenführen (optional)

Wie oben beschrieben, besteht die Möglichkeit, dass mehrere Nutzerprofile mit demselben `native_line_id` existieren. Wenn Ihre Aktualisierungsmethoden doppelte Benutzerprofile erstellen, können Sie mit dem Endpunkt `/user/merge` nicht identifizierte Benutzerprofile mit identifizierten Benutzerprofilen zusammenführen. 

Hier ist ein Beispiel für eine Nutzlast für `/users/merge`, der ein nicht identifiziertes Nutzerprofil mit dem Nutzer-Alias `line_id` zusammenstellt:

{% raw %}
```json
{
 "merge_updates": [
   {
     "identifier_to_merge": {
       "user_alias": {
         "alias_name": "U89f4a626548ccd48482f529a482f138b",
         "alias_label": "line_id"
       }
     },
     "identifier_to_keep": {
       "external_id": "known_external_id_from_your_application"
     }
   }
 ]
}
```
{% endraw %}

{% alert tip %}
Um mehr über die Verwaltung doppelter Nutzer:innen in Braze zu erfahren, lesen Sie bitte [Duplicate Users]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users).
{% endalert %}

## Benutzereinstellungen

LINE ist die Quelle der Wahrheit für den Abo-Status der Nutzer:innen. Selbst wenn Sie die LINE-ID eines Benutzers haben (`native_line_id`), wird LINE dem Benutzer keine Nachrichten zustellen, wenn dieser Benutzer dem LINE-Kanal, von dem aus Sie senden, nicht gefolgt ist.

Um diese Aufgabe zu bewältigen, bietet Braze Tools und eine Logik, die eine gut integrierte Nutzerbasis unterstützt, einschließlich der Synchronisierung von Abos und der Aktualisierung von Events für LINE-Follows und -Unfollows.

### Synchronisierung von Abonnements und Ereignislogik

1. **Abo-Synchronisationstool:** Dieses Tool wird automatisch nach einer erfolgreichen LINE-Kanalintegration eingesetzt. Verwenden Sie es, um bestehende Profile zu aktualisieren und neue Profile zu erstellen.<br><br>Alle Nutzerprofile von Braze, die ein `native_line_id` haben, das dem Kanal LINE folgt, werden auf den Abo-Gruppenstatus `subscribed` aktualisiert. Jeder Follower des LINE-Kanals, der kein Nutzerprofil von Braze mit der Adresse `native_line_id` hat, wird es haben:<br><br>\- Ein anonymes Benutzerprofil, das mit `native_line_id` erstellt wurde und auf die LINE ID des Benutzers nach dem Kanal eingestellt ist <br>\- Ein Benutzer-Alias `line_id`, der auf die dem Kanal folgende Benutzer-LINE-ID eingestellt ist <br>\- Ein Abo-Gruppenstatus von `subscribed`

{: start="2"}
2\. **Event-Updates:** Diese werden verwendet, um den Status des Abos eines Nutzers:innen zu aktualisieren. Wenn Braze-Updates von Nutzer-Events für den integrierten LINE-Kanal empfängt und es sich um ein Follow-Event handelt, hat das Nutzerprofil den Abo-Gruppenstatus `subscribed`. Wenn es sich um ein Unfollow-Event handelt, hat das Nutzerprofil einen Abo-Gruppenstatus von `unsubscribed`.<br><br>\- Alle Braze-Benutzerprofile mit einem passenden `native_line_id` werden automatisch aktualisiert. <br>\- Wenn für ein Event kein passendes Nutzerprofil existiert, [erstellt Braze eine:n anonyme:n Nutzer:in]({{site.baseurl}}/line/user_management/).

## Anwendungsfälle

Dies sind Anwendungsfälle, wie Nutzer:innen aktualisiert werden können, nachdem Sie die obigen Einrichtungsschritte ausgeführt haben.

##### Bestehendes Braze-Benutzerprofil folgt bereits dem LINE-Kanal

1. Das Braze-Benutzerprofil wird mit einem `native_line_id` -Attribut aktualisiert. Sein Standard-Abonnementstatus ist `unsubscribed`.
2. Das Tool zur Synchronisierung von Abonnements wird ausgeführt, stellt fest, dass der Benutzer dem LINE-Kanal folgt, und aktualisiert dann das Benutzerprofil mit dem Abonnementstatus `subscribed`.
3. Wenn sich der Abonnementstatus ändert (z. B. wenn der Benutzer den Kanal blockiert, entfreundet oder erneut folgt), erhält Braze die Aktualisierung von LINE und aktualisiert das Benutzerprofil mit `native_line_id` entsprechend.

##### Bestehendes Benutzerprofil hat LINE-Kanal blockiert, entfreundet oder entfolgt 

1. Das Braze-Benutzerprofil wird mit einem `native_line_id` -Attribut aktualisiert. Sein Standard-Abonnementstatus ist `unsubscribed`.
2. Das Abo-Synchronisierungstool findet nicht, dass der Nutzer:in dem Kanal LINE folgt und der Abo-Status des Nutzers:innen bleibt auf `unsubscribed`.
3. Wenn der Nutzer dem Kanal später folgt, erhält Braze das Update von LINE und aktualisiert das Nutzerprofil mit dem Abo-Status `subscribed`.

##### Die Erstellung des Nutzerprofils erfolgt nach LINE-Follow

1. Der Kanal erhält einen neuen LINE-Follower.
2. Braze erstellt ein anonymes Benutzerprofil mit dem Attribut `native_line_id`, das auf die LINE-ID des Followers eingestellt ist, und einem Benutzer-Alias von `line_id`, das auf die LINE-ID des Followers eingestellt ist. Das Profil hat einen Abonnementstatus von `subscribed`.
3. Der Benutzer wird durch den [Benutzerabgleich](#user-id-reconciliation) als Inhaber der LINE ID identifiziert.
  - Das Profil des oder der anonymen Nutzers oder Nutzerin kann über den Endpunkt [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) identifiziert werden. Spätere Aktualisierungen (über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Endpunkt, [CSV-Import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) oder [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) zu diesem Benutzerprofil können den Benutzer über diese bekannte `external_id` ansprechen.

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

  - Ein neues Nutzerprofil kann (über den Endpunkt [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), den [CSV-Import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) oder die [Datenaufnahme in der Cloud]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) durch Festlegen der `native_line_id` erstellt werden. Dieses neue Profil erbt den Status des Abonnementstatus des bestehenden anonymen Benutzerprofils. Beachten Sie, dass dies dazu führt, dass sich mehrere Profile dieselbe `native_line_id` teilen. Diese können jederzeit über den Endpunkt `/users/merge` im Rahmen des in [Schritt 5](#step-5-merge-profiles-optional) beschriebenen Prozesses zusammengeführt werden.

##### Die Erstellung des Benutzerprofils erfolgt vor dem LINE follow

1. Sie erwerben einen neuen Benutzer und senden die Informationen an Braze. Ein neues Benutzerprofil wird erstellt (Profil 1).
2. Der Benutzer folgt Ihrem LINE-Konto.
3. Braze empfängt ein Follow-Event und erstellt ein anonymes Nutzerprofil (Profil 2).
4. Der Benutzer wird durch den [Benutzerabgleich](#user-id-reconciliation) als Inhaber der LINE ID identifiziert.
5. Sie aktualisieren das Profil 1, um das Attribut `native_line_id` festzulegen. Dieses Profil erbt den Status des Abo-Status von Profil 2.
  - Jetzt gibt es zwei Benutzerprofile mit demselben `native_line_id`. Diese können jederzeit über den Endpunkt `/users/merge` im Rahmen des in [Schritt 5](#step-5-merge-profiles-optional) beschriebenen Prozesses zusammengeführt werden.

## Nutzer-ID-Abgleich 

LINE IDs werden automatisch von Braze empfangen, wenn ein Nutzer Ihrem Kanal folgt oder wenn Sie den einmaligen Workflow "Follower synchronisieren" verwenden. LINE IDs sind auch spezifisch für den Kanal, dem die Benutzer folgen, so dass es unwahrscheinlich ist, dass Benutzer ihre LINE IDs angeben können.

Es gibt zwei Möglichkeiten, eine LINE-ID mit einem bestehenden Nutzerprofil von Braze zu kombinieren:

- [LINE-Anmeldung](#line-login)
- [Verknüpfung von Nutzerkonten](#user-account-linking)

### LINE Anmeldung

Diese Methode verwendet Social Media Anmeldungen zum Abgleich. Wenn sich ein Benutzer bei Ihrer App anmeldet, hat er die Möglichkeit, mit [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) ein Benutzerkonto zu erstellen oder sich einzuloggen.

{% alert note %}
Um die richtige LINE-ID für jeden Benutzer zu erhalten, richten Sie LINE Login unter demselben Anbieter ein wie Ihr in Braze integriertes offizielles LINE-Konto oder -Kanal.
{% endalert %}

1. Rufen Sie die LINE-Entwicklerkonsole auf und [beantragen Sie die Erlaubnis, die E-Mail-Adressen der Benutzer zu erhalten](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission), die sich über LINE Login bei Ihrer App anmelden.

2. Befolgen Sie die entsprechenden Schritte, die von LINE zur Verfügung gestellt werden, um LINE Login zu implementieren:<br><br>
  - [Web-App-Anleitungen](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [Native App-Anleitungen](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>Achten Sie darauf, dass Sie `email` in den für Verifizierungsanfragen [festgelegten Umfang](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes) einbeziehen. 

{: start="3"}
3\. Verwenden Sie den [Aufruf „ID-Token verifizieren“](https://developers.line.biz/en/reference/line-login/#verify-id-token), um die E-Mail des Nutzers oder der Nutzerin zu erhalten. 

4. Speichern Sie die LINE ID des Benutzers (`native_line_id`) im Profil des Benutzers mit einer passenden E-Mail in Ihrer Datenbank, oder erstellen Sie ein neues Benutzerprofil mit der E-Mail und der LINE ID des Benutzers.

5. Senden Sie die neuen oder aktualisierten Benutzerinformationen über den [Endpunkt`/user/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users/), [CSV-Import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) oder [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/) an Braze.

#### Workflows

##### Bestehende:r Follower verwendet LINE-Anmeldung

**Szenario:** Ein anonymer Benutzer wurde bei der ersten Synchronisierung der Abonnenten oder nach der Integration durch ein "Follow"-Ereignis erstellt.

1. Der Benutzer meldet sich mit LINE Login bei Ihrer App an.
2. LINE liefert Ihnen die E-Mail-Adresse des Benutzers.
3. Sie senden Braze den aktualisierten Benutzer (das bestehende Benutzerprofil mit dieser E-Mail, um die LINE ID hinzuzufügen) oder Sie aktualisieren den anonymen Benutzer mit der E-Mail.

##### Neue:r Follower verwendet LINE-Anmeldung

**Szenario:** In Braze existiert kein Benutzerprofil mit der LINE ID des Benutzers.

1. Der Benutzer meldet sich mit LINE Login bei Ihrer App an.
2. LINE liefert Ihnen die E-Mail-Adresse des Benutzers.
3. Sie haben diese Möglichkeiten:
  - Aktualisieren Sie ein bestehendes Benutzerprofil mit dieser E-Mail, damit es auch die LINE ID des Benutzers enthält.
  - Erstellen Sie ein neues Benutzerprofil mit der E-Mail und der LINE ID.
4. Wenn der Benutzer Ihrem offiziellen LINE-Konto folgt, erhält Braze ein Follow-Ereignis und aktualisiert den Abonnementstatus des Benutzers auf `subscribed`.

### Verknüpfung von Nutzerkonten 

Mit dieser Methode können Benutzer ihr LINE-Konto mit dem Benutzerkonto Ihrer App verknüpfen. Sie können dann Liquid in Braze verwenden, z. B. {% raw %}`{{line_id}}`{% endraw %}, um eine personalisierte URL für den Benutzer zu erstellen, die die LINE-ID des Benutzers an Ihre Website oder App weiterleitet, die dann mit einem bekannten Benutzer verknüpft werden kann.

1. Erstellen Sie ein aktionsbasiertes Canvas, das auf einer Änderung des Abo-Status basiert und ausgelöst wird, wenn ein:e Nutzer:in Ihren LINE-Kanal abonniert.<br>![Canvas, das triggert, wenn ein Nutzer:in den LINE-Kanal abonniert wird.]({% image_buster /assets/img/line/account_link_1.png %})
2. Erstellen Sie eine Nachricht, die Benutzer dazu anregt, sich bei Ihrer Website oder App anzumelden, indem Sie die LINE ID des Benutzers als Abfrageparameter (über Liquid) übergeben, z.B. so:

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3\. Erstellen Sie eine Nachricht, in der Ihnen der Code für den Gutschein zugestellt wird.
4\. (Optional) Erstellen Sie eine aktionsbasierte Kampagne oder ein Canvas, das ausgelöst wird, wenn der LINE-Benutzer identifiziert wird, um dem Benutzer seinen Gutscheincode zu senden. <br>![Aktionsbasierte Kampagne, die ausgelöst wird, wenn der Nutzer:innen von LINE identifiziert wird.]({% image_buster /assets/img/line/account_link_2.png %})

#### Funktionsweise

Nachdem sich der oder die Nutzer:in angemeldet hat, wird auf Ihrer Website oder App eine Änderung vorgenommen, sodass die Nutzer-ID an Braze zurückgeschickt wird, um sie mit der LINE-ID zu verknüpfen, die als Teil der URL übergeben wurde:

```json
const currentUrl = new URL(window.location.href)
const queryParams = new URLSearchParams(currentUrl.search);
const lineUserId = queryParams.get("line_user_id")

if (user && isLoggedIn && lineUserId) {
  post(
   "https://rest.iad-03.braze.com	/users/identify",
   {
     "aliases_to_identify": [
       {
   "external_id": user.getUserId(),
   "user_alias": {
     "alias_name": lineUserId,
     "alias_label": "line_id"
   }
 }
      ]
    }
  )
  braze.logCustomEvent("identified_line_user_for_promotion");
}
```

#### Workflows

##### Bestehender Benutzer folgt Ihrem LINE-Kanal

**Szenario:** Ein bestehender Benutzer in Braze folgt Ihrem Kanal auf LINE.

1. LINE sendet Braze ein Follow-Event.
2. Braze erstellt ein anonymes Nutzerprofil mit der LINE ID, dem `line_id` Nutzer-Alias und dem LINE Abo-Gruppenstatus von `subscribed`.
3. Der Benutzer erhält eine LINE-Nachricht mit einem Link zu Ihrer Website und App und meldet sich an. Ihr Benutzerprofil ist nun bekannt.
4. Das erstellte anonyme Nutzerprofil wird identifiziert und über den [/users/identify-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) mit dem bekannten Nutzerprofil des Nutzers oder der Nutzerin zusammengeführt. Das bekannte Benutzerprofil enthält nun die LINE ID und hat den Abonnementstatus `subscribed`.
5. (Optional) Der Benutzer erhält eine LINE-Nachricht mit dem Gutscheincode und Braze protokolliert den Versand an das Braze-Benutzerprofil.

## LINE-Testbenutzer in Braze erstellen

Sie können Ihren LINE-Kanal testen, bevor Sie eine [Benutzerabstimmung](#user-id-reconciliation) einrichten, indem Sie ein "Wer bin ich"-Canvas oder eine Kampagne erstellen.

1. Richten Sie ein Canvas ein, das die Braze ID eines Nutzers:innen bei einem bestimmten triggernden Wort zurückgibt. <br><br>Beispiel Auslöser <br><br>![Triggern Sie die Kampagne an Nutzer:in, die eine eingehende LINE an eine bestimmte Abo-Gruppe gesendet haben.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>Beispielnachricht<br><br>![LINE Nachricht mit Angabe der Braze Nutzer:in ID.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. In Braze können Sie die Braze ID verwenden, um nach bestimmten Nutzer:innen zu suchen und sie bei Bedarf zu ändern.

{% alert important %}
Stellen Sie sicher, dass Canvas keine globale Kontrolle oder Kontrollgruppen hat, die das Senden verhindern.
{% endalert %}


