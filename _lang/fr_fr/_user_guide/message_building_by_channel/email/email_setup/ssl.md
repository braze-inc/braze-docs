---
nav_title: SSL chez Braze
article_title: Aperçu SSL
page_order: 5
page_type: reference
description: "Le présent article de référence couvre le SSL, ce pour quoi il est utilisé et comment il l’est chez Braze."
channel: email

---

# SSL chez Braze

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> Une couche de socket sécurisée (SSL) crypte une URL avec HTTPS au lieu de HTTP. HTTPS indique qu'il existe un certificat SSL ou TLS valide et fiable et que le site web peut être visité en toute sécurité.

## Pourquoi est-ce que le SSL est important ?

La plupart des domaines ne nécessitent pas de SSL, mais Braze recommande vivement l'utilisation de SSL pour les raisons suivantes.

La sécurisation de votre site Internet et des liens avec SSL est une pratique courante, même pour les entreprises qui ne traitent pas directement des informations sensibles sur le client. Les utilisateurs sont plus à l’aise des liens sécurisés avec SSL, et la couche d’authentification supplémentaire permet de protéger vos données.

### Nécessaire pour le suivi des clics et des ouvertures

Braze transforme vos liens en utilisant le sous-domaine de suivi des liens de votre marque pour suivre les clics et les ouvertures. Par défaut, ces liens commencent par HTTP. Les utilisateurs disposant de navigateurs ou d'extensions qui restreignent le trafic non sécurisé peuvent avoir des difficultés à passer par la redirection avant l'URL de destination, même si l'URL est sécurisée. Cela peut entraîner des ruptures d'images et un suivi imprécis. Appliquez SSL au sous-domaine de suivi des liens pour confirmer la sécurité des redirections.

### Exigences du navigateur

Les principaux navigateurs tels que Google Chrome limitent le trafic via des URL non sécurisés afin de protéger les utilisateurs. L'utilisation du SSL permet de confirmer que le contenu est fiable et de minimiser les problèmes tels que les liens et les images cassés dans les e-mails.

### Exigences des domaines HSTS 

Si vous disposez d'un domaine HTTP Strict Transport Security (HSTS), mettez en place SSL et configurez un réseau de diffusion de contenu pour qu'il envoie les certificats de sécurité requis. Sans SSL, les images et les liens web se brisent.

## Acquisition d’un certificat SSL

Acquérir un certificat SSL par l'intermédiaire d'un tiers, généralement un réseau de diffusion/distribution de contenu (CDN). Un CDN héberge le certificat et le sert au navigateur lorsqu'un utilisateur clique sur un lien en redirigeant le trafic via le CDN pour appliquer les certificats avant de l'envoyer à SendGrid ou SparkPost.

Pour commencer la configuration SSL, contactez votre gestionnaire satisfaction client de Braze pour lancer une configuration complète de l'e-mail Braze.

Une fois que Braze a lancé la configuration, suivez les étapes suivantes :
1. Braze fournit des enregistrements DNS à ajouter à votre registre de domaine.
2. Braze vérifie si les enregistrements ont été ajoutés correctement à votre registre.
3. Vous allez ensuite sélectionner un CDN et obtenir des certificats SSL auprès d’un fournisseur tiers. 
4. À ce stade, vous allez configurer votre CDN. Veuillez remarquer que Braze ne sera pas en mesure de vous aider à résoudre les problèmes de configuration CDN. Contactez votre fournisseur de diffusion de contenu pour toute assistance supplémentaire.
5. Contactez votre gestionnaire de satisfaction client pour activer SSL.

### Qu’est-ce qu’un CDN et pourquoi en ai-je besoin ?

Un réseau de réception/distribution de contenu (CDN) est une plateforme de serveurs qui permet de garantir des temps de chargement rapides des contenus sur plusieurs supports, tout en gérant les certificats de sécurité. 

{% alert important %}
La configuration CDN se fait toujours lorsque Braze a obtenu et validé vos enregistrements DNS. Si vous n'avez pas encore entamé cette étape, contactez votre gestionnaire de satisfaction client pour plus d'informations sur la marche à suivre.
{% endalert %}

Pour le suivi des clics et des ouvertures, les partenaires de réception/distribution transforment les liens en utilisant un sous-domaine de marque et le réseau de diffusion de contenu applique le certificat SSL à ces liens transformés. Les partenaires doivent souvent présenter des certificats valides au navigateur du destinataire pour que les liens et les images s'affichent correctement. Braze ne demandant ni ne gérant les certificats, vous devez passer par un réseau de diffusion contenu. 

{% alert note %}
Si vous ne pouvez pas ou ne voulez pas utiliser les CDN répertoriés pour le suivi SSL des clics et des ouvertures, vous pouvez mettre en place une configuration SSL personnalisée. Les CDN alternatifs ou les proxys personnalisés peuvent donner lieu à une configuration plus complexe. Reportez-vous à la documentation de [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) et de [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

#### Ressources complémentaires

{% alert important %}
Pour la résolution des problèmes liés à votre configuration de réseau de diffusion contenu, contactez votre fournisseur de réseau de diffusion contenu.
{% endalert %}

Le tableau suivant comprend des guides étape par étape rédigés par des partenaires ESP sur la manière de configurer certains CDN. Même si votre CDN spécifique n’a pas à être répertorié, vous devez vous assurer que votre CDN a la capacité d’appliquer des certificats SSL.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour Amazon SES, consultez [Option 2 : Configuration d'un domaine HTTPS](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) et spécifiez le domaine de suivi AWS par région en fonction de votre cluster Braze :

- **Clusters Braze aux États-Unis :** `r.us-east-1.awstrack.me`
- **Clusters Braze dans l’UE :** `r.eu-central-1.awstrack.me`

{% alert important %}
Lorsque vous configurez le domaine de diffusion de contenu de votre CDN, activez l'en-tête `X-Forwarded-Host` pour éviter les problèmes de sécurité potentiels tels que les attaques d'en-tête d'hôte. Reportez-vous à la documentation du réseau de diffusion de contenu ou à votre équipe d'assistance pour connaître les étapes à suivre.
{% endalert %}

#### Résolution des problèmes

Bien que vous deviez gérer la configuration du réseau de diffusion de contenu, les certificats et les problèmes de proxy avec votre réseau de diffusion de contenu, utilisez ces conseils pour identifier les problèmes courants de suivi des clics SSL.

##### Problèmes liés au registre des domaines

Exécutez une commande dig pour confirmer que vous pointez le suivi des liens vers le réseau de diffusion de contenu. Dans votre terminal, lancez `dig CNAME link_tracking_subdomain`. Sous `ANSWER SECTION`, il est indiqué où votre CNAME pointe. S'il pointe vers le fournisseur de services e-mail (SendGrid ou SparkPost) et non vers votre réseau de diffusion de contenu, reconfigurez votre registre de domaine pour qu'il pointe vers votre réseau de diffusion de contenu.

##### Problèmes liés au CDN

Si les liens d'e-mails en ligne/en production/instantanés s'interrompent pendant la configuration, il est probable que vous ayez orienté les DNS vers votre réseau de diffusion/instantané avant d'avoir effectué la configuration adéquate. Cela peut apparaître comme une erreur de « mauvais lien ». Contactez votre fournisseur de diffusion de contenu et consultez sa documentation pour résoudre les problèmes de configuration.

##### Statut d’activation SSL

Si vous avez terminé la configuration de SSL et que les liens apparaissent toujours comme HTTP, contactez votre gestionnaire satisfaction client de Braze pour confirmer que Braze a activé SSL. Braze n'active SSL qu'une fois toutes les étapes de configuration terminées.

