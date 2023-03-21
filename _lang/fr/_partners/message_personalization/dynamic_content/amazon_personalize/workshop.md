---
nav_title: Atelier
article_title: Atelier Amazon Personalize
alias: /partners/amazon_personalize_workshop/
description: "Cet article de référence décrit le processus de configuration d’Amazon Personalize et son intégration dans votre environnement Braze à l’aide du Contenu connecté."
page_type: partner
search_tag: Partenaire
---

# Atelier Amazon Personalize

> Cet article de référence décrit les étapes du processus de configuration d’Amazon Personalize et son intégration dans votre environnement Braze à l’aide du Contenu connecté. Cela est fait à l’aide d’un atelier pratique qui vous guidera dans toutes les étapes nécessaires au déploiement et au développement des solutions Amazon Personalize et à leur intégration dans une campagne d’e-mail Braze.

Les exemples suivants sont déployés dans un exemple de site de commerce électronique entièrement fonctionnel appelé Retail Demo Store (Boutique démo). Les ressources et le code de ce didacticiel sont publiés dans le document [AWS Samples Retail Demo Store](https://github.com/aws-samples/retail-demo-store/). Vous pouvez utiliser cette mise en œuvre de l’architecture de référence comme un schéma pour mettre en œuvre Amazon Personalize dans votre propre environnement.

## Conditions

Vous devrez cloner le [Référentiel Retail Demo Store](https://github.com/aws-samples/retail-demo-store/) et suivre les étapes décrites pour déployer l’environnement de l’atelier sur votre compte AWS. Un compte AWS est nécessaire pour terminer l’atelier et exécuter le code d’intégration.

## Architecture d’intégration

Avant de configurer Braze pour envoyer des messages personnalisés aux utilisateurs, passez en revue les composants pertinents requis pour un site web de commerce électronique typique, en utilisant l’architecture du Retail Demo Store comme exemple.

![Détails de l’architecture de personnalisation Braze avec les interactions des différents composants.]({% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}){: style="max-width:70%" }

1. L’IU Web du Retail Demo Store utilise la bibliothèque AWS Amplify JavaScript pour envoyer des événements de formation à Amazon Personalize.
2. Les enregistrements des utilisateurs de la campagne Braze sont mis à jour à partir du service Global Store User.
3. Lorsqu’une campagne Braze est lancée, un modèle de Contenu connecté est utilisé pour récupérer des recommandations de Personalize et remplir un modèle d’e-mail pour un utilisateur cible.
4. Les informations sur le catalogue des produits peuvent également être utilisées pour former les modèles de recommandation.

Braze enverra des e-mails à vos utilisateurs en fonction de leur comportement ou des attributs de leurs profils d’utilisateurs. Ces données peuvent aider à identifier les utilisateurs et à créer des profils d’utilisateur pour déterminer quand envoyer un message ou un e-mail.

Ce flux de données d’événement se produira en parallèle aux données d’événement comportemental envoyées à Amazon Personalize. Dans cet atelier, la boutique de démonstration utilise Amplify pour envoyer des événements à Personalize. Ces données sont utilisées pour former un modèle de recommandations qui peut ensuite être utilisé dans les appels de Contenu connecté de Braze pour personnaliser le contenu pour les utilisateurs lorsque votre campagne Braze est lancée.

Le Contenu connecté de Braze sera en mesure d’obtenir ces recommandations via un service de recommandation exécuté dans AWS. L’atelier Retail Demo Store montre un exemple de déploiement de service de recommandation. Dans un scénario de déploiement dans votre propre infrastructure, vous devrez déployer un service similaire pour obtenir des articles de votre propre service de catalogue.

## Configuration de l’atelier d’architecture de référence

### Étape 1 : Déployer l’architecture Retail Demo Store dans votre compte AWS

![Image des régions AWS disponibles.][2]{: style="float:right;max-width:40%;margin-top:15px;margin-bottom:10px;"}

Dans le tableau suivant, choisissez une **région AWS** et sélectionnez **Launch Stack (Lancer la pile)**. Cette liste ne représente pas toutes les régions possibles où vous pouvez déployer le projet, mais seules les régions actuellement configurées pour le déploiement avec le Retail Demo Store.

Acceptez toutes les valeurs par défaut des paramètres du modèle. Le déploiement de toutes les ressources du projet devrait prendre 25 à 30 minutes.

### Étape 2 : Créer des campagnes Amazon Personalize

Avant de pouvoir fournir des recommandations produit personnalisées, vous devez d’abord former les modèles de machine learning et fournir des endpoints d’inférence qui vous permettront d’obtenir des recommandations d’Amazon Personalize. Le modèle CloudFormation déployé à l’étape 1 comprend une instance de notebook Amazon SageMaker qui fournit un document Jupyter avec des instructions détaillées étape par étape.

1. Connectez-vous au compte AWS où vous avez déployé le modèle AWS CloudFormation à l’étape 1.
2. Dans la console Amazon SageMaker, choisissez **Notebook instances (Instances de notebook)**.
3. Si vous ne voyez pas l’instance de notebook **RetailDemoStore**, assurez-vous que vous êtes dans la même région où vous avez déployé le projet à l’étape 1.
4. Pour accéder à l’instance du notebook, choisissez **Open Jupyter (Ouvrir Jupyter)** ou **Open JupyterLab (Ouvrir JupyterLab)** .
5. Lorsque l’interface Web Jupyter a été chargée pour l’instance du notebook, choisissez le notebook `workshop/1-Personalization/1.1-Personalize.ipynb`. Il se peut que vous deviez choisir le dossier `workshop` pour afficher les sous-répertoires du notebook.
6. Une fois que vous avez ouvert le notebook `1.1-Personalize`, poursuivez l’atelier en exécutant chaque cellule. Vous pouvez choisir **Run (Exécuter)** dans la barre d’outils de Jupyter pour exécuter séquentiellement le code dans les cellules. Le notebook requiert environ deux heures pour être complété.

### Étape 3 : Envoyer des e-mails personnalisés depuis Braze

Grâce aux solutions et aux campagnes Amazon Personalize mises en place, votre instance du Retail Demo Store est prête à fournir des recommandations à vos campagnes d’e-mail. À l’étape 1, vous avez déployé l’application Web de démonstration et tous les services associés, y compris le service de recommandation nécessaire pour intégrer vos campagnes d’e-mail à Braze via le Contenu connecté, qui utilise les campagnes Amazon Personalize que vous avez déployées à l’étape 2.

Tout comme l’atelier sur la personnalisation de l’étape 2, l’atelier suivant sur la messagerie Braze vous guide dans la mise en place de l’intégration Braze et Amazon Personalize.

1. Connectez-vous au compte AWS où vous avez déployé le modèle AWS CloudFormation à l’étape 1.
2. Dans la console Amazon SageMaker, choisissez **Notebook instances (Instances de notebook)**.
3. Si vous ne voyez pas l’instance de notebook **RetailDemoStore**, assurez-vous que vous êtes dans la même région AWS où vous avez déployé le projet.
4. Pour accéder à l’instance du notebook, choisissez **Open Jupyter (Ouvrir Jupyter)** ou **Open JupyterLab (Ouvrir JupyterLab)** .
5. Lorsque l’interface Web Jupyter a été chargée pour l’instance du notebook, choisissez le notebook `workshop/4-Messaging/4.2-Braze.ipynb`. Il se peut que vous deviez choisir le dossier `workshop` pour afficher les sous-répertoires du notebook.
6. Quand vous avez le notebook `4.2-Braze` d’ouvert, poursuivez l’atelier en exécutant chaque cellule. Vous pouvez choisir **Run (Exécuter)** dans la barre d’outils de Jupyter pour exécuter séquentiellement le code dans les cellules. Le notebook requiert environ 1 heure pour être complété.

### Étape 4 : Nettoyer les ressources

Pour éviter d’engager des frais futurs, supprimez le projet Retail Demo Store créé des ressources AWS en supprimant la pile AWS CloudFormation que vous avez créée à l’étape 1.

[1]: {% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}
[2]: {% image_buster /assets/img/amazon_personalize/region.png %}