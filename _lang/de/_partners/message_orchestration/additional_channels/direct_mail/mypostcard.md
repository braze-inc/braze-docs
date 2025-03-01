---
nav_title: MyPostcard
article_title: MyPostcard
page_order: 1
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und MyPostcard, die es Ihnen ermöglicht, Direktwerbung als zusätzlichen Kanal für Ihren CRM-Workflow zu nutzen."
alias: /partners/mypostcard/
page_type: partner
search_tag: Partner

---

# MyPostcard

> [MyPostcard][1], eine weltweit führende Postkarten-App, ermöglicht Ihnen die einfache Durchführung von Direktmailing-Kampagnen und bietet eine nahtlose und profitable Möglichkeit, mit Ihren Kunden in Kontakt zu treten. 

Nutzen Sie die Integration von MyPostcard und Braze, um Ihren Kunden mühelos Print-Mailings zu senden.

## Voraussetzungen

| Anforderung                      | Beschreibung                                                                                                             |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| MyPostcard B2B-Konto           | Um die Vorteile dieser Integration zu nutzen, müssen Sie sich bei MyPostcard registrieren.                                          |
| B2B-API-Schlüssel und Anmeldeinformationen        | Sie finden Ihren API-Schlüssel und die Anmeldedaten im MyPostcard B2B Admin Tool.                                         |
| Genehmigte MyPostcard B2B-Kampagne | Um die Vorteile dieser Integration zu nutzen, müssen Sie eine Print-Mailing-Kampagne im MyPostcard B2B-Tool einrichten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Anwendungsfälle

Um Ihre Direktmailing-Kampagnen aufzuwerten, müssen Sie über die traditionellen Massenmailings hinausgehen und Print-Mailings nahtlos in Ihre Arbeitsabläufe integrieren. Auf diese Weise können Sie gezielt Kunden erreichen, die sich von Ihren E-Mail-Newslettern abgemeldet haben oder deren E-Mails als Spam markiert sind. Mit MyPostcard können Sie mühelos Print-Mailing-Kampagnen direkt über Braze versenden.

- Erstellen Sie in Braze intuitive Workflows, die Print-Mails als leistungsstarken neuen Kanal einbeziehen, ohne dass Sie über technisches Fachwissen verfügen müssen.
- Erschließen Sie das Potenzial personalisierter Print-Mailings mit ein paar einfachen Schritten.
- Profitieren Sie von einer unkomplizierten Implementierung, die von einem persönlichen Support durch ein engagiertes Team unterstützt wird.

## Integration

Um MyPostcard zu integrieren, [melden Sie sich an oder registrieren Sie sich][2] und erstellen Sie Ihre erste Kampagne, um sie über [Braze Webhooks][3] zu nutzen.

### Schritt 1: Erstellen Sie Ihre Braze Webhook-Vorlage

Erstellen Sie eine MyPostcard-Webhook-Vorlage zur Verwendung in zukünftigen Kampagnen oder Canvases, indem Sie auf der Braze-Plattform zu **Vorlagen** > **Webhook-Vorlagen** navigieren.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation/) verwenden, gehen Sie zu **Engagement** > **Vorlagen & Medien** > **Webhook-Vorlagen**.
{% endalert %}

Wenn Sie eine einmalige MyPostcard-Webhook-Kampagne erstellen oder eine vorhandene Vorlage verwenden möchten, wählen Sie **Webhook** in Braze, wenn Sie eine neue Kampagne erstellen. Füllen Sie die folgenden Felder aus:

| Feld         | Beschreibung                                               |
|---------------|-----------------------------------------------------------|
| **Webhook-URL** | Die Webhook-URL, wie sie im B2B Admin Tool angezeigt wird.             |
| **Anfragetext** | Rohtext (JSON-Format, zu finden im B2B Admin Tool).        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Anfragemethode und Kopfzeilen

MyPostcard erfordert eine HTTP-Methode zusammen mit den folgenden HTTP-Headern, die in die Vorlage aufgenommen werden müssen.

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
      <td><strong>Benutzername</strong></td>
      <td><code>{{ '&lt;username&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Passwort</strong></td>
      <td><code>{{ '&lt;password&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Inhalt-Typ</strong></td>
      <td><code>application/json</code></td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Anfragetext

Kopieren Sie den im B2B-Admin-Tool angezeigten Anfragetext und füllen Sie die Platzhalter mit Inhalten aus, indem Sie die Liquid-Personalisierungs-Tags verwenden.

![Die Registerkarte Zusammenstellen zeigt den JSON-Body und die Webhook-Informationen.][4]

### Schritt 2: Vorschau Ihrer Anfrage

Als nächstes sehen Sie sich Ihre Anfrage in der **Vorschau** an oder gehen Sie auf die Registerkarte **Test**, wo Sie einen zufälligen Benutzer, einen bestehenden Benutzer oder einen benutzerdefinierten Benutzer zum Testen Ihres Webhooks auswählen können. Vergessen Sie nicht, Ihre Vorlage zu speichern, bevor Sie die Seite verlassen!

![Testen Sie Webhook Tab mit verschiedenen Feldern, um die Implementierung zu überprüfen.][5]

{% alert important %}
Denken Sie daran, Ihre Vorlage zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Vorlagen finden Sie in der Liste **Gespeicherte Webhook-Vorlagen**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}

[1]: https://www.mypostcard.com
[2]: https://www.mypostcard.com/b2b/admin/
[3]: https://www.braze.com/docs/user_guide/message_building_by_channel/webhooks
[4]: {% image_buster /assets/img/mypostcard/mypostcard_compose.jpg %}
[5]: {% image_buster /assets/img/mypostcard/mypostcard_test.jpg %}
