---
nav_title: "Zustellbarkeitsfallen &amp; Spam-Trap's"
article_title: Zustellbarkeitsfehler und Spam-Traps
page_order: 7
page_type: reference
description: "Dieser Referenzartikel befasst sich mit potenziellen Fallstricken bei der E-Mail-Zustellung, mit Spam-Fallen und wie Sie diese vermeiden können."
channel: email

---

# [![Braze Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"} Zustellbarkeitsfallen und Spam-Trap

Die Zustellbarkeit Ihrer E-Mails kann durch folgende Spam-Traps beeinträchtigt werden:

| Trap-Typ | Beschreibung |
|---|---|
| Unverfälschte Traps | E-Mail-Adressen und Domains, die noch nie benutzt wurden. |
| Recycelte Traps | E-Mail-Adressen, die ursprünglich echte Nutzer:innen waren, jetzt aber inaktiv sind. |
| Tippfehler-Traps | E-Mail-Adressen mit häufigen Tippfehlern. |
| Spam-Beschwerden | Wenn Ihre E-Mail von einem Kunden als Spam markiert wird. |
| Hohe Absprungrate | Wenn Ihre E-Mail regelmäßig nicht zugestellt werden kann, weil die Adresse des Empfängers ungültig ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Wie Sie Spam-Trap vermeiden

Diese Fallen lassen sich vermeiden, wenn Sie ein bestätigtes Opt-in-Verfahren einrichten. Indem Sie eine erste Opt-in-E-Mail versenden und Ihre Kunden bitten, zu bestätigen, dass sie Ihre Nachrichten erhalten möchten, stellen Sie sicher, dass Ihre Empfänger von Ihnen hören möchten und dass Sie an echte, gültige Adressen senden. Hier finden Sie weitere Möglichkeiten, um Spam-Fallen zu vermeiden:

1. Senden Sie eine E-Mail für doppeltes Opt-in. Dies ist eine E-Mail, in der die Benutzer aufgefordert werden, ihre Abonnementwahlen durch Anklicken eines Links zu bestätigen.
2. Als Best Practice sollten Sie eine [Sunset-Richtlinie]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/) implementieren.
3. **Kaufen Sie niemals E-Mail-Listen.** 

{% alert tip %}
Die Teams für Customer-Success und Zustellbarkeit von Braze können Ihnen dabei helfen, die Zustellbarkeit weltweit zu maximieren.
{% endalert %}

## Entfernen einer E-Mail Adresse aus Ihrer Bounce- oder Spam-Liste

Mit den folgenden Endpunkten können Sie gebouncte E-Mails und E-Mails auf Ihrer Braze Spam-Liste entfernen:
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)