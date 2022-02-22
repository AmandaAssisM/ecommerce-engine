import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        'app.main:app',
        host='172.21.161.123',
        port=8001,
        reload=True
    )