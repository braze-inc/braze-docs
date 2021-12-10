---
nav_title: Facebook
article_title: Exportation du public sur Facebook
alias: /fr/partners/facebook/
description: "Cet article décrit le partenariat entre Braze et Facebook, une plateforme sociale de premier plan pour les marques à atteindre et à engager avec leurs clients."
page_type: partenaire
search_tag: Partenaire
page_order: 1
---

# Exportation de l'audience Facebook

Braze fournit la possibilité d'exporter manuellement vos utilisateurs depuis la page Segments de Braze. Ceci est une exportation statique unique et ne créera que de nouveaux publics personnalisés Facebook.

Les cas d'utilisation courants pour exporter des audiences personnalisées Facebook comprennent :
- Redimensionner les utilisateurs à des points spécifiques de leur cycle de vie
- Créer des listes de ciblage d'exclusion
- [Audiences apparentes][4] pour acquérir de nouveaux utilisateurs plus efficacement <br><br>

{% alert note %}
L'export public de Facebook utilise le __jeton d'accès utilisateur__ pour autoriser les requêtes.<br><br> Si vous utilisez cette fonctionnalité à côté de la fonction [Synchronisation de l'audience vers Facebook]({{site.baseurl}}/audience_sync_facebook/) (actuellement en Beta), Braze utilisera par défaut le __System User Token__ plus fiable que vous avez déjà généré, pour autoriser les requêtes.
{% endalert %}

## Pré-requis

{% raw %}
| Exigences                                                      | Origine       | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gestionnaire d'entreprise Facebook                             | [Facebook][1] | Un outil centralisé pour gérer les actifs Facebook de votre marque (par exemple, comptes publicitaires, pages, applications).                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Compte publicitaire Facebook                                   | [Facebook][2] | Un compte de publicité Facebook actif lié au Business Manager de votre marque que vous souhaitez utiliser vos audiences personnalisées de Braze. <br><br> Veuillez vous assurer que votre administrateur Facebook Business Manager vous a accordé des autorisations d'administration aux comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze et que vous avez accepté les conditions générales de votre compte publicitaire. Sinon, vous ne serez pas en mesure d'accéder à des comptes publicitaires Facebook au Brésil. |
| Conditions d'utilisation des audiences personnalisées Facebook | [Facebook][3] | Vous avez accepté les conditions d'utilisation des audiences personnalisées de Facebook pour vos comptes publicitaires Facebook que vous prévoyez utiliser avec Braze.                                                                                                                                                                                                                                                                                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endraw %}

## Intégration

### Se connecter à Facebook

Dans le tableau de bord de Braze, allez dans __Partenaires Technologiques__ et sélectionnez __Facebook__. Dans le module d'exportation public Facebook, cliquez sur __Connecter Facebook__.

!\[Activer Facebook\]\[6\]{: style="max-width:70%;"}

Une fenêtre de dialogue oAuth Facebook apparaîtra pour autoriser Braze à créer des audiences personnalisées dans vos comptes publicitaires Facebook.

!\[Facebook Dialog\]\[8\]{: style="max-width:30%;"} !\[Facebook Dialog\]\[7\]{: style="max-width:40%;"}

Une fois que vous avez lié Braze à votre compte Facebook, vous serez alors en mesure de sélectionner les comptes de pub que vous souhaitez synchroniser au sein de votre groupe d'application Braze.

!\[Facebook Dialog\]\[9\]{: style="max-width:70%;"}

Une fois que vous serez connecté avec succès, vous serez ramené à la page du partenaire, où vous pouvez voir quels comptes sont connectés et déconnecter les comptes existants.

!\[Facebook Connected\]\[10\]{: style="max-width:70%;"}

Votre connexion Facebook sera appliquée au niveau du groupe d'applications Braze. Si votre administrateur Facebook vous supprime de votre Business Manager Facebook ou accède aux comptes Facebook connectés, Braze détectera un jeton non valide. Par conséquent, vos Canvases actifs en utilisant Facebook Audience Steps montreront des erreurs, et Braze ne sera pas en mesure de synchroniser les utilisateurs.

{% alert important %}
Pour les clients qui ont précédemment subi le processus de révision de l'application Facebook pour la [Gestion de la publicité](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) et [Accès Standard de la gestion des publicités](https://developers.facebook.com/docs/marketing-api/access#standard), votre jeton d'utilisateur système sera toujours valide pour l'étape d'audience Facebook. Vous ne serez pas en mesure de modifier ou de révoquer le jeton d'utilisateur du système Facebook via la page partenaire de Facebook. Au lieu de cela, vous pouvez connecter votre compte Facebook pour remplacer votre jeton d'utilisateur système Facebook dans votre groupe d'application Braze.

<br><br>La nouvelle configuration de Facebook oAuth s'appliquera également aux [exportations Facebook via Segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Exportation de vos utilisateurs vers Facebook

L'Exportation de l'Audience Facebook de Braze est accessible via la page Segments. Cliquez sur l'engrenage à côté du segment que vous souhaitez exporter. Puis cliquez sur __Exporter en tant que public Facebook__.

Si vous n'avez pas déjà activé Facebook au Brésil, il vous demandera d'aller sur la page Facebook Technology Partners dans le tableau de bord. Si vous avez déjà activé Facebook via __Partenaires technologiques > Facebook__, vous serez en mesure de sélectionner le champ utilisateur à exporter, et une liste déroulante pour sélectionner votre compte d'annonce Facebook s'affiche.

Il y a trois champs possibles que vous pouvez exporter :

- Courriel
- Périphérique IDFA
- Numéro de téléphone

{% alert note %}
Vous ne pouvez sélectionner qu'un seul champ utilisateur dans une seule exportation. Si vous choisissez plusieurs types de données, Braze créera un public personnalisé distinct pour chacun.
{% endalert %}

Une fois que vous avez sélectionné le champ utilisateur, cliquez sur le bouton __Exporter__. Similaire aux exportations CSV, vous recevrez un e-mail lorsque le segment aura fini d'exporter vers Facebook.

Vous pouvez voir le public personnalisé sur [Facebook Ads Manager][13].

{% alert important %}
Pour des raisons de confidentialité des utilisateurs, Facebook ne vous autorise pas à voir:

- Utilisateurs exacts qui ont été ajoutés avec succès à un Public Personnalisé. [En savoir plus.](https://www.facebook.com/business/help/112061095610075)
- Taille de l'Audience Personnalisée. [En savoir plus.](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### Audiences regardées

Une fois que vous avez exporté avec succès un segment en tant qu'Audience Facebook, vous pouvez créer des groupes supplémentaires en utilisant les [audiences Lookalike][4] de Facebook. Cette fonctionnalité examine la démographie, les intérêts et les autres attributs de votre public choisi et crée un nouveau public de personnes ayant des attributs similaires.
[6]: {% image_buster /assets/img/fb/afb_1.png %} [7]: {% image_buster /assets/img/fb/afb_2.png %} [8]: {% image_buster /assets/img/fb/afb_3. ng %} [9]: {% image_buster /assets/img/fb/afb_4.png %} [10]: {% image_buster /assets/img/fb/afb_5.png %}

[1]: https://www.facebook.com/business/help/113163272211510?id=180505742745347
[2]: https://www.facebook.com/business/help/910137316041095?id=420299598837059
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: https://www.facebook.com/business/help/164749007013531?id=401668390442328
[4]: https://www.facebook.com/business/help/164749007013531?id=401668390442328
[13]: https://www.facebook.com/ads/manager/audiences/manage/
