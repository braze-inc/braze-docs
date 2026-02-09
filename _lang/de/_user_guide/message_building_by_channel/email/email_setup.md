---
nav_title: E-Mail einrichten
article_title: Onboarding-E-Mail einrichten
layout: dev_guide
page_order: 1
guide_top_header: "E-Mail-Einrichtung"
guide_top_text: "Braze kann Ihnen helfen, E-Mail Kampagnen zu versenden. Folgen Sie entweder unseren Anleitungen oder besuchen Sie unseren Braze Learning-Kurs <a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>E-Mail-Onboarding</a>."
page_type: landing
description: "Auf dieser Landing Page finden Sie Ressourcen für den Start von Kampagnen, einschließlich der Einrichtung Ihrer IPs und Domains, IP-Warming, E-Mail-Validierung und mehr."
channel: email

guide_featured_title: "Abschnittsartikel"
guide_featured_list:
- name: "Einrichten von IPs und Domains"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/
  image: /assets/img/braze_icons/target-05.svg
- name: "IP Erwärmung"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "E-Mail-Validierung"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/email_validation/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "E-Mail-Authentifizierung"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/authentication/
  image: /assets/img/braze_icons/user-square.svg
- name: "Importieren Ihrer E-Mail-Liste"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/
  image: /assets/img/braze_icons/list.svg
- name: "SSL-Übersicht"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ssl/
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "Einverständnis und Adresserfassung"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/
  image: /assets/img/braze_icons/book-closed.svg
- name: "Fallstricke bei der Zustellbarkeit und Spam-Trap"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/deliverability_pitfalls_and_spam_traps/
  image: /assets/img/braze_icons/alert-triangle.svg
---

## Anforderungen

Bevor Sie mit dem Versenden von E-Mails beginnen, benötigen Sie einige Dinge. Lesen Sie das folgende Chart, um mehr über diese Anforderungen zu erfahren.

| Anforderung | Beschreibung | Quelle |
|---|---|---|
| Eine dedizierte IP (Internetprotokoll)| Eine dedizierte IP ist eine einzigartige Internetadresse, die exklusiv für ein einzelnes Hosting-Konto bereitgestellt wird. | Braze stellt Ihnen dedizierte IPs zur Verfügung, um die Kontrolle über die Absender-Reputation Ihrer E-Mails zu gewährleisten. Das Braze Onboarding wird dies für Sie einrichten.|
| Whitelabel-Domains | Diese bestehen aus einer Domain und einer Subdomain. Durch Whitelabeling können Sie die E-Mail-Authentifizierungsprüfungen für DKIM und SPF umgehen. | Das Braze-Onboarding-Team wird diese Domains für Sie generieren, aber Sie müssen deren Namen selbst wählen. |
| Subdomänen | Dies ist eine Unterteilung einer Domain (z. B. „@news.company.com“) innerhalb Ihrer E-Mail Adresse. Mit einer Subdomain vermeiden Sie Fehler, die dem offiziellen Ruf Ihres Unternehmens bei E-Mails schaden könnten. | Das Onboarding-Team wird dies für Sie erstellen, aber Sie müssen den Namen der Subdomain festlegen. Sie können keine Subdomains verwenden, die derzeit außerhalb von Braze verwendet werden. |
| IP-Pools | Hierbei handelt es sich um eine optionale Konfiguration, die dazu dient, die Reputation verschiedener Arten von E-Mails (z.B. "Werbe-E-Mails" und "Transaktions-E-Mails") voneinander zu trennen, um zu verhindern, dass die Reputation der einen die der anderen beeinflusst, und um eine höhere Zustellbarkeit zu unterstützen. | Das Onboarding-Team wird die Pools für Sie einrichten. Wenn Sie dann Ihre E-Mail verfassen, können Sie den IP-Pool Ihrer E-Mail im Schritt **Targeting Zielgruppen** einsehen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## IP-Warming

{% alert important %}
IP-Warming ist der **wichtigste Schritt** bei der Einrichtung von E-Mails. Obwohl dies nicht der erste Schritt ist (es ist eigentlich der letzte), weisen wir Sie hier darauf hin, dass Sie Ihre IP-Adresse aufwärmen müssen, da sonst alle von Ihnen gesendeten E-Mails als Spam verschickt werden oder anderen Sendebarrieren unterliegen.
{% endalert %}

[IP-Warming]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) bedeutet, dass Sie in Ihrem ersten Stapel eine relativ kleine Anzahl von E-Mails versenden und dann im Laufe der Zeit das Volumen in den folgenden Stapeln leicht erhöhen, bis Sie Ihr typisches tägliches Volumen erreichen. Dies geschieht ganz am Ende des Einrichtungsprozesses Ihrer E-Mail.

Indem Sie mit kleineren Mengen an E-Mails beginnen, bauen Sie ein Vertrauensverhältnis zu Ihrem E-Mail-Anbieter auf und zeigen, dass Sie nur E-Mails an relevante Nutzer:innen senden. Wenn Sie Ihre ersten E-Mails an die Nutzer:innen mit dem größten Engagement senden, können Sie schneller Vertrauen bei Ihrem Anbieter gewinnen.

Nachdem Sie Ihre IP aufgewärmt haben, können Sie [mit dem Erstellen und Versenden von E-Mails beginnen]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/)!

<br><br>
