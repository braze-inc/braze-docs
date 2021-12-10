---
nav_title: Dépréciation TLS 1.0 & 1.1
page_order: 2
page_type: Mettre à jour
description: "Cet article décrit la dépréciation par Braze de TLS 1.0 et TLS 1.1, terminée en mai 2018."
---

# Dépréciation TLS 1.0 & 1.1

{% alert update %}
Braze a retiré le support des protocoles de chiffrement Transport Layer Security (TLS) dans les deux TLS 1. et 1.1, conformément aux recommandations formulées par le Conseil des normes de sécurité du PCI. Nous avons procédé à cette dépréciation du soutien en deux phases, complétées en mai 2018.
{% endalert %}

## Arrière-plan

Braze est en train de déprécier les procédés de chiffrement connus de Transport Layer Security (TLS) dans les deux TLS 1.0 et 1. , conformément aux recommandations formulées par le PCI Security Standards Council en deux phases se terminant en mai 2018.

Ce changement n’est pas effectué en réponse à une violation ou à un problème lié à la plateforme de Braze, mais par mesure de précaution pour maintenir nos meilleures normes de sécurité et de données et pour protéger proactivement nos clients et leurs clients.

Ces dernières années, un certain nombre de questions de sécurité systématiques liées à TLS et à ses prédécesseurs, Couche Sockets Secure (SSL), y compris [POODLE][1], [Heartbleed][2], [LOGJAM][3], et d'autres, menaçaient le trafic web crypté et exposaient des portions de l'internet à des violations de sécurité. Avec d'autres entreprises technologiques, Braze a déjà pris des mesures pour désactiver les protocoles et les algorithmes de chiffrement faibles au fur et à mesure que des attaques sont découvertes, par exemple, en supprimant le support de SSLv3 en 2014.

Plus récemment, le Conseil des normes de sécurité PCI a publié des directives relatives au chiffrement en avril 2015 pour la [norme de sécurité des données de l'industrie des cartes de paiement][4] (PCI-DSS). Le guide exclut SSL 3.0, TLS 1.0 et certaines des suites de chiffrement supportées par TLS 1. à partir de leur liste de protocoles de cryptage fort, et encourage les entreprises à cesser de supporter ces protocoles ou algorithmes pour assurer la sécurité des internautes.

Une suite de chiffrement est une combinaison d'algorithmes qui fournissent le chiffrement, l'authentification et l'intégrité des communications lors de la négociation d'une connexion sécurisée SSL ou TLS. Lorsqu’on a découvert qu’il était possible de briser un procédé de chiffrement donné – qu’il y ait ou non des attaques connues – le procédé de chiffrement est considéré comme présentant des « faiblesses » qui pourraient permettre de futures attaques. En excluant ces chiffrements TLS des exigences de conformité PCI DSS, le Conseil PCI DSS exige des fournisseurs de services qu'ils prennent en charge uniquement les meilleures normes de chiffrement. Le Conseil PCI DSS a fixé une date limite le 30 juin 2018 pour le respect de l'obligation de cryptage de ne plus prendre en charge le TLS 1. et TLS 1.1.

## Le plan de dépréciation de Braze
Afin de se conformer aux recommandations du Conseil PCI DSS, Braze augmentera les versions minimales de TLS que nous soutenons dans nos Services. Pour vous donner une meilleure idée de notre plan de conformité et de son impact potentiel sur votre marque et vos utilisateurs finaux, il y a deux phases principales de notre plan pour être conscient de:

### Phase 1 : 1er octobre 2017

Braze supprimera la possibilité d'utiliser les algorithmes suivants du tableau de bord Web de Braze et des APIs REST:

- `TLS_RSA_WITH_AES_256_CBC_SHA`
- `TLS_RSA_WITH_AES_128_CBC_SHA`
- `TLS_RSA_WITH_256_CBC_SHA256`
- `RSA_AVH_256_GCM_SHA384`
- `RSA_AVH_128_CBC_SHA256`
- `RSA_WITH_AES_128_GCM_SHA256`
- `TLS_RSA_WITH_3DES_EDE_CBC_SHA`

Ce changement ne devrait pas affecter les clients qui accèdent au tableau de bord de Braze, car tous les navigateurs Web modernes prennent en charge des algorithmes de chiffrement plus sécurisés. Cependant, si vous rencontrez une erreur de cryptage SSL lors de l'accès au tableau de bord web après le 1er octobre, vous serez en mesure de résoudre le problème en effectuant simplement la mise à jour vers la dernière version de votre navigateur Web.

Votre équipe d’ingénieurs devrait s’assurer qu’ils n’utilisent aucun de ces chiffrements pour communiquer entre serveurs et serveurs avec les API REST de Braze. S'ils le sont, ils devront mettre à jour leur code pour utiliser des algorithmes de chiffrement plus sécurisés avant le 1er octobre afin de continuer à utiliser les API de Braze. Cependant, afin de maintenir la prise en charge des appareils mobiles anciens ou périmés qui peuvent utiliser des algorithmes de chiffrement faibles, Braze continuera à supporter ces chiffrements sur l'APIS qui a reçu des données de nos SDK.

### Phase 2 : 31 mai 2018

Braze désactivera le support des TLS 1.0 et TLS 1. à travers tous les services Braze le 31 mai 2018 — y compris le tableau de bord Braze, les API REST et les APIs qui communiquent avec nos SDKs. Nous supprimerons également la prise en charge des algorithmes de chiffrement énumérés ci-dessus en relation avec les API qui reçoivent des données SDK. Cela signifie que toutes les communications TLS 1.0 et 1.1 de et vers Braze ne seront pas supportées par notre réseau à partir de cette date.

À la suite de ce changement, certains appareils mobiles anciens ou obsolètes – probablement ceux qui exécutent des versions antérieures d'Android – peuvent perdre la capacité de communiquer avec le Brésil, les empêchant d'envoyer des données à Braze ou de recevoir des messages dans l'application de Braze. Cependant, nous prévoyons que le changement n'affectera qu'un petit nombre d'appareils. Tous les périphériques qui sont affectés perdront également la possibilité de communiquer avec n'importe quel site ou service conforme à la PCI un mois plus tard le 30 juin, 2018, la date fixée par le PCI DSS Council pour le retrait de TLS 1. et les algorithmes TLS 1.1.

## Plan d'action
Si votre marque utilise les API REST de Braze, contactez votre équipe technique pour vous assurer que tous les appels de serveur à serveur à Braze s en utilisant TLS 1. par la liste ci-dessus afin d'éviter une interruption de service. Sachez que certains langages de programmation — comme Java 7 — utilisent par défaut les anciennes versions de TLS, pour que votre équipe d'ingénieurs ait besoin de quelques modifications de code pour prendre en charge les exigences de chiffrement mises à jour.

Les appareils Apple ne seront pas affectés par la dépréciation prévue par Braze parce qu’Apple a besoin de TLS 1.2 depuis la fin de 2016. Il en va de même pour les navigateurs Web modernes, donc nous ne prévoyons pas que ces changements auront un impact sur l'utilisation du Web SDK. Cependant, les appareils Android fonctionnant sous Android 4.4 (KitKat) ou inférieur peuvent ne pas utiliser TLS 1. par défaut, donc veuillez prendre des mesures pour mettre à jour l'une de vos intégrations Android vers au moins Braze SDK version 2. .3 (qui utilise TLS 1.2 par défaut, si un périphérique donné peut le supporter) d'ici le 31 mai 2018.

Enfin, en raison des faiblesses connues dans TLS 1.0 et TLS 1. suite de chiffrement, il est possible que des attaques puissent survenir dans le futur, ce qui nécessiterait Braze pour accélérer notre plan de dépréciation, afin de garantir la sécurité de tous nos clients. Braze surveillera l'état de sécurité et toutes les attaques pertinentes associées à TLS 1.0 et 1. , et vous gardera dans la boucle si nous apprenons des attaques qui modifieront la ligne de temps décrite ci-dessus. Mais à cause de cet impact potentiel, Nous vous recommandons fortement de travailler avec votre équipe d'ingénierie pour vous assurer que vos appels API à Braze sont sécurisés avec TLS 1. , et que vous prévoyez de passer au dernier SDK Android dans les mois à venir.


[1]: https://www.us-cert.gov/ncas/alerts/TA14-290A
[2]: https://en.wikipedia.org/wiki/Heartbleed
[3]: https://en.wikipedia.org/wiki/Logjam_(computer_security)
[4]: https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard
