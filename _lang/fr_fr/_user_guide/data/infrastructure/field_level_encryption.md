---
nav_title: "Cryptage au niveau du champ de l'identifiant"
article_title: Identifiant Cryptage au niveau du champ
page_order: 2
alias: "/field_level_encryption/"
description: "Cet article de référence explique comment crypter les adresses e-mail afin de minimiser les informations personnelles identifiables (PII) partagées dans Braze."
page_type: reference
---

# Cryptage au niveau du champ de l'identifiant

> Grâce au chiffrement au niveau du champ d'identification, vous pouvez chiffrer de façon fluide/sans heurts les adresses e-mail avec AWS Key Management Service (KMS) afin de minimiser les informations personnelles identifiables (PII) partagées dans Braze. Le chiffrement remplace les données sensibles par du texte chiffré, c'est-à-dire des informations chiffrées illisibles.

{% alert important %}
Le cryptage au niveau du champ d'identification est disponible en tant que fonctionnalité supplémentaire. Pour commencer à utiliser le cryptage au niveau du champ d'identification, contactez votre gestionnaire de compte Braze.
{% endalert %}

## Comment cela fonctionne-t-il ?

Les adresses e-mail doivent être hachées et cryptées avant d'être ajoutées à Braze. Lors de l'envoi d'un message, un appel est lancé à AWS KMS pour obtenir l'adresse e-mail décryptée. Ensuite, l'adresse e-mail hachée sera insérée dans les métadonnées des événements de réception/distribution pour être reliée à l'utilisateur d'origine. C'est ainsi que Braze peut suivre l'analyse/analytique des e-mails. Braze caviardera toutes les adresses e-mail en clair qui sont incluses et ne stockera pas l'adresse e-mail en clair de l'utilisateur.

## Conditions préalables

Pour utiliser le chiffrement au niveau du champ d'identification, vous devez avoir accès à AWS KMS pour [chiffrer](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) et [hacher les](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) adresses e-mail **avant de** les envoyer à Braze. 

Suivez ces étapes pour configurer votre méthode d'authentification par clé secrète AWS.

1. Pour récupérer votre ID de clé d'accès et votre clé d'accès secrète, [créez un utilisateur IAM et un groupe d'administrateurs](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) dans AWS avec une politique d'autorisations pour AWS Key Management Service. L'utilisateur IAM doit disposer des autorisations [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) et [kms:GenerateMac.](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html)  Pour plus d'informations, reportez-vous aux [autorisations AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html).
2. Sélectionnez **Afficher les informations de sécurité de l'utilisateur** pour révéler votre ID de clé d'accès et votre clé d'accès secrète. Notez ces informations d'identification quelque part ou sélectionnez le bouton **Télécharger les informations d'identification** car vous devrez les saisir lors de la connexion de vos clés AWS KMS.
3. Vous devez configurer KMS dans les régions AWS suivantes :
    - **Clusters américains de Braze :** `us-east-1`
    - **Brazez les grappes de l'UE :** `eu-central-1`
4. Dans AWS Key Management Service, créez deux clés et assurez-vous que l'utilisateur IAM est ajouté dans les autorisations d'utilisation des clés :
    - **[Cryptage/décryptage](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk):** Sélectionnez le type de clé **symétrique** et l'utilisation des clés de **chiffrement et de déchiffrement**.
    - **[Hash](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html):** Sélectionnez Type de clé **symétrique** et **Générer et vérifier l'** utilisation de la clé **MAC.**  La spécification clé devrait être **HMAC_256**. Après avoir créé la clé, notez l'ID de la clé HMAC quelque part, car vous devrez le saisir dans Braze.

\![]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## Étape 1 : Connectez vos clés AWS KMS

Dans le tableau de bord de Braze, accédez à **Paramètres des données** > **Chiffrement au niveau du champ**. Pour vos paramètres AWS KMS, entrez ce qui suit :

- ID de la clé d'accès
- Clé d'accès secrète
- ID de la clé HMAC (elle ne peut pas être mise à jour après avoir été enregistrée)

## Étape 2 : Sélectionnez vos champs cryptés

Ensuite, sélectionnez **Adresse e-mail** pour crypter le champ. 

Lorsque le cryptage est activé pour un champ, il n'est pas possible de revenir à un champ décrypté. Cela signifie que le cryptage est un paramètre permanent. Lorsque vous configurez le cryptage de l'adresse e-mail, assurez-vous qu'aucun utilisateur ne dispose d'une adresse e-mail dans l'espace de travail. Cela permet de s'assurer qu'aucune adresse e-mail en clair n'est stockée dans Braze lorsque vous activez la fonctionnalité pour l'espace de travail.

\![]({% image_buster /assets/img/field_level_encryption.png %})

## Étape 3 : Importation d'utilisateurs et mise à jour des données

Lorsque le cryptage au niveau du champ d'identification est activé, vous devez hacher et crypter l'adresse e-mail avant de l'ajouter à Braze. Veillez à mettre l'adresse e-mail en minuscules avant de la hacher. Pour plus de détails, voir l'[objet "Attributs de l'utilisateur"](#user-attributes-object).

Lorsque vous mettez à jour l'adresse e-mail dans Braze, vous devez utiliser la valeur hachée de l'e-mail partout où `email` est inclus. Il s'agit notamment de

- Les endpoints REST :
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- Ajout ou mise à jour d'utilisateurs via CSV

{% alert note %}
Lorsque vous créez un nouvel utilisateur avec une adresse e-mail, vous devez ajouter `email_encrypted` avec la valeur cryptée de l'e-mail de l'utilisateur. Sinon, l'utilisateur ne sera pas créé. De même, si vous ajoutez une adresse e-mail à un utilisateur existant qui n'a pas d'e-mail, vous devez ajouter `email_encrypted`. Dans le cas contraire, l'utilisateur ne sera pas mis à jour.
{% endalert %}

## Considérations

Ces fonctionnalités ne sont pas prises en charge avec le cryptage au niveau du champ d'identification :

- Identifier et capturer l'adresse e-mail via le SDK
- Formulaires d'envoi de messages in-app par e-mail
- Rapports sur le domaine du destinataire, y compris les graphiques du fournisseur de boîtes aux lettres Email Insights
- Filtre d'adresses e-mail par expression régulière
- Synchronisation de l'audience
- Intégration de Shopify

### Objet attributs de l'utilisateur

Lorsque vous utilisez le cryptage au niveau du champ d'identification avec l'endpoint `/users/track`, notez les détails de ces champs pour l'[objet attributs de l'utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object):

- Le champ `email` doit être la valeur hachée de l'e-mail.
- Le champ `email_encrypted` doit être la valeur cryptée de l'e-mail.

## Questions fréquemment posées

### Quelle est la différence entre le cryptage et le hachage ?

Le cryptage est une fonction bidirectionnelle qui permet de crypter et de décrypter des données. Si la même valeur en clair est chiffrée plusieurs fois, l'algorithme de chiffrement d'AWS (AES-256-GCM) produira des valeurs chiffrées différentes. Le hachage est une fonction à sens unique dans laquelle le texte en clair est brouillé de manière à ne pas pouvoir être décrypté. Le hachage permet d'obtenir la même valeur à chaque fois. Cela nous permet de maintenir l'état des abonnements pour plusieurs utilisateurs partageant la même adresse e-mail.

### Quelle adresse e-mail dois-je utiliser pour mon envoi de test ?

Les adresses e-mail en clair sont prises en charge dans le cadre de l'envoi de tests. Pour voir à quoi ressemble un e-mail pour un utilisateur spécifique, procédez comme suit :

1. Sélectionnez **Prévisualiser le message en tant qu'utilisateur**.
2. Dans **Test Send**, sélectionnez **Override recipients with current preview user's attributes (Remplacer les attributs des destinataires par ceux de l'utilisateur actuel)**.

{%raw%}
### Que se passe-t-il si j'ajoute cette adresse e-mail Liquid `{{${email_address}}}` dans Braze ?

Braze rendra l'adresse e-mail en clair lors de l'envoi de l'e-mail. Dans les aperçus, nous afficherons la version cryptée de l'e-mail. Nous vous recommandons d'utiliser l'ID externe de l'utilisateur si vous faites référence à un utilisateur dans une URL personnalisée en un clic.

`{{${email_address}}}` n'est actuellement pas pris en charge dans le centre de préférences et les pages de désabonnement.
{%endraw%}

### Quelle adresse e-mail dois-je m'attendre à voir figurer dans Currents ?

L'adresse électronique hachée est incluse dans les événements de réception/distribution des e-mails.

### Quelle adresse e-mail dois-je m'attendre à voir apparaître dans l'archivage des messages ?

L'adresse e-mail en clair est incluse dans l'archivage des messages. Ceux-ci sont envoyés directement au fournisseur de stockage en nuage du client et il peut y avoir d'autres données personnelles incluses dans le corps des e-mails.

### Puis-je utiliser mail-to list-unsubscribe pour la gestion des abonnements avec un cryptage au niveau du champ d'identification ?

Non. L'utilisation de mail-to list-unsubscribe enverrait l'adresse e-mail décryptée en clair à Braze. Lorsque le cryptage au niveau du champ d'identification est activé, nous prenons en charge la méthode HTTP : basée sur l'URL, y compris le clic unique. Nous vous recommandons également d'inclure un lien de désabonnement en un clic dans le corps de votre e-mail.

### Le cryptage au niveau du champ de l'identifiant prend-il en charge d'autres identifiants tels que le téléphone ?

Non. Actuellement, le cryptage au niveau du champ d'identification n'est pris en charge que pour les adresses e-mail.
