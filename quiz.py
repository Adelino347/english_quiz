from tkinter import *
import random


class Quiz(object):
    def __init__(self, conteiner, texto_enunciado, opcoes):
        """

        conteiner  --> Objeto onde um frame contendo os widgets será empacotado

        textos_enunciado --> Uma lista contendo strings com o(s) texto(s) do enunciado
        
        opcoes  -->  Uma lista contendo listas aninhadas onde há, para cada lista aninhada, no índice 0 os texto das alternativa, no índice 1 o valor da alternativa (ambos strings) e no índice 2 o método atribuído ao Radiobutton da alternativa" 
        """
        
        self.frame = Frame(self.conteier)
        self.frame1 = Frame(self.frame)
        self.frame2 = Frame(self.frame)
        self.frame.pack()
        self.frame1.pack()
        self.frame2.pack()

        self.texto_enunciado = textos_enunciado
        self.texto_opcoes = (opcao[0] for opcao in opcoes)
        self.valor_opces = (opcao[1] for opcao in opcoes)
        self.comandos_opcoes = (opcao[2] for opcao in opcoes)
        self.labels_enunciado = []
        self.radiobuttons_opcoes = []

        for texto in textos_enunciado:
            label = Label(self.frame1, text = texto)
            label.pack(side = LEFT)
            self.labes_enunciado.append(label)

        self.resposta = StrVar()
        for indice in range(len(texto_opcoes)):
            opcao = Radiobutton(self.frame2, indicaratoron = self.indicatoron, text = self.texto_opcoes[indice], value = self.valor_opcoes[indice], variable = self.resposta, command = self.comandos_opcoes[indice])
            opcao.pack(side = LEFT, anchor = W)
        
        

        
class QuizEnglishTime1(object):
    def __init__(self):
        self.minutes = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
           'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
           'twenty-one', 'twenty-two', 'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven', 'twenty-eight', 'twenty-nine', 'thirty',
           'thirty-one', 'thirty-two', 'thirty-three', 'thirty-four', 'thirty-five', 'thirty-six', 'thirty-seven', 'thirty-eight', 'thirty-nine', 'forty',
           'forty-one', 'forty-two', 'forty-three', 'forty-four', 'forty-five', 'forty-six', 'forty-seven', 'forty-eight', 'forty-nine', 'fifty',
           'fifty-one','fifty-two', 'fifty-three', 'fifty-four', 'fifty-five', 'fifty-six', 'fifty-seven', 'fifty-eight', 'fifty-nine']

        self.num_escrita = {0:"o'clock", 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
                            11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',20:'twenty',
                            21:'twenty-one', 22:'twenty-two', 23:'twenty-three', 24:'twenty-four', 25:'twenty-five', 26:'twenty-six', 27:'twenty-seven', 28:'twenty-eight', 29:'twenty-nine', 30:'thirty',
                            31:'thirty-one', 32:'thirty-two', 33:'thirty-three', 34:'thirty-four', 35:'thirty-five', 36:'thirty-six', 37:'thirty-seven', 38:'thirty-eight', 39:'thirty-nine', 40:'forty',
                            41:'forty-one', 42:'forty-two', 43:'forty-three', 44:'forty-four', 45:'forty-five', 46:'forty-six', 47:'forty-seven', 48:'forty-eight', 49:'forty-nine', 50:'fifty',
                            51:'fifty-one', 52:'fifty-two', 53:'fifty-three', 54:'fifty-four', 55:'fifty-five', 56:'fifty-six', 57:'fifty-seven', 58:'fifty-eight', 59:'fifty-nine'}
        
        self.horas_analog = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
        
        
        self.bg = "#00003f"
        self.bg_alternativas = 'white'
        self.fonte_pergunta = ('Times New Roman', 20, 'bold')
        self.fonte_alternativas = ("Comic Sans MS", 14)
        self.fg_pergunta = 'white'
        self.fg_alternativas = 'black'
        self.janela = Tk()
        self.janela.configure(background = self.bg)
        
        self.frame = Frame(self.janela, bg = self.bg)
        self.frame1 = Frame(self.frame, bg = self.bg)
        self.frame2 = Frame(self.frame, bg = self.bg)
        self.frame3 = Frame(self.frame, bg = self.bg)
        self.frame4 = Frame(self.frame, bg = self.bg)
        self.frame5 = Frame(self.frame, bg = self.bg)
        self.frame6 = Frame(self.frame, bg = self.bg)
        self.frame.pack()
        self.frame1.pack(anchor = W)
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        

        self.pergunta = Label(self.frame1,text = "* What's the time?", fg = self.fg_pergunta, bg = self.bg, font = self.fonte_pergunta, height = 3, width = 30, anchor = W)
        self.horaApresentada = Label(self.frame2, fg = 'darkred', bg = 'white', font = ('Impact', 30, 'bold'), relief = SOLID, height = 3, width =  10)
        self.resposta = StringVar()
        self.opcao1 = Radiobutton(self.frame3, indicatoron = 0, cursor = 'hand2', variable = self.resposta, text = "  A)  It's ", relief = SOLID, width = 45, height = 2, font = self.fonte_alternativas, anchor = W, command = self.conferir_botao, fg = self.fg_alternativas, bg = self.bg_alternativas)
        self.opcao2 = Radiobutton(self.frame4, indicatoron = 0, cursor = 'hand2', variable = self.resposta, text = "  B)  It's ", relief = SOLID, width = 45, height = 2, font = self.fonte_alternativas, anchor = W, command = self.conferir_botao, fg = self.fg_alternativas, bg = self.bg_alternativas)
        self.opcao3 = Radiobutton(self.frame5, indicatoron = 0, cursor = 'hand2', variable = self.resposta, text = "  C)  It's ", relief = SOLID, width = 45, height = 2, font = self.fonte_alternativas, anchor = W, command = self.conferir_botao, fg = self.fg_alternativas, bg = self.bg_alternativas)
        self.opcao4 = Radiobutton(self.frame6, indicatoron = 0, cursor = 'hand2', variable = self.resposta, text = "  D)  It's ", relief =SOLID, width = 45, height = 2, font = self.fonte_alternativas, anchor = W, command = self.conferir_botao, fg = self.fg_alternativas, bg = self.bg_alternativas)                          
        self.pergunta.pack(side = LEFT)
        self.horaApresentada.pack(side = LEFT)
        self.opcao1.pack(side = LEFT)
        self.opcao2.pack(side = LEFT)
        self.opcao3.pack(sid = LEFT)
        self.opcao4.pack(side = LEFT)

        self.opcao1.bind("<Return>", self.conferir1)
        self.opcao2.bind("<Return>", self.conferir2)
        self.opcao3.bind("<Return>", self.conferir3)
        self.opcao4.bind("<Return>", self.conferir4)
        self.horas_ditas = []
        self.perguntar()
        
    def perguntar(self):
        self.horas_opcoes = []
        self.hora = random.randint(1,12)
        self.minutos = random.randint(0,59)
        self.horaEscolhida = str(self.hora)+":"+str(self.minutos)
        if self.minutos<10:
            self.horaEscolhida = str(self.hora)+":0"+str(self.minutos)
        if self.hora<10:
            self.horaEscolhida = '0'+self.horaEscolhida
        while self.horaEscolhida in self.horas_ditas:
            self.hora = random.randint(1,12)
            self.minutos = random.randint(0,59)
            self.horaEscolhida = str(self.hora)+":"+str(self.minutos)
            if self.minutos<10:
                self.horaEscolhida = str(self.hora)+":0"+str(self.minutos)
            if self.hora<10:
                self.horaEscolhida = '0'+self.horaEscolhida
                
        self.horaApresentada['text'] = self.horaEscolhida
        
        self.horas_ditas.append(self.horaEscolhida)
        self.opcoes = [self.opcao1, self.opcao2, self.opcao3, self.opcao4]


        self.opcaoCorreta = self.opcoes[random.randint(0,3)]
        self.opcoes.remove(self.opcaoCorreta)
        
        self.valorCorreto = "%s %s" % (self.num_escrita[self.hora], self.num_escrita[self.minutos])
        self.opcaoCorreta['text'] = self.opcaoCorreta['text'][:11] + self.valorCorreto
        self.opcaoCorreta['value'] = self.valorCorreto
        
        opcoes = [self.valorCorreto]
        for opcao in self.opcoes:
            valor = "%s %s" % (random.choice(self.horas_analog), random.choice(self.minutes))
            while valor in opcoes:
                valor = "%s %s" % (random.choice(self.horas_analog), random.choice(self.minutes))
            opcoes.append(valor)
            opcao['text'] = opcao['text'][:11]+ valor
            opcao['value'] = valor

    def conferir_botao(self):
        if self.resposta.get() == self.valorCorreto:
            print("Acertô!")
            self.perguntar()
        else:
            print("Errou!")
    def conferir1(self, event):
        self.opcao1.invoke()
    def conferir2(self, event):
        self.opcao2.invoke()
    def conferir3(self, event):
        self.opcao3.invoke()
    def conferir4(self, event):
        self.opcao4.invoke()

class QuizEnglishTime2(QuizEnglishTime1):
    def perguntar(self):
        self.horas_opcoes = []
        self.hora = random.randint(1,12)
        self.minutos = random.randint(0,59)
        self.horaEscolhida = str(self.hora)+":"+str(self.minutos)
        if self.minutos<10:
            self.horaEscolhida = str(self.hora)+":0"+str(self.minutos)
        if self.hora<10:
            self.horaEscolhida = '0'+self.horaEscolhida
        while self.horaEscolhida in self.horas_ditas:
            self.hora = random.randint(1,12)
            self.minutos = random.randint(0,59)
            self.horaEscolhida = str(self.hora)+":"+str(self.minutos)
            if self.minutos<10:
                self.horaEscolhida = str(self.hora)+":0"+str(self.minutos)
            if self.hora<10:
                self.horaEscolhida = '0'+self.horaEscolhida
                
        self.horaApresentada['text'] = self.horaEscolhida
        
        self.horas_ditas.append(self.horaEscolhida)
        self.opcoes = [self.opcao1, self.opcao2, self.opcao3, self.opcao4]


        self.opcaoCorreta = self.opcoes[random.randint(0,3)]
        self.opcoes.remove(self.opcaoCorreta)

        self.valorCorreto = self.retornarEscrita(self.minutos, self.hora)
        
        self.opcaoCorreta['text'] = self.opcaoCorreta['text'][:11] + self.valorCorreto
        self.opcaoCorreta['value'] = self.valorCorreto
        
        opcoes = [self.valorCorreto]
        for opcao in self.opcoes:
            valor = self.retornarEscrita(random.randint(1, 12), random.randint(0,59))
            while valor in opcoes:
                valor = self.retornarEscrita(random.randint(1, 12), random.randint(0,59))
            opcoes.append(valor)
            opcao['text'] = opcao['text'][:11]+ valor
            opcao['value'] = valor
            
    def retornarEscrita(self, minutos, hora):
        if minutos == 30:
            valor = "%s half past %s"% (self.num_escrita[minutos], self.num_escrita[hora])
            
        if minutos<30 and minutos != 0:
            valor = "%s past %s" % (self.num_escrita[minutos], self.num_escrita[hora])
            
        elif minutos>30:
            if hora == 12:
                valor = "%s to %s" % (self.num_escrita[60-minutos], 'one')
            else:
                valor = "%s to %s" % (self.num_escrita[60-minutos], self.num_escrita[hora+1])
        else:
            valor = "%s %s" % (self.num_escrita[hora], self.num_escrita[minutos])
        return valor


if __name__ == '__main__':
    QuizEnglishTime2()
    QuizEnglishTime1()
        
        
