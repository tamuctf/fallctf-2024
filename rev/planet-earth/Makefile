NAME := planet-earth-revolves-leisurely

DOCKER_CONTEXT := default
DOCKER_GLOBAL := --context $(DOCKER_CONTEXT)

all: dist

clean:
	rm -f $(NAME) $(NAME).tar.gz
	docker container rm -f $(NAME)$(SUFFIX)

build: Dockerfile
	docker $(DOCKER_GLOBAL) build -t $(NAME) \
		--build-arg name=$(NAME) \
		.

extract:
	docker $(DOCKER_GLOBAL) run $(NAME) /bin/perl convert.pl > $(NAME)

dist: extract
	tar -czf $(NAME).tar.gz $(NAME)

.PHONY: all clean build extract dist
