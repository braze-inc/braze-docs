---
nav_title: eduMe
article_title: eduMe
description: "Cet article de référence décrit le partenariat entre Braze et eduMe, un outil de formation mobile qui vous permet d’exploiter le Contenu connecté de Braze afin de donner à vos utilisateurs accès aux cours et leçons d’eduMe dans vos campagnes Braze."
alias: /partners/edume/
page_type: partner
search_tag: Partenaire

---

# eduMe

> [eduMe](https://edume.com) est un outil de formation mobile qui donne à votre personnel les connaissances dont il a besoin pour réussir, quand il en a besoin, où qu’il se trouve. 

L’intégration de Braze et eduMe tire parti du [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) de Braze pour donner à vos utilisateurs l’accès aux cours et aux leçons d’eduMe de vos campagnes Braze. Les progrès individuels et de groupe peuvent ensuite être suivis via la fonctionnalité de reporting d’eduMe.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte eduMe | Un compte eduMe est requis pour profiter de ce partenariat. |
| Clé d’API eduMe | Vous devez demander une clé d’API à votre contact dans le service de support d’eduMe. Cette clé sera utilisée dans votre appel de Contenu connecté de Braze. |
| Secret de connexion de lien d’eduMe | Vous devez demander à votre contact dans le service de support d’eduMe de configurer un secret de connexion de lien pour votre organisation. Ce secret est utilisé pour permettre des liaisons uniformes dans le Contenu connecté. Vous n’aurez rien à faire avec ce secret. |
| ID de groupe et de contenu eduMe | Ces identifiants sont nécessaires pour configurer vos appels de Contenu connecté. Contactez votre service clientèle eduMe pour obtenir de l’aide pour obtenir ces identifiants. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Créez votre appel de Contenu connecté

Pour donner un accès utilisateur à un cours, une leçon ou une enquête eNPS, et suivre leur progression par rapport à votre ID utilisateur interne dans eduMe, suivez l’appel API indiqué dans cet exemple :

{% raw %}
```
Welcome to my Rickshaw App platform.
Access your onboarding course at:

{% connected_content
  https://connect.edume.com/
  EDUME-CONTENT-LINK-AND-CONTENT-ID&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "x-api-key": "YOUR-EDUME-API-KEY"
  }
%}
```
{% endraw %}

1. Remplacez `YOUR-EDUME-API-KEY` avec votre clé d’API eduMe.<br><br>
2. Remplacez le `EDUME-CONTENT-LINK-AND-CONTENT-ID` par la chaîne de lien de contenu correspondante et l’identifiant du module, de la leçon ou de l’enquête. Ces identifiants se trouvent dans votre compte eduMe.
  - Cours : `getCourseLink?moduleId=12087`
  - Leçon : `getLessonLink?lessonId=25805`
  - Enquête eNPS : `getSurveyLink?surveyId=654`<br><br>
3. Les utilisateurs qui arrivent à eduMe via ce lien seront ajoutés à une équipe ou un groupe eduMe de votre choix. Remplacez `groupId` avec l’ID d’équipe ou l’identifiant du groupe eduMe pertinents. Vous utiliserez généralement l’ID de l’équipe, sauf pour les cours nécessitant une inscription, auquel cas vous devez utiliser l’ID de groupe<br><br>
4. Incluez un champ approprié auquel mapper le champ `externalUserId`. L’exemple d’appel de Contenu connecté utilise `driver_id`, bien que votre champ soit probablement différent. Cet ID sera disponible dans les rapports eduMe, ce qui vous permet de les corréler avec vos systèmes.<br><br>
5. Enfin, personnalisez et testez votre message si nécessaire. Nous vous recommandons d’envoyer au moins un message de test, d’accéder au contenu eduMe, de terminer la leçon ou le cours, et de vérifier que les analytiques d’eduMe sont enregistrées. 
