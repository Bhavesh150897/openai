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
