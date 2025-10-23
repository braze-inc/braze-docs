---
nav_title: "Geografische Berechtigungen"
article_title: Geografische Berechtigungen
description: "Dieser Artikel behandelt die Länderzulassungsliste für geografische Berechtigungen, mit der Sie festlegen können, in welche Länder SMS, MMS und RCS zugestellt werden können."
page_order: 2
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/
  
---

# Geografische Berechtigungen

> Geografische Berechtigungen erhöhen die Sicherheit und schützen vor betrügerischem SMS-, MMS- und RCS-Verkehr, indem sie die Länder kontrollieren, in die Sie Nachrichten senden können. Sie können eine Liste zulässiger Länder angeben, um sicherzustellen, dass SMS-, MMS- und RCS-Nachrichten nur an zugelassene Regionen gesendet werden. Nur Administratoren können Änderungen an der Liste der zulässigen Länder vornehmen. Nicht-Administrator-Benutzer haben Zugriff auf eine schreibgeschützte Version der Zulassen-Liste, die angibt, in welche Länder eine Abonnementgruppe senden darf.

Als Administrator:in können Sie die Länder konfigurieren, die auf der Allowlist stehen. Die Länder-Allowlist wird auf der Ebene der [Abo-Gruppe]({{site.baseurl}}/sms_rcs_subscription_groups/) konfiguriert. Sie können darauf zugreifen, indem Sie auf **Zielgruppe** > **Abonnements** gehen und eine SMS-, MMS- oder RCS-Abo-Gruppe auswählen. Die Zulassen-Liste finden Sie unter **Geografische Berechtigungen**.

]({% image_buster /assets/img/sms/sms_geographic_permissions.png %})Der bearbeitbare Bereich für geografische SMS-Berechtigungen für einen Administrator, der mehrere Länder in der "Länderliste" ausgewählt hat.{: style="max-width:80%;"}()

### Länder auswählen

Fügen Sie über das Dropdown-Menü Länder zur Liste der zulässigen Länder hinzu. Die gebräuchlichsten SMS- und RCS-Länder werden oben angezeigt, andere darunter. Sie können auch nach Ländern suchen, indem Sie in das Textfeld tippen.

]({% image_buster /assets/img/sms/allowlist_dropdown.png %})Das Dropdown-Menü "Länderzulassungsliste", wobei die gängigsten Länder oben angezeigt werden.{: style="max-width:80%;"}()

Entfernen Sie zuvor ausgewählte Länder, indem Sie die entsprechenden Kontrollkästchen neben den Ländern deaktivieren.

### Speichern Ihrer Änderungen

Die Änderungen werden wirksam, nachdem Sie **Speichern** ausgewählt haben. Wenn Sie Länder aus Ihrer Zulassungsliste entfernen, werden alle SMS-, MMS- und RCS-Nachrichten nicht an Nummern in diesen Ländern gesendet.

]({% image_buster /assets/img/sms/delete_allowlist_warning.png %})Warnung Modal zur Bestätigung der Länder, die aus der Zulassungsliste gelöscht werden.{: style="max-width:70%;"}()

## Länder mit hohem Risiko

In bestimmten Ländern besteht ein höheres Risiko, dass SMS- und RCS-Datenverkehr gepumpt wird. Diese Länder sind in der Dropdown-Liste mit einem **hohen Risiko** gekennzeichnet.

]({% image_buster /assets/img/sms/high_risk.png %})Das Länder-Dropdown mit Aserbaidschan mit einem "Hochrisiko"-Tag.{: style="max-width:80%;"}()

Wenn Sie den Versand in diese Länder zulassen, müssen Sie zunächst das damit verbundene Risiko anerkennen, bevor das Land in Ihre Zulassungsliste aufgenommen wird.

{% alert note %}
Beschränken Sie die Länder auf Ihrer Allowlist auf die Länder, die Sie für Ihre Geschäftsanforderungen benötigen. So minimieren Sie das Potenzial für betrügerischen Traffic. Weitere Hinweise zur Verhinderung von SMS-Traffic-Pumping finden Sie in den [FAQs zu SMS-Traffic-Pumping-Betrug]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

## Sichtbarkeit von blockierten Sendungen

Sendeversuche an Länder, die nicht auf Ihrer Allowlist stehen, werden abgebrochen. Abgebrochene Nachrichten werden im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) und im [Nachrichten-Engagement-Event „SMS-Abbruch“]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) protokolliert. 

Abgebrochene Nachrichten, die durch blockierte Sendungen verursacht wurden, werden als **Fehler bei abgebrochenen Nachrichten** angezeigt und enthalten die Nachricht "Die Telefonnummer des Empfängers befindet sich in einem blockierten Land".

]({% image_buster /assets/img/sms/abort_log.png %})Abbruchprotokoll mit mehreren SMS-Sendungen, die blockiert wurden, weil die Telefonnummer in einem blockierten Land liegt.{: style="max-width:80%;"}()

