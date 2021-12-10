---
nav_title: Atelier
article_title: Atelier de personnalisation d'Amazon
alias: /fr_FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/FR/
description: "Cet article décrit le processus de configuration de la Personnalisation d'Amazon et de son intégration dans votre environnement Braze en utilisant le Contenu Connecté."
page_type: partenaire
search_tag: Partenaire
---

# Atelier de personnalisation Amazon

> Cet article vous guidera à travers le processus de configuration de la Personnalisation d'Amazon et de son intégration dans votre environnement Braze en utilisant le Contenu Connecté. Cela se fait à l'aide d'un atelier pratique qui vous guidera à travers toutes les étapes nécessaires pour déployer et former des solutions de personnalisation Amazon et les intégrer dans une campagne d'email de Braze.

Les exemples suivants sont déployés dans un exemple pleinement fonctionnel de site de commerce électronique appelé le magasin de démonstration de détail. Les ressources et le code de ce tutoriel sont publiés dans la boutique de démo [AWS Samples Retail Demo Store](https://github.com/aws-samples/retail-demo-store/). Vous pouvez utiliser cette implémentation d'architecture de référence comme un contour pour implémenter Amazon Personalize dans votre propre environnement.

## Exigences

Vous devrez cloner le [dépôt de magasin de démonstration de détail](https://github.com/aws-samples/retail-demo-store/) et suivre les étapes décrites ci-dessous pour déployer l'environnement d'atelier sur votre compte AWS. Un compte AWS est requis pour compléter l'atelier et exécuter le code d'intégration.

## Architecture d'intégration

Avant de configurer Braze pour envoyer des messages personnalisés aux utilisateurs, examiner les composants pertinents requis pour un site Web de commerce électronique typique, en utilisant l'architecture de la boutique de démonstration de détail comme exemple.

![Architecture de personnalisation de Braze]({% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}){: style="largeur-max-70%" }

1. L'interface web de la boutique de démonstration de détail utilise la bibliothèque JavaScript AWS pour envoyer des événements de formation à Amazon Personalize.
2. Les enregistrements des utilisateurs de campagne de Braze sont mis à jour à partir du service utilisateur de la boutique mondiale.
3. Lorsqu'une campagne Braze s'exécute, un modèle de contenu connecté est utilisé pour récupérer les recommandations de Personnaliser et remplir un modèle d'e-mail pour un utilisateur cible.
4. Des informations sur le catalogue de produits peuvent également être utilisées pour former des modèles de recommandations.

Braze enverra des courriels à vos utilisateurs en fonction de leur comportement ou de leurs attributs de profils. Ces données peuvent aider à identifier les utilisateurs et à construire des profils d'utilisateurs pour aider à déterminer quand envoyer un message ou un courriel.

Ce flux de données d'événement se produira en parallèle aux données d'événement comportemental envoyées à Amazon Personalize. Dans cet atelier, la boutique de démonstration utilise Amplify pour envoyer des événements à Personnaliser. Ces données sont utilisées pour former un modèle de recommandations qui peut ensuite être utilisé dans les appels de contenu connecté de Braze pour personnaliser le contenu aux utilisateurs lors de l'exécution de votre campagne Braze.

Braze Connected Content sera en mesure d'obtenir ces recommandations grâce à un service de recommandation fonctionnant dans AWS. L'atelier du magasin de démonstration de détail montre un exemple de déploiement du service de recommandation. Dans un scénario de déploiement dans votre propre infrastructure, vous devrez déployer un service similaire pour obtenir des articles de votre propre service de catalogue.

## Mise en place de l'atelier d'architecture de référence

### Étape 1 : Déployez la boutique de démo de détail sur votre compte AWS

!\[Choose AWS Region\]\[2\]{: style="float:right;max-width:40%;margin-top:15px;margin-bottom:10px;"}

Dans le tableau suivant, choisissez une **région AWS** et sélectionnez **pile de lancement**. Cette liste ne représente pas toutes les régions possibles où vous pouvez déployer le projet, seulement les régions actuellement configurées pour le déploiement avec la boutique de démonstration de détail.

Accepter toutes les valeurs de paramètre par défaut pour le template. Le déploiement de toutes les ressources du projet devrait prendre 25 à 30 minutes.

### Étape 2 : Construire des campagnes de personnalisation Amazon

Avant de pouvoir fournir des recommandations de produits personnalisées, vous devez d'abord former les modèles d'apprentissage automatique et fournir des points de terminaison d'inférence qui vous permettront d'obtenir des recommandations de la Personnalisation d'Amazon. Le modèle CloudFormation déployé à l'étape 1 inclut une instance de bloc-notes Amazon SageMaker qui fournit un bloc-notes Jupyter avec des instructions détaillées étape par étape.

1. Connectez-vous au compte AWS où vous avez déployé le modèle AWS CloudFormation à l'étape 1.
2. Sur la console Amazon SageMaker, choisissez __Instances Notebook__.
3. Si vous ne voyez pas l'instance de bloc-notes **RetailDemoStore** . assurez-vous que vous êtes dans la même région où vous avez déployé le projet à l'étape 1.
4. Pour accéder à l'instance de bloc-notes, choisissez **Open Jupyter** ou **Open JupyterLab**.
5. Quand l'interface web de Jupyter est chargée pour l'instance de bloc-notes, choisissez le bloc-notes `workshop/1-Personalization/1.1-Personalize.ipynb`. Vous devrez peut-être choisir le dossier `atelier` pour voir les sous-répertoires du bloc-notes.
6. Une fois que vous avez le bloc-notes `1.1-` ouvert, passez à travers l'atelier en exécutant chaque cellule. Vous pouvez choisir **Exécuter** depuis la barre d'outils Jupyter pour exécuter le code séquentiellement dans les cellules. Le bloc-notes prend environ deux heures.

### Étape 3 : Envoyez des e-mails personnalisés depuis Braze

Avec les solutions et les campagnes de personnalisation d'Amazon, votre instance du magasin de démo de détail est prête à fournir des recommandations à vos campagnes de messagerie. À l'étape 1, vous avez déployé l'application web de démonstration et tous les services associés, y compris le service de recommandation nécessaire pour intégrer vos campagnes de messagerie avec Braze à travers le contenu connecté, qui utilise les campagnes de personnalisation d'Amazon que vous avez déployées à l'étape 2.

Similaire à l'atelier de personnalisation à l'étape 2, l'atelier de messagerie Braze suivant vous permet de mettre en place l'intégration de la personnalisation de Braze et Amazon.

1. Connectez-vous au compte AWS où vous avez déployé le modèle AWS CloudFormation à l'étape 1.
2. Sur la console Amazon SageMaker, choisissez **Bloc-notes Instances**.
3. Si vous ne voyez pas l'instance de bloc-notes **RetailDemoStore** , assurez-vous que vous êtes dans la même région AWS où vous avez déployé le projet.
4. Pour accéder à l'instance de bloc-notes, choisissez **Open Jupyter** ou **Open JupyterLab**.
5. Quand l'interface web de Jupyter est chargée pour l'instance de bloc-notes, choisissez le bloc-notes `Workshop/4-Messaging/4.2-Braze.ipynb`. Vous devrez peut-être choisir le dossier `atelier` pour voir les sous-répertoires du bloc-notes.
6. Lorsque vous avez le bloc-notes `4.2-Braze` ouvert, passez à travers l'atelier en exécutant chaque cellule. Vous pouvez choisir **Exécuter** depuis la barre d'outils Jupyter pour exécuter le code séquentiellement dans les cellules. Le bloc-notes prend environ 1 heure à compléter.

### Étape 4 : Nettoyer les ressources

Pour éviter d'engendrer des frais futurs, supprimer les ressources AWS du projet de magasin de démo de détail créé en supprimant la pile AWS CloudFormation que vous avez créée à l'étape 1.
[1]: {% image_buster /assets/img/文_personalize/braze-personalize-arch.png %} [2]: {% image_buster /assets/img/文_personalize/region.png %}