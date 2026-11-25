export C_INCLUDE_PATH := /opt/homebrew/include
export LIBRARY_PATH   := /opt/homebrew/lib

CC      := clang
CFLAGS  := -fsanitize=signed-integer-overflow -fsanitize=undefined -fsanitize=address \
           -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra \
           -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow
LDLIBS  := -lcs50 -lm
YEAR    ?= 2026

ACTIONS := b r s c sub build run style check submit
ifeq ($(filter $(firstword $(MAKECMDGOALS)),$(ACTIONS)),$(firstword $(MAKECMDGOALS)))
  NAME := $(word 2,$(MAKECMDGOALS))
  ifneq ($(NAME),)
    $(eval .PHONY: $(NAME))
    $(eval $(NAME):;@:)
  endif
endif

DIR        := $(firstword $(wildcard $(NAME) 0*-*/$(NAME)))
SRC        := $(firstword $(wildcard $(DIR)/*.c))
BIN        := $(basename $(SRC))
BASE_NAME  := $(notdir $(patsubst %/,%,$(NAME)))
AUTO_SLUG  := $(subst -less,/less,$(subst -more,/more,$(BASE_NAME)))
SLUG       := $(if $(S),$(S),$(AUTO_SLUG))
CHECK_MODE = $(if $(UPDATE),--local,--offline)

.DEFAULT_GOAL := help
.PHONY: help b build r run s style c check sub submit clean

help:
	@echo "Usage:"
	@echo "  make r <name>             编译并运行（例：make r me）"
	@echo "  make s <name>             运行 style50 风格检查"
	@echo "  make c <name>             离线运行 check50（-less/-more 自动映射）"
	@echo "  make c <name> UPDATE=1    联网刷新 check50 用例库后再测"
	@echo "  make sub <name>           提交到 CS50（submit50）"
	@echo "  make clean                清理所有 .c 对应的编译产物与 .dSYM"

b:
	@test -n "$(NAME)" || { echo "Usage: make r <name> (e.g. make r me)"; exit 1; }
	@test -n "$(DIR)" || { echo "Error: '$(NAME)' not found under $(NAME)/ or 0*-*/$(NAME)/"; exit 1; }
	@if [ -f "$(DIR)/Makefile" ]; then $(MAKE) -C "$(DIR)"; else $(CC) $(CFLAGS) $(SRC) -o $(BIN) $(LDLIBS); fi

build: b

r: b
	./$(BIN)

run: r

s:
	@test -n "$(NAME)" || { echo "Usage: make s <name> (e.g. make s me)"; exit 1; }
	@test -n "$(DIR)" || { echo "Error: '$(NAME)' not found under $(NAME)/ or 0*-*/$(NAME)/"; exit 1; }
	style50 $(SRC)

style: s

c:
	@test -n "$(NAME)" || { echo "Usage: make c <name> (e.g. make c me)"; exit 1; }
	@test -n "$(DIR)" || { echo "Error: '$(NAME)' not found under $(NAME)/ or 0*-*/$(NAME)/"; exit 1; }
	cd $(DIR) && check50 $(CHECK_MODE) cs50/problems/$(YEAR)/x/$(SLUG)

check: c

sub:
	@test -n "$(NAME)" || { echo "Usage: make sub <name> (e.g. make sub me)"; exit 1; }
	@test -n "$(DIR)" || { echo "Error: '$(NAME)' not found under $(NAME)/ or 0*-*/$(NAME)/"; exit 1; }
	cd $(DIR) && submit50 cs50/problems/$(YEAR)/x/$(SLUG)

submit: sub

clean:
	@find . -maxdepth 4 -name '*.c' -exec sh -c 'for f; do rm -f "$${f%.c}"; rm -rf "$${f%.c}.dSYM"; done' _ {} +
