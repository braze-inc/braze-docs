---
nav_title: "Abo-Gruppen"
article_title: WhatsApp-Abo-Gruppen
page_order: 1
description: "Dieser Artikel beschreibt die WhatsApp-Abonnementgruppen, welche Abonnementstatus angeboten werden und wie Abonnementgruppen eingestellt werden."
page_type: reference
channel:
  - WhatsApp
 
---

# Abo-Gruppen

> WhatsApp-Abonnementgruppen werden bei der Integration von WhatsApp in Ihre App über das **Technologiepartner-Portal** erstellt.

## Abo-Status bei WhatsApp

Bei WhatsApp gibt es den Abo-Status `subscribed` und `unsubscribed`.

| Status | Definition |
| --- | --- |
| Abonniert | Der Benutzer hat ausdrücklich bestätigt, dass er WhatsApp-Nachrichten von einem bestimmten Unternehmen erhalten möchte. Benutzer können sich anmelden, indem sie ihren Anmeldestatus über die Braze-API aktualisieren lassen oder eine Opt-in-Strategie gemäß den Richtlinien von WhatsApp anwenden. |
| Abgemeldet | Jemand hat entweder nicht ausdrücklich sein Einverständnis zum Opt-in erteilt oder der Opt-in wurde ausdrücklich entfernt. <br><br> Benutzer, die sich aus einer WhatsApp-Abonnementgruppe abgemeldet haben, erhalten keine WhatsApp-Nachrichten mehr von sendenden Telefonnummern, die zu der Abonnementgruppe gehören. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Einstellen der WhatsApp-Abonnementgruppen der Benutzer

- **Rest-API:** Nutzerprofile können per Braze REST API über den [Endpunkt`/subscription/status/set`][4] programmbasiert eingestellt werden.
- **Web SDK:** Benutzer können einer E-Mail-, SMS- oder WhatsApp-Abonnementgruppe über die Methode `addToSubscriptionGroup` für [Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/braze/BrazeUser.html#addToSubscriptionGroup-java.lang.String-), [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287) oder [Web][11]] hinzugefügt werden.
- **Nutzerimport**: Benutzer können über **Benutzer importieren** zu E-Mail- oder SMS-Abonnementgruppen hinzugefügt werden. Wenn Sie den Status der Abonnementgruppe aktualisieren, müssen Sie diese beiden Spalten in Ihrer CSV-Datei haben: `subscription_group_id` und `subscription_state`. Weitere Informationen finden Sie unter [Benutzerimport]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status).

### Überprüfen der WhatsApp-Abonnementgruppe eines Benutzers

- **Benutzerprofil:** Auf einzelne Benutzerprofile können Sie über das Braze Dashboard unter **Publikum** > **Benutzer suchen** zugreifen. Hier können Sie Benutzerprofile nach E-Mail-Adresse, Telefonnummer oder externer Benutzer-ID abrufen. Wenn Sie sich in einem Benutzerprofil befinden, können Sie auf der Registerkarte **Engagement** die WhatsApp-Abonnementgruppe eines Benutzers und seinen Status einsehen.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie diese Seite unter **Benutzer** > **Benutzersuche**.
{% endalert %}

- **Rest-API:** Die  Abo-Gruppen einzelner Nutzerprofile können über den [Endpunkt Nutzerspezifische Abo-Gruppen auflisten][9] oder [Endpunkt Nutzerspezifischen Abo-Gruppen-Status auflisten][8] über die REST API von Braze eingesehen werden. 

## Opt-in und Opt-out bei WhatsApp

Gegenwärtig können sich Benutzer auf verschiedene Weise für WhatsApp-Nachrichten anmelden und [sich für oder gegen sie entscheiden]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/), z. B. [per SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), über eine Website, einen WhatsApp-Thread, per Telefon oder persönlich. Beachten Sie, dass Opt-ins obligatorisch sind.

Opt-in-Schlüsselwörter werden für WhatsApp derzeit nicht unterstützt. Ihre Nutzerliste müssen Sie also selber führen. WhatsApp hat einen rückwirkenden Ansatz für Opt-Ins und Ratenlimits. Wenn Nutzer anfangen, Sie zu melden oder zu blockieren, wird Ihr Ratenlimit herabgesetzt. 

## Aktualisierung des nutzerspezifischen Abo-Status im WhatsApp-Canvas {#update-subscription-status}

Je nach verwendeter Opt-in- bzw. Opt-out-Methode können Sie den nutzerspezifischen Abo-Status folgendermaßen aktualisieren:

- Erstellen Sie einen [Braze-to-Braze-Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know), der den Abo-Status per REST API aktualisiert:

![][1]{: style="max-width:90%;"}

Um Wettlaufsituationen zu vermeiden, sollten alle auf den Webhook folgenden Nachrichten in einem zweiten Canvas enthalten sein, der durch Ergebnisse aus dem ersten Canvas getriggert wird (etwa wenn jemand eine Canvas-Variante eingegeben hat und einer Abo-Gruppe in WhatsApp angehört).

- Verwenden Sie den erweiterten JSON-Editor, um das Nutzerprofil mit diesem Template zu aktualisieren: 

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```

![][2]{: style="max-width:90%;"}

{% alert note %}
Änderungen des nutzerspezifischen Abo-Status können bis zu 60 Sekunden dauern.
{% endalert %}

[1]: {% image_buster /assets/img/whatsapp/whatsapp118.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}
[4]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
