from django.shortcuts import HttpResponse
from django.template import loader
from main.services import calculate_week_number
#from django.views.decorators.cache import cache_page

#@cache_page(60 * 60 * 24)
def main_page(request):
    template = loader.get_template('index.html')
    context = {"calculate": "Расчитать"}
    
    if request.method == 'GET':
        week_number = None
        try:
            input_date = request.GET['date']
            week_number = calculate_week_number(input_date=input_date)
            if week_number:
                context['week_number'] = f"Номер запрашиваемой недели - {str(week_number)}"
                context['calculate'] += " ещё"
        except:
            pass

    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)    