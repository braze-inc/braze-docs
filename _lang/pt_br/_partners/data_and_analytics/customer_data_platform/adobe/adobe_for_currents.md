---
nav_title: Adobe para Currents
article_title: Adobe para Currents
alias: /partners/adobe_for_currents/
description: "Este artigo de referência descreve a parceria entre Braze Currents e Adobe, uma plataforma de dados do cliente que permite que as marcas conectem e mapeiem seus dados da Adobe (atributos e segmentos personalizados) para a Braze em tempo real."
page_type: partner
tool: Currents
search_tag: Partner
---

# Adobe para Currents

> [Adobe](https://www.adobe.com/) é uma plataforma de dados do cliente que permite que as marcas conectem e mapeiem seus dados do Adobe (atributos e segmentos personalizados) para Braze em tempo real.

A integração Braze e Adobe permite que você controle de forma contínua o fluxo de informações entre os dois sistemas. Com [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), você também pode conectar dados ao Adobe para torná-los acionáveis em toda a growth stack. 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Currents | Para exportar dados de volta para o Adobe, você precisa ter [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado para sua conta. |
| Conta do Adobe Experience Platform | Uma [conta do Adobe Experience Platform](https://experience.adobe.com/#/platform/home) é necessária para aproveitar esta parceria. |
| Permissão para criar um conector | Você precisa de permissões para criar uma conexão de fonte de streaming para usar esta integração. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Crie um esquema XDM no Adobe

1. No Adobe Experience Platform, Acessar **Schemas** > selecionar **Criar esquema** > selecionar **Evento de Experiência** > selecionar **Próximo**.<br><br>![Página do Adobe Schemas para o esquema chamado "Braze Currents Walk-Through".]({% image_buster /assets/img/adobe/currents_sources.png %})<br><br>
2. Forneça um nome e uma descrição para seu esquema. 
3. No painel **Composição**, configure os atributos do seu esquema:
- Em **Field groups**, selecione **Add** e, em seguida, adicione o grupo de campos **Braze Currents User Event**.
- Selecione **Salvar**.

Para saber mais sobre esquemas, consulte a documentação da Adobe sobre [criação de esquemas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

### Etapa 2: Conecte Braze à Adobe Experience Platform

1. No Adobe Experience Platform, Acessar **Sources** > **Catalog** > **Marketing automation**.
2. Selecione **Add data** para Braze Currents.
3. Fazer upload do [Braze Currents sample file](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json).<br><br>![Adobe "Add data page" (Adicionar página de dados).]({% image_buster /assets/img/adobe/currents_add_data.png %})<br><br>
4. Após o upload do seu arquivo, forneça os detalhes do seu fluxo de dados, incluindo informações sobre seu conjunto de dados e o esquema ao qual você está mapeando. 
    - Se esta é a sua primeira vez conectando uma fonte de Braze Currents, crie um novo conjunto de dados e certifique-se de usar o esquema que você criou em [Etapa 1](#step-1-create-an-xdm-schema-in-adobe). 
    - Se esta não é a sua primeira vez, use qualquer conjunto de dados existente que faça referência ao esquema Braze.
5. Configure o mapeamento para seus dados e resolva os problemas.
    - Altere o mapeamento de `id` de `to _braze.appID` para `_id` no nível raiz do esquema.
    - Certifique-se de que `properties.is_amp` está mapeado para `_braze.messaging.email.isAMP`.
    - Delete o `time` e `timestamp` mapeamento, então selecione o ícone de adicionar > **Adicionar campo calculado** e insira **tempo * 1000**. Selecione **Salvar**.
    - Selecione **Campo de destino do mapa** ao lado do novo campo de origem e mapeie-o para **timestamp** no nível raiz do esquema. <br><br>![Página "Adicionar dados" da Adobe com mapeamentos.]({% image_buster /assets/img/adobe/currents_mapping.png %})<br><br>
6. Selecione **Validar** para confirmar que você resolveu os problemas.

{% alert important %}
Os timestamps de braze são expressos em segundos. Para refletir com precisão os timestamps na Adobe Experience Platform, seus campos calculados precisam estar em milissegundos. Para converter segundos em milissegundos, use o cálculo **time * 1000**.
{% endalert %}

{: start="7"}
7\. Selecione **Próximo**, revise os detalhes do seu fluxo de dados e, em seguida, selecione **Concluir**.<br><br>![Página "Adicionar dados" da Adobe sem erros de mapeamento.]({% image_buster /assets/img/adobe/currents_no_errors.png %})

### Etapa 3: Coletar credenciais

Colete as seguintes credenciais para inserir no Braze, que permitirá ao Braze enviar dados para a Adobe Experience Platform.

| Campo         |Descrição                          |
|---------------|-------------------------------------|
| ID do cliente     | O ID do cliente associado à sua fonte do Adobe Experience Platform. |
| Segredo do cliente | O segredo do cliente associado à sua fonte do Adobe Experience Platform. |
| Tenant ID     | O ID do inquilino associado à sua fonte do Adobe Experience Platform. |
| Nome do sandbox  | A área de trabalho associada à sua fonte do Adobe Experience Platform.   |
| ID do Dataflow   | O ID do fluxo de dados associado à sua fonte do Adobe Experience Platform.   |
| Endpoint do streaming  | O endpoint de streaming associado à sua fonte do Adobe Experience Platform. O braze converte isso automaticamente para o ponto de extremidade de streaming em lote. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 4: Configure Currents para enviar dados para sua fonte de dados

1. No Braze, acesse **Integrações de Parceiros** > **Exportação de Dados**, e então selecione **Criar Novo Atual**. 
2. Forneça o seguinte:
    - Um nome para o conector
    - Informações de contato para notificações sobre o conector
    - As credenciais da [etapa 3](#step-3-gather-credentials)
3. Selecione os eventos que você deseja receber.
4. Opcionalmente, configure quaisquer exclusões ou transformações de campo desejadas.
5. Selecione **Iniciar Atual**.

