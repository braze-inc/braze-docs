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

{% alert note %}
Sie können [mehrere WhatsApp Business-Konten](({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/)) zu einem Braze Workspace hinzufügen. Jedes spezifische WhatsApp Business-Konto kann jedoch nur einem Braze Workspace hinzugefügt werden.
{% endalert %}

## Zugriff auf den Workflow

Gehen Sie zu **Partner-Integrationen** > **Technologiepartner**, suchen Sie dann nach **WhatsApp** und wählen Sie es aus. Ihre nächste Auswahl hängt von Ihrem Anwendungsfall ab:

- Wenn Sie WhatsApp in Ihren Workspace integrieren möchten, wählen Sie **Integration beginnen** aus. <br><br>]({% image_buster /assets/img/whatsapp/whatsapp1.png %})WhatsApp Partnerseite mit einem Button, um die Integration zu beginnen.{: style="max-width:80%;"}()<br><br>
- Wenn Sie ein WhatsApp Business-Konto zu einer bestehenden WhatsApp-Integration hinzufügen möchten, wählen Sie **WhatsApp Business-Konto hinzufügen**. <br><br>]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})"WhatsApp Messaging Integration" mit Optionen zum Hinzufügen eines WhatsApp Business Accounts oder einer Abo-Gruppe und einer Nummer.{: style="max-width:80%;"}()

Der Arbeitsablauf von hier aus ist für beide Anwendungsfälle gleich.

## In WhatsApp eingebetteter Anmelde-Workflow

1. Wählen Sie im Anmeldefenster von Meta (Facebook) **Anmelden als** oder **Weiter**. <br><br>]({% image_buster /assets/img/whatsapp/login_screen.png %})Meta-Anmeldefenster.{: style="max-width:60%;"}()<br><br>
2. Lesen Sie die Berechtigungen, die Sie mit Braze teilen werden, und wählen Sie dann **Starten**. <br><br>]({% image_buster /assets/img/whatsapp/get_started.png %})Liste der Berechtigungen, die Sie für die Integration mit Braze teilen werden.{: style="max-width:50%;"}()<br><br>
3. Wählen Sie in der Dropdown-Liste **Geschäftsportfolio** Ihr Geschäftsportfolio aus und wählen Sie dann **Weiter**. Dies stellt eine Verbindung zu Ihrem WhatsApp Business-Konto her. Wenn Sie also Ihr erwartetes Business-Portfolio nicht sehen, überprüfen Sie Ihre Berechtigungen.<br><br>]({% image_buster /assets/img/whatsapp/business_info.png %})Ein Fenster mit Feldern zur Eingabe Ihrer Geschäftsinformationen, einschließlich des Namens Ihres Geschäftsportfolios.{: style="max-width:50%;"}()<br><br>
4. Wählen Sie in den Dropdown-Feldern Folgendes aus und wählen Sie dann **Weiter**.
- **Wählen Sie ein WhatsApp Business-Konto**: Erstellen Sie ein WhatsApp Geschäftskonto
- **Erstellen oder wählen Sie ein WhatsApp Business-Profil**: Erstellen Sie ein neues WhatsApp-Geschäftsprofil <br><br>]({% image_buster /assets/img/whatsapp/create_select_waba.png %})Felder zur Angabe, ob Sie ein WhatsApp Business-Konto und -Profil auswählen oder erstellen.{: style="max-width:50%;"}()<br><br>
5. Machen Sie die folgenden Angaben und wählen Sie dann **Weiter**.
- WhatsApp Geschäftskonto Name
- WhatsApp-Anzeigename für Unternehmen
- Kategorie <br><br>]({% image_buster /assets/img/whatsapp/waba_details.png %})Felder zur Angabe von Details für das neue WhatsApp Business-Konto.{: style="max-width:50%;"}()<br><br>
6. Geben Sie Ihre Telefonnummer ein und wählen Sie entweder **Textnachricht** oder **Telefonanruf**. Diese Nummer muss alle Anforderungen an eine WhatsApp-Telefonnummer erfüllen, einschließlich der, dass sie nicht für andere WhatsApp-Konten registriert ist. <br><br>]({% image_buster /assets/img/whatsapp/add_phone_number.png %})Felder zum Hinzufügen einer Telefonnummer.{: style="max-width:50%;"}()<br><br>
7. Geben Sie Ihren Code für die Zwei-Faktor-Authentifizierung ein und wählen Sie dann **Weiter**. <br><br>]({% image_buster /assets/img/whatsapp/two_factor.png %})Ein Eingabefeld für einen Zwei-Faktor-Authentifizierungs Code.{: style="max-width:50%;"}()<br><br>
8. Überprüfen Sie die Berechtigungen, die Ihr WhatsApp Business-Konto erhalten wird, und wählen Sie dann **Weiter**. <br><br>]({% image_buster /assets/img/whatsapp/permissions.png %})Liste der vom WhatsApp Business-Konto angefragten Berechtigungen.{: style="max-width:50%;"}()<br><br>
9. Sie sind fertig! <br><br>]({% image_buster /assets/img/whatsapp/finish.png %})Fenster, das anzeigt, dass Sie bereit sind, mit dem Messaging zu beginnen.{: style="max-width:50%;"}()

