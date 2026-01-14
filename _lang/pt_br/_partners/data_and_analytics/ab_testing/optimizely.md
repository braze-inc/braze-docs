---
nav_title: Optimizely
article_title: Optimizely
page_order: 2
description: "Esse artigo de referência descreve a parceria entre o Braze e a Optimizely que permite que você sincronize seus segmentos de clientes, eventos e eventos do Currents do Braze com a plataforma de dados da Optimizely."
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# Optimizely

> [A Optimizely](https://www.optimizely.com/) é uma plataforma líder em experiência digital que oferece ferramentas de experimentação e gerenciamento de conteúdo para produtos digitais e campanhas de marketing.

A integração entre Braze e Optimizely é uma integração bidirecional que permite a você:

- Sincronize seus segmentos e eventos de clientes do Braze com a plataforma de dados da Optimizely (ODP) todas as noites para enriquecer os perfis, os relatórios e a segmentação de clientes da Optimizely.
- Envie eventos Braze Currents do Braze para a ferramenta de relatórios da Optimizely.
- Sincronize dados e eventos de clientes do ODP com o Braze para enriquecer seus dados de clientes do Braze e disparar envios de mensagens do Braze com base em eventos de clientes no ODP.

## Pré-requisitos

| Requisito                     | Descrição |
|----------------------------------|-------------|
| Conta da plataforma de dados da Optimizely | É necessário ter uma conta na Optimizely Data Platform (ODP) para aproveitar essa parceria. |
| Chave da API REST do Braze               | Uma chave da API REST do Braze com as seguintes permissões: `users.track`,`users.export.segments`,`segments.list`,`campaigns.trigger.send`, e `canvas.trigger.send`. |
| Currents                         | Para exportar dados de volta para o Optimizely, você precisa ter o Braze Currents configurado para sua conta. |
| URL e token da Optimizely         | Isso pode ser obtido navegando até seu dashboard do Optimizely e copiando a URL de ingestão e o token. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Configurar a integração

1. No **diretório de aplicativos** da Optimizely Data Platform (ODP), selecione o aplicativo **Braze** e, em seguida, selecione **Instalar aplicativo**.
2. Acesse a guia **Configurações**. Na seção **Authorization (Autorização** ), faça o seguinte:
    1. Insira **a chave da API REST** do Braze.
    2. Selecione o **URL de** sua **instância** do Braze.
    2. Selecione **Verify API Key (Verificar chave de API**).
3. No Braze, acesse **[Currents]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/)**.
4. Selecione **Create New Current (Criar nova corrente** ) > **Custom Currents Export (Exportar correntes personalizadas**).
5. Configure o Current usando o ponto de extremidade e o token fornecidos no ODP. Isso é necessário para sincronizar os eventos do Braze com o ODP. 

![Autorização da Optimizely.]({% image_buster /assets/img/optimizely/image1_authorization.png %})

{:start="6"}
6\. No ODP, expanda a seção **Segments** (Segmentos) e selecione segmentos específicos na lista **Segments to Sync (Segmentos para sincronização** ) ou selecione **Import All Customers (Importar todos os clientes** ) para sincronizar todos os segmentos.
7\. Adicione quaisquer [mapeamentos de campo adicionais](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR) que desejar entre o Braze e o ODP.
8\. Selecione **Salvar**.

![Optimizely Braze segment sync.]({% image_buster /assets/img/optimizely/image2_syncsegment.png %})

{% alert tip %}
Você deve selecionar segmentos para importar perfis de clientes Braze. Se você não selecionar nenhum segmento, a integração não importará nenhum perfil de cliente.
{% endalert %}

### Etapa 2: Campos de dados do mapa

A integração tem mapeamentos de campo de dados padrão entre o Braze e o ODP. Por exemplo, o campo **E-mail** no Braze é mapeado para o campo **E-mail visto pela última vez** no ODP.

![Campos de mapa de segmento Optimizely e Braze.]({% image_buster /assets/img/optimizely/image3_emailmapfield.png %})

#### Mapear campos adicionais (opcional)

Se houver campos de dados adicionais no Braze que você deseja mapear para o ODP, faça o seguinte no ODP:

1. Na seção **Segmentos** do app, selecione o campo Braze na lista suspensa **Campos de dados de usuários do Braze**.
2. Selecione o campo ODP na lista suspensa **Campos do cliente ODP**.
3. Selecione **Salvar mapa de campo**.

![Optimizely Braze Segment Save Field Maps]({% image_buster /assets/img/optimizely/image4_mapfields.png %})

#### Excluir mapeamentos de campo não necessários (opcional)

Você também pode excluir qualquer mapeamento de campo de dados que não seja necessário. Faça o seguinte no ODP:

1. Na seção **Segmentos** do app, selecione o mapeamento de campo que deseja excluir na lista suspensa **Mapa de campo**.
2. Selecione **Excluir mapa de campo**.

![Optimizely Braze Segment Delete Field Maps]({% image_buster /assets/img/optimizely/image5_deletephonefield.png %})

### Etapa 3: Sincronizar dados da Optimizely Data Platform (ODP) com o Braze

Depois de configurar a integração, você pode definir uma ativação no ODP para sincronizar os dados de seus clientes do ODP com o Braze.

1. Acesse **Activation** > **Engage** ( **Ativação** > **Engajamento** ) e selecione **Create New Campaign (Criar nova campanha**).
2. Selecione **Behavioral (Comportamental** ) para configurar uma sincronização automatizada e recorrente.
3. Selecione **Criar do zero** e, em seguida, insira um nome para a ativação que represente os dados que você está sincronizando com o Braze (como **Braze Data Sync**).
4. Na seção **Inscrição**, é possível sincronizar dados de clientes que correspondem a um segmento ou sincronizar dados de clientes que disparam um evento (como quando o ODP registra que um cliente abre um e-mail):
   - **Clientes que correspondem a um segmento:** Selecione o segmento desejado e, em seguida, selecione **Next**.<br><br>![Optimizely Select Segment]({% image_buster /assets/img/optimizely/image6_segment.png %})
   - **Clientes que disparam um evento:** Expanda a lista suspensa **Filter (Filtro** ) e selecione o evento ODP a ser usado como disparador para essa sincronização de dados com o Braze. Em seguida, expanda **Automation Rules** e ajuste conforme desejado. <br><br>![Optimizely Trigger Event]({% image_buster /assets/img/optimizely/image7_trigger.png %})
5. Expanda **os pontos de contato**, selecione para editar **o ponto de contato 1** e, em seguida, selecione **Braze**.
6. Expanda a seção **Direcionamento** e selecione o **Identificador de destino**.
7. Selecione uma das seguintes opções para **Adicionar usuários a** na seção **Configurar**:
    - **Campanha:** Adicionar clientes a uma campanha específica no Braze. Depois de escolher essa opção, você deve selecionar a campanha do Braze.
    - **Canvas:** Adicione clientes a uma tela específica no Braze. Depois de escolher essa opção, você deve selecionar a tela Braze.
    - **Somente atualização de perfil:** Atualizar apenas o perfil do cliente Braze.
8. (Opcional) Selecione o **número de campos adicionais** que você deseja sincronizar com o Braze (até 20).  
    Em seguida, selecione o seguinte para a lista suspensa e o campo de entrada de cada campo adicional:
    - Em cada lista suspensa **Field #**, selecione o campo do Braze que deseja preencher. 
    - Em cada **valor de número de campo** correspondente, digite o campo ODP que deseja enviar para o campo Braze selecionado. Por exemplo, se você selecionou **Company Name (Nome da empresa** ) na lista suspensa **Field # (Número do campo** ), digite `{{customer.company_name}}` para o **Field # Value (Valor do número do campo)** correspondente.
9. Selecione **Salvar** e, em seguida, selecione o nome da ativação na trilha de navegação.
10. Selecione **Selecionar hora de início e programação** na seção **Pontos de contato** se tiver selecionado **Clientes que correspondem a um segmento** para a inscrição.
11. Preencha as seguintes configurações:
    - **Recorrente ou contínuo:** Selecione **Recurring (Recorrente**).
    - **Data de início:** Digite a data em que você deseja enviar os dados para o Braze.
    - **De ponta a ponta:** O padrão é **Never**. Se quiser encerrar a sincronização de dados do Braze em uma data específica, defina isso aqui.
    - **Repetições:** Definido como **Diário**.
    - **Repetir a cada** \- Defina para **1 dia**.
    - **Tempo:** Digite a hora em que deseja enviar os dados para o Braze.
    - **Fuso horário:** Selecione o fuso horário no qual você deseja enviar esses dados.
12. Selecione **Aplicar**, **Salvar** e **Acessar**. Sua sincronização começa na data e hora de início designadas (ou quando ocorre o evento de gatilho).

## Solução de problemas

### Inspecionar eventos

Para verificar se os dados estão sendo sincronizados corretamente do ODP para o Braze, você pode inspecionar os eventos no ODP.

1. No ODP, acesse **Configurações da conta** > **Inspetor de eventos**.
2. Selecione **Start Inspector**.
3. Quando os dados estão disponíveis no inspetor, um número é exibido ao lado de **Refresh (Atualizar**). Selecione para visualizar os dados.
4. Os dados brutos que o ODP e o Braze enviam para frente e para trás são exibidos. Selecione **Exibir detalhes** para ver a versão formatada desses dados brutos.
5. Os campos de dados enviados do Braze de volta ao ODP começam com `_braze`.

### Verifique os registros de atividade

Cada sincronização de dados também é registrada no [log de atividades do ODP](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP):

1. Acesse **Configurações da conta** > **Registro de atividades**.
2. Filtre as categorias por **Braze**.
3. Selecione **Exibir detalhes** para obter uma exibição formatada dos detalhes do registro, incluindo o número de correspondências.

