---
nav_title: Facebook Lead Ads via Zapier
article_title: Facebook Lead Ads via Zapier
description: "Cet article de référence présente l'intégration entre Braze et Facebook Lead Ads via Zapier pour automatiser le transfert des données des prospects de Facebook vers Braze, permettant ainsi un engagement en temps réel et des actions de suivi personnalisées."
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag: Partner

---

# Facebook Lead Ads via l'intégration de Zapier

> Grâce à l'intégration de Facebook Lead Ads via <a href="https://zapier.com/" target="_blank">Zapier</a>, vous pouvez importer vos leads de Facebook dans Braze et suivre un événement personnalisé lorsque les leads sont capturés. 

Facebook Lead Ads est un format publicitaire qui permet aux entreprises de collecter des informations sur les prospects directement dans Facebook. Ces annonces sont conçues pour rendre le processus de génération de prospects facile et homogène. En tirant parti d'une intégration Zapier et de Braze, vous pouvez automatiser le transfert des données des prospects de Facebook vers Braze, ce qui permet un engagement en temps réel et des actions de suivi personnalisées. 

## Conditions préalables

| Exigences | Description |
|---|---|
| Compte Zapier | Un compte Zapier est nécessaire pour bénéficier de ce partenariat. Cette intégration nécessite l'utilisation d'<a href="https://zapier.com/app/pricing/" target="_blank">apps Zapier premium</a>, vérifiez donc que votre plan Zapier donne accès aux apps premium. |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Accès à Facebook Leads</a> | L'accès à Facebook Leads est requis pour chaque compte publicitaire que vous prévoyez d'utiliser avec Braze. |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">Facebook Business Manager</a> | Dans le cadre de cette intégration, vous utiliserez Facebook Business Manager, un outil centralisé permettant de gérer les ressources Facebook de votre marque (par exemple, les comptes publicitaires, les pages et les applications). |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">Compte publicitaire Facebook</a> | Vous aurez besoin d'un compte publicitaire Facebook actif lié au gestionnaire de compte de votre marque. <br><br>Assurez-vous que vous disposez de l'autorisation "Gérer les comptes publicitaires" pour chaque compte publicitaire que vous prévoyez d'utiliser avec Braze, et que vous avez accepté les conditions générales de votre compte publicitaire. |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">Page Facebook</a> | Vous aurez besoin d'une page Facebook active liée au gestionnaire de votre marque. <br><br>Assurez-vous que vous disposez des autorisations "Gérer les pages" pour chaque page Facebook que vous envisagez d'utiliser avec Braze. |
| Endpoint REST Braze | Assurez-vous de connaître l'[URL de votre endpoint REST][1]. Votre endpoint API correspond à l'URL du tableau de bord de votre instance Braze. <br><br> Par exemple, si l'URL de votre tableau de bord est `https://dashboard-03.braze.com`, votre endpoint sera `dashboard-03`. |
| Clé d'API REST Braze | Assurez-vous que vous disposez d'une clé API REST Braze avec des autorisations `users.track`. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Créez une campagne Lead Ads avec un formulaire instantané

Depuis le gestionnaire de publicités Facebook, créez une <a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">campagne Facebook Leads et un formulaire Facebook Lead Ads.</a>

Vous pouvez utiliser une adresse e-mail ou un numéro de téléphone lorsque vous adressez une requête à l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour mettre à jour ou créer le profil utilisateur. Pour cette raison, incluez un **champ Contact** pour l'**e-mail** ou le **téléphone** dans votre formulaire d'annonce de prospects. Si vous collectez des prénoms ou des noms de famille, collectez-les séparément dans votre formulaire au lieu d'utiliser les noms complets.

### Étape 2 : Connectez votre compte Facebook à Zapier. 

#### Étape 2a : Sélectionnez votre méthode de connexion dans Zapier.

Dans Zapier, allez dans **Apps** pour rechercher les apps Facebook disponibles. Sélectionnez soit **Facebook Lead Ads**, soit **Facebook Lead Ads (pour les administrateurs d'entreprise)**.

Pour plus d'informations sur ces deux méthodes de connexion de votre compte Facebook à Zapier, reportez-vous à :

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Facebook Lead Ads (pour les administrateurs d'entreprise)</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">Annonces de prospects sur Facebook</a>

![][2]{: style="max-width:80%;"}

#### Étape 2b : Ajouter Zapier à Leads Access dans Facebook Business Manager

Dans votre gestionnaire Facebook Business, allez dans **Intégrations** > **Accès aux prospects** dans le menu de gauche. Sélectionnez votre page Facebook, puis cliquez sur **CRM**. Dans l'onglet CRM, sélectionnez **Attribuer des CRM** et ajoutez **Zapier**.

![][3]{: style="max-width:80%;"}

Pour connaître les étapes permettant d'affecter Zapier en tant qu'intégration CRM, reportez-vous à la <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862" target="_blank">documentation de</a> Facebook.

### Étape 3 : Créer votre processus d’automatisation

#### Étape 3a : Créer le déclencheur 

Une fois que vous avez connecté votre compte Facebook, vous pouvez procéder à la création d'un processus d’automatisation. Pour le **déclencheur**, sélectionnez **Facebook Lead Ads** ou **Facebook Lead Ads (pour les administrateurs d'entreprise)** en fonction de votre choix à l'étape 2. 

![][4]{: style="max-width:80%;"}

Pour l'**événement**, sélectionnez **Nouveaux prospects** > **Continuer.** 

![][5]{: style="max-width:80%;"}

Sélectionnez votre compte Facebook, puis **Continuer**. 

![][6]{: style="max-width:80%;"}

Sélectionnez votre page Facebook et le formulaire instantané que vous avez précédemment créé, puis **Continuer**.

![][7]{: style="max-width:80%;"}

Ensuite, testez ce déclencheur. Après avoir validé votre formulaire, sélectionnez **Continuer avec l'enregistrement sélectionné**.

#### Étape 3b : Créer une action

Ajoutez une nouvelle étape, puis sélectionnez **Webhooks par Zapier.** Ensuite, sélectionnez **requête personnalisée** pour le champ **Événement**, puis cliquez sur **Continuer.** 

![][8]{: style="max-width:80%;"}

Enfin, configurez votre requête personnalisée en insérant des champs dans votre charge utile. L'extrait de code suivant montre un exemple de charge utile. 

```
{
    "attributes": [
        {
            "email": "<insert_email_field>",
            "first_name": "<insert_first_name_field>",
            "last_name": "<insert_last_name_field>",
            "lead_form": "<insert_form_name_field>",
            "fb_campaign": "<insert_campaign_id_field>",
            "fb_ad_set": "<insert_campaign_id_field>",
            "fb_ad": "<insert_campaign_id_field>",
            "email_subscribe": "subscribed",
            "subscription_groups" : [{
                "subscription_group_id": "<subscription_group_id>",
                "subscription_state": "subscribed"
                }
            ]
        }
    ],
    "events": [
        {
            "email": "<insert_email_field>",
            "name": "<insert_custom_event_name>",
            "time": "<insert_timestamp_field>",
            "_update_existing_only": false
        }
    ]
}`
```

Voici un exemple de ce à quoi cela ressemble dans Zapier :

![][9]{: style="max-width:80%;"}

Après avoir configuré votre webhook, sélectionnez **Continuer et tester**. Si le test est concluant, vous pouvez publier votre processus d’automatisation.

### Étape 4 : Tester votre processus d’automatisation de publicités pour les prospects Facebook

Pour tester cela de bout en bout, utilisez l'outil de test des annonces de prospects de Facebook dans votre console de développement Facebook. Pour plus d'informations, reportez-vous à la section <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">Tests et résolution des problèmes</a>.

## Gestion de l'identité des utilisateurs

Cette intégration vous permet d'attribuer vos prospects Facebook par e-mail via l'[endpoint`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-phone-number).

* Si l'e-mail correspond à un profil utilisateur existant, Braze met à jour le profil avec les données des prospects Facebook.
* S'il existe plusieurs profils utilisateurs avec le même e-mail, Braze donnera la priorité au profil le plus récemment mis à jour avec un ID externe pour les mises à jour.
* Si l'ID externe n'existe pas, Braze donnera la priorité au profil le plus récemment mis à jour avec l'e-mail correspondant.
* Si aucun profil n'existe avec l'e-mail fourni, Braze créera un nouveau profil et un nouveau profil d'alias utilisateur sera créé. Pour identifier les profils utilisateurs alias nouvellement créés, utilisez l'[endpoint`/users/identify`.]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)

{% alert note %}
Vous pouvez également utiliser un numéro de téléphone ou un ID externe dans le cadre de la requête adressée à Braze si ces champs sont disponibles et s'il s'agit de l'identifiant principal que vous souhaitez pour l'intégration. Pour ce faire, modifiez la charge utile de votre requête comme indiqué dans l'[endpoint`/users/track`.]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
{% endalert %}

## Résolution des problèmes

{% details J'ai testé le déclencheur et l'action avec succès, alors pourquoi je ne parviens pas à publier mon processus d’automatisation Zapier ? %}
Pour utiliser cette intégration, vous devez disposer d'un <a href="https://zapier.com/app/pricing/" target="_blank">plan Zapier</a> prenant en charge les apps premium.
{% enddetails %}

{% details Pourquoi les prospects Facebook ne sont-ils pas synchronisés avec Braze ? %}
1. Vérifiez que vous disposez d'un accès administrateur à votre page Facebook, à votre compte publicitaire et d'un accès aux prospects. Ensuite, reconnectez votre compte dans Zapier.
2. Vérifiez que le formulaire instantané que vous avez créé dans Facebook mappe le formulaire sélectionné dans votre étape de déclencheur. 
3. Vérifiez que vous avez affecté Zapier à l'accès aux prospects en vous rendant dans **Facebook Business Manager** > **Intégrations** > **Accès aux prospects.**
{% enddetails %}

{% details Pourquoi y a-t-il des profils utilisateurs en double avec le même e-mail ? %}
Il existe différentes façons de créer et de gérer les profils utilisateurs dans Braze, en fonction du [cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle).

En fonction de vos processus internes et du moment où vous déclenchez la création de clients dans Braze, vous pouvez rencontrer des profils utilisateurs en double en raison d'une condition de concurrence entre le profil utilisateur créé par l'intégration et la création de l'utilisateur à partir de votre système. Vous pouvez [fusionner des profils utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) dans Braze.
{% enddetails %}

{% details Je n'ai pas de compte Zapier. Comment puis-je déclencher des webhooks Facebook Lead Ads dans Braze ? %}
Si vous n'utilisez pas Zapier et ne prévoyez pas de le faire, vous pouvez créer l'intégration directement depuis Facebook dans Braze. Pour plus d'informations, reportez-vous à la <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">documentation Lead Ads.</a>

Pour récupérer des prospects depuis Facebook, utilisez les <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">webhooks.</a> Consultez la <a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">documentation sur les webhooks</a> pour commencer à utiliser les webhooks dans Facebook.

Après avoir établi l'URL des webhooks dans Facebook, travaillez avec votre équipe pour déterminer le meilleur chemin pour transmettre les données à l'[endpoint`/users/track`.]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) De manière similaire à l'approche Zapier, nous vous recommandons d'effectuer une [requête par e-mail]({{site.baseurl}}/api/endpoints/user_data/post_user_track#example-request-for-updating-a-user-profile-by-phone-number) via l'endpoint `users/track`.
{% enddetails %}

{% alert tip %}
Pour plus de conseils de résolution des problèmes, consultez le <a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">guide de résolution des problèmes des prospects Facebook</a> de Zapier.
{% endalert %}


[1]: {{site.baseurl}}/api/basics/#api-definitions
[2]: {% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}
[3]: {% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}
[4]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}
[5]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}
[6]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}
[7]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}
[8]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}
[9]: {% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}