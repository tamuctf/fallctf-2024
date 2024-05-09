NAME := permuted

CC := $(or $(CC),gcc)
CFLAGS := -no-pie 

all: $(NAME)

$(NAME): $(NAME).c
	$(CC) $^ -o $@ $(CFLAGS)

clean: .PHONY
	rm -f $(NAME) $(NAME).zip

build: Dockerfile
	docker $(DOCKER_GLOBAL) build -t $(NAME) .

extract: build
	$(eval id := $(shell docker create $(NAME)))
	docker cp $(id):/tmp/$(NAME) .
	docker rm -v $(id)

dist: extract
	zip $(NAME).zip $(NAME)

.PHONY: