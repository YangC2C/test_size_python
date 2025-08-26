from fastapi import FastAPI
import get_news 

app = FastAPI()

@app.get("/")
async def root():
    list_1 = get_news.jeju_news()
    list_2 = get_news.jemin_news()
    list_3 = get_news.omai_news()
    
    list_1.extend(list_2)
    list_1.extend(list_3)
    
    return list_1
