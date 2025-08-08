---
nav_title: EduMe
article_title: EduMe
description: "Este artigo de referência descreve a parceria entre o Braze e a eduMe, uma ferramenta de treinamento baseada em dispositivos móveis que lhe permite aproveitar o Conteúdo Conectado do Braze para dar aos seus usuários acesso aos cursos e lições da eduMe em suas campanhas Braze."
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# EduMe

> [O eduMe](https://edume.com) é uma ferramenta de treinamento baseada em dispositivos móveis que oferece à sua força de trabalho o conhecimento de que ela precisa para ter sucesso, quando precisar, onde quer que esteja. 

_Essa integração é mantida pela eduMe._

## Sobre a integração

A integração Braze e eduMe aproveita o Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) para dar aos seus usuários acesso aos cursos e lições da eduMe em suas campanhas Braze. Em seguida, o progresso individual e do grupo pode ser rastreado pela funcionalidade de relatórios da eduMe.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta EduMe | É necessário ter uma conta eduMe para aproveitar essa parceria. |
| Chave de API da EduMe | É necessário solicitar uma chave de API ao seu contato de sucesso do cliente da eduMe. Essa chave será usada na sua chamada do conteúdo conectado da Braze. |
| Segredo de assinatura de link da eduMe | É necessário solicitar ao seu contato de sucesso do cliente na eduMe a criação de um link de assinatura secreto para sua organização. Esse segredo é usado para ativar links contínuos no conteúdo conectado. Você não precisará fazer nada com esse segredo. |
| IDs de grupo e conteúdo do EduMe | Esses identificadores são necessários para configurar suas chamadas de Connected Content. Entre em contato com o atendimento ao cliente da eduMe para saber como obter esses identificadores. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Crie sua chamada de conteúdo conectado

Para dar a um usuário acesso a um curso, lição ou pesquisa eNPS e rastrear o progresso dele em relação ao seu ID de usuário interno no EduMe, siga a chamada da API mostrada neste exemplo:

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

1. Substitua `YOUR-EDUME-API-KEY` por sua chave de API eduMe.<br><br>
2. Substitua o endereço `EDUME-CONTENT-LINK-AND-CONTENT-ID` pela string de link de conteúdo correspondente e pelo identificador de módulo, lição ou pesquisa. Esses identificadores podem ser encontrados em sua conta eduMe.
  - Curso: `getCourseLink?moduleId=12087`
  - Lição: `getLessonLink?lessonId=25805`
  - Pesquisa eNPS: `getSurveyLink?surveyId=654`<br><br>
3. Os usuários que chegarem ao eduMe por meio desse link serão adicionados a uma equipe ou grupo do eduMe de sua escolha. Substitua `groupId` pelo ID da equipe relevante ou pelo ID do grupo EduMe. Normalmente, você usará o ID da equipe, exceto nos cursos que exigem inscrição, caso em que você deve usar o ID do grupo<br><br>
4. Inclua um campo apropriado para mapear o campo `externalUserId`. O exemplo de chamada de conteúdo conectado usa o endereço `driver_id`, embora seu campo provavelmente seja diferente. Esse ID estará disponível nos relatórios da eduMe, permitindo que você os correlacione com seus sistemas.<br><br>
5. Por fim, personalize e teste sua mensagem conforme necessário. Recomendamos que envie pelo menos uma mensagem de teste, acesse o conteúdo do EduMe, conclua a lição ou o curso e verifique se a análise de dados do EduMe está sendo registrada. 

