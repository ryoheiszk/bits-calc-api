from fastapi import FastAPI
import unicodedata

app = FastAPI()

@app.get("/{target_str}")
def root(target_str):
    bits = 0
    for char in target_str:
        if unicodedata.east_asian_width(char) in "FWA":
            bits += 2
        else:
            bits += 1

    return {"bits": bits}
