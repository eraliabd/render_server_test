from django.shortcuts import render

import config.settings
from .models import DollarCourse
import requests
import datetime


def main(request):
    current_date = datetime.date.today()

    API_KEY = config.settings.env.str("API_KEY")
    currency = "USD"
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

    response = requests.get(url)
    # print(response.status_code)
    course = response.json()['conversion_rate']
    # print(f"$1 - {course} som")

    if request.method == 'POST':
        som_input = request.POST.get('som_to_dollar', 0)
        dollar_input = request.POST.get('dollar_to_som', 0)
        # print(type(som_input), type(dollar_input))
        model = DollarCourse()

        if float(som_input) > 0:
            som_to_dollar = float(som_input) / course
            dollar_to_som = float(dollar_input) * course

            model.dollar_course = course
            model.dollar_input = dollar_input
            model.som_input = som_input
            model.som = som_to_dollar
            model.dollar = dollar_to_som
            model.save()

            context = {
                "course": course,
                "som_to_dollar": f"{som_to_dollar:.3f}",
                # "dollar_to_som": f"{dollar_to_som:.3f}",
                "date": current_date
            }
            return render(request, 'index.html', context)

        elif float(dollar_input) > 0:
            dollar_to_som = float(dollar_input) * course
            som_to_dollar = float(som_input) / course

            model.dollar_course = course
            model.dollar_input = dollar_input
            model.som_input = som_input
            model.som = som_to_dollar
            model.dollar = dollar_to_som
            model.save()

            context = {
                "course": course,
                # "som_to_dollar": f"{som_to_dollar:.3f}",
                "dollar_to_som": f"{dollar_to_som:.3f}",
                "date": current_date
            }
            return render(request, 'index.html', context)
    else:
        context = {
            "course": course,
            "date": current_date
        }
        return render(request, 'index.html', context)
