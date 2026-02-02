---
nav_title: Configurer avec Braze
article_title: Configurer avec Braze
page_order: 1
description: "Découvrez comment configurer et intégrer BrazeAI Decisioning <sup>StudioTM</sup> Go dans Braze."
---

# Configurer avec Braze

> Créez une campagne API dans Braze conçue pour BrazeAI Decisioning Studio™ Go.

## Étape 1 : Créer votre campagne 

1. Dans le tableau de bord de Braze, allez dans **Envoi de messages** > Campagnes.
2. Sélectionnez **Créer une campagne**.
3. Pour votre type de campagne, sélectionnez **Campagne API**.
4. Saisissez un nom pour votre campagne. Un exemple est "Decisioning Studio Go Email".

![Une campagne API intitulée "Decisioning Studio Go Email".]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5\. Pour votre canal de communication, sélectionnez **E-mail.**

![Option permettant de sélectionner votre canal de communication pour la campagne API.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6\. Dans **Options supplémentaires**, cochez la case **Autoriser les utilisateurs à redevenir éligibles pour recevoir la campagne.** 
7\. Pour le délai de réadmissibilité, entrez **1** et sélectionnez **Heures** dans la liste déroulante.

![Rééligibilité pour la campagne API sélectionnée.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8\. Sélectionnez **Enregistrer la campagne**.

## Étape 2 : Copiez et collez l'ID de votre campagne

Dans votre campagne API, copiez l'**ID de** la campagne. Ensuite, rendez-vous sur le portail BrazeAI Decisioning Studio™ Go et collez l'**ID de la campagne**.

![Un exemple d'envoi de messages ID à copier-coller.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

## Étape 3 : Copiez et collez votre envoi de messages ID

Dans votre campagne API, copiez l'**ID de la variation du message.** Ensuite, accédez au portail BrazeAI Decisioning Studio™ Go et collez l'**ID de la variation du message**.
