---
nav_title: Shopify Benutzer-Identitätsmanagement
article_title: "Shopify Benutzer-Identitätsmanagement"
description: "Dieser Referenzartikel beschreibt die Shopify-Funktion zur Verwaltung der Benutzeridentität."
page_type: partner
search_tag: Partner
alias: "/shopify_user_identity/"
page_order: 3
---

# Shopify Benutzeridentitätsverwaltung

> Braze empfängt Signale von Ihren Shopify-Kunden durch deren Verhalten vor Ort und durch das Abhören von Shopify-Webhooks, die Sie im Rahmen Ihrer Integration konfiguriert haben. Bei nicht-kopflosen Shopify-Websites hilft Braze bei der Abstimmung der Benutzer auf der Kassenseite. Für Shopify-Websites ohne Kopfzeile finden Sie in unserer Integrationsanleitung Hinweise zum [Abgleich von Benutzern an der Kasse]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#headless-checkout).

## Erfassen von Informationen für Benutzerprofile 

### Shopify Benutzerverfolgung

Wenn Ihre Shop-Besucher Gäste sind (d.h. anonym), erfasst Braze die `device_id` für die Sitzungen dieser Kunden. Nachdem Sie bei der [Implementierung des Web SDK]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk) einen Benutzerabgleich für Shopify-Formulare eingerichtet haben, werden Kunden-E-Mails zu anonymen Benutzerprofilen hinzugefügt, sobald Kunden ihre Informationen in ein Formular eingeben. 

Wenn Ladenbesucher ihre E-Mail in einen Shopify-Newsletter oder ein E-Mail-Erfassungsformular eingeben, erhält Braze ein Shopify-Webhook-Ereignis, um das Benutzerprofil zu erstellen. Braze führt dieses Benutzerprofil dann mit dem anonymen Benutzerprofil zusammen, das vom Web SDK verfolgt wird, und weist die Shopify-Kunden-ID als Benutzer-Alias im Benutzerprofil zu. 

Wenn Kunden zur Kasse gehen und andere identifizierbare Informationen, wie Telefonnummern, angeben, muss Braze die entsprechenden Benutzerdaten von Shopify-Webhooks erfassen und sie mit dem anonymen Benutzer mit der `device_id` zusammenführen.
- Wenn Sie das Web SDK über Shopify ScriptTag, auf einer nicht-kopflosen Shopify-Website oder über Google Tag Manager implementiert haben, sorgt Braze automatisch dafür, dass die Benutzerdaten von der Checkout-Seite und die Sitzungsdaten aus dem anonymen Benutzerprofil mit dem Benutzer-Alias-Profil mit der zugewiesenen Shopify-Kunden-ID zusammengeführt werden.
- Wenn Sie das Web SDK auf einer Shopify Headless-Website implementiert haben, müssen Sie sicherstellen, dass die auf der Kassenseite übermittelten Benutzerdaten entweder über das Web SDK oder die API dem richtigen Benutzerprofil zugewiesen werden. Weitere Informationen finden Sie unter [Implementierung des Web SDK direkt auf Ihrer Shopify-Website]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#headless-site).

Wenn der Kunde mit dem Bezahlvorgang fortfährt, prüft Braze, ob die eingegebene E-Mail-Adresse, Telefonnummer oder Shopify-Kunden-ID mit einem bestehenden Benutzerprofil übereinstimmt. Wenn es eine Übereinstimmung gibt, synchronisiert Braze die Shopify-Benutzerdaten mit diesem Profil.

Wenn die E-Mail-Adresse oder Telefonnummer mit mehreren identifizierten Benutzerprofilen verbunden ist, synchronisiert Braze die Shopify-Daten mit dem Profil mit der jüngsten Aktivität.

Wenn Braze keine Übereinstimmung für die E-Mail-Adresse oder Telefonnummer findet, erstellt Braze ein neues Benutzerprofil mit den unterstützten Shopify-Daten.

### Wenn Shopify-Kunden mit Braze synchronisieren

Braze aktualisiert bestehende Benutzerprofile oder erstellt neue Profile für Leads, Anmeldungen und Kontoregistrierungen, die in Ihrem Shopify-Shop erfasst wurden. Sie können Benutzerprofildaten mit den folgenden Methoden in Shopify und weiteren Methoden erfassen:
- Kunde erstellt ein Konto
- Die E-Mail-Adresse oder Telefonnummer des Kunden wird in einem Shopify-Erfassungsformular erfasst.
- Die E-Mail-Adresse des Kunden wird über ein Newsletter-Formular erfasst
- Die E-Mail-Adresse oder Telefonnummer des Kunden wird über ein Drittanbieter-Tool erfasst, das mit Shopify verbunden ist, z. B. EcomSend

Braze versucht zunächst, die unterstützten Shopify-Daten anhand der E-Mail-Adresse oder der Telefonnummer des Kunden den vorhandenen Benutzerprofilen zuzuordnen. 

Um doppelte Benutzerprofile zu vermeiden, müssen Sie unbedingt die Anweisungen zum Benutzerabgleich für Shopify Forms für die Methode überprüfen, die Sie zur [Implementierung des Web SDK auf Ihrer Shopify-Website]() verwendet haben.

## Zusammenführung von Benutzerprofilen 

{% alert note %}
Die standardmäßige Shopify-Integration bietet Tools, die Sie beim Zusammenführen Ihres anonymen Benutzerprofils und des Shopify-Aliasprofils unterstützen. Wenn Sie die Integration in eine Shopify-Website ohne Kopfzeile implementieren, lesen Sie den Abschnitt [Implementieren des Web-SDK direkt auf Ihrer Shopify-Website ohne Kopfzeile]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=headless%20shopify%20site#supported-features), um sicherzustellen, dass Sie Ihre Benutzer richtig abgleichen. <br><br> Wenn Sie auf doppelte Benutzerprofile stoßen, können Sie unser [Tool zur Massenzusammenführung]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging/) verwenden, um Ihre Daten zu bereinigen.
{% endalert %}

Braze führt die Felder aus dem anonymen Benutzerprofil mit dem identifizierten Benutzerprofil zusammen, wenn wir eine Übereinstimmung mit einem der folgenden Punkte finden:
- Shopify Kunden-ID
- E-Mail
- Telefonnummer

Braze führt die folgenden Felder aus dem anonymen Benutzerprofil mit dem identifizierten Benutzerprofil zusammen:
- Vorname
- Nachname
- E-Mail
- Geschlecht
- Geburtsdatum
- Telefonnummer
- Zeitzone
- Heimatstadt
- Land
- Sprache
- Angepasste Attribute
    - Benutzerdefinierte Ereignis- und Kaufereignisdaten (ohne Ereigniseigenschaften, Zählung und Zeitstempel für das erste und letzte Datum)
    - Benutzerdefinierte Ereignis- und Kaufereigniseigenschaften für die Segmentierung "X Mal in Y Tagen" (wobei X<=50 und Y<=30)
- Token drücken
- Nachrichtenverlauf
- Jedes der folgenden Felder des anonymen oder identifizierten Benutzerprofils, wie z. B. benutzerdefinierte Ereignisse, Anzahl der Kaufereignisse sowie Zeitstempel für das erste und letzte Datum
    - Diese zusammengeführten Felder aktualisieren die Filter "für X Ereignisse in Y Tagen". Für Kaufereignisse umfassen diese Filter "Anzahl der Käufe in Y Tagen" und "Geldausgabe in den letzten Y Tagen".

{% alert important %}
Sitzungsdaten werden im Rahmen des Zusammenführungsprozesses noch nicht unterstützt.
{% endalert %}

## Synchronisierung von Shopify-Abonnenten

Während der Shopify-Einrichtung bietet Braze flexible Steuerelemente, um Ihre Kunden-E-Mail-Adressen und SMS-Opt-in-Status mit den Abonnementgruppen und dem Abonnementstatus der Braze-Benutzerprofile zu synchronisieren. 

### Sammeln von E-Mail- oder SMS-Abonnenten

Während der Einrichtung Ihres Shopify-Shops in Braze haben Sie die Möglichkeit, Ihre E-Mail- und SMS-Abonnenten von Shopify mit Braze zu synchronisieren. 

#### Sammeln Sie E-Mail-Abonnenten

Um die Sammlung von E-Mail-Abonnenten zu aktivieren, schalten Sie die Funktion in Ihrer Shopify-Einrichtung ein. Wir empfehlen Ihnen, mindestens eine [Braze-Abonnementgruppe]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups) zuzuweisen, z. B. Shopify-E-Mail-Abonnenten. Braze fügt Ihre E-Mail-Abonnenten zu den angegebenen Abonnentengruppen hinzu, so dass sie bei der Zielgruppenansprache berücksichtigt werden, wenn Sie eine Nachricht senden. 

![]({% image_buster /assets/img/Shopify/collect_email.png %})

Wenn diese Funktion aktiviert ist, synchronisiert Braze Aktualisierungen für Ihre Shopify-E-Mail-Abonnenten und Aktualisierungen ihres E-Mail-Abonnementstatus in Echtzeit. Wenn Sie die Überschreibungsoption nicht aktivieren, werden Ihre Shopify-Kunden entweder von der mit Ihrem Shopify-Shop verbundenen Abonnementgruppe abonniert oder abgemeldet.

Wenn Sie die Überschreibungsoption aktivieren, wird Braze den globalen Abonnementstatus im Benutzerprofil aktualisieren. Das bedeutet, dass, wenn Ihre Kunden in Shopify als abgemeldet markiert sind, Braze den globalen Abonnementstatus im Benutzerprofil als abgemeldet markiert und den Kunden aus allen verfügbaren E-Mail-Abonnementgruppen abmeldet. Infolgedessen werden keine Nachrichten an Benutzer gesendet, die global von E-Mails abgemeldet wurden.

#### SMS-Abonnenten sammeln

Um SMS-Abonnenten von Shopify zu sammeln, müssen Sie im Rahmen Ihrer [SMS-Einrichtung]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup) [SMS-Abonnementgruppen]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) erstellen. 

Wenn Sie bereit sind, Ihre Shopify-SMS-Abonnenten zu sammeln, aktivieren Sie die SMS-Abonnentensammlung, indem Sie sie auf der Shopify-Einrichtungsseite einschalten. Sie müssen mindestens eine SMS-Abonnementgruppe auswählen, damit Sie SMS-Nachrichten entsprechend ausrichten und versenden können. 

![]({% image_buster /assets/img/Shopify/collect_sms.png %})

Wenn diese Funktion aktiviert ist, synchronisiert Braze Aktualisierungen für Ihre Shopify SMS-Abonnenten und deren SMS-Abonnementstatus in Echtzeit. Wenn Sie die Überschreibungsoption nicht aktivieren, werden Ihre Shopify-Kunden entweder von der mit Ihrem Shopify-Shop verbundenen Abonnementgruppe abonniert oder abgemeldet.

SMS-Abonnenten haben keinen globalen Abonnementstatus, so dass Sie sie bei der Verwendung einer Überschreibungsoption nicht berücksichtigen müssen. Ein Benutzer kann nur von einer SMS-Abonnementgruppe abgemeldet oder abonniert werden.

#### Veraltete benutzerdefinierte Attribute

Ältere Shopify-Kunden verwenden möglicherweise die alte Methode der Erfassung von E-Mail- und SMS-Abonnenten über die benutzerdefinierten Attribute `shopify_accepts_marketing` und `shopify_sms_consent`. Wenn Sie die obigen Einstellungen mit aktivierter Überschreibung speichern, entfernt Braze die benutzerdefinierten Attribute in den Benutzerprofilen und synchronisiert diese Werte mit der jeweiligen E-Mail-Abonnementgruppe und SMS-Abonnementgruppe.

Wenn Sie bestehende Kampagnen oder Canvases haben, die diese alten benutzerdefinierten Attribute verwenden, entfernen Sie diese Attribute und stellen Sie sicher, dass die Kampagnen oder Canvases den richtigen Abonnementstatus, die richtige Gruppe oder beides verwenden.
