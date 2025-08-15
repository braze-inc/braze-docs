---
nav_title: Configuration d’e-mail
article_title: Onboarding Configuration d’e-mail
layout: dev_guide
page_order: 1
guide_top_header: "Configuration d’e-mail"
guide_top_text: "Braze peut vous aider à commencer à envoyer des campagnes par e-mail. Suivez nos guides ou consultez notre Cours d’apprentissage Braze sur l’<a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>Onboarding des e-mails</a>."
page_type: landing
description: "Cette page d’accueil inclut des ressources pour bien démarrer avec les campagnes par e-mail, notamment pour configurer votre adresses IP et vos domaines, le réchauffement d’adresses IP, la validation des e-mails, et plus encore."
channel: email

guide_featured_title: "Section Articles"
guide_featured_list:
- name: "Configuration des IP et des domaines"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/
  image: /assets/img/braze_icons/target-05.svg
- name: "Réchauffement d’adresses IP"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "Validation des e-mails"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/email_validation/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "Authentification par e-mail"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/authentication/
  image: /assets/img/braze_icons/user-square.svg
- name: "Importation de votre liste d’e-mails"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/
  image: /assets/img/braze_icons/list.svg
- name: "Aperçu SSL"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ssl/
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "Consentement et collecte d’adresses"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/
  image: /assets/img/braze_icons/book-closed.svg
- name: "Écueils de livrabilité et pièges à spam"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/deliverability_pitfalls_and_spam_traps/
  image: /assets/img/braze_icons/alert-triangle.svg
---

## Conditions

Avant d’envoyer des SMS, vous avez besoin de certaines données. Consultez le tableau suivant pour en savoir plus sur ces exigences.

| Condition | Description | Source |
|---|---|---|
| Une IP dédiée (protocole Internet)| Une adresse IP dédiée est une adresse Internet unique fournie exclusivement à un seul compte d’hébergement. | Braze offre à ses clients des adresses IP dédiées, afin de garantir le contrôle de votre réputation d’expéditeur de courrier électronique. L’onboarding de Braze vous permettra de le configurer.|
| Domaines en Whitelabel | Elles consistent en un domaine et un sous-domaine. La marque blanche vous permet de transmettre les contrôles d'authentification des e-mails pour les méthodes DKIM et SPF. | L’équipe d’onboarding de Braze génèrera ces domaines pour vous, mais vous devez choisir leurs noms. |
| Sous-domaines | Il s'agit d'une subdivision d'un domaine (tel que « @news.company.com ») dans votre adresse e-mail. Le fait d’avoir un sous-domaine empêche toute erreur susceptible d’endommager la réputation officielle de votre entreprise par e-mail. | L’équipe d’onboarding le générera pour vous, mais vous devez choisir le nom du sous-domaine. Vous ne pouvez pas utiliser de sous-domaines actuellement utilisés en dehors de Braze. |
| Pools IP | Il s'agit d'une configuration facultative utilisée pour séparer la réputation de différents types d'e-mails (tels que "promotionnels" et "transactionnels") afin d'empêcher la réputation de l'un d'affecter l'autre et de favoriser une meilleure délivrabilité. | L’équipe d’onboarding mettra en place les pools pour vous. Ensuite, lorsque vous rédigez votre e-mail, sélectionnez le pool d'adresses IP de votre e-mail dans le menu déroulant **Pool d'adresses IP** de la page **Audiences cibles**.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Réchauffement d’adresses IP

{% alert important %}
Le réchauffement d’adresses IP est l'**étape la plus importante** dans le processus de configuration des e-mails. Bien qu’il ne s’agisse pas de votre première étape (c’est en fait la dernière !), nous la mentionnons ici pour vous rappeler que vous devez absolument réchauffer votre adresse IP, faute de quoi tout e-mail que vous envoyez sera envoyé dans les spams ou soumis à d’autres obstacles.
{% endalert %}

[Le réchauffement IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) consiste à envoyer un nombre relativement restreint d'e-mails lors de votre premier envoi, puis, au fil du temps, à augmenter légèrement le volume des envois suivants jusqu'à atteindre votre volume quotidien habituel. Cela se fait à la fin de votre processus de configuration de courrier électronique.

En commençant par des volumes plus petits d’e-mails, vous établissez un niveau de confiance avec votre fournisseur d’e-mails, ce qui montre que vous envoyez uniquement des e-mails aux utilisateurs concernés. Envoyer votre premier lot d’e-mails à vos utilisateurs les plus engagés peut vous aider à gagner plus rapidement la confiance de votre fournisseur.

Après avoir terminé de réchauffer votre adresse IP, vous pouvez [commencer à créer et à envoyer des e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) !

<br><br>