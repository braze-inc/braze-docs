---
nav_title: Digioh
article_title: Digioh
description: "Este artigo de referência descreve a parceria entre o Braze e a Digioh, uma plataforma de pesquisas que permite criar facilmente pop-ups, formulários, pesquisas e Centrais de Preferências de comunicação que geram engajamento real por meio de suas campanhas no Braze."
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> A [Digioh](https://www.digioh.com/) ajuda a aumentar suas listas, capturar dados primários e usar esses dados nas suas campanhas da Braze.

_Esta integração é mantida pelo Digioh._

## Sobre a integração

A integração entre o Braze e o Digioh permite que você use o construtor flexível de arrastar e soltar para criar formulários, pop-ups, centros de performance, landing pages e pesquisas que conectem você aos seus clientes. O Digioh auxiliará na configuração da integração e ajudará a criar, projetar e lançar sua primeira campanha para você.

!["Crie centros de preferência de e-mail e comunicações flexíveis com o Digioh"]({% image_buster /assets/img/digioh/pref_pop_examples.png %}){: style="border:0"}

## Pré-requisitos

| Requisito | Descrição |
|---|---|
|Conta Digioh | É necessário ter uma [conta da Digioh](https://www.digioh.com/) para usar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint da Braze API `/users/track/`  | Seu URL de endpoint REST com os detalhes de `/users/track/` anexados a ele. Seu endpoint dependerá da [URL do Braze para sua instância]({{site.baseurl}}/api/basics/#endpoints).<br><br>Por exemplo, se seu endpoint da API REST for `https://rest.iad-01.braze.com`, seu endpoint `/users/track/` será `https://rest.iad-01.braze.com/users/track/`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integração 

Para integrar a Digioh, configure primeiro o conector da Braze. Quando terminar, você precisará aplicar a integração a uma lightbox (widget). Visite o [Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/) para saber mais sobre os conceitos básicos de integração.

### Etapa 1: Criar integração com o Digioh 

No Digioh, clique na guia **Integrations (Integrações** ) e, em seguida, no botão **New Integration (Nova integração** ). Selecione **Braze** no menu suspenso **Integração** e nomeie a integração. 

!["Selecione a integração correta no menu suspenso"]({% image_buster /assets/img/digioh/2.png %}){: style="max-width:50%;"}

Em seguida, insira a chave da API REST da Braze e seu endpoint da API da Braze `/users/track/`. 

Por fim, use a seção de campos do mapa para mapear campos personalizados adicionais além do e-mail e do nome. O trecho de código a seguir mostra um exemplo de carga útil. Quando concluído, selecione **Criar integração**.

```json
{
    "attributes" : [
         {
           "external_id": "[EMAIL_MD5]",
           "email" : "[EMAIL]"
         }
     ]
}
```

### Etapa 2: Criar uma lightbox Digioh

Use o [editor de design](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) da Digioh para criar uma lightbox (widget). <br>
Interessado em ver uma galeria de maneiras de aproveitar o editor de design? Visite a [galeria de temas](https://www.digioh.com/theme-gallery) da Digioh.

### Etapa 3: Aplicar integração

Para aplicar essa integração a uma [lightbox](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) do Digioh, navegue até a página **Boxes** (Caixas) e selecione o link **Add** (Adicionar) ou **Edit** (Editar) na coluna **Integrations** (Integrações). Isso também pode ser adicionado na seção **Integração** do editor.

!["Adicione a integração a uma lightbox"]({% image_buster /assets/img/digioh/3.png %}){: style="max-width:90%"}

Aqui, selecione **Add Integration (Adicionar integração**), escolha a integração desejada e **Save (Salvar**). A Digioh agora passará seus leads capturados para a Braze em tempo real.


