---
nav_title: Criar códigos
article_title: Criar códigos de promoção
page_order: 0.1
description: "Aprenda como criar códigos de promoção em suas campanhas e Canvases."
---

# Criar códigos de promoção

> Aprenda como criar códigos de promoção em suas campanhas e Canvases.

## Criando uma lista de códigos de promoção {#create}

### Etapa 1: Criar uma nova lista

No dashboard, Acessar **Configurações de Dados** > **Códigos de Promoção**, então selecione **Criar Lista de Códigos de Promoção**.

![Botão para criar um código de promoção.]({% image_buster /assets/img/promocodes/promocode1.png %})

### Etapa 2: Insira os detalhes

1. Nomeie sua lista de códigos promocionais e adicione uma descrição opcional.
2. Em seguida, crie um trecho de código para o código de promoção. 

Aqui estão alguns detalhes a considerar ao criar um trecho de código:

- Você não pode editar um trecho de código depois de salvar.
- Trechos são sensíveis a maiúsculas e minúsculas. Por exemplo, o sistema reconhece "Birthday_promo" e "birthday_promo" como dois trechos diferentes.
- Use o nome do trecho em Liquid para referenciar este conjunto de códigos de promoção.
- Certifique-se de que o trecho de código não está sendo usado em outra lista.

![Uma lista de códigos de promoção chamada "SpringSale2025" com o trecho de código "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Etapa 3: Escolha opções de código de promoção

Cada lista de códigos promocionais tem uma data e hora de expiração correspondente que é definida no momento da criação. O comprimento máximo de expiração é de seis meses a partir do dia em que você cria ou edita sua lista.

Dentro desse período, você pode alterar e atualizar a data de expiração repetidamente. Esta data de expiração se aplica a todos os códigos adicionados a esta lista. Após a expiração, os códigos são excluídos do sistema Braze, e quaisquer mensagens chamando o trecho de código dessa lista não são enviadas.

![Configurações de expiração da lista que todos os códigos restantes expirarão em 30 de abril de 2025 às 12h.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

Você também tem a opção de configurar alertas de limite opcionais e personalizados. Se configurados, esses alertas enviam e-mail ao destinatário designado quando a lista estiver com poucos códigos de promoção disponíveis nesta lista ou quando sua lista de códigos de promoção estiver próxima da expiração. O destinatário é notificado uma vez por dia.

![Um exemplo de um alerta de limite para notificar "marketing@abc.com" quando a lista de códigos promocionais expirar em 5 dias.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Etapa 4: Fazer upload de códigos promocionais

O Braze não gerencia a criação ou o resgate de códigos, o que significa que você deve gerar seus códigos promocionais em um arquivo CSV e fazer upload deles no Braze. 

Certifique-se de que seu arquivo CSV siga estas diretrizes:

- Inclui uma coluna para códigos de promoção.
- Tem um código de promoção por linha.

Você pode usar nossa integração embutida com [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) ou [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) para criar e exportar códigos de promoção.

{% alert important %}
O tamanho máximo do arquivo é 100 MB e o tamanho máximo da lista é 20 milhões de códigos não utilizados. Se você encontrar que o arquivo errado foi enviado, faça upload de um novo para substituir o arquivo anterior.
{% endalert %}

1. Após o fazer upload ser concluído, selecione **Salvar Lista** para salvar todos os detalhes e códigos que você acabou de inserir.

![Arquivo CSV chamado "springsale" que foi enviado com sucesso.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. Após selecionar salvar, uma nova linha aparece no **Histórico de Importação**.
3\. Para atualizar a tabela para ver se sua importação foi concluída, selecione <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sincronizar** no topo da tabela.

![Códigos promocionais em processo de upload.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Arquivos maiores levam vários minutos para importar. Enquanto você espera, pode sair da página e trabalhar em outra coisa enquanto a importação está em andamento. Quando a importação termina, o status muda para **Completo** na tabela.
{% endalert %}

## Atualizando uma lista de códigos de promoção

Para atualizar uma lista, selecione uma de suas listas existentes. Você pode alterar o nome, a descrição, a expiração da lista e os alertas de limite. Você também pode adicionar mais códigos à lista carregando novos arquivos e selecionando **Atualizar Lista**. Todos os códigos na lista têm a mesma expiração, independentemente da data de importação.

{% alert important %}
Códigos promocionais não podem ser excluídos.
{% endalert %}

### Modificando uma lista de códigos promocionais incorretos 

Se você enviou um arquivo CSV com os códigos promocionais incorretos e selecionou **Salvar lista**, você pode resolver isso por qualquer um dos métodos:

- Descontinuar toda a lista: Pare de usar a lista atual de códigos promocionais em qualquer campanha, Canvases ou modelos. Em seguida, faça upload do arquivo CSV com os códigos corretos e use-os em seu envio de mensagens.
- Use os códigos incorretos: Crie uma campanha que envie códigos promocionais da lista de códigos promocionais incorretos para um espaço reservado até que todos os códigos incorretos sejam usados. Em seguida, faça upload dos códigos de promoção corretos para a mesma lista.
