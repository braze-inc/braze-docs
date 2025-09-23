---
nav_title: Stripo
article_title: Stripo
alias: /partners/stripo
description: "Cet article de référence présente le partenariat entre Braze et Stripo, un générateur de modèles d'e-mails par glisser-déposer qui vous permet de créer facilement des e-mails sophistiqués avec des éléments interactifs."
page_type: partner
search_tag: Partner

---

# Stripo

> [Stripo](https://stripo.email/) est un générateur de modèles d'e-mails par glisser-déposer qui vous aide à créer et à concevoir des e-mails responsives avec des éléments interactifs. Les utilisateurs de Stripo peuvent également modifier en HTML et décider des éléments à afficher ou à masquer sur différents appareils grâce à l'éditeur de Stripo.

_Cette intégration est maintenue par Stripo._

## À propos de l'intégration

L'intégration de Braze et Stripo vous permet d'exporter vos e-mails Stripo personnalisés et de les télécharger en tant que modèles dans Braze.

## Prérequis

| Condition | Descriptif |
| ------------| ----------- |
| Compte Stripo | Un compte Stripo est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations complètes sur les **modèles**. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Instance de cluster | Votre [instance de cluster]({{site.baseurl}}/api/basics/#endpoints) Braze s'aligne sur votre tableau de bord de Braze et votre endpoint REST.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration

### Étape 1 : Créer un e-mail Stripo

Créez un e-mail Stripo dans la plateforme Stripo et cliquez sur **Exporter.** 

![Stripo Export]({% image_buster /assets/img_archive/stripo_export.png %})

### Étape 2 : Exporter le modèle vers Braze

Dans la boîte de dialogue qui s'affiche, sélectionnez **Braze** comme méthode d'exportation 

Ensuite, entrez votre **nom de compte** (tel que le nom de l'espace de travail), votre **clé API** et votre **instance de cluster**.

![Stripo Form]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
Il s'agit d'une configuration unique, et toutes les prochaines exportations utiliseront automatiquement cette clé API.
{% endalert %}

## Utilisation

Recherchez le modèle Stripo qui a été chargé dans la section **Modèles et médias > Modèles d'e-mail** dans votre compte Braze. Vous pouvez maintenant utiliser ce modèle d'e-mail pour commencer à envoyer des messages engageants à vos clients !


