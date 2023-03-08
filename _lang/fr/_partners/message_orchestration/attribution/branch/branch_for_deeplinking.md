---
nav_title: Branch pour la création de liens profonds
article_title: Branch pour la création de liens profonds
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "Cet article décrit le partenariat entre Braze et Branch et comment l’utiliser pour soutenir vos pratiques de création de liens profonds."
search_tag: Partenaire

---

# Branch pour la création de liens profonds {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch][1] est une plateforme de liaison mobile qui vous aide à acquérir, engager et mesurer à travers tous les appareils, canaux et plateformes en vous offrant une vue complète de tous les points de contact avec les utilisateurs.

L’intégration de Braze et de Branch vous permet d’offrir de meilleures expériences à vos clients en vous permettant d’[attribuer]({{site.baseurl}}/partners/advertising_technologies/attribution/branch_for_attribution/) correctement le début de leur parcours d’utilisateur et de les relier par des liens profonds à l’emplacement prévu.

## Intégration

Pour assurer une bonne intégration de Branch, reportez-vous au [Guide d’intégration SDK de Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview). Reportez-vous au contenu suivant pour des cas d’utilisation supplémentaires.

### Prise en charge des liens universels iOS

Pour prendre en charge l’envoi de liens universels iOS en tant que liens profonds depuis Braze :

1. Reportez-vous à la documentation de Branch pour la configuration de [liens universels][3].
2. Ajouter la valeur `ABKURLDelegate` à votre intégration SDK Braze pour [acheminer les liens universels][4] à partir de votre application.

### Création de liens profonds dans l’e-mail

Voir la [documentation de Branch](https://docs.branch.io/pages/integrations/braze/) pour créer des liens profonds dans les e-mails envoyés par le biais de Braze.

Selon votre fournisseur de services d’e-mail, une personnalisation supplémentaire peut être nécessaire pour prendre en charge les liens universels suivis par clic :

- [SendGrid][5]
- [Mailjet][6]
- [SparkPost][7]

[1]: https://branch.io/
[2]: {{site.baseurl}}/partners/branch_for_attribution/
[3]: https://docs.branch.io/pages/deep-linking/universal-links/#search
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-customization
[5]: https://help.branch.io/using-branch/page/braze-sendgrid
[6]: https://help.branch.io/using-branch/page/braze-mailjet
[7]: https://help.branch.io/using-branch/page/braze-sparkpost