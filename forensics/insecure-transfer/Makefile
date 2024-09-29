NAME := insecure-transfer

all: dist

clean: .PHONY
	rm -f $(NAME).zip

dist:
	zip $(NAME).zip flag.zip capture.pcapng

.PHONY: