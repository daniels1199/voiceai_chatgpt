from dotenv import load_dotenv
import subprocess
from openai import OpenAI

# Configure a chave da API
load_dotenv()
client = OpenAI()

# Função para interagir com o modelo GPT-3.5 Turbo
def ask_gpt(prompt, prompt_list=[]):
    prompt_list.append({"role":"user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use o model GPT-3.5 Turbo
        messages = prompt_list,        
    )
    return response.choices[0].message

def speak_with_rhvoice(text):
    # Customize the RHVoice command based on your installation
    rhvoice_command = ['spd-say', '-o', 'rhvoice', '-l', 'pt','-w', text]
    # Use subprocess to call RHVoice
    subprocess.run(rhvoice_command)

def main():
    prompt_list = []
    while True:
        prompt = input("Você: ")

        if 'sair' in prompt.lower():
            speak_with_rhvoice("Tudo bem, Até logo.")
            break
    
    # Chamar a função ask_gpt com a entrada do usuário
        response = ask_gpt(prompt, prompt_list)
        prompt_list.append(response)
        print(f'Assistente: {response.content}')
        speak_with_rhvoice(response.content)

if __name__ == "__main__":
    print("Olá! Eu sou sua assistente virtual, como posso te ajudar?")
    speak_with_rhvoice("Olá! Eu sou sua assistente virtual, como posso lhe ajudar?")
    main()

