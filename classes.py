#tilføj en samlende funktion der looper, gennem de 2 andre funktioner. men de 2 andre funktioner skal ikke loop. Add counter som går op hver cycle, hvis cycle bliver for stor, stop loop og return (jeg kan ikke løse problemet)

#skriv funktioner færdige i længde, så går over i vinkler.
import math
class Trekant:
    def __init__(self, vinkel, længde):
        self.vinkel = vinkel
        self.længde = længde

    
    def retukendtv(self):
        vink_a = self.vinkel[0]
        vink_b = self.vinkel[1]
        vink_c = self.vinkel[2]

        if vink_a > 0 and vink_b == 0 or vink_b > 0 and vink_a == 0:  
            beregnede_vinkel = 180 - (vink_a + vink_b + vink_c)
            if vink_a == 0:
                vink_a == beregnede_vinkel
            if vink_b == 0:
                vink_b == beregnede_vinkel
            

        self.vinkel[0]=vink_a
        self.vinkel[1]=vink_b
    

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

            if længde_c == 0.0 and længde_a != 0.0 and længde_b != 0.0:
                længde_c = (math.sqrt(længde_b**2 + længde_a**2))

            
            if længde_b == 0.0 and længde_a !=0.0 and længde_c != 0.0:
                længde_b = math.sqrt(længde_c**2 - længde_a**2)

            
            if længde_a == 00.0 and længde_b and længde_c != 0.0:
                længde_a = math.sqrt(længde_c**2 - længde_b**2)
            
            #checker om cos, sin, eller tan kan anvendes.
        
            #sin beregninger:
        
            if vink_a and længde_a > 0 and længde_c == 0.0:
                længde_c = længde_a/math.sin(vink_a)
            
            if vink_a and længde_c > 0 and længde_a == 0.0:
                længde_a = længde_c*math.sin(vink_a)
            
            if vink_b and længde_b > 0 and længde_c == 0.0:
                længde_c = længde_b/math.sin(vink_b)
              
            if vink_b and længde_c > 0 and længde_b == 0.0:
                længde_b = længde_c*math.sin(vink_b)
            
            #cos beregninger:
            if vink_a and længde_b > 0 and længde_c == 0.0:
                længde_c = længde_b/math.cos(vink_a)
            
            if vink_a and længde_c > 0 and længde_b == 0.0:
                længde_b = længde_c*math.cos(vink_a)

            if vink_b and længde_a > 0 and længde_c == 0.0:
                længde_c = længde_a/math.cos(vink_b)
            
            if vink_b and længde_c > 0 and længde_a == 0.0:
                længde_a = længde_c*math.cos(vink_b)

            #tan beregninger:
            if vink_a and længde_b > 0 and længde_a == 0.0:
                længde_a = længde_b*math.tan(vink_a)
            
            if vink_b and længde_a > 0 and længde_b == 0.0:
                længde_b = længde_a*math.tan(vink_b)



                
            
            

            

            continue
        self.længde[0]=længde_a
        self.længde[1]=længde_b
        self.længde[2]=længde_c




        
       # if vink_a and længde_a > 0 and længde_b and længde_c
            

        

running = True

user_vinkel_a = float(input('Indtast vinkel A, hvis du ikke kender vinkel A, så bare skriv 0.\n'))
user_vinkel_b = float(input('Indtast vinkel B, hvis du ikke kender vinkel B, så bare skriv 0.\n'))
user_vinkel_c = float(input('Indtast vinkel C, hvis du ikke kender vinkel C, så bare skriv 0.\n'))
user_vinkler = [user_vinkel_a, user_vinkel_b, user_vinkel_c]
user_længder = [3, 0.0, 0.0]
user_trekant = Trekant(user_vinkler, user_længder)
user_trekant.retukendtv()
print (user_trekant.vinkel)
user_trekant.retberegning()
print(f'a: {user_trekant.længde[0]} b: {user_trekant.længde[1]} c: {user_trekant.længde[2]}')
