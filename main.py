from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import get_news

app = FastAPI()

# Serve static files (like css, js) from the 'static' directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/api/news")
async def get_news_api():
    """API endpoint to get the list of news articles."""
    list_1 = get_news.jeju_news()
    list_2 = get_news.jemin_news()
    list_3 = get_news.omai_news()
    
    list_1.extend(list_2)
    list_1.extend(list_3)
    
    return list_1

@app.get("/")
async def read_index():
    """Serves the main index.html file."""
    
    return FileResponse('static/index.html')
