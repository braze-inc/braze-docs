---
nav_title: Criar códigos
article_title: Criar códigos promocionais
page_order: 0.1
description: "Saiba como criar códigos promocionais em suas campanhas e Canvas."
---

# Criar códigos promocionais

> Saiba como criar códigos promocionais em suas campanhas e Canvas.

## Criação de uma lista de códigos promocionais {#create}

### Etapa 1: Criar uma nova lista

No dashboard, acesse **Configurações de dados** > **Códigos promocionais** e selecione **Criar lista de códigos promocionais**.

![Botão para criar um código promocional.]({% image_buster /assets/img/promocodes/promocode1.png %})

### Etapa 2: Insira os detalhes

1. Nomeie sua lista de códigos promocionais e adicione uma descrição opcional.
2. Em seguida, crie um trecho de código para o código de promoção. 

Aqui estão alguns detalhes a serem considerados ao criar um trecho de código:

- Não é possível editar um trecho de código depois de salvá-lo.
- Trechos são sensíveis a maiúsculas e minúsculas. Por exemplo, o sistema reconhece "Birthday_promo" e "birthday_promo" como dois trechos diferentes.
- Use o nome do snippet no Liquid para fazer referência a esse conjunto de códigos promocionais.
- Verifique se o trecho de código já não está sendo usado em outra lista.

![Uma lista de códigos promocionais denominada "SpringSale2025" com o snippet de código "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Etapa 3: Selecionar opções de código promocional

Cada lista de códigos promocionais tem uma data e hora de expiração correspondente que é definida no momento da criação. A duração máxima da expiração é de seis meses a partir do dia em que você estiver criando ou editando sua lista.

Dentro desse período, você pode alterar e atualizar a data de expiração repetidamente. Essa data de expiração se aplica a todos os códigos adicionados a essa lista. Após a expiração, os códigos são excluídos do sistema Braze, e todas as mensagens que chamem o trecho de código dessa lista não serão enviadas.

![As configurações de expiração da lista indicam que todos os códigos restantes expirarão em 30 de abril de 2025 às 12 horas.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

Você também tem a opção de configurar alertas de limite opcionais e personalizados. Se configurados, esses alertas enviarão e-mail ao destinatário designado quando a lista estiver com poucos códigos promocionais disponíveis nessa lista ou quando sua lista de códigos promocionais estiver perto de expirar. O destinatário é notificado uma vez por dia.

![Um exemplo de um alerta de limite para notificar "marketing@abc.com" quando a lista de códigos promocionais expirar em 5 dias.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Etapa 4: Fazer upload de códigos promocionais

O Braze não gerencia a criação ou o resgate de códigos, o que significa que você deve gerar seus códigos promocionais em um arquivo CSV e fazer upload deles no Braze. 

Certifique-se de que seu arquivo CSV siga estas diretrizes:

- Inclui uma coluna para códigos de promoção.
- Tem um código de promoção por linha.

Você pode usar nossa integração embutida com [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) ou [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) para criar e exportar códigos de promoção.

{% alert important %}
O tamanho máximo do arquivo é 100 MB e o tamanho máximo da lista é 20MM de códigos não utilizados. Se você descobrir que foi feito upload do arquivo errado, faça upload de um novo arquivo para substituir o anterior.
{% endalert %}

1. Após o fazer upload ser concluído, selecione **Salvar Lista** para salvar todos os detalhes e códigos que você acabou de inserir.

![Arquivo CSV chamado "springsale" que foi feito upload com sucesso.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. Após selecionar salvar, uma nova linha aparecerá no **Histórico de importação**.
3\. Para atualizar a tabela para ver se sua importação foi concluída, selecione <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sincronizar** no topo da tabela.

![Códigos promocionais em processo de fazer upload.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Arquivos maiores levam vários minutos para serem importados. Enquanto você espera, pode sair da página e trabalhar em outra coisa enquanto a importação está em andamento. Quando a importação for concluída, o status será alterado para **Complete** na tabela.
{% endalert %}

## Atualizando uma lista de códigos de promoção

Para atualizar uma lista, selecione uma de suas listas existentes. Você pode alterar o nome, a descrição, a expiração da lista e os alertas de limite. Você também pode adicionar mais códigos à lista carregando novos arquivos e selecionando **Atualizar Lista**. Todos os códigos da lista têm a mesma expiração, independentemente da data de importação.

{% alert important %}
Os códigos promocionais não podem ser excluídos.
{% endalert %}

### Modificação de uma lista incorreta de códigos promocionais 

Se tiver feito upload de um arquivo CSV com os códigos promocionais incorretos e selecionado **Salvar lista**, você poderá resolver isso por qualquer um dos métodos:

- Eliminar a lista inteira: Pare de usar a lista atual de códigos promocionais em quaisquer campanhas, Canvas ou modelos. Em seguida, faça upload do arquivo CSV com os códigos corretos e use-os em seu envio de mensagens.
- Use os códigos incorretos: Crie uma campanha que envie códigos promocionais da lista de códigos promocionais incorretos para um espaço reservado até que todos os códigos incorretos sejam usados. Em seguida, faça upload dos códigos promocionais corretos para a mesma lista.
