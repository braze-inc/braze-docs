---
nav_title: Fidelidade aberta
article_title: Fidelidade aberta
description: "A integração entre o Braze e o Open Loyalty permite que você sincronize dados de fidelidade, como saldo de pontos, alterações de nível e avisos de vencimento, diretamente no Braze em tempo real."
alias: /partners/openloyalty/
page_type: partner
search_tag: Partner
---

# Fidelidade aberta

> [O Open Loyalty](https://www.openloyalty.io/) é uma plataforma de programa de fidelidade baseada na nuvem que permite criar e gerenciar programas de fidelidade e recompensas para clientes. A integração entre o Braze e o Open Loyalty sincroniza dados de fidelidade, como saldo de pontos, alterações de nível e avisos de vencimento, diretamente no Braze em tempo real. Isso permite disparar mensagens personalizadas (e-mail, push, SMS) quando o status de fidelidade de um usuário muda.

_Essa integração é mantida pela Open Loyalty_

## Sobre a integração

Essa integração usa o Braze Data Transformations para capturar webhooks do Open Loyalty e mapeá-los para os perfis de usuários do Braze.

* **Atualizações em tempo real**: Empurre os eventos de fidelidade (pontos ganhos, upgrades de nível) para o Braze.
* **Personalização**: Use atribuições de fidelidade (saldo atual, nome do próximo nível) em seus modelos Braze.
* **Bi-direcional**: Atualize os atributos personalizados do cliente do Open Loyalty com base nos dados de engajamento do Braze.

## Casos de uso

Essa integração abrange os seguintes fluxos de dados:

1. **Sincronização de eventos com o Braze (entrada)**: Rastreie alterações de pontos, upgrades de níveis ou resgates de recompensas enviando dados do Open Loyalty para o Braze. A transformação de dados converte esses dados em um evento de usuário.
2. **Modificação de membros de fidelidade em aberto (saída)**: Atualize automaticamente os dados de usuários no Open Loyalty com base no comportamento do usuário no Braze, como adicionar etiquetas "VIP" ou atualizar atributos personalizados.

## Pré-requisitos

Antes de começar, você precisa dos seguintes itens:

| Requisito | Descrição |
| :--- | :--- |
| Abrir uma conta de fidelidade | É necessário ter uma conta de administrador em um locatário com fidelidade aberta para aproveitar essa parceria. |
| Chave da API REST do Open Loyalty | Uma chave da API REST do Open Loyalty (para integrações que enviam dados do Braze para o Open Loyalty). <br><br> Crie isso em **Configurações > Administradores > Chaves de API**. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Crie essa chave no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Transformação de Dados Braze | É necessário acessar a guia "Data Settings" (Configurações de dados) no Braze para configurar os ouvintes de webhook. |
| IDs correspondentes | O `external_id` do usuário no Braze deve corresponder ao `loyaltyCardNumber` (ou outro identificador padrão) no Open Loyalty. |
| Tenant ID | Seu Open Loyalty Tenant ID (necessário para atualizações de saída). |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Integração

A integração primária sincroniza os eventos do webhook do Open Loyalty com o Braze usando a transformação de dados.

### Etapa 1: Gerar o URL do webhook no Braze

Primeiro, crie uma transformação de dados no Braze para gerar um URL exclusivo para receber dados.

1.  No Braze, abra **Configurações de dados > Transformação de dados**.
2.  Clique em **Create Transformation (Criar transformação**).
3.  Preencha os seguintes campos:
     * **Nome da transformação**: Forneça um nome descritivo (por exemplo, "Open Loyalty Point Update Events").
     * **Selecione os destinos**: Selecione **POST: Rastreamento de usuários**.
4.  Clique em **Create Transformation (Criar transformação**).
5.  Localize o **URL do webhook** no lado direito e clique em **Copiar**.

{% alert important %}
Mantenha esse URL em segurança; você precisará dele para a próxima etapa.
{% endalert %}

### Etapa 2: Criar a inscrição do webhook no Open Loyalty

Diga ao Open Loyalty para enviar eventos específicos para o URL que você acabou de gerar.

1.  Faça o registro no painel de administração do Open Loyalty.
2.  Navegue até **Geral > Webhooks**.
3.  Clique em **Adicionar novo webhook** e configure a inscrição:
    * **eventName**: Selecione o evento que deseja rastrear (por exemplo, `AvailablePointsAmountChanged`, `CustomerLevelChanged`, ou `CampaignEffectWasApplied`).
    * **url**: Cole o URL do Webhook do Braze da etapa 1.
    * Adicione os seguintes cabeçalhos:
      * `Content-Type: application/json`
      * `User-Agent: partner-OpenLoyalty`
4.  Salve a inscrição do webhook.

### Etapa 3: Configurar a transformação de dados

Escreva a lógica JavaScript no Braze para mapear a carga útil de entrada do Open Loyalty para as propriedades do Braze.

1.  No Braze, abra a transformação de dados que você criou na etapa 1.
2.  Dispare o evento no Open Loyalty (por exemplo, altere os pontos de um associado ou atribua um nível) para gerar uma carga útil de amostra no painel **de detalhes do webhook**.
3.  No editor **de código de transformação**, escreva um script para mapear os dados de entrada. Use o exemplo a seguir como um guia:

```javascript
// 1. Parse the incoming Open Loyalty payload
const data = payload.data;

// 2. Construct the Braze API body
let brazecall = {
  "events": [
    {
      // CRITICAL: Map the identifier (e.g., loyaltyCardNumber -> external_id)
      "external_id": data.customer.loyaltyCardNumber,
     
      // Define the Event Name (what you see in Braze)
      "name": "Loyalty Event Triggered",
     
      // timestamp
      "time": new Date().toISOString(),
     
      // Map specific properties you want to use in emails/segments
      "properties": {
        "event_type": payload.type, // for example, 'AvailablePointsAmountChanged'
        "new_balance": data.amount,
        "change_amount": data.amountChange,
        "tier_name": data.tier ? data.tier.name : null
      }
    }
  ]
};

return brazecall;
```

{: start="4"}
4\. Clique em **Validate (Validar** ) para garantir que o código seja executado em sua carga útil de amostra e, em seguida, clique em **Activate (Ativar**).


## Usando o Open Loyalty com o Braze

Depois de concluir a integração de entrada, configure **as atualizações de saída** para modificar os membros do Open Loyalty com base no comportamento do Braze.

### Etapa 1: Configurar a campanha do Braze Webhook

Esse processo usa Braze Webhooks para enviar uma solicitação `PATCH` para a API de fidelidade aberta (por exemplo, para adicionar uma etiqueta "VIP").

1.  No Braze, crie uma nova **campanha de webhook** (ou use um webhook em uma tela).
2.  Clique em **Criar Webhook**.
3.  **URL do webhook**: Construa o URL usando sua instância do Open Loyalty, o Tenant ID e a variável Braze Liquid para o ID do usuário.
    * Formato:
      {% raw %}
      `https://<YOUR_OL_INSTANCE>/api/<TENANT_ID>/member/loyaltyCardNumber={{${user_id}}}`
      {% endraw %}
4. Preencha os seguintes campos:   
    * **Método de solicitação**: `PATCH`
    * **Cabeçalhos de solicitação**:
      * `Content-Type`: `application/json`
      * `X-AUTH-TOKEN`: `<YOUR_PERMANENT_TOKEN>`
      * `User-Agent: Braze`
5.  **Corpo da solicitação**: Selecione `Raw text` e cole a carga útil:

```json
{
  "customer": {
    "labels": [
      {
        "key": "braze_vip_segment",
        "value": "optedIn"
      }
    ]
  }
}
```

### Etapa 2: Configurar o disparador

1.  Navegue até a guia **Programação de** **entrega** ou **de entrada**.
2.  Preencha os seguintes campos:
    * **Método de entrega**: Baseado em ações.
    * **Disparar**: Defina o disparo relevante (por exemplo, um usuário insere um segmento específico no Braze).
    * **Lançamento**: Ativar a campanha.

## Solução de problemas

### Verificar eventos de entrada
Quando a Transformação de dados está ativa, os dados aparecem no Braze como um evento personalizado. Verifique isso criando uma campanha com um disparador **Perform Custom Event** e verificando se o evento definido (por exemplo, `Loyalty Event Triggered`) está disponível.

### Verificação de webhooks de saída
Verifique o registro de atividade de mensagens no Braze para garantir que o webhook retornou um status `200 OK`.
* **Erro 401**: Verifique seu token da Open Loyalty API.
* **Erro 404**: O ID do usuário no Braze não existe no Open Loyalty.