---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "L'intégration de Braze et d'Alpaco s'appuie sur la syntaxe d'Alpaco pour créer et exporter vers Braze des modèles d'e-mails basés sur des données."
page_type: partner
search_tag: Partner

---

# Alpaco

> [Alpaco](https://alpaco.email/) est un outil de marketing par e-mail en ligne qui offre un éditeur par glisser-déposer pour un nouveau niveau de contrôle de la conception et de la production. L'intégration entre Braze et Alpaco vous permet d'exporter vers Braze des e-mails conformes à votre marque et axés sur les données. 

_Cette intégration est maintenue par Alpaco._

{% alert note %}
Alpaco prend en charge l'[intégralité des variables liquides](https://shopify.github.io/liquid/) et, à ce titre, prend également en charge l'intégralité des variables liquides utilisées dans vos configurations de Braze.
{% endalert %}

## Conditions préalables

| Condition | Descriptif |
| ------------| ----------- |
| Compte Alpaco | Un compte Alpaco est nécessaire pour tirer parti de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations complètes sur les **modèles**. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Instance de cluster | Votre [instance de cluster]({{site.baseurl}}/api/basics/#endpoints) Braze s'aligne sur votre tableau de bord de Braze et votre endpoint REST. <br><br> Par exemple, si l'URL de votre tableau de bord est `https://dashboard-03.braze.com`, votre endpoint sera `dashboard-03`.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration

Fournissez votre clé API REST Braze et votre instance de cluster à l'équipe de satisfaction client d'Alpaco. L'équipe mettra ensuite en place l'intégration initiale pour vous.

{% alert note %}
Il s'agit d'une configuration unique et toutes les exportations futures utiliseront automatiquement cette clé API.
{% endalert %}

## Exportation des e-mails d'Alpaco vers Braze

### Étape 1 : Créer un modèle d'e-mail dans Alpaco

Dans la plateforme Alpaco, utilisez les différents paramètres et options pour créer un modèle qui exprime l'identité de votre marque. Sélectionnez **Enregistrer** lorsque vous êtes satisfait de votre modèle.

![Modèle Créer Alpaco]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Étape 2 : Créer un e-mail

Une fois le modèle créé, accédez au lobby et créez un e-mail avec le modèle. Sélectionnez **Vérifier** pour vous assurer que tout est correct.

![Créer un e-mail Alpaco]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Étape 3 : Vérifier un e-mail et l’exporter vers Braze

Sélectionnez **Exporter** et choisissez l'intégration Braze pour exporter votre modèle d'e-mail vers Braze. 

Si vous souhaitez apporter des modifications à votre modèle d'e-mail, faites-les dans Alpaco, puis exportez à nouveau l'e-mail vers Braze. Cela mettra à jour l'e-mail dans Braze avec vos changements.

![Exporter e-mail Alpaco]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Utiliser les modèles d'e-mail d'Alpaco dans Braze

Retrouvez votre e-mail Alpaco téléchargé en naviguant vers **Modèles et médias > Modèles d'e-mail** dans le tableau de bord de Braze. Vous pouvez maintenant utiliser ce modèle pour envoyer à vos utilisateurs des e-mails axés sur la marque et les données.


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
