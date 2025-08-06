---
nav_title: MyPostcard
article_title: MyPostcard
page_order: 1
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und MyPostcard, die es Ihnen erlaubt, Direkt-Mailing als zusätzlichen Kanal für Ihren CRM-Workflow zu nutzen."
alias: /partners/mypostcard/
page_type: partner
search_tag: Partner

---

# MyPostcard

> [MyPostcard](https://www.mypostcard.com), eine weltweit führende App für Postkarten, ermöglicht es Ihnen, Direkt-Mailing Kampagnen mit Leichtigkeit durchzuführen und bietet eine nahtlose und gewinnbringende Möglichkeit, mit Ihren Kund:in in Kontakt zu treten. 

Nutzen Sie die Integration von MyPostcard und Braze, um Ihren Kund:innen mühelos Print-Mailings zu senden.

## Voraussetzungen

| Anforderung                      | Beschreibung                                                                                                             |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| MyPostcard B2B-Konto           | Um die Vorteile dieser Integration zu nutzen, müssen Sie sich bei MyPostcard registrieren.                                          |
| B2B API-Schlüssel und Zugangsdaten        | Sie finden Ihren API-Schlüssel und die Zugangsdaten im MyPostcard B2B Admin Tool.                                         |
| Genehmigte MyPostcard B2B Kampagne | Um die Vorteile dieser Integration zu nutzen, müssen Sie eine Print-Mailing-Kampagne im MyPostcard B2B-Tool einrichten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Anwendungsfälle

Um Ihre Direkt-Mailing Kampagnen aufzuwerten, müssen Sie über die traditionellen Massenmailings hinausgehen und Print-Mailings nahtlos in Ihre Arbeitsabläufe integrieren. Auf diese Weise können Sie gezielt Kunden:in erreichen, die sich von Ihren E-Mail-Newslettern abgemeldet haben oder deren E-Mails als Spam markiert sind. Mit MyPostcard können Sie mühelos Print-Mailing-Kampagnen direkt über Braze versenden.

- Erstellen Sie in Braze intuitive Workflows, die Print-Mails als leistungsstarken neuen Kanal einbeziehen, ganz ohne technisches Know-how.
- Erschließen Sie das Potenzial personalisierter Drucksachen mit ein paar einfachen Schritten.
- Profitieren Sie von einer unkomplizierten Implementierung, die von einem personalisierten Support durch ein engagiertes Team unterstützt wird.

## Integration

Um MyPostcard zu integrieren, [melden Sie sich an oder registrieren Sie sich](https://www.mypostcard.com/b2b/admin/) und erstellen Sie Ihre erste Kampagne, um sie über [Braze-Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) zu nutzen.

### Schritt 1: Erstellen Sie Ihr Braze-to-Braze-Webhook Template

Erstellen Sie eine MyPostcard-Webhook-Vorlage zur Verwendung in zukünftigen Kampagnen oder Canvase, indem Sie auf der Braze-Plattform zu **Vorlagen** > **Webhook-Vorlagen** navigieren.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/) verwenden, gehen Sie zu **Engagement** > **Templates und Medien** > **Webhook Templates**.
{% endalert %}

Wenn Sie eine einmalige MyPostcard-Webhook-Kampagne erstellen oder eine vorhandene Vorlage verwenden möchten, wählen Sie bei der Erstellung einer neuen Kampagne **Webhook** in Braze aus. Füllen Sie die folgenden Felder aus:

| Feld         | Beschreibung                                               |
|---------------|-----------------------------------------------------------|
| **Webhook-URL** | Die Webhook-URL, wie sie im B2B Admin Tool angezeigt wird.             |
| **Anfragetext** | Rohtext (JSON-Format, zu finden im B2B Admin Tool).        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Anfragemethode und Header

MyPostcard erfordert eine HTTP-Methode zusammen mit den folgenden HTTP-Headern, die in das Template aufgenommen werden müssen.

{% raw %}
<table>
  <thead>
    <tr>
      <th><strong>Feld</strong></th>
      <th><strong>Details</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>HTTP-Methode</strong></td>
      <td><code>POST</code></td>
    </tr>
    <tr>
      <td><strong>Nutzername</strong></td>
      <td><code>{{ '&lt;username&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Passwort</strong></td>
      <td><code>{{ '&lt;password&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Content-Typ</strong></td>
      <td><code>application/json</code></td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Anfragetext

Kopieren Sie den Body der Anfrage, der im B2B-Admin-Tool angezeigt wird, und füllen Sie die Platzhalter mit Inhalten aus, indem Sie beliebige Tags zur Personalisierung in Liquid verwenden.

![Compose Tab, der den JSON-Body und die Webhook-Informationen anzeigt.]({% image_buster /assets/img/mypostcard/mypostcard_compose.jpg %})

### Schritt 2: Vorschau auf Ihre Anfrage

Als Nächstes erhalten Sie eine Vorschau Ihrer Anfrage im Panel **Vorschau** oder auf dem Tab **Test**. Dort können Sie einen zufälligen Benutzer, einen bestehenden Benutzer oder einen angepassten Nutzer:innen auswählen, um Ihren Webhook zu testen. Vergessen Sie nicht, Ihr Template zu speichern, bevor Sie die Seite verlassen!

![Testen Sie den Webhook Tab mit verschiedenen Feldern, um die Implementierung zu überprüfen.]({% image_buster /assets/img/mypostcard/mypostcard_test.jpg %})

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}

