import os
from plexapi.server import PlexServer

print("Logging in...")
plex = PlexServer(os.environ.get('PLEX_URL'), os.environ.get('PLEX_TOKEN'))
print("Logged in")

updated = 0
for video in plex.library.section('Music Videos').all():
    video.addLabel(video.locations[0].split("/")[4])
    updated += 1

print(f"Updated {updated} videos")
