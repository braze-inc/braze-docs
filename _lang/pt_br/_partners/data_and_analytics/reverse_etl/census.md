---
nav_title: Census
article_title: Census
description: "Este artigo de referência descreve a parceria entre o Braze e a Census, uma plataforma de integração de dados que permite criar dinamicamente segmentos de usuários direcionados com dados de seu data warehouse na nuvem."
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# Census

> A [Census](https://www.getcensus.com/) é uma plataforma de ativação de dados que conecta data warehouses em nuvem, como Snowflake e BigQuery, à Braze. As equipes de marketing podem aproveitar o poder de seus dados primários para criar segmentos de público dinâmicos, sincronizar atributos personalizados de clientes para personalizar campanhas e manter atualizados todos os seus dados no Braze. É mais fácil do que nunca agir com dados confiáveis e acionáveis, sem necessidade de fazer upload de CSV nem de pedir favores à equipe de engenharia.

A integração entre Braze e Census permite que você importe dinamicamente dados de públicos ou produtos para o Braze para enviar campanhas personalizadas. Por exemplo, você pode criar um coorte no Braze para "Assinantes de boletim informativo com CLV > 1000" para direcionar clientes de alto valor ou "Usuários ativos nos últimos 30 dias" para direcionar usuários específicos para testar um recurso beta futuro.

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
| Conta do Census | É necessário ter uma [conta Census](https://www.getcensus.com/) para aproveitar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com todas as permissões de dados de usuários (exceto `users.delete`) e permissões de `segments.list`. O conjunto de permissões pode mudar à medida que o Census adiciona suporte a mais objetos Braze, portanto, talvez você queira conceder mais permissões agora ou planejar a atualização dessas permissões no futuro. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze  | Sua URL de endpoint REST. Seu endpoint dependerá do [URL do Braze para sua instância]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
| Data warehouse e modelo de dados | Antes de iniciar a integração, você deve ter um data warehouse configurado no Census e definir um modelo do subconjunto de dados que deseja sincronizar com o Braze. Visite [a documentação do Census](https://docs.getcensus.com/destinations/braze) para obter uma lista de fontes de dados disponíveis e orientações sobre a criação de modelos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integração

### Etapa 1: Criar conexão de serviço Braze

Para integrar o Census na plataforma Census, navegue até a guia **Connections (Conexões)** e selecione **New Destination (Novo destino** ) para criar uma nova conexão de serviço Braze.

No prompt exibido, nomeie essa conexão e forneça o URL do endpoint do Braze e a chave da API REST do Braze (e, opcionalmente, sua chave de importação de dados para sincronizar coortes).

![]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Etapa 2: Criar uma sincronização do Census

Para sincronizar clientes com o Braze, você deve criar uma sincronização. Aqui, você definirá onde sincronizar os dados e como deseja que os campos sejam mapeados entre as duas plataformas.

1. Navegue até a guia **Syncs (Sincronizações** ) e selecione **New Sync (Nova sincronização**).<br><br> 
2. No criador, selecione o modelo de dados de origem do seu data warehouse.<br><br>
3. Configure o local para onde o modelo será sincronizado. Selecione **Braze** como destinos e o [tipo de objeto compatível](#supported-objects) a ser sincronizado.<br>![No prompt "Select a Destination", "Braze" é selecionado como a conexão e vários objetos são listados.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Selecione a regra de sincronização que deseja aplicar**(Atualizar ou Criar** é a opção mais comum, mas você pode escolher regras mais avançadas para lidar com a exclusão de dados, por exemplo).<br><br>
5. Em seguida, para fins de correspondência de registros, escolha uma chave de sincronização para [mapear](#supported-objects) o objeto do Braze para um campo do modelo.<br>![No prompt "Select a Sync Key" (Selecionar uma chave de sincronização), a "External User ID" (ID de usuário externo) do Braze corresponde a "user_id" na origem.]({% image_buster /assets/img/census/census_1.png %}){: style="max-width:80%;"}<br><br>
6. Por fim, mapeie os campos de dados do Census para os campos equivalentes do Braze.<br>![Mapeamento do Census]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
7. Confirme os detalhes e crie a sincronização. 

Após a execução da sincronização, você encontrará os dados de usuários na Braze. Agora é possível criar e adicionar um segmento Braze a futuras campanhas Braze e Canvas para direcionamento a esses usuários. 

{% alert note %}
Ao usar a integração do Census e do Braze, o Census enviará apenas os deltas (dados alterados) em cada sincronização para o Braze.
{% endalert %}

## Objetos suportados

Atualmente, o Census oferece suporte à sincronização dos seguintes objetos Braze:

| Nome do objeto | Comportamentos de sincronização |
| --- | --- |
| Usuário | Atualizar, criar, espelhar, excluir |
| Coorte | Atualizar, criar, espelhar | 
| Catálogo | Atualizar, criar, espelhar |
| Associação ao grupo de inscrições | Espelho |
| Evento | Anexar |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Além disso, o Census oferece suporte ao envio de [dados estruturados](https://docs.getcensus.com/destinations/braze#supported-objects) para o Braze: 
- Tokens por push do usuário: Para enviar tokens por push, seus dados devem ser estruturados como um vetor de objetos com 2 ou 3 valores: `app_id`, `token` e um `device_id` opcional.
- Atributos personalizados aninhados: Há suporte para objetos e vetores de objetos. Em abril de 2022, esse recurso ainda estava em acesso antecipado. Talvez seja necessário entrar em contato com o gerente da sua conta da Braze para obter acesso.

