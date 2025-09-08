---
nav_title: Dynamische SMS Link Vorschau
article_title: Dynamische SMS Link Vorschau
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie das Feature der SMS-Linkvorschau von Movable Ink einschalten und nutzen können."
page_type: partner
search_tag: Partner
---

# Dynamische SMS-Link-Vorschau

> Mit der dynamischen Vorschau auf SMS-Links von Movable Ink können Sie die Unmittelbarkeit von MMS zu den gleichen Kosten wie bei SMS nutzen. Dies erlaubt es Ihnen, mit Braze und Movable Ink kostengünstige, personalisierte Messaging-Erlebnisse zu liefern.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Movable Ink Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Movable Ink-Konto. |
| Datenquelle | Sie müssen eine Datenquelle mit Movable Ink verbinden. Dies kann über CSV, Website-Import oder API geschehen. |
| MMS-Versandmöglichkeiten | Bestätigen Sie, dass Sie für MMS über Braze eingerichtet sind.
| [Link-Verkürzung]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) | Vergewissern Sie sich, dass die Linkverkürzung aktiviert ist. | 
| Kontaktkarte | Ihre Marke (der Sender) muss als Kontakt auf dem Telefon des Nutzers:innen gespeichert sein, damit die Link-Vorschau unter iOS funktioniert. Dies kann mit einer Kontaktkarte oder einer anderen Methode geschehen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Folgen Sie den jeweiligen Schritten unten, um dynamische SMS-Links für iOS- und Android-Betriebssysteme zu versenden.

### iOS

{% alert important %}
Um eine Vorschau der Links für iOS zuzulassen, müssen Nutzer:innen Ihre Marke (den Sender) als Kontakt hinzufügen.
{% endalert %}

#### Schritt 1: Erstellen Sie eine Kampagne für Kontaktkarten

Nachdem Nutzer:innen Ihre Marke als Kontakt gespeichert haben, entweder über eine [Kontaktkarte]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) oder eine andere Methode, können sie die Aufforderungen **zum Laden der Vorschau** und Movable Ink-Links sehen.

![1]{: style="max-width:30%;"}

#### Schritt 2: Movable Ink Links versenden

1. Erstellen Sie eine SMS-Kampagne in Movable Ink und generieren Sie Ihre Click-through-URL.
2. Gehen Sie im Braze-Dashboard zu **Kampagnen** und richten Sie eine neue SMS/MMS-Kampagne über das Dropdown-Menü **Kampagne erstellen** ein.
3. In der SMS-Kampagne Komponist:
    - Legen Sie Ihre Abo-Gruppe fest.
    - Geben Sie Ihre Nachricht ein.
    - Fügen Sie Ihren Movable Ink-Link **als letztes** ein, nach allen anderen Texten im Textkörper der Nachricht. <br><br>![2]{: style="max-width:50%;"}

{% alert tip %}
Sehen Sie sich [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) an, um die Personalisierung von Liquid aufzufrischen.  
{% endalert %}

{: start="4"}
4\. Jetzt können Sie Ihre dynamische SMS-Link-Vorschau-Kampagne testen und starten.

![3]{: style="max-width:70%;"}

Nachdem Nutzer:innen die Vorschau des Links geladen haben, wird ein personalisiertes Bild gerendert, mit der Möglichkeit, einen Link zu Ihrer Website, App oder Landing Page zu erstellen.

![4]{: style="max-width:30%;"}

### Android (Google- und Samsung-Geräte)

Android Nutzer:innen müssen Ihre Marke nicht als Kontakt speichern, um dynamische SMS-Link-Vorschauen zu erhalten. Es ist aber dennoch empfehlenswert, damit das Gerät die Link-Vorschauen automatisch laden kann.

![5 ]{: style="max-width:30%;"}

Nutzer:innen, die Ihre Marke nicht als Kontakt gespeichert und die automatische Vorschau aktiviert haben, müssen **Vorschau auswählen**, um das Vorschaubild zu laden.

![6]{: style="max-width:30%;"}

## Überlegungen

- Fügen Sie nur einen Link zur Vorschau in Ihre Nachricht ein. Es werden keine Inhalte mit mehreren Links in Ihrem SMS-Text generiert. 
- Fügen Sie keine Zeichen nach dem Link zur Vorschau ein, da sonst das Erlebnis unterbrochen werden könnte.


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}
