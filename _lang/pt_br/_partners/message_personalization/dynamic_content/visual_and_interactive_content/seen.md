---
nav_title: Visto
article_title: Visto
description: "Visto permite experiências de vídeo personalizadas em grande escala, ajudando marcas a aumentar o engajamento ao longo da jornada do cliente."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# Visto

> [Visto](https://seen.io) permite que marcas criem e entreguem experiências de vídeo personalizadas em grande escala. Com o Visto, você pode projetar um vídeo em torno dos seus dados, personalizá-lo em grande escala na nuvem e, em seguida, distribuí-lo onde funciona melhor.
>
> A integração entre Braze e Visto permite que você envie dados de usuários do Braze para o Visto, gere vídeos personalizados dinamicamente e retorne ativos de vídeo—como uma URL de player única e miniatura—de volta ao Braze para uso em campanhas e Canvases.


## Casos de uso

O Visto suporta entrega automatizada de vídeo personalizado ao longo do ciclo de vida do cliente, incluindo:

- **Integração**: Dê as boas-vindas a novos usuários com vídeos personalizados para seu perfil ou contexto de inscrição
- **Conversão e ativação**: Reforce ações-chave com mensagens de vídeo contextuais
- **Fidelidade e upsell**: Destaque ofertas personalizadas ou marcos de uso
- **Recuperar e prevenção de churn**: Reengaje usuários inativos com conteúdo de vídeo personalizado


## Pré-requisitos

Antes de começar, você precisa do seguinte:

| Pré-requisito | Descrição |
|--------------|-------------|
| Acesso à Plataforma Visto | Você precisa de uma assinatura da Plataforma Visto ou de uma campanha ativa do Visto. Você precisa de acesso às configurações do seu Espaço de Trabalho para recuperar seu ID de Espaço de Trabalho e gerar um token de API. |
| URL do webhook de transformação de dados do Braze | A Transformação de Dados do Braze reformata os dados recebidos do Visto para que possam ser aceitos pelo endpoint /users/track do Braze. |
| Dados de usuários do Braze | A personalização de vídeo requer dados em nível de usuário. Certifique-se de que os atributos relevantes estejam disponíveis no Braze e que você passe **braze_id** como o identificador único. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}




## Como funcionam as Jornadas Vistas

O Seen usa [Jornadas](https://docs.seen.io/journey) para controlar como os dados recebidos são processados e como os vídeos são gerados.

Uma Jornada é um fluxo de trabalho configurável que:
- Recebe dados de sistemas externos (como o Braze)
- Aplica lógica e regras de personalização
- Gera um vídeo e ativos associados
- Retorna uma carga útil de resposta configurável

As Jornadas são compostas por **nós**, cada um com uma função específica:

- **nó de Disparo**: Define como e quando uma Jornada começa (para integrações com o Braze, use um `On Create` disparador)
- **nó Condicional**: Roteia usuários através de diferentes caminhos lógicos com base nos valores dos dados
- **nó de Projeto**: Aplica personalização dinâmica de vídeo usando os dados recebidos
- **nó de Player**: Gera uma URL de player de vídeo única
- **nó de Webhook**: Define a carga útil de resposta enviada de volta ao Braze

Como as respostas da Jornada são configuráveis, certifique-se de que os campos de saída retornados pelo Seen correspondam aos atributos esperados pela sua Transformação de Dados do Braze.


## Limite de taxa
A API Seen aceita até 100 chamadas a cada 10 segundos.


## Integração

Neste exemplo, a Braze envia dados de usuários para a Seen para gerar um vídeo personalizado. A Seen então retorna uma URL única do player de vídeo e uma URL de miniatura, que são armazenadas como atributos personalizados na Braze para uso no envio de mensagens.

Se você tiver várias campanhas de vídeo com a Seen, repita o processo para conectar a Braze com todas as campanhas de vídeo.

### Etapa 1: Crie uma campanha de webhook para enviar dados para a Seen

Crie uma nova [Campanha de Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) na Braze.

Configure o webhook da seguinte forma:

- **URL do webhook**:  
  `https://next.seen.io/v1/workspaces/{WORKSPACE_ID}/data`  
  Encontre seu ID de Espaço de Trabalho nas configurações da Plataforma Seen.

- **Método HTTP**: POST
- **Corpo da solicitação**: Texto bruto  
  Use o seguinte exemplo como ponto de partida. Consulte a [documentação de criação de dados da Seen](https://docs.seen.io/create-data) para mais informações.

{% raw %}
```json
{
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "id": "{{${braze_id}}}"
}
```
{% endraw %}
- **Cabeçalhos de solicitação**:
  - `Authorization`: Portador `{Seen_API_TOKEN}`
  - `Content-Type`: `application/json`

  > Gere um [token de API](https://docs.seen.io/authorization) na Plataforma Seen nas configurações do Espaço de Trabalho. Você pode entrar em contato com seu gerente de sucesso do cliente da Seen para obter assistência.

- Para testar o webhook com um usuário, mude para a guia **Teste**.
- Após confirmar que o teste funciona como pretendido, complete a configuração do webhook.


### Etapa 2: Configure uma Jornada na Plataforma Seen

A Seen usa [Jornadas](https://docs.seen.io/journey) para definir como os dados recebidos são processados, personalizados e retornados à Braze.  
Cada Jornada é um fluxo de trabalho configurável composto por nós que permitem controlar tanto a lógica de geração de vídeo quanto a carga útil da resposta.

Para configurar sua Jornada:

1. Crie uma nova Jornada na Plataforma Seen
2. Adicione um **nó de Trigger** e selecione o `On Create` trigger  
   Isso garante que a Jornada comece quando a Braze enviar dados para o Seen. Crie e adicione qualquer lógica de [segmentação](https://docs.seen.io/segments) dentro do seu espaço de trabalho, se necessário.
3. Construa sua lógica usando os seguintes nós conforme necessário:
   - **nó Condicional**: Roteie usuários com base em valores de atributos (por exemplo, tipo de plano ou região)
   - **nó de Projeto**: Aplique personalização dinâmica de vídeo usando os dados recebidos
   - **nó de Player**: Gere uma URL única do player de vídeo
4. Adicione um **nó de Webhook** para definir a resposta enviada de volta para a Braze

#### Requisitos de resposta do nó Webhook

Como a carga útil da resposta é configurável, certifique-se de que os seguintes campos sejam retornados para suportar a Transformação de Dados da Braze descrita na próxima etapa:

| Campo | Descrição |
|------|-------------|
| `id` | Deve corresponder ao `braze_id` enviado pela Braze |
| `player_url` | URL única para o player de vídeo personalizado |
| `email_thumbnail_url` | URL da miniatura do vídeo gerado |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Se o seu caso de uso exigir atributos adicionais, inclua-os na resposta e mapeie-os na Braze.


### Etapa 3: Crie uma Transformação de Dados para receber dados do Seen

Use as Transformações de Dados da Braze para ingerir a resposta da Jornada Seen e armazenar ativos de vídeo no perfil do usuário.

1. Crie os seguintes [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) na Braze:
   - `player_url`
   - `email_thumbnail_url`
2. Navegue até **Configurações de Dados** → **Transformação de Dados** e clique em **Criar transformação**
3. Configure a transformação:
   - **Começar do zero**
   - **Destino** → POST: rastreia usuários
4. Compartilhe a URL do webhook gerado com o Seen, ou adicione-a diretamente ao **nó do Webhook** da Jornada
5. Use o seguinte código de transformação:

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.id,
      "_update_existing_only": true,
      "player_url": payload.player_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```

{: start="6"}
6\. Envie uma carga útil de teste para o endpoint fornecido. Envie dados para a Plataforma Seen para executar sua Jornada, ou envie a carga útil diretamente para a Braze com [Postman](https://www.postman.com/) ou outro serviço similar.
7\. Selecione **Validar** para garantir que tudo funcione como pretendido.
8\. Selecione **Save** and **Activate** (Salvar e ativar).