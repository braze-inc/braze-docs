---
nav_title: Aperçu SSL
article_title: Aperçu SSL
page_order: 9
page_type: Référence
description: "Cet article de référence couvre le SSL, ce qui est utilisé et comment il est utilisé au Brésil."
channel: Email
---

# SSL à Braze

{% include video.html id="zP1N_wN0SsQ" align="right" %}

> Un Secure Socket Layer (SSL) crypte une URL avec HTTPS au lieu du protocole HTTP moins sécurisé. Les URL avec HTTPS indiquent qu'un certificat SSL ou TLS valide et digne de confiance existe et que le site est en toute sécurité à visiter et non pas une arnaque ou la source de logiciels malveillants dangereux.

## Pourquoi SSL est-il important ?

Bien que la plupart des domaines ne requièrent pas de SSL, ce sont les raisons pour lesquelles nous recommandons fortement SSL à nos utilisateurs :
1. __Requis par certains navigateurs principaux__: les protocoles SSL sont de plus en plus répandus aujourd'hui car les principaux navigateurs comme Google Chrome commencent à restreindre le trafic à travers des URL non sécurisées pour protéger leurs utilisateurs. Les entreprises avec SSL sur leur site Web s'assurent à ces principaux navigateurs que leur contenu est fiable, minimiser les problèmes de visualisation de contenu tels que les liens cassés et les images dans leurs e-mails.<br><br>
2. __Nécessaire pour Click and Open Tracking__: Au Brésil, quand nous envoyons des emails, nous transformons d'abord vos liens à l'aide de votre sous-domaine de suivi de liens de marque pour suivre les clics utilisateur et s'ouvrir. Par défaut, ces liens commenceront par HTTP. Cela signifie que les utilisateurs avec un navigateur ou une extension qui restreint le trafic non sécurisé peuvent avoir des difficultés à traverser la redirection avant d'atterrir à l'URL de destination, même si l'URL est sécurisée. Cela peut conduire à des images cassées et des clics inexacts et ouvrir le suivi à travers vos e-mails. Pour cette raison, il est préférable d'appliquer une couche SSL au sous-domaine de suivi des liens pour assurer des redirections sécurisées dans vos e-mails. <br><br>
3. __Les domaines HSTS requièrent SSL__: indépendamment de quels navigateurs vos utilisateurs peuvent accéder à vos e-mails, vous devez configurer SSL si vous avez un domaine HTTP Strict Transport Security (HSTS) et configurer un CDN pour envoyer les certificats de sécurité nécessaires. Si la configuration de SSL échoue, l'image et les liens web seront cassés.<br><br>
4. __Meilleures pratiques générales__: sécuriser votre site Web et les liens avec SSL est une pratique courante même pour les entreprises qui ne traitent pas directement avec des informations clients sensibles. Les utilisateurs font plus confiance aux liens qui sont sécurisés avec SSL, et la couche supplémentaire d'authentification aide à protéger vos données.

## Acquisition d'un certificat SSL

L'acquisition d'un certificat SSL peut se faire en utilisant un tiers, généralement un réseau de distribution de contenu (CDN). Un CDN peut héberger le certificat SSL et le servir au navigateur à chaque fois qu'un de vos liens est cliqué. Cela se fait en redirigeant le trafic à travers le CDN pour appliquer les certificats nécessaires avant de l'envoyer à nos partenaires de courriel Sendgrid ou Sparkpost.

Prêt à démarrer avec votre installation SSL? Consultez notre prochain article SSL [ici]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ssl/ssl_clicktracking/). 