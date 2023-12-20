import json
import openai
import os

def lambda_handler(event, context):
    openai.api_key = os.getenv('API_KEY')

    # Log the body before parsing it
    print(f"event['body']: {event['body']}")

    # Parse the request body and extract the message
    if event['body'] is not None:
        body = json.loads(event['body'])
    else:
        body = {}
    chatHistory = body.get('chatHistory', [])

    # Convert chat history from request to the format expected by the OpenAI API
    messages = [{'role': msg['sender'], 'content': msg['message']} for msg in chatHistory]

    chat = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    
    gpt_response = chat.choices[0].message.content

    print("gpt_response:", gpt_response)

    try:
        # Your existing code...
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'message': gpt_response})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }
