{% if include.alert == 'User profile external_id' %}

{% alert warning %}
N'attribuez pas de `external_id` à un profil utilisateur avant de pouvoir l'identifier de manière unique. Une fois que vous avez identifié un utilisateur, vous ne pouvez plus le rendre anonyme.
<br><br>
Un site `external_id` peut être mis à jour en utilisant l'[endpoint`/users/external_ids/rename` ]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/). Toutefois, toute tentative de définir un autre `external_id` pendant la session d'un utilisateur créera un nouveau profil utilisateur auquel sera associé le nouveau `external_id`. Aucune donnée ne sera transmise entre les deux profils.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment Currents multiple connectors' %}

{% alert warning %}
Si vous avez l'intention de créer plusieurs connecteurs Currents identiques (par exemple, deux connecteurs d'événement d'engagement lié aux messages), ils doivent se trouver dans des espaces de travail différents. Étant donné que l'intégration Segment Currents Braze ne peut pas isoler les événements de différentes applications au sein d’un seul espace de travail, s’ils se trouvent dans un même espace, cela entraînera une déduplication inutile des données et des pertes de données.
{% endalert %}

{% endif %}

{% if include.alert == 'Canvas race condition audience trigger' %}

{% alert warning %}
Évitez de configurer une campagne ou un Canvas basé sur une action avec le même déclencheur que le filtre d'audience (comme un attribut modifié ou un événement personnalisé effectué). Une [condition de concurrence]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) peut se produire : l'utilisateur n'est pas dans l'audience au moment où il effectue l'événement déclencheur, ce qui signifie qu'il ne recevra pas la campagne ou n'entrera pas dans le Canvas.
{% endalert %}

{% endif %}
