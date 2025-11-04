---
nav_title: Distributionen mit angepassten Attributen
article_title: Ausschüttungen mit angepassten Attributen mit Voucherify
page_order: 3
alias: /partners/voucherify/custom_attributes/
description: "Dieser referenzierte Artikel beschreibt die Integration von Braze mit Voucherify. Die Integration von Braze ermöglicht es Ihnen, Voucherify Codes in Ihren Nachrichten von Braze zu versenden."
page_type: partner
search_tag: Partner
---

# Distributionen mit angepassten Attributen

> Die Integration von Braze ermöglicht es Ihnen, Voucherify Codes in Ihren Nachrichten von Braze zu versenden. Dieser referenzierte Artikel beschreibt, wie Sie angepasste Attribute von Braze mit Voucherify-Distributionen verwenden können.

_Diese Integration wird von Voucherify gepflegt._

{% alert tip %}
Bevor Sie angepasste Attribute von Braze in Voucherify-Verteilungen verwenden, müssen Sie Ihre Nutzer:innen zum Voucherify-Dashboard hinzufügen. Sie können Braze Connected Content verwenden, um Nutzer:innen zu synchronisieren oder Ihre Kund:innen über CSV oder API zu importieren. Besuchen Sie [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers), um mehr zu erfahren.
{% endalert %}

Mit angepassten Attributen von Braze können Sie Voucherify Codes an angepasste Attribute in Nutzerprofilen in Braze zuweisen. Sie können eindeutige Gutscheine, Geschenkkarten, Treuekarten und Empfehlungscodes verwenden. Verbinden Sie zunächst Voucherify mit Braze, erstellen Sie eine Verteilung in Voucherify und erstellen Sie schließlich eine Kampagne in Braze mit dem angepassten Attribut Snippet in Ihrer Nachrichten-Vorlage.

## Schritt 1: Verbinden Sie Ihr Voucherify-Konto mit Braze

Verbinden Sie zunächst Ihr Voucherify-Konto mit Braze.

1. Kopieren Sie den REST-API-Schlüssel aus Ihrem Braze-Konto.
2. Gehen Sie zum Verzeichnis **Integrationen** in Ihrem Voucherify-Dashboard, suchen Sie Braze und wählen Sie **Verbinden.**  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_integrations.png %}){: style="margin-top:15px;margin-left:25px;margin-bottom:15px;"}
    
3. Fügen Sie den Braze API-Schlüssel ein und wählen Sie **Verbinden**:  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_enter_API_key.png %}){: style="max-width:60%;margin-top:15px;margin-left:25px;margin-bottom:15px;"}


## Schritt 2: Code-Verteilung

Wenn eine Verbindung besteht, können Sie eine neue [Voucherify-Verteilung](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work) starten, die dem angepassten Attribut im Nutzerprofil in Braze einen Code zuweist. Später können Sie empfangene Attribute mit Codes in Ihren Kampagnen in Braze verwenden.

Bevor Sie die Verteilung einrichten, müssen Sie Ihre Braze-Nutzer:innen zum Voucherify-Dashboard hinzufügen. Besuchen Sie [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers), um mehr zu erfahren.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_distribution.png %})

Sie können Codes auf zwei Arten an Braze weitergeben:

- **Manueller Modus**
- Definieren Sie einen **automatisierten Workflow**, der die Zustellung von Code als Reaktion auf eine Aktion Ihrer Nutzer:innen auslöst.

Sowohl im manuellen als auch im automatischen Modus sendet Voucherify eindeutige Codes mit ihren Attributen und ordnet sie den angepassten Attributen von Braze in den Profilen der Nutzer:innen zu.

![Felder auf angepasste Attribute abbilden]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_fields_mapping.png %})

{% tabs %}
{% tab Manuelle Verteilung %}

Der manuelle Modus ist eine einmalige Aktion, bei der einer ausgewählten Zielgruppe Codes zugewiesen werden. Gehen Sie zu den **Verteilungen** in Ihrem Dashboard, führen Sie den Verteilungsmanager mit dem Plus aus, und wählen Sie **Manuelle Nachricht**.

1.  Nennen Sie Ihren Vertrieb.

    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}<br>  
    
    Wählen Sie eine Kampagne, die als Quelle eindeutiger Codes dienen soll **(1)**, und wählen Sie ein Segment von Nutzer:innen oder einen einzelnen Kunden als Empfänger **(2)**. Besuchen Sie [Voucherify](https://support.voucherify.io/article/51-customer-segments), um mehr über Segmente von Kund:in zu erfahren.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution_choose_segment.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  

2.  Als nächstes fügen Sie Marketing-Berechtigungen hinzu. Wenn Sie keine Genehmigungen von Ihrer Zielgruppe einholen, deaktivieren Sie die Zustimmungsprüfung.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_consents.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
3.  Wählen Sie Braze als Kanal und passen Sie die angepassten Felder an, die dem Nutzerprofil in Braze hinzugefügt werden sollen. Sie müssen das Feld für den Code des veröffentlichten Gutscheins hinzufügen; die übrigen Felder sind optional.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_channel.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
4.  Wenn Sie fertig sind, können Sie eine Zusammenfassung der Verteilung sehen. Klicken Sie auf **Speichern und Senden**, um die Codes den Nutzerprofilen in Braze zuzustellen.  

_Beachten Sie, dass alle manuellen Verteilungen mit einer 10-minütigen Verzögerung verschickt werden._

{% endtab %}
{% tab Automatischer Arbeitsablauf %}

Voucherify kann als Reaktion auf die folgenden Trigger automatisch Codes an Braze pushen:

- **Von Kunden:in eingegebenes/verlassenes spezifisches Voucherify Segment**
- **Erfolgreiche Veröffentlichung des Codes** \- die Nachricht wird gesendet, wenn der Code einer Kampagne an einen Kunden in Voucherify veröffentlicht (zugewiesen) wurde.
- **Auftragsstatus geändert** (Auftrag erstellt, Auftrag aktualisiert, Auftrag wurde bezahlt, Auftrag storniert)
- **Geschenkguthaben hinzugefügt** \- die Nachricht wird gesendet, wenn Geschenkguthaben auf der Karte der Kund:in hinzugefügt wird.
- **Treuepunkte hinzugefügt** \- die Nachricht wird gesendet, wenn Treuepunkte zum Profil der Kund:in hinzugefügt werden.
- **Gutschein eingelöst** \- die Nachricht wird an Kund:innen gesendet, die erfolgreich Gutscheine eingelöst haben.
- **Gutscheineinlösung Rollback** \- die Nachricht wird an die Kund:in gesendet, deren Einlösung erfolgreich rückgängig gemacht wurde.
- **Einlösung von Prämien** \- die Nachricht wird gesendet, wenn eine Kund:in eine Treue- oder Empfehlungsprämie einlöst.
- **Für einen Kunden wurde ein angepasstes Event protokolliert** \- die Nachricht wird ausgelöst, wenn Voucherify ein bestimmtes angepasstes Event protokolliert.

Um einen automatischen Workflow mit Braze und Voucherify einzurichten, [besuchen Sie das Tutorial für Distributoren](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work).

{% endtab %}
{% endtabs %}

## Schritt 3: Verwenden Sie angepasste Attribute von Voucherify in Ihrer Braze Kampagne

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_code.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Sobald das angepasste Attribut mit dem Code zu den angepassten Attributen des Kunden in Braze hinzugefügt wurde, können Sie es in Ihren Kampagnen verwenden.

Bearbeiten Sie den Nachrichtentext und fügen Sie das angepasste Attribut hinzu, das in der Voucherify-Verteilung definiert wurde. Platzieren Sie {% raw %}`{{custom_attribute.${custom_attribute_with_code}}}`{% endraw %}, um den eindeutigen Code anzuzeigen.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_body.png %}){: style="max-width:75%;"}

Wenn er fertig ist, sehen Sie den Code in der Vorschau Ihrer Nachricht.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_preview.png %})

