---
nav_title: EduMe
article_title: EduMe
description: "Cet article décrit le partenariat entre Braze et EduMe, un outil de formation mobile qui vous permet de tirer parti de Braze Connected Content pour donner à vos utilisateurs accès aux cours et aux leçons d'EduMe dans vos campagnes de Braze."
alias: /fr/partners/edume/
page_tpe: partenaire
search_tag: Partenaire
---

# EduMe

> [EduMe](https://edume.com) est un outil de formation mobile qui donne à votre main-d'œuvre les connaissances dont elle a besoin pour réussir, quand elle en a besoin, où qu'elle soit.

L'intégration de Braze et EduMe tire parti de Braze [Contenu Connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) pour donner à vos utilisateurs accès aux cours et leçons d'EduMe dans vos campagnes de Braze. Les progrès individuels et de groupe peuvent ensuite être suivis grâce à la fonctionnalité de rapport EduMe.

## Pré-requis

| Exigences                         | Libellé                                                                                                                                                                                                                                                     |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte EduMe                      | Un compte EduMe est requis pour profiter de ce partenariat.                                                                                                                                                                                                 |
| Clé API EduMe                     | Vous devez demander une clé API à votre contact client EduMe avec succès. Cette clé sera utilisée dans votre appel de contenu connecté à Braze.                                                                                                             |
| Secret de signature du lien EduMe | Vous devez demander à votre contact client à EduMe de mettre en place un secret de signature de lien pour votre organisation. Ce secret est utilisé pour activer les liens transparents dans le contenu connecté. Vous n'aurez rien à faire avec ce secret. |
| Groupe et ID de contenu EduMe     | Ces identifiants sont nécessaires pour configurer vos appels de contenu connecté. Communiquez avec votre interlocuteur du service à la clientèle EduMe pour obtenir ces identifiants.                                                                       |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Créez votre appel de contenu connecté

Pour donner à un utilisateur accès à un cours, une leçon ou une enquête eNPS, et pour suivre leur progression par rapport à votre identifiant utilisateur interne dans EduMe, suivez l'appel API affiché dans cet exemple :

{% raw %}
```
Bienvenue sur ma plateforme Rickshaw App.
Veuillez accéder à votre cours d'intégration à:

{% connected_content
  https://edume-braze-connect.herokuapp. om/
  <EDUME-CONTENT-LINK-AND-CONTENT-ID>&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "X-Api-Key": "<YOUR-EDUME-API-KEY>"
  }
%}
```
{% endraw %}

1. Remplacez `<YOUR-EDUME-API-KEY>` par votre clé API EduMe<br><br>
2. Remplacez le `<EDUME-CONTENT-LINK-AND-CONTENT-ID>` par la chaîne de lien de contenu correspondante et le module, la leçon ou l'identifiant de l'enquête. Ces identifiants peuvent être trouvés dans votre compte EduMe.
  - Course: `getCourseLink?moduleId=12087`
  - Leçon : `getLessonLink?lessonId=25805`
  - Enquête eNPS : `getSurveyLink?surveyId=654`<br><br>
3. Les utilisateurs qui arrivent à EduMe via ce lien seront ajoutés à une équipe ou un groupe de votre choix. Remplacer `groupId` par le groupe EduMe ou l'ID d'équipe concerné.<br><br>
4. Inclure un champ approprié pour associer le champ `externalUserId`. L'exemple ci-dessus utilise le `driver_id`, bien que votre champ soit probablement différent. Cet identifiant sera disponible dans les rapports EduMe vous permettant de les corréler avec vos systèmes.<br><br>
5. Enfin, personnalisez et testez votre message au besoin. Nous vous recommandons d'envoyer au moins un message de test, d'accéder au contenu EduMe compléter la leçon ou le cours, et vérifier que les analyses EduMe sont enregistrées. 
