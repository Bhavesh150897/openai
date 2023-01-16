from django.shortcuts import render
import openai

openai.api_key = "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"

model_engine = "text-davinci-003"

def home(request):
    if request.method == 'POST':
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=request.POST.get('openai'),
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        return render(request, 'poll/index.html', {'response':response})
    else:
        return render(request, 'poll/index.html')
