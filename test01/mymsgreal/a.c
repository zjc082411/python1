.SUFFIXES:
.SUFFIXES:.c .o
WORKDIR=.
INCLDIR=$(WORKDIR)/incl
LIBDIR=$(HOME)/lib
BINDIR=$(HOME)/bin

CC=gcc

INCLFLG=-I$(INCLDIR)
LIBFLG=-L$(LIBDIR)
CFLAG=-c -g $(INCLFLG)
LIBS=

VPATH=$(WORKDIR)/src

OBJ7=itcast_asn1_der.o itcastderlog.o keymng_msg.o
bmymessafereal.so:$(OBJ7)
	$(CC) -shared -fPIC $^ -o $@
	@cp $@ $(LIBDIR)
#gcc -shared -fPIC itcast_asn1_der.o itcastderlog.o keymng_msg.o itcast_asn1_der.o  -o libmymessafereal.so
$@代表目标文件
$^依赖项  通过变量来实现赋值
makefile 主要是通过目标  依赖 和规则  主要的有头文件的-I
还有的是动态库 ——L  是动态库的路径 -l lib.so动太库
还有的就是什么呢：
.c.o:表示规则




