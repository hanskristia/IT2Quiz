from random import randint,choice, shuffle
class SpørsmålQuiz:
    """klasse for hvert quizspørsmål. Inneholder et riktig svar og andre svaralternativer
    Har en metode for å gi svar og svaralternativer i en tilfeldig rekkefølge, med fasit: giSpørsmål()"""
    
    def __init__(self, spørsmål:str, fasit:str, svaralternativer:list ) -> None:
        self.spørsmål=spørsmål
        self.fasit_indeks = randint(0,len(svaralternativer))
        
        self.svaralternativer=self.stokkListe(svaralternativer)
        self.svaralternativer.insert(self.fasit_indeks,fasit)

    def giSpørsmål(self)-> tuple[str,list]:
        """ returnerer spørsmålet, listen med svaralternativer"""
        return self.spørsmål, self.svaralternativer

    def erRiktig(self,svar:int):
        if svar-1 == self.fasit_indeks:
            return True
        else: 
            return False
    
    def stokkListe(self, liste:list)->list:
        """ stokker en liste"""
        stokket=[]
        while liste:
            valgt=choice(liste)
            liste.remove(valgt)
            stokket.append(valgt)
        return stokket

class Quiz:
    
    def __init__(self) -> None:
        self.stilteSpørsmål=[]
        self.spørsmål=[] 
        self.poeng = 0
        self.poengGrense = 2

    def setSpørsmål(self,spm:SpørsmålQuiz):
        """ Legger til et nytt spørsmål til denne quizen"""
        self.spørsmål.append(spm)
    
    def hentSpørsmål(self)->SpørsmålQuiz:
        """ Henter et spørsmål som ikke er stilt iløpet av denne quizen. """
        nytt_spørsmål = choice(self.spørsmål)
        self.spørsmål.remove(nytt_spørsmål) #flytter spørsmålet
        self.stilteSpørsmål.append(nytt_spørsmål)
        return nytt_spørsmål


    def stillSpørsmål(self, spørsmål:SpørsmålQuiz) -> int:
            """ printer en liste med spørsmålet og returnerer indeksen til riktig svar"""
            # spørsmålstekst, riktig, alternativer=spørsmål.giSpørsmål()
            spørsmålstekst, alternativer = spørsmål.giSpørsmål()

            print(spørsmålstekst)
            for i in range(len(alternativer)):
                print(f"{i+1}. ", alternativer[i])

    def erFerdig(self)->bool:
        if self.poeng >= self.poengGrense:
            return True
        elif len(self.spørsmål) == 0:
            return  True
        else:
            return False # Vi er ikke ferdige

    def play(self):
        """ en fun-fun-funksjon som lar deg spille et quiz spill.
        Målet er å komme til 2 poeng, raskest mulig.
        """
        while not self.erFerdig():

            spm = self.hentSpørsmål() # Henter et nytt spørsmål
            svar=int(input("Hva er riktig svaralternativ?")) #tar inn et svaralternativ. Disse går fra 1 og oppover.

            if spm.erRiktig(svar):
                self.poeng+=1
                print("riktig!")
            else:
                print("feil, riktig svar er ", spm.riktig)

        if self.poeng >= self.poengGrense :
            print("hurra! du fikk", self.poeng," på ", len(self.stilteSpørsmål), "forsøk")
        else:
            print("oi, vi gikk vist tomt for spørsmål...")
            print(self.spørsmål)


matteQuiz = Quiz()
spm1=SpørsmålQuiz("hva er 2+2?" , "4" , [1,2,3])
spm2=SpørsmålQuiz("hva er 3+2?" , "5" , [1,2,3])
spm3=SpørsmålQuiz("hva er 3+3?" , "6" , [1,2,3])
matteQuiz.setSpørsmål(spm1)
matteQuiz.setSpørsmål(spm2)
matteQuiz.setSpørsmål(spm3)
matteQuiz.setSpørsmål(SpørsmålQuiz("hva er 3+4?" , "7" , [1,2,3]))
matteQuiz.setSpørsmål(SpørsmålQuiz("hva er 3+5?" , "8" , [1,2,3]))
matteQuiz.setSpørsmål(SpørsmålQuiz("hva er 3+6?" , "9" , [1,2,3]))

matteQuiz.play()