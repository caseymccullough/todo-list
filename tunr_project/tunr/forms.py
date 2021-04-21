from django import forms
from .models import Artist, Song
​
# const [artist, setArtist] = useState('');
​
class ArtistForm(forms.ModelForm):
​
    class Meta:
        model = Artist
        fields = ('name', 'photo_url', 'nationality')
​
# Create a SongForm class
class SongForm(forms.ModelForm):
​
    class Meta:
        model = Song
        fields = ('artist', 'album', 'preview_url', 'title')