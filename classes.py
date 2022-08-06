#vinkel argument for antal af decimaler
import math
class Trekant:
    def __init__(self, vinkel, længde):
        self.vinkel = vinkel
        self.længde = længde
        self.area = 0
        self.perimeter = 0

    def løsret(self):
        while 0 in self.vinkel or 0 in self.længde:
            self.retukendtv()
            self.retberegning()
            print(self.vinkel)
            print(self.længde)
        self.retarea()
        self.omkreds()
    


    def retarea(self):
        
        længde_a = self.længde[0]
        længde_b = self.længde [1]
        self.area = længde_a*længde_b*0.5
    

    def omkreds(self):
        længde_a = self.længde[0]
        længde_b = self.længde [1]
        længde_c = self.længde[2]
        self.perimeter = længde_a + længde_b + længde_c
        
    
    def retukendtv(self):
        vink_a = math.radians(self.vinkel[0])
        vink_b = math.radians(self.vinkel[1])
        vink_c = math.radians(self.vinkel[2])

        længde_a = self.længde[0]
        længde_b = self.længde [1]
        længde_c = self.længde[2]

        if vink_a > 0 and vink_b == 0 or vink_b > 0 and vink_a == 0:  
            beregnede_vinkel = math.radians(180) - (vink_a + vink_b + vink_c)
            if vink_a == 0:
                vink_a = beregnede_vinkel
            if vink_b == 0:
                vink_b = beregnede_vinkel
        
        #cos
        if længde_c and længde_b > 0 and vink_a == 0:
            vink_a = math.acos(længde_b/længde_c)
        if længde_c and længde_a > 0 and vink_b == 0:
            vink_b = math.acos(længde_a/længde_c)

        #sin
        if længde_c and længde_a > 0 and vink_a == 0:
            vink_a = math.asin(længde_a/længde_c)
        
        if længde_c and længde_b > 0 and vink_b == 0:
            vink_b = math.asin(længde_b/længde_c)

        #tan
        if længde_a and længde_b > 0 and vink_a == 0:
            vink_a = math.atan(længde_a/længde_b)
        
        if længde_a and længde_b > 0 and vink_b == 0:
            vink_b = math.atan(længde_b/længde_a)

        self.vinkel[0] = math.degrees(vink_a)
        self.vinkel[1] = math.degrees(vink_b)
    

    def retberegning(self):

        #definerer siderne og vinklerne i den givne retvinklede trekant.

        længde_a = self.længde[0]
        længde_b = self.længde [1]
        længde_c = self.længde[2]
        
        vink_a = math.radians(self.vinkel[0])
        vink_b = math.radians(self.vinkel[1])
        vink_c = math.radians(self.vinkel[2])
        
        #checkr, om trekantens side kan findes med pythagoras sætning
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

        self.længde[0]=længde_a
        self.længde[1]=længde_b
        self.længde[2]=længde_c
            

running = True

user_vinkel_a = float(input('Indtast vinkel A, hvis du ikke kender vinkel A, så bare skriv 0.\n'))
user_vinkel_b = float(input('Indtast vinkel B, hvis du ikke kender vinkel B, så bare skriv 0.\n'))
user_vinkel_c = float(input('Indtast vinkel C, hvis du ikke kender vinkel C, så bare skriv 0.\n'))
user_vinkler = [user_vinkel_a, user_vinkel_b, user_vinkel_c]
user_længder = [3, 0, 0]
user_trekant = Trekant(user_vinkler, user_længder)
user_trekant.løsret()
print ( f'Vinkel A:{user_trekant.vinkel[0]} Vinkel B: {user_trekant.vinkel[1]} Vinkel C: {user_trekant.vinkel[2]}')
print(f'a: {user_trekant.længde[0]} b: {user_trekant.længde[1]} c: {user_trekant.længde[2]}')
print(f'areal: {user_trekant.area}')
print(f'omkreds: {user_trekant.perimeter}')
