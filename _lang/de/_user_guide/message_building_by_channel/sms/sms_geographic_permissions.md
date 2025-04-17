---
nav_title: "Geografische Berechtigungen für SMS"
article_title: Geografische Berechtigungen für SMS
description: "Dieser Artikel befasst sich mit der Länderliste für die geografischen SMS-Berechtigungen, mit der Sie festlegen können, in welche Länder SMS zugestellt werden können."
page_order: 4.5
page_type: reference
channel:
  - SMS
alias: "/sms_geographic_permissions/"
  
---

# Geografische Berechtigungen für SMS

> Die geografischen SMS-Berechtigungen erhöhen die Sicherheit und schützen vor betrügerischem SMS-Verkehr, indem sie die Länder kontrollieren, in die Sie SMS-Nachrichten senden können. Sie können eine Liste zulässiger Länder angeben, um sicherzustellen, dass SMS-Nachrichten nur an zugelassene Regionen gesendet werden. Nur Administratoren können Änderungen an der Liste der zulässigen Länder vornehmen. Nicht-Administrator-Benutzer haben Zugriff auf eine schreibgeschützte Version der Zulassen-Liste, die angibt, in welche Länder eine Abonnementgruppe senden darf.

![Der schreibgeschützte Bereich SMS Geographic Permissions für einen Nicht-Administrator, der in der Länderliste die Vereinigten Staaten und das Vereinigte Königreich ausgewählt hat.][6]{: style="max-width:80%;"}

## Konfigurieren Ihrer SMS-Länderzulassungsliste

Als Administrator:in können Sie die Länder konfigurieren, die auf der Allowlist stehen. Die Länder-Allowlist wird auf der Ebene der [Abo-Gruppe]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) konfiguriert. Sie können darauf zugreifen, indem Sie auf **Audience** > **Abonnements** gehen und eine SMS-Abonnementgruppe auswählen. Die Zulassungsliste befindet sich unter **SMS Geografische Berechtigungen**.

![Der bearbeitbare Bereich für geografische SMS-Berechtigungen für eine:n Administrator:in, der oder die Australien, Kanada und die Vereinigten Staaten in der „Länder-Allowlist“ ausgewählt hat.][1]{: style="max-width:80%;"}

### Länder auswählen

Fügen Sie über das Dropdown-Menü Länder zur Liste der zulässigen Länder hinzu. Die gebräuchlichsten SMS-Länder werden oben angezeigt, andere darunter. Sie können auch nach Ländern suchen, indem Sie in das Textfeld tippen.

![Das Dropdown-Menü "Länderliste", in dem die gängigsten Länder ganz oben angezeigt werden.][2]{: style="max-width:80%;"}

Entfernen Sie zuvor ausgewählte Länder, indem Sie die entsprechenden Kontrollkästchen neben den Ländern deaktivieren.

### Speichern Ihrer Änderungen

Die Änderungen werden wirksam, nachdem Sie **Speichern** ausgewählt haben. Wenn Sie Länder aus Ihrer Zulassungsliste entfernen, werden alle SMS- und MMS-Nachrichten an Nummern in diesen Ländern nicht mehr gesendet.

![Warnmeldung zur Bestätigung der Länder, die aus der Allowlist gelöscht werden.][3]{: style="max-width:70%;"}

## Länder mit hohem Risiko

In bestimmten Ländern besteht ein höheres Risiko, dass der SMS-Verkehr gepumpt wird. Diese Länder sind in der Dropdown-Liste mit einem **hohen Risiko** gekennzeichnet.

![Das Länder-Dropdown mit Aserbaidschan mit dem Tag "Hohes Risiko".][4]{: style="max-width:80%;"}

Wenn Sie den Versand in diese Länder zulassen, müssen Sie zunächst das damit verbundene Risiko anerkennen, bevor das Land in Ihre Zulassungsliste aufgenommen wird.

{% alert note %}
Beschränken Sie die Länder auf Ihrer Allowlist auf die Länder, die Sie für Ihre Geschäftsanforderungen benötigen. So minimieren Sie das Potenzial für betrügerischen Traffic. Weitere Hinweise zur Verhinderung von SMS-Traffic-Pumping finden Sie in den [FAQs zu SMS-Traffic-Pumping-Betrug]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

## Sichtbarkeit von blockierten Sendungen

Sendeversuche an Länder, die nicht auf Ihrer Allowlist stehen, werden abgebrochen. Abgebrochene Nachrichten werden im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) und im [Nachrichten-Engagement-Event „SMS-Abbruch“]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) protokolliert. 

Abgebrochene Nachrichten, die durch blockierte Sendungen verursacht wurden, werden als `Abort_Type = "blocked_recipient_country"` mit dem Abbruchprotokoll angezeigt, in dem das blockierte Land aufgeführt ist.

![Abbruchprotokoll mit dem abort_type von blocked_recipient_country und den Länderinitialen der gesperrten Rufnummer.][5]{: style="max-width:80%;"}

[1]: {% image_buster /assets/img/sms/sms_geographic_permissions.png %}
[2]: {% image_buster /assets/img/sms/allowlist_dropdown.png %}
[3]: {% image_buster /assets/img/sms/delete_allowlist_warning.png %}
[4]: {% image_buster /assets/img/sms/high_risk.png %}
[5]: {% image_buster /assets/img/sms/abort_log.png %}
[6]: {% image_buster /assets/img/sms/sms_geographic_permissions_read_only.png %}