---
nav_title: "SMS-Abo-Gruppen"
article_title: SMS-Abo-Gruppen
page_order: 4
description: "Dieser Referenzartikel behandelt SMS-Abonnementgruppen, Abonnementstatus und die Einrichtung von Abonnementgruppen."
page_type: reference
channel:
  - SMS
  
---

# SMS-Abonnementgruppen

> Abonnementgruppen sind die Grundlage für den Versand von SMS und MMS über Braze. Eine Abo-Gruppe ist eine Sammlung von [Absender-Telefonnummern][2] (wie Shortcodes, Langcodes und/oder alphanumerische Absender-IDs), die für eine bestimmte Art von Messaging verwendet werden. Wenn eine Marke beispielsweise plant, sowohl Transaktions- als auch Werbe-SMS zu versenden, müssen Sie in Ihrem Braze-Dashboard zwei Abonnementgruppen mit separaten Pools von Sende-Telefonnummern einrichten.

## SMS-Abo-Status

Es gibt zwei Abonnementstatus für SMS-Benutzer: `subscribed` und `unsubscribed`. Der Abonnementstatus eines Benutzers wird nicht von verschiedenen Abonnementgruppen gemeinsam genutzt, d.h. ein Benutzer kann `subscribed` zu einer Transaktions-Abonnementgruppe, aber `unsubscribed` zu einer Werbe-Abonnementgruppe gehören. Für Marken stellt diese Trennung der Staaten sicher, dass sie weiterhin relevante SMS-Nachrichten an ihre Nutzer senden können.

| Status | Definition |
| --------- | ---------- |
| Abonniert | Der Benutzer hat ausdrücklich bestätigt, dass er SMS von einer bestimmten Abonnementgruppe erhalten möchte. Ein:e Nutzer:in kann entweder abonniert werden, indem sein oder ihr Abonnementstatus über die Braze-Abonnement-API aktualisiert wird, oder indem er oder sie eine Antwort mit einem Opt-in-Schlüsselwort per SMS sendet. Ein:e Nutzer:in muss einer SMS-Abo-Gruppe beitreten, um eine SMS empfangen zu können. |
| Abgemeldet | Der Benutzer hat sich ausdrücklich gegen Nachrichten aus Ihrer SMS-Abonnementgruppe und den Absendertelefonnummern innerhalb der Abonnementgruppe entschieden. Sie können sich abmelden, indem sie eine Antwort mit einem Opt-in-Schlüsselwort senden, oder eine Marke kann Nutzer:innen über die [Braze-Abo-API][4] abmelden. Benutzer, die sich von einer SMS-Abonnementgruppe abmelden, erhalten keine SMS mehr von den Telefonnummern, die zu dieser Abonnementgruppe gehören.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Wie die SMS-Abonnementgruppen der Benutzer festgelegt werden 

- **Rest-API:** Nutzerprofile können über den [`/subscription/status/set`-Endpunkt][4] mit Hilfe der Braze-REST-API programmatisch eingestellt werden.
- **SDK-Integration** Benutzer können mit der Methode `addToSubscriptionGroup` für [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) oder [Web][11]] zu einer E-Mail- oder SMS-Abonnementgruppe hinzugefügt werden.
- **Wird automatisch beim Opt-in/Opt-out des Nutzers oder der Nutzerin verarbeitet:** Wenn Nutzer:innen ein Standard Opt-in oder Opt-out [Schlüsselwort][7]] eingeben, setzt und aktualisiert Braze automatisch ihren Abo-Status.
- **Nutzerimport**: Benutzer können über **Benutzer importieren** zu E-Mail- oder SMS-Abonnementgruppen hinzugefügt werden. Wenn Sie den Status der Abonnementgruppe aktualisieren, müssen Sie diese beiden Spalten in Ihrer CSV-Datei haben: `subscription_group_id` und `subscription_state`. Weitere Informationen finden Sie unter [Benutzerimport]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status).

Wenn eine Rufnummer in einem Nutzerprofil aktualisiert wird, erbt die neue Rufnummer den Abo-Gruppenstatus des Nutzers oder der Nutzerin. Wenn die Telefonnummer auf eine Nummer aktualisiert wird, die bereits in Braze existiert, wird der Abonnementstatus dieser bestehenden Telefonnummer übernommen.

Wenn beispielsweise Nutzer:in A eine Telefonnummer hat, die mehreren Abonnementgruppen zugeordnet ist, und diese Telefonnummer dann zu Nutzer:in B hinzugefügt wird, wird Nutzer:in B denselben Abonnementgruppen zugeordnet. Um zu verhindern, dass ein Nutzer die bestehenden Abos erbt, können Sie die Abo-Gruppen der alten Nummer über die REST API zurücksetzen, wenn ein Nutzer:innen seine Nummer ändert. Wenn sich mehrere Nutzer:innen diese Telefonnummer teilen, werden sie alle abgemeldet.

### Wie Sie die SMS-Abonnementgruppe eines Benutzers überprüfen

- **Benutzerprofil:** Auf einzelne Benutzerprofile können Sie über das Braze-Dashboard zugreifen, indem Sie in der Seitenleiste die Option Benutzersuche wählen. Hier können Sie Benutzerprofile nach E-Mail-Adresse, Telefonnummer oder externer Benutzer-ID abrufen. Wenn Sie sich in einem Benutzerprofil befinden, können Sie auf der Registerkarte Engagement die SMS-Abonnementgruppen eines Benutzers einsehen. 
- **Rest-API:** Die Abo-Gruppe der einzelnen Nutzerprofile kann über den [Endpunkt für die Abo-Gruppe des Nutzers oder der Nutzerin][9] oder den [Endpunkt für den Status der Abo-Gruppe des Nutzers oder der Nutzerin][8] mithilfe der Braze-REST API angezeigt werden. 

## Versenden mit einer Abonnementgruppe

Um eine SMS-Kampagne über Braze zu starten, müssen Sie eine Abonnementgruppe in der Dropdown-Liste auswählen, wie in der folgenden Abbildung gezeigt. Nach der Auswahl wird Ihrer Kampagne oder Ihrem Canvas automatisch ein Zielgruppenfilter hinzugefügt, der sicherstellt, dass nur Nutzer `subscribed`, die der ausgewählten Abonnementgruppe angehören, zur Zielgruppe gehören. Um die internationalen [Telekommunikations-Compliance und -Richtlinien][3] einzuhalten, sendet Braze niemals SMS an Benutzer, die sich nicht bei der ausgewählten Abonnementgruppe angemeldet haben.  

![SMS-Editor mit geöffneter Dropdown-Liste der Abo-Gruppe und „Messaging-Dienst A für SMS“ vom Nutzer oder von der Nutzerin hervorgehoben.][6]

## Einrichtungsprozess

Während Ihres SMS-Onboarding-Prozesses wird ein Braze Onboarding-Manager Abonnementgruppen für Ihr Dashboard-Konto einrichten. Er wird mit Ihnen zusammen festlegen, wie viele Abonnementgruppen Sie benötigen, und die entsprechenden Telefonnummern für den Versand zu Ihren Abonnementgruppen hinzufügen. Der Zeitrahmen für die Einrichtung einer Abonnementgruppe hängt von der Art der Telefonnummern ab, die Sie hinzufügen möchten. Shortcode-Anwendungen können beispielsweise zwischen 8 bis 12 Wochen dauern, während Langcodes innerhalb eines Tages eingerichtet werden können. Wenn Sie Fragen zur Einrichtung Ihres Braze-Dashboards haben, wenden Sie sich an Ihren Braze-Vertreter, um Unterstützung zu erhalten.  

## Abonnementgruppe MMS-Aktivierung

Um eine MMS-Nachricht senden zu können, muss mindestens eine Nummer in Ihrer Abonnementgruppe für den Versand von MMS aktiviert sein. Dies wird durch einen Tag angezeigt, der sich neben der Abo-Gruppe befindet. 

![Dropdown-Menü Abonnementgruppe mit der Markierung "Nachrichtendienst A für SMS". Dem Entry ist der Tag „MMS“ vorangestellt.][10]{: style="max-width:40%"}


[1]: {% image_buster /assets/img/sms/multi_country_subgroups.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/
[4]: {{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[6]: {% image_buster /assets/img/sms/sms_subgroup_select.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[10]: {% image_buster /assets/img/sms/mms_sub_group_tag.png %}
[11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
