---
nav_title: Datentransformation
hidden: true
---

# Braze Data Transformation

> Braze [Data Transformation]({{site.baseurl}}/data_transformation/) kann einen Webhook von einer Partnerplattform aufnehmen und es einem Kunden ermöglichen, ein Mapping zu definieren, um die Nutzdaten dieses Webhooks in die gewünschten Benutzerdaten umzuwandeln, z. B. Attribute, Events oder Käufe auf Braze-Benutzerprofilen.

## Wie eine auf Datentransformation basierende Integration aussehen würde

Eine Partnerintegration, die auf dem Feature Datentransformation basiert, könnte eine Code-Vorlage für die Transformation sein, die über die öffentliche Dokumentation mit den Kund:innen geteilt wird.

Für gegenseitige Kund:in würde es etwa so aussehen:

1. Sie melden sich bei Ihrer Plattform an und richten Webhooks ein.
2. Sie arbeiten mit ihrem Braze Team zusammen, um Zugriff auf Braze Data Transformation zu erhalten und eine neue Transformation in ihrem Braze-Dashboard zu erstellen.
3. Die durch die Transformation erzeugte URL wird kopiert.
4. Zurück in Braze senden sie einen Test-Webhook an die kopierte Transformation-URL.
5. In Braze kopieren sie die Code-Vorlage für die Transformation und fügen sie ein.
6. Sie ermöglichen die Transformation.
7. Wenn diese Funktion aktiviert ist, können sie über das Braze-Tool für die Nutzersuche überprüfen, ob das Nutzerprofil auf der Grundlage des Webhooks aktualisiert wurde, und den Code für die Transformation wie gewünscht bearbeiten.

{% alert tip %}
Es wird empfohlen, für jeden an Braze gesendeten Webhook-Typ eine Transformation zu erstellen, wenn Sie Code-Beispiele für die Transformation erstellen.
{% endalert %}
