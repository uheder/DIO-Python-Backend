from fastapi import FastAPI
import uvicorn


app = FastAPI(title='WorkoutAPI')

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8080, log_level='info', reload=True)