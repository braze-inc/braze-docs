---
nav_title: Meilleures pratiques de collecte
article_title: Meilleures pratiques de collecte
page_order: 3.1
page_type: reference
description: "L'article suivant permet de clarifier les différentes méthodes et les meilleures pratiques pour la collecte de données sur les utilisateurs nouveaux et existants."

---

# Meilleures pratiques de collecte

> Savoir quand et comment collecter les données des utilisateurs connus et inconnus peut s'avérer difficile lorsque vous envisagez le cycle de vie du profil utilisateur de vos clients. Cet article aide à clarifier les différentes méthodes et les meilleures pratiques pour la collecte de données d'utilisateurs nouveaux et existants en vous guidant à travers un cas d'utilisation.

L'exemple suivant est un cas d'utilisation de la collecte d'e-mails, mais la logique s'applique à de nombreux scénarios de collecte de données différents. Dans cet exemple, nous supposons que vous avez déjà intégré un formulaire d'inscription ou un moyen de recueillir des informations sur les utilisateurs. 

Lorsqu'un utilisateur vous fournit des informations à enregistrer, nous vous recommandons de vérifier si les données existent déjà dans votre base de données et, le cas échéant, de créer un profil d'alias utilisateur ou de mettre à jour le profil d'utilisateur existant.

Si un utilisateur inconnu consulte votre site puis, à une date ultérieure, crée un compte ou s'identifie par le biais d'une inscription par e-mail, la fusion des profils doit être gérée avec précaution. En fonction de la méthode de fusion utilisée, les informations relatives aux utilisateurs alias uniquement ou les données anonymes peuvent être écrasées.

## Capturer les données de l'utilisateur à l'aide d'un formulaire web

### Étape 1 : Vérifier si l'utilisateur existe

Lorsqu'un utilisateur saisit un contenu au moyen d'un formulaire web, vérifiez si un utilisateur possédant cet e-mail existe déjà dans votre base de données. Il y a deux façons de procéder :

- **Vérifiez la base de données interne (recommandé) :** Si vous disposez d'un enregistrement ou d'une base de données externe contenant les informations fournies par l'utilisateur et existant en dehors de Braze, faites-y référence au moment de l'envoi de l'e-mail ou de la création du compte afin de confirmer que les informations n'ont pas déjà été saisies.
- **[`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/):** Utilisez `email` comme identifiant, et un nouveau profil utilisateur sera créé si l'adresse e-mail n'existe pas encore.

### Étape 2 : Enregistrement ou mise à jour de l'utilisateur

- **Si un utilisateur existe :**
  - Ne créez pas de nouveau profil.
  - Enregistrez un attribut personnalisé (par exemple, `newsletter_subscribed: true`) sur le profil de l'utilisateur pour indiquer que l'utilisateur a envoyé son e-mail dans le cadre d'un abonnement à la lettre d'information. S'il existe plusieurs profils utilisateurs Braze avec la même adresse e-mail, tous les profils seront exportés.<br><br>
- **Si un utilisateur n'existe pas :**
  - Créez un profil d'alias uniquement via l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Cet endpoint acceptera un [objet`user_alias` ]({{site.baseurl}}/api/objects_filters/user_alias_object/) et créera un profil d'alias uniquement lorsque `update_existing_only` est défini sur `false`. Définissez l'e-mail de l'utilisateur comme alias d'utilisateur pour faire référence à cet utilisateur à l'avenir (car l'utilisateur n'aura pas d'adresse `external_id`).

Diagramme montrant le processus de mise à jour d'un profil utilisateur alias d'utilisateur. Un utilisateur soumet son adresse e-mail et un attribut personnalisé, son code postal, sur une page d'atterrissage marketing. Une flèche pointant de la page de destination vers un profil d'utilisateur avec alias uniquement montre une requête API de Braze vers l'endpoint Suivre l'utilisateur, le corps de la requête contenant le nom et le libellé de l'alias, l'e-mail et le code postal de l'utilisateur. Le profil porte le libellé d'"alias utilisateur créé uniquement dans Braze" avec les attributs du corps de la demande pour montrer les données reflétées sur le profil nouvellement créé.]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## Capturer les e-mails des utilisateurs à l'aide d'un formulaire de capture d'e-mail

Utilisez un formulaire de capture d'e-mail pour inviter les utilisateurs à communiquer leur adresse e-mail, qui sera ajoutée à leur profil utilisateur. Pour plus d'informations sur la mise en place de ce formulaire, consultez le [formulaire de capture d'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/)
 
## Identification des alias d'utilisateurs uniquement

Lors de l'identification des utilisateurs à la création du compte, les utilisateurs à alias uniquement peuvent être identifiés et se voir attribuer un ID externe via l'[endpoint`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) en fusionnant l'utilisateur à alias uniquement avec le profil connu. 

Pour vérifier si un utilisateur est un alias uniquement, [vérifiez si l'utilisateur existe](#step-1-check-if-user-exists) dans votre base de données. 
- Si un enregistrement externe existe, vous pouvez appeler l'endpoint `/users/identify/`. 
- Si le [point de terminaison`/users/export/id` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) renvoie un `external_id`, vous pouvez appeler le point de terminaison `/users/identify/`.
- Si l'endpoint ne renvoie rien, il ne faut pas appeler `/users/identify/`.

## Capturer les données de l'utilisateur lorsque des informations sur l'utilisateur sous forme d'alias seulement sont déjà présentes

Lorsqu'un utilisateur crée un compte ou s'identifie par le biais d'une inscription par e-mail, vous pouvez fusionner les profils. Pour obtenir la liste des champs qui peuvent être fusionnés, reportez-vous à la section [Comportement de fusion des mises à jour.]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior)

### Fusionner des profils utilisateurs en double

Au fur et à mesure que vos données utilisateurs s'étoffent, vous pouvez fusionner les profils utilisateurs en double depuis le tableau de bord de Braze. Ces profils dupliqués doivent être trouvés à l'aide de la même requête de recherche. Pour plus d'informations sur la duplication des profils utilisateurs, consultez la rubrique [Fusionner les profils]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#merge-profiles).

Vous pouvez également utiliser l'[endpoint Fusionner les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) pour fusionner un profil utilisateur dans un autre. 

{% alert note %}
Une fois les profils utilisateurs fusionnés, cette action ne peut pas être annulée.
{% endalert %}

## Ressources complémentaires
- Consultez notre article sur le [cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) Braze pour plus de détails.<br>
- Consultez notre documentation sur la définition des ID utilisateur et l'appel de la méthode `changeUser()` pour [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#suggested-user-id-naming-convention) et le [Web.]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web)

