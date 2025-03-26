---
nav_title: Dynamische SMS-Link-Vorschau
article_title: Dynamische SMS-Link-Vorschau
description: "In diesem Referenzartikel erfahren Sie, wie Sie die SMS-Linkvorschau von Movable Ink einschalten und verwenden können."
page_type: partner
search_tag: Partner
---

# Dynamische SMS-Link-Vorschau

> Mit der dynamischen SMS-Linkvorschau von Movable Ink können Sie die Unmittelbarkeit von MMS zu den gleichen Kosten wie bei SMS nutzen. So können Sie Braze und Movable Ink nutzen, um kostengünstige, personalisierte Rich Messaging-Erlebnisse zu liefern.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Movable Ink Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Movable Ink-Konto. |
| Datenquelle | Sie müssen eine Datenquelle mit Movable Ink verbinden. Dies kann über CSV, Website-Import oder API erfolgen. |
| MMS-Versandmöglichkeiten | Bestätigen Sie, dass Sie für MMS über Braze eingerichtet sind.
| [Link-Verkürzung]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/) | Vergewissern Sie sich, dass die Linkverkürzung aktiviert ist. | 
| Kontaktkarte | Ihre Marke (der Absender) muss als Kontakt auf dem Telefon des Benutzers gespeichert sein, damit die Linkvorschau unter iOS funktioniert. Dies kann mit einer Kontaktkarte oder einer anderen Methode geschehen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Folgen Sie den jeweiligen Schritten unten, um dynamische SMS-Links für iOS- und Android-Betriebssysteme zu versenden.

### iOS

{% alert important %}
Um Link-Vorschaubilder für iOS zuzulassen, müssen Benutzer Ihre Marke (den Absender) als Kontakt hinzufügen.
{% endalert %}

#### Schritt 1: Erstellen Sie eine Kontaktkartenkampagne

Nachdem Benutzer Ihre Marke als Kontakt gespeichert haben, entweder über eine [Kontaktkarte]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/) oder eine andere Methode, können sie die **Tap to Load-Vorschauaufforderungen** und Movable Ink-Links sehen.

![1]{: style="max-width:30%;"}

#### Schritt 2: Movable Ink Links versenden

1. Erstellen Sie eine SMS-Kampagne in Movable Ink und generieren Sie Ihre Click-Through-URL.
2. Gehen Sie im Braze Dashboard zu **Kampagnen** und richten Sie eine neue SMS/MMS-Kampagne aus dem Dropdown-Menü **Kampagne erstellen** ein.
3. Im SMS-Kampagnen-Composer:
    - Legen Sie Ihre Abonnementgruppe fest.
    - Geben Sie Ihre Nachricht ein.
    - Fügen Sie Ihren Movable Ink-Link **als letztes** ein, nach allen anderen Texten im Nachrichtentext. <br><br>![2]{: style="max-width:50%;"}

{% alert tip %}
Sehen Sie sich [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) an, um die Personalisierung von Liquid aufzufrischen.  
{% endalert %}

{: start="4"}
4\. Sie können nun Ihre dynamische SMS-Link-Vorschaukampagne testen und starten.

![3]{: style="max-width:70%;"}

Nachdem Nutzer die Linkvorschau geladen haben, wird ein personalisiertes Bild mit der Möglichkeit, einen Link zu Ihrer Website, App oder Landing Page zu erstellen, angezeigt.

![4]{: style="max-width:30%;"}

### Android (Google- und Samsung-Geräte)

Android-Nutzer müssen Ihre Marke nicht als Kontakt speichern, um dynamische SMS-Link-Vorschauen zu erhalten. Es ist aber dennoch empfehlenswert, damit das Gerät die Linkvorschauen automatisch laden kann.

![5]{: style="max-width:30%;"}

Benutzer, die Ihre Marke nicht als Kontakt gespeichert und die automatische Vorschau aktiviert haben, müssen auf **Vorschau laden tippen**, um das Vorschaubild zu laden.

![6]{: style="max-width:30%;"}

## Überlegungen

- Fügen Sie nur einen Vorschaulink in Ihre Nachricht ein. Es werden keine Inhalte mit mehreren Links in Ihrem SMS-Text erstellt. 
- Fügen Sie nach dem Vorschaulink keine Zeichen ein, da sonst das Erlebnis unterbrochen werden könnte.


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}
