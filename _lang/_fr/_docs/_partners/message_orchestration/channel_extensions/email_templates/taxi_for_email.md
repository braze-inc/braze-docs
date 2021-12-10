---
nav_title: Taxi par e-mail
article_title: Taxi par e-mail
alias: /fr/partners/taxi_for_email
description: "Cet article décrit le partenariat entre Braze et Taxi pour courriel, un outil de marketing de courriel en ligne qui permet aux clients de Braze de créer des modèles de courriel intelligents en utilisant leur interface glisser-déposer et une syntaxe simple mais puissante."
page_type: partenaire
search_tag: Partenaire
---

# Taxi par e-mail

[Taxi for Email](http://taxiforemail.com/) est un outil de marketing par e-mail en ligne qui offre un éditeur d'e-mail visuel intuitif glisser-déposer. Les taxis encouragent les équipes à collaborer facilement sur des campagnes de courriel, permettant aux rédacteurs et aux rédacteurs en chef l'accès et les ressources dont ils ont besoin pour construire des e-mails, le tout sans code.

L'intégration de Braze et Taxi tire parti de la syntaxe simple mais puissante de Taxi, pour créer et exporter des modèles d'e-mails intelligents vers Brésil.

## Pré-requis

| Exigences               | Libellé                                                                                                                                                                                                                                                                                       |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Taxi pour compte e-mail | Un compte Taxi pour Courriel est requis pour profiter de ce partenariat.                                                                                                                                                                                                                      |
| Braze clé API REST      | Une clé API Braze REST avec les permissions complètes de **Modèles**. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__                                                                       |
| Braze endpoint          | Votre point de terminaison [Braze]({{site.baseurl}}/api/basics/#endpoints) s'aligne sur l'URL de votre tableau de bord Braze.<br><br> Par exemple, si l'URL de votre tableau de bord est `https://dashboard-03. raze.com`, votre point de terminaison sera `tableau de bord -03`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

### Étape 1 : Créer un modèle d'e-mail de taxi

Créez un modèle de Taxi sur la plateforme de Taxi. Une fois créé, accédez à votre **Paramètres de l'organisation** et sélectionnez l'onglet **Connecteurs ESP**.

### Étape 2 : Créer un connecteur Braze

1. Dans la boîte de dialogue qui apparaît, cliquez sur le bouton **Ajouter un nouveau** et sélectionnez **Braze** dans la liste déroulante.
2. Cliquez sur **Braze** pour modifier les paramètres du connecteur Braze.
3. Entrez votre point de terminaison Braze et votre clé API Braze.

Votre champ de connecteur deviendra vert une fois que les détails avec les autorisations correctes seront fournis. Si ce champ n'est pas vert, vérifiez que vos champs correspondent aux exigences énumérées ci-dessus.

## Usage

Trouvez votre modèle de taxi téléchargé dans la section **Modèles & Médias > Modèles d'e-mail** de votre compte Braze. Vous pouvez maintenant utiliser ce modèle d'e-mail pour commencer à envoyer des messages de messagerie engageants à vos clients !
