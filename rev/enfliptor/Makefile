NAME := enfliptor

DOCKER_CONTEXT := default
DOCKER_GLOBAL := --context $(DOCKER_CONTEXT)

clean: .PHONY
	rm -f $(NAME).tar.gz $(NAME).exe

build: Dockerfile
	docker $(DOCKER_GLOBAL) build -t $(NAME) .

extract:
	$(eval id := $(shell docker create $(NAME)))
	docker cp $(id):/App/enfliptor/out/$(NAME).exe $(NAME).exe
	docker rm -v $(id)

dist: extract
	tar -czf $(NAME).tar.gz $(NAME).exe flag.enc

.PHONY:
