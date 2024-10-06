NAME := planet-earth-revolves-leisurely

DOCKER_CONTEXT := default
DOCKER_GLOBAL := --context $(DOCKER_CONTEXT)

all: dist

clean:
	rm -f $(NAME) $(NAME).tar.gz || true
	docker $(DOCKER_GLOBAL) container rm -f $(shell docker $(DOCKER_GLOBAL) ps -a -q --filter "ancestor=$(NAME)") || true
	docker $(DOCKER_GLOBAL) image rm -f $(NAME)

build: Dockerfile
	docker $(DOCKER_GLOBAL) build -t $(NAME) \
		--build-arg name=$(NAME) \
		.

extract: build
	docker $(DOCKER_GLOBAL) run $(NAME) /bin/perl convert.pl > $(NAME)

dist: extract
	tar -czf $(NAME).tar.gz $(NAME)

.PHONY: all clean build extract dist
