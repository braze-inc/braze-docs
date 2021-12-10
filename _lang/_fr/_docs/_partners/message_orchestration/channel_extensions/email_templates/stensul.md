---
nav_title: Stensul
article_title: Stensul
alias: /fr/partners/stensul
description: "Cet article décrit le partenariat entre Braze et Stensul, une plateforme de messagerie d'entreprise qui vous permet de créer facilement des modèles de courriels répondant aux besoins de votre téléphone mobile sur tous les canaux."
page_type: partenaire
search_tag: Partenaire
---

# Stensul

> [Stensul](https://stensul.com/) permet aux courriers électroniques marketeurs de construire facilement des e-mails mobiles à marque à Stensul avant de les envoyer en aval au Brésil, en temps réel, pour la création de campagnes.

L'intégration de Braze et Stensul vous permet d'exporter vos e-mails Stensul au format HTML et de les télécharger en tant que modèles au Brésil.

## Pré-requis

| Exigences           | Libellé                                                                                                                                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Stensul      | Un compte Stensul est requis pour profiter de ce partenariat.                                                                                                                                                           |
| Braze clé API REST  | Une clé API Braze REST avec les permissions complètes de **Modèles**. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__ |
| Instance de cluster | L'instance Braze [de votre instance]({{site.baseurl}}/api/basics/#endpoints) s'aligne sur votre tableau de bord Braze et votre point de terminaison REST.                                                               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

Fournissez votre clé API Braze REST et l'instance de cluster à votre équipe de succès client Stensul. Une fois fournies, ils mettront en place l'intégration initiale pour vous.

{% alert important %}
Ceci est une configuration unique et toutes les exportations à l'avenir utiliseront automatiquement cette clé API.
{% endalert %}

### Étape 1 : Créer un e-mail Stensul

Créez un e-mail Stensul dans la plateforme Stensul et cliquez sur **Terminez**.

![Options de sauvegarde Stensul]({% image_buster /assets/img_archive/stensul_save_options.png %})

### Étape 2 : Exporter le modèle à Braze
Dans le nouveau dialogue qui apparaît sur la page d'achèvement, sélectionnez **Télécharger vers ESP**.

![Options de téléchargement Stensul]({% image_buster /assets/img_archive/stensul_upload_options.png %})

Ensuite, entrez le **nom du modèle**, **sujet**, et **préen-tête** pour votre e-mail et sélectionnez **Télécharger**. Vous recevrez alors une confirmation que le téléchargement a été réussi et un historique des précédents téléchargements du fichier, le cas échéant.

![Envoi de Stensul réussi]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## Usage

Trouvez votre modèle Stensul téléchargé dans la section **Modèles & Médias > Modèles d'e-mails** de votre compte Braze. Vous pouvez maintenant utiliser ce modèle d'e-mail pour commencer à envoyer des messages de messagerie engageants à vos clients !
