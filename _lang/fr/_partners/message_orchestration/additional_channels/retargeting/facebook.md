---
nav_title: Facebook
article_title: Exportation de l’audience Facebook
alias: /partners/facebook/
description: "Cet article de référence présente le partenariat entre Braze et Facebook, une plateforme sociale leader pour les marques qui s’engagent à atteindre leurs clients et à s’engager auprès de ceux-ci."
page_type: partner
search_tag: Partenaire
page_order: 1

---

# Exportation de l’audience Facebook

L’intégration Braze et Facebook vous permet d’exporter manuellement vos segments utilisateurs de Braze vers Facebook pour créer des audiences personnalisées dans Facebook. Il s’agit d’une exportation d’audience statique unique qui ne créera que de nouvelles audiences personnalisées dans Facebook.

Les cas d’utilisation courants pour synchroniser les audiences personnalisées dans Facebook comprennent :
- Recibler les utilisateurs à des points spécifiques de leur cycle de vie
- Créer des listes de ciblage d’exclusion
- [Audiences similaires][4] pour acquérir de nouveaux utilisateurs plus efficacement
<br><br>

{% alert note %}
L’exportation de l’audience Facebook utilise le **Jeton d’accès utilisateur** pour autoriser les demandes.<br><br>
Si vous utilisez cette fonctionnalité en même temps que la fonctionnalité [Audience Sync to Facebook]({{site.baseurl}}/audience_sync_facebook/) (actuellement en version bêta), Braze utilisera par défaut le **jeton d’utilisateur système** plus fiable que vous avez déjà généré, pour autoriser les demandes.
{% endalert %}

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| [Facebook Business Manager][1] | Un outil centralisé pour gérer les actifs Facebook de votre marque (p. ex., comptes publicitaires, pages, applications). |
| [Compte publicitaire Facebook][2] | Un compte publicitaire Facebook actif lié au directeur commercial de votre marque que vous souhaitez utiliser avec l’audience personnalisée de Braze.<br><br>Assurez-vous que votre administrateur commercial Facebook a accordé vos autorisations d’administrateur aux comptes publicitaires Facebook que vous prévoyez d’utiliser avec Braze, et que vous avez accepté les conditions générales de votre compte. Sinon, vous ne pourrez accéder à aucun compte publicitaire Facebook au sein de Braze. |
| [Conditions générales des audiences personnalisées de Facebook][3]| Vous devez accepter les Conditions générales des audiences personnalisées de Facebook pour vos comptes publicitaires Facebook que vous prévoyez d’utiliser avec Braze.|
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Connectez-vous à Facebook

Dans le tableau de bord de Braze, accédez à **Technology Partners (Partenaires technologiques)** et sélectionnez **Facebook**. Dans le module Facebook Audience Export, cliquez sur **Connect Facebook (Connecter Facebook)**.

![Page de partenaire technologique de Facebook sur la plateforme Braze.][6]{: style="max-width:70%;"}

Une boîte de dialogue de Facebook oAuth apparaît pour autoriser Braze à créer des audiences personnalisées dans vos comptes publicitaires Facebook.

![La première boîte de dialogue Facebook invitant à se « Connecter comme X », où X est votre nom d’utilisateur Facebook.][8]{: style="max-width:30%;"}  ![La deuxième boîte de dialogue de Facebook vous demandant l’autorisation de gérer les publicités pour vos comptes publicitaires.][7]{: style="max-width:40%;"}

Une fois que vous avez lié Braze à votre compte Facebook, vous pourrez sélectionner les comptes publicitaires que vous souhaitez synchroniser au sein de votre groupe d’apps Braze. 

![Une liste des comptes publicitaires disponibles que vous pouvez connecter à Facebook.][9]{: style="max-width:70%;"}

Une fois que vous vous êtes connecté avec succès, vous serez ramené à la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![Version mise à jour de la page des partenaires de technologies de Facebook montrant les comptes publicitaires connectés avec succès.][10]{: style="max-width:70%;"}

Votre connexion à Facebook sera appliquée au niveau du groupe d’apps dans Braze. Si votre administrateur Facebook vous retire de votre Facebook Business Manager ou vous retire l’accès aux comptes Facebook connectés, Braze détectera un jeton non valide. Par conséquent, vos Canvas actifs utilisant des étapes d’audience Facebook afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs. 

{% alert important %}
Pour les clients qui ont déjà passé le processus d’examen de l’application Facebook pour [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) et [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard), votre jeton d’utilisateur système sera toujours valable pour l’étape de l’audience Facebook. Vous ne pourrez pas modifier ou révoquer le jeton d’utilisateur du système Facebook via la page partenaire Facebook. Au lieu de cela, vous pouvez connecter votre compte Facebook pour remplacer votre jeton d’utilisateur du système Facebook dans votre groupe d’apps de Braze. 

<br><br>La nouvelle configuration de Facebook oAuth s’appliquera également aux [exportations de Facebook via les segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites). 
{% endalert %}

### Exportation de vos utilisateurs dans Facebook

L’exportation de l’audience Facebook de Braze est accessible via la page **Segments**. Cliquez sur l’engrenage à côté du segment que vous souhaitez exporter. Puis cliquez sur **Export as Facebook Audience (Exporter en tant que Facebook Audience)**.

![Une liste de segments Braze. Pour le premier segment, le symbole de configuration est sélectionné et le bouton « Export as Facebook Audience » (Exporter en tant que Facebook Audience) est affiché.][11]

Si vous n’avez pas encore activé Facebook dans Braze, vous serez invité à vous rendre sur la page de partenaire technologique de Facebook dans le tableau de bord. Si vous avez déjà activé Facebook par le biais de **Technology Partners > Facebook**, vous pourrez sélectionner le champ utilisateur à exporter, et une liste déroulante permettant de sélectionner votre compte publicitaire Facebook s’affichera.

Il existe trois champs d’utilisateur possibles que vous pouvez exporter :  

- E-mail
- IDFA de l’appareil
- Numéro de téléphone

{% alert note %}
Vous ne pouvez sélectionner qu’un seul champ utilisateur dans une exportation. Si vous choisissez plus d’un type de données, Braze créera une audience personnalisée distincte pour chacun.
{% endalert %}

Une fois que vous avez sélectionné le champ utilisateur, cliquez sur le bouton **Export (Exporter)**. Comme pour les exportations CSV, vous recevrez un e-mail lorsque l’exportation du segment vers Facebook sera terminée.

Vous pouvez visualiser l’audience personnalisée dans [Facebook Ads Manager (Gestionnaire publicitaire Facebook)][13].

{% alert important %}
Pour des raisons de confidentialité des utilisateurs, Facebook ne vous permet pas de voir :

- Les utilisateurs qui ont été ajoutés avec succès à une audience personnalisée. [En savoir plus.](https://www.facebook.com/business/help/112061095610075)
- La taille de l’audience personnalisée. [En savoir plus.](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### Configurer l’exportation de votre audience

Lorsque vous créez des audiences Facebook, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences et afin de respecter les lois sur la confidentialité, telles que le droit « Ne pas vendre ou partager » en vertu du [CCPA](https://oag.ca.gov/privacy/ccpa). Les marketeurs doivent mettre en œuvre les filtres pertinents pour l’éligibilité des utilisateurs dans leurs critères d’entrée Canvas. Nous énumérons quelques options ci-dessous. 

Si vous avez collecté l’[IDFA iOS via le SDK Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), vous pourrez utiliser le filtre **Ads Tracking Enabled (Suivi des publicités activé)**. Sélectionnez la valeur `true` pour envoyer uniquement les utilisateurs vers les destinations de synchronisation d’audience auxquelles ils sont abonnés. 

![][16]{: style="max-width:75%;"}

Si vous recueillez des « abonnements », des « désabonnements », des « Ne pas vendre ou partager » ou tout autre attribut personnalisé pertinent, vous devez les inclure dans vos critères d’entrée Canvas comme filtre :

![Un Canvas avec une audience d’entrée de « opted_in_marketing » correspond à « true ».][15]{: style="max-width:75%;"}


#### Audiences similaires

Une fois que vous avez réussi à exporter un segment en tant qu’audience Facebook, vous pouvez créer des groupes supplémentaires à l’aide des [Audiences similaires][4] de Facebook. Cette fonctionnalité examine les données démographiques, les intérêts et autres attributs de votre audience choisie et crée une nouvelle audience de personnes ayant des attributs similaires.

[1]: https://www.facebook.com/business/help/113163272211510?id=180505742745347
[2]: https://www.facebook.com/business/help/910137316041095?id=420299598837059
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: https://www.facebook.com/business/help/164749007013531?id=401668390442328
[6]: {% image_buster /assets/img/fb/afb_1.png %}
[7]: {% image_buster /assets/img/fb/afb_2.png %}
[8]: {% image_buster /assets/img/fb/afb_3.png %}
[9]: {% image_buster /assets/img/fb/afb_4.png %}
[10]: {% image_buster /assets/img/fb/afb_5.png %}
[11]: {% image_buster /assets/img/fb/afb_6.png %}
[13]: https://www.facebook.com/ads/manager/audiences/manage/
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
