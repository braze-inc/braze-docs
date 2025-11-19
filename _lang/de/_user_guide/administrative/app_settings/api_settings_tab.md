---
nav_title: APIs und Bezeichner
article_title: APIs und Bezeichner
page_order: 3
page_type: reference
description: "Dieser Artikel behandelt die Seite APIs und Identifikatoren, auf der die API-Kennungen für Ihren Arbeitsbereich angezeigt werden."

---

# API-Schlüssel

> Die Seite **APIs und Identifikatoren** ist Ihr zentraler Knotenpunkt für die Verwaltung all Ihrer REST-API-Schlüssel an einem Ort. Hier können Sie auf die API-Schlüssel und App-Bezeichner der einzelnen Workspaces zugreifen.

Die Seite **APIs und Identifikatoren** finden Sie unter **Einstellungen**.

### API-Schlüssel

In diesem Abschnitt finden Sie Ihre REST API-Schlüssel für den Workspace, die eindeutigen Bezeichner, die Ihnen den Zugriff auf Ihre Daten für einen Workspace ermöglichen. Bei jeder Anfrage an die Braze-API ist ein REST-API-Schlüssel erforderlich. Weitere Informationen zur Erstellung und Verwendung von API-Schlüsseln finden Sie in unserer [Übersicht über REST-API-Schlüssel]({{site.baseurl}}/api/api_key/).

#### API IP allowlisting

Für zusätzliche Sicherheit können Sie eine Liste von IP-Adressen und Subnetzen angeben, die REST-API-Anfragen für einen bestimmten REST-API-Schlüssel stellen dürfen. Dies wird als Allowlisting oder Whitelisting bezeichnet. Um bestimmte IP-Adressen oder Subnetze zuzulassen, fügen Sie sie bei der Erstellung eines neuen REST-API-Schlüssels dem Abschnitt **Whitelist IPs** hinzu: 

![API IP Whitelisting Abschnitt der Erstellung eines neuen API-Schlüssels]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Wenn Sie nichts angeben, können Anfragen von jeder IP-Adresse gesendet werden.

{% alert tip %}
Einen Braze-to-Braze Webhook erstellen und allowlisting verwenden? Sehen Sie sich unsere Liste der [IPs an, die Sie auf die Whitelist setzen können]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

### App-Kennungen

Dieser Abschnitt enthält eine Liste von Bezeichnern, die dazu dienen, bestimmte Apps in Anfragen an die Braze API zu referenzieren. Weitere Informationen über Anwendungskennungen finden Sie unter [API-Schlüssel für Anwendungskennungen]({{site.baseurl}}/api/identifier_types/).

### Andere Identifikatoren

Für die Integration mit unserer API können Sie nach den Identifikatoren für alle Segmente, Kampagnen, Content Cards und mehr suchen, auf die Sie über die externe API von Braze zugreifen möchten. Alle Nachrichten sollten in [UTF-8](https://en.wikipedia.org/wiki/UTF-8) kodiert sein. Nachdem Sie einen von ihnen ausgewählt haben, wird der Bezeichner unterhalb des Dropdown-Menüs angezeigt.

Weitere Informationen finden Sie unter [API-Kennungstypen]({{site.baseurl}}/api/identifier_types/).

