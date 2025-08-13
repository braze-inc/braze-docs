---
nav_title: Atelier
article_title: Atelier de personnalisation Amazon Personalize
alias: /partners/amazon_personalize_workshop/
description: "Cet article de référence décrit le processus de configuration d'Amazon Personalize et son intégration dans votre environnement Braze à l'aide du contenu connecté."
page_type: partner
search_tag: Partner
---

# Atelier Amazon Personalize

> Cet article de référence vous guidera dans le processus de configuration d'Amazon Personalize et de son intégration dans votre environnement Braze à l'aide du contenu connecté. Pour ce faire, un atelier pratique vous guidera à travers toutes les étapes nécessaires au déploiement et à la formation des solutions Amazon Personalize et à leur intégration dans une campagne d'e-mailing de Braze.

_Cette intégration est gérée par Amazon Personalize._

## À propos de l'intégration

Les exemples suivants sont déployés dans un exemple de site de commerce électronique entièrement fonctionnel appelé Retail Demo Store (Boutique démo). Les ressources et le code de ce tutoriel sont publiés dans la [boutique de démonstration AWS Samples Retail.](https://github.com/aws-samples/retail-demo-store/) Vous pouvez utiliser cette mise en œuvre de l'architecture de référence comme une ébauche pour mettre en œuvre Amazon Personalize dans votre propre environnement.

## Exigences

Vous devez cloner la [boutique de démonstration](https://github.com/aws-samples/retail-demo-store/) et suivre les étapes décrites pour déployer l'environnement de l'atelier dans votre compte AWS. Un compte AWS est nécessaire pour effectuer l'atelier et exécuter le code d'intégration.

## Architecture d'intégration

Avant de configurer Braze pour envoyer des messages personnalisés aux utilisateurs, passez en revue les composants pertinents requis pour un site web de commerce électronique typique, en utilisant l’architecture du Retail Demo Store comme exemple.

![Une image décomposant l'architecture de personnalisation de Braze et montrant comment les différents composants interagissent les uns avec les autres.]({% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}){: style="max-width:70%" }

1. L'interface utilisateur web de Retail Demo Store utilise la bibliothèque JavaScript AWS Amplify pour envoyer des événements de formation à Amazon Personalize.
2. Les enregistrements des utilisateurs de la campagne Braze sont mis à jour à partir du service Global Store User.
3. Lorsqu'une campagne Braze s'exécute, un modèle de contenu connecté est utilisé pour récupérer des recommandations de Personalize et remplir un modèle d'e-mail pour un utilisateur ciblé.
4. Les informations du catalogue de produits peuvent également être utilisées pour former des modèles de recommandation.

Braze enverra des e-mails à vos utilisateurs en fonction de leur comportement ou des attributs de leur profil utilisateur. Ces données peuvent aider à identifier les utilisateurs et à créer des profils utilisateurs pour déterminer quand envoyer un message ou un e-mail.

Ce flux de données d'événement se produira en parallèle des données comportementales d'événement envoyées à Amazon Personalize. Dans cet atelier, la boutique de démonstration utilise Amplify pour envoyer des événements à Personalize. Ces données sont utilisées pour former un modèle de recommandations qui peut ensuite être utilisé dans les appels de contenu connecté de Braze pour personnaliser le contenu aux utilisateurs lors de l'exécution de votre campagne Braze.

Le contenu connecté de Braze pourra obtenir ces recommandations via un service de recommandation fonctionnant dans AWS. L'atelier "Boutique de démonstration" présente un exemple de déploiement d'un service de recommandation. Dans un scénario de déploiement dans votre propre infrastructure, vous devrez déployer un service similaire pour obtenir des éléments de votre propre service de catalogue.

## Mise en place de l'atelier sur l'architecture de référence

### Étape 1 : Déployez la boutique de démonstration de vente au détail sur votre compte AWS.

![Une image des régions AWS disponibles.][2]{: style="float:right;max-width:40%;margin-top:15px;margin-bottom:10px;"}

Dans le tableau suivant, choisissez une **région AWS** et sélectionnez **Lancer Stack**. Cette liste ne contient pas toutes les régions où vous pouvez déployer le projet, mais seulement les régions actuellement configurées pour un déploiement avec la boutique de démonstration.

Accepter toutes les valeurs des paramètres par défaut du modèle. Le déploiement de toutes les ressources du projet devrait prendre de 25 à 30 minutes.

### Étape 2 : Créer des campagnes Amazon Personalize

Avant de pouvoir fournir des recommandations de produits personnalisées, vous devez d'abord former les modèles de machine learning et fournir des endpoints d'inférence qui vous permettront d'obtenir des recommandations d'Amazon Personalize. Le modèle CloudFormation déployé à l'étape 1 inclut une instance de bloc-notes Amazon SageMaker qui fournit un bloc-notes Jupyter avec des instructions détaillées.

1. Connectez-vous au compte AWS dans lequel vous avez déployé le modèle AWS CloudFormation à l'étape 1.
2. Dans la console Amazon SageMaker, choisissez **Instances de bloc-notes**.
3. Si vous ne voyez pas l'instance de bloc-notes **RetailDemoStore**, assurez-vous que vous êtes dans la même région que celle où vous avez déployé le projet à l'étape 1.
4. Pour accéder à l'instance de bloc-notes, choisissez **Ouvrir Jupyter** ou **Ouvrir JupyterLab**.
5. Une fois l'interface web Jupyter chargée pour l'instance de bloc-notes, choisissez le `workshop/1-Personalization/1.1-Personalize.ipynb`bloc-notes. Il se peut que vous deviez choisir le dossier `workshop` pour voir les sous-répertoires du bloc-notes.
6. Une fois le bloc-notes `1.1-Personalize` ouvert, parcourez l'atelier en exécutant chaque cellule. Vous pouvez choisir **Exécuter** dans la barre d'outils Jupyter pour exécuter séquentiellement le code dans les cellules. Deux heures environ sont nécessaires pour effectuer cet atelier.

### Étape 3 : Envoyez des e-mails personnalisés depuis Braze

Une fois les solutions et les campagnes Amazon Personalize en place, votre instance de la boutique de démonstration Retailing est prête à fournir des recommandations à vos campagnes d'e-mail. À l'étape 1, vous avez déployé l'application Web de démonstration et tous les services associés, y compris le service de recommandation nécessaire à l'intégration de vos campagnes d'e-mail à Braze via Connected Content, qui utilise les campagnes Amazon Personalize que vous avez déployées à l'étape 2.

À l'instar de l'atelier sur la personnalisation de l'étape 2, l'atelier suivant sur l'envoi de messages par Braze vous guide dans la configuration de l'intégration de Braze et d'Amazon Personalize.

1. Connectez-vous au compte AWS dans lequel vous avez déployé le modèle AWS CloudFormation à l'étape 1.
2. Dans la console Amazon SageMaker, choisissez **Instances de bloc-notes**.
3. Si vous ne voyez pas l'instance de bloc-notes **RetailDemoStore**, assurez-vous que vous vous trouvez dans la même région AWS que celle où vous avez déployé le projet.
4. Pour accéder à l'instance de bloc-notes, choisissez **Ouvrir Jupyter** ou **Ouvrir JupyterLab**.
5. Une fois l'interface web Jupyter chargée pour l'instance de bloc-notes, choisissez le `workshop/4-Messaging/4.2-Braze.ipynb`bloc-notes. Il se peut que vous deviez choisir le dossier `workshop` pour voir les sous-répertoires du bloc-notes.
6. Une fois le bloc-notes `4.2-Braze` ouvert, parcourez l'atelier en exécutant chaque cellule. Vous pouvez choisir **Exécuter** dans la barre d'outils Jupyter pour exécuter séquentiellement le code dans les cellules. La création du bloc-notes dure environ une heure.

### Étape 4 : Nettoyer les ressources

Pour éviter d'encourir des frais à l'avenir, supprimez les ressources AWS que le projet Retail Demo Store a créées en supprimant la pile AWS CloudFormation que vous avez créée à l'étape 1.


[1]: {% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}
[2]: {% image_buster /assets/img/amazon_personalize/region.png %}