---
nav_title: Copiando entre espaços de trabalho
article_title: Copiando entre espaços de trabalho
alias: "/copying_to_workspaces/"
page_order: 0.5
page_type: reference
description: "Este artigo fornece uma visão geral de como copiar campanhas para diferentes espaços de trabalho."
tool: Campaigns
---

# Copiando entre espaços de trabalho

> Copiar campanhas entre espaços de trabalho permite que você inicie a composição da sua mensagem começando com uma cópia de uma campanha em um espaço de trabalho diferente. Essa cópia permanecerá como um rascunho até a edição e o lançamento, ajudando-o a manter e desenvolver suas estratégias de envio de mensagens bem-sucedidas.<br><br>Esta página cobre como copiar campanhas para diferentes espaços de trabalho e lista o que é e o que não é copiado.

{% alert important %}
Copiar campanhas entre espaços de trabalho está geralmente disponível para os seguintes canais suportados: SMS, mensagens no app, e-mail, modelos de e-mail e Blocos de Conteúdo. Outro suporte de canal (como para push e cartões de conteúdo) ainda não está disponível.
{% endalert %}

## Como copiar uma campanha para um espaço de trabalho diferente

![Menu com a opção "Copy to workspace" (Copiar para o espaço de trabalho).][1]{: style="float:right;max-width:25%;margin-left:15px;"}

Selecione o ícone de engrenagem <i class="fas fa-cog"></i> ao lado da campanha selecionada e selecione **Copiar para o espaço de trabalho**. Após copiar, recomendamos revisar e testar sua campanha para confirmar que todos os campos funcionam corretamente.

Quando você copia uma campanha entre espaços de trabalho, campos como nome e descrição da campanha, variantes, tipo de cronograma de entrega e comportamentos de conversão são copiados. Para campanhas de e-mail, campos como corpo do e-mail, assunto e pré-cabeçalho também são copiados para o espaço de trabalho de destino. 

Observe que campanhas multicanal com canais não suportados não podem ser copiadas para um espaço de trabalho diferente.

### O que é copiado entre espaços de trabalho

É importante frisar que esta não é uma lista abrangente do que é copiado entre espaços de trabalho e o que é omitido. Como uma boa prática, verifique os detalhes da campanha e teste para confirmar que sua campanha funciona como esperado.

{% tabs %}
{% tab Campanhas %}

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
{% tab Comportamentos de Conversão %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs de espaços de trabalho |
| Interação de campanha |  ID da campanha | 
| Nome do evento personalizado |  | 
| Nome do produto |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Ações %}

| Copiado | Omitido |
|---|---|
| Tipos de ação | Enviar contagem |
| Variações de mensagens |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Variações de Mensagens %}

| Copiado | Omitido |
|---|---|
| Enviar porcentagem | ID da API |
| Tipo |  IDs do grupo de teste | 
|  |  IDs de modelo de link | 
|  |  IDs de grupo de usuários internos | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Mensagem de E-mail Variada %}

| Copiado | Omitido |
|---|---|
| [Corpo do e-mail]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/?tab=email%20body) | Endereço de origem |
| Extras de mensagem |  Responder a | 
| Título |  CCO | 
| Assunto |  Modelo de link | 
|  |  Apelidamento de link |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Corpo do e-mail %}

| Copiado | Omitido |
|---|---|
| Texto simples | Apelidamento de link |
| HTML e conteúdo de arrastar e soltar |  | 
| pré-cabeçalho |  | 
| CSS embutido |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Modelos de e-mail %}

| Copiado | Omitido |
|---|---|
| [Corpo do e-mail]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/?tab=email%20body) | IDs de API |
| Descrição | IDs de imagem | 
| Assunto | Territórios | 
| Cabeçalhos | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Blocos de Conteúdo %}

| Copiado | Omitido |
|---|---|
| Nome | Apelidamento de link |
| Descrição | Chaves de API | 
| Conteúdo | Territórios | 
| HTML e conteúdo de arrastar e soltar | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Variação de Mensagem SMS %}

| Copiado | Omitido |
|---|---|
| Corpo | serviço de envio de mensagens |
| Encurtamento de link | Itens de mídia VCF | 
| Clique em rastreamento |  | 
| Itens de mídia |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Copiando campanhas que contêm Liquid

Para corpos de mensagens que incluem referências Liquid, as referências são copiadas para o espaço de trabalho de destino, mas podem não funcionar como esperado. Isso significa que, se uma campanha do espaço de trabalho A for copiada para o espaço de trabalho B, então o espaço de trabalho B não poderá referenciar os detalhes do espaço de trabalho A, incluindo referências Liquid. Por exemplo, campos como ações de disparar e filtros de público não são copiados.

Nota as seguintes referências de Liquid com dependências ao copiar campanhas entre espaços de trabalho:

- Tags de itens do catálogo
- Tags de conteúdo conectado
- Blocos de conteúdo
- Atributos personalizados
- Centros de preferência
- Recomendações de produtos
- Estado de inscrição tags
- Etiquetas de voucher e promoção

Quando você copia uma campanha entre espaços de trabalho, os blocos de conteúdo não serão copiados. No entanto, um bloco de conteúdo pode ser referenciado no espaço de trabalho de destino se existir um bloco com o mesmo nome. Alternativamente, você pode criar o bloco de conteúdo (ou essas referências Liquid) no espaço de trabalho de destino para evitar erros ao lançar uma campanha.

### Cópia de campanhas com feature flags

Para copiar uma campanha de sinalizador de recurso entre espaços de trabalho, certifique-se de que o espaço de trabalho de destino tenha um [experimento de sinalizador de recurso]({{site.baseurl}}/developer_guide/feature_flags/experiments) configurado com um ID que corresponda ao sinalizador de recurso referenciado na campanha original. Se você copiar uma campanha, mas não houver um ID de sinalizador de recurso correspondente no espaço de trabalho de destino, a seleção do sinalizador de recurso na campanha ficará em branco quando for copiada, e você terá de selecionar um diferente.

[1]: {% image_buster /assets/img_archive/clone_campaign.png %}

