---
nav_title: "Configuration de l'e-mail"
article_title: "Configuration de l'e-mail d'onboarding"
layout: dev_guide
page_order: 1
guide_top_header: "Configuration de l'e-mail"
guide_top_text: "Braze peut vous aider à commencer à envoyer des campagnes d'e-mail. Suivez nos guides ou consultez notre cours d'apprentissage Braze sur <a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>l'onboarding par e-mail</a>."
page_type: landing
description: "Cette page d'atterrissage comprend des ressources sur la façon d'implémenter des campagnes d'e-mail, y compris la configuration de vos IP et domaines, le réchauffement des IP, la validation des e-mails, et plus encore."
channel: email

guide_featured_title: "Articles de section"
guide_featured_list:
- name: "Configuration des IP et des domaines"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/
  image: /assets/img/braze_icons/target-05.svg
- name: "Réchauffement d'adresses IP"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "Validation de l'e-mail"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/email_validation/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "Authentification par e-mail"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/authentication/
  image: /assets/img/braze_icons/user-square.svg
- name: "Importation de votre liste d'e-mails"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/
  image: /assets/img/braze_icons/list.svg
- name: "Aperçu du SSL"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ssl/
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "Consentement et collecte d'adresses"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/
  image: /assets/img/braze_icons/book-closed.svg
- name: "Pièges de la livrabilité et pièges à spam"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/deliverability_pitfalls_and_spam_traps/
  image: /assets/img/braze_icons/alert-triangle.svg
---

## Exigences

Avant de commencer à envoyer des e-mails, vous avez besoin de certaines choses. Reportez-vous au tableau suivant pour en savoir plus sur ces exigences.

| Exigence | Description | Source |
|---|---|---|
| Une IP (Internet Protocol) dédiée| Une IP dédiée est une adresse internet unique fournie exclusivement à un seul compte d'hébergement. | Braze vous fournit des adresses IP dédiées afin de garantir le contrôle de la réputation de votre expéditeur d'e-mails. L'onboarding de Braze s'en chargera pour vous.|
| Domaines marqués d'une marque blanche | Ceux-ci se composent d'un domaine et d'un sous-domaine. En utilisant la marque blanche, vous pouvez passer les contrôles d'authentification des e-mails pour DKIM et SPF. | L'équipe Braze Onboarding générera ces domaines pour vous, mais vous devez choisir leurs noms. |
| Sous-domaines | Il s'agit d'une subdivision d'un domaine (comme "@news.company.com") dans votre adresse e-mail. Le fait de disposer d'un sous-domaine permet d'éviter toute erreur susceptible de nuire à la réputation de l'e-mail officiel de votre entreprise. | L'équipe Onboarding le génère pour vous, mais vous devez décider du nom du sous-domaine. Vous ne pouvez pas utiliser des sous-domaines qui sont actuellement utilisés en dehors de Braze. |
| Pools IP | Il s'agit d'une configuration facultative utilisée pour séparer la réputation des différents types d'e-mail (tels que "promotionnel" et "transactionnel") afin d'éviter que la réputation de l'un n'ait un impact sur l'autre et de favoriser une meilleure livrabilité. | L'équipe Onboarding se chargera de mettre en place les pools pour vous. Ensuite, lorsque vous rédigez votre e-mail, vous pouvez afficher le pool d'adresses IP de votre e-mail dans l'étape **Audiences cibles**.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## réchauffement d'adresses IP

{% alert important %}
Le réchauffement d'adresses IP est l'**étape la plus importante** de la configuration de l'e-mail. Bien qu'il ne s'agisse pas de la première étape (c'est en fait la dernière), nous vous rappelons ici que vous devez réchauffer votre adresse IP, faute de quoi tous les e-mails que vous enverrez seront envoyés dans des spams ou soumis à d'autres barrières d'envoi.
{% endalert %}

Le [réchauffement d'adresses IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) consiste à envoyer un nombre relativement faible d'e-mails dans votre premier lot, puis, au fil du temps, à augmenter légèrement le volume dans les lots suivants jusqu'à ce que vous atteigniez votre volume quotidien habituel. Cette opération s'effectue à la toute fin de la procédure de configuration de votre e-mail.

En commençant par de plus petits volumes d'e-mails, vous établissez un niveau de confiance avec votre fournisseur d'e-mails, en montrant que vous n'envoyez des e-mails qu'à des utilisateurs pertinents. Envoyer votre premier lot d'e-mails à vos utilisateurs les plus engagés peut vous aider à gagner plus rapidement la confiance de votre fournisseur.

Après avoir réchauffé votre IP, vous pouvez [commencer à créer et à envoyer des e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/)!

<br><br>
