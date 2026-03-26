---
nav_title: "Abo-Gruppen"
article_title: SMS und RCS Abo-Gruppen
page_order: 1
description: "Dieser Referenzartikel behandelt Abo-Gruppen, Abo-Status und die Einrichtung von Abo-Gruppen für SMS-, MMS- und RCS-Kanäle."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS
  
---

# SMS und RCS Abo-Gruppen

> Abo-Gruppen sind die Grundlage für den Versand von SMS-, MMS- und RCS-Nachrichten über Braze. Eine Abo-Gruppe ist eine Sammlung von [Absendern]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) (wie RCS-verifizierte Absender, SMS-Shortcodes, SMS-Langcodes oder alphanumerische SMS-Absender-IDs), die für eine bestimmte Art von Messaging verwendet werden. Wenn eine Marke beispielsweise plant, sowohl Transaktions- als auch Werbe-SMS zu versenden, müssen in Ihrem Braze-Dashboard zwei Abo-Gruppen mit separaten Pools von Sende-Telefonnummern eingerichtet werden.

## Status der Abo-Gruppe

Es gibt zwei Abo-Status für SMS- und RCS-Nutzer:innen: `subscribed` und `unsubscribed`. Der Abo-Status einer Nutzerin oder eines Nutzers befindet sich auf der Ebene der Abo-Gruppe und wird nicht über Abo-Gruppen hinweg geteilt. Das bedeutet, dass ein:e Nutzer:in in einer transaktionalen Abo-Gruppe `subscribed` sein kann, aber `unsubscribed` in einer Aktions-Gruppe. Für Marken stellt diese Trennung der Status sicher, dass sie weiterhin relevante SMS- und RCS-Nachrichten an ihre Nutzer:innen senden können.

| Status | Definition |
| --------- | ---------- |
| Abonniert | Nutzer:innen haben ausdrücklich bestätigt, dass sie SMS und RCS von einer bestimmten Abo-Gruppe erhalten möchten. Ein:e Nutzer:in kann entweder abonniert werden, indem der Abo-Status über die Braze-Abo-API aktualisiert wird, oder indem eine Antwort mit einem Opt-in-Schlüsselwort per SMS gesendet wird. Ein:e Nutzer:in muss bei einer SMS- oder RCS-Abo-Gruppe abonniert sein, um SMS, RCS oder beides zu erhalten. |
| Abgemeldet | Der/die Nutzer:in hat sich ausdrücklich gegen Nachrichten von Ihrer SMS- und RCS-Abo-Gruppe und den Sende-Telefonnummern innerhalb der Abo-Gruppe entschieden. Die Abmeldung kann durch das Senden einer Antwort mit einem Opt-out-Schlüsselwort erfolgen, oder eine Marke kann Nutzer:innen über die [Braze-Abo-API]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) abmelden. Nutzer:innen, die sich von einer SMS- und RCS-Abo-Gruppe abgemeldet haben, erhalten keine SMS oder RCS mehr von den Sende-Telefonnummern, die zu dieser Abo-Gruppe gehören.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Den Status eines Nutzers/einer Nutzerin festlegen

Wenn eine Telefonnummer in einem Nutzerprofil aktualisiert wird, erbt die neue Telefonnummer den Abo-Gruppenstatus des Nutzers/der Nutzerin. Wenn die Telefonnummer auf eine Nummer aktualisiert wird, die bereits in Braze existiert, wird der Abo-Status dieser bestehenden Telefonnummer übernommen.

Wenn beispielsweise Nutzer:in A eine Telefonnummer hat, die mehreren Abo-Gruppen zugeordnet ist, und diese Telefonnummer dann zu Nutzer:in B hinzugefügt wird, wird Nutzer:in B denselben Abo-Gruppen zugeordnet. Um zu verhindern, dass ein:e Nutzer:in die bestehenden Abos erbt, können Sie die Abo-Gruppen der alten Nummer über die Braze REST API zurücksetzen, sobald ein:e Nutzer:in die Nummer ändert. Wenn sich mehrere Nutzer:innen diese Telefonnummer teilen, werden sie alle abgemeldet.

Darüber hinaus kann der Abo-Status der Telefonnummer eines/einer ehemaligen Nutzers/Nutzerin übernommen werden – auch wenn diese Telefonnummer derzeit keinem Nutzerprofil zugeordnet ist. Wenn beispielsweise ein:e Nutzer:in die Telefonnummer `123-456-7890` hat, eine Abo-Gruppe abonniert und dann die Telefonnummer gelöscht wird, bleibt der mit `123-456-7890` verknüpfte Abo-Status bestehen und wird angewendet, wenn die Nummer später erneut zugewiesen wird.

Um den Abo-Gruppenstatus eines Nutzers/einer Nutzerin festzulegen, verwenden Sie eine der folgenden Methoden:

- **REST API:** Nutzerprofile können programmgesteuert über den [`/subscription/status/set`-Endpunkt]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) mithilfe der Braze REST API festgelegt werden.
- **SDK-Integration:** Nutzer:innen können einer E-Mail- oder SMS- und RCS-Abo-Gruppe über die Methode `addToSubscriptionGroup` für [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) oder [Internet](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup) hinzugefügt werden.
- **Wird automatisch beim Opt-in/Opt-out verarbeitet:** Wenn Nutzer:innen ein Standard-Opt-in- oder Opt-out-[Schlüsselwort]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/) per SMS senden, setzt und aktualisiert Braze automatisch den Abo-Status.
- **Nutzerimport:** Nutzer:innen können über **Nutzer:innen importieren** zu E-Mail- oder SMS- und RCS-Abo-Gruppen hinzugefügt werden. Wenn Sie den Abo-Gruppenstatus aktualisieren, müssen Sie diese beiden Spalten in Ihrer CSV-Datei haben: `subscription_group_id` und `subscription_state`. Weitere Informationen finden Sie unter [Nutzerimport]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status).

### Die Gruppe eines Nutzers/einer Nutzerin prüfen

Um die Abo-Gruppe eines Nutzers/einer Nutzerin zu überprüfen, verwenden Sie eine der folgenden Methoden:

- **Nutzerprofil:** Auf einzelne Nutzerprofile können Sie über das Braze-Dashboard zugreifen, indem Sie in der Seitenleiste **Nutzersuche** auswählen. Hier können Sie Nutzerprofile nach E-Mail-Adresse, Telefonnummer oder externer Nutzer-ID suchen. Innerhalb eines Nutzerprofils können Sie auf dem Tab „Engagement" die SMS- und RCS-Abo-Gruppen eines Nutzers/einer Nutzerin einsehen. 
- **REST API:** Die Abo-Gruppen einzelner Nutzerprofile können über den [Endpunkt „Abo-Gruppen des Nutzers auflisten"]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) oder den [Endpunkt „Abo-Gruppenstatus des Nutzers auflisten"]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) mithilfe der Braze REST API angezeigt werden. 

## Versenden von Nachrichten mit einer Abo-Gruppe

Um eine SMS- oder RCS-Kampagne über Braze zu starten, wählen Sie eine Abo-Gruppe aus dem Dropdown-Menü **SMS/MMS/RCS-Varianten** aus. Nach der Auswahl wird Ihrer Kampagne oder Ihrem Canvas automatisch ein Zielgruppen-Filter hinzugefügt, der sicherstellt, dass nur Nutzer:innen mit dem Status `subscribed` in der ausgewählten Abo-Gruppe zur Zielgruppe gehören.

{% alert important %}
In Übereinstimmung mit den internationalen [Telekommunikationsvorschriften und -richtlinien]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) wird Braze niemals SMS oder RCS an Nutzer:innen senden, die die ausgewählte Abo-Gruppe nicht abonniert haben.  
{% endalert %}

![SMS-Editor mit geöffneter Dropdown-Liste der Abo-Gruppe und „Messaging-Dienst A für SMS" vom Nutzer/von der Nutzerin hervorgehoben.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Aktivierung von Abo-Gruppen

Um Abo-Gruppen für SMS, MMS oder RCS zu aktivieren, lesen Sie die folgenden Hinweise:

{% tabs local %}
{% tab SMS %}
Während Ihres SMS-Onboarding-Prozesses wird ein Braze-Onboarding-Manager Abo-Gruppen für Ihr Dashboard-Konto einrichten. Er wird mit Ihnen zusammen festlegen, wie viele Abo-Gruppen Sie benötigen, und die entsprechenden Sende-Telefonnummern zu Ihren Abo-Gruppen hinzufügen. Der Zeitrahmen für die Einrichtung einer Abo-Gruppe hängt von der Art der Telefonnummern ab, die Sie hinzufügen möchten. Shortcode-Anträge können beispielsweise zwischen 8 und 12 Wochen dauern, während Langcodes innerhalb eines Tages eingerichtet werden können. Sollten Sie Fragen zur Einrichtung Ihres Braze-Dashboards haben, wenden Sie sich bitte an Ihre Braze-Vertretung, um Support zu erhalten.  
{% endtab %}

{% tab MMS %}
Um eine MMS-Nachricht senden zu können, muss mindestens eine Nummer in Ihrer Abo-Gruppe für den Versand von MMS aktiviert sein. Dies wird durch einen Tag angezeigt, der sich neben der Abo-Gruppe befindet. 

![Dropdown-Menü der Abo-Gruppe mit der Markierung „Messaging-Dienst A für SMS". Dem Eintrag ist der Tag „MMS" vorangestellt.]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Ein RCS-verifizierter Absender muss in Ihrer Abo-Gruppe vorhanden sein, bevor Sie eine RCS-Nachricht senden können. 

Es gibt zwei Möglichkeiten, einen RCS-verifizierten Absender hinzuzufügen:
- Zu einer bestehenden Abo-Gruppe hinzufügen
- Eine neue RCS-Abo-Gruppe erstellen
Die Wahl hängt weitgehend von den RCS-Anwendungsfällen ab, an denen Sie interessiert sind. 

Abhängig von Ihrer Integration kann Braze RCS-verifizierte Absender zu Ihren bestehenden SMS-Abo-Gruppen hinzufügen oder neue Abo-Gruppen für Sie einrichten. In jedem Fall wird Ihr Customer-Success-Manager Sie durch ein nahtloses und effizientes Upgrade des SMS-Verkehrs leiten.
{% endtab %}
{% endtabs %}

## Migration des SMS-Verkehrs zu RCS

Wenn Sie über getrennte Abo-Gruppen für SMS und RCS verfügen, können Sie Nutzer:innen in einem einzigen Schritt per Canvas von SMS zu RCS migrieren. 

Braze empfiehlt, das Senden von RCS zunächst mit einer kleineren Anzahl von Nutzer:innen zu testen und im Laufe der Zeit weitere Nutzer:innen in die RCS-Abo-Gruppe zu migrieren. Wenn Sie beispielsweise 1.000.000 Nutzer:innen in einer SMS-Abo-Gruppe haben, könnte dies so aussehen, dass Sie zunächst alle Nutzer:innen in die neue Abo-Gruppe migrieren und dann eine kleinere Zielgruppe von 50.000 bis 100.000 (5–10 %) segmentieren, um die RCS-Nachrichten zu testen.

### 1. Schritt: Erstellen Sie ein Canvas und füllen Sie den Zeitplan für den Eingang aus

Erstellen Sie ein Canvas und geben Sie ihm einen leicht identifizierbaren Namen (z. B. „SMS-RCS Abo-Gruppe Nutzertransfer"). Planen Sie die Kampagne dann zu einem für Sie passenden Zeitpunkt.

### 2. Schritt: Definieren Sie Ihre Zielgruppe

Definieren Sie Ihre Zielgruppe mit einer der folgenden Methoden. Gehen Sie dann zum Schritt **Sendeeinstellungen** und wählen Sie **Nutzer:innen, die abonniert oder Opt-in sind**.

| Methode                          | Beschreibung                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Ein Segment erstellen**         | Erstellen Sie ein Segment, das alle Nutzer:innen einer Abo-Gruppe oder einer Untergruppe umfasst, indem Sie Segmentierungsfilter verwenden (z. B. zufällig ausgewählte 5–10 %). Segmente werden vor jedem Versand aktualisiert, um Ihre aktuelle Nutzerbasis widerzuspiegeln.        |
| **Kampagne- oder Canvas-Filter anwenden** | Verfeinern Sie die Zielgruppe im Schritt **Zielgruppe** Ihrer Kampagne oder Ihres Canvas. Passen Sie die Targeting-Optionen an, ohne die Seite zu verlassen, um noch flexibler zu sein.                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 3. Schritt: Konfigurieren Sie einen Nutzer-Update-Schritt

Fügen Sie einen Nutzer-Update-Schritt zu Ihrem Canvas hinzu. Öffnen Sie im Schritt den **erweiterten JSON-Editor** und geben Sie Folgendes ein (für das Feld des eindeutigen Nutzerbezeichners empfehlen wir die Verwendung des Feldes `braze_id`):

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

![„User Update Object", das den zuvor genannten JSON-Code enthält.]({% image_buster /assets/img/sms/user_update_object.png %})

### 4. Schritt: Testen Sie das Canvas

Wir empfehlen Ihnen dringend, [Ihr Canvas zu testen]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/), um sicherzustellen, dass es wie erwartet funktioniert, bevor Sie es an Ihre breitere Zielgruppe senden.

### 5. Schritt: Starten Sie Ihr Canvas

Nachdem Sie Ihr Canvas erfolgreich getestet haben, starten Sie es für Ihre Nutzer:innen!

Um zu bestätigen, dass Ihre Nutzer:innen erfolgreich migriert wurden, empfehlen wir, einige einzelne Nutzerprofile zu überprüfen, die aktualisiert wurden. Suchen Sie auf dem Tab **Engagement** nach **Kontakteinstellungen** und scrollen Sie, um die Abo-Gruppen zu sehen, die der/die Nutzer:in abonniert hat. Der Schalter für die RCS-Abo-Gruppe sollte jetzt aktiviert sein.