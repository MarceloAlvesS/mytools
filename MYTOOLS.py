def pi_real(N: int):
     global PI_INT

     if N == 0:
        return '3'
     elif N <= 100:
        return '3,' + PI_INT[:N]
     else:
         print('Não está registrado mais de 100 casas do numero pi')
         return PI_INT

def e_real(N: int):
     global E_INT

     if N == 0:
        return '2'
     elif N <= 100:
        return '2,' + E_INT[:N]
     else:
         print('Não está registrado mais de 100 casas do numero e')
         return E_INT

PI_INT: str = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
E_INT: str = '7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274'
