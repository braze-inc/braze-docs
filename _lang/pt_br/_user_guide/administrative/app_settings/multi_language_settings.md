---
nav_title: Configurações em vários idiomas
article_title: Configurações em vários idiomas
alias: "/multi_language_support/"
page_order: 5.5
description: "Este artigo fornece uma visão geral das configurações multilíngues no dashboard da Braze e como usar localidades em seu envio de mensagens."
---

# Configurações em vários idiomas

> Ao ajustar as configurações multilíngues, é possível direcionar usuários em diferentes idiomas e locais com mensagens diferentes, tudo em uma única mensagem de e-mail.

## Pré-requisitos

Para editar e gerenciar o suporte a vários idiomas, é necessário ter a permissão de usuário "Manage Multi-Language Settings" (Gerenciar configurações de vários idiomas). Para adicionar a localização a uma mensagem, você precisará de permissões para editar campanhas.

## Adicionar uma localização

1. Acesse **Configurações** > **Suporte a vários idiomas** em **Configurações do espaço de trabalho**.
2. Selecione **Add locale (Adicionar localização**).
3. Digite um nome para a localização.
4. Para as **atribuições do usuário**, selecione o idioma a ser adicionado usando o menu suspenso **Idioma**.
5. (opcional) Selecione o país a ser associado ao idioma.
6. Selecione **Add locale (Adicionar localização**). 

![Um exemplo de francês adicionado como localização para usuários cujo país é o Canadá.][2]{: style="max-width:80%;"}

Para obter as etapas de uso dessas localidades em suas campanhas de e-mail e no Canva, consulte [Uso de localidades]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/).

## Perguntas frequentes

#### Quantas localizações posso adicionar?
Você pode adicionar até 200 localidades.

#### Onde os arquivos de tradução são armazenados no Braze?
Os arquivos de tradução são armazenados no nível da campanha, o que significa que cada variante de mensagens deve ter traduções feitas upload.

#### O nome da localização precisa seguir um padrão ou formato específico?
Não. Você pode usar sua convenção de nomenclatura preferida. O nome da localização é usado ao selecionar a localização no editor e estará nos cabeçalhos do arquivo baixado com os IDs de tradução.

#### Posso usar atributos personalizados para definir uma localidade?
Atualmente, não. Entre em contato com o gerente da sua conta ou deixe um [feedback sobre o produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) com mais detalhes sobre como definir as localizações.

[2]: {% image_buster /assets/img/multi-language_support/add_locale.png %}
