---
nav_title: Désactivation de TLS 1.0 et 1.1
page_order: 2

page_type: update
description: "Cet article décrit l’obsolescence de TLS 1.0 et TLS 1.1 de Braze, achevée en mai 2018."
---
# Désactivation de TLS 1.0 et 1.1

{% alert update %}
Braze a cessé sa prise en charge des chiffrements TLS (Transport Layer Security) dans les TLS 1.0 et 1.1, conformément aux recommandations du PCI Security Standards Council. Nous avons effectué cette déforestation de soutien en deux phases, achevée en mai 2018.
{% endalert %} 

## Arrière-plan

Braze désactive les chiffrements de sécurité des couches de transport TLS 1.0 et 1.1, conformément aux recommandations du PCI Security Standards Council, en deux phases qui seront terminées en mai 2018.

Ce changement n’est pas en réponse à une violation ou à un problème lié à la plateforme de Braze, c’est une mesure de précaution pour maintenir nos meilleures normes de sécurité et de données et protéger de façon proactive nos clients ainsi que leurs clients.

Ces dernières années, un certain nombre de problèmes de sécurité systématiques associés à la fois à TLS et à son prédécesseur, Secure Sockets Layer (SSL), notamment [POODLE](https://www.us-cert.gov/ncas/alerts/TA14-290A), [Heartbleed](https://en.wikipedia.org/wiki/Heartbleed) et [LOGJAM](https://en.wikipedia.org/wiki/Logjam_(computer_security)), ont menacé le trafic web crypté et exposé certaines parties de l'internet à des failles de sécurité. Comme les autres sociétés technologiques, Braze a déjà pris des mesures pour désactiver les protocoles de chiffrement faibles et les chiffrements lorsque des attaques sont découvertes, par exemple en arrêtant de prendre en charge SSLv3 en 2014.

Plus récemment, le Conseil des normes de sécurité PCI a publié en avril 2015 des orientations relatives au chiffrement pour la [norme de sécurité des données de l'industrie des cartes de paiement](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) (PCI-DSS). Ces directives excluent SSL 3.0, TLS 1.0 et certaines suites de chiffrement prises en charge par TLS 1.1 dans leur liste de protocoles de chiffrement cryptographique robuste et encouragent les entreprises à cesser de prendre en charge ces protocoles ou  chiffrements afin de garantir la sécurité des utilisateurs Internet.

Une suite de chiffrement est une combinaison d’algorithmes qui fournissent le cryptage, l’authentification et l’intégrité des communications lors de la négociation d’une connexion SSL ou TLS sécurisée. Quand on découvre qu’il peut être cassé, qu’il y ait ou non des attaques connues, le chiffrement est considéré comme ayant des « faiblesses » qui pourraient permettre de futures attaques. En excluant ces chiffrements TLS des exigences de conformité PCI DSS, le PCI DSS Council exige des fournisseurs de services qu’ils prennent en charge uniquement les meilleures normes de chiffrement. Le PCI DSS Council a fixé une date limite du 30 juin 2018 pour la conformité avec l’exigence de cryptage relative à la désactivation de TLS 1.0 et TLS 1.1.

## Plan d’obsolescence de Braze
Afin de se conformer aux recommandations du PCI DSS Council, Braze augmentera les versions minimales de TLS que nous prenons en charge sur nos Services. Pour vous donner une meilleure idée de notre plan de conformité et de son impact potentiel sur votre marque et vos utilisateurs, notre plan comporte deux phases principales :

### Phase 1 : 1er octobre 2017

Braze supprimera la capacité d’utiliser les  chiffrements suivants sur le tableau de bord Web de Braze et des API REST :

- `TLS_RSA_WITH_AES_256_CBC_SHA`
- `TLS_RSA_WITH_AES_128_CBC_SHA`
- `TLS_RSA_WITH_AES_256_CBC_SHA256`
- `TLS_RSA_WITH_AES_256_GCM_SHA384`
- `TLS_RSA_WITH_AES_128_CBC_SHA256`
- `TLS_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_RSA_WITH_3DES_EDE_CBC_SHA`

Ce changement ne devrait pas affecter les clients accédant au tableau de bord de Braze, car tous les navigateurs Web modernes prennent en charge des méthodes de chiffrement plus sécurisées. Cependant, si vous avez une erreur de cryptage SSL en accédant au tableau de bord Web après le 1er octobre, vous pourrez résoudre le problème simplement en installant la dernière version de votre navigateur Web.

Votre équipe d’ingénierie doit s’assurer qu’elle n’utilise aucun de ces chiffrements pour des communications serveur à serveur avec les API REST de Braze. Si c’est le cas, elle devra mettre à jour son code pour utiliser des chiffrements plus sécurisés avant le 1er octobre pour pouvoir continuer à utiliser les API de Braze. Toutefois, pour maintenir le support pour les appareils mobiles anciens et obsolètes qui peuvent utiliser des chiffrements faibles, Braze continuera à prendre en charge ces ciphers sur les API qui ont reçu des données de nos SDK.

### Phase 2 : 31 mai 2018

Braze va désactiver TLS 1.0 et TLS 1.1 sur tous les services Braze le 31 mai 2018, y compris le tableau de bord de Braze, les API REST et les API qui communiquent avec nos SDK. Nous désactiverons également les chiffrements répertoriés dans la section précédente en relation avec les API qui reçoivent des données SDK. Cela signifie que toutes les communications TLS 1.0 et 1.1 vers et depuis Braze ne seront pas prises en charge par notre réseau à compter de cette date.

À la suite de ce changement, certains appareils mobiles anciens ou obsolètes, qui sont susceptibles d’être utilisés en version précoce d’Android, peuvent perdre la capacité de communiquer avec Braze, les empêchant d’envoyer des données à Braze ou de recevoir des messages dans l’application Braze. Cependant, nous prévoyons que ce changement affectera seulement un petit nombre d’appareils. Tous les appareils concernés perdent également la capacité de communiquer avec tout site Internet ou service conforme à la norme PCI un mois plus tard, le 30 juin 2018, date fixée par le PCI DSS Council pour la désactivation des chiffrements TLS 1.0 et TLS 1.1.

## Plan d’action
Si votre marque utilise les API REST de Braze, adressez-vous à votre équipe d’ingénierie pour vous assurer que tous les appels serveurs à serveurs vers Braze utilisent TLS 1.2 avant les dates citées ci-dessus pour éviter une interruption de service. Sachez que certains langages de programmation, comme Java 7, utilisent par défaut des versions plus anciennes de TLS, et votre équipe d’ingénierie devra peut-être modifier du code pour se conformer à ces nouvelles exigences de chiffrement.

Les appareils Apple ne seront pas affectés par la mise en obsolescence prévue de Braze, car Apple requiert TLS 1.2 depuis fin 2016. Il en va de même pour les navigateurs Web modernes, donc nous ne prévoyons pas que ces changements auront un impact sur l’utilisation du SDK Web. Cependant, les appareils Android exécutant Android 4.4 (KitKat) ou inférieur ne peuvent pas utiliser TLS 1.2 par défaut, alors prenez des mesures pour mettre à niveau l’une quelconque de vos intégrations Android à au moins le système de développement de données de Braze version 2.0.3 (qui utilise TLS 1.2 par défaut, si un appareil donné peut le prendre en charge), avant le 31 mai 2018.

Enfin, en raison des faiblesses connues de TLS 1.0 et de la suite de chiffrement TLS 1.1, il est possible que des attaques puissent survenir à l’avenir, ce qui nous obligerait à accélérer notre plan de dépréciation afin d’assurer la sécurité de tous les clients de Braze. Braze surveillera le paysage de sécurité et toutes les attaques dues aux protocoles TLS 1.0 et 1.1, et vous tiendra informé si des attaques nous poussent à modifier le calendrier présenté un peu plus haut. Mais en raison de cet impact potentiel, nous vous recommandons vivement de travailler avec votre équipe d’ingénierie pour vous assurer que vos appels API vers Braze sont sécurisés avec TLS 1.2, et de prévoir une mise à niveau vers le dernier SDK Android dans les prochains mois.


