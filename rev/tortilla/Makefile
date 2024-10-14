NAME := tortilla

DOCKER_CONTEXT := default
DOCKER_GLOBAL := --context $(DOCKER_CONTEXT)

all: $(NAME)

$(NAME): 
	pyinstaller --add-data "data\*;data\" --noconsole -F .\game.py   

clean: .PHONY
	rm -f $(NAME).exe $(NAME).tar.gz

build: Dockerfile
	docker $(DOCKER_GLOBAL) build -t $(NAME) .

extract:
	$(eval id := $(shell docker create $(NAME)))
	docker cp $(id):/app/dist/game.exe $(NAME).exe
	docker rm -v $(id)

dist: extract
	tar -czf $(NAME).tar.gz $(NAME).exe
	rm -f $(NAME).exe

.PHONY:
