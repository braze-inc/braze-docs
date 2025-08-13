---
nav_title: Lexer
article_title: Lexer
description: "Cet article de référence présente le partenariat entre Braze et Lexer, une plateforme de données client qui met les données client entre les mains des marketeurs pour inspirer des expériences qui stimulent les ventes."
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# Lexer

> [Lexer][6], une plateforme de données client créée pour le commerce de détail, aide les marques à générer des ventes incrémentales grâce à des expériences client améliorées en combinant un enrichissement robuste des données avec des outils intuitifs et des conseils d'experts.

_Cette intégration est maintenue par Lexer._

## À propos de l'intégration

L'intégration de Braze et Lexer vous permet de synchroniser les données entre les deux plateformes. Utilisez vos données Lexer pour créer de précieux segments Braze ou importez vos segments existants dans Lexer pour obtenir des informations. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte partenaire | Un compte Lexer est nécessaire pour bénéficier de ce partenariat. |
| Clé d'API REST Braze | Une clé API REST de Braze avec toutes les autorisations `user` (à l'exception de `user.delete`) et `segment.list`. Le jeu de permissions peut changer au fur et à mesure que Lexer ajoute la prise en charge de nouveaux objets Braze, de sorte que vous pouvez soit vouloir accorder plus de permissions maintenant, soit prévoir de mettre à jour ces permissions à l'avenir.<br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | Votre [URL d’endpoint REST]({{site.baseurl}}/api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Compartiment S3 d'Amazon AWS et identifiants | Avant de commencer l'intégration, vous devez disposer des identifiants d'accès à un compartiment AWS S3 connecté à votre hub Lexer (il peut s'agir d'un compartiment que vous créez ou d'un compartiment que Lexer crée et gère pour vous). Consultez [Lexer](https://learn.lexer.io/docs/amazon-s3) pour obtenir des conseils sur cette exigence. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Dans Lexer, naviguez vers **Gestion > Intégration**, sélectionnez la tuile **Braze** et cliquez sur **Intégrer Braze.** Fournissez les informations suivantes :
- **Endpoint REST de Braze**
- **Clé API REST de Braze**
- **Informations de connexion AWS**
  - **Nom du compartiment S3 AWS**
  - **AWS S3 [région du compartiment S3][4]**
  - **Chemin d'accès au compartiment AWS S3**: Ce chemin doit correspondre à celui que vous avez spécifié lors de la [connexion de votre compartiment S3 à Braze][5]. Ce champ doit être vide si vous n'avez rien spécifié à Braze.
  - **Clé d'accès secrète d'AWS S3**: Visitez Amazon pour obtenir des informations sur [la création d'une clé d'accès][3].
- **ID de segment d’export Braze** : L'ID du segment que vous avez créé dans Braze et qui contient tous les utilisateurs que vous souhaitez exporter vers Lexer. S'il y a des utilisateurs que vous ne voulez pas exporter vers Lexer, vous pouvez les exclure du segment que vous avez créé dans Braze. Pour trouver votre identifiant de segment, cliquez sur le segment de votre choix dans Braze et localisez l'**identifiant API du segment.**

![][1]

### Choix d'une option AWS S3 (gérée par Lexer ou autogérée)
L'utilisation d'un compartiment géré par Lexer est le meilleur moyen de connecter Braze à votre concentrateur Lexer et réduira le nombre de configurations nécessaires. Lexer vous fournira les détails ponctuels dont vous aurez besoin pour configurer Braze.

Si vous avez déjà connecté un compartiment S3 à Braze et que vous l'utilisez à d'autres fins, vous devrez à la place fournir à Lexer un accès à ce compartiment autogéré en suivant les étapes précédentes.

Cette intégration fonctionne en fournissant à Lexer votre jeton API et vos secrets existants afin de permettre à Lexer d'effectuer ces exportations en votre nom. Il importe également vos données Braze dans Lexer en utilisant ces identifiants et votre configuration S3 pour synchroniser automatiquement vos données sur les deux plateformes.

## Envoi de segments à Braze

### Étape 1 : Créer une activation

Lexer Activate mettra automatiquement à jour vos profils Braze, en ajoutant ou en supprimant des attributs au fur et à mesure que les clients entrent et sortent de votre segmentation.

1. Dans Lexer, dans **Activations Lexer**, cliquez sur **ACTIVER UNE NOUVELLE AUDIENCE**.
2. Sélectionnez l'activation de Braze appropriée pour cette campagne.
3. Ajoutez votre segment.
4. Mettez à jour le nom de votre audience ; il deviendra votre valeur d'attribut dans Braze.
5. Il s'agit de l'attribut personnalisé que nous allons mettre à jour dans Braze. Contactez le [service d’assistance de Lexer](support@lexer.io) pour mettre à jour l’attribut.
6. Cochez l'action de liste appropriée - dans la plupart des cas, vous voudrez maintenir votre liste.
7. Passez en revue les conditions générales et cliquez sur **ENVOYER L'AUDIENCE**.

![][7]

### Étape 2 : Vérifier l'activation

Une fois que l'envoi de votre activation a été confirmé dans Activate, les enregistrements commenceront à se mettre à jour dans Braze. Vos profils ne seront entièrement mis à jour dans Braze qu'après avoir reçu un e-mail de confirmation de Lexer.

### Étape 3 : Créez votre segment Braze

Dans Braze, vous verrez que le nom de votre audience dans Lexer est maintenant une valeur dans votre attribut personnalisé `lexer_audience`. Braze a une limite de 100 valeurs par attribut.

Pour créer votre segment, accédez à **Segment > + Créer un segment** et sélectionnez **Attribut personnalisé** comme filtre. Ensuite, sélectionnez `lexer_audience` comme attribut et le nom de l'audience Lexer que vous souhaitez utiliser. Une fois terminé, **enregistrez** votre audience.

Vous pouvez désormais ajouter ce segment nouvellement créé aux futures campagnes et Canvas de Braze afin de cibler ces utilisateurs finaux.


[1]: {% image_buster /assets/img/lexer/braze_integrate_screen.png %}
[2]: {{site.baseurl}}/api/basics/#company-secret-explanation
[3]: https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/
[4]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html
[5]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/
[6]: https://lexer.io/
[7]: {% image_buster /assets/img/lexer/lexer.png %}
