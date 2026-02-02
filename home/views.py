from django.shortcuts import render, redirect, get_object_or_404
from .models import NoteData
from .forms import NotesForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# ----------------------
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


# Create note
@login_required
def index(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("notes_detail")
    else:
        form = NotesForm()
    return render(request, "index.html", {"form": form})


# ----------------------
# Show all notes
@login_required
def notes_detail(request):
    notes = NoteData.objects.filter(user=request.user, is_trashed=False).order_by(
        "-created_at"
    )
    return render(request, "notes_detail.html", {"notes": notes})


# ----------------------
# Open single note
@login_required
def open_note(request, pk):
    note = get_object_or_404(NoteData, id=pk, user=request.user)
    return render(request, "open_note.html", {"open_note": note})


# ----------------------
# Edit note
@login_required
def edit_note(request, pk):
    note = get_object_or_404(NoteData, id=pk, user=request.user)
    if request.method == "POST":
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes_detail")
    else:
        form = NotesForm(instance=note)
    return render(request, "edit_note.html", {"form": form})


# ----------------------
# Move note to trash
@login_required
def move_to_trash(request, pk):
    note = get_object_or_404(NoteData, id=pk, user=request.user)
    note.is_trashed = True
    note.save()
    return redirect("notes_detail")


# ----------------------
# Restore note from trash
@login_required
def return_note(request, pk):
    note = get_object_or_404(NoteData, id=pk, user=request.user)
    note.is_trashed = False
    note.save()
    return redirect("trash_notes")


# ----------------------
# Show trashed notes
@login_required
def trash_notes(request):
    notes = NoteData.objects.filter(user=request.user, is_trashed=True).order_by(
        "-created_at"
    )
    return render(request, "trash_notes.html", {"trash_notes": notes})


# ----------------------
# Delete note permanently
@login_required
def delete_note(request, pk):
    note = get_object_or_404(NoteData, id=pk, user=request.user)
    note.delete()
    return redirect("trash_notes")


# ----------------------
# Detect user (Profile page)
@login_required
def detect_user(request):
    return render(request, "detect_user.html", {"user": request.user})
