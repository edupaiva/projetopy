from fastapi import FastAPI

app = FastAPI()

@app.get("/{local}")
async def get_data(local):
        """Esta função recebe o nome da localidade pelo url como parametro 
           localiza o arquivo .txt referente a localidade e retorna os dados cadastrados
           Obs: Digite o nome da localidade em minusculo, sem acento e sem espaço
           Não é necessário digitar o .txt depois do nome da localidade
        """
        location=open(local+'.txt','r')
        list_of_lists = [float((line.strip())) for line in location]
        location.close()

        soma = round(sum(list_of_lists),2)
        quant = len(list_of_lists)
        media = round(soma/quant,2)
        maior = max(list_of_lists)
        menor = min(list_of_lists)
        
        return {"valores": list_of_lists , "soma": soma, "quantidade" : quant, "media" : media, "maior" : maior, "menor" : menor }
