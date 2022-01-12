---
nav_title: Synchronisation de l'audience vers Google
article_title: Synchronisation de l'audience sur les toiles avec Google
alias: /synchronisation_google_audience/
description: "Cet article de référence couvrira comment utiliser Braze Audience Sync à Google, pour livrer des publicités basées sur les déclencheurs comportementaux, la segmentation et plus encore."
Tool:
  - Toile
---

# Synchronisation de l'audience vers Google

L'intégration de Braze Audience Sync à Google permet aux marques d'étendre la portée de leurs trajets clients inter-canaux à Google Search, Google Shopping, Gmail, YouTube et Google Display. En utilisant les données de vos clients de première partie, vous pouvez livrer des publicités en toute sécurité en fonction des déclencheurs de comportement, de la segmentation et plus encore. Tous les critères que vous utilisez généralement pour déclencher un message (par exemple, push, email, SMS, etc.). dans le cadre d'un Braze Canvas peut être utilisé pour déclencher une publicité pour cet utilisateur via [Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en) de Google.

Les cas d'utilisation courants pour la synchronisation des audiences personnalisées comprennent :
- Cibler les utilisateurs de grande valeur via plusieurs canaux pour générer des achats ou des engagements.
- Recibler les utilisateurs qui sont moins réceptifs aux autres canaux de marketing.
- Créer des publics de suppression pour empêcher les utilisateurs de recevoir des publicités alors qu'ils sont déjà des consommateurs loyaux de votre marque.
- Créer des audiences similaires pour acquérir de nouveaux utilisateurs plus efficacement.

{% alert note %}
Cette fonctionnalité permet aux marques de contrôler quelles données spécifiques sont partagées avec Google. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager vos données personnelles sont prises en considération au plus haut point. Pour en savoir plus sur notre politique de confidentialité des données de Braze, veuillez cliquer [ici](https://www.braze.com/privacy).
{% endalert %}

## Intégration

### Exigences d'intégration

Vous devrez vous assurer que vous avez créé et/ou complété les éléments suivants avant de configurer votre étape Google Audience dans Canvas.

| Exigences                    | Origine                                                              | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Google Annonces       | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Un compte Google pubs actif pour votre marque.<br><br>Si vous cherchez à partager un public sur plusieurs comptes gérés, vous pouvez télécharger vos audiences dans votre compte [gestionnaire](https://support.google.com/google-ads/answer/6139186).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Correspondance client Google | [Google](https://support.google.com/google-ads/answer/6299717)       | Le match client n'est pas disponible pour tous les annonceurs.<br><br>__Pour utiliser la correspondance client, votre compte doit avoir:__<br>• Une bonne histoire de conformité à la politique<br>• Un bon historique de paiement<br>• Au moins 90 jours d'historique dans Google Ads<br>• Plus de 50 USD, 00 durées de vie totales. Pour les annonceurs dont les comptes sont gérés dans des devises autres que les USD, votre montant de dépense sera converti en USD en utilisant le taux de conversion mensuel moyen pour cette devise.<br><br>Si votre compte ne répond pas aux critères ci-dessus, votre compte est actuellement inéligible à utiliser la correspondance client.<br><br>Veuillez discuter avec votre représentant Google Ads pour plus de conseils sur la disponibilité de la correspondance client pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Processus d'implémentation
### Étape 1 : Connecter un compte Google
Pour commencer, allez dans l'onglet **Google Ads** de la page **Technology Partners** et sélectionnez __Connect Google Ads__.

!\[Google Sync\]\[1\]

Vous serez ensuite invité à sélectionner le courriel associé à votre compte Google Ads et à accorder à Braze l'accès à votre compte Google Ads.

Notez que Braze ne gérera que vos auditoires.

!\[Google Sync\]\[2\]{: style="max-width:30%;"} !\[Google Sync\]\[3\]{: style="max-width:29%;"}

Une fois que vous aurez connecté votre compte Google Ads, vous serez renvoyé à votre page partenaire Google Ads au Brésil.

!\[Google Sync\]\[4\]

{% alert important %}
Si vous prévoyez d'exporter des IDFA iOS ou Google Advertising IDs dans la synchronisation de votre audience, Google nécessite votre ID d'application iOS et votre ID d'application Android dans les requêtes. Dans le module de synchronisation Google Audience, sélectionnez __Ajouter des identifiants de publicité mobile__, saisissez l'ID de votre application iOS et l'ID de l'application Android (nom du package de l'application), et enregistrez chacun.

![Synchronisation Google]({% image_buster /assets/img/google_sync/google_sync5.png %})
{% endalert %}

### Étape 2 : Ajouter une étape Google Audience dans Canvas

Ajoutez une étape dans votre Canvas, sélectionnez le menu déroulant en haut de l'étape et sélectionnez l'étape __Google Audience__.

!\[Google Sync\]\[6\]

### Étape 3 : Configuration de la synchronisation

Cliquez sur le bouton __Audience personnalisée__ pour ouvrir l'éditeur d'étape.

Sélectionnez le compte Google ad désiré. Sous la liste déroulante __Choisir une nouvelle audience ou une audience existante__ , tapez le nom d'un public nouveau ou existant.

{% tabs %}
{% tab Create a New Audience %}
__Créer une nouvelle audience__<br> Entrez un nom pour le nouveau public personnalisé, sélectionnez __Ajouter des utilisateurs à l'audience__ et sélectionnez les données du champ utilisateur à envoyer avec votre public. Vous pouvez choisir :
- __Informations de contact client__ qui contiendront l'e-mail et/ou les numéros de téléphone de vos utilisateurs s'ils existent dans Braze
- __Identifiant de l'annonceur mobile__ que vous devrez ensuite sélectionner soit iOS IDFA soit Android GAID

Ensuite, enregistrez votre audience en cliquant sur le bouton __Créer un public__ en bas de l'éditeur d'étape.

![Synchronisation Google]({% image_buster /assets/img/google_sync/google_sync7.png %})

Les utilisateurs seront avertis en haut de l'éditeur d'étapes si le public est créé avec succès ou si des erreurs surviennent au cours de ce processus. Les utilisateurs peuvent référencer ce public pour le retrait des utilisateurs plus tard dans le voyage de Canvas parce que le public a été créé en mode brouillon.

![Synchronisation Google]({% image_buster /assets/img/google_sync/google_sync9.png %})

Lorsque vous lancez une toile avec un nouveau public, Braze créera un nouveau public personnalisé lors du lancement de Canvas et par la suite synchronisera les utilisateurs en temps quasi réel au moment où ils entreront dans le pas de Google Audience.

{% alert important %}
Compte tenu des exigences du Match Client de Google, vous ne pouvez pas avoir les coordonnées du client et les identifiants de l'annonceur mobile dans les mêmes listes de clients. Google Customer Match utilisera ensuite ces informations pour déterminer qui peut être ciblé dans Google Search, Google Display, YouTube et Gmail. Pour plus de détails sur les conditions du Match Client Google, veuillez consulter leur [documentation](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Sync with an Existing Audience %}
__Synchroniser avec une Audience Existante__<br> Braze offre également la possibilité d'ajouter ou de supprimer des utilisateurs des listes de clients Google existantes pour s'assurer que ces audiences sont à jour. Pour synchroniser avec un public existant, sélectionnez un public personnalisé existant à synchroniser, puis choisissez si vous voulez __Ajouter à l'auditoire__ ou __Retirer du public__. Braze va alors soit ajouter ou supprimer des utilisateurs en temps quasi réel au moment où ils entrent dans le pas d'audience Google.

Une fois que vous avez configuré votre étape Google Audience, sélectionnez __Terminé__. Votre étape Google Audience inclura des détails sur le nouveau public.

![Synchronisation Google]({% image_buster /assets/img/google_sync/google_sync8.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Lancez Canvas

Complétez le reste de votre voyage utilisateur dans Canvas puis lancez ! Si vous avez choisi de créer un nouveau public, Braze créera d'abord le public au sein de Google, puis ajoutera des utilisateurs au fur et à mesure qu'ils atteignent cette étape dans votre Canvas. Si vous avez choisi d'ajouter ou de supprimer des utilisateurs d'un public existant, Braze ajoutera ou supprimera des utilisateurs quand ils atteindront cette étape dans leur voyage utilisateur.

Les utilisateurs passeront ensuite à l'étape suivante du Canvas s'il y en a une ou quitteront le Canvas s'il s'agit de la dernière étape.

## Synchronisation des utilisateurs et limites de taux

Au fur et à mesure que les utilisateurs atteignent l'étape de Synchronisation Audience, Braze synchronisera ces utilisateurs en temps quasi réel tout en respectant les limites de taux de l'API Google Ads. Cela signifie en pratique que Braze essaiera de traiter autant d'utilisateurs toutes les 5 secondes avant d'envoyer ces utilisateurs à Google.

Une fois qu'un client est sur le point d'atteindre la limite de taux de l'API Google Ads, Google fournira des commentaires à Braze sur les recommandations de réessai. Si un client Braze atteint sa limite de taux, Braze le Canvas réessaiera la synchronisation pendant jusqu'à &#126;13 heures. Si la synchronisation n'est pas possible, ces utilisateurs sont répertoriés sous la métrique Utilisateurs erronés.

## Comprendre les analyses
<br>
__Entré__: Nombre d'utilisateurs qui sont entrés dans cette étape pour être synchronisés avec Google.

__Procédé à l'étape suivante__: Combien d'utilisateurs ont avancé à l'étape suivante s'il y en a une. Tous les utilisateurs vont progresser automatiquement. 0 si c'est la dernière étape dans la branche Canvas .

__Utilisateurs synchronisés__: Nombre d'utilisateurs qui ont été correctement synchronisés avec Google.

__Utilisateur non synchronisé__: Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants à correspondre.

__Utilisateurs Erreur__: Nombre d'utilisateurs qui n'ont pas été synchronisés à Google à cause d'une erreur, après &#126;13 heures de tentatives. Pour des erreurs spécifiques, comme les perturbations du service API Google Ads, Canvas réessaiera la synchronisation jusqu'à &#126;13 heures. Si la synchronisation n'est pas encore possible à ce stade, l'utilisateur ne sera pas synchronisé.

__Utilisateurs en attente__: Nombre d'utilisateurs actuellement traités par Braze pour se synchroniser avec Google.

__Toile Sortie__: Nombre d'utilisateurs qui ont quitté le Canevas. Cela se produit lorsque la dernière étape dans une Canvas est une étape Google.

## Dépannage
{% détails Pourquoi ne puis-je pas sélectionner plusieurs champs dans ma configuration Google Audience Step ? %}
Google Customer Match a des exigences strictes en ce qui concerne la façon dont ces audiences sont formatées et les informations sur les clients sont incluses. Plus précisément, les identifiants des annonceurs mobiles doivent être téléchargés séparément des informations de contact du client (c.-à-d. courriel et numéro de téléphone). Veuillez vous référer à [la documentation de Google sur le match client](https://support.google.com/google-ads/answer/7659867?hl=en#undefined) pour plus de détails.
{% enddetails %}

{% de détails Combien de temps faudra-t-il pour synchroniser mon public sur Google ? %}
Il peut prendre entre 6 et 12 heures pour qu'un public soit synchronisé sur Google.
{% enddetails %}

{% des détails, j'ai synchronisé un public, mais la taille du public dans Google est zéro. %}
À des fins de confidentialité, la taille de la liste des utilisateurs s'affichera comme zéro jusqu'à ce que la liste ait au moins __1 000 membres__. Après cela, la taille sera arrondie aux deux chiffres les plus significatifs.
{% enddetails %}

{% de détails que j'ai synchronisé un public sur Google, mais mes annonces ne servent pas. %}
Vérifiez que vos audiences contiennent au moins __5 000__ utilisateurs pour vous assurer que les publicités commencent à servir.
{% enddetails %}
[1]: {% image_buster /assets/img/google_sync/google_sync1.png %} [2]: {% image_buster /assets/img/google_sync/google_sync2.png %} [3]: {% image_buster /assets/img/google_sync/google_sync3. ng %} [4]: {% image_buster /assets/img/google_sync/google_sync4.png %} [6]: {% image_buster /assets/img/google_sync/google_sync6. ng %} [8]: {% image_buster /assets/img/google_sync/google_sync8.png %}
