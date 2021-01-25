from fastapi import FastAPI


app = FastAPI()


@app.on_event('startup')
def startup():
  pass


@app.on_event('shutdown')
def shutdown():
  pass
