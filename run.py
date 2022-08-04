import os
from plexapi.server import PlexServer
import logging

logging.getLogger().setLevel(os.environ.get('LOG_LEVEL', logging.INFO))

logging.info(f"Logging into Plex @ {os.environ.get('PLEX_URL')}")
plex = PlexServer(os.environ.get('PLEX_URL'), os.environ.get('PLEX_TOKEN'))

all_videos = plex.library.section('Music Videos').all()
logging.info(f"Iterating over all {len(all_videos)} music videos")

updated = 0
for video in all_videos:
    if len(video.labels) == 0:  # for simplicity, just assume any labels means there's nothing to do
        playlist = video.locations[0].split("/")[4]  # for simplicity, we don't do any safety checks here
        video.addLabel(video.locations[0].split("/")[4])
        updated += 1

logging.info(f"Updated {updated} music videos")
