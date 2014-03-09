import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist
 
engine = create_engine('sqlite:///mymusic.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Create an artist
new_artist = Artist("Newsboys")

more_albums= []
# add more albums
for i in range(1,5):
	more_albums.append(Album("Some album " + str(i),
                     "some genre",
                     "some publisher", "CD"))
               
new_artist.albums.extend(more_albums)
 
# Add the record to the session object
session.add(new_artist)
# commit the record the database
session.commit()
