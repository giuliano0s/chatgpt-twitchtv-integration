# chatgpt-twitchtv-integration

Simples integração entre o ChatGPT e a plataforma de livestreaming Twitch TV

# Como usar
## Configurando o browser
- Baixe o Google Chrome, crie um perfil no navegador e guarde seu ID, achado em 'Caminho de perfil' em 'chrome://version/'. A intenção é salvar os cookies para usar no código
  - Exemplo: C:\Users\User\AppData\Local\Google\Chrome\User Data\Profile 4 | o Id é 'Profile 4'
- Vá até https://www.twitch.tv , crie um perfil dedicado ao bot e outro para você caso não tenha. De preferência verifique email e senha

## Configurando o código
- coloque o ID do perfil (no exemplo 'Profile 4') em > pipeline.ipynb > classe Utils (segundo bloco) > variável 'profile_name'
- configure os parâmetros da classe Chatbot:
  - botIdName = nome de usuário do bot
  - botName = nome de interpretação do bot
  - fileName = arquivo de texto da engenharia de prompt
  - streamId= id do canal da TwitchTV
  - pronouns = feminino/masculino
  - mainUser = seu nome de usuário TwitchTV
  - openai_key = key OpenAI
 
## Engenharia de prompt
- Existem 3 exemplos de engenharia de prompt em ./Utils/characters:
  - butler.txt = personalidade de mordomo
  - helto_hater.txt = interpreta alguém que desgosta do streamer Helto
  - musk.txt = interpreta a persona de Elon Musk
 
## Conversando com o bot
- Vá até o chat do usuário colocado em streamId
- Converse com o bot utilizando @{botIdName} para referir-se à ele
  - exemplo:
  - input: Olá @testingbot9966
  - output: Olá! sou Elon Musk! Como posso ajudar?
- Vídeo de demonstração: https://www.youtube.com/watch?v=0as82V29gfQ
