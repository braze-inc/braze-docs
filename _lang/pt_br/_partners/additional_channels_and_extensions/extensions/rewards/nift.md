---
nav_title: Nift
article_title: Nift
description: "Este artigo de referência descreve a parceria entre a Braze e a Nift, uma plataforma bilateral que ajuda as empresas a adquirir, engajar e reter clientes."
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# Nift

> A [Nift](https://gonift.com/) ajuda as empresas a adquirir, engajar e reter clientes. A plataforma bilateral ajuda os parceiros a agradecerem seus clientes com cartões-presente da Nift. Agradecer aos clientes aumenta o valor do tempo de vida e gera receita incremental.

_Essa integração é mantida pelo Nift._

## Sobre a integração

A integração entre a Braze e a Nift permite disparar automaticamente "agradecimentos" com presentes da Nift em momentos-chave do ciclo de vida do cliente e identificar quais clientes usaram o presente. Os cartões-presente Nift podem ser usados para acessar produtos e serviços fornecidos por marcas que confiam na tecnologia de matchmaking da Nift para adquirir novos clientes de forma econômica em escala.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta Nift | É necessário ter uma conta Nift para aproveitar esta parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com todas as permissões de dados de usuários. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze | Sua URL de endpoint REST. Seu endpoint dependerá do [URL da Braze para [sua instância]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Conecte-se ao Braze no Nift

Visite seu [Nift dashboard](https://www.gonift.com/users/sign_in), navegue até **Contas** > **Integrações** > **Braze**, e clique em **Conectar**.

### Etapa 2: Adicionar credenciais Braze

Na página **Link your Braze Account** (Vincular sua conta da Braze), forneça sua chave da API REST da Braze e selecione seu endpoint da Braze, que depende do URL da Braze para [sua instância]({{site.baseurl}}/api/basics/#endpoints).

Você pode alterar o nome do parâmetro de ID do cliente no link de referência enviado aos seus clientes. Nift usará isso para marcar seus clientes como processados na Braze quando eles tiverem selecionado um presente de uma de nossas marcas.

Clique em **Vincular Conta**.

!["Página de integração do serviço Nift solicitando ao usuário a chave de API do Braze e a URL do dashboard do Braze.]({% image_buster /assets/img/nift/link_your_braze_account.png %})

## Usando a integração

Para usar a integração, distribua o link de referência no seu envio de mensagens. Quando seu cliente usa o link de indicação e seleciona um presente de uma de nossas marcas, a Nift os marcará como processados no Braze.

Após a integração com a Braze, a Nift enviará automaticamente eventos para o registro de cliente existente na Braze com estes dados:

- Nome do evento: `nift_processed`
- Tempo: A hora que o cliente selecionou/usou o presente



