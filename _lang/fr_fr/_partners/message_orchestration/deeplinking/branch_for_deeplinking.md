---
nav_title: Branch pour la création de liens profonds
article_title: Branch pour la création de liens profonds
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "Cet article de référence décrit le partenariat entre Braze et Branch et comment il peut vous aider à créer des liens profonds."
search_tag: Partner

---

# Branch pour la création de liens profonds {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://branch.io/), une plateforme de liaison mobile, vous aide à acquérir, engager et mesurer à travers tous les appareils, canaux et plateformes en fournissant une vue complète de tous les points de contact de l'utilisateur.

_Cette intégration est maintenue par la branche._

## À propos de l'intégration

L'intégration de Braze et Branch vous permet d'offrir de meilleures expériences à vos clients en [attribuant]({{site.baseurl}}/partners/message_orchestration/attribution/branch_for_attribution/) correctement le début de leur parcours utilisateur et en les connectant par des liens profonds à l'emplacement prévu.

## Intégration

Consultez [le guide d'intégration du SDK de Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview) pour mettre en place votre intégration Branch. Vous trouverez ci-dessous d'autres cas d'utilisation.

### Prise en charge des liens universels iOS

Pour prendre en charge l'envoi de liens universels iOS en tant que liens profonds dans Braze :

1. Suivez les instructions fournies dans la documentation de Branch pour configurer les [liens universels](https://help.branch.io/developers-hub/docs/ios-universal-links).
2. Mettez en œuvre la méthode [`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate)[braze(_:shouldOpenURL :)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:shouldopenurl:)-6xxc5) dans votre intégration SDK Braze pour [acheminer les liens universels]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-handling-customization) depuis votre application.

### Création de liens profonds dans des e-mails

Consultez notre documentation sur les [liens universels et les liens applicatifs.]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/)
ou consultez [la documentation de Branch](https://help.branch.io/developers-hub/docs/ios-universal-links#apps-that-always-work) pour mettre en place la création de liens profonds à partir d'e-mails envoyés par l'intermédiaire de Braze.

La liaison avec des numéros de téléphone (en ajoutant `tel` à `href`) n'est pas prise en charge dans l'application Gmail pour iOS, sauf si l'utilisateur accorde des autorisations d'appel à l'application.

En fonction de votre ESP, une personnalisation supplémentaire peut être nécessaire pour prendre en charge les liens universels avec suivi des clics. Vous trouverez ces informations dans notre article dédié. Vous pouvez également consulter les références suivantes pour en savoir plus :

- [Sendgrid](https://help.branch.io/using-branch/page/braze-sendgrid)
- [SparkPost](https://help.branch.io/using-branch/page/braze-sparkpost)


