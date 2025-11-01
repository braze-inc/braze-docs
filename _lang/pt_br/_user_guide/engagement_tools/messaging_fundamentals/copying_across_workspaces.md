---
nav_title: Cópia entre espaços de trabalho
article_title: Cópia entre espaços de trabalho
page_order: 4.5
alias: "/copying_to_workspaces/"
page_type: reference
description: "Este artigo de referência fornece uma visão geral de como copiar campanhas e Canvases para diferentes espaços de trabalho."
tool:
    - Campaigns
    - Canvas
---

# Cópia de campanhas e telas entre espaços de trabalho

> A cópia de campanhas entre espaços de trabalho permite que você inicie a composição de sua mensagem começando com uma cópia de uma campanha em um espaço de trabalho diferente. Esta página aborda como copiar campanhas para diferentes espaços de trabalho e lista o que é e o que não é copiado.

Quando você copia uma campanha ou Canvas para um espaço de trabalho diferente, a cópia permanecerá como um rascunho até que você edite e lance, ajudando-o a manter e desenvolver suas estratégias de mensagens bem-sucedidas.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
A cópia de campanhas entre espaços de trabalho está geralmente disponível. O suporte de canal para cartões de conteúdo não está disponível no momento.
{% endalert %}

Você pode copiar campanhas entre espaços de trabalho para esses canais compatíveis: SMS, mensagens no aplicativo, notificações por push, e-mail e webhooks. Você também pode copiar entre modelos de e-mail, sinalizadores de recursos e blocos de conteúdo. Observe que as campanhas multicanais com canais não suportados não podem ser copiadas para um espaço de trabalho diferente.

Para copiar uma campanha em um espaço de trabalho diferente:

1. Selecione o ícone de engrenagem <i class="fas fa-cog"></i> ao lado da campanha selecionada.
2. Selecione **Copiar para o espaço de trabalho**. 
3. Depois de copiar, revise e teste sua campanha para confirmar que todos os campos funcionam corretamente.

{% endtab %}
{% tab canvas %}

{% alert important %}
A cópia de telas entre espaços de trabalho está geralmente disponível. Os seguintes canais não são compatíveis no momento: LINE, Content Cards e WhatsApp.
{% endalert %}

Você pode copiar Canvases entre workspaces para estes canais compatíveis: e-mail, mensagens no aplicativo, push, webhooks e SMS.

Para copiar um Canvas para um espaço de trabalho diferente:

1. Selecione o menu <i class="fa-solid fa-ellipsis-vertical"></i> ao lado do Canvas selecionado.
2. Selecione **Copiar para o espaço de trabalho**. 
3. Depois de copiar, revise e teste seu Canvas para confirmar que todos os campos funcionam corretamente.

Ao copiar um Canvas com etapas do Audience Sync, as configurações não serão copiadas para o espaço de trabalho de destino, mas as etapas da jornada serão.

{% endtab %}
{% endtabs %}

## O que é copiado nos espaços de trabalho

Observe que a lista a seguir não é uma lista abrangente do que é copiado entre os espaços de trabalho e do que é omitido. Como prática recomendada, verifique os detalhes da campanha e do Canvas e teste para confirmar que sua mensagem funciona conforme o esperado.

### Detalhes

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Descrição | Territórios | 
| Tipo | Tags | 
| Ações (aninhadas) | Segmentos | 
| Comportamentos de conversão (aninhados) | Aprovações | 
| Configurações de tempo de silêncio | Programação de acionamento | 
| Configurações de limitação de frequência | Resumos de campanhas | 
| Estado da assinatura do destinatário |  | 
| Programação recorrente |  | 
| É transacional |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Descrição | Territórios | 
| Tipo | Tags | 
| Ações (aninhadas) | Segmentos | 
| Comportamentos de conversão (aninhados) | Aprovações | 
| Configurações de tempo de silêncio | Programação de acionamento | 
| Configurações de limitação de frequência | Resumos do Canvas | 
| Estado da assinatura do destinatário |  | 
| Programação recorrente |  | 
| É transacional |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Comportamentos de conversão

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs de espaço de trabalho |
| Interação de campanha |  ID da campanha | 
| Nome do evento personalizado |  | 
| Nome do produto |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs de espaço de trabalho |
| Interação com o Canvas |  ID da tela | 
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
| Tipo de comportamento | IDs de espaço de trabalho |
| Interação de campanha |  ID da campanha | 
| Nome do evento personalizado |  | 
| Nome do produto |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs de espaço de trabalho |
| Interação com o Canvas |  ID da tela | 
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
| Enviar porcentagem | ID DA API |
| Tipo |  IDs de grupos de sementes | 
|  |  IDs de modelos de links | 
|  |  IDs de grupos de usuários internos | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Enviar porcentagem | ID DA API |
| Tipo |  IDs de grupos de sementes | 
|  |  IDs de modelos de links | 
|  |  IDs de grupos de usuários internos | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}


### Variação da mensagem de e-mail

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Corpo do e-mail | Do endereço |
| Extras de mensagens |  Responder a | 
| Título |  BCC | 
| Assunto |  Modelo de link | 
|  |  Aliasing de links |
|  | Traduções |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Corpo do e-mail | Do endereço |
| Extras de mensagens |  Responder a | 
| Título |  BCC | 
| Assunto |  Modelo de link | 
|  |  Aliasing de links |
|  | Traduções |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Corpo do e-mail

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Texto simples | Aliasing de links |
| HTML e conteúdo de arrastar e soltar | Traduções | 
| Pré-cabeçalho |  | 
| CSS em linha |  | 
| HTML AMP |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Texto simples | Aliasing de links |
| HTML e conteúdo de arrastar e soltar | Traduções | 
| Pré-cabeçalho |  | 
| CSS em linha |  | 
| HTML AMP |  |
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
| Nome | Aliasing de links |
| Descrição | Chaves de API | 
| Conteúdo | Territórios | 
| HTML e conteúdo de arrastar e soltar | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Nome | Aliasing de links |
| Descrição | Chaves de API | 
| Conteúdo | Territórios | 
| HTML e conteúdo de arrastar e soltar | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Variação da mensagem SMS

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Corpo | Serviço de mensagens |
| Encurtamento de links | Itens de mídia VCF | 
| Rastreamento de cliques |  | 
| Itens de mídia |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Corpo | Serviço de mensagens |
| Encurtamento de links | Itens de mídia VCF | 
| Rastreamento de cliques |  | 
| Itens de mídia |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Cópia de mensagens que contêm Liquid

As referências líquidas nos corpos das mensagens são copiadas para o espaço de trabalho de destino, mas as referências podem não funcionar como esperado. Isso significa que, se um Canvas do espaço de trabalho A for copiado para o espaço de trabalho B, o espaço de trabalho B não poderá fazer referência aos detalhes do espaço de trabalho A, incluindo referências Liquid. Por exemplo, campos como ações de acionamento e filtros de público não são copiados.

Mantenha o controle das seguintes referências Liquid com dependências ao copiar campanhas e Canvases entre espaços de trabalho:

- Etiquetas de itens de catálogo
- Tags de conteúdo conectado
- Blocos de conteúdo
- Atributos personalizados
- Centros de preferência
- Recomendações de produtos
- Tags de estado da assinatura
- Tags de vouchers e promoções

## Cópia de mensagens com sinalizadores de recursos

Para copiar uma campanha de sinalizador de recurso e um Canvas com uma etapa de sinalizador de recurso entre espaços de trabalho, certifique-se de que o espaço de trabalho de destino tenha um [experimento de sinalizador de recurso]({{site.baseurl}}/developer_guide/feature_flags/experiments) configurado com um ID que corresponda ao sinalizador de recurso referenciado na campanha original ou à etapa de sinalizador de recurso referenciada no Canvas original.

Se você copiar uma campanha ou tela que tenha uma etapa de sinalizador de recurso com um ID de sinalizador de recurso que não exista no espaço de trabalho de destino, a etapa de sinalizador de recurso será copiada, mas seu conteúdo não será.

## Cópia de mensagens com blocos de conteúdo

Quando você copia uma campanha entre espaços de trabalho, os blocos de conteúdo não são copiados. No entanto, um Content Block pode ser referenciado no espaço de trabalho de destino se existir um bloco com o mesmo nome. Como alternativa, você pode criar o Content Block (ou essas referências Liquid) no espaço de trabalho de destino para evitar erros ao iniciar uma campanha.

Para Canvases que fazem referência a um Content Block, o Content Block deve primeiro ser copiado para o espaço de trabalho de destino.
