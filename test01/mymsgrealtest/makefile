# Makefile 
.SUFFIXES:
.SUFFIXES:  .c .o

all: testmsgreal


CC	= gcc


WORKDIR=.
LIBDIR=$(HOME)/lib
LIBS = -L$(LIBDIR) -lmymessagereal
OUTDIR=$(HOME)/bin

INCLDIR=$(WORKDIR)/incl
INCLFLG= -I$(WORKDIR)/incl
CFLAG= $(INCLFLG) -g -c -Wall

VPATH = $(WORKDIR)/src

OBJ1 = dm01_test.o 

testmsgreal:$(OBJ1)
	$(CC) $(LIBS) $^ -o $@ 
	
	
#testmsgreal:dm01_test.o
#	gcc  -L/home/it01/lib -lmymessagereal  dm01_test.o   -o testmsgreal	
#	gcc -L/home/it01/lib/  -lmessagereal -I/home/it01/mymsgreal/incl/  1.o 2.o -o 1.exe	


# 把所有的。c 生成。o
# gcc -I./incl -g -c -Wall keymng_msg_test.c -o keymng_msg_test.o
#.o:.c
#keymng_msg_test.c====>keymng_msg_test.o
	
.c.o:
	$(CC) $(CFLAG) $<

#.o:.c 1.c 2.c
#	gcc 	-I./incl  -g -c $< -Wall
#	gcc 	-I./incl  -g -c 1.c -1.o -Wall
#	gcc 	-I./incl  -g -c 2.c -2.o -Wall

.PHONY:clean
clean:
	rm *.o
	rm testmsgreal
	rm *.ber
	rm *.txt
	


