---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "Die Integration von Braze und Alpaco nutzt die Syntax von Alpaco, um datengesteuerte E-Mail-Vorlagen zu erstellen und in Braze zu exportieren."
page_type: partner
search_tag: Partner

---

# Alpaco

> [Alpaco](https://alpaco.email/) ist ein Online-E-Mail-Marketing-Tool, das einen Drag-and-Drop-E-Mail-Editor für eine neue Ebene der Kontrolle über Design und Ausgabe bietet. Die Integration von Braze und Alpaco ermöglicht Ihnen den Export von marken- und datengesteuerten E-Mails nach Braze. 

{% alert note %}
Alpaco unterstützt [alle Liquid-Variablen](https://shopify.github.io/liquid/) und somit auch alle Liquid-Variablen, die Sie in Ihren Braze-Konfigurationen verwenden.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| ------------| ----------- |
| Alpaco Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Alpaco-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit vollständigen **Vorlagenberechtigungen**. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Cluster-Instanz | Ihre [Braze-Cluster-Instanz]({{site.baseurl}}/api/basics/#endpoints) ist auf Ihr Braze-Dashboard und Ihren REST-Endpunkt abgestimmt. <br><br> Wenn Ihre Dashboard-URL zum Beispiel `https://dashboard-03.braze.com` lautet, ist Ihr Endpunkt `dashboard-03`.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

Stellen Sie dem Alpaco-Kundenerfolgsteam Ihren Braze REST API-Schlüssel und Ihre Cluster-Instanz zur Verfügung. Das Team wird dann die erste Integration für Sie einrichten.

{% alert note %}
Dies ist eine einmalige Einrichtung und alle zukünftigen Exporte werden automatisch diesen API-Schlüssel verwenden.
{% endalert %}

## Exportieren von Alpaco-E-Mails nach Braze

### Schritt 1: Erstellen Sie eine E-Mail-Vorlage in Alpaco

Nutzen Sie die verschiedenen Einstellungen und Optionen auf der Alpaco-Plattform, um eine Vorlage zu erstellen, die Ihre Markenidentität zum Ausdruck bringt. Wählen Sie **Speichern**, wenn Sie mit Ihrer Vorlage zufrieden sind.

![Alpaco Vorlage erstellen]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Schritt 2: Erstellen Sie eine E-Mail

Nachdem die Vorlage erstellt wurde, navigieren Sie zur Lobby und erstellen eine E-Mail mit der Vorlage. Wählen Sie **Überprüfen**, um sicherzustellen, dass alles richtig aussieht.

![Alpaco E-Mail erstellen]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Schritt 3: Überprüfen und Exportieren von E-Mails nach Braze

Wählen Sie **Exportieren** und wählen Sie die Braze-Integration, um Ihre E-Mail-Vorlage nach Braze zu exportieren. 

Wenn Sie Änderungen an Ihrer E-Mail-Vorlage vornehmen möchten, nehmen Sie diese Änderungen in Alpaco vor und exportieren Sie die E-Mail dann erneut nach Braze. Dadurch wird die E-Mail in Braze mit Ihren Änderungen aktualisiert.

![Alpaco Export email]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Verwendung von Alpaco-E-Mail-Vorlagen in Braze

Sie finden Ihre hochgeladene Alpaco-E-Mail, indem Sie im Braze Dashboard zu **Vorlagen & Medien > E-Mail-Vorlagen** navigieren. Mit dieser Vorlage können Sie nun marken- und datengesteuerte E-Mails an Ihre Nutzer versenden.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
