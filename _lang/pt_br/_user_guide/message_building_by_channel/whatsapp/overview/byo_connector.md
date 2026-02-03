---
nav_title: Conector WhatsApp BYO
article_title: Traga seu próprio conector WhatsApp
page_order: 0
description: "Este artigo de referência fornece um guia passo a passo para configurar um conector WhatsApp Traga Seu Próprio, que dá acesso ao Braze ao seu Gerenciador de Negócios WhatsApp Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Traga seu próprio conector WhatsApp

> O conector WhatsApp Traga Seu Próprio (BYO) oferece uma parceria entre Braze e Infobip, na qual você dá acesso ao Braze ao seu Gerenciador de Negócios WhatsApp (WABA) Infobip. Isso permite que você gerencie e pague pelos custos de envio de mensagens diretamente com a Infobip enquanto usa o Braze para segmentação, personalização e orquestração de campanhas. O Braze mantém toda a funcionalidade existente que o canal WhatsApp oferece, como mensagens de saída, processamento de mensagens de entrada, fluxos do WhatsApp e análise de dados.

## Solicitações 

| Requisito | Descrição |
| --- | --- |
| Conta Infobip | Uma conta Infobip é necessária para usar o conector WhatsApp BYO.
| Créditos de envio de mensagens | Você consome créditos de envio de mensagens do Braze quando envia mensagens pelo WhatsApp. |
| Requisitos do WhatsApp | Complete todos os [requisitos do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#prerequisites). |
| Número de telefone | Sugerimos que você [adquira um número de telefone através da Infobip](https://www.infobip.com/docs/numbers/getting-started) para conveniência. |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## Configurar 

Antes de configurar o conector WhatsApp BYO, confirme que o envio anterior da sua Conta de Negócios WhatsApp não foi feito através da Infobip.

### Casos suportados

- A Conta de Negócios WhatsApp e o número de telefone nunca estiveram conectados a um parceiro antes
- A Conta de Negócios WhatsApp está conectada diretamente ao Braze através da integração nativa.
    - Siga os passos em [migração do número de telefone do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration/) para migrar seus números de telefone para uma nova Conta de Negócios WhatsApp, um número de telefone por vez.
- A Conta de Negócios WhatsApp está conectada a um provedor de solução diferente do Braze e da Infobip
    - Siga os passos em [migração do número de telefone do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration/) para migrar seus números de telefone para uma nova Conta de Negócios WhatsApp, um número de telefone por vez.

## Etapa 1: Recupere as informações da conta Infobip {#step-1}

1. No Infobip, identifique a conta que você deseja usar com sua Conta do WhatsApp Business. 
2. Acesse **Ferramentas de Desenvolvedor** > **Chaves de API** e selecione **Criar Chave de API**.

![Página "Criar chave de API" com uma data de criação de "16/12/2025" e data de expiração de "16/12/36".]({% image_buster /assets/img/whatsapp/byo_connector/create_api_key.png %})

{: start="3"}
3\. Dê à chave um nome significativo, como “Braze - Meu Nome de Espaço de Trabalho - Meu Nome de WABA”.
4\. Adicione uma data de vencimento que esteja longe no futuro para evitar problemas com a expiração do token.
    \- Faça uma nota para gerar uma nova chave de API e reconectar seu WABA antes da data de vencimento.
5\. Selecione esses escopos:
- `Message:send`
- `Whatsapp:manage`
- `Whatsapp:message:send`
- `Account-management:manage`
- `Subscriptions:manage`
- `Metrics:manage`
6. Após criar a chave, copie a Chave de API.
    - A chave só pode ser copiada por um tempo limitado após a criação. Você pode repetir essas etapas para criar uma nova chave se precisar conectar outra Conta do WhatsApp Business no futuro.

!["Chave de API de Exemplo Braze" com 6 escopos adicionados.]({% image_buster /assets/img/whatsapp/byo_connector/api_key.png %})

{: start="7"}
7\. Copie a URL base da API da conta.

![Página "chaves de API" com uma URL base da API destacada.]({% image_buster /assets/img/whatsapp/byo_connector/api_base_url.png %})

## Etapa 2: Inicie o cadastro embutido

1. No Braze, acesse **Integrações de Parceiros** > **Parceiros de Tecnologia** > **WhatsApp**
2. Selecione a guia **Conector BYO - Infobip**.

![A página de Parceiros de Tecnologia do WhatsApp.]({% image_buster /assets/img/whatsapp/byo_connector/byo_tab_tech_parners.png %})

{: start="3"}
3\. Insira a chave de API e a URL base de [Etapa 1](#step-1).
4\. Selecione **Conectar**.
5\. Prossiga pelo [fluxo de trabalho de Cadastro Embutido]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/#whatsapp-embedded-signup-workflow) com estas considerações:
- Você não pode selecionar o mesmo portfólio de negócios que é usado por um provedor de soluções de negócios diferente.
- Você não pode selecionar um número de telefone que está sendo usado por outro Provedor de Solução Empresarial.
- Você deve criar um novo WABA, não selecionar um existente.

{% alert note %}
Para receber o código de verificação, acesse seu dashboard do Infobip > **Abrir** > **Logs**, e pegue o código da mensagem SMS recebida.  
{% endalert %}

![Registros de mensagens mostrando uma mensagem SMS recebida com o código de verificação.]({% image_buster /assets/img/whatsapp/byo_connector/verification_code.png %})

Após concluir a configuração, seu número de telefone é listado como um grupo de inscrições sob seu Grupo do WhatsApp Business. O Grupo do WhatsApp Business contém o nome da conta Infobip e a URL base da API à qual está conectado. Contas conectadas através da integração nativa não têm um nome de conta Infobip.

{% alert note %}
Conecte cada Conta do WhatsApp Business a uma única conta Infobip. Cada vez que você conectar um número de telefone adicional ou grupo de inscrições, se a Conta do WhatsApp Business já estiver conectada a uma conta Infobip, você deve reinserir as credenciais da API para a conta existente.
{% endalert %}

## Etapa 3: Enviando mensagens

Siga o processo de envio da integração nativa, incluindo:
- [Inscrevendo usuários no grupo de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/)
- [Criação de uma mensagem do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/)

## Resolvendo problemas de configuração

### Não foi possível recuperar o ID da Conta do WhatsApp Business

Confirme que sua Conta do WhatsApp Business não está conectada a um espaço de trabalho Braze diferente.

### Não foi possível compartilhar o ID da Conta do WhatsApp Business com o Infobip

1. Confirme que sua Conta do WhatsApp Business não está conectada ao Braze ou a outro parceiro.
2. Confirme que nenhum número de telefone em sua Conta do WhatsApp Business está conectado a uma conta Infobip diferente. Para números importados, você pode encontrar o número no Infobip e selecionar **Cancelar número**.

![O botão "Cancelar número" para um número Infobip.]({% image_buster /assets/img/whatsapp/byo_connector/cancel_number.png %})

## Considerações 


Embora toda a funcionalidade existente com o Braze seja suportada, esses casos de uso atualmente não são suportados.

| Caso de uso | Motivo |
| --- | --- |
| Processando mensagens recebidas no Braze e Infobip | Isso impede trens de lógica que são acionados por qualquer um dos sistemas, gerando, consequentemente, threads de mensagens duplicadas e potencialmente contraditórias. |
| Enviando mensagens do Braze e Infobip | Para contas do WhatsApp Business conectadas ao Braze, todo o envio se origina do Braze. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

