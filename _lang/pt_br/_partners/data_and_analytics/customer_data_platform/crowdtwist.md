---
nav_title: Oracle Crowdtwist
article_title: Crowdtwist
description: "Este artigo descreve a parceria entre o Braze e o Oracle Crowdtwist, por meio de modelos de transformação de dados do Braze especialmente criados e dos Data Push Objects do Crowdtwist."
page_type: partner
search_tag: Partner

---

# Oracle Crowdtwist

> [O Oracle Crowdtwist](https://www.oracle.com/uk/cx/marketing/customer-loyalty/) é uma solução líder em fidelidade do cliente nativa da nuvem que capacita as marcas a oferecer experiências personalizadas aos clientes. Sua solução oferece mais de 100 jornadas de engajamento prontas para uso, proporcionando um rápido retorno do investimento para que os profissionais de marketing desenvolvam uma visão mais completa do cliente.

O recurso Data Push do Oracle Crowdtwist permite que os metadados de usuários ou eventos sejam transmitidos sempre que ocorrer uma atualização na plataforma do Crowdtwist.

Este guia descreve como integrar os feeds Live Push de perfil de usuário, atividade de usuário e resgate de usuário do Oracle Crowdtwist ao seu ambiente Braze. Há dois tipos adicionais de Data Push disponíveis que não são explicitamente abordados nesta documentação, mas sua configuração segue os mesmos princípios descritos abaixo. 

* [Perfil de usuário do Live Push](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/PushUserProfile-withTiersv2.html): Inclui a criação de novos perfis e atualizações de perfis existentes.

* [Atividade do usuário de push ao vivo](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html): Inclui dados de conclusões de atividades de usuários.

* [Redenção de usuários por push ao vivo](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserRedemption.html): Inclui dados de resgates de recompensas de usuários. 

Ao usar um modelo de transformação de dados do Braze, você pode filtrar os elementos do Data Push que não são relevantes para o Braze e atribuir os valores necessários no Braze para que possam ser aproveitados pelos "destinos" disponíveis.

Por exemplo, use um Data Push para passar eventos e atributos personalizados relevantes para o Braze, como quando um usuário muda de nível de fidelidade ou resgata uma recompensa. Também é possível usá-lo para registrar atributos personalizados no Braze assim que esses dados forem atualizados no perfil de usuário de um membro, como o saldo de pontos de um usuário. 

## Pré-requisitos


| Requisito | Descrição |
| --- | --- |
| Conta Oracle Crowdtwist | É necessário ter uma [conta Oracle Crowdtwist](https://www.oracle.com/uk/cx/marketing/customer-loyalty/) para aproveitar essa parceria. |
| Ponto de extremidade de transformação de dados Braze| Essa integração se baseia na [ferramenta de transformação de dados]({{site.baseurl}}/user_guide/data/data_transformation/overview) da Braze. Quando você cria uma transformação de dados, o Braze gera um endpoint exclusivo que pode ser adicionado como um destino para o Data Push do Crowdtwist.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

O Braze e o Oracle Crowdtwist criaram [modelos de transformação de dados]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation?redirected=1#step-2-create-a-transformation) para ajudar nossos clientes a desenvolver suas próprias transformações de dados que aproveitam os eventos Perfil do usuário, Resgate do usuário e Atividade do usuário. 

## Etapa 1: Criar transformação de dados a partir do modelo Oracle Crowdtwist

Navegue até **Configurações de dados > Transformação de dados > Criar transformações > Usar um modelo** > e selecione o modelo "BRAZE <> CROWDTWIST" de sua escolha. 

Você encontrará quatro modelos - um para transformar eventos de Perfil do usuário, Atividade do usuário e Resgate do usuário, e um modelo mestre que usa lógica condicional para aplicar a vários eventos de Data Push.

Conforme mostrado na [documentação do Data Push do Oracle Crowdtwist](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/DataPush.html), os objetos Data Push contêm metadados diferentes, portanto, cada um requer seu próprio código de transformação para criar objetos Braze apropriados. O modelo mestre ilustra como configurar uma única transformação de dados para aceitar cada um dos três tipos de objetos e cria uma saída apropriada com valores de cada objeto.

## Etapa 2: Atualizar e testar o modelo

Abaixo, você verá os modelos anotados. O corpo desses modelos foi projetado para ser aplicado ao destino `/users/track`. As anotações são marcadas pelo início da linha `//` e pelo texto verde, e você pode excluí-las sem afetar a operação do código de transformação. 

A transformação usa JavaScript, que cria um objeto chamado "brazecall". Esse objeto é onde você cria o corpo da solicitação que é enviado para um endpoint da Braze REST API. Para obter orientação sobre as estruturas necessárias das solicitações para esses destinos, consulte os links na seção "destinos".    

{% alert note %}
Observe que os "valores" de cada "chave" começam com `payload.`. A carga útil representa o objeto de dados recebido do Oracle Crowdtwist. Use a notação de ponto do JavaScript para escolher qual dado você deseja preencher os elementos do seu objeto Braze. Por exemplo, quando você vê `external_id: payload.thirdPartyId`, isso significa que a ID externa do Braze é definida pelo valor `third_party_id` armazenado no Oracle Crowdtwist. Para saber mais sobre o esquema ou a composição dos objetos provenientes do Oracle Crowdtwist, consulte [a documentação da Oracle](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html).
{% endalert %}

{% alert important %}
 Use os objetos enviados do Oracle Crowdtwist para criar usuários no Braze. Ao incluir a chave `update_existing_only` com o valor `false`, se um atributo ou objeto de evento incluir um identificador que não exista no Braze, o Braze criará um perfil de usuário com as atribuições incluídas no evento ou objeto de atributo. Se você preferir que o Oracle Crowdtwist atualize somente os perfis que já existem no Braze, defina essa atribuição como `true` em cada atributo ou objeto de evento.
{% endalert %}

### Modelos de transformação de dados
{% tabs %}
{% tab User Profile Event Template%}
```javascript
let brazecall = {
 "attributes": [
   {
     //You must include an appropriate identifier for your attribute or event object from data available in Oracle Crowdtwist. This could be an external ID, Braze ID, user alias, phone, or email address for attribute or event objects.
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
   // **Important** To allow Oracle Crowdtwist events to create users in Braze, set the value of "_update_existing_only" to false. Otherwise, set this value to true in your event and attribute objects.
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
 //In this example, the "tierInfo" object from Crowdtwist is transformed into a Braze Nested Custom Attribute. Use the "_merge_objects" value to avoid duplications in a data point efficient manner.
 //The "tierinfo_current_level" attribute is a flat Braze custom attribute, while "tierInfo" below is a nested object mirroring the Crowdtwist payload; the difference in capitalization is intentional.
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{ 
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
//Below we show how to create both custom attributes and events from a single Crowdtwist User Profile object.
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
//Below we can see how to write a timestamp in your object, which is a required value for some objects, like the Event Object. 
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
// After the /users/track request is assigned to brazecall, return brazecall to create an output.
return brazecall;

```

{% endtab %}
{% tab User Activity Event Template %}
```javascript
let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
```
{% endtab %}
{% tab Redemption Event Template %}
```javascript
let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   //A user redemption event may not have a third party id, in which case you can instead provide the opportunity to include a user alias.
   "user_alias": { "alias_name" : "crowdtwist_redemption_username", "alias_label" : payload.userName},
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;

```
{%endtab%}
{% tab Master Template %}
```javascript
//The master template uses JavaScript's conditional operators to determine the output of the Data Transformation. This example shows how to apply JavaScript to your transformation to allow for a dynamic range of sources or inputs. 

 // We open the transformation with a simple "if" function. We're checking if the value "payload.tierInfo" is present. "tierInfo" is a value that is always populated in the User Profile Live Push object, but is not present in the others.

if (payload.tierInfo) {
let brazecall = {
 "attributes": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{ 
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
return brazecall;
//Now we use an "else if" operator to change the "brazecall" body if the object is a User Activity event by checking if the unique key "activityId" has been populated.
} else if (payload.activityId) {
 let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
//Finally, this conditional statement triggers if the Data Push object is a User Redemption event, based on whether a value populates in the key "rewardId".
} else if (payload.rewardId) {
 let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;
} else {
 //Include this error message to help with troubleshooting in the log if a call fails. Replace the text in the parentheses with anything that might be clearer to your team based on your Data Transformation.
 throw new Error("No appropriate Identifiers found");
}

```
{% endtab %}
{% endtabs %}

### Destinos

Os modelos deste guia foram criados para serem entregues no destino "Track Users", mas você pode projetar seu modelo para enviar a qualquer um dos endpoints listados no [guia Data Transformation do Braze]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation/#step-2-create-a-transformation), com o suporte da [documentação REST API]({{site.baseurl}}/api/home) associada.

### Testes

Depois de modificar o modelo a seu gosto, você deve validar se ele está funcionando corretamente. Clique em "Validate" (Validar) para retornar uma prévia da saída de seu código e verificar se é uma solicitação aceitável para os destinos escolhidos. 

![Captura de tela da interface de transformação de dados do Braze]({% image_buster /assets/img/crowdtwist_tools/screenshot.png %}){: style="max-width:70%;margin-bottom:15px;border:none;"}

Quando estiver satisfeito com o objeto que você vê no campo "output" (saída), clique em **Activate (ativar** ) para que o endpoint da transformação de dados esteja pronto para aceitar dados. 

Você encontrará o URL do webhook de sua transformação de dados no painel do lado esquerdo. Copie-o e use-o para configuração no Hub de integração do Oracle Crowdtwist.

{% alert important %}
Os endpoints do Braze Data Transformation têm um limite de frequência de 1.000 solicitações por minuto. Considere a velocidade na qual você deseja que esses dados sejam disponibilizados no Braze e fale com seu gerente de conta do Braze se precisar de um limite de frequência de transformação de dados mais alto.
{% endalert %}

As transformações de dados são uma ferramenta muito dinâmica e você pode projetá-las para fins que vão além do que está descrito neste documento com um conhecimento de JavaScript e com a orientação da nossa documentação da API REST. Para obter suporte ou solução de problemas em alterações complexas em seus modelos de transformação de dados, fale com o gerente de sucesso do cliente para saber mais sobre as orientações disponíveis.