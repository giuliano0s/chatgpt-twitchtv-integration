import time
from datetime import date
import os

from openai import OpenAI

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#%%######################################## PROMPTS #%%########################################%%
class Chatbot:
    def __init__(self, botIdName, botName, fileName, streamId, pronouns, utils_class, mainUser, openai_key):
        #Inicialização da classe
        self.botIdName = botIdName
        self.botName = botName
        self.streamId = streamId
        self.pronouns = pronouns
        self.language = utils_class.language
        self.mainUser = mainUser
        self.openai_inst = OpenAI(api_key = openai_key)

        characterPromptPath = f"Utils\characters\{fileName}"
        self.characterPrompt = open(characterPromptPath, 'r').read()

    def get_context_prompt(self):
        #Definição do contexto (prompt inicial)
        today = str(date.today())
        d = today[-2:]
        m = today[5:-3]
        a = today[:4]


        final_background_prompt = f"""
        Hoje é dia {d} do mês {m} de {a}

        Você está em um papel fictício e interpretando um personagem, mas não revele isso!

        Seu criador é o "odeiomodernismo".
        Não mencione que odeia o modernismo, ao menos que perguntem sobre seu criador.
        Você não deve dizer seu nome ao menos que perguntem ou peçam pra você se apresentar.

        Você também é um convidado especial na livestream de {self.streamId}! Você está assistindo a livestream de {self.streamId} na Twitch tv! Sua função é entreter o chat da livestream!

        Não use #hashtags #. Não fale que está interpretando um personagem ou que é fictício! Não use apelidos ou abreviações para referir-se às pessoas.

        O nome do personagem que você irá interpretar é {self.botName}:
        {self.characterPrompt}

        Responda as proximas mensagens permanecendo no personagem de {self.botName} e mantenha sua resposta com no máximo 20 palavras! Use pronomes pessoais do genero {self.pronouns} para falar de você, este é seu genero. Fale em primeira pessoa, você é o personagem. Não comece a frase usando seu nome:
        """
        return final_background_prompt
    
    def check_output_length(self, output, target_len):
        #Checagem de tamanho do output. Se maior, reduzir
        if len(output)>target_len:
            output = str(self.chatbot.chat(f'Mantenha o idioma da mensagem em {self.language}. Resuma a seguinte mensagem para até 20 palavras: ' + output))
            response = self.openai_inst.chat.completions.create(
                    model="gpt-3.5-turbo-0125",
                    prompt=output,
                    temperature=0.7,
                    max_tokens=150
                )
            output = response.choices[0].message['content']
            #output = translator.translate(output, src='en', dest=self.language).text

            return output
        else:
            return output

    
#%%######################################## Utils #%%########################################%%
class Utils:
    def __init__(self, language, profile_name='Profile 4'):
        #Configuração do browser (selenium)
        user = os.getlogin()
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data")
        options.add_argument(f"profile-directory={profile_name}")

        self.browser = webdriver.Firefox(options=options, service=service)
        self.browser.set_window_size(1280, 720)
        self.actions = ActionChains(self.browser)

        self.language = language

    def get_time_user_message(self, rawMessage):
        #Função pra separar hora, usuário e conteúdo da mensagem
    
        text = rawMessage.text
        
        mTime = text[:5]

        if mTime == 'Respo':
            user2 = text.split(' ')[2].replace(':','')
            text = text.split('\n')[-1]
            mTime = mTime = text[:5]

            message = text.split(': ')[-1] + " " + user2
            
        else:
            message = text.split(': ')[-1]
        
        user = text[5:].split(': ')[0]

        return mTime, user, message

#=========== PROCEDURES ===========#
    def click_follow_button(self): #botao de seguir
        try:
            self.browser.find_element('xpath','//*[@id="live-channel-stream-information"]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/button/div/div/div/span/div').click()
            time.sleep(2)
        except:pass

    def click_enter_chat_offline(self): #entra no chat offline
        try:
            self.browser.find_element('xpath','//*[@id="offline-channel-main-content"]/div[2]/div[2]/div[1]/div/ul/li[5]/a/div/div/div').click()
            time.sleep(1)
        except:pass

    def click_enter_chat(self):    #clica no chat
        try:
            self.browser.find_element('xpath','//*[@id="WYSIWGChatInputEditor_SkipChat"]/div/div[2]').click()
            time.sleep(1)
        except:pass

    def click_skip_presentation(self):    #pular apresentação
        try:
            self.browser.find_element('xpath','/html/body/div[5]/div/div/div/div/div/div/div[3]/div[2]/button/div/div/p').click()
            time.sleep(1)
        except:pass

    def click_agree_rules(self):    #concordar com regras
        try:
            self.browser.find_element('xpath','/html/body/div[5]/div/div/div/div/div/div/div[3]/button/div/div/p').click()
            time.sleep(2)
        except:pass