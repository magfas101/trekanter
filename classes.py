import math
class Trekant:
    def __init__(self, vinkel, længde):
        self.vinkel = vinkel
        self.længde = længde

    
    def ukendtv(self):
        vink_a = self.vinkel[0]
        vink_b = self.vinkel[1]
        vink_c = self.vinkel[2]

        if vink_a == 0 or vink_b == 0  or vink_c == 0:
            beregnede_vinkel = 180 - (vink_a + vink_b + vink_c)
            print(f'Den sidste vinkel er {beregnede_vinkel} grader')
            return beregnede_vinkel
        else:
            print('Denne funktion kan kun bruges til at beregne en manglende vinkel!')
    

    def retberegning(self):

        #definerer siderne og vinklerne i den givne retvinklede trekant.

        længde_a = self.længde[0]
        længde_b = self.længde [1]
        længde_c = self.længde[2]
        
        vink_a = math.radians(self.vinkel[0])
        vink_b = math.radians(self.vinkel[1])
        vink_c = math.radians(self.vinkel[2])
        
        #checkr, om trekantens side kan findes med pythagoras sætning
        while længde_a == 0.0 or længde_b == 0.0 or længde_c == 0.0:
            
            print(f'{længde_b} {længde_a}  {længde_c}')


            if længde_c == 0.0 and længde_a != 0.0 and længde_b != 0.0:
                beregnede_længde = (math.sqrt(længde_b**2 + længde_a**2))

                print(f'den beregnede længde er: {beregnede_længde} a')
            
            if længde_b == 0.0 and længde_a !=0.0 and længde_c != 0.0:
                længde_b = math.sqrt(længde_c**2 - længde_a**2)
                print(f'den beregnede længde er: {længde_c} b' )
                print(f'{længde_b} {længde_a}  {længde_c}')

            
            if længde_a == 00.0 and længde_b and længde_c != 0.0:
                beregnede_længde = math.sqrt(længde_c**2 - længde_b**2)
                print(f'den beregnede længde er: {beregnede_længde} c')
            
            #checker om cos, sin, eller tan kan anvendes.
        
            #sin beregninger:
        
            if vink_a and længde_a > 0 and længde_c == 0.0:
                længde_c = længde_a/math.sin(vink_a)
                print(f'den beregnede længde er: {længde_c} d')
            
            if vink_a and længde_c > 0 and længde_a == 0.0:
                længde_a = længde_c*math.sin(vink_a)
                print(f'den beregnede længde er: {længde_a} e')
            
            if vink_b and længde_b > 0 and længde_c == 0.0:
                beregnede_længde = længde_b/math.sin(vink_b)
                print(f'den beregnede længde er: {beregnede_længde} f')
            
            if vink_b and længde_c > 0 and længde_b == 0.0:
                beregnede_længde = længde_c*math.sin(vink_b)
                print(f'den beregnede længde er: {beregnede_længde} g')
            
            #cos beregninger:
            if vink_a and længde_b > 0 and længde_c == 0.0:
                beregnede_længde = længde_b/math.cos(vink_a)
                print(f'den beregnede længde er: {beregnede_længde} h')
            
            if vink_a and længde_c > 0 and længde_b == 0.0:
                beregnede_længde = længde_c*math.cos(vink_a)
                print(f'den beregnede længde er: {beregnede_længde} j')
            
            continue


            #tan beregninger:




        
       # if vink_a and længde_a > 0 and længde_b and længde_c
            

        

running = True

user_vinkel_a = float(input('Indtast vinkel A, hvis du ikke kender vinkel A, så bare skriv 0.\n'))
user_vinkel_b = float(input('Indtast vinkel B, hvis du ikke kender vinkel B, så bare skriv 0.\n'))
user_vinkel_c = float(input('Indtast vinkel C, hvis du ikke kender vinkel C, så bare skriv 0.\n'))
user_vinkler = [user_vinkel_a, user_vinkel_b, user_vinkel_c]
user_længder = [0.0, 0.0, 5]
user_trekant = Trekant(user_vinkler, user_længder)
user_trekant.ukendtv()
user_trekant.retberegning()