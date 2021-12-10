---
nav_title: EduMe
article_title: EduMe
description: "Cet article décrit le partenariat entre Braze et EduMe, un outil de formation mobile qui vous permet de donner à votre personnel ou à vos clients accès aux cours et aux cours créés dans EduMe. Ils pourront accéder à ce contenu de manière transparente dans leur navigateur, et vous pourrez suivre leur progression en tant que groupe ou en tant qu'individus en utilisant la fonctionnalité de signalement EduMe ."
alias: /fr/partners/edume/
page_tpe: partenaire
search_tag: Partenaire
---

# EduMe

> [EduMe](https://edume.com) est un outil de formation mobile qui donne à votre main-d'œuvre les connaissances dont elle a besoin pour réussir. Quand ils en ont besoin, où qu'ils soient. <br><br>Utilisez [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) dans Braze pour donner à votre personnel ou à vos clients accès aux cours et cours dans EduMe. Ils pourront accéder à ce contenu de manière transparente dans leur navigateur, et vous pourrez suivre leur progression en tant que groupe ou en tant qu'individus en utilisant la fonctionnalité de signalement EduMe .

## Pré-requis

Afin d'utiliser le Contenu Connecté avec EduMe, vous devrez configurer quelques éléments avec votre contact client avec succès.

| Exigences                                                        | Origine | Accès                                                                                                                                                                    | Libellé                                                                                                                                                                   |
| ---------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clé API EduMe                                                    | EduMe   | Vous devez demander une clé API à votre contact client avec succès chez EduMe                                                                                            | Utilisez la clé API EduMe lors de la configuration du contenu connecté EduMe tel que décrit ci-dessous.                                                                   |
| Secret de signature du lien EduMe                                | EduMe   | Vous devez demander à votre contact client à EduMe de mettre en place un secret de signature de lien pour votre organisation.                                            | Ce secret est utilisé en coulisses pour activer les liens transparents dans le contenu connecté. Vous n'avez pas à trouver cette clé ou rien faire avec elle directement. |
| Connaissance des identifiants de groupe et de contenu dans EduMe | EduMe   | Le contact réussi de votre client chez EduMe vous aidera à connaître les ID du contenu et des groupes d'utilisateurs pertinents dans EduMe pour votre cas d'utilisation. | Vous utiliserez ces identifiants lors de la configuration des extraits de contenu connecté en suivant les instructions ci-dessous.                                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration de contenu connecté

Utilisez cette intégration pour donner à vos utilisateurs accès aux cours et leçons que vous avez publiés dans EduMe.

### Accès à un cours

Pour donner un accès à un cours à un utilisateur et pour suivre ses progrès par rapport à votre identifiant utilisateur interne dans EduMe, suivre l'appel API affiché dans cet exemple simple :

{% raw %}
```
Bienvenue sur ma plateforme Rickshaw App.
Veuillez accéder à votre cours d'intégration à:

{% connected_content
  https://edume-braze-connect.herokuapp. om/getCourselink ? oduleId=12087&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "X-Api-Key": "YOUR-EDUME-API-KEY"
    }
%}
```
{% endraw %}

### Adaptation de l'exemple pour votre propre cas d'utilisation

Pour passer de l'exemple à votre propre cas d'utilisation, mettez à jour ce qui suit :
1. Inclure votre clé API EduMe là où elle est affichée dans le message.
2. Inclure le module EduMe `ID` approprié dans l'appel API de contenu connecté en tant que paramètre `moduleId`.
3. Les utilisateurs qui arrivent à EduMe via ce lien seront ajoutés à une équipe ou un groupe de votre choix dans EduMe. Trouvez l'ID `` pour le groupe ou l'équipe concerné dans EduMe et incluez-le comme paramètre `groupId` dans l'appel API.
4. Inclure un champ approprié de vos données utilisateur dans Braze en tant que paramètre `externalUserId` dans l'appel API. L'exemple suppose que cela serait trouvé en tant que `driver_id` où vous faites l'appel. Vous aurez probablement un ID approprié dans une variable différente. Cet identifiant sera disponible dans les rapports EduMe vous permettant de les corréler avec vos propres systèmes.
5. Personnalisez le message et inscrivez-le au bon endroit dans votre campagne ou dans Canvas.
6. Testez le flux : Envoyez un message de test à vous-même, accédez au contenu EduMe via le lien que vous recevez, compléter la leçon ou le cours, et vérifier que vous pouvez trouver le dossier de votre achèvement dans les rapports EduMe .

### Accès à une leçon

De même, un lien vers une leçon particulière peut être créé en utilisant l'URL suivante de la même manière :
{%raw%}
```
https://edume-braze-connect.herokuapp.com/getLessonLink?lessonId=25805&groupId=4719&externalUserId={{${driver_id}}}
```
{%endraw%}
Les différences sont le point de terminaison de l'API `getLessonLink`, et fournissant un ID de leçon dans le paramètre `lessonId` au lieu d'un ID de module. Sinon, tout fonctionne de la même façon que pour les cours.

### Accès à une enquête eNPS

En ce qui concerne les leçons, un lien vers une enquête eNPS particulière peut être créé en utilisant l'URL suivante :
{%raw%}
```
https://edume-braze-connect.herokuapp.com/getSurveyLink?surveyId=654&groupId=7961&externalUserId={{${driver_id}}}
```
{%endraw%}
Encore une fois, les différences sont le point de terminaison de l'API `getSurveyLink`, et fournissant un surveyId dans le paramètre `surveyId`. Dans le cas contraire, c'est exactement le même processus que pour les cours.
