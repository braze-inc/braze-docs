---
nav_title: Tinyindices
article_title: Tinyindices
alias: /fr/partners/tinyclues/
description: "Cet article décrit le partenariat entre Braze et Tinyclues, qui offre une fonctionnalité de création du public pour vous aider à envoyer des campagnes plus ciblées, trouver de nouvelles opportunités de produits et augmenter les revenus grâce à une interface utilisateur incroyablement conviviale."
page_type: partenaire
search_tag: Partenaire
---

# Tinyindices

> [Tinyclues](https://www.tinyclues.com/) est une fonctionnalité de création d'audience qui offre la capacité d'augmenter le nombre de campagnes et de revenus sans nuire à l'expérience client et à l'analyse pour suivre les performances des campagnes CRM en ligne et hors ligne.

Ensemble, l’intégration de Braze et Tinyclues offre aux utilisateurs une voie vers une meilleure planification et une meilleure stratégie de CRM permettant aux utilisateurs d'envoyer plus de campagnes de ciblage, de trouver de nouvelles opportunités de produits et d'augmenter leurs revenus à l'aide d'une interface utilisateur incroyablement conviviale.

## Aperçu

Pour intégrer Braze et Tinyclues, vous devez exporter une campagne Tinyclues existante et créer un segment de cohorte utilisateur dans la plateforme Braze pour filtrer les futures campagnes.

1. Configurez la plate-forme Tinyclues avec les paramètres appropriés.
2. Chaque fois qu'une campagne est exécutée sur Tinyclues Action, le public associé est automatiquement repoussé au Brésil.
3. À partir de la plate-forme Braze, créez un segment des utilisateurs de la campagne Tinyclues.
3. Créez une campagne Braze et utilisez l'option de filtrage dédié pour cibler votre segment de cohorte Tinyclues.

## Exigences d'intégration

Vous devez avoir accès aux éléments suivants :
- Un compte actif de Tinyclues.
- Un compte de Braze actif avec la possibilité d'utiliser l'intégration de Tinyclues.
- La clé API correspondant à l'intégration de Tincylues doit être communiquée à votre représentant de Tinyclues Data Operation pour mettre en place l'intégration.

## Processus d'implémentation

### Étape 1 : Récupère la clé d'importation de données Braze
Dans votre compte Braze, accédez aux **partenaires technologiques** et sélectionnez **Tinyclues**. Ici, vous trouverez votre point de terminaison REST et générez votre clé d'importation de données Braze.

!\[Tinyclues\]\[6\]{: style="max-width:70%;"}

### Étape 2 : Partager la clé API avec les opérations de données Tinyclues

Vous devrez fournir la clé d'importation de données et votre point de terminaison REST à l'équipe des opérations de données Tinyclues pour que l'intégration soit complète. Tinyclues établira ensuite la connexion et vous contactera une fois la configuration terminée.

### Étape 3 : Exporter une campagne depuis la plateforme Tinyclues

Chaque fois que vous voulez créer une cohorte d'utilisateurs Tinyclues à utiliser en Brésil, vous devrez d'abord l'exporter depuis la plateforme Tinyclues.

Dans les Tinyclues, sélectionnez la/les campagne(s) que vous souhaitez exporter et cliquez sur __Exporter les campagnes__.

!\[Tinyclues\]\[1\]

Lors de l'exportation, l'audience sera automatiquement téléchargée sur votre compte Braze.

### Étape 4 : Utilisez les Tinyindices personnalisés à Braze

Ensuite, sur la plate-forme Braze, accédez à __Segments__, nommez votre segment de cohorte Tinyclues et sélectionnez __Tinyclues Cohorts__ comme filtre. De là, vous pouvez choisir quelle cohorte Tinyclues vous souhaitez inclure. Une fois créé, vous pourrez sélectionner votre segment de cohorte Tinyclues comme filtre d’audience lors de la création d’une campagne ou d’un Canvas.

Vous avez des difficultés à localiser votre cohorte? Consultez notre section [dépannage](#troubleshooting) pour obtenir des conseils.

!\[Tinyclues\]\[3\]{: style="max-width:70%;"}<br><br> !\[Tinyclues\]\[4\]{: style="max-width:70%;"}

### Étape 5 : Récupérez votre audience à Braze

Sur la plate-forme de Braze, créez une campagne ou Canvas. Pour l'étape cible du public, sélectionnez le segment de cohorte Tinyclues que vous venez de construire.

!\[Tinyclues\]\[5\]{: style="max-width:80%;"}

## Dépannage

Avez-vous de la difficulté à trouver la bonne cohorte dans la liste? Vérifiez le nom dans l'interface utilisateur des Tinyclues en cliquant sur la campagne et en vérifiant le **Nom du fichier d'exportation**.

!\[Tinyclues\]\[2\]{: style="max-width:30%;"}

Vous rencontrez toujours des difficultés à récupérer votre audience? Contactez l'équipe de Tinyclues pour obtenir un support supplémentaire : [support@tinyclues.com](mailto:support@tinyclues.com).
[1]: {% image_buster /assets/img/tinyclues/tinyclues_1.png %} [2]: {% image_buster /assets/img/tinyclues/tinyclues_2.png %} [3]: {% image_buster /assets/img/tinyclues/tinyclues_3. ng %} [4]: {% image_buster /assets/img/tinyclues/tinyclues_4.png %} [5]: {% image_buster /assets/img/tinyclues/tinyclues_5. ng %} [6]: {% image_buster /assets/img/tinyclues/tinyclues_6.png %}  
