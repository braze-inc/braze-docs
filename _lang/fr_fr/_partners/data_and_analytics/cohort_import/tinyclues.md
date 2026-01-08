---
nav_title: Tinyclues
article_title: Tinyclues
alias: /partners/tinyclues/
description: "Cet article de référence présente le partenariat entre Braze et Tinyclues, qui propose une fonctionnalité de création d'audience pour vous aider à envoyer des campagnes de ciblage plus nombreuses, à trouver de nouvelles opportunités de produits et à élever le chiffre d'affaires à l'aide d'une interface utilisateur incroyablement conviviale."
page_type: partner
search_tag: Partner

---

# Tinyclues

> [Tinyclues](https://www.tinyclues.com/) est une fonctionnalité de création d'audience qui offre la possibilité d'augmenter le nombre de campagnes et le chiffre d'affaires sans nuire à l'expérience client et à l'analyse/analytique pour suivre les performances des campagnes CRM en ligne et hors ligne.

L'intégration de Braze et Tinyclues offre aux utilisateurs un chemin vers une meilleure planification et stratégie CRM, permettant aux utilisateurs d'envoyer des campagnes plus ciblées, de trouver de nouvelles opportunités de produits, et d'élever le chiffre d'affaires en utilisant une interface utilisateur incroyablement conviviale.

## Prérequis

| Condition | Descriptif |
|---|---|
| Compte Tinyclues | Un compte Tinyclues est nécessaire pour bénéficier de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration de données

Pour intégrer Braze et Tinyclues, vous devez configurer la plateforme Tinyclues, exporter une campagne Tinyclues existante et créer un segment de cohorte d'utilisateurs dans Braze qui pourra être utilisé pour cibler les utilisateurs dans les campagnes futures.

### Étape 1 : Obtenir la clé d'importation des données de Braze

Dans Braze, naviguez vers **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Tinyclues**. 

Ici, vous trouverez votre endpoint REST et générerez la clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante.<br><br>![]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"} 

Pour terminer l'intégration, vous devrez fournir la clé d'importation des données et l'endpoint REST à votre équipe d'exploitation des données de Tinyclues. Tinyclues établira alors la connexion et vous contactera une fois la configuration terminée.

### Étape 2 : Exporter une campagne depuis la plateforme Tinyclues

Chaque fois que vous voudrez créer une cohorte d'utilisateurs de Tinyclues pour l'utiliser dans Braze, vous devrez d'abord l'exporter depuis la plateforme Tinyclues.

Dans Tinyclues, sélectionnez la ou les campagnes que vous souhaitez exporter et cliquez sur **Exporter les campagnes.** Lors de l'exportation, l'audience sera automatiquement téléchargée sur votre compte Braze.

![]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### Étape 3 : Créez un segment à partir de l'audience personnalisée de Tinyclues.

Dans Braze, naviguez vers **Segments**, nommez votre segment de cohorte Tinyclues et sélectionnez **Cohortes Tinyclues** comme filtre. À partir de là, vous pouvez choisir la cohorte Tinyclues que vous souhaitez inclure. Une fois votre segment de cohorte Tinyclues créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une campagne ou d'un Canvas.

![]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![Dans le générateur de segments de Braze, le filtre d'attributs utilisateur "cohorte Tinyclues" est défini sur "inclut" et "cohorte primaire".]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

Vous avez des difficultés à localiser votre cohorte ? Consultez notre section [résolution des problèmes](#troubleshooting) pour obtenir des conseils. 

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze pourront être ajoutés ou supprimés d'une cohorte. L'importation d'une cohorte ne créera pas de nouveaux utilisateurs dans Braze.
{% endalert %}

## Utilisation de cette intégration

Pour utiliser votre segment Tinyclues, créez une campagne ou un Canvas Braze et sélectionnez le segment comme audience cible. 

![Dans le générateur de campagne de Braze, à l'étape du ciblage, le filtre "Cibler les utilisateurs par segment" est défini sur "Cohorte de Tinyclues".]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## Correspondance entre les utilisateurs

Les utilisateurs identifiés peuvent être associés à leur adresse `external_id` ou `alias`. Les utilisateurs anonymes peuvent être mis en relation avec leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id`, et doivent être identifiés par leur `external_id` ou `alias`.

## Résolution des problèmes

Vous avez du mal à trouver la bonne cohorte dans la liste ? Dans Tinyclues, affichez les détails de votre campagne et vérifiez le nom en cochant le **Nom du fichier d'exportation.**

![Le nom de votre cohorte apparaît en bas de la page des détails de la campagne.]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

Vous n'arrivez toujours pas à extraire votre audience ? Contactez l'[équipe de Tinyclues](mailto:support@tinyclues.com) pour obtenir une assistance supplémentaire.

