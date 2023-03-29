---
nav_title: Tinyclues
article_title: Tinyclues
alias: /partners/tinyclues/
description: "Cet article de référence présente le partenariat entre Braze et Tinyclues, qui offre une fonctionnalité de développement d’audiences pour vous aider à envoyer davantage de campagnes de ciblage, à trouver de nouvelles opportunités de produits et à augmenter vos revenus en utilisant une interface utilisateur incroyablement conviviale."
page_type: partner
search_tag: Partenaire

---

# Tinyclues

> [Tinyclues](https://www.tinyclues.com/) est une fonctionnalité de développement d’audiences qui vous permet de lancer davantage de campagnes et d’augmenter vos revenus sans nuire à l’expérience client. De plus, Tinyclues propose également des analyses pour suivre le rendement de vos campagnes CRM en ligne et hors ligne.

L’intégration de Braze et de Tinyclues permet aux utilisateurs d’améliorer leur stratégie CRM et la planification des campagnes CRM pour envoyer davantage de campagnes ciblées, trouver de nouvelles opportunités de produits et augmenter leurs revenus à l’aide d’une interface utilisateur incroyablement conviviale.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Tinyclues | Un compte Tinyclues est nécessaire pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration de l’importation de données

Pour intégrer Braze et Tinyclues, vous devez configurer la plateforme Tinyclues, exporter une campagne Tinyclues existante et créer un segment de cohorte d’utilisateurs dans Braze qui peut être utilisé pour cibler des utilisateurs dans de futures campagnes.

### Étape 1 : Obtenir la clé d’importation des données Braze

Dans Braze, accédez à **Technology Partners (Partenaires technologiques)** et sélectionnez **Tinyclues**. Ici, vous trouverez votre endpoint REST et pourrez générer votre clé d’importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante.<br><br>![][6]{: style="max-width:90%;"} 

Pour terminer l’intégration, vous devrez fournir la clé d’importation des données et l’endpoint REST à votre équipe d’opérations de données Tinyclues. Tinyclues établira ensuite la connexion et vous contactera une fois la configuration terminée.

### Étape 2 : Exporter une campagne à partir de la plateforme Tinyclues

Chaque fois que vous souhaitez créer une cohorte d’utilisateurs Tinyclues pour l’utiliser dans Braze, vous devrez d’abord l’exporter depuis la plateforme Tinyclues.

Dans Tinyclues, sélectionnez la ou les campagnes à exporter et cliquez sur **Export Campaigns (Exporter des campagnes)**. L’audience sera automatiquement téléchargée sur votre compte Braze lors de l’exportation.

![][1]

### Étape 3 : Créer un segment à partir d’une audience personnalisée Tinyclues

Dans Braze, accédez à **Segments**, nommez votre segment de cohorte Tinyclues et sélectionnez **Tinyclues Cohorts (Cohortes Tinyclues)** comme filtre. Choisissez maintenant la cohorte Tinyclues que vous souhaitez inclure. Une fois créé, vous pouvez sélectionner votre segment de cohorte Tinyclues comme filtre d’audience au moment de créer une campagne ou un Canvas.

![][3]{: style="max-width:90%;"}<br><br>
![Dans le générateur de segments de Braze, le filtre des attributs utilisateur « Tinyclues Cohort (Cohorte Tinyclues) » est défini sur « includes (inclut) » et « Primary cohort (Cohorte principale) ».][4]{: style="max-width:90%;"}

Vous avez du mal à trouver votre cohorte ? Consultez notre section [résolution des problèmes](#troubleshooting) pour obtenir des conseils. 

## Comment utiliser cette intégration

Pour utiliser votre segment Tinyclues, créez une campagne ou un Canvas Braze et sélectionnez le segment comme audience cible. 

![Dans le générateur de campagne Braze, à l’étape du ciblage, le filtre « Target users by segment (Cibler les utilisateurs par segment) » est défini sur « Tinyclues cohort (Cohorte Tinyclues) ».][5]{: style="max-width:90%;"}

## Résolution des problèmes

Vous avez des difficultés à trouver la bonne cohorte dans la liste ? Dans Tinyclues, consultez les détails de votre campagne et vérifiez le nom de votre cohorte en cochant la case **Export File Name (Exporter le nom du fichier)**.

![Le bas de la page des détails de la campagne affiche le nom de votre cohorte.][2]{: style="max-width:30%;"}

Vous avez toujours du mal à récupérer votre audience ? Contactez l’[équipe de Tinyclues](mailto:support@tinyclues.com) pour obtenir de l’aide.

[1]: {% image_buster /assets/img/tinyclues/tinyclues_1.png %} 
[2]: {% image_buster /assets/img/tinyclues/tinyclues_2.png %} 
[3]: {% image_buster /assets/img/tinyclues/tinyclues_3.png %} 
[4]: {% image_buster /assets/img/tinyclues/tinyclues_4.png %}
[5]: {% image_buster /assets/img/tinyclues/tinyclues_5.png %}  
[6]: {% image_buster /assets/img/tinyclues/tinyclues_6.png %}  