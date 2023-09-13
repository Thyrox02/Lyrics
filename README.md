
# ![Logo](https://i.imgur.com/U9YCwwT.png)                                                          [Lyrics](https://github.com/Thyrox02/Lyrics/commit/36b5cc3b866a2282c77bc94a7a4860f6f9410535/) is a Flask-Powered App for Practicing Language Skills Through Lyrics aimed at helping students practice their English language skills through music.                                                                                                            ## Table of content                                                                                 - [Inspiration](#inspiration)                     - [Built With](#built-with)                       - [Getting Started](#getting-started)             - [Features](#features)                               - [Song Selection](#song-selection)               - [Words To Explore](#words-to-Explore)           - [Linguistic Breakdown and Highlighting Of Selected Words](#linguistic-breakdown-and-highlighting-of-selected-words)                                 - [Submit interpretations and view past submissions](#submit-interpretations-and-view-past-submissions)                                               - [Suggest a Song Form](#suggest-a-song)      - [API](#API)
# ![Logo](https://i.imgur.com/U9YCwwT.png)                                                          [Lyrics](https://github.com/Thyrox02/Lyrics/commit/36b5cc3b866a2282c77bc94a7a4860f6f9410535/) is a Flask-Powered App for Practicing Language Skills Through Lyrics aimed at helping students practice their English language skills through music.                                                                                                            ## Table of content                                                                                 - [Inspiration](#inspiration)                     - [Built With](#built-with)                       - [Getting Started](#getting-started)             - [Features](#features)                               - [Song Selection](#song-selection)               - [Words To Explore](#words-to-Explore)           - [Linguistic Breakdown and Highlighting Of Selected Words](#linguistic-breakdown-and-highlighting-of-selected-words)                                 - [Submit interpretations and view past submissions](#submit-interpretations-and-view-past-submissions)                                               - [Suggest a Song Form](#suggest-a-song)      - [API](#API) [Future](#future)                               - [Attributions](#attributions)                   - [Author](#author)                                                                                 ## Inspiration                                                                                      Oddly enough, I don’t really have any interest in Music, even though my project is all about learning language through lyrics. I had decided very early on that I wanted to work with a RESTful API, and needed a reason to use it. i grow up in an environment full of many children and i observed how their parents use music to help them learn English language and that inspired me 
## Built With

### Tools

# ![Tools](https://i.imgur.com/vKyy1ZR.png)

### Architecture                                                                                    # ![Architecture](https://i.imgur.com/E3TaTuX.png)                                                  ## Getting Started                                                                                  To install it, simply clone this repository. You can start the app by running `web_app.app` and `api.v1.app` as Python modules in separate terminal windows. Please note, in order to run this app, you will need to install necessary dependencies as well as pass in the correct MySQLdb and Words API credentials respectively.

## Features

### **Song selection**

Lyrics provides a selection of "clean" and vocabulary-rich songs to explore from a variety of different genres. The data for each song is fetched from the internal RESTful API and is used to fill each Bootstrap card. The song's id is used as the id for the "View" button within the song's card. This allows for the correct song details to be fetched when the user clicks on the button since the id becomes part of the URL for the song.

# ![song-selection](https://i.imgur.com/h3m9fko.png) 

# ![words-to-explore](https://i.imgur.com/JBlT2hx.png)                                                                                                ### **Linguistic Breakdown and Highlighting of Words**                                                                                                                                                  When a user selects a specific word from a song, the linguistic breakdown is fetched from the external Words API. The JS script will then create a menu based the number of entries available for the word. When a user clicks on one of the entries, the script will then see what sections are available for that entry (ex: "Definition", "Synonyms", "Exam
ples"). The available sections and their content will populate a dynamic tabbed interface for the user to browse. In addition, the word is highlighted in the lyrics. This was made possible by first parsing the lyrics and adding span elements around words that appear in the "Pick a word to explore!" list. The spans have aligned classes added to them that allow them to be targeted and thus highlighted when a word is selected.

# ![linguistic-breakdown-and-highlighting-of-words](https://i.imgur.com/YKhWuCj.png)

### **Submit Interpretations and View Past Interpretations**

After exploring the linguistic breakdown of a word, the user can share what they think the artist means by the word. When they press "Submit", their interpretation is sent as a `POST` request to the internal RESTful API. The `better-profanity` module is then used to check the interpretation for profanity and if so, the submission is not stored in the database and a warning dialog is displayed to the user. If there is no profanity, the submission is stored in the database and can be seen in the "Latest Interpretations" section, which is an accordian-style display.

# ![submit-interpretations-and-view-past-interpretations](https://i.imgur.com/lAmK39I.png)

### **Suggest a Song Form**                                                                         If a user would like to suggest a song to be added to the collection of songs to learn from, they can visit the "Suggest a Song" page and fill out the form. The form will ask for all necessary attributes for creating a new Song object including the song's artist, title, and words to learn from. The user must also submit their email and name so they can be notified if the song is added to the collection and receive credit for their contribution.

# ![suggest-a-song-form](https://i.imgur.com/jspGhrb.png)                                                                                             ## API                                            
I built an internal RESTful API for this web application so that data can be flexibly retreived from the MySQLdb. All available endpoints can be found in the `api.v1.views` directory. Here's a description of each endpoint:

/api/v1/interpretations/<word_id>/<song_id>

* GET: Retrieves all Interpretation objects for a word from a song and returns a list containing
    all of them

* POST: Creates an interpretation for a word from a song

/api/v1/interpretations/<interpretation_id>

* PUT: Updates an Interpretation object

/api/v1/songs/<song_id>/words
* GET: Retrieves all words from a song and returns a list containing                                    all of them

/api/v1/songs                                                                                       * GET: Retrieves all Song objects from database and returns a list containing
    all of them

/api/v1/songs/<text>                                                                                * GET: Retrieves Song object from database and ret
urns a dictionary

/api/v1/songs/genre/<genre>                                                                         * GET: Retrieves all Song objects from database wi
th a specified genre

/api/v1/suggestions/
                                                  * GET: Retrieves all Suggestion objects from datab
ase and returns a list containing
    all of them

* POST: Creates a Suggestion object               
/api/v1/words/<text>

* GET: Retrieves word_id based on word

/api/v1/words_api/<text>

* GET: Retrieves data for word from external API a
nd returns response to client-side.
     By passing in API credentials from the comman
d line when running the API and
     using the internal API for the fetch, it prevents credentials from being exposed                    on the front-end.

## Future

Beyond this initial MVP which was built in 2 weeks, I would like to continue to add many more features to Lyric

## Attributions                                                 
Shout-out to [Open Lyrics Database](https://github.com/Lyrics/lyrics) for the lyrics shown!                                     

 Licenses for images from Wikimedia Commons:
* [The xx at the Alcatraz.jpg](https://commons.wikimedia.org/wiki/File:The_xx_at_the_Alcatraz.jpg)
* [Adele Live 2016 tour.jpeg](https://commons.wiki
media.org/wiki/File:Adele_Live_2016_tour.jpeg)
* [Paul Simonon The Clash September 20 1979 Pallad
ium NYC.jpg](https://commons.wikimedia.org/wiki/Fi
le:Paul_Simonon_The_Clash_September_20_1979_Pallad
ium_NYC.jpg)
                                                                ## Author                                         
### **Jimoh Lukman Olamilekan**

Jimoh Lukman Olamilekan is a graduate of Anatomy, university of Ilorin  and current full stack softw
are engineer enthusiast with a passion to creating
 products that connect and empower others.
                                                     
[Github](https://github.com/Thyrox02/Lyrics)
[LinkedIn](https://www.linkedin.com/in/techflavour
)
[Twitter](https://twitter.com/Thyrox_02?s=09)

[Deployed page](https://github.com/Thyrox02/Lyrics
/deployments/github-pages)
