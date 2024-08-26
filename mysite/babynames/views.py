from django.shortcuts import render
from .models import BabyName

def index(request):
    # Get the list of available years for the dropdown
    years = BabyName.objects.values_list('year', flat=True).distinct().order_by('-year')

    # Default values for initial load
    selected_year = years.first()  # Default to the most recent year
    selected_sex = 'M'  # Default to 'M' (Male)

    # Query for the initial load (can be empty if you don't want to show any names at first)
    names = BabyName.objects.filter(
        year=selected_year,
        sex=selected_sex,
        year_rank__lte=100  # Adjust this condition if you want to include ties
    ).order_by('year_rank')

    # Render the index template
    return render(request, 'babynames/index.html', {
        'years': years,
        'selected_year': selected_year,
        'selected_sex': selected_sex,
        'sex_label': "Male",
        'names': names,
    })

def get_names(request):
    # Get selected year and sex from the request
    selected_year = request.GET.get('year')
    selected_sex = request.GET.get('sex')

    # Determine the label for the selected sex
    sex_label = "Male" if selected_sex == "M" else "Female"

    # Query for the top names based on rank <= 100
    names = BabyName.objects.filter(
        year=selected_year,
        sex=selected_sex,
        year_rank__lte=100
    ).order_by('year_rank')

    # Render the results.html template with the filtered data
    return render(request, 'babynames/results.html', {
        'selected_year': int(selected_year),
        'selected_sex': selected_sex,
        'sex_label': sex_label,
        'names': names,
    })


def search_name(request):
    # Initialize variables
    query_name = ''
    query_year_start = ''
    query_year_end = ''
    query_sex = ''
    results = []

    # Generate a list of years from 1880 to 2023
    years = list(range(1880, 2024))

    if request.method == 'GET':
        # Get the name, year range, and sex from the request
        query_name = request.GET.get('name', '').capitalize()
        query_year_start = request.GET.get('year_start', '1880')
        query_year_end = request.GET.get('year_end', '2023')
        query_sex = request.GET.get('sex', '')

        if query_name and query_year_start and query_year_end and query_sex:
            # Query the database for the specified name, year range, and sex
            results = BabyName.objects.filter(
                name=query_name,
                year__range=(query_year_start, query_year_end),
                sex=query_sex
            ).order_by('year')

        # Determine the label for the selected sex
        sex_label = "Male" if query_sex == "M" else "Female"

    return render(request, 'babynames/search.html', {
        'years': years,
        'query_name': query_name,
        'query_year_start': query_year_start,
        'query_year_end': query_year_end,
        'query_sex': query_sex,
        'sex_label': sex_label,
        'results': results,
    })

from django.shortcuts import render
from .models import BabyName

def search_results(request):
    # Get the name, year range, and sex from the request
    query_name = request.GET.get('name', '').capitalize()
    query_year_start = request.GET.get('year_start', '1880')
    query_year_end = request.GET.get('year_end', '2023')
    query_sex = request.GET.get('sex', '')

    results = []
    search_performed = False  # Flag to track if a search has been performed

    if query_name and query_year_start and query_year_end and query_sex:
        search_performed = True  # Set flag to True since search criteria are provided
        # Query the database for the specified name, year range, and sex
        results = BabyName.objects.filter(
            name=query_name,
            year__range=(query_year_start, query_year_end),
            sex=query_sex
        ).order_by('year')

    # Determine the label for the selected sex
    sex_label = "Male" if query_sex == "M" else "Female"

    return render(request, 'babynames/search_results.html', {
        'query_name': query_name,
        'query_year_start': query_year_start,
        'query_year_end': query_year_end,
        'query_sex': query_sex,
        'sex_label': sex_label,
        'results': results,
        'search_performed': search_performed,  # Pass the flag to the template
    })


