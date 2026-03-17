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

> Le protocole SSL (Secure Socket Layer) crypte une URL avec HTTPS au lieu de HTTP. HTTPS indique qu'un certificat SSL ou TLS valide et fiable existe et que le site web peut être consulté en toute sécurité.

## Pourquoi est-ce que le SSL est important ?

La plupart des domaines ne nécessitent pas de SSL, mais Braze recommande fortement d'utiliser SSL pour les raisons suivantes.

La sécurisation de votre site Internet et des liens avec SSL est une pratique courante, même pour les entreprises qui ne traitent pas directement des informations sensibles sur le client. Les utilisateurs sont plus à l’aise des liens sécurisés avec SSL, et la couche d’authentification supplémentaire permet de protéger vos données.

### Nécessaire pour le suivi des clics et des ouvertures

Braze transforme vos liens en utilisant votre sous-domaine de suivi de liens personnalisé afin de suivre les clics et les ouvertures. Par défaut, ces liens commencent par HTTP. Les utilisateurs disposant de navigateurs ou d'extensions qui restreignent le trafic non sécurisé peuvent rencontrer des difficultés pour passer par la redirection avant l'URL de destination, même si l'URL est sécurisée. Cela peut entraîner des images endommagées et un suivi inexact. Veuillez appliquer le protocole SSL au sous-domaine de suivi des liens afin de garantir la sécurité des redirections.

### Exigences du navigateur

Les principaux navigateurs, tels que Google Chrome, limitent le trafic via des URL non sécurisées afin de protéger les utilisateurs. L'utilisation du protocole SSL permet de confirmer la fiabilité du contenu et de minimiser les problèmes tels que les liens et les images brisés dans les e-mails.

### Exigences des domaines HSTS 

Si vous disposez d'un domaine HTTP Strict Transport Security (HSTS), veuillez configurer SSL et configurer un réseau de diffusion de contenu pour envoyer les certificats de sécurité requis. Sans SSL, les liens vers les images et les sites web ne fonctionnent pas correctement.

## Acquisition d’un certificat SSL

Obtenir un certificat SSL par l'intermédiaire d'un tiers, généralement un réseau de diffusion de contenu (CDN). Un réseau de diffusion de contenu héberge le certificat et le transmet au navigateur lorsqu'un utilisateur clique sur un lien en redirigeant le trafic via le réseau de diffusion de contenu afin d'appliquer les certificats avant de l'envoyer à Sendgrid ou SparkPost.

Pour commencer la configuration SSL, veuillez contacter votre gestionnaire de la satisfaction client Braze afin de lancer une configuration complète de l'e-mail Braze.

Une fois que Braze a lancé la configuration, veuillez suivre les étapes suivantes :
1. Braze fournit des enregistrements DNS à ajouter à votre registre de domaine.
2. Braze vérifie si les enregistrements ont été ajoutés correctement à votre registre.
3. Vous allez ensuite sélectionner un CDN et obtenir des certificats SSL auprès d’un fournisseur tiers. 
4. À ce stade, vous allez configurer votre CDN. Veuillez remarquer que Braze ne sera pas en mesure de vous aider à résoudre les problèmes de configuration CDN. Veuillez contacter votre fournisseur de réseau de diffusion de contenu pour toute assistance supplémentaire.
5. Veuillez contacter votre gestionnaire de la satisfaction client pour activer le protocole SSL.

### Qu’est-ce qu’un CDN et pourquoi en ai-je besoin ?

Un réseau de diffusion de contenu (CDN) est une plateforme de serveurs qui contribue à garantir des temps de chargement rapides pour le contenu sur plusieurs supports, tout en gérant les certificats de sécurité. 

{% alert important %}
La configuration CDN se fait toujours lorsque Braze a obtenu et validé vos enregistrements DNS. Si vous n'avez pas encore entrepris cette étape, veuillez contacter votre gestionnaire de la satisfaction client pour obtenir plus d'informations sur la manière de procéder.
{% endalert %}

Pour le suivi des clics et des ouvertures, les partenaires de réception/distribution transforment les liens à l'aide d'un sous-domaine de marque et le réseau de diffusion de contenu applique le certificat SSL à ces liens transformés. Les partenaires doivent fréquemment présenter des certificats valides au navigateur du destinataire pour que les liens et les images s'affichent correctement. Étant donné que Braze ne demande ni ne gère de certificats, il est nécessaire de procéder à cette configuration via un réseau de diffusion de contenu. 

{% alert note %}
Si vous ne pouvez pas ou ne souhaitez pas utiliser les CDN répertoriés pour le suivi des clics et des ouvertures SSL, vous pouvez configurer une configuration SSL personnalisée. L'utilisation d'autres CDN ou de proxys personnalisés peut entraîner une configuration plus complexe. Veuillez consulter la documentation [Sendgrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) et [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

#### Ressources complémentaires

{% alert important %}
Pour la résolution des problèmes liés à la configuration de votre réseau de diffusion de contenu, veuillez contacter votre fournisseur de réseau de diffusion de contenu.
{% endalert %}

Le tableau suivant comprend des guides étape par étape rédigés par des partenaires ESP sur la manière de configurer certains CDN. Même si votre CDN spécifique n’a pas à être répertorié, vous devez vous assurer que votre CDN a la capacité d’appliquer des certificats SSL.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour Amazon SES, consultez [Option 2 : Configurez un domaine HTTPS](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) et indiquez le domaine de suivi AWS par région en fonction de votre cluster Braze :

- **Clusters Braze aux États-Unis :** `r.us-east-1.awstrack.me`
- **Clusters Braze dans l’UE :** `r.eu-central-1.awstrack.me`

{% alert important %}
Lorsque vous configurez le domaine de suivi des clics de votre réseau de diffusion de contenu, veuillez activer `X-Forwarded-Host`l'en-tête pour prévenir d'éventuels problèmes de sécurité tels que les attaques par en-tête d'hôte. Veuillez consulter la documentation du réseau de diffusion de contenu ou votre équipe d'assistance pour connaître la procédure à suivre.
{% endalert %}

#### Résolution des problèmes

Bien que vous deviez gérer la configuration du réseau de diffusion de contenu, les certificats et les problèmes de proxy avec votre réseau de diffusion de contenu, veuillez utiliser ces conseils pour identifier les problèmes courants liés au suivi des clics SSL.

##### Problèmes liés au registre des domaines

Exécutez une commande dig pour vérifier que le suivi des liens pointe bien vers le réseau de diffusion de contenu. Dans votre terminal, veuillez exécuter `dig CNAME link_tracking_subdomain`. Sous `ANSWER SECTION`, il indique où pointe votre CNAME. Si le pointeur est dirigé vers le fournisseur de services d'e-mailing (Sendgrid ou SparkPost) et non vers votre réseau de diffusion de contenu, veuillez reconfigurer votre registre de domaine afin qu'il pointe vers votre réseau de diffusion de contenu.

##### Problèmes liés au CDN

Si les liens e-mail en ligne/en production/instantanés ne fonctionnent plus pendant la configuration, il est probable que vous ayez redirigé le dns vers votre réseau de diffusion de contenu avant d'avoir correctement configuré le système. Cela peut apparaître comme une erreur de « mauvais lien ». Veuillez contacter votre fournisseur de réseau de diffusion de contenu et examiner sa documentation afin de résoudre les problèmes de configuration.

##### Statut d’activation SSL

Si vous avez terminé la configuration SSL et que les liens apparaissent toujours en HTTP, veuillez contacter votre gestionnaire de la satisfaction client Braze afin de confirmer que Braze a bien activé SSL. Braze n'active SSL qu'une fois toutes les étapes de configuration terminées.

