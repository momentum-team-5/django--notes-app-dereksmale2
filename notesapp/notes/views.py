from django.shortcuts import render, redirect, get_object_or_404
from .models import Note


def notes_list(request):
    notes = Note.objects.all()

    return render(request, "notes/notes_list.html", {"notes": notes})


def notes_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note_filter = Note.objects.filter(note=note)

    if note_filter:
        note_filter = note_filter[0]

    else:
        note_filter = None

    return render(request, "notes/notes_detail.html", {"note": note, "note_filter": note_filter})


def add_note(request):
    if request.method == 'GET':
        form = NoteForm()

    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='notes_list')

    return render(request, "notes/add_note.html", {"form": form})


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'GET':
        form = NoteForm(instance=note)
    
    else:
        form = NoteForm(data=request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(to='notes_list')

    return render(request, "notes.edit_note.html", {"form": form, "note": note})


def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(to='notes_list')

    return render(request, "notes/delete_note.html", {"note": note})


