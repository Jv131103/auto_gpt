import pyautogui
from time import sleep
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import keyboard as kb

def verificar_lps():
	return ("Linguagens disponíveis [Digite igual os exemplos]:\n" +
	"[1] -> python\n" +
	"[2] -> c\n" +
	"[3] -> c#\n" +
	"[4] -> php\n" +
	"[5] -> c++\n" +
	"[6] -> java\n" +
	"[7] -> js (Java Script)\n" +
	"[8] -> rust\n" +
	"[9] -> sql\n" +
	"[10] -> shell (Shell Script(Linux))\n" +
	"[11] -> bat (CMD/DOS Windows[EXE])\n" +
	"[0] -> ! (SAIR DO PROGRAMA)")

def converter(lp):
        d_lp = {"1": "python", "2": "c", "3": "c#", "4": "c++", "5": "php",
                "6": "java", "7": "js", "8": "rust", "9": "sql",
                "10":"shell", "11":"bat"}
        for c, v in d_lp.items():
                if lp == c:
                        return v
        else:
                return lp


def executar_maquina(lp):
        x = lp
        if x == "js":
                x = "Java Script"
        try:
                pyautogui.press('win')  # Pressione a tecla Win (ou ajuste para a tecla usada para abrir o menu Iniciar)
                sleep(0.5)
                pyautogui.write('Bloco de Notas')  # Digite "Notepad++" para localizar o programa
                sleep(0.5)
                pyautogui.press('enter')
                sleep(3)
                print("Executou!")
                pyautogui.write(f"""Hello, World em {x.title()}

""", interval=0.2)
                escrever_lp(lp)  # Escrever o código no Bloco de Notas
                pyautogui.press("enter")
                pyautogui.write("FIM!", interval=0.2)
                pyautogui.press("enter")
                pyautogui.write("Obrigado e volte sempre :)", interval=0.2)
                pyautogui.hotkey("alt", "f4")
        except TypeError as e:
                print("Para controle, vamos contornar esse Nonetype")
                print(e)
        except FileNotFoundError:
                print("Erro!")


def executar_no_chrome(lp):
        try:
                # Configurar opções do Chrome para usar um perfil temporário (navegação privada
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("--incognito")

                # Inicializar o driver do Chrome com as opções definidas
                driver = webdriver.Chrome(options=chrome_options)

                # Abrir o site
                driver.get("https://pt.anotepad.com/")

                # Aguardar 5 segundos para que o usuário visualize a página
                sleep(3)

                # Localizar o campo de texto pelo ID "edit_title"
                input_element = driver.find_element(By.ID, "edit_title")
                # Inserir texto no campo de texto
                input_element.send_keys(f"Hello, World em {lp.upper()}")

                # Aguardar 2 segundos para dar tempo de visualizar a alteração no campo de texto
                sleep(3)
                    
                # Localizar o campo de texto pelo ID "edit_textarea"
                textarea_element = driver.find_element(By.ID, "edit_textarea")
                # Clicar no campo de texto para dar foco
                textarea_element.click()
                cod_lp = escrever_lp(lp)
                # Clicar no campo de texto para dar foco
                textarea_element.send_keys(f"{cod_lp}")
        except Exception as e:
                print("Ocorreu um erro:", e)
        finally:
                sleep(5)
                # Fechar o navegador, se o driver estiver definido
                driver.quit()


def escrever_lp(lp):
        if lp == "1" or lp == "python":
                cod_py = kb.write("""print('Hello, World!')

""", delay=0.2)
                return cod_py
        elif lp == "2" or lp == "c":
                cod_c = kb.write("""#include <stdio.h>
#include <stdlib.h>

int main(){
        printf("Hello, World!");
        return 0;
        system("pause");
}

""", delay=0.2)
                return cod_c

        elif lp == "3" or lp == "c#":
                cod_csharp = kb.write("""using System;

class Program{
	static void Main(){
		Console.WriteLine("Hello, World!");
	}
}

""", delay=0.2)
                return cod_csharp

        elif lp == "4" or lp == "php":
                cod_php = kb.write('''<?php

php echo "Hello, World!"

?>

''', delay=0.2)
                return cod_php

        elif lp == "5" or lp == "c++":
                cod_cplus = kb.write("""#include <iostream>

int main() {
	std::cout << "Hello World!" << std::endl;
    	return 0;
}

""", delay=0.2)
                return cod_cplus

        elif lp == "6" or lp == "java":
                codjava = kb.write("""public class HelloWorld {
        public static void main(String[] args) {
                System.out.println("Hello, World!");
    	}
}

""", delay=0.2)
                return codjava

        elif lp == "7" or lp == "js":
                codjs = kb.write("""Console.log('Hello, World');

""", delay=0.2)
                return codjs

        elif lp == "8" or lp == "rust":
                codrust = kb.write("""fn main(){
	println!("Hello, World!");
}

""", delay=0.2)
                return pyautogui.typewrite(codrust, interval=0.2)

        elif lp == "9" or lp == "sql":
                codsql = kb.write("""CREATE TABLE hello(
	hello_ VARCHAR(15)
);

INSERT INTO hello(hello_)
VALUES("Hello, World!");

SELECT * FROM hello;

""", delay=0.2)
                return codsql

        elif lp == "10" or lp == "shell":
                codshell = kb.write('''echo "Hello, World!"

''', delay=0.2)
                return codshell

        elif lp == "11" or lp == "bat":
                codshell = kb.write('''echo "Hello, World!"
''', delay=0.2)

                return codshell

        else:
                return kb.write('''Desculpe não possuímos essa linguagem
no momento!
Você pode verificar qual linguagem quer ver o HELLO, WOLRD! digitando oo no menu interativo
''', delay=0.2)
                

if __name__ == "__main__":
        while True:
                lp = input("Qual LP quer ver: [oo -> Detalhes] ").strip().lower()
                if lp == "!" or lp == "0" or lp.lower() == "exit": break
                while lp == "oo":
                        print(verificar_lps())
                        lp = input("Qual LP quer ver: [oo -> Detalhes] ")
                lp = converter(lp)
                escolha = ""
                while escolha not in ["WEB", "MAQ"]:
                        escolha = input("Quer ver na WEB ou na máquina[Digite maq]? ").strip().upper()
                        if escolha == "WEB":
                                executar_no_chrome(lp)
                                print("FIM!")
                                print("Obrigado por acessar aqui :)")
                                print("Obrigado por acessar a nossa Plataforma Web!")
                                print("Volte Sempre")
                        elif escolha == "MAQ":
                                print("Peço que aguarde ....")
                                executar_maquina(lp)
                        elif escolha == "!": break
                        else:
                                print("Não entendi!")

