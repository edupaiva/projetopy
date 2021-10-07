from fastapi import FastAPI


app = FastAPI()



@app.get("/{local}")
async def get_data(local):
       	
	location=open(local+'.txt','r')
        list_of_lists = [float((line.strip())) for line in location]
        location.close()

        soma = round(sum(list_of_lists),2)
        quant = len(list_of_lists)
        media = round(soma/quant,2)
        
        return {"valores": converted_list, "quant" : count, "media" : avg , "soma" : round(sum, 0)  }
