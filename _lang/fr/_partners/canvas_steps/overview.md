---
nav_title: Aperçu
article_title: Aperçu
description: "Cet article de référence vous explique comment utiliser la fonction de synchronisation de Braze vers Facebook, pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
page_order: 0
Tool:
  - Canvas

---

# Aperçu de la synchronisation de l'audience

> La fonctionnalité de synchronisation de l’audience de Braze vous permet d’étendre la portée de vos campagnes à de nombreuses technologies sociales et publicitaires de premier plan. Grâce à [Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas), les marques peuvent synchroniser de manière dynamique et sécurisée les données first-party des utilisateurs dans l'écosystème publicitaire afin de favoriser le marketing et l'efficacité opérationnelle.

## Cas d'utilisation

- Le ciblage des utilisateurs à forte valeur ajoutée via les canaux propriétaires et payants pour susciter des achats ou un engagement incrémentiels.
- Création d'audiences lookalike de vos utilisateurs à forte valeur ajoutée pour optimiser les coûts d'acquisition de nouveaux utilisateurs et les conversions.
- Recibler les utilisateurs qui sont moins réactifs aux autres canaux de marketing avec des publicités.
- Créer des audiences de suppression pour éviter que les utilisateurs ne reçoivent des publicités alors qu'ils sont déjà des consommateurs fidèles de votre marque.

## Disponibilité des fonctionnalités

Tous les clients de Braze auront immédiatement accès à la fonction de synchronisation avec Google et Facebook. Pour débloquer d’autres destinations de la fonction de synchronisation, notamment TikTok, Pinterest, Snapchat ou Criteo, vous devez acheter Audience Sync Pro. Contactez votre gestionnaire de compte Braze pour plus de détails.

## Comment cela fonctionne-t-il ?

Pour utiliser la fonction de synchronisation vers Google ou Facebook, connectez votre compte publicitaire en recherchant le partenaire sur la page **partenaires technologiques**.

![][3]{: style="max-width:35%;"} ![][4]{: style="max-width:35%;"}

Après avoir connecté votre compte d'annonces, vous pouvez créer un canvas avec une étape de synchronisation de l'audience.

![][22]{: style="max-width:75%;"}

Sélectionnez ensuite le partenaire avec lequel vous souhaitez synchroniser les audiences.

![][19]{: style="max-width:85%;"}

Pour chaque partenaire, vous devez configurer les éléments suivants dans le cadre de l'étape de synchronisation de l'audience : 
- Compte d'annonces
- Audience 
- Action d'ajouter ou de supprimer des utilisateurs 
- Champs à faire correspondre 

Gardez à l'esprit que Braze synchronisera les utilisateurs dès qu'ils entreront dans l'étape de synchronisation de l'audience au sein de votre Canvas. 

Pour chaque destination de la fonction de synchronisation, le partenaire peut avoir des exigences différentes quant aux champs que nous pouvons envoyer. Pour plus de détails, reportez-vous à la documentation spécifique du partenaire. 

### Audience Sync Pro

Pour utiliser un partenaire de synchronisation d’audience professionnelle, notamment TikTok, Pinterest, Snapchat ou Criteo, vous pourrez sélectionner vos partenaires en fonction de vos attributions d'achats de synchronisation d’audiences professionnelle dans la section **Audience Sync Pro** de la page **Partenaires technologiques**.

![][5]{: style="max-width:75%;"}

Tout d'abord, sélectionnez les partenaires que vous voulez utiliser en choisissant Sélectionner des partenaires. Chaque achat d'Audience Sync Pro vous permettra d'obtenir 3 destinations d’Audience Sync Pro, qui seront disponibles dans chacun de vos espaces de travail au sein de votre tableau de bord.

![][6]{: style="max-width:65%;"}

Après avoir sélectionné vos destinations Audience Sync Pro, connectez votre compte publicitaire partenaire sélectionné en cliquant sur la vignette des partenaires.

![][7]{: style="max-width:70%;"}

![][9]{: style="max-width:70%;"}

Enfin, créez votre étape de canvas pour la synchronisation de l’audience en utilisant cette destination Audience Sync Pro.

## Considérations relatives à la confidentialité des données

{% alert important %}
Cette documentation n'a pas pour but de fournir des conseils juridiques et ne peut être considérée comme telle. L'utilisation de la fonction de synchronisation de l'audience est soumise à des exigences légales spécifiques. Pour vous assurer que vous l'utilisez en conformité avec toutes les lois applicables, vous devez demander l'avis de votre conseiller juridique.
{% endalert %}

Lorsque vous créez des audiences pour le suivi publicitaire, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et vous conformer aux lois sur la protection de la vie privée, telles que le droit "Ne pas vendre ou partager" en vertu de la [CCPA.](https://oag.ca.gov/privacy/ccpa) Les marketeurs devraient implémenter les filtres pertinents pour l'éligibilité des utilisateurs dans leurs critères d'entrée de canvas. Ci-dessous, nous listons quelques options.

Si vous avez collecté l'[IDFA iOS par le biais du SDK de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), vous pourrez utiliser le filtre " Suivi des publicités activé ". Sélectionnez la valeur `true` afin d'envoyer uniquement les utilisateurs vers les destinations de synchronisation d'audience où ils ont donné leur consentement.

![][2]

Si vous collectez `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, ou tout autre attribut personnalisé pertinent, vous devez les inclure dans les critères d'entrée de votre Canvas en tant que filtre :

![Un canvas dont l'audience d'entrée est "opted_in_marketing" est égal à "true".][1]

Pour en savoir plus sur la manière de se conformer à ces lois sur la protection des données au sein de la plateforme Braze, consultez l'[assistance technique sur la protection des données.]({{site.baseurl}}/dp-technical-assistance/)

[1]: {% image_buster /assets/img/audience_sync/audience_sync.png %}
[2]: {% image_buster /assets/img/audience_sync/audience_sync2.png %}
[3]: {% image_buster /assets/img/audience_sync/facebook_partner.png %}
[4]: {% image_buster /assets/img/audience_sync/google_ads_partner.png %}
[5]: {% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}
[6]: {% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}
[7]: {% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}
[8]: {% image_buster /assets/img/audience_sync/audience_sync_pro3b.png %}
[9]: {% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/audience_sync6.png %}
[22]: {% image_buster /assets/img/audience_sync/audience_sync7.png %}