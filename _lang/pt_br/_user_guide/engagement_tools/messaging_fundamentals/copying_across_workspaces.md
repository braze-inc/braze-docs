---
nav_title: Copiando entre espaços de trabalho
article_title: Cópia entre espaços de trabalho
page_order: 4.5
alias: "/copying_to_workspaces/"
page_type: reference
description: "Este artigo de referência fornece uma visão geral de como copiar campanhas e telas para diferentes espaços de trabalho."
tool:
    - Campaigns
    - Canvas
---

# Cópia de campanhas e telas entre espaços de trabalho

> Copiar campanhas entre espaços de trabalho permite que você inicie a composição da sua mensagem começando com uma cópia de uma campanha em um espaço de trabalho diferente. Esta página cobre como copiar campanhas para diferentes espaços de trabalho e lista o que é e o que não é copiado.

Ao copiar uma campanha ou um Canva para um espaço de trabalho diferente, a cópia permanecerá como rascunho até que seja editada e lançada, ajudando-o a manter e desenvolver suas estratégias de envio de mensagens bem-sucedidas.

{% tabs local %}
{% tab campanhas %}

{% alert important %}
A cópia de campanhas entre espaços de trabalho está geralmente disponível. O suporte de canal para cartões de conteúdo não está disponível no momento.
{% endalert %}

Você pode copiar campanhas entre espaços de trabalho para esses canais compatíveis: SMS, mensagens no app, notificações por push, e-mail e webhooks. Você também pode copiar modelos de e-mail, sinalizadores de recursos e blocos de conteúdo. Observe que campanhas multicanal com canais não suportados não podem ser copiadas para um espaço de trabalho diferente.

Para copiar uma campanha em um espaço de trabalho diferente:

1. Selecione o ícone de engrenagem <i class="fas fa-cog"></i> ao lado da campanha selecionada.
2. Selecione **Copy to workspace (Copiar para o espaço de trabalho**). 
3. Depois de copiar, revise e teste sua campanha para confirmar que todos os campos funcionam corretamente.

{% endtab %}
{% tab canvas %}

{% alert important %}
A cópia de telas entre espaços de trabalho está geralmente disponível. Os canais a seguir não são compatíveis no momento: LINE, cartões de conteúdo e WhatsApp.
{% endalert %}

Você pode copiar Canvas entre espaços de trabalho para estes canais compatíveis: e-mail, mensagens no app, push, webhooks e SMS.

Para copiar um Canva em um espaço de trabalho diferente:

1. Selecione o menu <i class="fa-solid fa-ellipsis-vertical"></i> ao lado da tela selecionada.
2. Selecione **Copy to workspace (Copiar para o espaço de trabalho**). 
3. Depois de copiar, revise e teste seu Canva para confirmar que todos os campos funcionam corretamente.

Ao copiar um Canvas com etapas do Audience Sync, as configurações não serão copiadas para o espaço de trabalho de destino, mas as etapas da jornada serão.

{% endtab %}
{% endtabs %}

## O que é copiado entre espaços de trabalho

Note que a lista a seguir não é uma lista abrangente do que é copiado entre os espaços de trabalho e do que é omitido. Como prática recomendada, verifique os detalhes da campanha e do Canva e teste para confirmar que sua mensagem funciona conforme o esperado.

### Informações

{% tabs local %}
{% tab campanhas %}

| Copiado | Omitido |
|---|---|
| Descrição | Territórios | 
| Tipo | Tags | 
| Ações (aninhadas) | Segmentos | 
| Comportamentos de conversão (aninhados) | Aprovações | 
| Configurações de tempo de silêncio | Cronograma de disparo | 
| Configurações de limitação de frequência | Resumos de campanhas | 
| Estado de inscrição do destinatário |  | 
| Agenda recorrente |  | 
| É Transacional |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Descrição | Territórios | 
| Tipo | Tags | 
| Ações (aninhadas) | Segmentos | 
| Comportamentos de conversão (aninhados) | Aprovações | 
| Configurações de tempo de silêncio | Cronograma de disparo | 
| Configurações de limitação de frequência | Resumos do Canva | 
| Estado de inscrição do destinatário |  | 
| Agenda recorrente |  | 
| É Transacional |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Comportamentos de conversão

{% tabs local %}
{% tab campanhas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs de espaços de trabalho |
| Interação de campanha |  ID da campanha | 
| Nome do evento personalizado |  | 
| Nome do produto |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs de espaços de trabalho |
| Interação com a tela |  ID do canva | 
| Nome do evento personalizado |  | 
| Nome do produto |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Ações

{% tabs local %}
{% tab campanhas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs de espaços de trabalho |
| Interação de campanha |  ID da campanha | 
| Nome do evento personalizado |  | 
| Nome do produto |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs de espaços de trabalho |
| Interação com a tela |  ID do canva | 
| Nome do evento personalizado |  | 
| Nome do produto |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Variações de mensagens

{% tabs local %}
{% tab campanhas %}

| Copiado | Omitido |
|---|---|
| Enviar porcentagem | ID da API |
| Tipo |  IDs do grupo de teste | 
|  |  IDs de modelo de link | 
|  |  IDs de grupo de usuários internos | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Enviar porcentagem | ID da API |
| Tipo |  IDs do grupo de teste | 
|  |  IDs de modelo de link | 
|  |  IDs de grupo de usuários internos | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}


### Variação da mensagem de e-mail

{% tabs local %}
{% tab campanhas %}

| Copiado | Omitido |
|---|---|
| Corpo do e-mail | Endereço de origem |
| Extras de mensagem |  Responder a | 
| Título |  CCO | 
| Assunto |  Modelo de link | 
|  |  Apelidamento de link |
|  | Traduções |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Corpo do e-mail | Endereço de origem |
| Extras de mensagem |  Responder a | 
| Título |  CCO | 
| Assunto |  Modelo de link | 
|  |  Apelidamento de link |
|  | Traduções |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Corpo do e-mail

{% tabs local %}
{% tab campanhas %}

| Copiado | Omitido |
|---|---|
| Texto simples | Apelidamento de link |
| HTML e conteúdo de arrastar e soltar | Traduções | 
| pré-cabeçalho |  | 
| CSS embutido |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Texto simples | Apelidamento de link |
| HTML e conteúdo de arrastar e soltar | Traduções | 
| pré-cabeçalho |  | 
| CSS embutido |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Modelos de e-mail

{% tabs local %}
{% tab campanhas %}

| Copiado | Omitido |
|---|---|
| Corpo do e-mail | IDs de API |
| Descrição | IDs de imagem | 
| Assunto | Territórios | 
| Cabeçalhos | Tags | 
| | Traduções |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Corpo do e-mail | IDs de API |
| Descrição | IDs de imagem | 
| Assunto | Territórios | 
| Cabeçalhos | Tags | 
| | Traduções |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Blocos de conteúdo

{% tabs local %}
{% tab campanhas %}

| Copiado | Omitido |
|---|---|
| Nome | Apelidamento de link |
| Descrição | Chaves de API | 
| Conteúdo | Territórios | 
| HTML e conteúdo de arrastar e soltar | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Nome | Apelidamento de link |
| Descrição | Chaves de API | 
| Conteúdo | Territórios | 
| HTML e conteúdo de arrastar e soltar | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Variação de mensagens SMS

{% tabs local %}
{% tab campanhas %}

| Copiado | Omitido |
|---|---|
| Corpo | serviço de envio de mensagens |
| Encurtamento de link | Itens de mídia VCF | 
| Clique em rastreamento |  | 
| Itens de mídia |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Corpo | serviço de envio de mensagens |
| Encurtamento de link | Itens de mídia VCF | 
| Clique em rastreamento |  | 
| Itens de mídia |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Cópia de mensagens que contêm Liquid

As referências Liquid nos corpos das mensagens são copiadas para o espaço de trabalho de destino, mas as referências podem não funcionar como esperado. Isso significa que, se uma tela do espaço de trabalho A for copiada para o espaço de trabalho B, o espaço de trabalho B não poderá fazer referência aos detalhes do espaço de trabalho A, incluindo referências Liquid. Por exemplo, campos como ações de disparar e filtros de público não são copiados.

Mantenha o controle das seguintes referências Liquid com dependências ao copiar campanhas e telas entre espaços de trabalho:

- Tags de itens do catálogo
- Tags de conteúdo conectado
- Blocos de conteúdo
- Atributos personalizados
- Centros de preferência
- Recomendações de produtos
- Estado de inscrição tags
- Etiquetas de voucher e promoção

## Cópia de mensagens com feature flags

Para copiar uma campanha de sinalizador de recurso e um Canvas com uma etapa de sinalizador de recurso entre espaços de trabalho, certifique-se de que o espaço de trabalho de destino tenha um [experimento de sinalizador de recurso]({{site.baseurl}}/developer_guide/feature_flags/experiments) configurado com um ID que corresponda ao sinalizador de recurso referenciado na campanha original ou à etapa do canva referenciada no Canvas original.

Se você copiar uma campanha ou uma tela que tenha uma etapa do Feature Flag com um ID de feature flag que não exista no espaço de trabalho de destino, a etapa do Feature Flag será copiada, mas seu conteúdo não será.

## Cópia de mensagens com blocos de conteúdo

Quando você copia uma campanha entre espaços de trabalho, os blocos de conteúdo não serão copiados. No entanto, um bloco de conteúdo pode ser referenciado no espaço de trabalho de destino se existir um bloco com o mesmo nome. Alternativamente, você pode criar o bloco de conteúdo (ou essas referências Liquid) no espaço de trabalho de destino para evitar erros ao lançar uma campanha.

Para as telas que fazem referência a um bloco de conteúdo, o bloco de conteúdo deve primeiro ser copiado para o espaço de trabalho de destino.
