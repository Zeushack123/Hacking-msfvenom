class ZeusPirata:
    
    
    def vogais(self, palavra):
        # Variaveis importantes
        letras = "aeiouAEIOU"
        contador_vogais = 0
        contador_consoantes = 0
        
        # Cores
        cor_verde = '\033[92m'
        cor_padrao = '\033[0m'
        
        # Metodo usado para Descobir as vogais e consoantes
        for i in palavra:
            if i in letras:
                contador_vogais += 1
            else:
                if i.isalpha():
                    contador_consoantes += 1
        
        # Tratameto de singular e plural
        resultado_vogais = f"{contador_vogais} vogal" if contador_vogais == 1 else f"{contador_vogais} vogais"
        resultado_consoantes = f"{contador_consoantes} consoante" if contador_consoantes == 1 else f"{contador_consoantes} consoantes"
        
        # Mostra o resultado
        return f"Na palavra {cor_verde + palavra + cor_padrao} tem {resultado_vogais} e {resultado_consoantes}"
          

zeus = ZeusPirata()

resultado = zeus.vogais("abelha")
print(resultado)