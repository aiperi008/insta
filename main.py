from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="InstaSMM AI")


class SMMRequest(BaseModel):
    business_niche: str
    product_description: str

@app.post("/generate")
async def generate_content(request: SMMRequest):
    try:
        niche = request.business_niche
        desc = request.product_description

        if not niche or not desc:
            raise HTTPException(status_code=400, detail="Маалымат толук толтурулган жок!")


        return {
            "status": "success",
            "business_niche": niche,
            "data": {
                "strong_points": f"'{niche}' нишасы үчүн рыноктогу негизги артыкчылыктар аныкталды.",
                "content_plan": [
                    "1-күн: Продукция менен тааныштыруу",
                    "2-күн: Пайдалуу кеңештер жана лайфхактар",
                    "3-күн: Кардарлардын пикирлери жана акция"
                ],
                "post_text": f"Саламатсыздарбы! {desc} боюнча эң сонун сунуштарыбыз бар. Бизге келиңиздер!",
                "hashtags": "#бизнес #кыргызстан #instasmm #маркетинг",
                "reels_script": "Кадр 1: Товарды көрсөтүү. Кадр 2: Колдонуу процесси. Кадр 3: Даяр жыйынтык.",
                "direct_reply_templates": "Саламатсызбы! Баасы директте жазылды, сураныч көңүл буруңуз."
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)