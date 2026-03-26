---
nav_title: LINE-Einrichtung
article_title: LINE-Einrichtung
description: "In diesem Artikel erfahren Sie, wie Sie den Braze LINE-Kanal einrichten, einschließlich der Voraussetzungen und der vorgeschlagenen nächsten Schritte."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# LINE-Einrichtung

> In diesem Artikel erfahren Sie, wie Sie den LINE-Kanal in Braze einrichten, Nutzer:innen einrichten, Nutzer-IDs abgleichen und LINE-Testnutzer:innen in Braze erstellen.

## Voraussetzungen

Für die Integration von LINE mit Braze benötigen Sie Folgendes:

- [LINE-Geschäftskonto](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- Premium- oder verifizierter Kontostatus (notwendig für die Synchronisierung bestehender Follower)
   - [LINE-Kontorichtlinien](https://terms2.line.me/official_account_guideline_oth) ansehen
- [LINE-Entwicklerkonto](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE-Messaging-API-Kanal](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

Das Versenden von LINE-Nachrichten über Braze wird von den Nachrichtenguthaben Ihres Kontos abgezogen.

{% alert note %}
**Festlegen von `native_line_id`**: Sie können `native_line_id` festlegen, indem Sie Updates für Nutzer:innen an Braze senden (beispielsweise über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)-Endpunkt, [CSV-Import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/cloud_ingestion/)). Falls Ihr clientseitiges SDK kein spezielles Feld für `native_line_id` enthält, übermitteln Sie es mithilfe einer dieser Methoden in serverseitigen Updates für Nutzer:innen.
{% endalert %}

## Arten von LINE-Konten

| Kontotyp | Beschreibung |
| --- | --- |
| Unverifiziertes Konto | Ein ungeprüftes Konto, das von jedermann (Privatperson oder Unternehmen) erstellt werden kann. Dieses Konto wird mit einem grauen Badge dargestellt und erscheint nicht in den Suchergebnissen der LINE-App. |
| Verifiziertes Konto | Ein Konto, das die Überprüfung von LINE Yahoo bestanden hat. Dieses Konto wird mit einem blauen Badge dargestellt und erscheint in den Suchergebnissen der LINE-App.<br><br>Dieses Konto ist nur für Konten mit Sitz in Japan, Taiwan, Thailand und Indonesien verfügbar.  |
| Premium-Konto | Ein Konto, das die Überprüfung von LINE Yahoo bestanden hat. Dieses Konto ist mit einem grünen Badge gekennzeichnet und wird in den Suchergebnissen der LINE-App angezeigt. Dieser Kontotyp wird während des Screenings nach dem Ermessen von LINE automatisch gewährt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erforderlicher Kontotyp

Um Follower mit Braze zu synchronisieren, muss Ihr LINE-Konto verifiziert oder Premium sein. Wenn Sie ein Konto erstellen, ist sein Standardstatus unverifiziert. Sie müssen eine Kontoverifizierung beantragen.

### Beantragung eines verifizierten LINE-Kontos

{% alert important %}
Verifizierte Konten sind nur für Konten mit Sitz in Japan, Taiwan, Thailand und Indonesien verfügbar.
{% endalert %}

1. Wählen Sie auf der LINE-Seite **Offizielles Konto** die Option **Einstellungen**.
2. Wählen Sie unter **Status der Offenlegung von Informationen** die Option **Kontoüberprüfung anfordern**.
3. Geben Sie die erforderlichen Informationen ein.
4. Warten Sie auf eine Benachrichtigung mit den Ergebnissen der Überprüfung.

## Integration von LINE

Um konsistente Nutzer-Updates einzurichten, die LINE-IDs bestehender Nutzer:innen zu übernehmen und sie alle mit dem Abo-Status von LINE zu synchronisieren:

1. [Importieren oder aktualisieren Sie bekannte Nutzer:innen](#step-1-import-or-update-existing-line-users)
2. [Integrieren Sie den LINE-Kanal](#step-2-integrate-line-channel)
3. [Gleichen Sie Nutzer-IDs ab](#step-3-reconcile-user-ids)
4. [Ändern Sie die Update-Methoden für Nutzer:innen](#step-4-change-your-user-update-methods)
5. [(Optional) Führen Sie Nutzerprofile zusammen](#step-5-merge-profiles-optional)

{% alert note %}
Es ist nur ein LINE-Konto pro Workspace zulässig. Wenn Sie über mehrere LINE-Konten verfügen, empfehlen wir, jedes Konto in einem separaten Workspace zu verwenden.
{% endalert %}

## 1. Schritt: Bestehende LINE-Nutzer:innen importieren oder aktualisieren

Dieser Schritt ist notwendig, wenn Sie bereits identifizierte LINE-Nutzer:innen haben, da Braze später automatisch deren Abo-Status abruft und das richtige Nutzerprofil aktualisiert. Wenn Sie die Nutzer:innen noch nicht mit ihrer LINE-ID abgeglichen haben, überspringen Sie diesen Schritt. 

Sie können Nutzer:innen mit einer der von Braze unterstützten Methoden importieren oder aktualisieren, einschließlich dem [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)-Endpunkt, [CSV-Import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/cloud_ingestion/). 

Unabhängig von der verwendeten Methode aktualisieren Sie `native_line_id`, um die LINE-ID der Nutzer:innen anzugeben. Weitere Informationen zu `native_line_id` finden Sie unter [Nutzereinrichtung](#user-setup).

{% alert note %}
Der Abo-Gruppenstatus sollte nicht angegeben werden und wird ignoriert. LINE ist die maßgebliche Quelle für den Abo-Status der Nutzer:innen, der entweder über das Abo-Synchronisierungstool oder durch Event-Updates mit Braze synchronisiert wird.
{% endalert %}

## 2. Schritt: LINE-Kanal integrieren

Nachdem der Integrationsprozess abgeschlossen ist, zieht Braze automatisch die LINE-Follower dieses Kanals in Braze ein. Für alle LINE-IDs, die bereits mit einem Braze-Nutzerprofil verknüpft sind, wird jedes Profil mit dem Status „abonniert" aktualisiert, und alle verbleibenden LINE-IDs erzeugen anonyme Nutzer:innen. Außerdem werden für neue Follower Ihres LINE-Kanals nicht identifizierte Nutzerprofile erstellt, wenn sie dem Kanal folgen.

### Schritt 2.1: Webhook-Einstellungen bearbeiten

1. Gehen Sie in LINE auf den Tab **Messaging API** und bearbeiten Sie Ihre **Webhook-Einstellungen**:
   - Setzen Sie die **Webhook-URL** auf `https://anna.braze.com/line/events`.
      - Braze ändert diese URL bei der Integration automatisch in eine andere URL, die auf Ihrem Dashboard-Cluster basiert.
   - Aktivieren Sie **Webhook verwenden** und **Erneute Webhook-Zustellung**. <br><br> ![Webhook-Einstellungsseite, um die Webhook-URL zu überprüfen oder zu bearbeiten, „Webhook verwenden", „Erneute Webhook-Zustellung" und „Fehlerstatistik-Aggregation" ein- oder auszuschalten.]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. Notieren Sie sich die folgenden Informationen auf dem Tab **Providers**:

| Informationstyp | Ort |
| --- | --- |
| Anbieter-ID | Wählen Sie Ihren Anbieter und gehen Sie dann zu ***Einstellungen** > **Grundlegende Informationen** |
| Kanal-ID | Wählen Sie Ihren Anbieter und gehen Sie dann zu **Kanäle** > Ihr Kanal > **Grundeinstellungen** |
| Kanalgeheimnis | Wählen Sie Ihren Anbieter und gehen Sie dann zu **Kanäle** > Ihr Kanal > **Grundeinstellungen**. |
| Kanalzugriffs-Token | Wählen Sie Ihren Anbieter und gehen Sie dann zu **Kanäle** > Ihr Kanal > **Messaging-API**. Wenn kein Kanalzugriffs-Token vorhanden ist, wählen Sie **Ausstellen**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="3"}
3. Gehen Sie zu Ihrer Seite **Einstellungen** > **Antworteinstellungen** und führen Sie folgende Schritte aus:
   - Schalten Sie die **Begrüßungsnachricht** aus. Dies kann in Braze über einen Follow-Trigger gehandhabt werden.
   - Schalten Sie **Automatische Antwortnachrichten** aus. Alle getriggerten Nachrichten sollten über Braze erfolgen. Das hindert Sie nicht daran, direkt von der LINE-Konsole aus zu senden.
   - Aktivieren Sie **Webhooks**.

![Seite mit den Antworteinstellungen mit Umschaltern für die Art und Weise, wie Ihr Konto Chats handhabt.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### Schritt 2.2: LINE-Abo-Gruppen in Braze erstellen

1. Rufen Sie die Braze Technology Partners-Seite für LINE auf und geben Sie die Informationen ein, die Sie auf dem Tab LINE **Providers** notiert haben:
   - Anbieter-ID
   - Kanal-ID
   - Kanalgeheimnis
   - Kanalzugriffs-Token

Wenn Sie in Ihrem LINE-Konto ein IP-Whitelisting hinzufügen möchten, fügen Sie alle IP-Adressen, die für Ihren Cluster in der [IP-Zulassungsliste]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-allowlisting) aufgeführt sind, zu Ihrer Zulassungsliste hinzu.

{% alert important %}
Vergewissern Sie sich während der Integration, dass Ihr Kanalgeheimnis korrekt ist. Wenn es nicht korrekt ist, kann es zu Unstimmigkeiten beim Abo-Status kommen.
{% endalert %}

![LINE-Messaging-Integrationsseite mit Abschnitt „LINE-Integration".]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2. Nach der Verbindung erstellt Braze automatisch eine Braze-Abo-Gruppe für jede LINE-Integration, die erfolgreich zu Ihrem Workspace hinzugefügt wurde. <br><br> Alle Änderungen an Ihrer Follower-Liste (z. B. neue Follower oder Unfollower) werden automatisch in Braze übertragen.

![Abschnitt „LINE-Abo-Gruppen", der eine Abo-Gruppe für den Kanal „LINE" anzeigt.]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## 3. Schritt: Nutzer-IDs abgleichen

Kombinieren Sie die LINE-IDs Ihrer Nutzer:innen mit ihren bestehenden Braze-Nutzerprofilen, indem Sie die Schritte unter [Nutzer-ID-Abgleich](#user-id-reconciliation) ausführen.

## 4. Schritt: Update-Methoden für Nutzer:innen ändern 

Angenommen, Sie haben bereits eine Methode, um Nutzer-Updates an Braze zu übermitteln, dann müssen Sie diese aktualisieren, um das neue Feld `native_line_id` einzubeziehen, damit nachfolgende Nutzer-Updates, die an Braze gesendet werden, dieses Feld enthalten.

Es kann sein, dass in Braze nicht identifizierte Nutzerprofile mit `native_line_id` existieren, die im Rahmen der Synchronisierung des Abo-Status erstellt wurden, oder wenn ein neuer Follower Ihrem Kanal gefolgt ist. 

Wenn ein:e LINE-Nutzer:in in Ihrer Anwendung durch einen [Nutzerabgleich](#user-id-reconciliation) oder auf andere Weise identifiziert wird, können Sie ein potenziell nicht identifiziertes Nutzerprofil in Braze mit dem [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)-Endpunkt ansprechen. Jedes nicht identifizierte Nutzerprofil mit einem `native_line_id` hat auch einen Nutzer-Alias `line_id`, der zum Targeting des zu identifizierenden Nutzerprofils verwendet werden kann.

Hier ist ein Beispiel für eine Payload für `/users/identify`, die auf ein nicht identifiziertes Nutzerprofil mit dem Nutzer-Alias `line_id` abzielt: 

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

Wenn für die von Ihnen angegebene `external_id` kein Nutzerprofil vorhanden ist, wird sie dem nicht identifizierten Nutzerprofil hinzugefügt, sodass es identifiziert wird. Wenn für die `external_id` ein Nutzerprofil existiert, werden alle Attribute, die ausschließlich auf dem nicht identifizierten Nutzerprofil vorhanden sind, in das bekannte Nutzerprofil kopiert, einschließlich `native_line_id` und dem Abo-Status der Nutzer:innen.

Sie können LINE-Nutzer:innen, die in Ihrer Anwendung bekannt sind, über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)-Endpunkt aktualisieren, indem Sie ihre externen Bezeichner und `native_line_id` übergeben. Wenn für eine:n Nutzer:in bereits ein nicht identifiziertes Nutzerprofil existiert und dieselbe `native_line_id` über `/users/track` zu einem anderen Nutzerprofil hinzugefügt wird, erbt es alle Abo-Status des nicht identifizierten Nutzerprofils. Es gibt jedoch doppelte Nutzerprofile mit derselben `native_line_id`. Alle nachfolgenden Abo-Updates durch Event-Aktualisierungen werden alle Profile entsprechend aktualisieren. 

{% alert note %}
LINE-Abo-Status werden anhand von `native_line_id` verfolgt, nicht anhand von `external_id`. Wenn beispielsweise das Nutzerprofil von Nutzer:in B mit derselben `native_line_id` wie Nutzer:in A erstellt wird, aber nicht mit derselben `external_id`, erbt Nutzer:in B den LINE-Abo-Status von Nutzer:in A.
{% endalert %}

Hier ist ein Beispiel für eine Payload für `/users/track`, die ein Nutzerprofil anhand der externen Nutzer-ID aktualisiert, um eine `native_line_id` hinzuzufügen: 

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

## 5. Schritt: Profile zusammenführen (optional)

Wie oben beschrieben, besteht die Möglichkeit, dass mehrere Nutzerprofile mit derselben `native_line_id` existieren. Wenn Ihre Update-Methoden doppelte Nutzerprofile erstellen, können Sie mit dem Endpunkt `/user/merge` nicht identifizierte Nutzerprofile mit identifizierten Nutzerprofilen zusammenführen. 

Hier ist ein Beispiel für eine Payload für `/users/merge`, die ein nicht identifiziertes Nutzerprofil mit dem Nutzer-Alias `line_id` als Ziel hat:

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
Mehr über die Verwaltung doppelter Nutzer:innen in Braze erfahren Sie unter [Doppelte Nutzer:innen]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users).
{% endalert %}

## Nutzereinrichtung

LINE ist die maßgebliche Quelle für den Abo-Status der Nutzer:innen. Selbst wenn Sie die LINE-ID einer Nutzer:in haben (`native_line_id`), wird LINE der Nutzer:in keine Nachrichten zustellen, wenn diese:r dem LINE-Kanal, von dem aus Sie senden, nicht folgt.

Um dies zu verwalten, bietet Braze Tools und eine Logik, die eine gut integrierte Nutzerbasis unterstützt, einschließlich der Synchronisierung von Abos und Event-Updates für LINE-Follows und -Unfollows.

### Synchronisierung von Abos und Event-Logik

1. **Abo-Synchronisierungstool:** Dieses Tool wird automatisch nach einer erfolgreichen LINE-Kanalintegration eingesetzt. Verwenden Sie es, um bestehende Profile zu aktualisieren und neue Profile zu erstellen.<br><br>Alle Braze-Nutzerprofile, die eine `native_line_id` haben, die dem LINE-Kanal folgt, werden auf den Abo-Gruppenstatus `subscribed` aktualisiert. Jeder Follower des LINE-Kanals, der kein Braze-Nutzerprofil mit der `native_line_id` hat, erhält:<br><br>- Ein anonymes Nutzerprofil, das mit `native_line_id` erstellt wurde und auf die LINE-ID der dem Kanal folgenden Nutzer:in gesetzt ist <br>- Einen Nutzer-Alias `line_id`, der auf die LINE-ID der dem Kanal folgenden Nutzer:in gesetzt ist <br>- Einen Abo-Gruppenstatus von `subscribed`

{: start="2"}
2. **Event-Updates:** Diese werden verwendet, um den Abo-Status einer Nutzer:in zu aktualisieren. Wenn Braze Event-Updates für den integrierten LINE-Kanal empfängt und es sich um ein Follow-Event handelt, erhält das Nutzerprofil den Abo-Gruppenstatus `subscribed`. Wenn es sich um ein Unfollow-Event handelt, erhält das Nutzerprofil den Abo-Gruppenstatus `unsubscribed`.<br><br>- Alle Braze-Nutzerprofile mit einer passenden `native_line_id` werden automatisch aktualisiert. <br>- Wenn für ein Event kein passendes Nutzerprofil existiert, [erstellt Braze eine:n anonyme:n Nutzer:in]({{site.baseurl}}/line/user_management/).

## Anwendungsfälle

Dies sind Anwendungsfälle, wie Nutzer:innen aktualisiert werden können, nachdem Sie die obigen Einrichtungsschritte ausgeführt haben.

##### Bestehendes Braze-Nutzerprofil folgt bereits dem LINE-Kanal

1. Das Braze-Nutzerprofil wird mit einem `native_line_id`-Attribut aktualisiert. Sein Standard-Abo-Status ist `unsubscribed`.
2. Das Abo-Synchronisierungstool wird ausgeführt, stellt fest, dass die Nutzer:in dem LINE-Kanal folgt, und aktualisiert dann das Nutzerprofil mit dem Abo-Status `subscribed`.
3. Wenn sich der Abo-Status ändert (z. B. wenn die Nutzer:in den Kanal blockiert, entfreundet oder erneut folgt), erhält Braze das Update von LINE und aktualisiert das Nutzerprofil mit der `native_line_id` entsprechend.

##### Bestehendes Nutzerprofil hat den LINE-Kanal blockiert, entfreundet oder entfolgt 

1. Das Braze-Nutzerprofil wird mit einem `native_line_id`-Attribut aktualisiert. Sein Standard-Abo-Status ist `unsubscribed`.
2. Das Abo-Synchronisierungstool stellt fest, dass die Nutzer:in dem LINE-Kanal nicht folgt, und der Abo-Status bleibt auf `unsubscribed`.
3. Wenn die Nutzer:in dem Kanal später folgt, erhält Braze das Update von LINE und aktualisiert das Nutzerprofil mit dem Abo-Status `subscribed`.

##### Nutzerprofil wird nach LINE-Follow erstellt

1. Der Kanal erhält eine:n neue:n LINE-Follower.
2. Braze erstellt ein anonymes Nutzerprofil mit dem Attribut `native_line_id`, das auf die LINE-ID der Follower:in gesetzt ist, und einem Nutzer-Alias `line_id`, der auf die LINE-ID der Follower:in gesetzt ist. Das Profil hat einen Abo-Status von `subscribed`.
3. Die Nutzer:in wird durch den [Nutzerabgleich](#user-id-reconciliation) als Inhaber:in der LINE-ID identifiziert.
  - Das anonyme Nutzerprofil kann über den [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)-Endpunkt identifiziert werden. Spätere Aktualisierungen (über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)-Endpunkt, [CSV-Import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) zu diesem Nutzerprofil können die Nutzer:in über die bekannte `external_id` ansprechen.

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

  - Ein neues Nutzerprofil kann (über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)-Endpunkt, [CSV-Import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) durch Festlegen der `native_line_id` erstellt werden. Dieses neue Profil erbt den Abo-Status des bestehenden anonymen Nutzerprofils. Beachten Sie, dass dies dazu führt, dass sich mehrere Profile dieselbe `native_line_id` teilen. Diese können jederzeit über den Endpunkt `/users/merge` im Rahmen des in [Schritt 5](#step-5-merge-profiles-optional) beschriebenen Prozesses zusammengeführt werden.

##### Nutzerprofil wird vor dem LINE-Follow erstellt

1. Sie gewinnen eine:n neue:n Nutzer:in und senden die Informationen an Braze. Ein neues Nutzerprofil wird erstellt (Profil 1).
2. Die Nutzer:in folgt Ihrem LINE-Konto.
3. Braze empfängt ein Follow-Event und erstellt ein anonymes Nutzerprofil (Profil 2).
4. Die Nutzer:in wird durch den [Nutzerabgleich](#user-id-reconciliation) als Inhaber:in der LINE-ID identifiziert.
5. Sie aktualisieren Profil 1, um das Attribut `native_line_id` festzulegen. Dieses Profil erbt den Abo-Status von Profil 2.
  - Jetzt gibt es zwei Nutzerprofile mit derselben `native_line_id`. Diese können jederzeit über den Endpunkt `/users/merge` im Rahmen des in [Schritt 5](#step-5-merge-profiles-optional) beschriebenen Prozesses zusammengeführt werden.

## Nutzer-ID-Abgleich 

LINE-IDs werden automatisch von Braze empfangen, wenn eine Nutzer:in Ihrem Kanal folgt oder wenn Sie den einmaligen Workflow „Follower synchronisieren" verwenden. LINE-IDs sind auch spezifisch für den Kanal, dem die Nutzer:innen folgen, sodass es unwahrscheinlich ist, dass Nutzer:innen ihre LINE-IDs selbst angeben können.

Es gibt zwei Möglichkeiten, eine LINE-ID mit einem bestehenden Braze-Nutzerprofil zu kombinieren:

- [LINE-Anmeldung](#line-login)
- [Verknüpfung von Nutzerkonten](#user-account-linking)

### LINE-Anmeldung

Diese Methode verwendet Social-Media-Anmeldungen zum Abgleich. Wenn sich eine Nutzer:in bei Ihrer App anmeldet, hat sie die Möglichkeit, mit [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) ein Nutzerkonto zu erstellen oder sich einzuloggen.

{% alert note %}
Um die richtige LINE-ID für jede Nutzer:in zu erhalten, richten Sie LINE Login unter demselben Anbieter ein wie Ihr in Braze integriertes offizielles LINE-Konto oder Ihren LINE-Kanal.
{% endalert %}

1. Rufen Sie die LINE-Entwicklerkonsole auf und [beantragen Sie die Erlaubnis, die E-Mail-Adressen der Nutzer:innen zu erhalten](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission), die sich über LINE Login bei Ihrer App anmelden.

2. Befolgen Sie die entsprechenden Schritte, die von LINE bereitgestellt werden, um LINE Login zu implementieren:<br><br>
  - [Web-App-Anleitungen](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [Native-App-Anleitungen](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>Achten Sie darauf, dass Sie `email` in den für Verifizierungsanfragen [festgelegten Umfang](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes) einbeziehen. 

{: start="3"}
3. Verwenden Sie den [Aufruf „ID-Token verifizieren"](https://developers.line.biz/en/reference/line-login/#verify-id-token), um die E-Mail-Adresse der Nutzer:in zu erhalten. 

4. Speichern Sie die LINE-ID der Nutzer:in (`native_line_id`) im Nutzerprofil mit einer passenden E-Mail in Ihrer Datenbank, oder erstellen Sie ein neues Nutzerprofil mit der E-Mail und der LINE-ID der Nutzer:in.

5. Senden Sie die neuen oder aktualisierten Nutzerinformationen über den [`/user/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users/), [CSV-Import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import) oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/cloud_ingestion/) an Braze.

#### Workflows

##### Bestehende:r Follower verwendet LINE-Anmeldung

**Szenario:** Eine anonyme Nutzer:in wurde bei der ersten Abonnent:innen-Synchronisierung oder nach der Integration durch ein „Follow"-Event erstellt.

1. Die Nutzer:in meldet sich mit LINE Login bei Ihrer App an.
2. LINE liefert Ihnen die E-Mail-Adresse der Nutzer:in.
3. Sie senden Braze die aktualisierte Nutzer:in (das bestehende Nutzerprofil mit dieser E-Mail, um die LINE-ID hinzuzufügen) oder Sie aktualisieren die anonyme Nutzer:in mit der E-Mail.

##### Neue:r Follower verwendet LINE-Anmeldung

**Szenario:** In Braze existiert kein Nutzerprofil mit der LINE-ID der Nutzer:in.

1. Die Nutzer:in meldet sich mit LINE Login bei Ihrer App an.
2. LINE liefert Ihnen die E-Mail-Adresse der Nutzer:in.
3. Sie haben folgende Möglichkeiten:
  - Aktualisieren Sie ein bestehendes Nutzerprofil mit dieser E-Mail, damit es auch die LINE-ID der Nutzer:in enthält.
  - Erstellen Sie ein neues Nutzerprofil mit der E-Mail und der LINE-ID.
4. Wenn die Nutzer:in Ihrem offiziellen LINE-Konto folgt, erhält Braze ein Follow-Event und aktualisiert den Abo-Status der Nutzer:in auf `subscribed`.

### Verknüpfung von Nutzerkonten 

Mit dieser Methode können Nutzer:innen ihr LINE-Konto mit dem Nutzerkonto Ihrer App verknüpfen. Sie können dann Liquid in Braze verwenden, z. B. {% raw %}`{{line_id}}`{% endraw %}, um eine personalisierte URL für die Nutzer:in zu erstellen, die die LINE-ID an Ihre Website oder App weiterleitet, wo sie dann mit einer bekannten Nutzer:in verknüpft werden kann.

1. Erstellen Sie ein aktionsbasiertes Canvas, das auf einer Änderung des Abo-Status basiert und ausgelöst wird, wenn eine Nutzer:in Ihren LINE-Kanal abonniert.<br>![Canvas, das getriggert wird, wenn eine Nutzer:in den LINE-Kanal abonniert.]({% image_buster /assets/img/line/account_link_1.png %})
2. Erstellen Sie eine Nachricht, die Nutzer:innen dazu anregt, sich bei Ihrer Website oder App anzumelden, indem Sie die LINE-ID als Abfrageparameter (über Liquid) übergeben, z. B.:

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3. Erstellen Sie eine Folgenachricht, die den Gutscheincode zustellt.
4. (Optional) Erstellen Sie eine aktionsbasierte Kampagne oder ein Canvas, das ausgelöst wird, wenn die LINE-Nutzer:in identifiziert wird, um den Gutscheincode zu senden. <br>![Eine aktionsbasierte Kampagne, die ausgelöst wird, wenn die LINE-Nutzer:in identifiziert wird.]({% image_buster /assets/img/line/account_link_2.png %})

#### Funktionsweise

Nachdem sich die Nutzer:in angemeldet hat, wird auf Ihrer Website oder App eine Änderung vorgenommen, sodass die Nutzer-ID an Braze zurückgeschickt wird, um sie mit der LINE-ID zu verknüpfen, die als Teil der URL übergeben wurde. Beispiel-Code:

```javascript
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

##### Bestehende:r Nutzer:in folgt Ihrem LINE-Kanal

**Szenario:** Eine bestehende Nutzer:in in Braze folgt Ihrem Kanal auf LINE.

1. LINE sendet Braze ein Follow-Event.
2. Braze erstellt ein anonymes Nutzerprofil mit der LINE-ID, dem `line_id`-Nutzer-Alias und dem LINE-Abo-Gruppenstatus `subscribed`.
3. Die Nutzer:in erhält eine LINE-Nachricht mit einem Link zu Ihrer Website und App und meldet sich an. Das Nutzerprofil ist nun bekannt.
4. Das erstellte anonyme Nutzerprofil wird identifiziert und über den [/users/identify-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) mit dem bekannten Nutzerprofil zusammengeführt. Das bekannte Nutzerprofil enthält nun die LINE-ID und hat den Abo-Status `subscribed`.
5. (Optional) Die Nutzer:in erhält eine LINE-Nachricht mit dem Gutscheincode und Braze protokolliert den Versand im Braze-Nutzerprofil.

## LINE-Testnutzer:innen in Braze erstellen

Sie können Ihren LINE-Kanal testen, bevor Sie den [Nutzerabgleich](#user-id-reconciliation) einrichten, indem Sie ein „Wer bin ich"-Canvas oder eine entsprechende Kampagne erstellen.

1. Richten Sie ein Canvas ein, das die Braze-Nutzer-ID bei einem bestimmten Trigger-Wort zurückgibt. <br><br>Beispiel-Trigger <br><br>![Trigger, um die Kampagne an Nutzer:innen zu senden, die eine eingehende LINE-Nachricht an eine bestimmte Abo-Gruppe gesendet haben.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>Beispielnachricht<br><br>![LINE-Nachricht mit Angabe der Braze-Nutzer-ID.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. In Braze können Sie die Braze-ID verwenden, um nach bestimmten Nutzer:innen zu suchen und sie bei Bedarf zu ändern.

{% alert important %}
Stellen Sie sicher, dass das Canvas keine globale Kontrollgruppe oder Kontrollgruppen hat, die das Senden verhindern.
{% endalert %}