{% if include.section == "Prerequisites" %}
## Pré-requisitos

Para editar e gerenciar o [suporte multilíngue]({{site.baseurl}}/multi_language_support/), você precisa das seguintes [permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) para o seu espaço de trabalho:

- Ver Configurações de Localização
- Editar Configurações de Localização
- Excluir Configurações de Localização

Para adicionar a localidade a uma mensagem, você precisa da permissão "Editar Campanhas".

{% alert important %}
O suporte multilíngue está atualmente em acesso antecipado. Fale com seu gerente de conta da Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

{% endif %}

{% if include.section == "Preview" %}

## Faça uma prévia das suas localidades

No dropdown **Prévia da mensagem como usuário** dentro da guia **Teste**, selecione **Usuário personalizado** e insira diferentes idiomas para visualizar a mensagem e verificar se ela é traduzida conforme esperado.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Perguntas frequentes

#### Posso fazer uma alteração no texto traduzido em uma das minhas localidades?
Sim. Primeiro, faça a edição no CSV e depois faça upload do arquivo novamente para alterar o texto traduzido.

#### Posso aninhar tags de tradução?
Não.

#### Posso adicionar estilo HTML nas tags de tradução?
Sim, mas certifique-se de verificar se a formatação HTML não é traduzida junto com o conteúdo.

#### Que validações ou verificações extras a Braze faz?

| Cenário                                                                                                                                                 | Validação na Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Um arquivo de tradução não tem localidades associadas à mensagem atual.                                                                               | Esse arquivo de tradução não será carregado.                                                                       |
| Um arquivo de tradução está sem alguns blocos de texto, como um texto dentro de tags de tradução Liquid, da mensagem de e-mail atual.                                | Esse arquivo de tradução não será carregado.                                                                       |
| O arquivo de tradução inclui o texto padrão que não corresponde aos blocos de texto da mensagem de e-mail atual.                                          | Esse arquivo de tradução não será carregado. Corrija isso no seu CSV antes de tentar fazer upload novamente.               |
| O arquivo de tradução inclui localidades que não existem nas configurações de **Suporte Multilíngue**.                                                           | Essas localidades não serão salvas na Braze.                                                                      |
| O arquivo de tradução inclui blocos de texto que não existem na mensagem atual (como o rascunho atual no momento em que as traduções são carregadas). | Os blocos de texto que não existirem na sua mensagem atual não serão salvos do arquivo de tradução na Braze. |
| Remoção de uma localidade da mensagem depois que essa localidade já tiver sido carregada para a mensagem como parte do arquivo de tradução.                           | A remoção da localidade removerá todas as traduções associadas à localidade na sua mensagem.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}