---
nav_title: Prise en charge de plusieurs magasins
permalink: "/shopify_multiple_store/"
hidden: true
---

# Prise en charge de plusieurs magasins Shopify

> Connectez plusieurs boutiques Shopify à un espace de travail unique grâce à notre nouvelle version bêta pour la prise en charge de plusieurs boutiques, afin d'avoir une vue holistique de vos clients sur tous les marchés. Créez et lancez des programmes d'automatisation et des parcours dans un espace de travail unique sans dupliquer les efforts sur plusieurs instances. 

{% alert important %}
La prise en charge de plusieurs boutiques Shopify est disponible en version bêta, laquelle peut contenir des bogues. Cette fonctionnalité est susceptible d'être modifiée au fur et à mesure du développement.
{% endalert %}

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Créer un [groupe d'abonnement e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#create-a-group) pour chaque magasin | Une fois le groupe d'abonnement par e-mail créé, vous le désignerez au magasin spécifique au cours de l'étape "[Collecte des abonnés par e-mail ou SMS]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#step-5-collect-email-or-sms-subscribers)" du processus de configuration.<br><br>Cette information est nécessaire pour vous permettre de savoir à quel groupe d'abonnement e-mail de votre magasin vos utilisateurs appartiennent, à des fins de conformité. |
| Auditer et mettre à jour les segments, les campagnes et les canvas à l'aide des attributs de Shopify. | Les attributs personnalisés collectés auprès de plusieurs magasins seront au format d'un objet imbriqué, ce qui diffère de la structure actuelle utilisée dans l'intégration globale de Shopify, qui est formatée sous la forme d'une valeur de chaîne de caractères. Par conséquent, vous devrez mettre à jour tous les segments, campagnes ou Canvas au nouveau format après avoir connecté plusieurs magasins pour utiliser le filtre "Attribut personnalisé imbriqué" ou mettre à jour l'événement déclencheur "Modifier l'attribut personnalisé".<br><br>Si vous n'utilisez aucun de ces attributs aujourd'hui, vous pouvez ignorer ceci. |
| Auditer et mettre à jour l'alias Shopify | L'alias `shopify_customer_id` sera migré vers {% raw %}`shopify_customer_id_{{storename}}`{% endraw %} si vous connectez plus d'un magasin. Veillez à mettre à jour tous les systèmes internes pour utiliser le nouvel alias. L'ancien alias, `shopify_customer_id`, sera supprimé. Si vous n'utilisez pas l'alias aujourd'hui, vous pouvez l'ignorer. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration
Grâce à la prise en charge de plusieurs magasins par Braze, vous pouvez :
- Disposer d'une vue à 360° de vos clients dans l'ensemble des boutiques
- Créez des segments de vos clients à l'aide des données agrégées de votre magasin. 
- Mettez en place des envois de messages ou des parcours au fur et à mesure que vos clients se déplacent dans les différents magasins.
- Gestion des abonnements aux e-mails et aux SMS dans différents magasins

{% alert important %}
La prise en charge de plusieurs marques dans un même espace de travail augmente la probabilité de profils utilisateurs en double, car les utilisateurs peuvent faire des achats d'une marque à l'autre. Nous vous suggérons de placer chaque marque dans son propre espace de travail.
{% endalert %}

### Création d'un magasin supplémentaire
1. Après avoir installé votre première boutique, sélectionnez l'option **\+ Connecter une nouvelle boutique.** <br>![][1]{: style="max-width:70%;"}<br><br>
2. Passez en revue le processus d'onboarding pour ce nouveau magasin. Vous trouverez plus de détails dans notre guide sur [la configuration de Shopify.]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/) <br><br>Notez que les paramètres du magasin précédent peuvent être reportés, mais vous pouvez les mettre à jour en conséquence au fur et à mesure que vous avancez dans votre onboarding.<br><br>
3. Pour l'étape de collecte des abonnés par e-mail ou SMS :
- Pour collecter correctement les abonnements aux e-mails et aux SMS pour chaque magasin, vous devez attribuer des groupes d'abonnement uniques à chaque configuration de magasin. 
- Nous vous suggérons de **ne pas** activer « Remplacer l'état global existant pour les utilisateurs » car cela peut entraîner le désabonnement global de vos clients s'ils ont interagi avec plusieurs de vos magasins.<br><br>
4. Répétez cette installation pour autant de magasins que nécessaire.<br><br>
5. Pour afficher l'intégration de chaque magasin et configurer les paramètres avancés, cliquez sur un magasin dans le menu déroulant :<br>![][2]{: style="max-width:70%;"}

## Données de Shopify

### Alias Shopify

{% raw %}Après avoir connecté plusieurs magasins, tous les utilisateurs entrants de Shopify auront un nouvel alias, `shopify_customer_id_{{storename}}` en plus de l'alias existant, `shopify_customer_id`. Notez que `shopify_customer_id` est un ancien alias et qu'il sera supprimé lorsque cette fonctionnalité sera disponible de manière générale. Pensez à procéder à la transition vers le nouvel alias. {% endraw %}

### Attributs personnalisés Shopify

Lorsque vous connectez plusieurs magasins, les attributs suivants sont synchronisés sous la forme d'un objet imbriqué qui contient la valeur par magasin et la valeur globale :
- `shopify_tags`
- `shopify_order_count` (uniquement disponible via le remplissage de l’historique)
- `shopify_total_spent` (uniquement disponible via le remplissage de l’historique)

Pour utiliser des événements personnalisés lors de la création ou de la modification d'un segment, sélectionnez le filtre **Attribut personnalisé imbriqué** et localisez votre attribut imbriqué. Pour vous aider à identifier le chemin ou le champ spécifique de l'objet, utilisez l'outil [Générer un schéma.]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#generate-schema) Après avoir sélectionné les attributs imbriqués, un champ avec un bouton plus apparaît à côté des attributs sélectionnés pour que vous puissiez spécifier le chemin d'accès. Pour en savoir plus sur les attributs imbriqués, voir [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/).

![3]{:style="max-width:70%;"}

Vous pouvez spécifier votre chemin en le tapant dans le champ ou en cliquant sur le bouton plus et en sélectionnant le chemin.

![4]{:style="max-width:70%;"}

### Événements personnalisés de Shopify

Après avoir connecté plus d'un magasin, les événements personnalisés de Shopify entrants contiendront désormais une nouvelle propriété d'événement, `shopify_storefront`. Reportez-vous au [traitement des données de Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_processing#supported-shopify-events) pour connaître tous les événements personnalisés pris en charge dans cette intégration. Cette propriété d'événement fournit le domaine de la boutique Shopify d'où provient l'événement.

### Livraison/distribution par événement ou suivi des conversions

Pour déclencher l'envoi de messages aux utilisateurs effectuant des actions auprès d'un magasin spécifique :

1. Accédez à l'étape **Planifier la livraison** de votre campagne.
2. Sélectionnez **Perform Custom Event** comme événement déclencheur.
![5]{:style="max-width:70%;"}
3. Sélectionnez un événement Shopify comme événement déclencheur, par exemple **shopify_created_order**, et la case à cocher **Ajouter des filtres de propriété**.
![6]{:style="max-width:70%;"}
4. Sélectionnez **Basic Property** dans la liste déroulante **Add Filter.** 
5. Sélectionnez **shopify_storefront** et saisissez le domaine Shopify complet de la boutique.
![7]{:style="max-width:70%;"}


### Fusion et synchronisation des utilisateurs de Shopify

Si l'ID client Shopify, l'adresse e-mail ou le numéro de téléphone de l'utilisateur existe déjà dans Braze à l'aide de l'alias, {% raw %}`shopify_customer_id_{{storefront_domain}}`, `shopify_email`, ou `shopify_phone`, {% endraw %}, nous mettrons alors à jour le profil utilisateur existant. Si ces alias n'existent pas dans Braze, nous créerons un nouveau profil utilisateur. Notez qu'il est possible que les données d'un utilisateur (par exemple, la ville) diffèrent entre plusieurs boutiques Shopify pour le même utilisateur. Dans ce cas, Braze mettra toujours à jour le profil utilisateur à partir de la boutique dont l'activité est la plus récente. 

{% alert warning %}
Braze mettra à jour le profil utilisateur avec les données clients Shopify du magasin dont l'activité est la plus récente. Cela signifie que tous les attributs, tels que l'e-mail, le numéro de téléphone, le téléphone d'envoi, la ville, etc. peuvent être remplacés par ceux du magasin avec l’activité la plus récente. Par exemple, si un utilisateur a un numéro de téléphone différent dans deux magasins différents, Braze mettra à jour le profil utilisateur avec le numéro de téléphone du magasin dont l'activité est la plus récente.
{% endalert %}

[1]: {% image_buster /assets/img/multiple_stores.png %}
[2]: {% image_buster /assets/img/multiple_stores2.png %}
[3]: {% image_buster /assets/img/shopify_nested_attributes.png %}
[4]: {% image_buster /assets/img/shopify_tags.png %}
[5]: {% image_buster /assets/img/shopify_add_trigger.png %}
[6]: {% image_buster /assets/img/shopify_select_event.png %}
[7]: {% image_buster /assets/img/shopify_enter_storefront.png %}
