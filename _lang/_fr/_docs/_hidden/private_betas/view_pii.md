---
nav_title: Voir la permission de l'utilisateur PII
permalink: /view_pii/
hidden: vrai
---

# View PII

Cela couvrira une nouvelle autorisation qui n'est accessible qu'à quelques clients sélectionnés.  Vous pouvez en savoir plus sur les capacités d'autorisation d'équipe [ici]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

## Comment ça marche

Par défaut, tous les administrateurs auront leur permission "Voir pii" activée.  Cela signifie qu'ils peuvent voir les adresses e-mail et les numéros de téléphone dans le tableau de bord. Lorsque cette permission est désactivée, les développeurs ne peuvent pas voir l'adresse e-mail ou le numéro de téléphone dans le tableau de bord.

## Zones limitées

| Navigation sur le tableau de bord | Résultat                                                                                                                                                                                                                                                                                                                                                                                                         | Notes                                                                                            |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Recherche utilisateur             | Le développeur qui se connecte n'est plus en mesure de rechercher par adresse e-mail ou par numéro de téléphone :<br><br>__&#45;__ Impossible d'afficher l'adresse e-mail ou le numéro de téléphone lors de la visualisation d'un profil utilisateur<br><br>__&#45;__ Ne peut pas modifier l'adresse e-mail ou le numéro de téléphone d'un utilisateur depuis le tableau de bord | L'accès à cette section, nécessite toujours l'accès à la permission 'Voir le profil utilisateur' |
| Import de l'utilisateur           | Le développeur ne peut plus télécharger de fichiers depuis la page d'importation de l'utilisateur                                                                                                                                                                                                                                                                                                                |                                                                                                  |
| Segments/Campagnes/Toile          | Sous la liste déroulante des données utilisateur : <br><br>__&#45;__ Le développeur ne voit plus l'option 'Adresse E-mail d'exportation CSV'<br><br>__&#45;__ Le développeur ne recevra plus l'adresse e-mail ou le numéro de téléphone dans le fichier CSV, lors de la sélection "CSV Export des données utilisateurs"                                                          |                                                                                                  |
| Groupe de test interne            | Le développeur ne peut plus voir l'adresse e-mail d'un utilisateur ajouté au groupe de test interne                                                                                                                                                                                                                                                                                                              |                                                                                                  |
| Journal d'activité des messages   | Le développeur ne verra plus l'adresse e-mail ou le numéro de téléphone des utilisateurs identifiés via le journal d'activité du message                                                                                                                                                                                                                                                                         |                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Images

!\[Page de profil utilisateur\]\[1\]{: style="max-width:60%"}

!\[New User Permission\]\[2\]{: style="max-width:60%"}

!\[Options de téléchargement des données utilisateurs\]\[3\]{: style="max-width:60%"}

{% alert note %}
Lors de la prévisualisation d'un message, la permission "voir pii" n'est pas appliquée, ainsi les développeurs peuvent voir l'adresse e-mail ou le numéro de téléphone s'ils ont été référencés dans le message via Liquid.
{% endalert %}

 [1]: {% image_buster /assets/img/user_profile_obfuscated1.png %} "profil utilisateur obfuscated1" [2]: {% image_buster /assets/img/user_profile_obfuscated2. ng %} "profil utilisateur obfusqué 2" [3]: {% image_buster /assets/img/user_profile_obfuscated3.png %} "profil utilisateur obfusqué 3"

