---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "Die Integration von Braze und Alpaco nutzt die Syntax von Alpaco, um datengestützte E-Mail Templates zu erstellen und nach Braze zu exportieren."
page_type: partner
search_tag: Partner

---

# Alpaco

> [Alpaco](https://alpaco.email/) ist ein Online-Tool für E-Mail Marketing, das einen Drag-and-Drop-Editor für E-Mails bietet, mit dem Sie Design und Ausgabe auf ein neues Niveau bringen können. Die Integration von Braze und Alpaco erlaubt Ihnen den Export von marken- und datengestützten E-Mails nach Braze. 

_Diese Integration wird von Alpaco gepflegt._

{% alert note %}
Alpaco unterstützt [alle Liquid-Variablen](https://shopify.github.io/liquid/) und somit auch alle Liquid-Variablen, die in Ihren Braze-Konfigurationen verwendet werden.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| ------------| ----------- |
| Alpaco Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Alpaco-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit vollständigen **Templates-Berechtigungen**. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Cluster Instanz | Ihre [Braze-Cluster-Instanz]({{site.baseurl}}/api/basics/#endpoints) ist auf Ihr Braze-Dashboard und Ihren REST-Endpunkt abgestimmt. <br><br> Wenn Ihre Dashboard-URL zum Beispiel `https://dashboard-03.braze.com` lautet, ist Ihr Endpunkt `dashboard-03`.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

Stellen Sie dem Customer-Success-Team von Alpaco Ihren Braze REST API-Schlüssel und Ihre Cluster-Instanz zur Verfügung. Das Team wird dann die erste Integration für Sie einrichten.

{% alert note %}
Dies ist eine einmalige Einrichtung und alle zukünftigen Exporte werden automatisch diesen API-Schlüssel verwenden.
{% endalert %}

## Exportieren von Alpaco E-Mails nach Braze

### Schritt 1: Erstellen Sie eine E-Mail-Vorlage in Alpaco

Nutzen Sie die verschiedenen Einstellungen und Optionen auf der Alpaco-Plattform, um ein Template zu erstellen, das Ihre Markenidentität zum Ausdruck bringt. Wählen Sie **Speichern**, wenn Sie mit Ihrem Template zufrieden sind.

![Alpaco Template erstellen]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Schritt 2: Eine E-Mail erstellen

Nachdem die Vorlage erstellt wurde, navigieren Sie zur Lobby und erstellen eine E-Mail mit der Vorlage. Wählen Sie **Überprüfen**, um sicherzustellen, dass alles richtig aussieht.

![Alpaco E-Mail erstellen]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Schritt 3: Überprüfen und Exportieren von E-Mails nach Braze

Wählen Sie **Exportieren** und wählen Sie die Integration von Braze, um Ihre E-Mail-Vorlage nach Braze zu exportieren. 

Wenn Sie Änderungen an Ihrer E-Mail-Vorlage vornehmen möchten, nehmen Sie diese Änderungen in Alpaco vor und exportieren Sie die E-Mail dann erneut nach Braze. Dadurch wird die E-Mail in Braze mit Ihren Änderungen aktualisiert.

![Alpaco Export email]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Verwendung von Alpaco E-Mail Templates in Braze

Sie finden Ihre hochgeladene Alpaco E-Mail, indem Sie im Braze-Dashboard zu **Templates und Medien > E-Mail-Vorlagen** navigieren. Mit diesem Template können Sie jetzt marken- und datengestützte E-Mails an Ihre Nutzer:innen versenden.


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
