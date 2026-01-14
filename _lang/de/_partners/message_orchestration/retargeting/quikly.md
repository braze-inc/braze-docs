---
nav_title: Quikly
article_title: Quikly
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Quickly, einer Plattform für Dringlichkeitsmarketing, die es Ihnen erlaubt, Konversionen auf Events innerhalb einer Customer Journey von Braze zu beschleunigen."
alias: /partners/quikly/
page_type: partner
search_tag: Partner

---

# Quikly

> [Quikly](https://www.quikly.com), eine Plattform für Dringlichkeits-Marketing, nutzt die Psychologie, um Verbraucher:in zu motivieren, so dass Marken die Resonanz auf ihre wichtigsten Marketing-Initiativen sofort erhöhen können.

_Diese Integration wird von Quikly gepflegt._

## Über die Integration

Die Partnerschaft von Braze und Quikly erlaubt es Ihnen, Konversionen auf Events innerhalb einer Customer Journey von Braze zu beschleunigen. Quikly nutzt die Psychologie der Dringlichkeit, um Verbraucher:in auf unterhaltsame - und sofortige - Weise zu motivieren. Marken können Quikly zum Beispiel nutzen, um sofort neue E-Mail- und SMS-Abonnenten direkt in Braze zu akquirieren oder um andere wichtige Marketing-Ziele wie das Herunterladen Ihrer mobilen App zu motivieren.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Schnelles Konto | Um die Vorteile dieser Partnerschaft nutzen zu können, benötigen Sie ein Partnerkonto [bei Quikly](https://www.quikly.com). |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track`, `subscription.status.set`, `users.export.ids`, und `subscription.status.get`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Quikly API-Schlüssel (optional) | Ein API-Schlüssel von Quikly, der von Ihrem Client Success Manager bereitgestellt wird (nur Webhook). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Quikly ermöglicht es Marken, die Akquise per E-Mail oder SMS zu beschleunigen und motiviert Abonnent:innen, First-Party-Daten direkt in Braze bereitzustellen. Sie können Braze auch verwenden, um abgelaufene Kund:innen mit einer Quikly-Aktivierung anzusprechen, die diese Zielgruppe reaktiviert und an sich bindet. Außerdem können Marketer diese Integration nutzen, um bestimmte Customer Journey Events mit eindeutigen Belohnungsstrukturen zu incentivieren. 

Zum Beispiel:
 - Bauen Sie über Tage hinweg Vorfreude und Engagement auf, indem Sie Verbraucher:in für die Chance auf aufregende Rewards mit [Quikly Hype](https://www.quikly.com/urgency-marketing/platform/product-overview/hype) opt-in gewinnen. First-Party-Daten werden automatisch an Braze gepusht.
 - Beschleunigen Sie die Gewinnung neuer E-Mail- und SMS-Abonnenten mit eindeutigen Realtime-Angeboten, die auf der Reaktionsgeschwindigkeit der Verbraucher:in, dem Ranking mit anderen, dem Zufallsprinzip oder vor Ablauf der Zeit oder der Mengen basieren, mit [Quikly Swap](https://www.quikly.com/urgency-marketing/platform/product-overview/swap).
 - Motivieren Sie bestimmte Schritte in der Customer Journey mit eindeutigen Belohnungsstrukturen über Webhooks.
 - Wenden Sie angepasste Attribute oder Events auf das Profil des Nutzers an, wenn dieser an einer Quikly-Aktivierung teilnimmt.

## Integration

Im Folgenden finden Sie vier verschiedene Integrationen: E-Mail-Erfassung, SMS-Erfassung, angepasste Attribute und Webhooks. Welche Integration Sie wählen, hängt von Ihrer Quikly Aktivierung und Ihrem Anwendungsfall ab.

{% tabs %}
{% tab E-Mail-Akquise %}

### E-Mail-Akquise

Wenn Ihre Quikly-Aktivierungen E-Mail-Adressen oder Profildaten von Kunden erfassen, müssen Sie Quikly lediglich Ihren REST API-Schlüssel und Endpunkt mitteilen. Quikly wird Ihr Markenkonto so konfigurieren, dass diese Daten an Braze weitergegeben werden. Wenn Sie zusätzliche Nutzer:innen-Attribute wünschen, erwähnen Sie dies, wenn Sie die Zugangsdaten für die API an Quikly übermitteln.

Im Folgenden finden Sie eine Übersicht darüber, wie Quikly diesen Arbeitsablauf durchführt.
1. Nach der Teilnahme an einer Quikly-Aktivierung plant Quikly einen Zeitplan für die Suche nach Nutzern:innen mit Hilfe der [Export-API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/), um zu sehen, ob ein Nutzer:innen mit einer bestimmten `email_address` existiert.
2. Loggen Sie den Nutzer:innen ein oder aktualisieren Sie ihn.
  - Wenn der Nutzer:in existiert:
    - Erstellen Sie kein neues Profil.
    - Falls gewünscht, kann Quikly ein angepasstes Attribut im Profil des Nutzers protokollieren, um anzuzeigen, dass der Nutzer:innen an der Aktivierung teilgenommen hat.
  - Wenn der Nutzer:in nicht existiert:
    - Quikly erstellt über den Braze [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ein reines Alias-Profil, wobei die E-Mail des Nutzers als Nutzer-Alias festgelegt wird, um diesen Nutzer in Zukunft zu referenzieren (da der Nutzer keine externe ID hat).
    - Falls gewünscht, kann Quikly angepasste Events protokollieren, um anzuzeigen, dass dieses Profil an der Quikly-Aktivierung teilgenommen hat.

{% details /benutzer/tracking anfrage %}

#### Anfrage-Header
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

Quikly Aktivierungen können Mobilfunknummern direkt von Kund:innen sammeln und ein neues SMS Abo einrichten. Um diese Integration zu aktivieren, stellen Sie Ihrem Quikly Client Success Manager die `subscription_group_id` zur Verfügung. Sie können auf die `subscription_group_id` einer Abo-Gruppe zugreifen, indem Sie zur Seite **Abo-Gruppe** navigieren.

Quikly führt eine Abo-Suche anhand der Telefonnummer des Kunden durch und schreibt ihm bei der Aktivierung automatisch gut, wenn bereits ein SMS-Abonnement besteht. Andernfalls wird ein neues Abo eingeleitet, und nachdem der Status des Abos überprüft wurde, wird dem Kunden eine Gutschrift erteilt.

Hier sehen Sie den kompletten Arbeitsablauf, wenn eine Kund:in ihre Handynummer und ihre Zustimmung über Quikly angibt:
1. Quikly führt eine Abo-Suche anhand des [Abo-Gruppenstatus]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) durch, um festzustellen, ob ein bestimmtes `phone` bei einem `subscription_group_id` abonniert ist. Wenn ein Abo besteht, schreiben Sie dem Nutzer:innen in der Quikly-Aktivierung gut. Es sind keine weiteren Maßnahmen erforderlich.
2. Quikly führt mit dem [Endpunkt Benutzerprofil nach Bezeichner exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) eine Suche nach Nutzer:innen durch, um festzustellen, ob ein Benutzerprofil mit einem bestimmten `email_address` existiert. Wenn kein Nutzer existiert, erstellen Sie über den Braze [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ein reines Nutzer-Alias-Profil, wobei Sie die E-Mail des Nutzers als Nutzer-Alias festlegen, um diesen Nutzer in Zukunft zu referenzieren (da der Nutzer keine externe ID hat).
3. Aktualisieren Sie den Abo-Status über den [Endpunkt Status der Abo-Gruppe des Nutzers:innen aktualisieren.]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)

Um bestehende Double Opt-in SMS Abo-Workflows zu unterstützen, kann Quikly anstelle des oben beschriebenen Workflows ein angepasstes Event an Braze senden. In diesem Fall wird das Update des Abo-Status nicht direkt durchgeführt, sondern das [angepasste Event triggert den Double Opt-in Prozess]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/) und der Abo-Status wird regelmäßig überwacht, um zu überprüfen, ob der Nutzer:in vollständig opt-in ist, bevor er in der Quikly Aktivierung gutgeschrieben wird.

{% alert important %}
Braze empfiehlt, bei der Erstellung neuer Nutzer:innen über den Endpunkt `/users/track` eine Verzögerung von etwa 2 Minuten einzuhalten, bevor Nutzer:innen der entsprechenden Abo-Gruppe hinzugefügt werden, damit Braze Zeit hat, das Nutzerprofil vollständig zu erstellen.
{% endalert %}

{% details Ausführliche /subscription/status/set Anfrage %}
#### Anfrage-Header
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

Je nach Ihrer Braze-Implementierung möchten Sie vielleicht, dass Ereignisse innerhalb der Quikly-Aktivierung zur weiteren Verarbeitung durch Braze kaskadiert werden. Sie können zum Beispiel ein angepasstes Attribut anwenden, das darauf basiert, welche Stufe oder welcher Anreiz bei der Quikly-Aktivierung erreicht wurde, so dass Sie die entsprechende Content-Card anzeigen können, wenn der Benutzer Ihre App öffnet oder sich auf Ihrer Website einloggt. Quikly wird direkt mit Ihnen zusammenarbeiten, um diese Integrationen zu implementieren.

{% endtab %}
{% tab Webhooks %}
### Webhooks
Verwenden Sie Webhooks, um Anreize für bestimmte Events in der Customer Journey zu triggern. Wenn Sie beispielsweise ein Braze-Ereignis für den Fall haben, dass sich ein Nutzer bei Ihrer App anmeldet, Push-Benachrichtigungen einschaltet oder Ihren Shop-Locator verwendet, können Sie einen Webhook verwenden, um ein angepasstes Angebot für diesen Nutzer auf der Grundlage der Konfiguration einer bestimmten Quikly-Aktivierung zu triggern. Sie können z.B. die ersten X Nutzer:innen, die eine Aktion ausführen (z.B. sich bei Ihrer App anmelden), mit einem angepassten Angebot belohnen oder ein Angebot bereitstellen, dessen Wert mit zunehmender Zeit abnimmt, um eine sofortige Reaktion zu motivieren.

### Erstellen Sie einen Quikly-Webhook in Braze

Um eine Quikly Webhook-Vorlage für künftige Kampagnen oder Canvase zu erstellen, navigieren Sie in der Braze-Plattform zu **Templates** > **Webhook-Vorlagen**. 

Wenn Sie eine einmalige Quikly-Webhook-Kampagne erstellen oder ein bestehendes Template verwenden möchten, wählen Sie bei der Erstellung einer neuen Kampagne **Webhook** in Braze aus.

Wählen Sie **Leeres Template** aus und geben Sie Folgendes für die Webhook-URL und den Body der Anfrage ein:
- **Webhook URL**: https://api.quikly.com/webhook/braze
- **Körper der Anfrage**: JSON Schlüssel-Wert-Paare

#### Kopfzeilen der Anfrage und Methode

Quikly benötigt eine `HTTP Header` für die Autorisierung.

- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Autorisierung**: Überbringer [PARTNER_AUTHORIZATION_HEADER]
  - **Content-Typ**: application/json

#### Anfragetext

Auswählen ***JSON Schlüssel-Wert-Paare*** und fügen Sie die folgenden Paare hinzu:
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### Vorschau auf Ihre Anfrage

Eine Vorschau Ihrer Anfrage finden Sie im Panel **Vorschau** oder auf dem Tab `Test`, wo Sie einen zufälligen Nutzer, einen bestehenden Nutzer:innen auswählen oder Ihren eigenen anpassen können, um Ihren Webhook zu testen.

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}

{% endtab %}
{% endtabs %}

## Support
Wenden Sie sich bei Fragen an Ihren Client Success Manager bei Quikly.


