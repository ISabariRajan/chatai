# from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def chatbot_response(request):
    prompt = request.POST.get('prompt', '')
    # process the prompt and generate a response
    response = generate_response(prompt)
    if response['type'] == 'text':
        # if the response is text, return a JsonResponse with the text
        return JsonResponse({'response': response['text']})
    elif response['type'] == 'image':
        # if the response is an image, return a JsonResponse with the URL of the image
        return JsonResponse({'response': response['url']})