---
nav_title: Einzigartige Rabattcodes 
article_title: Eindeutige Rabattcodes versenden
alias: /shopify_discount_codes/
page_order: 6
description: "Dieser Artikel referenziert einen von der Community eingereichten Anwendungsfall zur Verwendung von Braze Aktionscodes mit dem Shopify Bulk Discount Code Bot, um eindeutige Rabattcodes über Ihre Kampagnen und Canvase zu versenden."
---

# Versenden eindeutiger Rabattcodes über Shopify

> Dieser von der Community eingereichte Anwendungsfall zeigt, wie Sie Braze [Aktionscodes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) mit dem Shopify Bulk Discount Code Bot verwenden können, um eindeutige Rabattcodes für Ihre Kampagnen und Canvase zu generieren. Eindeutige Rabattcodes helfen dabei, die Ausnutzung von generischen Aktionscodes zu vermeiden.

{% alert important %}
Dies ist eine von der Community eingereichte Integration, die nicht direkt von Braze unterstützt wird. Der Bulk Discount Code Bot wird direkt von Shopify unterstützt. Nur Braze Aktionscodes werden von Braze unterstützt.
{% endalert %}

## Anforderungen

| Anforderung | Beschreibung |
| --- | --- |
| Einen Shopify Shop einrichten | Bestätigen Sie, dass Sie bereits [einen Shopify Shop mit Braze eingerichtet]({{site.baseurl}}/shopify_overview/) haben. |
| Die App Bulk Discount Code Bot installieren | Laden Sie die App [Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator) im Shopify App Store herunter. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Eindeutige Rabattcodes versenden

### Schritt 1: Konfigurieren Sie Ihre Rabattcodes

Verwenden Sie den Bulk Discount Code Bot, um Ihre Rabattcodes nach der Anzahl der zu generierenden Codes, der Länge des Codes, dem Wert des Rabatts und vielem mehr zu konfigurieren.

![Die Konfigurationsoptionen für ein Rabattset.][1]

### Schritt 2: Exportieren Sie Ihre Codes

Suchen Sie Ihren Rabattcode in der Suchleiste des Bulk Discount Code Bot und wählen Sie dann **Codes exportieren** > **Codes herunterladen**, um eine CSV-Datei in Ihren Download-Ordner zu laden.

![Suchleiste mit einer Dropdown-Liste, in der die Rabattsätze angezeigt werden, und einer Reihe von Buttons zum Auswählen.][2]{: style="max-width:70%;"}

Löschen Sie in der CSV-Datei Zeile 1, um die Spaltenüberschrift "Promo" zu entfernen. Dadurch wird verhindert, dass "Promo" in Braze zu einem Rabattcode wird.

![Ein Flussdiagramm, das das Entfernen der Zeilenüberschrift "Promo" in einer CSV-Datei zeigt.][3]{: style="max-width:60%;"}

### Schritt 3: Fügen Sie Ihre Rabattcodes zu Braze hinzu

Gehen Sie in Braze zu **Dateneinstellungen** > **Aktionscodes** > **Liste der Aktionscodes erstellen** und [konfigurieren Sie Ihre Liste der Rabattcodes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/#creating-a-promotion-code-list). Vergewissern Sie sich, dass Sie mit dem Ablaufdatum übereinstimmen, das vom Bulk Rabattcode Bot konfiguriert wurde.

Laden Sie dann Ihre CSV-Datei hoch und wählen Sie **Liste speichern**.

### Schritt 4: Fügen Sie Ihre Rabattcodes zu einer Kampagne oder einem Canvas-Schritt von Braze hinzu.

Wenn Sie Ihre eindeutigen Rabattcodes in einer einzigen Kampagne verwenden möchten oder wenn es Ihnen nichts ausmacht, dass Nutzer:innen mehrere eindeutige Codes in verschiedenen Kampagnen oder Canvas-Schritten erhalten, kopieren Sie das Liquid-Snippet des Codes aus der Liste der Aktionscodes, die Sie gespeichert haben.

![Ein Liquid Code-Snippet mit einem Button zum Kopieren.][4]{: style="max-width:60%;"}

Fügen Sie das Liquid-Snippet in eine Kampagne oder einen Canvas-Schritt ein. 

![Ein GIF, das zeigt, wie das Liquid Snippet zu einem Canvas-Schritt hinzugefügt wird.][5]

Wenn Sie möchten, dass Benutzer nur einen einzigen Rabattcode erhalten, unabhängig davon, wie oft der Rabattcode in Kampagnen oder Canvase referenziert wird, erstellen Sie einen Schritt [zur Benutzeraktualisierung]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) direkt vor dem ersten Schritt der Nachricht, der den Rabattcode einem angepassten Attribut wie "Promo Code" zuordnet.

{% alert tip %}
Sie können auch [ein angepasstes Attribut erstellen]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), indem Sie zu **Dateneinstellungen** > **Benutzerdefinierte Attribute** gehen.
{% endalert %}

Führen Sie im Schritt Nutzer:innen aktualisieren für jedes Feld folgende Schritte aus:
- **Attributname:** Wählen Sie einen **Promo Code** aus.
- **Aktion:** Wählen Sie **Update** aus.
- **Schlüssel-Wert:** Fügen Sie das Liquid Code Snippet ein.

![Ein Nutzer:innen Update-Schritt, der ein Attribut "Promo Code" mit dem Liquid Snippet aktualisiert.][6]

Jetzt können Sie das angepasste Attribut {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} zu jeder Nachricht hinzufügen, und der Rabattcode wird als Template eingefügt.

## Rabattcode Verhalten

{% details Multichannel-Kampagne oder Canvas-Schritt %}

Wenn ein Rabattcode-Snippet in einer Multichannel-Kampagne oder einem Canvas-Schritt verwendet wird, erhalten die Nutzer:innen immer einen eindeutigen Code. Wenn ein Nutzer:innen über mehr als einen Kanal einen Code erhalten kann, erhält er über jeden Kanal denselben Code. Mit anderen Worten, ein berechtigter Nutzer:innen erhält nur einen Code für alle Nachrichten, die von dieser Kampagne oder diesem Canvas-Schritt verschickt werden.

{% enddetails %}

{% details Verschiedene Canvas-Schritte oder separate Kampagnen %}

Wenn ein Rabattcode in mehreren Canvas-Schritten oder separaten Kampagnen referenziert wird, erhält ein berechtigter Nutzer:innen mehrere eindeutige Rabattcodes (einen Code für jeden Canvas-Schritt oder jede Kampagne).

{% enddetails %}

[1]: {% image_buster /assets/img/Shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/Shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/Shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/Shopify/liquid_code_snippet.png %}
[5]: {% image_buster /assets/img/Shopify/liquid_promo_code.gif %}
[6]: {% image_buster /assets/img/Shopify/user_update_step.png %}