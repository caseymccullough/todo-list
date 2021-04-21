from django.shortcuts import render, redirect
from .models import Artist, Song
from .forms import ArtistForm, SongForm

# Index
# New
# Destroy
# Update
# Create
# Edit
# Show


#Index Artists
def artist_list (request): # request = a special object that holds info that was sent from the browser
    artists = Artist.objects.all()
    return render(request, 'tunr/artist_list.html', {'artists': artists} ) 
    # 2nd argument describes template 
    #3rd what we are injecting . . . 

#Index Songs
def song_list (request): # request = a special object that holds info that was sent from the browser
    songs = Song.objects.all()
    return render(request, 'tunr/song_list.html', {'songs': songs} ) 
    # 2nd argument describes template
    # 3rd what we are injecting . . . 

# New/ Create
# invoked when user wants to create a new artist
def artist_create(request):
    if request.method == "POST":
        #create a form instance and populate from data
            form = ArtistForm(request.POST)
            #check whether it's valid
            if form.is_valid():
                # Save new artist and redirect to its show page
                artist = form.save()
                return redirect('artist_detail', pk = artist.pk)
            else:
                form = ArtistForm()
                return render(request, 'tunr/artist_form.html', {'form': form})

# Destroy an artist
def artist_delete(request, pk):
    Artist.object.get(id=pk).delete()
    # back to artist list page 
    return redirect('artist_list')


# Update / Edit
def artist_edit (request, pk):
    artist = Artist.objects().get(pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save() # data now from form prev from db
            return redirect('artist_detail', pk=artist.pk)
        else: # they are requesting to get the form
            form = ArtistForm(instance = artist) # populate with current data
            return render(request, 'tunr/artist_form.html', {'form': form})



    


#Show a single artist
# /artists/:id  note id must be primary key
def artist_detail(request, pk): # primary key
    artist = Artist.objects.get(id=pk)
    return render (request, 'tunr/artist_detail.html', {'artist': artist})

#Show a single song
# /song/:id  note id must be primary key
def song_detail(request, pk): # primary key
    song = Song.objects.get(id=pk)
    return render (request, 'tunr/song_detail.html', {'song': song})

 
