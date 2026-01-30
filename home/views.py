from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NoteData
from .forms import NotesForm

# Create your views here.


# Write information
def index(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes_detail")
    else:
        form = NotesForm()

    return render(request, "index.html", {"form": form})


# Notes Informationl
def notes_detail(request):
    notes = NoteData.objects.filter(is_trashed=False).order_by("-created_at")
    return render(request, "notes_detail.html", {"notes": notes})


# Open Note
def open_note(request, pk):
    open_note = NoteData.objects.get(id=pk)
    return render(request, "open_note.html", {"open_note": open_note})


# Edit notes
def edit_note(request, id):
    note = NoteData.objects.get(id=id)
    if request.method == "POST":
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes_detail")
    else:
        form = NotesForm(instance=note)

    return render(request, "edit_note.html", {"form": form})


# Move to trash
def move_to_trash(request, id):
    item = NoteData.objects.get(id=id)
    item.is_trashed = True
    item.save()
    return redirect("notes_detail")
    
# Return Note
def return_note(request, pk):
    item = NoteData.objects.get(pk=pk)
    item.is_trashed = False
    item.save()
    return redirect("trash_notes")

# Trashes look
def trash_notes(request):
    trash_notes = NoteData.objects.filter(is_trashed=True).order_by("-created_at")
    return render(request, "trash_notes.html", {"trash_notes": trash_notes})


# Delete note
# To‘g‘ri
def delete_note(request, id):
    note = NoteData.objects.get(id=id)
    note.delete()
    return redirect("trash_notes")
