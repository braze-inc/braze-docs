---
nav_title: Facebook
article_title: "Exportation de l'audience Facebook"
alias: /partners/facebook/
description: "Cet article de référence décrit le partenariat entre Braze et Facebook, une plateforme de réseau social de premier plan permettant aux marques d'atteindre et d'engager leurs clients."
page_type: partner
search_tag: Partner

---

# Export de l’audience Facebook

> L'intégration de Braze et Facebook vous permet d'exporter manuellement vos segments Braze vers Facebook pour créer des audiences personnalisées Facebook. Il s'agit d'un export d'audience statique ponctuel qui ne crée que de nouvelles audiences personnalisées Facebook.

Les cas d'utilisation courants pour l'exportation des audiences personnalisées de Facebook incluent :
- Reciblage des utilisateurs à des points spécifiques de leur cycle de vie
- Création de listes de ciblage d'exclusion
- Création d’[audiences similaires](https://www.facebook.com/business/help/164749007013531?id=401668390442328) pour acquérir de nouveaux utilisateurs plus efficacement
<br><br>

{% alert note %}
L'export de l'audience Facebook utilise le **jeton d'accès utilisateur** pour autoriser les requêtes.<br><br>
Si vous utilisez cette fonctionnalité avec la fonctionnalité [Audience Sync to Facebook]({{site.baseurl}}/audience_sync_facebook/), Braze utilisera par défaut le **jeton d'utilisateur système** plus fiable que vous avez déjà généré, pour autoriser les requêtes.
{% endalert %}

{% alert note %}
Si vous participez au test des comptes de Meta Work en version bêta, assurez-vous de déconnecter et reconnecter votre compte à la [page partenaire Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook).
{% endalert %}

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| [Gestionnaire d’affaires Facebook](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | Un outil centralisé pour gérer les actifs Facebook de votre marque (par exemple, les comptes publicitaires, les pages, les applications). |
| [Compte publicitaire Facebook](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | Un compte publicitaire Facebook actif lié au gestionnaire d'entreprise de votre marque que vous souhaitez utiliser avec les audiences personnalisées de Braze.<br><br>Assurez-vous que votre gestionnaire d'entreprise Facebook vous a accordé les autorisations d'administrateur sur les comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze, et que vous avez accepté les termes et conditions de votre compte publicitaire. Sinon, vous ne pourrez accéder à aucun compte publicitaire Facebook dans Braze. |
| [Conditions des audiences personnalisées de Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php)| Vous devez accepter les conditions des audiences personnalisées de Facebook pour vos comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Connectez-vous à Facebook

1. Dans le tableau de bord de Braze, allez à **Intégrations de partenaires** > **Partenaires technologiques** et sélectionnez **Facebook**. 

{: start="2"}
2\. Dans le module d'exportation de l'audience Facebook, sélectionnez **Connecter Facebook**. <br><br>![Page partenaire technologique de Facebook dans la plateforme Braze.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Dans la fenêtre de dialogue oAuth de Facebook, autorisez Braze à créer des audiences personnalisées dans vos comptes publicitaires Facebook. <br><br>![La première boîte de dialogue Facebook vous invite à vous connecter en tant que X, X étant votre nom d'utilisateur Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![La deuxième boîte de dialogue Facebook vous demande l'autorisation de gérer les publicités de vos comptes publicitaires.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4\. Après avoir lié Braze à votre compte Facebook, sélectionnez les comptes publicitaires que vous souhaitez synchroniser dans votre espace de travail Braze. <br><br>![Liste des comptes publicitaires disponibles que vous pouvez connecter à Facebook.]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> Après vous être connecté, vous serez redirigé vers la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants. <br><br> ![Une version mise à jour de la page des partenaires technologiques de Facebook montrant que les comptes publicitaires ont été connectés avec succès.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Votre connexion Facebook est appliquée au niveau de l'espace de travail Braze. Si votre administrateur Facebook vous supprime de votre gestionnaire d'entreprise Facebook ou de l'accès aux comptes Facebook connectés, Braze détectera un jeton invalide. En conséquence, vos Canvases actifs utilisant des étapes d'audience Facebook afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs. 

{% alert important %}
Pour les clients qui ont déjà suivi le processus de révision de l'application Facebook pour [Gestion des publicités](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) et [Accès standard à la gestion des publicités](https://developers.facebook.com/docs/marketing-api/access#standard), votre jeton d'utilisateur système sera toujours valide pour l'étape de l'audience Facebook. Vous ne pourrez pas modifier ou révoquer le jeton d'utilisateur système Facebook via la page partenaire Facebook. Au lieu de cela, vous pouvez connecter votre compte Facebook pour remplacer votre jeton d'utilisateur système Facebook dans votre espace de travail Braze. 

<br><br>La nouvelle configuration oAuth de Facebook s'appliquera également aux [exportations Facebook via des segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Étape 2 : Exportez vos utilisateurs vers Facebook

Dans Braze, l'export de l'audience Facebook est accessible via la page **Segments**. 

1. Sur la page **Segments**, sélectionnez le segment que vous souhaitez exporter.
2. Sélectionnez **Données utilisateur**, puis sélectionnez **Exporter en tant qu'audience Facebook.** <br><br>![La section "Détails du segment" d'un segment dont les "Données utilisateur" sont sélectionnées pour afficher une liste déroulante d'options comprenant "Exporter en tant qu'audience Facebook".]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3\. Si vous n'avez pas encore activé Facebook dans Braze, vous serez invité à aller à la page des partenaires technologiques de Facebook dans le tableau de bord. Si vous avez déjà activé Facebook via **Partenaires technologiques** > **Facebook**, vous pourrez sélectionner votre compte publicitaire Facebook et les champs utilisateurs à exporter. <br><br> Il existe trois champs utilisateur possibles que vous pouvez exporter :
- IDFA de l’appareil
- Numéro de téléphone 
- E-mail

{% alert note %}
Vous ne pouvez sélectionner qu'un seul champ utilisateur dans une seule exportation. Si vous choisissez plusieurs types de données, Braze créera une audience personnalisée distincte pour chacun de ces types.
{% endalert %}

{: start="4"}
4\. Après avoir sélectionné le champ utilisateur, sélectionnez **Exporter segment.** Comme les exportations CSV, vous recevrez un e-mail lorsque le segment aura terminé l'exportation vers Facebook.
5\. Affichez l'audience personnalisée dans le [gestionnaire des publicités Facebook](https://www.facebook.com/ads/manager/audiences/manage/).

{% alert important %}
Pour des raisons de confidentialité des utilisateurs, Facebook ne vous permet pas de voir :

- Les utilisateurs exacts qui ont été ajoutés avec succès à une audience personnalisée. [En savoir plus.](https://www.facebook.com/business/help/112061095610075)
- La taille de l'audience personnalisée. [En savoir plus.](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### Configuration de votre exportation d'audience

Lors de la création d'audiences Facebook, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et afin de respecter les lois sur la confidentialité, telles que le droit « Ne pas vendre ou partager » en vertu du [CCPA](https://oag.ca.gov/privacy/ccpa). Les marketeurs devraient implémenter les filtres pertinents pour l'éligibilité des utilisateurs dans leurs critères d'entrée de canvas. Ci-dessous, nous listons quelques options. 

- Si vous avez collecté l'[IDFA iOS via le SDK Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), vous pourrez utiliser le filtre **Suivi des publicités activé**. Sélectionnez la valeur `true` afin d'envoyer uniquement les utilisateurs vers les destinations de synchronisation d'audience où ils ont donné leur consentement. 

![]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- Si vous collectez des opt-ins, des opt-outs, `Do Not Sell Or Share`, ou d'autres attributs personnalisés pertinents, vous devez les inclure dans vos critères d'entrée de canvas en tant que filtre : 

![Un canvas dont l'audience d'entrée est "opted_in_marketing" est égale à "true".]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### Audiences similaires

Une fois que vous avez exporté avec succès un segment en tant qu'audience Facebook, vous pouvez créer des groupes supplémentaires en utilisant les [audiences similaires](https://www.facebook.com/business/help/164749007013531?id=401668390442328) de Facebook. Cette fonctionnalité examine les données démographiques, les intérêts et d'autres attributs de votre audience choisie et crée une nouvelle audience de personnes ayant des attributs similaires.

