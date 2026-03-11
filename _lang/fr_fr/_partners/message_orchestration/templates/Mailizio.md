---
nav_title: Mailizio
article_title: Mailizio
alias: /partners/mailizio
description: "Cet article de référence présente le partenariat entre Braze et Mailizio, une plateforme de création et de gestion d'e-mails qui vous permet de concevoir des contenus réutilisables et sécurisés pour votre marque et de les exporter vers Braze."
page_type: partner
search_tag: Partner

---

# Mailizio

> [Mailizio](https://mailizio.com/) est une plateforme de création et de gestion d'e-mails qui facilite la conception de contenus réutilisables et adaptés à la marque à l'aide d'un éditeur visuel intuitif. Grâce à l'intégration de Mailizio à Braze, vous pouvez exporter vos blocs de contenu et vos modèles d'e-mail, puis générer automatiquement des messages in-app à partir de ces mêmes ressources, ce qui permet un déploiement rapide et entièrement contrôlé des campagnes.

_Cette intégration est maintenue par Mailizio._

## À propos de l'intégration

L'intégration de Mailizio et Braze vous permet de concevoir des modèles d'e-mails dynamiques à l'aide de l'éditeur de Mailizio, d'exploiter les variables Liquid telles qu'elles sont utilisées dans vos configurations Braze, et de les envoyer à Braze pour une exécution rationalisée de la campagne.

## Cas d’utilisation

- Transférez des modèles d'e-mails prêts à l'emploi directement dans Braze pour les campagnes et les messages transactionnels.
- Créez des modules de contenu réutilisables (en-têtes, pieds de page, promotions et autres) pour rationaliser la production sur plusieurs campagnes et canaux.
- Générez des messages in-app à partir d'e-mails : Mailizio identifie les sections pertinentes de votre e-mail et vous permet d'exporter le HTML pour l'utiliser dans vos campagnes in-app.
- Personnalisez à l'échelle avec des variables Liquid compatibles avec Braze dans les e-mails et les messages in-app.
- Veillez à la cohérence de votre image de marque en gérant les ressources créatives dans Mailizio et en les mettant à jour dans Braze à l'aide d'une seule exportation.

## Conditions préalables

| Condition | Description |                          
| ----------- | ----------- |  
| Compte Mailizio | Un compte Mailizio est nécessaire pour bénéficier de ce partenariat. |  
| Clé d'API REST Braze | Une clé API Braze REST avec des autorisations complètes sur les **modèles**.<br><br>Vous pouvez créer une clé API REST de Braze dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API.** |  
| Endpoint REST Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépend de l'URL Braze de votre instance. |  
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration

Fournissez votre clé API REST Braze et votre instance de cluster à votre gestionnaire de satisfaction client Mailizio. L'équipe Mailizio met ensuite en place l'intégration initiale pour vous.

{% alert important %}
Il s'agit d'une configuration unique, et toutes les exportations futures utiliseront automatiquement cette clé API.
{% endalert %}

### Étape 1 : Créer un e-mail dans Mailizio

Dans Mailizio, utilisez l'éditeur par glisser-déposer pour créer un e-mail qui reflète l'identité de votre marque, puis cliquez sur **Enregistrer** pour conserver votre travail.

![éditeur par glisser-déposer screenshot]({% image_buster /assets/img/mailizio/screenshot_1.png %})

### Étape 2 : Exporter votre modèle d'e-mail vers Braze

Lorsque vous êtes prêt, cliquez sur **Exporter la lettre d'information**. Dans la fenêtre contextuelle, sélectionnez **Braze-email** et confirmez l'exportation.

Si vous mettez à jour votre contenu ultérieurement, réexportez à partir de Mailizio pour l'actualiser dans Braze.

![capture d'écran de la fenêtre modale/boîte de dialogue, etc.]({% image_buster /assets/img/mailizio/screenshot_2.png %})

{% alert important %}  
Vous pouvez créer et exporter des blocs de contenu de la même manière en utilisant l'éditeur de **modules** de Mailizio.  
{% endalert %}

## Utilisation

Retrouvez le modèle Mailizio que vous avez téléchargé dans la section **Modèles & Media > Modèles d'e-mail de** votre compte Braze. Vous pouvez désormais utiliser ce modèle d'e-mail pour commencer à envoyer des e-mails attrayants à vos clients !
