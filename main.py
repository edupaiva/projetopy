from fastapi import FastAPI


app = FastAPI()



@app.get("/{local}")
async def get_data(local):
        location=open(local+'.txt','r')
        values=location.readlines()
        sum =0
        avg=0
        count=0

        for v in values:
	        count+=1
	        sum+=float(v)

        avg = round(sum/count,0)

        sample_list = values
        converted_list = []

        for element in sample_list:
            converted_list.append(element.strip())
        
        return {"valores": converted_list, "quant" : count, "media" : avg , "soma" : round(sum, 0)  }