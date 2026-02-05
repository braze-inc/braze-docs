---
nav_title: Kameleoon
article_title: Kameleoon
description: "Saiba como integrar o Kameleoon ao Braze"
alias: /partners/kameleoon/
page_type: partner
search_tag: Partner
---

# Kameleoon

>[O Kameleoon](https://www.kameleoon.com) é uma solução de otimização com experimentos, personalização com IA e recursos de gerenciamento de recursos em uma única plataforma unificada.

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Requisito | Descrição |  
| --- | --- |  
| Conta Kameleoon | É necessário ter uma conta Kameleoon para aproveitar essa parceria.|  
| Conta Braze| Uma conta Braze ativa com o [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) integrado em sua página da Web. Você também precisará ativar a segmentação de propriedades de eventos. Para solicitá-lo, consulte [Considerações](#considerations).|  
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Casos de uso

A Kameleoon envia eventos personalizados para o Braze para identificar os usuários que participam de campanhas de experimentação e personalização, ativando um direcionamento mais preciso e o envio de mensagens personalizadas.

## Integração do Kameleoon

Essa integração é executada como um rastreador JavaScript por meio do site engine.js do Kameleoon. Ela pode ser rapidamente ativada na plataforma da Kameleoon.

### Etapa 1: Acessar a página de integrações do Kameleoon

Em seu app Kameleoon, selecione **Admin** e, em seguida, **Integrations (Integrações** ) na barra lateral.

![O painel de administração na plataforma Kameleoon.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### Etapa 2: Instale a ferramenta Braze

Por padrão, a ferramenta Braze não está instalada. Procure o ícone do Braze e selecione **Instalar a ferramenta**. ![Um quadrado cinza com uma seta apontando para baixo.]({% image_buster /assets/img/kameleoon/img_2.png %})

Selecione os projetos para os quais você deseja ativar a ferramenta Braze, para que os dados do Kameleoon sejam reportados corretamente ao Braze.

![O ícone da ferramenta Braze na Kameloon.]({% image_buster /assets/img/kameleoon/img_3.png %})

Depois de configurar a ferramenta, selecione **Validate (Validar**), que fechará o painel de configuração. Em seguida, você verá uma alternância **ON** ao lado do ícone da ferramenta Braze, incluindo o número de projetos nos quais a ferramenta está configurada.

![A ferramenta Braze foi ativada no Kameleoon.]({% image_buster /assets/img/kameleoon/img_4.png %})

{% alert important %}  
Esse recurso está na versão beta. Participe do [Kameleoon Beta Program](https://help.kameleoon.com/account-and-team-management/join-beta-program/) para começar a usar essa integração.  
{% endalert %}  
    
### Etapa 3: Associar o Braze às campanhas da Kameleoon

#### No editor gráfico/código

Para finalizar seu experimento, selecione a etapa **Integrações** para configurar o Braze como uma ferramenta de rastreamento e, em seguida, selecione **Braze**.

![O dashboard Integrations (Integrações) no Kameleoon mostra todas as integrações disponíveis, incluindo a integração ativa Braze.]({% image_buster /assets/img/kameleoon/img_5.png %})

O Braze será mencionado no resumo antes de entrar em operação. O Kameleoon transmitirá automaticamente os dados para o Braze, e você poderá usá-los para análise e segmentação diretamente no Braze.

##### Criação de personalização

Na página **Personalization Creation (Criação de personalização** ), você pode selecionar o Braze entre as ferramentas de relatório para personalizar seus relatórios.

![Seção Reporting Tools mostrando integrações como Heap, Mixpanel, Clarity, com Braze selecionado.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### Criação de Feature Flag

Configure a integração no ambiente do sinalizador de recursos na seção **Integrações**. Ative a capacitação para os ambientes em que você deseja que ela esteja ativa.

![A página Feature Flag no Kameleoon com as integrações disponíveis. Há dois switches para cada parceiro, "Regras de entrega" e "Experimentos de recursos".]({% image_buster /assets/img/kameleoon/img_7.png %})

##### Página de resultados

Depois que o Braze for definido como uma ferramenta de relatório para um experimento, você poderá selecioná-lo (ou desmarcá-lo) na página de resultados do Kameleoon no menu **de configuração do experimento**.

{% alert note %}  
Essa integração requer uma [implementação híbrida](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics) e é compatível apenas com SDKs da Web.
{% endalert %}

![O painel lateral da página de resultados no Kameleoon.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

As ferramentas de relatório associadas ao experimento serão exibidas. Selecione **Editar** para editar essa seleção.

### Etapa 4: Analise e aproveite seus dados do Kameleoon no Braze

Depois que a integração for configurada, o Kameleoon enviará eventos personalizados chamados `kameleoon_exposure` com propriedades como **Nome do experimento**, **ID do experimento**, **Nome da variação**, **ID da variação** para o Braze.

![O registro de usuários de eventos personalizados no Braze, mostrando um exemplo de carga útil do evento que foi recebido pelo Braze do Kameleoon.]({% image_buster /assets/img/kameleoon/img_9.png %})

Em seguida, você pode visualizar esses dados nos eventos personalizados, criar relatórios de eventos personalizados para identificar a exposição da campanha do Kameleoon e ativar a segmentação com base nas propriedades do evento. Você pode usar eventos personalizados ao criar campanhas e Canvas subsequentes ou vinculados por meio de [jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/#action-groups), [disparos baseados em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery) ou criação de [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

Além disso, esses eventos poderão ser acessados por meio de [objetos de eventos personalizados do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) para permitir relatórios e análises abrangentes.

## Considerações

### Segmentação de propriedades de eventos de solicitação

Antes de poder usar a segmentação de propriedades de eventos, você precisará ativá-la no Braze. Use o modelo a seguir para entrar em contato com o CSM da Braze ou com a equipe de suporte para obter acesso.

   <table>
   <thead>
      <tr>
         <th>Campo</th>
         <th>Informações</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Assunto</strong></td>
         <td>Solicitação para ativar a segmentação de propriedades de eventos para a integração com o Kameleoon</td>
      </tr>
      <tr>
         <td><strong>Corpo</strong></td>
         <td>
         Olá, equipe do Braze,<br><br>
         Gostaríamos de ativar a segmentação de propriedades de eventos para eventos enviados de nossa integração com o Kameleoon&lt;>Braze. Aqui estão os detalhes:<br><br>
         - <strong>Nome do evento:</strong> Kameleoon<br>
         - <strong>Propriedades do evento:</strong> <code>kameleoon_campaign_name</code>, <code>kameleoon_variation_name</code><br><br>
         Por favor, confirme quando as propriedades forem ativadas em nossa conta.<br><br>
         Obrigada.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Pontos de dados do Braze

O evento personalizado enviado do Kameleoon para o Braze - incluindo quaisquer propriedades de evento ativadas para segmentação - registrará pontos de dados na sua instância do Braze.