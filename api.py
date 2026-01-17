from openai import OpenAI

# ⚠️ Hardcoding API keys is NOT recommended for production
client = OpenAI(
    api_key="sk-svcacct-X9US-viU2qBslrkGtp15CmSr1uoHonzcnWqRASdW7WE1XM2Y07KD7EO1r_CKRtX-FlZGcrIT3BlbkFJwXjurPPc2ZDyHaK45S0-ZWUX3yh8f_p9UGWb4yjmNzYix3IrabGpuoSKhETrKkAEiC6DNAA"
)

question = "What is gradient descent in machine learning?"

response = client.responses.create(
    model="gpt-4.1-mini",
    input=question
)

print(response.output_text)
