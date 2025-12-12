---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "L'intégration entre Braze et Alpaco vous permet d'exporter vers Braze des modèles d'e-mail et des blocs de contenu conformes à la marque et compatibles avec Liquid, prêts à être utilisés dans les e-mails et les messages in-app."
page_type: partner
search_tag: Partner
---

# Alpaco

> [Alpaco](https://alpaco.email/) est un outil de gestion créative en ligne qui offre un éditeur par glisser-déposer permettant de créer du contenu réutilisable et sûr pour la marque Braze. L'intégration d'Alpaco et de Braze vous permet d'exporter des blocs de contenu, des modèles d'e-mail et des modèles de message in-app.

_Cette intégration est maintenue par Alpaco._

{% alert note %}
Alpaco prend en charge l'[intégralité des variables liquides](https://shopify.github.io/liquid/) et, à ce titre, prend également en charge l'intégralité des variables liquides utilisées dans vos configurations de Braze.
{% endalert %}

## Conditions préalables

| Condition | Descriptif |
| ------------| ----------- |
| Compte Alpaco | Un compte Alpaco est nécessaire pour tirer parti de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations complètes sur les **modèles**. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Instance de cluster | Votre [instance de cluster]({{site.baseurl}}/api/basics/#endpoints) Braze s'aligne sur votre tableau de bord de Braze et votre endpoint REST. <br><br> Par exemple, si l'URL de votre tableau de bord est `https://dashboard-03.braze.com`, votre endpoint sera `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Cas d’utilisation

- Exportez des **modèles d'e-mail** entièrement conçus pour les campagnes de Braze et l'envoi de messages transactionnels.
- Créez et gérez des **blocs de contenu modulaires** (e.g., en-têtes, pieds de page, promotions) qui peuvent être réutilisés sur plusieurs canaux.
- Concevez des **messages in-app** attrayants avec la même flexibilité créative que les e-mails, ce qui permet de proposer facilement des expériences cohérentes et conformes à la marque sur l'ensemble des canaux.
- Permettez la **personnalisation** en incluant des étiquettes Liquid prises en charge par Braze, telles que `{{first_name}}` ou `{{custom_attribute}}`.
- Maintenez la **cohérence de la marque** en centralisant la conception créative dans Alpaco et en poussant les mises à jour vers Braze avec une seule exportation.

## Intégration

Fournissez votre clé API REST Braze et votre instance de cluster à l'équipe de satisfaction client d'Alpaco. L'équipe mettra ensuite en place l'intégration initiale pour vous.

{% alert note %}
Il s'agit d'une configuration unique et toutes les exportations futures utiliseront automatiquement cette clé API.
{% endalert %}

## Exportation des messages d'Alpaco vers Braze

### Étape 1 : Créer un modèle dans Alpaco

Dans Alpaco, créez un modèle qui exprime l'identité de votre marque. Lorsque vous êtes prêt, sélectionnez **Enregistrer.**

![Modèle Créer Alpaco]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Étape 2 : Rédiger un message en utilisant le modèle

Ensuite, rendez-vous dans le lobby d'Alpaco et utilisez votre modèle pour créer un e-mail, un message in-app ou un bloc de contenu. Pour vérifier votre message avant de l'exporter, sélectionnez **Réviser.**

![Créer un e-mail Alpaco]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Étape 3 : Exporter votre message à Braze

Sélectionnez **Exporter**, puis choisissez l'intégration Braze et indiquez si vous exportez un modèle d'e-mail ou un bloc de contenu.

Si vous apportez des modifications après l'exportation, vous pouvez réexporter le contenu depuis Alpaco pour le mettre à jour dans Braze.

![Exporter e-mail Alpaco]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Utilisation des gabarits et des blocs Alpaco dans Braze

Selon le type de contenu que vous exportez, votre modèle apparaîtra dans l'une des sections suivantes :

- **Modèles et médias > Modèles d'e-mail**
- **Modèles et médias > Blocs de contenu**

Les modèles d'Alpaco sont idéaux pour les gestionnaires qui souhaitent gérer la cohérence de leur marque de manière centralisée. Ils prennent également en charge les tags intégrés de Braze pour faciliter la catégorisation et la gestion du contenu.
