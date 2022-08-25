
build:
	docker build -t plex-label-music-videos .

run:
	@docker run -e PLEX_URL=$(PLEX_URL) -e PLEX_TOKEN=$(PLEX_TOKEN) -e GENRE_TAGS=$(GENRE_TAGS) plex-label-music-videos

.PHONY: build run
