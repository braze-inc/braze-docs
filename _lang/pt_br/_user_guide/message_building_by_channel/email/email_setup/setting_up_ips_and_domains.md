---
nav_title: Configuração de IPs e domínios
article_title: Configuração de IPs e domínios
page_order: 0
page_type: tutorial
channel: email
description: "Este artigo explica como configurar seus IPs e domínios para o envio de e-mails pelo Braze."

---

# Configuração de IPs e domínios

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

> Este artigo o guiará pelos requisitos e etapas necessários para configurar seus endereços IP e pools, bem como os domínios e subdomínios necessários antes de começar a enviar e-mails com o Braze.<br><br>Embora a maior parte do processo de configuração seja feita pela Braze, descrevemos os requisitos e os materiais para essa configuração.

## Método 1: Coordenar com Braze (recomendado)

### Etapa 1: Informações gerais

Envie as seguintes informações ao seu representante Braze:

* Seus domínios e subdomínios escolhidos
* O número aproximado de e-mails que você enviará por mês, o que ajudará a determinar quantos IPs serão necessários
* Como você prefere mapear seus domínios de envio para seu IP alocado

### Etapa 2: Braze configura informações

Depois de receber seu e-mail, começaremos a trabalhar na configuração de seus IPs, domínios e subdomínios e pools de IPs.

### Etapa 3: Adicionar registros DNS

Depois que seus IPs, domínios, subdomínios e pools de IPs estiverem configurados, enviaremos uma lista de registros DNS. Peça aos seus engenheiros e desenvolvedores que adicionem esses registros DNS onde for necessário e, depois que eles forem adicionados, informe a equipe de integração do Braze.

### Próximas etapas

Verificaremos sua configuração e validaremos todas as informações em nossos sistemas internos. A equipe de integração do Braze o avisará quando estiver pronto para acessar ou se houver problemas com seus registros DNS que devam ser resolvidos com sua equipe de engenharia.

## Método 2: Configuração de e-mail por autoatendimento

Esse método configurará um domínio de envio, um domínio de rastreamento e um IP no total para uma empresa. Se estiver planejando configurar mais, consulte a equipe de integração da Braze (método 1).

{% alert important %}
Esse recurso de configuração de e-mail por autoatendimento está atualmente na versão beta. Entre em contato com o gerente da sua conta Braze se estiver interessado em participar da versão beta.<br>Se estiver usando o recurso de configuração de e-mail de autoatendimento, não deixe de consultar também a equipe de integração do Braze.
{% endalert %}

### Pré-requisitos

Para usar a configuração de e-mail por autoatendimento, você deve atender aos seguintes pré-requisitos:

1. Você é um novo cliente em processo de integração.
2. Você tem a permissão em nível de empresa "Can Manage Company Settings" (Pode gerenciar configurações da empresa).

### Etapa 1: Iniciar a configuração

1. Acesse **Configurações** > **Configurações administrativas** em **Configurações da empresa**. 
2. Em seguida, selecione a guia **Verificação do remetente**. Para visualizar essa guia, você deve ter a permissão no nível da empresa "Pode gerenciar configurações da empresa".
3. Clique no botão **Iniciar configuração**.

### Etapa 2: Adicionar e verificar um domínio de envio

Um domínio de envio é usado no endereço do remetente na hora de enviar um e-mail. Insira um domínio de envio e clique em **Enviar**. 

Em seguida, adicione os registros TXT e CNAME da parte inferior da página ao seu provedor DNS. Em seguida, retorne ao dashboard da Braze e clique em **Verificar**.

![]({% image_buster /assets/img_archive/email_setup_rdns_records.png %})

{% alert important %}
O domínio de envio deve ser subordinado a um domínio que você possui. Por exemplo, se você é proprietário de "example.com", um subdomínio poderia ser "mail.example.com", o que lhe permite usar o endereço de envio "@mail.example.com".
{% endalert %}

### Etapa 3: Adicionar e verificar um domínio de rastreamento

Um domínio de rastreamento é usado para envolver links em seus e-mails para fins de rastreamento de cliques e de marca. Isso ficará visível para os usuários quando eles passarem o mouse sobre os links do e-mail ou clicarem neles. Recomendamos que você faça a correspondência com seu domínio de envio.

Digite um domínio de rastreamento e clique em **Enviar**. Em seguida, adicione os registros CNAME da parte inferior da página ao seu provedor DNS. Em seguida, retorne ao dashboard da Braze e clique em **Verificar**.

### Etapa 4: Adicionar um endereço IP

O Braze gerará um registro A para associar seu endereço IP ao seu subdomínio de envio em uma configuração chamada DNS reverso (rDNS). Adicione o registro A em seu provedor DNS e clique em **Configurar rDNS** para atender à entregabilidade.

Note que os domínios adicionais que foram adicionados não aparecerão na seção **Verificação de remetente**. Para adicionar mais domínios, entre em contato com a equipe de suporte da Braze.

### Próximas etapas

Após a conclusão da verificação do remetente, recomendamos o aquecimento de IP para que suas mensagens cheguem às caixas de entrada dos destinos com uma taxa consistentemente alta. Depois de concluir essa configuração, consulte também a equipe de integração do Braze para confirmar se seus domínios e [endereço IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) estão funcionando.

