from dotenv import load_dotenv
load_dotenv()
from lambda_function import lambda_handler

event = {"text": "which is the best God of war game"}
context = None
result = lambda_handler(event, context)
print(result)
