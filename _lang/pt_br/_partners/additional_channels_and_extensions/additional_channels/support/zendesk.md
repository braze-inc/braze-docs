---
nav_title: Zendesk
article_title: Zendesk
description: "Este artigo de referência descreve a parceria entre Braze e a Zendesk, um pacote de suporte popular que permite utilizar webhooks da Braze para sincronizar dados de suporte entre as duas plataformas."
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# Zendesk

> Com o [Zendesk Support Suite](https://www.zendesk.com/support-suite/), as empresas podem ter conversas naturais com clientes por meio de atendimento omnicanal, por e-mail, chat na web, voz ou apps de mensagens em redes sociais. A Zendesk oferece um sistema de criação de tickets simplificado que valoriza o rastreamento e a priorização das interações, permitindo que as empresas tenham uma visão histórica unificada de seus clientes.

A integração de servidor para servidor entre a Braze e a Zendesk permite permite usar: 
- Webhooks do Braze para automatizar a criação de tickets de suporte no Zendesk devido ao engajamento com mensagem nas jornadas dos usuários no Braze. Por exemplo, após implementar e testar com sucesso uma integração, a Braze pode criar um ticket de suporte a partir de um usuário respondendo negativamente a uma mensagem no app "Gostando do nosso app?", permitindo que sua equipe de suporte acompanhe o cliente.
- Webhooks do Zendesk para suportar casos de uso bidirecionais, como atualizar o perfil do usuário no Braze devido a atividades no Zendesk. Por exemplo, após um ticket ser resolvido, registre um evento no perfil do usuário na Braze.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta do Zendesk | Uma conta de administrador do [Zendesk](https://`<your-zendesk-instance>`.zendesk.com/agent/admin) é necessária para aproveitar esta parceria. |
| Token da API da Zendesk | Um token de API do Zendesk](https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-) é necessário para enviar solicitações do Braze para o endpoint de ticket do Zendesk. |
| Identificador comum (recomendado) | É recomendável um [identificador comum](#common-identifier) entre Braze e Zendesk. |
| chave de API Braze | Uma chave de API da Braze é necessária para enviar solicitações do Zendesk para um endpoint da Braze. Certifique-se de que a chave de API que você usa tem as permissões corretas para o endpoint do Braze que seu webhook do Zendesk está usando. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração do Braze com o Zendesk

### Etapa 1: Crie seu webhook do Braze

Para criar um webhook:

- **Campanhas:** Acessar a página **Campanhas** no dashboard da Braze. Clique **Criar Campanha** e selecione **Webhook**.
- **Canvas:** De um canva novo ou existe, crie uma etapa completa ou de mensagem no construtor de canva. Em seguida, clique em **Mensagens** e selecione **Webhook** nas opções de mensagem.

No seu webhook, preencha os seguintes campos:
- **URL do webhook**: `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **Corpo da solicitação**: Texto bruto

Outros casos de uso podem ser tratados por meio das [APIs de suporte do Zendesk](https://developer.zendesk.com/rest_api/docs/support/introduction), que alterariam o ponto de extremidade `/api/v2/` adequadamente no final do URL do webhook.

#### Cabeçalho e método da solicitação

O Zendesk requer um cabeçalho HTTP para autorização e um método HTTP. Na guia **Configurações**, substitua o <email_address> pelo e-mail do administrador do Zendesk e o <api_token> pelo token da API do Zendesk.

- **Método HTTP**: POST
- **Cabeçalhos de solicitação**:
  - **Autorização**: Básico {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![]({% image_buster /assets/img_archive/zendesk_step1.gif %}){: style="max-width:70%;"}

#### Corpo da solicitação

Defina os detalhes do ticket, como tipo, assunto e status, na sua carga útil do webhook. Os detalhes do ticket são extensíveis e personalizados com base na [API de tickets do Zendesk](https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket). Use o exemplo a seguir para ajudar a estruturar sua carga útil e inserir os campos desejados.

{% raw %}
```json
{% assign ticket_type = 'question/incident/task/problem' %} << Choose one >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Your message here >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}", 
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "urgent",
"status": "{{ ticket_status }}"
  }
}
```
{% endraw %}

### Etapa 2: veja uma prévia da sua solicitação

Seu texto bruto será automaticamente destacado se for uma tag Braze aplicável.

Pré-visualize a solicitação no painel **Preview (Pré-visualização)** ou navegue até a guia **Test (Teste)**, onde é possível selecionar um usuário aleatório, um usuário existente ou personalizar o seu próprio usuário para testar o webhook.

Por fim, verifique se o ticket foi criado no lado do Zendesk.

## Identificador comum

Se você tem um identificador comum entre a Braze e a Zendesk, é recomendável utilizá-lo como o `requester_id`. Isso ajudará a unificar os dois conjuntos de usuários. Alternativamente, se não for o caso, recomendamos passar um conjunto de atributos identificadores, como nome, endereço de e-mail, número de telefone ou outros.

## integração do Zendesk com o Braze

### Etapa 1: Criar um webhook

1. No [Centro de Administração](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), clique em **Aplicativos e integrações** na barra lateral e selecione **Webhooks > Webhooks**.<br><br>
2. Clique em **Criar webhook**.<br><br>
3. Selecione **disparar** ou **Automação** e clique em **Próximo**.<br>![]({% image_buster /assets/img_archive/zendesk2.png %}){: style="max-width:70%;"}<br><br>
4. Forneça as seguintes informações no seu webhook:
- Digite um nome e uma descrição para o webhook.
- Insira o URL do endpoint da Braze que seu webhook usará. {% raw %}Nosso exemplo usará `https://{{instance_url}}/users/track`.{% endraw %}
- Selecione POST como o método de solicitação do webhook e defina o formato da solicitação para JSON.
- Selecione o método de autenticação do token portador para o webhook e forneça sua [chave de API da Braze]({{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys).
  - Certifique-se de que a chave de API que você está usando tem as [permissões corretas]({{site.baseurl}}/api/basics/#rest-api-key-permissions) para o endpoint Braze que seu webhook está usando.<br><br>
5. (Recomendado) Teste o webhook para verificar se está funcionando corretamente.<br><br>
6. Para disparar e automatizar webhooks, você deve conectar o webhook a um gatilho ou automação antes de finalizar a configuração. Consulte a seguinte para o nosso exemplo de criar um para o webhook. Depois que o disparador é criado, você pode voltar a esta página e selecionar **Finalizar configuração**.

### Etapa 2: Criar um disparar ou automação

[Siga as instruções da Zendesk](https://support.zendesk.com/hc/en-us/articles/4408839108378#topic_bwm_1tv_dpb) sobre como conectar seu webhook a um disparar ou automação.

Nosso exemplo abaixo usará um disparar para invocar o webhook quando o status de um caso de suporte for alterado para "Resolvido" ou "Fechado". 

1. No **Centro de Administração**, clique em **Objetos e regras** na barra lateral, depois selecione **Regras de negócios > Gatilhos**.<br><br>
2. Selecione **Adicionar disparar**.<br><br>
3. Nomeie seu gatilho e selecione uma categoria.<br><br>
4. Selecione **Adicionar condição** para configurar quais condições devem disparar o webhook. Por exemplo, "Categoria de status alterada para fechada" ou "Categoria de status alterada para resolvida".![]({% image_buster /assets/img_archive/zendesk1.png %}){: style="max-width:70%;"}<br><br>
5. Selecione **Adicionar ação**, escolha **Notificar webhook ativo**, e selecione no menu suspenso o webhook criado na etapa anterior.<br><br>
6. Defina o corpo JSON para estar em conformidade com seu endpoint Braze, usando os espaços reservados de variáveis do Zendesk para preencher dinamicamente os campos relevantes.<br>![]({% image_buster /assets/img_archive/zendesk3.png %}){: style="max-width:70%;"}<br><br>
7. Selecione **Criar**.<br><br>
8. Retorne ao seu webhook e clique em **Finish setup** (Concluir configuração).


