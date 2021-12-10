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

> [Branche][1], une plateforme mobile de liaison, vous aide à acquérir, engager, et mesurer sur tous les appareils, canaux et plates-formes en fournissant une vue globale de tous les points de contact de l'utilisateur. Cet article vous guidera à travers la façon d'utiliser la Branche avec Braze pour répondre à vos besoins de liens profonds.

Branche, avec Braze, vous permet de fournir de meilleures expériences à vos clients en vous permettant d'attribuer correctement le début de leur voyage utilisateur & de les connecter à travers des liens profonds vers leur emplacement prévu.

La branche et Braze vous aident à comprendre exactement quand et où les utilisateurs ont été acquis, ainsi que comment personnaliser leurs voyages grâce à une [attribution]({{site.baseurl}}/partners/advertising_technologies/attribution/branch_for_attribution/) robuste et un lien profond.


## Installer l'attribution {#branch-install-attribution}

La succursale offre une fonction d'attribution d'installation pour mesurer l'acquisition des utilisateurs. Consultez notre [documentation d'attribution][2] pour des instructions d'intégration.

## Liaison profonde

Suivez le guide d'intégration SDK de la branche pour démarrer avec votre intégration Branch et Braze. Pour des cas d'utilisation supplémentaires, voir ci-dessous.

## Prise en charge des liens universels iOS

Pour soutenir l'envoi de liens iOS Universal en tant que liens profonds de l'intérieur du Brésil :

1. Suivez la documentation de la branche [pour la configuration des liens universels][3].
2. Ajoutez `ABKURLDelegate` à votre intégration Braze SDK pour acheminer les liens universels depuis votre application. Consultez notre [documentation de personnalisation de lien][4] pour plus de détails sur l'implémentation.

## Lien profond dans l'e-mail

Pour configurer des liens profonds à partir des e-mails envoyés via Braze, consultez la documentation de la [Branche](https://docs.branch.io/pages/integrations/braze/).

Selon votre ESP, une personnalisation supplémentaire est nécessaire pour supporter les liens universels suivis de clic:

- [SendGrid][5]
- [Mailjet][6]
- [Poteau étincelant][7]


[1]: https://branch.io/
[2]: {{site.baseurl}}/partners/branch_for_attribution/
[3]: https://docs.branch.io/pages/deep-linking/universal-links/#search
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-customization
[5]: https://help.branch.io/using-branch/page/braze-sendgrid
[6]: https://help.branch.io/using-branch/page/braze-mailjet
[7]: https://help.branch.io/using-branch/page/braze-sparkpost
