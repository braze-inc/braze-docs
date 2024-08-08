---
nav_title: Configuration d’e-mail
article_title: Onboarding Configuration d’e-mail
layout: dev_guide
page_order: 5
guide_top_header: "Configuration d’e-mail"
guide_top_text: "Vous souhaitez commencer à envoyer des campagnes par e-mail ? Braze peut vous aider ! Suivez nos guides ou consultez notre Cours d’apprentissage Braze sur l’<a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>Onboarding des e-mails</a>."
page_type: landing
description: "Cette page d’accueil comprend des ressources pour bien démarrer avec les campagnes par e-mail, notamment pour configurer votre IPS et vos domaines, le réchauffement d’adresse IP, la validation des e-mails, etc."
channel: email

guide_featured_title: "Section Articles"
guide_featured_list:
- name: "Configuration des IP et des domaines"
  link: /docs/user_guide/onboarding_with_braze/email_setup/setting_up_ips_and_domains/
  image: /assets/img/braze_icons/target-05.svg
- name: "Réchauffement d’adresses IP"
  link: /docs/user_guide/onboarding_with_braze/email_setup/ip_warming/
  image: /assets/img/braze_icons/alert-circle.svg
- name: "Validation des e-mails"
  link: /docs/user_guide/onboarding_with_braze/email_setup/email_validation/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "Authentification par e-mail"
  link: /docs/user_guide/onboarding_with_braze/email_setup/authentication/
  image: /assets/img/braze_icons/user-square.svg
- name: "Importation de votre liste d’e-mails"
  link: /docs/user_guide/onboarding_with_braze/email_setup/import_your_email_list/
  image: /assets/img/braze_icons/list.svg
- name: "Aperçu SSL"
  link: /docs/user_guide/onboarding_with_braze/email_setup/ssl/
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "Consentement et collecte d’adresses"
  link: /docs/user_guide/onboarding_with_braze/email_setup/consent_and_address_collection/
  image: /assets/img/braze_icons/book-open-01.svg
- name: "Écueils de délivrabilité et pièges à spam"
  link: /docs/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/
  image: /assets/img/braze_icons/alert-triangle.svg
---

## Conditions

Avant d’envoyer des SMS, vous avez besoin de certaines données. Consultez le tableau suivant pour en savoir plus sur ces exigences.

| Condition | Description | Source |
|---|---|---|
| Une IP dédiée (protocole Internet)| Une adresse IP dédiée est une adresse Internet unique fournie exclusivement à un seul compte d’hébergement. | Braze offre à ses clients des adresses IP dédiées, afin de garantir le contrôle de votre réputation d’expéditeur de courrier électronique. L’équipe d’onboarding de Braze les configurera pour vous..|
| Domaines en Whitelabel | Elles consistent en un domaine et un sous-domaine. Le whitelabel vous permet de passer des contrôles d’authentification par e-mail pour DKIM et SPF. | L’équipe d’onboarding de Braze génèrera ces domaines pour vous, mais vous devez choisir leurs noms. |
| Sous-domaines | Il s’agit d’une subdivision d’un domaine (c.-à-d. « @news.company.com ») dans votre adresse e-mail. Le fait d’avoir un sous-domaine empêche toute erreur susceptible d’endommager la réputation officielle de votre entreprise par e-mail. | L’équipe d’onboarding le générera pour vous, mais vous devez choisir le nom du sous-domaine. Vous ne pouvez pas utiliser de sous-domaines actuellement utilisés en dehors de Braze. |
| Pools IP | Il s’agit d’une configuration facultative utilisée pour séparer la réputation de différents types d’e-mails (c.-à-d., « promotionnel » et « transactionnel ») afin d’empêcher la réputation de l’un d’avoir un impact sur l’autre et de garantir une plus grande délivrabilité. | L’équipe d’onboarding mettra en place les pools pour vous. Ensuite, lorsque vous rédigez votre e-mail, sélectionnez le pool d’adresses IP de votre e-mail dans la liste déroulante **IP Pool (Pool IP)** de la page **Target Users (Cibler les utilisateurs)**..|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Réchauffement d’adresses IP

{% alert important %}
Le réchauffement IP est l’**étape la plus importante** du processus de configuration des e-mails. Bien qu’il ne s’agisse pas de votre première étape (c’est en fait la dernière !), nous la mentionnons ici pour vous rappeler que vous devez absolument réchauffer votre adresse IP, faute de quoi tout e-mail que vous envoyez sera envoyé dans les spams ou soumis à d’autres obstacles.
{% endalert %}

Le [réchauffement d’adresses IP]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/) fait référence au fait d’envoyer un nombre relativement restreint d’e-mails dans votre premier lot, puis au fil du temps, d’augmenter légèrement le volume dans les lots suivants jusqu’à ce que vous atteigniez votre volume quotidien habituel. Cela se fait à la fin de votre processus de configuration de courrier électronique.

En commençant par des volumes plus petits d’e-mails, vous établissez un niveau de confiance avec votre fournisseur d’e-mails, ce qui montre que vous envoyez uniquement des e-mails aux utilisateurs concernés. Envoyer votre premier lot d’e-mails à vos utilisateurs les plus engagés peut vous aider à gagner plus rapidement la confiance de votre fournisseur.

Après avoir réchauffé votre adresse IP, vous pouvez [commencer à créer et à envoyer des e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/) !

Pour plus d’informations sur les e-mails de Braze, consultez notre [section e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/).<br><br>
