from collections import Counter
from django.shortcuts import render
import matplotlib.pyplot as plt
from .models import Vote
from django.http import HttpResponse
import base64
from io import BytesIO
from django.shortcuts import render, redirect
from .forms import VoteForm


def vote(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = VoteForm()
    return render(request, 'example/vote.html', {'form': form})


def success(request):
    return render(request, 'example/success.html')


def histogram(request):
    # Query the database to get the votes
    votes = Vote.objects.values_list('choice', flat=True)

    # Count the occurrences of each candidate
    candidate_counts = dict(Counter(votes))

    # Plotting the histogram
    plt.bar(candidate_counts.keys(), candidate_counts.values())
    plt.xlabel('Candidates')
    plt.ylabel('Votes Count')
    plt.title('Votes Histogram')

    # Save plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Encode plot to base64 string
    plot_data = base64.b64encode(buffer.getvalue()).decode()

    plt.close()

    # Render template with base64 encoded plot
    return render(request, 'example/histogram.html', {'plot_data': plot_data})
