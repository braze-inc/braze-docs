---
nav_title: Archives utilisateur
article_title: Archives utilisateur
permalink: /user_archival/
page_order: 0
page_type: reference
description: "Cet article de référence décrit les définitions d’archivage des utilisateurs, le blocage des courriers indésirables et comment personnaliser la politique d’archivage."

---
# Archives utilisateur

> Chaque semaine, le dimanche à 5 h 30 EST, Braze exécute un processus visant à supprimer les utilisateurs inactifs et dormants dans les services Braze. Notez que Braze n’archive pas les utilisateurs à moins que le nombre d’utilisateurs de l’espace de travail n’atteigne le seuil de 250 000. 

Ce processus a pour but d'aider Braze à fournir des statistiques précises concernant les audiences atteignables dans le cadre de la campagne. Il sert également à respecter deux concepts clés du [RGPD][1]:

1. Le principe de limitation du stockage : les données personnelles traitées et stockées ne doivent pas être conservées plus longtemps que nécessaire
2. Il faut avoir un objectif commercial légitime pour traiter les données personnelles.

C’est-à-dire que les données à caractère personnel traitées et conservées ne doivent être conservées plus longtemps que nécessaire et que les données personnelles ne doivent être traitées qu’à des fins professionnelles légitimes. Les utilisateurs archivés auront également leur statut de désabonnement supprimé conformément au RGPD.

{% alert note %} Les clients ont un contrôle total sur le fait qu'un utilisateur soit inactif ou dormant. Braze Canvas offre la possibilité de le faire automatiquement, ce qui vous permet de désactiver efficacement cette fonctionnalité pour certains ou pour tous vos utilisateurs inactifs ou dormants. {% endalert %}

## Définitions des archives utilisateur

### Utilisateurs actifs

Braze définit un " utilisateur actif " pour une période donnée comme tout utilisateur qui a enregistré une session dans une application mobile ou un site web, qui a été mis à jour, qui a reçu un message ou qui a interagi avec un message.

Si vous définissez des ID utilisateur pour identifier les utilisateurs lorsqu’un nouvel utilisateur se connecte, il sera compté comme un utilisateur actif séparé. Les utilisateurs mis à jour via l’API seront également comptés comme utilisateurs actifs dans la période où ils ont été mis à jour.

{% alert important %}
Les utilisateurs inactifs et les utilisateurs dormants seront archivés, sauf si l'utilisateur est exclu de l'archivage pour les raisons énumérées ci-dessous.
{% endalert %}

### Utilisateurs inactifs

Les utilisateurs inactifs sont des utilisateurs qui ne sont pas joignables et qui sont probablement perdus. Les utilisateurs inactifs sont ceux qui répondent à tous ces critères :

- Ne peuvent pas recevoir un e-mail. Par exemple, ils n’ont pas d’adresse e-mail ou ils sont désabonnés à toutes les listes de diffusion.
- Ne peuvent pas recevoir de SMS. Par exemple, ils n’ont pas de numéro de téléphone valide, ou ils sont désabonnés de tous les groupes d’abonnement SMS.
- Ne peuvent pas recevoir des notifications push. Par exemple, ils ont désinstallé l’application ou désactivé la notification push dans les autorisations.
- Impossible de recevoir un message WhatsApp. Par exemple, ils n'ont pas de numéro de téléphone valide ou sont désabonnés de tous les groupes d'abonnement WhatsApp.
- Impossible de recevoir un message LINE. Par exemple, ils n'ont pas d'ID LINE ou sont désabonnés de tous les groupes d'abonnement LINE.
- Je n'ai pas utilisé d'application mobile ni visité de site web dans un espace de travail depuis plus de six mois.
- Je n'ai reçu aucun message d'un espace de travail depuis plus de six mois.
- Ils n'ont pas été mis à jour depuis plus de six mois.

Dans ce cas, ces utilisateurs ne peuvent pas être recevoir de communications et ils ne s’engagent pas avec votre marque. Dans les faits, ces utilisateurs se sont désabonnés.

### Utilisateurs dormants

Les utilisateurs dormants sont des utilisateurs qui n’ont pas eu d’activité au cours des douze derniers mois et :

- Vous n'avez pas utilisé d'application mobile ni visité de site web dans un espace de travail depuis plus de 12 mois.
- Je n'ai pas reçu de messages d'un espace de travail depuis plus de 12 mois.
- N'ont pas été mises à jour depuis plus de 12 mois.

## Utilisateurs du groupe de contrôle global

Les utilisateurs du groupe de contrôle global ne seront jamais archivés, même s'ils répondent à la définition d'utilisateurs inactifs ou dormants. 

### Groupe d’échantillons de traitement

Les utilisateurs du groupe de contrôle global dans un rapport sur le groupe de contrôle global sont exclus de l'archivage.

## Utilisateurs test

Les utilisateurs test ne seront jamais archivés, même s'ils répondent à la définition d'utilisateurs inactifs ou dormants.

## Filtrage du spam

Braze bloque les utilisateurs individuels avec plus de 5 millions de sessions (« utilisateurs factices »), et n’ingère plus leurs événements SDK, car ils sont généralement le résultat d’une intégration incorrecte. Si vous constatez que cela s'est produit pour un utilisateur légitime, ouvrez un ticket auprès de l'[assistance]({{site.baseurl}}/braze_support/) Braze.

Pour trouver les utilisateurs factices dans votre tableau de bord, procédez comme suit :

1. Créez un [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).
2. Sélectionnez le filtre `Session Count` et de l’appliquer à `more than 5,000,000`.
3. Exportez le segment via CSV.

Si nécessaire, vous pouvez supprimer les utilisateurs via l'[endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).

[1]: {{site.baseurl}}/dp-technical-assistance/#the-right-to-erasure
[2]: {% image_buster /assets/img_archive/user_archival_policy1.png %}
[3]: {% image_buster /assets/img_archive/user_archival_policy2.png %}
[4]: {% image_buster /assets/img_archive/user_archival_policy3.png %}

## Personnaliser votre politique d’archivage de l’utilisateur

Braze propose des fonctionnalités d'orchestrations de données qui vous permettent de personnaliser votre politique d'archivage de l'utilisateur. Créez une politique d'archivage des utilisateurs qui vous offre le meilleur des deux mondes avec le composant Canvas [User Update]({{site.baseurl}}/user_update/).

Ceci vous permet de :

- Vous conformer au RGPD et aux bonnes pratiques en matière de confidentialité en supprimant les profils utilisateurs qui ne sont plus importants.
- Conserver tous les profils utilisateurs dont vous avez vraiment besoin pour vos affaires.

### Étapes

1. Ciblez les utilisateurs qui répondent aux critères d'archivage de votre marque et que vous souhaitez conserver. Par exemple, vous pouvez conserver les utilisateurs qui
    - Le dernier message reçu remonte à plus de 23 semaines ou vous n'avez jamais reçu de message.<br>ET<br>
    - Dernière utilisation de votre application il y a plus de 23 semaines ou aucune session dans votre application<br><br>
      ![Cibler des utilisateurs qui ont reçu un message il y a plus de 23 semaines, n’ont jamais reçu un message d’une campagne ou d’une étape de Canvas, a utilisé ces applications il y a plus de 23 semaines et ont utilisé ces applications exactement zéro fois.][2]<br><br>
2. Définissez la rééligibilité pour être d’un peu moins de 6 mois.<br><br>
      ![Les contrôles d’entrée avec la rééligibilité activée et sa fenêtre définie sur 23 semaines.][3]<br><br>
3. Configurez l'étape de mise à jour de l'utilisateur pour ajouter un événement à chaque profil.<br><br>
      ![Étape de mise à jour de l'utilisateur qui ajoute l'événement "do_not_archive" au profil de l'utilisateur.][4]
{% details Exemple d'objet Mise à jour utilisateur %}

{% raw %}
```json
{
    "events": [
        {
            "name": "do_not_archive",
            "time": "{{ 'now' | time_zone: 'UTC' | date: '%Y-%m-%dT%H:%M:%SZ' }}"
        }
    ]
}
```
{% endraw %}

{% enddetails %}
