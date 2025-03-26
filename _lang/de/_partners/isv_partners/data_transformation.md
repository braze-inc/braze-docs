---
nav_title: Datentransformation
hidden: true
---

# Braze Data Transformation

> Braze [Data Transformation]({{site.baseurl}}/data_transformation/) kann einen Webhook von einer Partnerplattform aufnehmen und einem Kunden ermöglichen, ein Mapping zu definieren, um die Nutzdaten dieses Webhooks in die gewünschten Benutzerdaten umzuwandeln, z. B. Attribute, Ereignisse oder Käufe in Braze-Benutzerprofilen.

## Wie eine auf Datentransformation basierende Integration aussehen würde

Eine Partnerintegration, die auf der Funktion Datenumwandlung basiert, könnte eine Codevorlage für die Umwandlung sein, die über die öffentliche Dokumentation mit Kunden geteilt wird.

Für Kunden auf Gegenseitigkeit würde es in etwa so aussehen:

1. Sie melden sich bei Ihrer Plattform an und richten Webhooks ein.
2. Sie arbeiten mit ihrem Braze-Team zusammen, um Zugriff auf Braze Data Transformation zu erhalten und eine neue Transformation in ihrem Braze-Dashboard zu erstellen.
3. Die durch die Transformation erzeugte URL wird kopiert.
4. Zurück in Braze senden sie einen Test-Webhook an die kopierte Transformations-URL.
5. In Braze kopieren sie die Vorlage für den Transformationscode und fügen sie ein.
6. Sie ermöglichen die Transformation.
7. Wenn diese Funktion aktiviert ist, können Sie über das Braze-Benutzersuchtool überprüfen, ob das Benutzerprofil auf der Grundlage des Webhooks aktualisiert wurde, und den Transformationscode wie gewünscht bearbeiten.

{% alert tip %}
Es wird empfohlen, für jeden an Braze gesendeten Webhook-Typ eine Transformation zu erstellen, wenn Sie Beispiele für Transformationscode erstellen.
{% endalert %}
