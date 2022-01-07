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

L'intégration de Braze et de Tinyclues offre aux utilisateurs une voie vers une meilleure planification et stratégie de CRM permettant aux utilisateurs d'envoyer des campagnes plus ciblées, de trouver de nouvelles opportunités de produits et d'augmenter leurs revenus à l'aide d'une interface utilisateur incroyablement conviviale.

## Pré-requis

| Exigences        | Libellé                                                         |
| ---------------- | --------------------------------------------------------------- |
| Compte Tinyclues | Un compte Tinyclues est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Pour intégrer Braze et Tinyclues, vous devez configurer la plate-forme Tinyclues, exporter une campagne existante de Tinyclues, et créer un segment de cohorte utilisateur à Braze qui peut être utilisé pour cibler les utilisateurs dans de futures campagnes.

### Étape 1 : Récupère la clé d'importation de données Braze

Au Brésil, accédez aux **partenaires technologiques** et sélectionnez **Tinyclues**. Ici, vous trouverez votre point de terminaison REST et générez votre clé d'importation de données Braze. Une fois généré, vous pouvez créer une nouvelle clé ou invalider une clé existante.<br><br>!\[Tinyclues\]\[6\]{: style="max-width:90%;"}

Pour compléter l'intégration, vous devrez fournir la clé d'importation de données et le point de terminaison REST à votre équipe d'opérations de données Tinyclues. Tinyclues établira ensuite la connexion et vous contactera une fois la configuration terminée.

### Étape 2 : Exporter une campagne depuis la plateforme Tinyclues

Chaque fois que vous voulez créer une cohorte d'utilisateurs Tinyclues à utiliser en Brésil, vous devrez d'abord l'exporter depuis la plateforme Tinyclues.

Dans les Tinyclues, sélectionnez la/les campagne(s) que vous souhaitez exporter et cliquez sur **Exporter les campagnes**. Lors de l'exportation, l'audience sera automatiquement téléchargée sur votre compte Braze.

!\[Tableau de bord de Tinyclues\]\[1\]

### Étape 3 : Créez un segment à partir du public personnalisé de Tinyclues

Au Brésil, accédez à **Segments**, nommez votre segment de cohorte Tinyclues et sélectionnez **Tinyclues Cohorts** comme filtre. De là, vous pouvez choisir quelle cohorte Tinyclues vous souhaitez inclure. Une fois créé, vous pouvez sélectionner votre segment de cohorte Tinyclues comme filtre d’audience lors de la création d’une campagne ou d’un Canvas.

!\[Tinyclues create segement\]\[3\]{: style="max-width:90%;"}<br><br> !\[Tinyclues select cohort\]\[4\]{: style="max-width:90%;"}

Vous avez des difficultés à localiser votre cohorte? Consultez notre section [dépannage](#troubleshooting) pour obtenir des conseils.

## Utiliser cette intégration

Pour utiliser votre segment Tinyclues, créez une campagne Braze ou Canvas et sélectionnez le segment comme public cible.

!\[Public Tinyclues\]\[5\]{: style="max-width:90%;"}

## Dépannage

Avez-vous de la difficulté à trouver la bonne cohorte dans la liste? Dans Tinyclues, consultez les détails de votre campagne et vérifiez le nom en vérifiant le **Nom du fichier d'exportation**.

!\[Tinyclues troubleshooting\]\[2\]{: style="max-width:30%;"}

Vous rencontrez toujours des difficultés à récupérer votre audience? Contactez l'équipe [Tinyclues](mailto:support@tinyclues.com) pour un support supplémentaire.
[1]: {% image_buster /assets/img/tinyclues/tinyclues_1.png %} [2]: {% image_buster /assets/img/tinyclues/tinyclues_2.png %} [3]: {% image_buster /assets/img/tinyclues/tinyclues_3. ng %} [4]: {% image_buster /assets/img/tinyclues/tinyclues_4.png %} [5]: {% image_buster /assets/img/tinyclues/tinyclues_5. ng %} [6]: {% image_buster /assets/img/tinyclues/tinyclues_6.png %}  