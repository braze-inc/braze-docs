---
nav_title: Kopieren über Arbeitsbereiche hinweg
article_title: Kopieren über Arbeitsbereiche hinweg
alias: "/copying_to_workspaces/"
page_order: 0.5
page_type: reference
description: "Dieser Artikel gibt einen Überblick darüber, wie Sie Kampagnen in verschiedene Arbeitsbereiche kopieren können."
tool: Campaigns
---

# Kopieren zwischen Arbeitsbereichen

> Durch das Kopieren von Kampagnen über verschiedene Arbeitsbereiche hinweg können Sie mit einer Kopie einer Kampagne in einem anderen Arbeitsbereich beginnen und so die Erstellung Ihrer Nachrichten beschleunigen. Dieser Text bleibt als Entwurf erhalten, bis Sie ihn bearbeiten und veröffentlichen. So können Sie Ihre erfolgreichen Kommunikationsstrategien beibehalten und ausbauen.<br><br>Auf dieser Seite erfahren Sie, wie Sie Kampagnen in verschiedene Arbeitsbereiche kopieren können und was kopiert wird und was nicht.

{% alert important %}
Das Kopieren von Kampagnen in andere Arbeitsbereiche ist in folgenden Kanälen möglich: SMS, In-App-Nachrichten, E-Mail, E-Mail-Vorlagen und Inhaltsblöcke. Andere Kanäle (wie Push- und Content-Cards) werden bislang nicht unterstützt.
{% endalert %}

## Wie kopiere ich eine Kampagne in einen anderen Arbeitsbereich?

![Menü mit der Option "In Workspace kopieren".][1]{: style="float:right;max-width:25%;margin-left:15px;"}

Wählen Sie das Zahnradsymbol <i class="fas fa-cog"></i> neben der ausgewählten Kampagne, und wählen Sie **In Workspace kopieren**. Nach dem Kopieren sollten Sie die Kampagne überprüfen und testen, um sicherzustellen, dass alle Felder korrekt funktionieren.

Wenn Sie eine Kampagne in andere Arbeitsbereiche kopieren, werden Felder wie Kampagnenname und -beschreibung, Varianten, Bereitstellungszeitplan und Konversionsverhalten ebenfalls kopiert. Bei E-Mail-Kampagnen werden Felder wie der E-Mail-Text, der Betreff und die Kopfzeile ebenfalls in den Zielarbeitsbereich kopiert. 

Beachten Sie, dass Multichannel-Kampagnen mit nicht unterstützten Kanälen nicht in andere Arbeitsbereiche kopiert werden können.

### Was über Arbeitsbereiche hinweg kopiert wird

Die folgende Liste ist nicht vollständig. Überprüfen Sie am besten die Details der Kampagne und testen Sie, ob Ihre Kampagne wie erwartet funktioniert.

{% tabs %}
{% tab Kampagnen %}

| Kopiert | Ausgelassen |
|---|---|
| Beschreibung | Territorien | 
| Typ | Tags | 
| Aktionen (verschachtelt) | Segmente | 
| Konvertierungsverhalten (verschachtelt) | Genehmigungen | 
| Konfigurationen für die stille Zeit | Auslösezeitplan | 
| Frequency-Capping | Kampagnen-Zusammenfassungen | 
| Abonnementstatus |  | 
| Wiederholungen |  | 
| Ist transaktional |  | 

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Konvertierungsverhalten %}

| Kopiert | Ausgelassen |
|---|---|
| Verhalten | Arbeitsbereich-IDs |
| Interaktion im Rahmen der Kampagne |  Kampagnen-ID | 
| Name des angepassten Events |  | 
| Produktname |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Aktionen %}

| Kopiert | Ausgelassen |
|---|---|
| Aktionsarten | Zählung senden |
| Nachrichtenvarianten |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Nachrichtenvarianten %}

| Kopiert | Ausgelassen |
|---|---|
| Prozentsatz senden | API-ID |
| Typ |  Seedgruppen-IDs | 
|  |  Linkvorlagen-IDs | 
|  |  Interne Benutzergruppen-IDs | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab E-Mail-Varianten %}

| Kopiert | Ausgelassen |
|---|---|
| [E-Mail-Textkörper]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/?tab=email%20body) | Absender |
| Nachrichtenzusätze |  Antwort an | 
| Titel |  BCC | 
| Betreff |  Link-Template | 
|  |  Link-Aliasing |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Haupttext %}

| Kopiert | Ausgelassen |
|---|---|
| Klartext | Link-Aliasing |
| HTML und Drag-and-Drop-Inhalte |  | 
| Preheader |  | 
| Inline-CSS |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab E-Mail-Vorlagen %}

| Kopiert | Ausgelassen |
|---|---|
| [E-Mail-Textkörper]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/?tab=email%20body) | API-IDs |
| Beschreibung | Bild-IDs | 
| Betreff | Territorien | 
| Kopfzeilen | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Content-Blöcke %}

| Kopiert | Ausgelassen |
|---|---|
| Name | Link-Aliasing |
| Beschreibung | API-Schlüssel | 
| Content | Territorien | 
| HTML und Drag-and-Drop-Inhalte | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab SMS-Varianten %}

| Kopiert | Ausgelassen |
|---|---|
| Textkörper | Messenger |
| Link-Verkürzung | VCF-Medienobjekte | 
| Klick-Tracking |  | 
| Medien |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Kopieren von Kampagnen, die Liquid enthalten

Bei Nachrichtentexten mit Liquid-Verweisen werden diese zwar in den Zielarbeitsbereich kopiert, funktionieren aber u. U. nicht wie erwartet. Wenn eine Kampagne aus Arbeitsbereich A in Arbeitsbereich B kopiert wird, kann letzterer also nicht unbedingt auf Details aus Arbeitsbereich A und insbesondere nicht auf Liquid verweisen. So werden u. a. keine Felder wie Auslöseaktionen und Zielgruppenfilter übernommen.

Beachten Sie die folgenden Liquid-Referenzen mit Abhängigkeiten beim Kopieren von Kampagnen zwischen Arbeitsbereichen:

- Katalogartikel-Tags
- Connected-Content-Tags
- Content-Blöcke
- Angepasste Attribute
- Einstellungszentren
- Produkt-Empfehlungen
- Abonnementstatus-Tags
- Gutschein- und Aktionstags

Wenn Sie eine Kampagne in andere Arbeitsbereiche kopieren, werden die Content-Blöcke nicht mitkopiert. Sie können jedoch im Zielarbeitsbereich referenziert werden, wenn ein Block mit demselben Namen existiert. Alternativ können Sie ihn (oder entsprechende Liquid-Verweise) auch im Zielarbeitsbereich erstellen und so Fehler beim Kampagnenstart vermeiden.

### Kopieren von Kampagnen mit Feature-Flags

Um eine Feature-Flag-Kampagne zwischen Workspaces zu kopieren, vergewissern Sie sich, dass im Ziel-Workspace ein [Feature-Flag-Experiment]({{site.baseurl}}/developer_guide/feature_flags/experiments) mit einer ID konfiguriert ist, die mit dem Feature-Flag übereinstimmt, auf das in der ursprünglichen Kampagne referenziert wurde. Wenn Sie eine Kampagne kopieren, aber im Workspace des Ziels keine passende Feature-Flag ID vorhanden ist, ist die Auswahl der Feature-Flags in der Kampagne beim Kopieren leer, und Sie müssen eine andere auswählen.

[1]: {% image_buster /assets/img_archive/clone_campaign.png %}

