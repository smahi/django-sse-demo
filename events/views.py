from django.shortcuts import render
from django.http import StreamingHttpResponse

import asyncio
import random
import json

# Create your views here.
async def index_page(request):
    return render(request, "index.html")
        
async def stream_content():
    await asyncio.sleep(10)
    data = {
        "type": "info",
        "message": "Please place your finger on the sensor"
    }
    
    yield f'data: {json.dumps(data)}\n\n'
    await asyncio.sleep(random.randint(3, 5))

    data = {
        "type": "info",
        "message": "Scanning finger print....."
    }
    
    yield f'data: {json.dumps(data)}\n\n'
    await asyncio.sleep(random.randint(3, 5))

    data = {
        "type": "success",
        "message": "Finger print scanned successfully"
    }
    
    yield f'data: {json.dumps(data)}\n\n'
    await asyncio.sleep(random.randint(3, 5))

    
    
    


async def sse_events(request):
    return StreamingHttpResponse(stream_content(), content_type="text/event-stream")