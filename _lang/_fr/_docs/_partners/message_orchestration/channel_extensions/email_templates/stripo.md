---
nav_title: Stripo
article_title: Stripo
alias: /fr/partners/stripo
description: "Cet article décrit le partenariat entre Braze et Stripo, un constructeur de modèles de courriel glisser-déposer qui vous permet de créer facilement des e-mails sophistiqués avec des éléments interactifs."
page_type: partenaire
search_tag: Partenaire
---

# Stripo

> [Stripo](https://stripo.email/) est un constructeur de modèles d'e-mails par glisser-déposer qui vous aide à créer et concevoir des e-mails réactifs avec des éléments interactifs. Les utilisateurs de Stripo peuvent également modifier en HTML et décider quels éléments afficher ou masquer sur différents appareils via l'éditeur Stripo.

L'intégration de Braze et Stripo vous permet d'exporter vos e-mails Stripo personnalisés et de les télécharger en tant que modèles au sein du Brésil.

## Pré-requis

| Exigences           | Libellé                                                                                                                                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Stripo       | Un compte Stripo est requis pour profiter de ce partenariat.                                                                                                                                                            |
| Braze clé API REST  | Une clé API Braze REST avec les permissions complètes de **Modèles**. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__ |
| Instance de cluster | L'instance Braze [de votre instance]({{site.baseurl}}/api/basics/#endpoints) s'aligne sur votre tableau de bord Braze et votre point de terminaison REST.                                                               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

### Étape 1 : Créer un e-mail Stripo

Créez un e-mail Stripo sur la plateforme Stripo et cliquez sur **Exporter**.

![Export Stripo]({% image_buster /assets/img_archive/stripo_export.png %})

### Étape 2 : Exporter le modèle à Braze

Dans la boîte de dialogue qui apparaît, sélectionnez **Braze** comme méthode d'exportation

Ensuite, entrez votre **nom de compte** (i.e. Nom du groupe d'applications), **clé API**, et votre instance **cluster**.

![Forme Stripo]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
Ceci est une configuration unique et toutes les exportations à l'avenir utiliseront automatiquement cette clé API.
{% endalert %}

## Usage

Trouvez votre modèle Stripo téléchargé dans la section **Modèles & Médias > Modèles d'e-mail** de votre compte Braze. Vous pouvez maintenant utiliser ce modèle d'e-mail pour commencer à envoyer des messages de messagerie engageants à vos clients !
