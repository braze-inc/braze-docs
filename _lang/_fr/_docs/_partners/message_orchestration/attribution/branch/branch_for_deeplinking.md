---
nav_title: Branche pour les liens profonds
article_title: Branche pour les liens profonds
alias: /fr/partners/branch_pour_deeplinking/
page_type: partenaire
description: "Cet article décrit le partenariat entre Braze et la Branche et comment l'utiliser pour soutenir vos pratiques de liaison profonde."
search_tag: Partenaire
---

# Branche pour la liaison profonde {#branch}

{% include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branche][1], une plateforme mobile de liaison, vous aide à acquérir, engager, et mesurer sur tous les appareils, canaux et plates-formes en fournissant une vue globale de tous les points de contact de l'utilisateur.

L'intégration de Braze et de la Branche vous permet de fournir de meilleures expériences à vos clients en vous permettant d'attribuer correctement []({{site.baseurl}}/partners/advertising_technologies/attribution/branch_for_attribution/) le début de leur voyage utilisateur et de les connecter par le biais de liens profonds à l'emplacement prévu.

## Intégration

Suivez le guide d'intégration [SDK de la branche](https://help.branch.io/developers-hub/docs/native-sdks-overview) pour démarrer avec votre intégration de branche. Pour des cas d'utilisation supplémentaires, voir ci-dessous.

### Soutenir les liens universels iOS

Pour soutenir l'envoi de liens universels iOS en tant que liens profonds de l'intérieur du Brésil :

1. Suivez la documentation de la branche pour la mise en place de [liens universels][3].
2. Ajoutez le `ABKURLDelegate` à votre intégration Braze SDK pour [router les liens universels][4] depuis votre application.

### Lien profond dans l'e-mail

Consultez la documentation de la [Branche](https://docs.branch.io/pages/integrations/braze/) pour configurer des liens profonds à partir des e-mails envoyés par l'intermédiaire du Brésil.

Selon votre ESP, une personnalisation supplémentaire peut être nécessaire pour supporter les liens universels suivis de clic:

- [SendGrid][5]
- [Mailjet][6]
- [Poteau étincelant][7]

[1]: https://branch.io/
[3]: https://docs.branch.io/pages/deep-linking/universal-links/#search
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-customization
[5]: https://help.branch.io/using-branch/page/braze-sendgrid
[6]: https://help.branch.io/using-branch/page/braze-mailjet
[7]: https://help.branch.io/using-branch/page/braze-sparkpost