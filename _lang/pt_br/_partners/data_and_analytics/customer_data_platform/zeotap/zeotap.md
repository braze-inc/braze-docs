---
nav_title: Zeotap
description: "Este artigo de referência descreve a parceria entre a Braze e a Zeotap, uma plataforma de dados do cliente de última geração que fornece resolução, insights e enriquecimento de identidade."
page_type: partner
search_tag: Partner
page_order: 1
---

# Zeotap

> A [Zeotap](https://zeotap.com/) é uma plataforma de dados do cliente de última geração que ajuda você a descobrir e entender seu público móvel, fornecendo resolução de identidade, insights e enriquecimento de dados.

Com a integração do Zeotap e do Braze, você pode ampliar a escala e o alcance de suas campanhas sincronizando os segmentos de clientes do Zeotap para mapear os dados de usuários para as contas de usuários do Braze. Em seguida, é possível agir com base nesses dados, oferecendo experiências de direcionamento personalizadas aos seus usuários.

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
|Conta Zeotap | É necessário ter uma [conta da Zeotap](https://zeotap.com/) para usar a parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze  | Sua URL de endpoint REST. Seu endpoint dependerá do [URL do Braze para sua instância]({% image_buster /assets/img/zeotap/zeotap1.png %}). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integração

### Etapa 1: Criar um destino Zeotap

1. Na plataforma Zeotap Unity, navegue até o aplicativo **DESTINATIONS** (DESTINOS).
2. Em **All Channels (Todos os canais**), selecione **Braze**.
3. No prompt exibido, dê nome aos destinos e forneça o nome do cliente e a chave da API REST da Braze associados à sua conta da Braze.
4. Por fim, selecione sua instância de endpoint REST da Braze no menu suspenso e salve o destino. <br><br>![]({% image_buster /assets/img/zeotap/zeotap1.png %})

### Etapa 2: Crie e vincule um segmento Zeotap a seu destino 
 
1. Na plataforma Zeotap Unity, navegue até o aplicativo **CONNECT** (CONECTAR).
2. Crie um segmento e selecione o destino Braze criado na etapa 1.
3. Selecione um identificador de saída compatível: MAIDs, endereço de e-mail com hash SHA256 ou qualquer identificador de cliente 1P reconhecido pelo Braze (se quiser usar um identificador personalizado para sua conta do Braze, entre em contato com a Zeotap para que ele possa ser ativado para sua conta). Somente um identificador de saída pode ser usado para a integração com o Braze. Esses identificadores devem ser os mesmos que a ID externa definida ao coletar dados do Braze SDK.
4. Salve o segmento.

![]({% image_buster /assets/img/zeotap/zeotap2.png %})

{% alert note %}
Os identificadores que aparecem estão disponíveis no segmento e são suportados pela Braze.
{% endalert %}

### Etapa 3: Criar segmento de Braze

Após a criação, o push e o processamento bem-sucedidos de um segmento no Zeotap, os usuários do Zeotap aparecerão no dashboard do Braze. Você pode procurar usuários por ID de usuário no dashboard do Braze. 

![Um perfil de usuário do Braze mostrando o segmento de um a quatro listado como "true" em "Custom attributes" (Atributos personalizados).]({% image_buster /assets/img/zeotap/zeotap4.png %})

Se um usuário fizer parte do segmento Zeotap, o nome do segmento aparecerá como um atributo personalizado em seu perfil de usuário com o valor booleano `true`. Anote o nome do atributo personalizado, pois você precisará dele ao criar um segmento Braze. 

Em seguida, você deve criar e definir esse segmento no Braze:
1. No dashboard do Braze, selecione **Segmentos** e depois **Criar segmento**.
2. Em seguida, dê um nome ao seu segmento e selecione o segmento de atributo personalizado criado na Zeotap.
3. Salve suas alterações. 

![No criador de segmentos do Braze, você pode encontrar os segmentos importados definidos como atributos personalizados.]({% image_buster /assets/img/zeotap/zeotap3.png %})

Agora é possível adicionar esse segmento recém-criado a futuras campanhas e canvas do Braze para direcionamento a esses usuários finais. 

