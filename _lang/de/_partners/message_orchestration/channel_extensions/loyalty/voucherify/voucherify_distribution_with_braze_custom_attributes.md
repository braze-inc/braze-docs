---
nav_title: Verteilungen mit benutzerdefinierten Attributen
article_title: Ausschüttungen mit benutzerdefinierten Attributen mit Voucherify
page_order: 3
alias: /partners/voucherify/custom_attributes/
description: "Dieser Referenzartikel beschreibt die Integration von Braze mit Voucherify. Die Braze-Integration ermöglicht es Ihnen, Voucherify-Codes in Ihren Braze-Nachrichten zu versenden."
page_type: partner
search_tag: Partner
---

# Verteilungen mit benutzerdefinierten Attributen

> Die Braze-Integration ermöglicht es Ihnen, Voucherify-Codes in Ihren Braze-Nachrichten zu versenden. Dieser Referenzartikel beschreibt, wie Sie die benutzerdefinierten Attribute von Braze mit Voucherify-Distributionen verwenden können.

{% alert tip %}
Bevor Sie die benutzerdefinierten Attribute von Braze in Voucherify-Distributionen verwenden, müssen Sie Ihre Braze-Benutzer zum Voucherify-Dashboard hinzufügen. Sie können Braze Connected Content verwenden, um Benutzer zu synchronisieren oder Ihre Kunden über CSV oder API zu importieren. Besuchen Sie [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers), um mehr zu erfahren.
{% endalert %}

Mit den benutzerdefinierten Attributen von Braze können Sie Voucherify-Codes benutzerdefinierten Attributen in Benutzerprofilen in Braze zuweisen. Sie können einzigartige Gutscheine, Geschenkkarten, Treuekarten und Empfehlungscodes verwenden. Verbinden Sie zunächst Voucherify mit Braze, erstellen Sie eine Verteilung in Voucherify und erstellen Sie schließlich eine Kampagne in Braze mit dem benutzerdefinierten Attribut-Snippet in Ihrer Nachrichtenvorlage.

## Schritt 1: Verbinden Sie Ihr Voucherify-Konto mit Braze

Verbinden Sie zunächst Ihr Voucherify-Konto mit Braze.

1. Kopieren Sie den REST-API-Schlüssel aus Ihrem Braze-Konto.
2. Gehen Sie zum **Integrationsverzeichnis** in Ihrem Voucherify Dashboard, suchen Sie Braze und wählen Sie **Verbinden.**  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_integrations.png %}){: style="margin-top:15px;margin-left:25px;margin-bottom:15px;"}
    
3. Fügen Sie den Braze API-Schlüssel ein und wählen Sie **Verbinden**:  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_enter_API_key.png %}){: style="max-width:60%;margin-top:15px;margin-left:25px;margin-bottom:15px;"}


## Schritt 2: Code-Verteilung

Wenn Sie verbunden sind, können Sie eine neue [Voucherify-Verteilung](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work) starten, die dem benutzerdefinierten Attribut im Benutzerprofil in Braze einen Code zuweist. Später können Sie empfangene Attribute mit Codes in Ihren Braze-Kampagnen verwenden.

Bevor Sie die Verteilung einrichten, müssen Sie Ihre Braze-Benutzer zum Voucherify-Dashboard hinzufügen. Besuchen Sie [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers), um mehr zu erfahren.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_distribution.png %})

Sie können Codes auf zwei Arten an Braze weitergeben:

- **Manueller Modus**
- Definieren Sie einen **automatisierten Workflow**, der die Bereitstellung von Code als Reaktion auf eine Aktion Ihrer Benutzer auslöst.

Sowohl im manuellen als auch im automatischen Modus sendet Voucherify eindeutige Codes mit ihren Attributen und ordnet sie den Braze Custom Attributes in den Profilen der Benutzer zu.

![Felder auf benutzerdefinierte Attribute zuordnen]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_fields_mapping.png %})

{% tabs %}
{% tab Manuelle Verteilung %}

Der manuelle Modus ist eine einmalige Aktion, bei der einem ausgewählten Publikum Codes zugewiesen werden. Gehen Sie zu den **Verteilungen** in Ihrem Dashboard, starten Sie den Verteilungsmanager mit dem Pluszeichen und wählen Sie **Manuelle Nachricht**.

1.  Nennen Sie Ihren Vertrieb.

    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}<br>  
    
    Wählen Sie eine Kampagne, die eine Quelle für eindeutige Codes sein wird **(1)** und wählen Sie ein Nutzersegment oder einen einzelnen Kunden als Empfänger **(2)**. Besuchen Sie [Voucherify](https://support.voucherify.io/article/51-customer-segments), um mehr über Kundensegmente zu erfahren.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution_choose_segment.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  

2.  Als nächstes fügen Sie Marketingberechtigungen hinzu. Wenn Sie keine Genehmigungen von Ihrem Publikum einholen, deaktivieren Sie die Zustimmungsprüfung.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_consents.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
3.  Wählen Sie Braze als Kanal und ordnen Sie benutzerdefinierte Felder zu, die dem Benutzerprofil in Braze hinzugefügt werden. Sie müssen das Feld für den Code des veröffentlichten Gutscheins hinzufügen; die übrigen Felder sind optional.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_channel.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
4.  Wenn Sie fertig sind, können Sie eine Zusammenfassung der Verteilung sehen. Klicken Sie auf **Speichern und Senden**, um Codes an Benutzerprofile in Braze zu senden.  

_Beachten Sie, dass alle manuellen Verteilungen mit einer 10-minütigen Verzögerung verschickt werden._

{% endtab %}
{% tab Automatischer Arbeitsablauf %}

Voucherify kann Codes als Reaktion auf die folgenden Auslöser automatisch an Braze senden:

- **Kunde hat bestimmtes Voucherify-Segment betreten/verlassen**
- **Erfolgreiche Veröffentlichung des Codes** \- die Nachricht wird gesendet, wenn der Code aus einer Kampagne einem Kunden in Voucherify veröffentlicht (zugewiesen) wurde.
- **Auftragsstatus geändert** (Auftrag erstellt, Auftrag aktualisiert, Auftrag bezahlt, Auftrag storniert)
- **Geschenkguthaben hinzugefügt** \- die Nachricht wird gesendet, wenn der Karte des Kunden Geschenkguthaben hinzugefügt wird.
- **Treuepunkte hinzugefügt** \- die Nachricht wird gesendet, wenn dem Profil des Kunden Treuepunkte hinzugefügt werden.
- **Gutschein eingelöst** \- die Nachricht wird an Kunden gesendet, die erfolgreich Gutscheine eingelöst haben.
- **Rollback der Gutscheineinlösung** \- die Nachricht wird an den Kunden gesendet, dessen Einlösung erfolgreich rückgängig gemacht wurde.
- **Einlösung einer Prämie** \- die Nachricht wird gesendet, wenn ein Kunde eine Treue- oder Empfehlungsprämie einlöst.
- **Benutzerdefiniertes Ereignis wurde für einen Kunden protokolliert** \- die Nachricht wird ausgelöst, wenn Voucherify ein bestimmtes benutzerdefiniertes Ereignis protokolliert.

Um einen automatischen Workflow mit Braze und Voucherify einzurichten, [besuchen Sie das Tutorial für Distributoren](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work).

{% endtab %}
{% endtabs %}

## Schritt 3: Verwenden Sie Voucherify-Attribute in Ihrer Braze-Kampagne

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_code.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Sobald das benutzerdefinierte Attribut mit dem Code zu den benutzerdefinierten Attributen des Kunden in Braze hinzugefügt wurde, können Sie es in Ihren Kampagnen verwenden.

Bearbeiten Sie den Nachrichtentext und fügen Sie das in der Voucherify-Verteilung definierte benutzerdefinierte Attribut hinzu. Platzieren Sie {% raw %}`{{custom_attribute.${custom_attribute_with_code}}}`{% endraw %}, um den eindeutigen Code anzuzeigen.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_body.png %}){: style="max-width:75%;"}

Wenn er fertig ist, sehen Sie den Code in Ihrer Nachrichtenvorschau.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_preview.png %})
