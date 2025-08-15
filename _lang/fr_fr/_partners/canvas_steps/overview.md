---
nav_title: "À propos d'Audience Sync"
article_title: "À propos d'Audience Sync"
description: "Cet article de référence vous explique comment utiliser la fonction de synchronisation de Braze vers Facebook, pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
page_order: 0
Tool:
  - Canvas

---

# À propos d'Audience Sync

> La fonctionnalité de synchronisation de l’audience de Braze vous permet d’étendre la portée de vos campagnes à de nombreuses technologies sociales et publicitaires de premier plan. Grâce à [Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas), les marques peuvent synchroniser de manière dynamique et sécurisée les données first-party des utilisateurs dans l'écosystème publicitaire afin de favoriser le marketing et l'efficacité opérationnelle.

## Disponibilité des fonctionnalités

Tous les clients de Braze auront immédiatement accès à la fonction de synchronisation avec Google et Facebook. Pour débloquer d’autres destinations de la fonction de synchronisation, notamment TikTok, Pinterest, Snapchat ou Criteo, vous devez acheter Audience Sync Pro. Contactez votre gestionnaire de compte Braze pour plus de détails.

## Cas d'utilisation

- Le ciblage des utilisateurs à forte valeur ajoutée en utilisant des canaux propriétaires et payants pour susciter des achats ou un engagement incrémentiels.
- Création d'audiences lookalike de vos utilisateurs à forte valeur ajoutée pour optimiser les coûts d'acquisition de nouveaux utilisateurs et les conversions.
- Recibler les utilisateurs qui sont moins réactifs aux autres canaux de marketing avec des publicités.
- Créer des audiences de suppression pour éviter que les utilisateurs ne reçoivent des publicités alors qu'ils sont déjà des consommateurs fidèles de votre marque.

## Aperçu

<style>
table td {
    word-break: break-word;
}
</style>

| Destination | Il est temps que la destination corresponde aux membres de l'audience | Limite de débit | Sosie ou sosie réel | Conseils |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_steps/criteo_audience_sync) | Jusqu'à 24 heures | 250 000 demandes par minute. Les données sont regroupées toutes les 5 secondes, avec une relance automatique basée sur les commentaires de Google. | Oui | {::nomarkdown}<ul><li>Criteo prend en charge jusqu'à 1 000 audiences publicitaires.</li><li>La taille minimale de l'audience est de 500 personnes, et la taille recommandée est de plus de 20 000 personnes.</li></ul>{:/} |
| [Facebook ou Instagram]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/) | Jusqu'à 24 heures | 190 000 comptes publicitaires par heure | Oui | {::nomarkdown}<ul><li>Facebook prend en charge jusqu'à 500 audiences publicitaires.</li><li>Facebook exige que les audiences soient composées d'au moins 1 000 utilisateurs.</li></ul>{:/} |
| [Google Ads ou YouTube]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/) | Entre 6 et 12 heures | Les données sont regroupées toutes les 5 secondes, avec une relance automatique basée sur les commentaires de Google. | Non | {::nomarkdown}<ul><li><b>Match des clients :</b> Utilisez soit l'annonce mobile, soit l'adresse e-mail ou le numéro de téléphone.</li><li>Google Audiences nécessite au moins 5 000 utilisateurs pour commencer à diffuser des annonces.</li><li>La taille de l'audience sera nulle jusqu'à ce qu'il y ait au moins 1 000 utilisateurs.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_steps/linkedin_audience_sync) | 48 heures | LinkedIn traite 10 requêtes par seconde et 100 000 utilisateurs par demande. Les utilisateurs des lots de Braze se succèdent toutes les 5 secondes. | L'intelligence artificielle au service des prédictions d'audience | {::nomarkdown}<ul><li>La taille minimale de l'audience est de 300 membres, le ciblage de l'emplacement/localisation étant pris en considération.</li><li>LinkedIn affiche le taux correspondant dans le tableau de bord de Braze.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_steps/pinterest_audience_sync/) | Entre 24 et 48 heures | Pinterest traite 7 requêtes par seconde et 100 000 utilisateurs par demande. Les utilisateurs des lots de Braze se succèdent toutes les 5 secondes. | Oui | Les audiences Pinterest nécessitent au moins 100 utilisateurs. |
| [Snapchat]({{site.baseurl}}/partners/canvas_steps/snapchat_audience_sync/) | N/A | Snapchat traite 10 requêtes par seconde et 100 000 utilisateurs par requête. Les utilisateurs des lots de Braze se succèdent toutes les 5 secondes. | Oui | Snapchat prend en charge jusqu'à 1 000 audiences publicitaires. |
| [TikTok]({{site.baseurl}}/partners/canvas_steps/tiktok_audience_sync/) | Entre 24 et 48 heures | TikTok traite 50 requêtes par seconde et 10 000 utilisateurs par demande. Les utilisateurs des lots de Braze se succèdent toutes les 5 secondes. | Oui | {::nomarkdown}<ul><li>TikTok prend en charge jusqu'à 400 audiences publicitaires.</li><li>Les audiences de TikTok nécessitent au moins 1 000 utilisateurs pour commencer à diffuser des publicités.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
<sup>Lorsque la limite de débit est atteinte, Braze effectue une nouvelle tentative de synchronisation pendant 13 heures.</sup>

## Comment cela fonctionne-t-il ?

Pour utiliser la fonction de synchronisation vers Google ou Facebook, connectez votre compte publicitaire en recherchant le partenaire sur la page **partenaires technologiques**.

![Partenaire technologique de Facebook.][3]{: style="max-width:35%;"} ![Partenaire technologique de Google Ads.][4]{: style="max-width:35%;"}

Après avoir connecté votre compte publicitaire, vous pouvez créer un canvas avec une étape de synchronisation de l'audience.

![Menu du composant canvas pour ajouter l'étape du canvas de synchronisation de l'audience au parcours de l'utilisateur.][22]{: style="max-width:75%;"}

Sélectionnez ensuite le partenaire avec lequel vous souhaitez synchroniser les audiences.

![Option permettant de sélectionner votre partenaire de synchronisation d'audience dans l'étape Synchronisation d'audience.][19]{: style="max-width:85%;"}

Pour chaque partenaire, vous devez configurer les éléments suivants dans le cadre de l'étape de synchronisation de l'audience : 

- Compte d'annonces
- Audience 
- Action d'ajouter ou de supprimer des utilisateurs 
- Champs à faire correspondre 

Gardez à l'esprit que Braze synchronisera les utilisateurs dès qu'ils entreront dans l'étape de synchronisation de l'audience au sein de votre Canvas. 

Pour chaque destination de la fonction de synchronisation, le partenaire peut avoir des exigences différentes quant aux champs que nous pouvons envoyer. Pour plus de détails, reportez-vous à la documentation spécifique du partenaire. 

### Audience Sync Pro

Pour utiliser un partenaire de synchronisation d’audience professionnelle, notamment TikTok, Pinterest, Snapchat ou Criteo, vous pourrez sélectionner vos partenaires en fonction de vos attributions d'achats de synchronisation d’audiences professionnelle dans la section **Audience Sync Pro** de la page **Partenaires technologiques**.

![Audience Sync Pro sans partenaires sélectionnés pour l'instant.][5]{: style="max-width:75%;"}

Tout d'abord, sélectionnez les partenaires que vous voulez utiliser en choisissant Sélectionner des partenaires. Chaque achat d'Audience Sync Pro vous permettra d'obtenir 3 destinations d’Audience Sync Pro, qui seront disponibles dans chacun de vos espaces de travail au sein de votre tableau de bord.

![Possibilité de sélectionner jusqu'à trois partenaires à connecter à Braze.][6]{: style="max-width:65%;"}

Après avoir sélectionné vos destinations Audience Sync Pro, connectez votre compte publicitaire partenaire sélectionné en cliquant sur la vignette des partenaires.

![Un exemple de Snapchat et TikTok sélectionnés comme partenaires pour Audience Sync.][7]{: style="max-width:70%;"}

![Audience Snapchat Synchronisez les paramètres avec le message : "Vous avez connecté avec succès 1 compte Snapchat".][9]{: style="max-width:70%;"}

Enfin, créez votre étape de canvas pour la synchronisation de l’audience en utilisant cette destination Audience Sync Pro.

### E-mails d'erreur de la synchronisation de l'audience

Si l'erreur est liée à l'intégration globale du partenaire (comme un problème d'autorisation), un e-mail est envoyé à l'utilisateur qui a connecté l'intégration. Si cet utilisateur n'existe plus, ce sont les administrateurs qui recevront les e-mails. 

Si l'erreur est liée à des problèmes avec le composant Audience Sync (tel que "Audience Does Not Exist") dans Canvas, un e-mail est envoyé à l'utilisateur qui a configuré le Canvas. Si cet utilisateur n'existe plus, il revient à l'administrateur de l'entreprise.

Pour configurer les destinataires de ces e-mails, contactez votre gestionnaire de satisfaction client pour ajouter des destinataires sous **Préférences de notification.** Comme cette fonctionnalité modifie le comportement actuel, vous devrez immédiatement ajouter des destinataires à cette nouvelle préférence de notification, car Braze ne propose pas d'abonnement par défaut, et vous assurer qu'aucun e-mail d'erreur n'est manqué.

## Considérations relatives à la confidentialité des données

{% alert important %}
Cette documentation n'a pas pour but de fournir des conseils juridiques et ne peut être considérée comme telle. L'utilisation de la fonction de synchronisation de l'audience est soumise à des exigences légales spécifiques. Pour vous assurer que vous l'utilisez en conformité avec toutes les lois applicables, vous devez demander l'avis de votre conseiller juridique.
{% endalert %}

Lorsque vous créez des audiences pour le suivi publicitaire, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et vous conformer aux lois sur la protection de la vie privée, telles que le droit "Ne pas vendre ou partager" en vertu de la [CCPA.](https://oag.ca.gov/privacy/ccpa) Les marketeurs devraient implémenter les filtres pertinents pour l'éligibilité des utilisateurs dans leurs critères d'entrée de canvas. Ci-dessous, nous listons quelques options.

Si vous avez collecté l'[IDFA iOS par le biais du SDK de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), vous pourrez utiliser le filtre " Suivi des publicités activé ". Sélectionnez la valeur `true` afin d'envoyer uniquement les utilisateurs vers les destinations de synchronisation d'audience où ils ont donné leur consentement.

![Un canvas dont l'audience d'entrée est "Ad Tracking Enabled is true".][2]

Si vous collectez `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, ou tout autre attribut personnalisé pertinent, vous devez les inclure dans les critères d'entrée de votre Canvas en tant que filtre :

![Un canvas dont l'audience d'entrée est "opted_in_marketing equals true".][1]

Pour en savoir plus sur la manière de se conformer à ces lois sur la protection des données au sein de la plateforme Braze, consultez l'[assistance technique sur la protection des données.]({{site.baseurl}}/dp-technical-assistance/)

## Gérer le consentement pour le ciblage publicitaire

En tant qu'annonceur, il vous incombe de gérer le consentement au suivi publicitaire ou au ciblage de vos utilisateurs.

Pour envoyer des publicités à vos utilisateurs, vous devez vous conformer à toutes les lois et réglementations applicables, ainsi qu'aux politiques et exigences de la plateforme publicitaire. N'utilisez Braze pour cibler et synchroniser les utilisateurs que lorsque vous avez obtenu leur consentement. 

Pour maintenir à jour vos listes d'audience dans ces plateformes publicitaires et supprimer les utilisateurs qui ont révoqué leur consentement, configurez un Canvas pour supprimer les utilisateurs de ces listes d'audience existantes à l'aide d'une étape de Synchronisation d'audience.


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