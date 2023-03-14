---
nav_title: Lexer
article_title: Lexer
page_order: 1
description: "Cet article présente le partenariat entre Braze et Lexer, une plateforme de données client qui aide les marketeurs à créer des expériences qui génèrent des ventes grâce aux données."
alias: /partners/lexer/
page_type: partner
search_tag: Partenaire
---

# Lexer

> [Lexer][6] est une plateforme de données client conçue pour la vente au détail et qui aide les marques à augmenter leurs ventes grâce à des expériences client améliorées, combinant un enrichissement des données robuste avec des outils extrêmement intuitifs et des conseils d’experts.

L’intégration entre Braze et Lexer vous permet de synchroniser des données entre les deux plateformes. Utilisez vos données Lexer pour créer des segments Braze, ou importez vos propres données dans Lexer pour en extraire de précieuses informations. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte partenaire | Un compte Lexer est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé API REST de Braze avec des autorisations `users.track` (sauf `user.delete`) et des autorisations `segment.list`. Les autorisations peuvent changer à mesure que Lexer prend en charge un plus grand nombre d’objets Braze. Vous pouvez donc choisir d’accorder davantage d’autorisations maintenant ou prévoir de mettre à jour ces autorisations à l’avenir.<br><br> Cela peut être créé dans le **Tableau de bord de Braze > Developer Console > REST API Key (Clé API REST) > Create New Api Key** (Créer une nouvelle clé API) |
| Endpoint REST de Braze | [L’URL de votre endpoint REST]({{site.baseurl}}/api/basics/#endpoints). Votre endpoint dépendra de l’URL Braze pour votre instance. |
| Informations d’identification et compartiment S3 d’Amazon AWS | Avant de commencer l’intégration, vous devez disposer des informations d’identification d’un compartiment S3 d’AWS connecté à votre hub Lexer (il peut s’agir d’un compartiment que vous créez ou d’un que Lexer crée et gère pour vous). Rendez-vous sur le site Web de [Lexer](https://learn.lexer.io/docs/amazon-s3) pour obtenir des conseils sur cette exigence. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Dans Lexer, accédez **Manage (Gérer) > Integration (Intégration)**, puis sélectionnez la mosaïque **Braze** et cliquez sur **Integrate Braze (Intégrer Braze)**. Fournissez les informations suivantes :
- **Endpoint REST de Braze**
- **Clé API REST Braze**
- **Informations d’identification AWS**
  - **Nom du compartiment AWS S3**
  - **Région du compartiment [AWS S3][4]**
  - **Chemin d’accès du compartiment AWS S3** : Ce chemin doit correspondre au chemin que vous avez indiqué en [connectant votre compartiment S3 à Braze][5]. Ce champ doit être vide si vous n’avez rien indiqué dans Braze.
  - **Clé d’accès secrète AWS S3** : Consultez le site Web d’Amazon pour obtenir des informations sur la [création d’une clé d’accès][3].
- **ID du segment d’exportation Braze** : L’ID du segment que vous avez créé dans Braze, contenant tous les utilisateurs que vous souhaitez exporter vers Lexer. Si vous ne souhaitez pas exporter certains utilisateurs vers Lexer, vous pouvez les exclure du segment que vous avez créé dans Braze. Pour trouver l’identifiant de votre segment, cliquez sur le segment souhaité dans Braze et recherchez l’**Identifiant d’API Segment**.

![][1]

### Choisir une option AWS S3 (géré par Lexer ou géré par vous-même)
L’option de compartiment géré par Lexer est la méthode recommandée pour connecter Braze à votre hub Lexer et réduire la configuration nécessaire. Lexer vous fournira des informations ponctuelles dont vous aurez besoin pour configurer Braze.

Si vous avez déjà connecté un compartiment S3 à Braze et que vous l’utilisez pour autre chose, vous devrez permettre à Lexer d’accéder à ce compartiment auto-géré en suivant les étapes précédentes.

Cette intégration fonctionne en fournissant votre jeton API et vos clés secrètes à Lexer, ce qui lui permet de réaliser ces exportations en votre nom. Elle importe également vos données Braze dans Lexer en utilisant ces informations d’identification et votre configuration S3 pour synchroniser automatiquement vos données sur les deux plateformes.

## Envoyer des segments à Braze

### Étape 1 : Créer une activation

Lexer Activate mettra automatiquement à jour vos profils Braze, ajoutant ou supprimant des attributs lorsque les clients entrent et sortent de votre segment.

1. Dans Lexer, dans **Lexer Activations (Activations Lexer)**, cliquez sur **ACTIVATE NEW AUDIENCE (ACTIVER UNE NOUVELLE AUDIENCE)**.
2. Sélectionnez l’activation Braze appropriée pour cette campagne.
3. Ajoutez votre segment.
4. Mettez à jour le nom de votre audience ; il deviendra votre valeur d’attribut dans Braze.
5. Il s’agit de l’attribut personnalisé que nous allons mettre à jour dans Braze. Contactez le [service d’assistance Lexer](support@lexer.io) pour le mettre à jour.
6. Vérifiez l’action de la liste appropriée (dans la plupart des cas, vous souhaiterez conserver votre liste).
7. Passez en revue les conditions générales et cliquez sur **SEND AUDIENCE (ENVOYER L’AUDIENCE)**.

![][7]

### Étape 2 : Vérifier l’activation

Une fois votre activation confirmée comme envoyée dans Activate, vous verrez que les enregistrements commencent à être mis à jour dans Braze. Vos profils ne seront pas entièrement mis à jour dans Braze tant que vous n’aurez pas reçu d’e-mail de confirmation de la part de Lexer.

### Étape 3 : Créez votre segment Braze

Dans Braze, vous verrez que le nom de votre audience dans Lexer est maintenant une valeur dans votre attribut personnalisé d’`lexer_audience`. Braze a une limite de 100 valeurs par attribut.

Pour créer votre segment, accédez à **Segment > > + Create Segment (+ Créer segment)** et sélectionnez **Custom Attribute (Attribut personnalisé)** en tant que filtre. Ensuite, sélectionnez `lexer_audience` comme votre attribut et le nom de l’audience Lexer que vous souhaitez. Une fois terminé, **enregistrez** votre audience.

Vous pouvez maintenant ajouter le segment que vous venez de créer dans de futures campagnes et Canvas de Braze pour cibler ces utilisateurs finaux.

[1]: {% image_buster /assets/img/lexer/braze_integrate_screen.png %}
[2]: {{site.baseurl}}/api/basics/#company-secret-explanation
[3]: https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/
[4]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html
[5]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/
[6]: https://lexer.io/
[7]: {% image_buster /assets/img/lexer/lexer.png %}