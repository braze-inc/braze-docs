---
nav_title: Configuration de l'e-mail
article_title: Configuration de l'e-mail d'intégration
layout: en vedette
page_order: 5
guide_top_header: "Configuration de l'e-mail"
guide_top_text: "Vous voulez donc commencer à envoyer des campagnes d'e-mail? Braze Onboarding peut vous aider avec cela! Suivez notre guide ci-dessous ou consultez notre <a href='https://lab.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>cours LAB sur la livrabilité</a>."
page_type: atterrissage
description: "Cette page d'accueil contient des ressources pour démarrer avec des campagnes de courriel."
channel: Email
guide_featured_title: "Articles de la section"
guide_featured_list:
  - 
    name: "Configuration des IPs & Domaines"
    link: /fr/docs/user_guide/onboarding_with_braze/email_setup/setting_up_ips_and_domains/
    fa_icon: fa-dot-circle
  - 
    name: Authentification
    link: /fr/docs/user_guide/onboarding_with_braze/email_setup/authentication/
    fa_icon: fas fa-user-shield
  - 
    name: "Consentement & Collecte d'adresse"
    link: /fr/docs/user_guide/onboarding_with_braze/email_setup/consent_and_address_collection/
    fa_icon: fa-carnet d'adresses
  - 
    name: "Pièges de livrabilité & Pièges à Spam"
    link: /docs/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/
    fa_icon: fa-exclamation-triangle
  - 
    name: Importation de votre liste d'emails dans Braze
    link: /fr/docs/user_guide/onboarding_with_braze/email_setup/import_votre_email_list/
    fa_icon: fas fa-list
  - 
    name: Validation de l'email
    link: /fr/docs/user_guide/onboarding_with_braze/email_setup/email_validation/
    fa_icon: fas fa-envelope-square
  - 
    name: Réchauffement IP
    link: /fr/docs/user_guide/onboarding_with_braze/email_setup/ip_warming/
    fa_icon: fas fa-exclamation
  - 
    name: Aperçu SSL
    link: /fr/docs/user_guide/onboarding_with_braze/email_setup/ssl/
    fa_icon: fas fa-mouse-pointeur
---

## Exigences

Avant de commencer à envoyer des e-mails, il y a des choses dont vous avez besoin. Consultez le tableau ci-dessous pour en savoir plus.

| Exigences                          | Libellé                                                                                                                                                                                                                                                           | Acquisition                                                                                                                                                                                                           |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Une IP dédiée (protocole Internet) | Une adresse IP dédiée est une adresse Internet unique fournie exclusivement à un seul compte d’hébergement.                                                                                                                                                       | Braze donne à ses clients des adresses IP dédiées, pour assurer le contrôle de la réputation de votre expéditeur de courriel. L'embarquement de Braze le configurera pour vous.                                       |
| Domaines en marque blanche         | Celles-ci se composent d'un domaine et d'un sous-domaine. La Whitelabling vous permet de passer les vérifications d'authentification par e-mail pour DKIM et SPF.                                                                                                 | L'intégration à Braze générera ces domaines pour vous, mais vous devez choisir leurs noms.                                                                                                                            |
| Sous-domaines                      | Ceci est une subdivision d'un domaine et ressemble généralement à : `@news.company.com` dans votre adresse e-mail. Avoir un sous-domaine empêchera toute erreur qui pourrait nuire à la réputation officielle de votre entreprise.                                | L'intégration de Braze va générer pour vous, mais vous devez décider du nom du sous-domaine. Vous ne pouvez pas utiliser de sous-domaines qui sont actuellement utilisés en dehors de Braze.                          |
| Pools IP                           | Il s'agit d'une configuration optionnelle utilisée pour séparer la réputation de différents types d'e-mails (par exemple: "promotionnel" vs. "transactionnel") pour éviter que la réputation de l'un n'affecte l'autre et pour assurer une livraison plus élevée. | L'embarquement de Braze mettra en place les piscines pour vous ; Puis, lors de la rédaction de votre courriel, choisissez la réserve IP de votre courrier à partir du menu déroulant sur la page Utilisateurs cibles. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Le réchauffement IP

{% alert important %}
Le réchauffement IP est l'étape __la plus importante__ du processus de configuration de l'email. Bien que ce ne soit pas votre première étape (c'est en fait la dernière! , nous l'appelons ici pour vous faire savoir que vous devez absolument réchauffer votre adresse IP ou que tous les courriels que vous envoyez seront envoyés au spam ou seront soumis à d'autres barrières d'envoi.
{% endalert %}

[IP Warmup]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/) est quand vous envoyez un nombre relativement réduit d'e-mails dans votre premier lot, puis au fil du temps, augmentez légèrement le volume des lots suivants jusqu'à ce que vous atteigniez votre volume quotidien typique. Cela se fait à la fin du processus de configuration de votre e-mail.

En commençant par de plus petits volumes de courriels, vous établissez un niveau de confiance avec votre fournisseur de messagerie, montrant que vous envoyez uniquement des courriels aux utilisateurs pertinents.

Envoyez votre premier lot d'emails à vos utilisateurs les plus engagés. Cela vous aidera à gagner la confiance plus rapidement avec votre fournisseur.

Une fois que vous avez terminé avec votre IP Warmup, n'hésitez pas à [commencer à créer et envoyer des e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/)!

## Plus de ressources

Pour plus d'informations sur les courriels au Brésil, consultez notre section dédiée [e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/).
