import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "ivoascjr9@gmail.com"
assunto = "Análises do Projeto 2020"

mensagem = f"""
Prezado gestor,

Seguem as análises solicitadas da ação {ticker}:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou a disposição!

Atte.
"""
# Abrir o navegador e ir para o gmail

webbrowser.open("www.gmail.com")
time.sleep(15)

# Configurando uma pausa de 7 segundos entre cada comando
pyautogui.PAUSE = 7

# Clicar no botão "Escrever"
pyautogui.click(x=81, y=185)

# Digitar o email do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

# Digitar o assunto do email
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

# Digitar o mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")

# Clica no botão "Enviar"

pyautogui.click(x=829, y=702)

# Fechar o gmail

pyautogui.hotkey("ctrl", "f4")

print("Email enviado com sucesso!")

