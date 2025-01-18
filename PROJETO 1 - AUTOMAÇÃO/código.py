import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.7

# ENTRAR NO SISTEMA / abrir o google
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)

# REALIZAR LOGIN
pyautogui.click(x=530, y=376)
pyautogui.write("mv969870@gmail.com")
pyautogui.press("tab")
pyautogui.write("asiujfgvasi")
pyautogui.press("enter")


#IMPORTAR BASE DE DADOS
tabela = pandas.read_csv("produtos.csv")

time.sleep(1)


# CADASTRAR 1 PRODUTO / REPETIR O PROCESSO PARA TODOS

for linha in tabela.index:
    pyautogui.click(x=534, y=260)
    
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(10000)