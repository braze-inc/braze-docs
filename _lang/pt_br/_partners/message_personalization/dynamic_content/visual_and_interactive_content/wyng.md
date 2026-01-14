---
nav_title: Wyng
article_title: Wyng
description: "Este artigo de referência descreve a parceria entre o Braze e a Wyng, uma plataforma de dados voluntários que facilita a coleta, o uso e a integração das preferências e atribuições dos clientes por meio de microexperiências, portais de preferências dos clientes e uma plataforma API."
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [A Wyng](https://wyng.com/) facilita a criação de experiências digitais interativas (ou seja, questionários, centrais de preferências, promoções) que engajam os consumidores nos momentos certos, coletam preferências e outros dados voluntários e personalizam em tempo real.

_Essa integração é mantida pela Wyng._

## Sobre a integração

A integração entre a Braze e a Wyng permite que você aproveite os dados voluntários obtidos por meio das experiências da Wyng para personalizar as interações no Braze Campaigns e no Braze Canvas. A Wyng também pode alimentar uma Central de Preferências, para que os consumidores possam controlar os dados e as preferências (inclusive as preferências de comunicação) que compartilham com sua marca.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Wyng | É necessário ter uma conta Wyng para aproveitar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Conecte a integração do Braze

Na Wyng, acesse [**Integrações**](https://wyng.com/dashboard/integrations/) e selecione a guia **Add (Adicionar** ). Em seguida, passe o mouse sobre o **Braze** e clique em **Connect** para a integração.

![O ladrilho do parceiro Braze na plataforma Wyng.]({% image_buster /assets/img/wyng/2.png %}){: style="max-width:80%;"}

### Etapa 2: Configurar o conector Braze

1. Na janela de configuração que se abre, forneça sua chave da API REST da Braze.
![Uma imagem da aparência do prompt de credenciais.]({% image_buster /assets/img/wyng/4.png %}){: style="max-width:80%;"}<br><br>
2. Em seguida, use o menu suspenso para selecionar a campanha Wyng que você gostaria de compartilhar com o Braze.![Uma imagem do conector Braze solicitando que você selecione uma campanha Wyng existente que gostaria de compartilhar com o Braze.]({% image_buster /assets/img/wyng/5.png %}){: style="max-width:80%;"}<br><br>
3. Em seguida, você deve configurar inscrições, objetos de atributo e evento e eventos personalizados.<br><br>
- **Configuração das inscrições (obrigatório)**<br>
Para inscrever usuários em grupos de inscrições, clique em **Add Subscription (Adicionar inscrição** ) e adicione o nome e o ID do grupo de inscrições. Para adicionar vários nomes e IDs de grupos, clique novamente no botão **Add Subscription (Adicionar inscrição** ).<br>![Uma imagem solicitando o nome e o ID de um grupo de inscrições.]({% image_buster /assets/img/wyng/8.png %}){: style="max-width:80%;"}<br><br>
- **Configuração do rastreamento do usuário**<br>
Clique em **Adicionar propriedade personalizada** para adicionar pares de objetos de atributo e evento para enviar ao endpoint `/users/track`. Use isso para adicionar valores de atribuição codificados para cada transação de dados enviada para a integração. Para adicionar várias propriedades, clique novamente no botão **Adicionar propriedade personalizada**.<br>![Uma imagem solicitando que você adicione propriedades personalizadas de atributo.]({% image_buster /assets/img/wyng/9.png %}){: style="max-width:80%;"}<br><br>
- **Enviar evento personalizado**<br>
Opcionalmente, você pode ativar o **envio de eventos personalizados**. Se essa opção estiver ativada, inclua o nome do evento e o ID do app correspondente.<br>![Uma imagem solicitando que você envie eventos personalizados, se necessário.]({% image_buster /assets/img/wyng/10.png %}){: style="max-width:80%;"}<br><br>
4. Por fim, mapeie os campos da Wyng para os campos da API da Braze com base em seu caso de uso. Clique em **Select a field** (Selecionar um campo ) para escolher os campos a serem mapeados e, em seguida, clique em **Save** (Salvar) para salvar sua integração. Quando salvos, esses campos mapeados podem ser encontrados em **Integrations > Manage (Integrações > Gerenciar**).
![Um exemplo dos diferentes campos Wyng que você pode mapear para determinados campos Braze.]({% image_buster /assets/img/wyng/11.png %}){: style="max-width:80%;"}
![Uma lista de campos de sincronização disponíveis.]({% image_buster /assets/img/wyng/12.png %}){: style="max-width:80%;margin-top:2px"}

### Etapa 3: Teste sua integração

No Wyng, teste o envio do formulário em sua campanha do Wyng. Também é possível enviá-lo na campanha de prévia se não quiser adicionar um registro à campanha de produção principal. Você deverá ver uma transação bem-sucedida no dashboard de **integração**.

## Usando esta integração

Quando o conector de dados estiver instalado, todos os campos criados no Wyng e adicionados ao Braze poderão ser usados como qualquer outro campo de dados para disparar campanhas, segmentar públicos ou alimentar conteúdo personalizado.

As aplicações são amplas e perguntas específicas podem ser enviadas para [contact@wyng.com](mailto:contact@wyng.com) ou para seu gerente de conta específico.

## Solução de problemas

### Falha no envio

No caso de um envio com falha, ao enviar dados para o Braze, clique no link **View Log (Exibir registro)** para revisar o envio com falha e a mensagem de erro associada.

![O link "View Log" (Exibir registro) encontra-se no cabeçalho das ações.]({% image_buster /assets/img/wyng/14.png %}){: style="max-width:80%;"}

A página de registro mostrará o envio com falha, a quantidade de tentativas, os dados do envio, o erro e um link para repetir o envio.

![Um exemplo do que um envio com falha mostrará.]({% image_buster /assets/img/wyng/15.jpg %}){: style="max-width:80%;"}

A seção **View Error** mostrará o código de erro e algumas informações adicionais sobre a causa do erro. Em seguida, você pode fazer uma referência cruzada do código de erro com a Braze para determinar a causa.

![Um exemplo de registro de erros mostrado na plataforma Wyng.]({% image_buster /assets/img/wyng/16.jpg %}){: style="max-width:80%;"}

Se tiver alguma dúvida adicional, entre em contato com o suporte da Wyng[(support@wyng.com](mailto:contact@wyng.com)) para obter assistência.


