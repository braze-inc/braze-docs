---
nav_title: Shopify Benutzeridentitätsmanagement
article_title: "Shopify Benutzeridentitätsmanagement"
description: "Dieser referenzierte Artikel beschreibt das Feature zur Verwaltung der Nutzer:innen in Shopify."
page_type: partner
search_tag: Partner
alias: "/shopify_user_identity/"
page_order: 3
---

# Verwaltung der Nutzer:innen in Shopify

> Braze empfängt Signale von Ihren Shopify-Kunden durch deren On-Site-Verhalten und durch Abhören von Shopify-Webhooks, die Sie im Rahmen Ihrer Integration konfiguriert haben. Bei Shopify-Websites, die nicht ohne Kopfzeile arbeiten, hilft Braze beim Abgleich der Nutzer:innen auf der Kassenseite. Für Shopify-Websites ohne Kopfzeile referenzieren Sie auf unsere Integrationsanleitung, wie Sie [Nutzer:innen aus der Kasse abgleichen]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#headless-checkout) können.

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## Erfassen von Informationen für Nutzer:innen-Profile 

### Shopify Nutzer:innen Tracking

Wenn Ihre Shop-Besucher Gäste sind (d.h. anonym), erfasst Braze die `device_id` für die Sitzungen dieser Kund:innen. Nachdem Sie bei der [Implementierung des Internet SDK]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk) einen Benutzerabgleich für Shopify-Formulare eingerichtet haben, werden den anonymen Nutzerprofilen E-Mails hinzugefügt, wenn Nutzer:innen ihre Daten in ein Formular eingeben. 

Wenn Shop-Besucher ihre E-Mail in einen Shopify-Newsletter oder ein E-Mail-Erfassungsformular eingeben, erhält Braze ein Shopify-Webhook-Ereignis, um das Nutzerprofil zu erstellen. Braze führt dieses Nutzerprofil dann mit dem anonymen Nutzerprofil zusammen, das vom Internet SDK getrackt wird, und weist die Shopify Kunden-ID als Nutzer-Alias im Nutzerprofil zu. 

Wenn Kunden zur Kasse gehen und andere identifizierbare Daten wie Telefonnummern angeben, muss Braze die entsprechenden Nutzerdaten von Shopify-Webhooks erfassen und sie mit dem anonymen Nutzer:in mit dem `device_id` zusammenführen.
- Wenn Sie das Internet SDK über Shopify ScriptTag, auf einer nicht-kopflosen Shopify-Website oder über den Google Tag Manager implementiert haben, sorgt Braze automatisch dafür, dass die Nutzerdaten von der Checkout-Seite und die Sitzungsdaten aus dem anonymen Nutzerprofil mit der zugewiesenen Shopify Kund:in-Profil zusammengeführt werden.
- Wenn Sie das Web SDK auf einer Shopify Headless-Website implementiert haben, müssen Sie sicherstellen, dass die Nutzerdaten, die auf der Kassenseite übermittelt werden, entweder über das Web SDK oder die API dem richtigen Nutzerprofil zugeordnet werden. Weitere Informationen finden Sie unter [Implementierung des Internet SDK direkt auf Ihrer Shopify-Website ohne Kopfhörer]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#headless-site).

Wenn Kunden den Bestellvorgang fortsetzen, prüft Braze, ob die von ihnen eingegebene E-Mail Adresse, Telefonnummer oder Shopify Kunden:in mit einem bestehenden Nutzerprofil übereinstimmt. Wenn es eine Übereinstimmung gibt, synchronisiert Braze die Nutzerdaten von Shopify mit diesem Profil.

Wenn die E-Mail Adresse oder Telefonnummer mit mehreren identifizierten Nutzerprofilen verbunden ist, synchronisiert Braze die Shopify Daten mit dem Profil mit der jüngsten Aktivität.

Wenn Braze keine Übereinstimmung für die E-Mail Adresse oder Telefonnummer findet, erstellt Braze ein neues Nutzerprofil mit den unterstützten Shopify Daten.

### Wenn Shopify Kund:innen mit Braze synchronisieren

Braze aktualisiert bestehende Nutzerprofile oder erstellt neue Profile für Leads, Registrierungen und Nutzer:innen, die in Ihrem Shopify Shop erfasst wurden. Sie können Nutzerprofile mit den folgenden Methoden in Shopify erfassen und mehr:
- Kund:in erstellt ein Konto
- Die E-Mail Adresse oder Telefonnummer des Kunden wird in einem Shopify Erfassungsformular erfasst
- Die E-Mail Adresse der Kund:in wird über ein Newsletter-Formular erfasst
- Die E-Mail Adresse oder Telefonnummer der Kund:in wird über ein Drittanbieter-Tool erfasst, das mit Shopify verbunden ist, wie z.B. EcomSend

Braze versucht zunächst, die unterstützten Shopify Daten anhand der E-Mail Adresse oder der Telefonnummer des Nutzers:innen den vorhandenen Nutzerprofilen zuzuordnen. 

Um doppelte Nutzerprofile zu vermeiden, ist es wichtig, dass Sie die Anweisungen zum Nutzerabgleich für Shopify Forms für die Methode überprüfen, die Sie zur [Implementierung des Internet SDK auf Ihrer Shopify Website]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk) verwendet haben.

## Nutzerprofile zusammenführen 

{% alert note %}
Die Standard Shopify Integration bietet Tools, die Sie beim Zusammenführen Ihres anonymen Nutzerprofils und des Shopify Alias-Profils unterstützen. Wenn Sie die Integration in eine Shopify-Website ohne Kopfzeile implementieren, lesen Sie den Abschnitt [Implementieren des Web SDK direkt auf Ihrer Shopify-Website ohne Kopfzeile]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=headless%20shopify%20site#supported-features), um sicherzustellen, dass Sie Ihre Nutzer:innen richtig abgleichen. <br><br> Wenn Sie auf doppelte Nutzer:innen-Profile stoßen, können Sie unser [Tool zur Zusammenführung von]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging/) Daten verwenden, um Ihre Daten zu bereinigen.
{% endalert %}

Braze führt die Felder des anonymen Nutzerprofils mit dem identifizierten Nutzerprofil zusammen, wenn wir eine Übereinstimmung mit einer der folgenden Angaben finden:
- Shopify ID für Kund:innen
- E-Mail
- Telefonnummer

Braze führt die folgenden Felder des anonymen Nutzerprofils mit dem identifizierten Nutzerprofil zusammen:
- Vorname
- Nachname
- E-Mail
- Geschlecht
- Geburtsdatum
- Telefonnummer
- Zeitzone
- Wohnort
- Land
- Sprache
- Angepasste Attribute
    - Angepasste Event- und Kauf-Event Daten (ohne Event-Eigenschaften, Zählung und Zeitstempel des ersten und letzten Datums)
    - Angepasste Event- und Kauf-Event-Eigenschaften für die Segmentierung "X mal in Y Tagen" (wobei X<=50 und Y<=30)
- Push-Token
- Verlauf der Nachrichten
- Jedes der folgenden Felder des anonymen Nutzerprofils oder des identifizierten Nutzerprofils, wie z.B. angepasstes Event, Anzahl der Kauf-Events und Zeitstempel für das erste und letzte Datum
    - Diese zusammengeführten Felder aktualisieren die Filter "für X Ereignisse in Y Tagen". Bei Kauf-Events umfassen diese Filter "Anzahl der Käufe in Y Tagen" und "Geldausgabe in den letzten Y Tagen".

{% alert important %}
Sitzungsdaten werden im Rahmen des Zusammenführungsprozesses noch nicht unterstützt.
{% endalert %}

## Synchronisierung von Shopify Abonnent:innen

Während der Shopify-Einrichtung bietet Braze flexible Steuerelemente, um die E-Mail-Adressen Ihrer Kund:innen und den Opt-in-Status von SMS mit den Abo-Gruppen und dem Abo-Status der Nutzer:innen-Profile von Braze zu synchronisieren. 

### Sammeln von E-Mail- oder SMS-Abonnenten

Während der Einrichtung Ihres Shopify-Shops in Braze haben Sie die Möglichkeit, Ihre E-Mail- und SMS-Abonnenten von Shopify mit Braze zu synchronisieren. 

#### E-Mail-Abonnent:innen erfassen

Um die Erfassung von E-Mails an Abonnent:innen zu aktivieren, schalten Sie das Feature in Ihrer Shopify-Einrichtung ein. Wir empfehlen Ihnen, mindestens eine [Abo-Gruppe]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups) von Braze zuzuweisen, wie z.B. Shopify E-Mail Abonnent:innen. Braze fügt Ihre E-Mail Abonnenten zu den angegebenen Abo-Gruppen hinzu, so dass sie in Ihr Targeting einbezogen werden, wenn Sie eine Nachricht senden. 

![]({% image_buster /assets/img/Shopify/collect_email.png %})

Wenn diese Funktion aktiviert ist, synchronisiert Braze Updates für Ihre Shopify E-Mail Abonnenten und Updates für deren E-Mail Abonnent:innen in Realtime. Wenn Sie die Überschreibungsoption nicht aktivieren, werden Ihre Shopify Kunden entweder von der mit Ihrem Shopify Shop verbundenen Abo-Gruppe abgemeldet oder abgemeldet.

Wenn Sie die Überschreibungsoption aktivieren, aktualisiert Braze den globalen Abo-Status im Nutzerprofil. Das bedeutet, wenn Ihre Kunden in Shopify als abgemeldet markiert sind, markiert Braze den globalen Abo-Status im Nutzerprofil als abgemeldet und meldet den Kunden von allen verfügbaren E-Mail Abo-Gruppen ab. Infolgedessen werden keine Nachrichten an Nutzer:innen gesendet, die sich global von E-Mails abgemeldet haben.

#### SMS-Abonnent:innen erfassen

Um SMS-Abonnenten von Shopify zu sammeln, müssen Sie im Rahmen Ihrer [SMS-Einrichtung]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/sms_setup/sms_sending/) [Abo-Gruppen]({{site.baseurl}}/sms_rcs_subscription_groups/) erstellen. 

Wenn Sie bereit sind, Ihre Shopify SMS Abonnenten zu sammeln, aktivieren Sie die Sammlung von SMS Abonnenten, indem Sie sie auf der Shopify Einrichtungsseite einschalten. Sie müssen mindestens eine Abo-Gruppe für SMS auswählen, damit Sie SMS-Nachrichten entsprechend targeting und versenden können. 

![]({% image_buster /assets/img/Shopify/collect_sms.png %})

Wenn diese Funktion aktiviert ist, synchronisiert Braze Updates für Ihre Shopify SMS-Abonnenten und deren Abo-Status in Realtime. Wenn Sie die Überschreibungsoption nicht aktivieren, werden Ihre Shopify Kunden entweder von der mit Ihrem Shopify Shop verbundenen Abo-Gruppe abgemeldet oder abgemeldet.

SMS Abonnenten:innen haben keinen globalen Abo-Status, so dass Sie sie bei der Verwendung einer Überschreibungsoption nicht berücksichtigen müssen. Ein Nutzer:in kann nur von einer SMS-Abo-Gruppe abgemeldet oder abonniert werden.

#### Angepasste Attribute Legacy

Ältere Shopify Kund:innen haben möglicherweise die alte Methode der Erfassung von E-Mail- und SMS-Abonnenten über die angepassten Attribute `shopify_accepts_marketing` und `shopify_sms_consent`. Wenn Sie die obigen Einstellungen mit aktivierter Überschreibung speichern, entfernt Braze die angepassten Attribute in den Nutzerprofilen und synchronisiert diese Werte mit der jeweiligen E-Mail-Abonnementgruppe und SMS-Abonnementgruppe.

Wenn Sie bestehende Kampagnen oder Canvase haben, die diese angepassten Attribute verwenden, entfernen Sie diese Attribute und stellen Sie sicher, dass die Kampagnen oder Canvase den entsprechenden Abo-Status, die entsprechende Gruppe oder beides verwenden.
