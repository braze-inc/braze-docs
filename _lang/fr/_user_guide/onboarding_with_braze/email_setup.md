---
nav_title: Configuration d’e-mail
article_title: Onboarding Configuration d’e-mail
layout: dev_guide
page_order: 5
guide_top_header: "Configuration d’e-mail"
guide_top_text: "Vous souhaitez commencer à envoyer des campagnes par e-mail ? Braze peut vous aider ! Suivez nos guides ou consultez notre Cours d’apprentissage Braze sur l’<a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>Onboarding des e-mails</a>."
page_type: landing
description: "Cette page d’accueil comprend des ressources pour vous aider à démarrer des campagnes par e-mail."
channel: email

guide_featured_title: "Section Articles"
guide_featured_list:
- name: "Configuration des IP et des domaines"
  link: /docs/user_guide/onboarding_with_braze/email_setup/setting_up_ips_and_domains/
  fa_icon: far fa-dot-circle
- name: Authentification
  link: /docs/user_guide/onboarding_with_braze/email_setup/authentication/
  fa_icon: fas fa-user-shield
- name: "Consentement et collecte d’adresses"
  link: /docs/user_guide/onboarding_with_braze/email_setup/consent_and_address_collection/
  fa_icon: fas fa-address-book
- name: "Écueils de délivrabilité et pièges à spam"
  link: /docs/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/
  fa_icon: fas fa-exclamation-triangle
- name: Importer votre liste d’e-mails dans Braze
  link: /docs/user_guide/onboarding_with_braze/email_setup/import_your_email_list/
  fa_icon: fas fa-list
- name: Validation des e-mails
  link: /docs/user_guide/onboarding_with_braze/email_setup/email_validation/
  fa_icon: fas fa-envelope-square
- name: Réchauffement d’adresses IP
  link: /docs/user_guide/onboarding_with_braze/email_setup/ip_warming/
  fa_icon: fas fa-exclamation
- name: Aperçu SSL
  link: /docs/user_guide/onboarding_with_braze/email_setup/ssl/
  fa_icon: fas fa-mouse-pointer
---

## Conditions

Avant d’envoyer des SMS, vous avez besoin de certaines données. Consultez le tableau suivant pour en savoir plus.

|Condition | Description | Source |
|---|---|---|
| Une IP dédiée (protocole Internet)| Un IP dédié est une adresse Internet unique fournie exclusivement à un compte d’hébergement unique. | Braze offre à ses clients des adresses IP dédiées, afin de garantir le contrôle de votre réputation d’expéditeur de courrier électronique. L’équipe d’onboarding de Braze les configurera pour vous..|
| Domaines en Whitelabel | Elles consistent en un domaine et un sous-domaine. Le whitelabel vous permet de passer des contrôles d’authentification par e-mail pour DKIM et SPF. | L’onboarding de Braze génère ces domaines pour vous, mais vous devez choisir leurs noms. |
|Sous-domaines | Il s’agit d’une sous-division d’un domaine et ressemble généralement à : `@news.company.com` dans votre adresse e-mail. Le fait d’avoir un sous-domaine empêche toute erreur susceptible d’endommager la réputation officielle de votre entreprise par e-mail. | L’onboarding de Braze vous permet de les générer, mais vous devez décider du nom du sous-domaine. Vous ne pouvez pas utiliser de sous-domaines actuellement utilisés en dehors de Braze. |
|Pools IP | Il s’agit d’une configuration facultative utilisée pour séparer la réputation de différents types d’e-mails (par exemple : « promotionnel » et « transactionnel ») afin d’empêcher la réputation de l’un d’avoir un impact sur l’autre et de garantir une plus grande délivrabilité. | L’onboarding de Braze configure les pools pour vous ; ensuite, lorsque vous composez votre e-mail, choisissez le pool IP de votre e-mail dans le menu déroulant Pool de PI sur la page Utilisateurs cibles.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Réchauffement d’adresses IP

{% alert important %}
Le réchauffement IP est l’**étape la plus importante** du processus de configuration des e-mails. Bien qu’il ne s’agisse pas de votre première étape (c’est en fait la dernière !), nous l’appelons ici pour vous informer que vous devez absolument réchauffer votre adresse IP ou que tout e-mail que vous envoyez sera envoyé dans les spams ou soumis à d’autres obstacles.
{% endalert %}

[Réchauffement IP]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/) lorsque vous envoyez un nombre relativement restreint d’e-mails dans votre premier lot, puis au fil du temps, augmentez légèrement le volume dans les lots suivants jusqu’à ce que vous atteigniez votre volume quotidien habituel. Cela se fait à la fin de votre processus de configuration de courrier électronique.

En commençant par des volumes plus petits d’e-mails, vous établissez un niveau de confiance avec votre fournisseur de messagerie, ce qui montre que vous envoyez uniquement des e-mails aux utilisateurs concernés. Envoyez votre premier lot d’e-mails à vos utilisateurs les plus engagés. Cela vous aidera à gagner en confiance plus rapidement avec votre fournisseur.

Après avoir réchauffé votre IP, n’hésitez pas à [commencer à créer et à envoyer des e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/)!

## Ressources supplémentaires

Pour plus d’informations sur les e-mails de Braze, consultez notre [section e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/).<br><br>
