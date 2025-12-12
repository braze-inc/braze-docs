---
nav_title: "Abo-Gruppen"
article_title: SMS und RCS Abo-Gruppen
page_order: 1
description: "Dieser referenzierte Artikel behandelt Abo-Gruppen, Abo-Status und die Einrichtung von Abo-Gruppen für SMS-, MMS- und RCS-Kanäle."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS
  
---

# SMS und RCS Abo-Gruppen

> Abo-Gruppen sind die Grundlage für den Versand von SMS-, MMS- und RCS-Nachrichten über Braze. Eine Abo-Gruppe ist eine Sammlung von [Absendern]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) (wie RCS-verifizierte Absender, SMS Shortcodes, SMS Langcodes oder alphanumerische SMS Absender IDs), die für eine bestimmte Art von Messaging verwendet werden. Wenn eine Marke beispielsweise plant, sowohl Transaktions- als auch Werbe-SMS zu versenden, müssen Sie in Ihrem Braze-Dashboard zwei Abonnementgruppen mit separaten Pools von Sende-Telefonnummern einrichten.

## Status der Abo-Gruppe

Es gibt zwei Abo-Status für SMS- und RCS-Nutzer:innen: `subscribed` und `unsubscribed`. Der Abo-Status eines Nutzers befindet sich auf der Ebene der Abo-Gruppe und wird nicht von allen Abo-Gruppen gemeinsam genutzt. Das bedeutet, dass ein Nutzer:in einer transaktionalen Abo-Gruppe `subscribed` sein kann, aber `unsubscribed` in einer Aktions-Gruppe. Für Marken stellt diese Trennung der Zustände sicher, dass sie weiterhin relevante SMS- und RCS-Nachrichten an ihre Nutzer:innen senden können.

| Status | Definition |
| --------- | ---------- |
| Abonniert | Nutzer:innen haben ausdrücklich bestätigt, dass sie SMS und RCS von einer bestimmten Abo-Gruppe erhalten möchten. Ein:e Nutzer:in kann entweder abonniert werden, indem sein oder ihr Abonnementstatus über die Braze-Abonnement-API aktualisiert wird, oder indem er oder sie eine Antwort mit einem Opt-in-Schlüsselwort per SMS sendet. Ein Nutzer:in muss bei einer Abo-Gruppe für SMS oder RCS abonniert sein, um SMS, RCS oder beides zu erhalten. |
| Abgemeldet | Der Nutzer:in hat sich ausdrücklich gegen Messaging von Ihrer SMS- und RCS-Abo-Gruppe und den Abo-Telefonnummern innerhalb der Abo-Gruppe entschieden. Sie können sich abmelden, indem sie eine Antwort mit einem Opt-in-Schlüsselwort senden, oder eine Marke kann Nutzer:innen über die [Braze-Abo-API]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) abmelden. Nutzer:innen, die sich von einer Abo-Gruppe für SMS und RCS abgemeldet haben, erhalten keine SMS oder RCS mehr von sendenden Telefonnummern, die zu dieser Abo-Gruppe gehören.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Den Status eines Nutzer:in festlegen

Wenn eine Rufnummer in einem Nutzerprofil aktualisiert wird, erbt die neue Rufnummer den Abo-Gruppenstatus des Nutzers oder der Nutzerin. Wenn die Telefonnummer auf eine Nummer aktualisiert wird, die bereits in Braze existiert, wird der Abonnementstatus dieser bestehenden Telefonnummer übernommen.

Wenn beispielsweise Nutzer:in A eine Telefonnummer hat, die mehreren Abonnementgruppen zugeordnet ist, und diese Telefonnummer dann zu Nutzer:in B hinzugefügt wird, wird Nutzer:in B denselben Abonnementgruppen zugeordnet. Um zu verhindern, dass ein Nutzer:innen die bestehenden Abos erbt, können Sie die Abo-Gruppen der alten Nummer über die Braze REST API zurücksetzen, sobald ein Nutzer:innen seine Nummer ändert. Wenn sich mehrere Nutzer:innen diese Telefonnummer teilen, werden sie alle abgemeldet.

Um den Status der Abo-Gruppe eines Nutzers:innen festzulegen, verwenden Sie eine der folgenden Methoden:

- **Rest-API:** Nutzerprofile können programmatisch über den Endpunkt [\`/subscription/status/set\`]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) mit Hilfe der Braze REST API eingestellt werden.
- **SDK-Integration** Nutzer:innen können einer E-Mail- oder SMS- und RCS-Abo-Gruppe über die Methode `addToSubscriptionGroup` für [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) oder [Internet](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup) hinzugefügt werden.
- **Wird automatisch beim Opt-in/Opt-out des Nutzers oder der Nutzerin verarbeitet:** Wenn Nutzer:innen ein Standard Opt-in oder Opt-out [Schlüsselwort]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/) eingeben, setzt und aktualisiert Braze automatisch ihren Abo-Status.
- **Nutzerimport**: Nutzer:innen können über **Benutzer importieren** zu E-Mail- oder SMS- und RCS-Abo-Gruppen hinzugefügt werden. Wenn Sie den Status der Abonnementgruppe aktualisieren, müssen Sie diese beiden Spalten in Ihrer CSV-Datei haben: `subscription_group_id` und `subscription_state`. Weitere Informationen finden Sie unter [Benutzerimport]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status).

### Prüfen der Gruppe eines Nutzers:in

Um die Abo-Gruppe eines Nutzers:innen zu überprüfen, verwenden Sie eine der folgenden Methoden:

- **Benutzerprofil:** Auf einzelne Nutzerprofile können Sie über das Braze-Dashboard zugreifen, indem Sie in der Seitenleiste die Option **Nutzersuche** auswählen. Hier können Sie Benutzerprofile nach E-Mail-Adresse, Telefonnummer oder externer Benutzer-ID abrufen. Innerhalb eines Nutzerprofils können Sie auf dem Tab Engagement die SMS- und RCS-Abo-Gruppen eines Nutzers:innen einsehen. 
- **Rest-API:** Die Abonnementgruppen der einzelnen Benutzerprofile können über den [Endpunkt Abonnementgruppen des Benutzers auflisten]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) oder den [Endpunkt Status der Abonnementgruppen des Benutzers auflisten]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) mit Hilfe der Braze REST API angezeigt werden. 

## Versenden von Nachrichten mit einer Abo-Gruppe

Um eine SMS- oder RCS-Kampagne über Braze einzuführen, wählen Sie eine Abo-Gruppe aus dem Dropdown-Menü **SMS/MMS/RCS-Varianten** aus. Nach der Auswahl wird Ihrer Kampagne oder Ihrem Canvas automatisch ein Zielgruppenfilter hinzugefügt, der sicherstellt, dass nur Nutzer `subscribed`, die der ausgewählten Abonnementgruppe angehören, zur Zielgruppe gehören.

{% alert important %}
In Übereinstimmung mit den internationalen [Telekommunikationsvorschriften und -richtlinien]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) wird Braze niemals SMS oder RCS an Nutzer:in senden, die nicht die ausgewählte Abo-Gruppe abonniert haben.  
{% endalert %}

![SMS-Editor mit geöffnetem Abo-Gruppen-Dropdown und der Markierung "Messaging Dienst A für SMS" durch den Nutzer:innen.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Enablement von Abo-Gruppen

Um Abo-Gruppen für SMS, MMS oder RCS zu aktivieren, referenzieren Sie auf Folgendes:

{% tabs local %}
{% tab SMS %}
Während Ihres SMS-Onboarding-Prozesses wird ein Braze Onboarding-Manager Abonnementgruppen für Ihr Dashboard-Konto einrichten. Er wird mit Ihnen zusammen festlegen, wie viele Abonnementgruppen Sie benötigen, und die entsprechenden Telefonnummern für den Versand zu Ihren Abonnementgruppen hinzufügen. Der Zeitrahmen für die Einrichtung einer Abonnementgruppe hängt von der Art der Telefonnummern ab, die Sie hinzufügen möchten. Shortcode-Anwendungen können beispielsweise zwischen 8 bis 12 Wochen dauern, während Langcodes innerhalb eines Tages eingerichtet werden können. Wenn Sie Fragen zur Einrichtung Ihres Braze-Dashboards haben, wenden Sie sich an Ihren Braze-Vertreter, um Unterstützung zu erhalten.  
{% endtab %}

{% tab MMS %}
Um eine MMS-Nachricht senden zu können, muss mindestens eine Nummer in Ihrer Abonnementgruppe für den Versand von MMS aktiviert sein. Dies wird durch einen Tag angezeigt, der sich neben der Abo-Gruppe befindet. 

![Abo-Gruppe mit hervorgehobenem "Messaging Dienst A für SMS" in der Auswahlliste. Dem Entry ist der Tag „MMS“ vorangestellt.]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Ein RCS-überprüfter Sender muss in Ihrer Abo-Gruppe vorhanden sein, bevor Sie eine RCS-Nachricht senden können. 

Es gibt zwei Möglichkeiten, einen RCS-überprüften Sender hinzuzufügen:
- Zu einer bestehenden Abo-Gruppe hinzufügen
- Erstellen Sie eine neue RCS Abo-Gruppe
Die Wahl hängt weitgehend von den RCS Anwendungsfällen ab, an denen Sie interessiert sind. 

Abhängig von Ihrer Integration kann Braze RCS-überprüfte Absender zu Ihren bestehenden SMS-Abo-Gruppen hinzufügen oder neue Abo-Gruppen für Sie einrichten. In jedem Fall wird Ihr Customer-Success-Manager:in Sie durch ein nahtloses und effizientes Upgraden des SMS-Verkehrs leiten.
{% endtab %}
{% endtabs %}

## Migration des SMS-Verkehrs zu RCS

Wenn Sie über getrennte Abo-Gruppen für SMS und RCS verfügen, können Sie Nutzer:innen in einem einzigen Schritt per Canvas von SMS zu RCS migrieren. 

Braze empfiehlt, das Senden von RCS an eine kleinere Anzahl von Nutzern zu testen und im Laufe der Zeit weitere Nutzer:innen in die RCS Abo-Gruppe zu migrieren. Wenn Sie z.B. 1.000.000 Nutzer in einer SMS-Abo-Gruppe haben, könnte dies so aussehen, dass Sie zunächst alle Nutzer:innen in die neue Abo-Gruppe migrieren und dann eine kleinere Zielgruppe von 50.000 bis 100.000 (5-10%) segmentieren, um die RCS Nachrichten zu testen.

### Schritt 1: Erstellen Sie ein Canvas und füllen Sie den Zeitplan für den Eingang aus.

Erstellen Sie ein Canvas und geben Sie ihm einen leicht zu identifizierenden Namen (z.B. "SMS-RCS Abo-Gruppe Nutzer:innen"). Dann planen Sie die Kampagne, wann immer es Ihnen passt.

### Schritt 2: Definieren Sie Ihre Zielgruppe

Definieren Sie Ihre Zielgruppe mit einer der folgenden Methoden. Gehen Sie dann zum Schritt **Sendeeinstellungen** und wählen Sie **Nutzer:in, die Abonnent:in oder Opt-in sind**.

| Methode                          | Beschreibung                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Ein Segment erstellen**         | Erstellen Sie ein Segment, das alle Nutzer:innen einer Abo-Gruppe oder eine Teilmenge mit Hilfe von Segmentierungsfiltern (e.g., zufällige 5-10%) umfasst. Segmente werden vor jedem Versand aktualisiert, um Ihre aktuelle Nutzer:innen-Basis widerzuspiegeln.        |
| **Kampagne oder Canvas Filter anwenden** | Verfeinern Sie die Zielgruppe im **Target Audience-Schritt** Ihrer Kampagne oder Ihres Canvas. Passen Sie die Targeting-Optionen an, ohne die Seite zu verlassen, um noch flexibler zu sein.                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Schritt 3: Konfigurieren Sie einen Schritt zum Nutzer:in Update

Fügen Sie einen Nutzer:innen-Update-Schritt zu Ihrem Canvas hinzu. Im Schritt Öffnen Sie den **erweiterten JSON-Editor** und geben Sie Folgendes ein (für das Feld eindeutiger Bezeichner für Nutzer:innen empfehlen wir die Verwendung des Feldes `braze_id` ):

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

!["User Update Object", das den zuvor angegebenen JSON Code enthält.]({% image_buster /assets/img/sms/user_update_object.png %})

### Schritt 4: Testen Sie das Canvas

Wir empfehlen Ihnen dringend, [Ihr Canvas zu testen]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/), um sicherzustellen, dass es wie erwartet funktioniert, bevor Sie es an Ihre breitere Zielgruppe senden.

### Schritt 5: Starten Sie Ihr Canvas

Nachdem Sie Ihr Canvas erfolgreich getestet haben, starten Sie es für Ihre Nutzer:innen!

Um sich zu vergewissern, dass Ihre Nutzer:innen erfolgreich migriert wurden, empfehlen wir, einige einzelne Nutzerprofile zu überprüfen, die aktualisiert wurden. Suchen Sie auf dem Tab **Engagement** nach **Kontakteinstellungen** und scrollen Sie, um die Abo-Gruppen zu sehen, die der Nutzer:in abonniert hat. Das Umschalten der RCS Abo-Gruppe sollte jetzt aktiviert sein.
