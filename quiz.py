import random
class SpørsmålQuiz:
    """klasse for hvert quizspørsmål. Inneholder et riktig svar og andre svaralternativer
    Har en metode for å gi svar og svaralternativer i en tilfeldig rekkefølge, med fasit: stillSpørsmål()"""
    def __init__(self, spørsmål:str, riktig:str, svaralternativer:list ) -> None:
        self.spørsmål=spørsmål
        self.riktig=riktig
        self.svaralternativer=svaralternativer
    
    def giSpørsmål(self)-> tuple[str,str, list]:
        """ returnerer spørsmålet, riktig svar og listen med svaralternativer"""
        
        return self.spørsmål, self.riktig, self.svaralternativer
# En endring som er viktig

class Quiz:
    
    
    def __init__(self) -> None:
        self.stilteSpørsmål=[] #indekser over spørsmål som er stilt
        self.spørsmål=[] 
    def setSpørsmål(self,spm:SpørsmålQuiz):
        """ Legger til et nytt spørsmål til denne quizen"""
        self.spørsmål.append(spm)
    
    def getNyttspørsmål(self):
        """ Henter et spørsmål som ikke er stilt iløpet av denne quizen. """
        indeks= random.randint(0,len(self.spørsmål)-1)
        while indeks in self.stilteSpørsmål:
            indeks= random.randint(0,len(self.spørsmål)-1)
            #TODO fiks
        self.stilteSpørsmål.append(indeks)
        return self.spørsmål[indeks]


    def stillSpørsmål(self, spørsmål) -> int:
            """ printer en liste med spørsmålet og returnerer indeksen til riktig svar"""
            spørsmålstekst,riktig, alternativer=spørsmål.giSpørsmål()

            fasit=random.randint(0,len(alternativer))
            utskrift=self.stokk(alternativer)
            utskrift.insert(fasit, riktig)

            print (spørsmålstekst)
            for i in range(len(utskrift)):
                print(f"{i+1}. ", utskrift[i])

            return fasit

    def stokk(self, liste):
        """ stokker en liste"""
        stokket=[]
        for i in range(len(liste)):
            ny=liste.pop()
            stokket.insert(random.randint(0,len(stokket)),ny)
        return stokket

    def play(self):
        """ en fun-fun-funksjon som lar deg spille et quiz spill.
        Målet er å komme til 2 poeng, raskest mulig.
        """
        poeng=0

        while poeng<2 or len(self.stilteSpørsmål)== len(self.spørsmål):

            spm = self.getNyttspørsmål() # Henter et nytt spørsmål
            indeksFasit=self.stillSpørsmål(spm)  # Stiller spørsmålet med tilfeldig rekkefølge
            svar=int(input("Hva er riktig svaralternativ?")) #tar inn et svaralternativ. Disse går fra 1 og oppover.

            if indeksFasit==svar-1:
                poeng+=1
                print("riktig!")
            else:
                print("feil, riktig svar er ", spm.riktig)

        if poeng >= 2 :
            print("hurra! du fikk", poeng," på ", len(self.stilteSpørsmål), "forsøk")
        else:
            print("oi, vi gikk vist tomt for spørsmål...")


matteQuiz = Quiz()
spm1=SpørsmålQuiz("hva er 2+2?" , "4" , [1,2,3])
spm2=SpørsmålQuiz("hva er 3+2?" , "5" , [1,2,3])
spm3=SpørsmålQuiz("hva er 3+3?" , "6" , [1,2,3])
matteQuiz.setSpørsmål(spm1)
matteQuiz.setSpørsmål(spm2)
matteQuiz.setSpørsmål(spm3)
print("Hei, fra HAns")
matteQuiz.play()