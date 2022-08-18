import os
from plexapi.server import PlexServer
import logging
import time

logging.getLogger().setLevel(os.environ.get('LOG_LEVEL', logging.INFO))

genre_tag_map = {}
if os.environ.get('GENRE_TAGS') is not None:
    auto_tag_input = os.environ.get('GENRE_TAGS')
    for part in auto_tag_input.split(';'):
        key, value = part.split('=')
        genre_tag_map[key] = value

logging.info(f"Logging into Plex @ {os.environ.get('PLEX_URL')}")
plex = PlexServer(os.environ.get('PLEX_URL'), os.environ.get('PLEX_TOKEN'))

logging.info(f"Refreshing Library")
plex.library.section("Music Videos").update()
time.sleep(30)

all_videos = plex.library.section('Music Videos').all()
logging.info(f"Iterating over all {len(all_videos)} music videos")

updated = 0
for video in all_videos:
    if len(video.labels) == 0:  # for simplicity, just assume any labels means there's nothing to do
        playlist_source = video.locations[0].split("/")[4]
        video.addLabel(playlist_source)

        for playlist_search, genre_assignment in genre_tag_map.items():
            if playlist_search in playlist_source:
                video.addGenre(genre_assignment)
        updated += 1

logging.info(f"Updated {updated} music videos")
