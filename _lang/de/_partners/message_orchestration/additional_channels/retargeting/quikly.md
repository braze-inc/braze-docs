---
nav_title: Quikly
article_title: Quikly
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Quickly, einer Plattform für Dringlichkeitsmarketing, die es Ihnen ermöglicht, Konversionen bei Ereignissen innerhalb einer Braze Customer Journey zu beschleunigen."
alias: /partners/quikly/
page_type: partner
search_tag: Partner

---

# Quikly

> [Quikly][1], eine Plattform für Dringlichkeitsmarketing, nutzt die Psychologie, um Verbraucher zu motivieren, so dass Marken die Resonanz auf ihre wichtigsten Marketinginitiativen sofort erhöhen können.

Die Partnerschaft zwischen Braze und Quikly ermöglicht es Ihnen, die Konversionen bei Ereignissen innerhalb einer Braze Customer Journey zu beschleunigen. Quikly nutzt die Psychologie der Dringlichkeit, um die Verbraucher auf unterhaltsame - und sofortige - Weise zu motivieren. Marken können Quikly zum Beispiel nutzen, um sofort neue E-Mail- und SMS-Abonnenten direkt in Braze zu gewinnen oder um andere wichtige Marketingziele wie den Download Ihrer mobilen App zu motivieren.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Schnelles Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Quikly-Markenpartnerkonto][1]. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track`, `subscription.status.set`, `users.export.ids` und `subscription.status.get`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][2]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Quikly API-Schlüssel (optional) | Ein Quikly API-Schlüssel, der von Ihrem Kundenerfolgsmanager bereitgestellt wird (nur Webhook). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Quikly ermöglicht es Marken, die E-Mail- oder SMS-Akquise zu beschleunigen und motiviert Abonnenten dazu, direkt in Braze Erstanbieterdaten bereitzustellen. Sie können Braze auch verwenden, um abgelaufene Kunden mit einer Quikly-Aktivierung anzusprechen, die diese Zielgruppe reaktiviert und an sich bindet. Darüber hinaus können Marketingexperten diese Integration nutzen, um Anreize für bestimmte Customer Journey-Ereignisse mit einzigartigen Belohnungsstrukturen zu schaffen. 

Zum Beispiel:
 - Bauen Sie über Tage hinweg Vorfreude und Engagement auf, indem Sie sich für die Chance auf spannende Belohnungen mit [Quikly Hype][3] anmelden. Daten von Erstanbietern werden automatisch an Braze übermittelt.
 - Beschleunigen Sie die Akquise neuer E-Mail- und SMS-Abonnenten mit einzigartigen Echtzeitangeboten, die auf der Reaktionsgeschwindigkeit eines Verbrauchers, dem Rang im Vergleich zu anderen, dem Zufallsprinzip oder dem Ablauf der Zeit oder der Menge basieren - mit [Quikly Swap][4].
 - Motivieren Sie bestimmte Schritte in der Customer Journey mit einzigartigen Belohnungsstrukturen unter Verwendung von Webhooks.
 - Wenden Sie benutzerdefinierte Attribute oder Ereignisse auf das Profil des Benutzers an, wenn dieser an einer Quikly-Aktivierung teilnimmt.

## Integration

Im Folgenden finden Sie vier verschiedene Integrationen: E-Mail-Erfassung, SMS-Erfassung, benutzerdefinierte Attribute und Webhooks. Welche Integration Sie wählen, hängt von Ihrer Quikly-Aktivierung und Ihrem Anwendungsfall ab.

{% tabs %}
{% tab E-Mail-Akquisition %}

### E-Mail-Akquisition

Wenn Ihre Quikly-Aktivierungen E-Mail-Adressen oder Profildaten von Kunden erfassen, müssen Sie Quikly lediglich Ihren REST-API-Schlüssel und den Endpunkt mitteilen. Quikly wird Ihr Markenkonto so konfigurieren, dass diese Daten an Braze weitergegeben werden. Wenn Sie zusätzliche Benutzerattribute haben möchten, erwähnen Sie dies, wenn Sie Quikly die API-Anmeldeinformationen zur Verfügung stellen.

Im Folgenden finden Sie eine Übersicht darüber, wie Quikly diesen Arbeitsablauf durchführt.
1. Wenn Sie an einer Quikly-Aktivierung teilnehmen, plant Quikly eine Benutzersuche über die [Export-API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/), um zu sehen, ob ein Benutzer mit einer bestimmten `email_address` existiert.
2. Melden Sie den Benutzer an oder aktualisieren Sie ihn.
  - Wenn der Benutzer existiert:
    - Erstellen Sie kein neues Profil.
    - Falls gewünscht, kann Quikly ein benutzerdefiniertes Attribut im Profil des Benutzers protokollieren, um anzuzeigen, dass der Benutzer an der Aktivierung teilgenommen hat.
  - Wenn der Benutzer nicht existiert:
    - Quikly erstellt ein reines Alias-Profil über den [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) von Braze. Dabei wird die E-Mail des Benutzers als Benutzer-Alias festgelegt, um diesen Benutzer in Zukunft referenzieren zu können (da der Benutzer keine externe ID hat).
    - Falls gewünscht, kann Quikly benutzerdefinierte Ereignisse protokollieren, um anzuzeigen, dass dieses Profil an der Quikly-Aktivierung teilgenommen hat.

{% details /benutzer/anforderung verfolgen %}

#### Kopfzeilen der Anfrage
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Anfragetext
```
{
  "attributes": [{
    "_update_existing_only": false,
    "user_alias:": {
      "alias_name": "email@example.com",
      "alias_label: "email"
    },
    "email": "email@example.com"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab SMS-Erfassung %}

### SMS-Abonnements

Quikly-Aktivierungen können Mobiltelefonnummern direkt von Kunden erfassen und ein neues SMS-Abonnement einleiten. Um diese Integration zu aktivieren, stellen Sie Ihrem Quikly Client Success Manager die `subscription_group_id` zur Verfügung. Sie können auf die `subscription_group_id` einer Abonnementgruppe zugreifen, indem Sie zur Seite **Abonnementgruppe** navigieren.

Quikly führt eine Abo-Suche anhand der Telefonnummer des Kunden durch und schreibt ihm bei der Aktivierung automatisch gut, wenn bereits ein SMS-Abonnement besteht. Andernfalls wird ein neues Abonnement eröffnet, und nachdem der Abonnementstatus überprüft wurde, wird dem Kunden eine Gutschrift erteilt.

Hier ist der komplette Arbeitsablauf, wenn ein Kunde seine Handynummer und seine Zustimmung über Quikly angibt:
1. Quikly führt eine Abo-Suche anhand des [Status der Abonnementgruppe]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) durch, um festzustellen, ob ein bestimmtes `phone` bei einem `subscription_group_id` abonniert ist. Wenn ein Abonnement besteht, schreiben Sie es dem Benutzer in der Quikly-Aktivierung gut. Es sind keine weiteren Maßnahmen erforderlich.
2. Quikly führt eine Benutzersuche mit dem [Endpunkt Benutzerprofil nach Kennung exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) durch, um zu sehen, ob ein Benutzerprofil mit einer bestimmten `email_address` existiert. Wenn kein Benutzer vorhanden ist, erstellen Sie über den [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) von Braze ein reines Alias-Profil, wobei Sie die E-Mail des Benutzers als Benutzer-Alias festlegen, um diesen Benutzer in Zukunft zu referenzieren (da der Benutzer keine externe ID haben wird).
3. Aktualisieren Sie den Abonnementstatus über den [Endpunkt Status der Abonnementgruppe des Benutzers aktualisieren]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

Um bestehende Double-Opt-In-SMS-Abonnement-Workflows zu unterstützen, kann Quikly anstelle des obigen Workflows ein benutzerdefiniertes Ereignis an Braze senden. In diesem Fall wird der Status des Abonnements nicht direkt aktualisiert, sondern das [benutzerdefinierte Ereignis löst den Double-Opt-In-Prozess aus]({{site.baseurl}}/user_guide/message_building_by_channel/sms/non_native/double_opt_in/) und der Status des Abonnements wird regelmäßig überwacht, um zu überprüfen, ob der Benutzer sich vollständig angemeldet hat, bevor er in der Quikly-Aktivierung gutgeschrieben wird.

{% alert important %}
Braze empfiehlt, bei der Erstellung neuer Benutzer über den Endpunkt `/users/track` eine Verzögerung von ca. 2 Minuten einzuhalten, bevor die Benutzer zur entsprechenden Abonnementgruppe hinzugefügt werden, damit Braze Zeit hat, das Benutzerprofil vollständig zu erstellen.
{% endalert %}

{% details Ausführliche /subscription/status/set Anfrage %}
#### Kopfzeilen der Anfrage
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Anfragetext
```
{
  "subscription_group_id": "the-id-of-the-subscription-group",
    "subscription_status": "subscribed",
    "phone": "+13135551212"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab Benutzerdefinierte Attribute %}
### Angepasste Attribute

Je nach Ihrer Braze-Implementierung möchten Sie vielleicht, dass Ereignisse innerhalb der Quikly-Aktivierung zur weiteren Verarbeitung durch Braze kaskadiert werden. Sie können zum Beispiel ein benutzerdefiniertes Benutzerattribut anwenden, das darauf basiert, welche Stufe oder welcher Anreiz bei der Quikly-Aktivierung erreicht wurde. So können Sie die entsprechende Inhaltskarte anzeigen, wenn der Benutzer Ihre App öffnet oder sich auf Ihrer Website anmeldet. Quikly wird direkt mit Ihnen zusammenarbeiten, um diese Integrationen zu implementieren.

{% endtab %}
{% tab Webhaken %}
### Webhooks
Verwenden Sie Webhooks, um Anreize für bestimmte Ereignisse in der Customer Journey auszulösen. Wenn Sie beispielsweise ein Braze-Ereignis haben, wenn sich ein Benutzer bei Ihrer App anmeldet, Push-Benachrichtigungen aktiviert oder Ihren Store Locator verwendet, können Sie einen Webhook verwenden, um ein individuelles Angebot für diesen Benutzer auf der Grundlage der Konfiguration einer bestimmten Quikly-Aktivierung auszulösen. Ein Beispiel für eine solche Taktik ist die Belohnung der ersten X Nutzer, die eine Aktion durchführen (z. B. die Anmeldung bei Ihrer App), mit einem individuellen Angebot oder die Bereitstellung eines Angebots, dessen Wert mit zunehmender Zeit abnimmt, um eine sofortige Reaktion zu motivieren.

### Erstellen Sie einen Quikly Webhook in Braze

Um eine Quikly Webhook-Vorlage für zukünftige Kampagnen oder Canvases zu erstellen, navigieren Sie zu **Vorlagen** > **Webhook-Vorlagen** in der Braze-Plattform. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, gehen Sie zu **Engagement** > **Vorlagen & Medien** > **Webhook-Vorlagen**.
{% endalert %}

Wenn Sie eine einmalige Quikly-Webhook-Kampagne erstellen oder eine bestehende Vorlage verwenden möchten, wählen Sie **Webhook** in Braze, wenn Sie eine neue Kampagne erstellen.

Wählen Sie **Leere Vorlage** und geben Sie Folgendes für die Webhook-URL und den Anfragetext ein:
- **Webhook URL**: https://api.quikly.com/webhook/braze
- **Körper der Anfrage**: JSON Schlüssel/Wert-Paare

#### Kopfzeilen der Anfrage und Methode

Quikly benötigt eine `HTTP Header` für die Autorisierung.

- **HTTP-Methode**: POST
- **Kopfzeile der Anfrage**:
  - **Autorisierung**: Überbringer [PARTNER_AUTHORIZATION_HEADER]
  - **Inhalt-Typ**: application/json

#### Anfragetext

Wählen Sie ***JSON Schlüssel/Wertpaare*** und fügen Sie die folgenden Paare hinzu:
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### Vorschau Ihrer Anfrage

Zeigen Sie Ihre Anfrage in der **Vorschau** an oder gehen Sie auf die Registerkarte `Test`, wo Sie einen zufälligen Benutzer, einen vorhandenen Benutzer oder einen eigenen Benutzer auswählen können, um Ihren Webhook zu testen.

{% alert important %}
Denken Sie daran, Ihre Vorlage zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Vorlagen finden Sie in der Liste **Gespeicherte Webhook-Vorlagen**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}

{% endtab %}
{% endtabs %}

## Unterstützen Sie
Wenden Sie sich bei Fragen an Ihren Kundenbetreuer bei Quikly.

[1]: https://www.quikly.com
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.quikly.com/urgency-marketing/platform/product-overview/hype
[4]: https://www.quikly.com/urgency-marketing/platform/product-overview/swap
