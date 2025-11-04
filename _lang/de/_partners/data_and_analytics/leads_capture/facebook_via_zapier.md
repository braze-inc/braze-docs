---
nav_title: Facebook Lead Ads über Zapier
article_title: Facebook Lead Ads über Zapier
description: "Dieser referenzierte Artikel beschreibt die Integration zwischen Braze und Facebook Lead Ads über Zapier, um die Übertragung von Lead-Daten von Facebook an Braze zu automatisieren und so Engagement in Realtime und personalisierte Folgeaktionen zu ermöglichen."
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag: Partner

---

# Facebook Lead Ads über Zapier Integration

> Mit der Facebook Lead Ads Integration über <a href="https://zapier.com/" target="_blank">Zapier</a> können Sie Ihre Leads aus Facebook in Braze importieren und ein angepasstes Event verfolgen, wenn Leads erfasst werden. 

Facebook Lead Ads ist ein Anzeigenformat, das es Unternehmen erlaubt, Lead-Informationen direkt in Facebook zu sammeln. Diese Anzeigen wurden entwickelt, um den Prozess der Lead-Generierung einfach und nahtlos zu gestalten. Indem Sie eine Zapier Integration und Braze nutzen, können Sie die Übertragung von Lead-Daten von Facebook zu Braze automatisieren und so Engagement und personalisierte Folgeaktionen in Realtime ermöglichen. 

## Voraussetzungen

| Anforderungen | Beschreibung |
|---|---|
| Zapier-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Zapier-Konto. Diese Integration erfordert die Verwendung von <a href="https://zapier.com/app/pricing/" target="_blank">Premium-Apps von Zapier</a>. Stellen Sie also sicher, dass Ihr Zapier-Tarif Zugang zu Premium-Apps hat. |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Facebook Leads Zugang</a> | Der Zugang zu Facebook Leads ist für jedes Anzeigenkonto erforderlich, das Sie mit Braze verwenden möchten. |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">Facebook Business Manager:in</a> | Im Rahmen dieser Integration verwenden Sie den Facebook Business Manager, ein zentrales Tool zur Verwaltung der Facebook-Assets Ihrer Marke (z.B. Anzeigenkonten, Seiten und Apps). |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">Facebook Werbekonto</a> | Sie benötigen ein aktives Facebook-Anzeigenkonto, das mit dem Business Manager Ihrer Marke verknüpft ist. <br><br>Vergewissern Sie sich, dass Sie die Berechtigung "Anzeigenkonten verwalten" für jedes Anzeigenkonto haben, das Sie mit Braze verwenden möchten, und dass Sie die Geschäftsbedingungen für Ihr Anzeigenkonto akzeptiert haben. |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">Facebook-Seite</a> | Sie benötigen eine aktive Facebook-Seite, die mit dem Business Manager Ihrer Marke verknüpft ist. <br><br>Vergewissern Sie sich, dass Sie die Berechtigung "Seiten verwalten" für jede Facebook-Seite haben, die Sie mit Braze verwenden möchten. |
| Braze REST Endpunkt | Stellen Sie sicher, dass Sie die [URL REST-Endpunktes]({{site.baseurl}}/api/basics/#api-definitions) kennen. Ihr API-Endpunkt entspricht der Dashboard-URL für Ihre Braze-Instanz. <br><br> Wenn Ihre Dashboard-URL zum Beispiel `https://dashboard-03.braze.com` lautet, ist Ihr Endpunkt `dashboard-03`. |
| Braze REST API-Schlüssel | Stellen Sie sicher, dass Sie über einen Braze REST API-Schlüssel mit `users.track` Berechtigungen verfügen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie eine Lead Ads Kampagne mit einem Sofortformular

Erstellen Sie im Facebook Ads Manager:in eine <a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">Facebook Leads Kampagne und ein Facebook Lead Ads Formular</a>.

Sie können entweder eine E-Mail Adresse oder eine Telefonnummer verwenden, wenn Sie eine Anfrage an den [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) stellen, um das Nutzerprofil zu aktualisieren oder zu erstellen. Fügen Sie daher ein **Kontaktfeld** für **E-Mail** oder **Telefon** in Ihr Lead-Anzeigenformular ein. Wenn Sie Vornamen oder Nachnamen sammeln, erfassen Sie diese separat in Ihrem Formular, anstatt die vollständigen Namen zu verwenden.

### Schritt 2: Verbinden Sie Ihr Facebook-Konto mit Zapier 

#### Schritt 2a: Wählen Sie Ihre Verbindungsmethode in Zapier aus

Gehen Sie in Zapier auf **Apps**, um nach verfügbaren Facebook-Apps zu suchen. Wählen Sie entweder **Facebook Lead Ads** oder **Facebook Lead Ads (für Business-Administratoren)**.

Weitere Informationen zu diesen beiden Methoden, um Ihr Facebook-Konto mit Zapier zu verbinden, finden Sie hier:

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Facebook Lead Ads (für Business Admins)</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">Facebook-Lead-Anzeigen</a>

![]({% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}){: style="max-width:80%;"}

#### Schritt 2b: Zapier zum Leads-Zugang im Facebook Business Manager hinzufügen:in

Gehen Sie in Ihrem Facebook Business Manager im linken Menü auf **Integrationen** > **Leads Access**. Wählen Sie Ihre Facebook-Seite aus, und klicken Sie dann auf **CRMs**. Auf dem Tab CRM wählen Sie **CRMs zuweisen** und fügen **Zapier** hinzu.

![]({% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}){: style="max-width:80%;"}

Die Schritte zur Zuweisung von Zapier als CRM Integration finden Sie in der Dokumentation von Facebook</a>.

### Schritt 3: Erstellen Sie Ihren Zap

#### Schritt 3a: Erstellen Sie den Trigger 

Sobald Sie Ihr Facebook-Konto verbunden haben, können Sie mit der Erstellung eines Zap fortfahren. Wählen Sie als **Auslöser** **Facebook Lead Ads** oder **Facebook Lead Ads (für Business Admins)**, je nachdem, was Sie in Schritt 2 ausgewählt haben. 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}){: style="max-width:80%;"}

Wählen Sie für das **Ereignis** **Neue Leads** > **Weiter**. 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}){: style="max-width:80%;"}

Wählen Sie Ihr Facebook-Konto aus, und **fahren Sie fort**. 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}){: style="max-width:80%;"}

Wählen Sie Ihre Facebook-Seite und das zuvor erstellte Sofortformular aus und klicken Sie auf **Fortfahren**.

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}){: style="max-width:80%;"}

Testen Sie nun diesen Trigger. Nachdem Sie Ihre Formularausgabe validiert haben, wählen Sie **Mit ausgewähltem Datensatz fortfahren**.

#### Schritt 3b: Eine Aktion erstellen

Fügen Sie einen neuen Schritt hinzu und wählen Sie dann **Webhooks von Zapier**. Wählen Sie als nächstes für das Feld **Event** die Option **Angepasste Anfrage** aus und klicken Sie dann auf **Weiter**. 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}){: style="max-width:80%;"}

Zum Schluss richten Sie Ihre angepasste Anfrage ein, indem Sie Felder in Ihre Nutzdaten einfügen. Der folgende Code Snippet zeigt eine Beispiel-Nutzlast. 

```
{
    "attributes": [
        {
            "email": "<insert_email_field>",
            "first_name": "<insert_first_name_field>",
            "last_name": "<insert_last_name_field>",
            "lead_form": "<insert_form_name_field>",
            "fb_campaign": "<insert_campaign_id_field>",
            "fb_ad_set": "<insert_campaign_id_field>",
            "fb_ad": "<insert_campaign_id_field>",
            "email_subscribe": "subscribed",
            "subscription_groups" : [{
                "subscription_group_id": "<subscription_group_id>",
                "subscription_state": "subscribed"
                }
            ]
        }
    ],
    "events": [
        {
            "email": "<insert_email_field>",
            "name": "<insert_custom_event_name>",
            "time": "<insert_timestamp_field>",
            "_update_existing_only": false
        }
    ]
}`
```

Hier sehen Sie ein Beispiel dafür, wie dies in Zapier aussieht:

![]({% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}){: style="max-width:80%;"}

Nachdem Sie Ihren Webhook konfiguriert haben, wählen Sie **Weiter und testen**. Wenn der Test erfolgreich ist, können Sie Ihr Zap veröffentlichen.

### Schritt 4: Testen Sie Ihre Facebook Lead Ads Zap

Um dies End-to-End zu testen, verwenden Sie das Leads Ads Testing Tool von Facebook in Ihrer Facebook Entwickler:in-Konsole. Weitere Informationen finden Sie unter <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">Testen und Fehlerbehebung</a>.

## Verwaltung der Nutzer:innen

Diese Integration ermöglicht es Ihnen, Ihre Facebook-Leads per E-Mail über den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-phone-number) zu attributieren.

* Wenn die E-Mail mit einem bestehenden Nutzerprofil übereinstimmt, aktualisiert Braze das Profil mit den Daten von Facebook-Leads.
* Wenn es mehrere Nutzerprofile mit derselben E-Mail gibt, gibt Braze dem zuletzt aktualisierten Profil mit einer externen ID bei Updates den Vorrang.
* Wenn die externe ID nicht existiert, gibt Braze dem zuletzt aktualisierten Profil mit der passenden E-Mail den Vorrang.
* Wenn für die angegebene E-Mail kein Profil existiert, erstellt Braze ein neues Profil, und es wird ein neues Nutzer:in-Profil mit Alias erstellt. Um die neu erstellten Nutzer:in-Profile zu identifizieren, verwenden Sie den [Endpunkt`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).

{% alert note %}
Sie können auch eine Telefonnummer oder eine externe ID als Teil der Anfrage an Braze verwenden, wenn diese Felder verfügbar sind und der primäre Bezeichner, den Sie für die Integration wünschen. Ändern Sie dazu die Nutzdaten Ihrer Anfrage wie im [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) angegeben.
{% endalert %}

## Fehlersuche

{% details Ich habe den Trigger und die Aktion erfolgreich getestet. Warum kann ich dann meinen Zapier-Zap nicht veröffentlichen? %}
Um diese Integration nutzen zu können, müssen Sie über einen <a href="https://zapier.com/app/pricing/" target="_blank">Zapier-Plan</a> verfügen, der Premium-Apps unterstützt.
{% enddetails %}

{% details Warum werden Facebook-Leads nicht mit Braze synchronisiert? %}
1. Vergewissern Sie sich, dass Sie Administrator-Zugriff auf Ihre Facebook-Seite, Ihr Anzeigenkonto und Ihren Lead-Zugang haben. Verbinden Sie dann Ihr Konto in Zapier erneut.
2. Überprüfen Sie, ob das von Ihnen in Facebook erstellte Sofortformular mit dem in Ihrem Trigger-Schritt ausgewählten Formular übereinstimmt. 
3. Vergewissern Sie sich, dass Sie Zapier den Leads Access zugewiesen haben, indem Sie zu **Facebook Business Manager** > **Integrationen** > **Lead Access** gehen.
{% enddetails %}

{% details Warum sehe ich doppelte Nutzerprofile mit der gleichen E-Mail? %}
Es gibt eindeutige Möglichkeiten, Nutzerprofile in Braze auf der Grundlage ihres [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle) zu erstellen und zu verwalten.

Abhängig von Ihren internen Prozessen und wenn Sie die Erstellung von Kund:in in Braze triggern, kann es zu doppelten Nutzerprofilen kommen, da eine Race-Condition zwischen dem Nutzerprofil, das von der Integration erstellt wird, und dem Nutzerprofil, das in Ihrem System erstellt wird, besteht. In Braze können Sie [Nutzer:innen-Profile zusammenführen]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).
{% enddetails %}

{% details Ich habe kein Zapier-Konto. Wie kann ich Facebook Lead Ads Webhooks in Braze triggern? %}
Wenn Sie Zapier nicht verwenden und auch nicht vorhaben, Zapier zu verwenden, können Sie die Integration direkt von Facebook in Braze erstellen. Weitere Informationen finden Sie in der <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">Dokumentation von Lead Ads</a>.

Um Leads von Facebook abzurufen, verwenden Sie <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">Webhooks</a>. Lesen Sie die <a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">Dokumentation zu Webhooks</a>, um mit Webhooks in Facebook zu beginnen.

Nachdem Sie die Webhooks-URL in Facebook eingerichtet haben, arbeiten Sie mit Ihrem Team zusammen, um den besten Weg zur Weiterleitung der Daten an den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) zu finden. Ähnlich wie bei Zapier empfehlen wir, eine [Anfrage per E-Mail]({{site.baseurl}}/api/endpoints/user_data/post_user_track#example-request-for-updating-a-user-profile-by-phone-number) über den Endpunkt `users/track` zu stellen.
{% enddetails %}

{% alert tip %}
Weitere Tipps zur Fehlerbehebung finden Sie in der <a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">Anleitung zur Fehlerbehebung für Facebook-Leads</a> von Zapier.
{% endalert %}


