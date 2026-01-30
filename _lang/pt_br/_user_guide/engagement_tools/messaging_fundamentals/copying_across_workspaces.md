---
nav_title: Copiar entre espaços de trabalho
article_title: Copiar Entre Espaços de Trabalho
page_order: 4
alias: "/copying_to_workspaces/"
page_type: reference
description: "Este artigo de referência fornece uma visão geral de como copiar campanhas e Canvases para diferentes espaços de trabalho."
tool:
    - Campaigns
    - Canvas
---

# Copiar campanhas e Canvases entre espaços de trabalho

> Copiar campanhas entre espaços de trabalho permite que você inicie a composição da sua mensagem começando com uma cópia de uma campanha em um espaço de trabalho diferente. Esta página cobre como copiar campanhas para diferentes espaços de trabalho e lista o que é e o que não é copiado.

Quando você copia uma campanha ou Canvas para um espaço de trabalho diferente, a cópia permanecerá como um rascunho até que você edite e lance, ajudando você a manter e construir suas estratégias de envio de mensagens bem-sucedidas.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
Copiar campanhas entre espaços de trabalho está geralmente disponível. O suporte a canais para Cartões de Conteúdo não está atualmente disponível.
{% endalert %}

Você pode copiar campanhas entre espaços de trabalho para estes canais suportados: SMS, mensagens no aplicativo, notificações por push, e-mail e webhooks. Você também pode copiar modelos de e-mail, flags de recursos e Blocos de Conteúdo. Observe que campanhas multicanal com canais não suportados não podem ser copiadas para um espaço de trabalho diferente.

Para copiar uma campanha para um espaço de trabalho diferente:

1. Selecione o ícone de <i class="fas fa-cog"></i> engrenagem ao lado da campanha selecionada.
2. Selecione **Copiar para espaço de trabalho**. 
3. Após copiar, revise e teste sua campanha para confirmar que todos os campos funcionam corretamente.

{% endtab %}
{% tab canvas %}

{% alert important %}
Copiar Canvases entre espaços de trabalho está geralmente disponível. Os seguintes canais não estão atualmente suportados: LINE, Cartões de Conteúdo e WhatsApp.
{% endalert %}

Você pode copiar Canvases entre espaços de trabalho para estes canais suportados: e-mail, mensagens no aplicativo, push, webhooks e SMS.

Para copiar um Canvas para um espaço de trabalho diferente:

1. Selecione o menu <i class="fa-solid fa-ellipsis-vertical"></i> ao lado do Canvas selecionado.
2. Selecione **Copiar para espaço de trabalho**. 
3. Após copiar, revise e teste seu Canvas para confirmar que todos os campos funcionam corretamente.

Ao copiar um Canvas com etapas de Sincronização de Público, as configurações não serão copiadas para o espaço de trabalho de destino, mas as etapas na jornada serão.

{% endtab %}
{% endtabs %}

## O que é copiado entre espaços de trabalho

Observe que a seguinte não é uma lista abrangente do que é copiado entre espaços de trabalho e o que é omitido. Como uma boa prática, verifique os detalhes da campanha e do Canvas e teste para confirmar que sua mensagem funciona como esperado.

### Informações

{% tabs local %}
{% tab campaigns %}

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
| Configurações de limitação de frequência | Resumos de Canvas | 
| Estado de inscrição do destinatário |  | 
| Agenda recorrente |  | 
| É Transacional |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Comportamentos de conversão

{% tabs local %}
{% tab campaigns %}

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
| Interação do Canvas |  ID do canva | 
| Nome do evento personalizado |  | 
| Nome do produto |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Ações

{% tabs local %}
{% tab campaigns %}

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
| Interação do Canvas |  ID do canva | 
| Nome do evento personalizado |  | 
| Nome do produto |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Variações de mensagens

{% tabs local %}
{% tab campaigns %}

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
{% tab campaigns %}

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
{% tab campaigns %}

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
{% tab campaigns %}

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
{% tab campaigns %}

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

### Variação da mensagem de SMS

{% tabs local %}
{% tab campaigns %}

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

## Copiando mensagens que contêm Liquid

Referências Liquid dentro dos corpos das mensagens são copiadas para o espaço de trabalho de destino, mas as referências podem não funcionar como esperado. Isso significa que se um Canvas do Espaço de Trabalho A for copiado para o Espaço de Trabalho B, então o Espaço de Trabalho B não pode referenciar os detalhes do Espaço de Trabalho A, incluindo referências Liquid. Por exemplo, campos como ações de disparar e filtros de público não são copiados.

Mantenha o controle das seguintes referências Liquid com dependências ao copiar campanhas e Canvases entre espaços de trabalho:

- Tags de itens do catálogo
- Tags de conteúdo conectado
- Blocos de conteúdo
- Atributos personalizados
- Centros de preferência
- Recomendações de produtos
- Estado de inscrição tags
- Etiquetas de voucher e promoção

## Copiando mensagens com feature flags

Para copiar uma campanha de feature flag e um Canvas com uma etapa de Feature Flag entre espaços de trabalho, certifique-se de que o espaço de trabalho de destino tenha um [experimento de feature flag]({{site.baseurl}}/developer_guide/feature_flags/experiments) configurado com um ID que corresponda ao feature flag referenciado na campanha original ou à etapa de Feature Flag referenciada no Canvas original.

Se você copiar uma campanha ou Canvas que tem uma etapa de Feature Flag com um ID de feature flag que não existe no espaço de trabalho de destino, a etapa de Feature Flag será copiada, mas seu conteúdo não será.

## Copiando mensagens com Blocos de Conteúdo

Quando você copia uma campanha entre espaços de trabalho, os blocos de conteúdo não serão copiados. No entanto, um bloco de conteúdo pode ser referenciado no espaço de trabalho de destino se existir um bloco com o mesmo nome. Alternativamente, você pode criar o bloco de conteúdo (ou essas referências Liquid) no espaço de trabalho de destino para evitar erros ao lançar uma campanha.

Para Canvases que referenciam um Bloco de Conteúdo, o Bloco de Conteúdo deve primeiro ser copiado para o espaço de trabalho de destino.
