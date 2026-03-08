---
nav_title: Splio
article_title: Splio
alias: /partners/splio/
description: "Cet article de référence présente le partenariat entre Braze et Splio, qui vous permet d'envoyer des campagnes plus ciblées, de trouver de nouvelles opportunités de produits et d'augmenter vos chiffres d'affaires."
page_type: partner
search_tag: Partner

---

# Splio

> [Splio](https://splio.com/) est un outil de création d'audience qui vous permet d'augmenter le nombre de campagnes et le chiffre d'affaires sans nuire à l'expérience client, et qui fournit des analyses pour suivre les performances des campagnes CRM en ligne et hors ligne.

L'intégration de Braze et Splio vous permet de planifier et d'exécuter de meilleures stratégies CRM, d'envoyer des campagnes plus ciblées, de trouver de nouvelles opportunités de produits et d'augmenter votre chiffre d'affaires.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Splio | Vous avez besoin d'un compte Splio pour ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration de l'importation de données

Pour intégrer Braze et Splio, vous devez configurer la plateforme Splio, exporter une campagne Splio existante et créer un segment de cohorte dans Braze pour cibler les utilisateurs dans les futures campagnes.

### Étape 1 : Obtenez la clé d'importation des données Braze

Dans Braze, allez dans **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Splio**.

Trouvez votre endpoint REST et générez votre clé d'importation des données Braze. Après avoir généré la clé, vous pouvez créer une nouvelle clé ou invalider une clé existante.<br><br>![La page partenaire technologique de Splio avec l'endpoint REST et la clé d'importation des données.]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"}

Pour terminer l'intégration, fournissez la clé d'importation des données et l'endpoint REST à votre équipe d'exploitation des données Splio. Splio établit la connexion et vous contacte une fois la configuration terminée.

### Étape 2 : Exporter une campagne depuis la plateforme Splio

Chaque fois que vous souhaitez créer une cohorte d'utilisateurs Splio dans Braze, vous devez d'abord l'exporter depuis la plateforme Splio.

Dans Splio, sélectionnez les campagnes que vous souhaitez exporter et cliquez sur **Exporter les campagnes.** Après l'exportation, l'audience est automatiquement téléchargée sur votre compte Braze.

![Exporter des campagnes depuis la plateforme Splio.]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### Étape 3 : Créez un segment à partir de l'audience personnalisée de Splio.

Dans Braze, naviguez vers **Segments**, nommez votre segment de cohorte Splio et sélectionnez **Cohortes Splio** comme filtre. À partir de là, choisissez la cohorte Splio à inclure. Après avoir créé votre segment de cohorte Splio, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une campagne ou d'un Canvas.

![Création d'un segment de cohorte Splio dans Braze.]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![Dans le générateur de segments de Braze, le filtre d'attributs utilisateur "Splio cohorte" est défini sur "inclut" et "Cohorte primaire".]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

Vous avez des difficultés à localiser votre cohorte ? Consultez la section [résolution des problèmes](#troubleshooting) pour obtenir des conseils.

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze sont ajoutés ou supprimés d'une cohorte. L'importation d'une cohorte ne crée pas de nouveaux utilisateurs dans Braze.
{% endalert %}

## Utilisation de cette intégration

Pour utiliser votre segment Splio, créez une campagne ou un Canvas Braze et sélectionnez le segment comme votre audience cible.

![Dans le générateur de campagne Braze, à l'étape du ciblage, le filtre "Cibler les utilisateurs par segment" est défini sur "Cohorte Splio".]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## Correspondance des utilisateurs

Braze fait correspondre les utilisateurs identifiés par leur `external_id` ou `alias`. Les utilisateurs anonymes sont mis en relation avec leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être associés à leur `device_id`, et doivent être associés à leur `external_id` ou `alias`.

## Résolution des problèmes

Si vous ne trouvez pas la bonne cohorte dans la liste, consultez les détails de votre campagne dans Splio et vérifiez le nom en contrôlant le **Nom du fichier d'exportation.**

![Le nom de votre cohorte apparaît au bas de la page des détails de la campagne.]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

Si vous rencontrez des difficultés pour récupérer votre audience, contactez l' [équipe de Splio](mailto:support-team@splio.com) pour obtenir de l'aide.