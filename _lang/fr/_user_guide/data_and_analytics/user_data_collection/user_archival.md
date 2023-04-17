---
nav_title: Archives utilisateur
article_title: Archives utilisateur
page_order: 0
page_type: reference
description: "Cet article de référence décrit les définitions d’archivage des utilisateurs, le blocage des courriers indésirables et comment personnaliser la politique d’archivage."

---
# Archives utilisateur

> Chaque semaine, le dimanche à 5 h 30 EST, Braze exécute un processus visant à supprimer les utilisateurs inactifs et dormants dans les services Braze. Notez que Braze n’archive pas les utilisateurs à moins que le nombre d’utilisateurs du groupe d’apps n’atteigne le seuil de 250 000. 

Ce processus garantit que Braze fournit des statistiques précises sur les publics accessibles à la campagne. Il permet aussi de se conformer à deux concepts clés du [RGPD][1] :

1. Le principe de limitation du stockage - les données personnelles traitées et stockées ne doivent pas être conservées plus longtemps que nécessaire
2. Il faut avoir un objectif commercial légitime pour traiter les données personnelles.

C’est-à-dire que les données à caractère personnel traitées et conservées ne doivent être conservées plus longtemps que nécessaire et que les données personnelles ne doivent être traitées qu’à des fins professionnelles légitimes. Les utilisateurs archivés auront également leur statut de désabonnement supprimé conformément au RGPD.

{% alert note %} Les clients ont un contrôle total sur le statut inactif ou dormant des utilisateurs et peuvent empêcher l’archivage des profils utilisateur en enregistrant un point de donnée à intervalle régulier. Braze Canvas offre la possibilité de le faire automatiquement, ce qui vous permet de désactiver efficacement cette fonctionnalité pour certains ou pour tous vos utilisateurs inactifs ou dormants.  {% endalert %}

## Définitions des archives utilisateur

### Utilisateurs actifs

Braze définit un « utilisateur actif » pour une période de temps donné comme étant tout utilisateur ayant enregistré une session dans l’application mobile ou le site Internet, a au moins un point de donné enregistré pour eux (par. ex., événement personnalisé, achat, attribut utilisateur), a reçu un message ou interagi avec un d’eux.

Si vous définissez des ID utilisateur pour identifier les utilisateurs lorsqu’un nouvel utilisateur se connecte, il sera compté comme un utilisateur actif séparé. Les utilisateurs mis à jour via l’API seront également comptés comme utilisateurs actifs dans la période où ils ont été mis à jour.

### Utilisateurs inactifs

Les utilisateurs inactifs sont des utilisateurs qui ne sont pas joignables et qui sont probablement churnés. Les utilisateurs inactifs sont ceux qui répondent à tous ces critères :

- Ne peuvent pas recevoir un e-mail. Par exemple, ils n’ont pas d’adresse e-mail ou ils sont désabonnés à toutes les listes de diffusion.
- Ne peuvent pas recevoir de SMS. Par exemple, ils n’ont pas de numéro de téléphone valide, ou ils sont désabonnés de tous les groupes d’abonnement SMS.
- Ne peuvent pas recevoir des notifications push. Par exemple, ils ont désinstallé l’application ou désactivé la notification push dans les permissions.
- N’ont utilisé aucune application mobile ou visité un site Internet dans un groupe d’apps depuis plus de six mois.
- N’ont reçu aucun message d’un groupe d’apps depuis plus de six mois.
- Braze n’a traité aucun point de données pour ce profil utilisateur depuis plus de six mois.

Dans ce cas, ces utilisateurs ne peuvent pas être recevoir de communications et ils ne s’engagent pas avec votre marque. Dans les faits, ces utilisateurs se sont désabonnés.

### Utilisateurs dormants

Les utilisateurs dormants sont des utilisateurs qui n’ont pas eu d’activité au cours des douze derniers mois et :

- N’ont utilisé aucune application mobile ou n’ont pas visité un site Internet dans un groupe d’apps depuis plus de 12 mois.
- N’ont reçu aucun message d’un groupe d’apps depuis plus de 12 mois.
- Braze n’a traité aucun point de données pour ce profil utilisateur depuis plus de 12 mois.

## Filtrage du spam

Braze bloque les utilisateurs individuels avec plus de 5 millions de sessions (« utilisateurs factices »), et n’ingère plus leurs événements SDK, car ils sont généralement le résultat d’une intégration incorrecte. Si vous constatez que cela s’est produit pour un utilisateur légitime, créez un ticket de [support]({{site.baseurl}}/braze_support/) Braze.

Pour trouver les utilisateurs factices dans votre tableau de bord, procédez comme suit :

1. Créez un [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).
2. Sélectionnez le filtre `Session Count` et de l’appliquer à `more than 5,000,000`.
3. Exportez le segment via CSV.

Si nécessaire, vous pouvez supprimer les utilisateurs via le endpoint de l’API [Users Delete (Supprimer les utilisateurs)]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).

[1]: {{site.baseurl}}/dp-technical-assistance/#the-right-to-erasure
[2]: {% image_buster /assets/img_archive/user_archival_policy1.png %}
[3]: {% image_buster /assets/img_archive/user_archival_policy2.png %}
[4]: {% image_buster /assets/img_archive/user_archival_policy3.png %}

## Personnaliser votre politique d’archivage de l’utilisateur

Braze fournit des fonctionnalités d’orchestration des données qui facilitent la personnalisation de votre politique d’archivage de l’utilisateur et la rendent plus rapide. Créez une politique d’archivage de l’utilisateur qui vous offre le meilleur des deux mondes avec le composant de [mise à jour de l’utilisateur]({{site.baseurl}}/user_update/) du Canvas.

Ceci vous permet de :

- Vous conformer au RGPD et aux bonnes pratiques en matière de confidentialité en supprimant les profils utilisateurs qui ne sont plus importants.
- Conserver tous les profils utilisateurs dont vous avez vraiment besoin pour vos affaires.

### Étapes

1. Cibler les utilisateurs qui correspondent aux critères d’archivage que vous souhaitez conserver.<br><br>
      ![Cibler des utilisateurs qui ont reçu un message il y a plus de 23 semaines, n’ont jamais reçu un message d’une campagne ou d’un Canvas Step, a utilisé ces applications il y a plus de 23 semaines et ont utilisé ces applications exactement zéro fois.][2]<br><br>
2. Définissez la rééligibilité pour être d’un peu moins de 6 mois.<br><br>
      ![Les contrôles d’entrée avec la rééligibilité activée et sa fenêtre définie sur 23 semaines.][3]<br><br>
3. Configurez l’étape de mise à jour l’utilisateur pour ajouter un attribut à chaque profil.<br><br>
      ![L’étape de mise à jour l’utilisateur qui ajoute l’attribut « do_not_archive » : vrai pour le profil utilisateur.][4]
{% details Exemple d’objet  User Update  %}
```json
{
    "attributes": [ 
        {
            "do_not_archive": true
        }
    ]
}
```
{% enddetails %}