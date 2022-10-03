---
nav_title: "Autorisation utilisateur : Afficher les informations personnellement identifiables"
permalink: /view_pii/
hidden: true
---

# Afficher les informations personnellement identifiables

Cet article couvre une nouvelle autorisation qui n’est accessible qu’à quelques clients sélectionnés. Pour les capacités d’autorisation d’équipe existantes, consultez [Définition des autorisations utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

## Fonctionnement

Par défaut, tous les administrateurs peuvent utiliser la fonction **Afficher les informations personnellement identifiables**. Cela signifie qu’ils peuvent voir les adresses e-mail et les numéros de téléphone dans tout le tableau de bord.
Lorsque cette autorisation est désactivée, les développeurs ne peuvent voir aucune adresse e-mail ou numéro de téléphone dans le tableau de bord de Braze.

## Zones restreintes

|Navigation sur le tableau de bord| Résultat| Remarques|
|--------------------|-------|------|
| User Search | Le développeur qui se connecte ne peut plus effectuer de recherche par adresse e-mail ou numéro de téléphone :<br><br>**&#45;** Impossible d’afficher l’adresse e-mail ou le numéro de téléphone lors de l’affichage d’un profil utilisateur.<br><br>**&#45;** Impossible de modifier l’adresse e-mail ou le numéro de téléphone d’un profil utilisateur à  partir du tableau de bord de Braze.| L’accès à cette section nécessite toujours l’accès au profil utilisateur. |
| User Import | Le développeur ne peut pas télécharger les fichiers de la page **User Import**. | |
| Segments/Campagne/Canvas | Dans la liste déroulante **Données utilisateur** : <br><br>**&#45;** Le développeur n’aura pas accès à l’option **CSV Export Email Address** (Exportation CSV des e-mails). <br><br>**&#45;** Le développeur ne recevra pas l’adresse e-mail ou le numéro de téléphone dans le fichier CSV si **CSV Export User Data** (Exportation CSV des données utilisateur) est sélectionné. | |
| Groupe de test interne | Le développeur n’aura pas accès à l’adresse e-mail des utilisateurs ajoutés au groupe de test interne. | |
| Journal d’activité de message | Le développeur n'aura pas accès à l'adresse e-mail ou au numéro de téléphone des utilisateurs identifiés via le journal d'activité des messages. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

![Un profil d’utilisateur avec une adresse e-mail et un numéro de téléphone cachés, indiquant que les autorisations de développeur actuelles ne permettent pas d’utiliser la fonction Afficher les informations personnellement identifiables.][1]{: style="max-width:60%"}

![La case Afficher les informations personnellement identifiables est cochée, permettant d’afficher les adresses e-mail et numéros de téléphone de l’utilisateur.][2]{: style="max-width:60%"}

![La liste déroulante Données utilisateur comporte deux options de téléchargement : CSV Export All Recipient Data (Exportation CSV de toutes les données des destinataires) et CSV Export Recipient Email Addresses (Exporation CSV des adresses e-mail des destinataires)][3]{: style="max-width:60%"}

{% alert note %}
Lorsque vous prévisualisez un message, la fonction **Afficher les informations personnellement identifiables** n’est pas disponible. Les développeurs peuvent voir l’adresse e-mail ou le numéro de téléphone s’ils ont été référencés dans le message via Liquid.
{% endalert %}

[1]: {% image_buster /assets/img/user_profile_obfuscated1.png %} "user profile obfuscated1"
[2]: {% image_buster /assets/img/user_profile_obfuscated2.png %} "user profile obfuscated2"
[3]: {% image_buster /assets/img/user_profile_obfuscated3.png %} "user profile obfuscated3"

