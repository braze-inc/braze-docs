---
nav_title: Eingebettete Anmeldung
article_title: Eingebettete WhatsApp-Anmeldung
page_order: 0
description: "Dieser Referenzartikel bietet eine Schritt-für-Schritt-Anleitung für den in WhatsApp eingebetteten Anmelde-Workflow in Braze."
page_type: reference
channel:
  - WhatsApp
---

# Eingebettete WhatsApp-Anmeldung

> Dieser Referenzartikel bietet eine Schritt-für-Schritt-Anleitung für den in WhatsApp eingebetteten Anmelde-Workflow in Braze.

Der in WhatsApp eingebettete Anmelde-Workflow wird aufgerufen, wenn Sie [WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) zum ersten Mal in Ihren Braze-Workspace [integrieren]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) und wenn Sie [ein WhatsApp-Business-Konto]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/) zu einer bestehenden WhatsApp-Integration [hinzufügen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/).

## Zugriff auf den Workflow

Gehen Sie zu **Partner-Integrationen** > **Technologiepartner**, suchen Sie dann nach **WhatsApp** und wählen Sie es aus. Ihre nächste Auswahl hängt von Ihrem Anwendungsfall ab:

- Wenn Sie WhatsApp in Ihren Workspace integrieren möchten, wählen Sie **Integration beginnen** aus. <br><br>![][10]{: style="max-width:80%;"}<br><br>
- Wenn Sie ein WhatsApp Business-Konto zu einer bestehenden WhatsApp-Integration hinzufügen möchten, wählen Sie **WhatsApp Business-Konto hinzufügen**. <br><br>![][11]{: style="max-width:80%;"}

Der Arbeitsablauf von hier aus ist für beide Anwendungsfälle gleich.

## In WhatsApp eingebetteter Anmelde-Workflow

1. Wählen Sie im Anmeldefenster von Meta (Facebook) **Anmelden als** oder **Weiter**. <br><br>![Meta-Anmeldefenster.][1]{: style="max-width:60%;"}<br><br>
2. Lesen Sie die Berechtigungen, die Sie mit Braze teilen werden, und wählen Sie dann **Starten**. <br><br>![Liste der Berechtigungen, die Sie für die Integration mit Braze teilen werden.][2]{: style="max-width:50%;"}<br><br>
3. Wählen Sie in der Dropdown-Liste **Geschäftsportfolio** Ihr Geschäftsportfolio aus und wählen Sie dann **Weiter**. Dies stellt eine Verbindung zu Ihrem WhatsApp Business-Konto her. Wenn Sie also Ihr erwartetes Business-Portfolio nicht sehen, überprüfen Sie Ihre Berechtigungen.<br><br>![Ein Fenster mit Feldern zur Eingabe Ihrer Geschäftsinformationen, einschließlich des Namens Ihres Geschäftsportfolios.][3]{: style="max-width:50%;"}<br><br>
4. Wählen Sie in den Dropdown-Feldern Folgendes aus und wählen Sie dann **Weiter**.
- **Wählen Sie ein WhatsApp Business-Konto**: Erstellen Sie ein WhatsApp Geschäftskonto
- **Erstellen oder wählen Sie ein WhatsApp Business-Profil**: Erstellen Sie ein neues WhatsApp-Geschäftsprofil <br><br>![Felder, die Sie ausfüllen müssen, wenn Sie ein WhatsApp-Business-Konto und -Profil auswählen oder erstellen.][4]{: style="max-width:50%;"}<br><br>
5. Machen Sie die folgenden Angaben und wählen Sie dann **Weiter**.
- WhatsApp Geschäftskonto Name
- WhatsApp-Anzeigename für Unternehmen
- Kategorie <br><br>![Felder zur Angabe von Details für das neue WhatsApp Business-Konto.][5]{: style="max-width:50%;"}<br><br>
6. Geben Sie Ihre Telefonnummer ein und wählen Sie entweder **Textnachricht** oder **Telefonanruf**. Diese Nummer muss alle Anforderungen an eine WhatsApp-Telefonnummer erfüllen, einschließlich der, dass sie nicht für andere WhatsApp-Konten registriert ist. <br><br>![Felder zum Hinzufügen einer Telefonnummer.][6]{: style="max-width:50%;"}<br><br>
7. Geben Sie Ihren Code für die Zwei-Faktor-Authentifizierung ein und wählen Sie dann **Weiter**. <br><br>![Ein Eingabefeld für einen Zwei-Faktor-Authentifizierungscode.][7]{: style="max-width:50%;"}<br><br>
8. Überprüfen Sie die Berechtigungen, die Ihr WhatsApp Business-Konto erhalten wird, und wählen Sie dann **Weiter**. <br><br>![Liste der vom WhatsApp Business-Konto angeforderten Berechtigungen.][8]{: style="max-width:50%;"}<br><br>
9. Sie sind fertig! <br><br>![Fenster, das anzeigt, dass Sie bereit sind, Nachrichten an Personen zu senden.][9]{: style="max-width:50%;"}

[1]: {% image_buster /assets/img/whatsapp/login_screen.png %}
[2]: {% image_buster /assets/img/whatsapp/get_started.png %}
[3]: {% image_buster /assets/img/whatsapp/business_info.png %}
[4]: {% image_buster /assets/img/whatsapp/create_select_waba.png %}
[5]: {% image_buster /assets/img/whatsapp/waba_details.png %}
[6]: {% image_buster /assets/img/whatsapp/add_phone_number.png %}
[7]: {% image_buster /assets/img/whatsapp/two_factor.png %}
[8]: {% image_buster /assets/img/whatsapp/permissions.png %}
[9]: {% image_buster /assets/img/whatsapp/finish.png %}
[10]: {% image_buster /assets/img/whatsapp/whatsapp1.png %}
[11]: {% image_buster /assets/img/whatsapp/multiple_wabas.png %} 