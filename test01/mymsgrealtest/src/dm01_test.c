

#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "keymng_msg.h"

//我们
int mywritefile(unsigned char *buf, int len)
{
	FILE *fp = NULL;
	fp = fopen("c:/teacher.ber", "wb+");
	if (fp == NULL)
	{
		printf("fopen file error \n");
		return -1;
	}
	fwrite(buf, 1, len, fp);
	fclose(fp);
	return 0;
}


int main()
{
	int					ret = 0;
	Teacher				t1;

	unsigned char		*myOut = NULL;
	int					myOutlen;

	Teacher				*myStruct = NULL;
	int					iType = 0;
	memset(&t1, 0, sizeof(Teacher));
	strcpy(t1.name, "myname");
	t1.age = 32;
	t1.p = (char *)malloc(100);
	strcpy(t1.p, "aafffffff"); //
	t1.plen = strlen(t1.p);


	ret = MsgEncode(&t1, ID_MsgKey_Teacher, &myOut, &myOutlen);
	if (ret != 0)
	{
		printf("func MsgEncode() err:%d \n", ret);
		return ret;
	}

	mywritefile(myOut, myOutlen);

	ret = MsgDecode(myOut, myOutlen, (void **)&myStruct, &iType);
	if (ret != 0)
	{
		printf("func MsgEncode() err:%d \n", ret);
		return ret;
	}

	//释放内存块

	//if (myOut != NULL)  free(myOut) ;  不能直接释放动态库的内存 只能调用动态库提供的api函数 去释放动态库的内存
	MsgMemFree((void **)&myOut, 0);
	MsgMemFree((void **)&myStruct, iType);
	
	printf("111111111111111111111\n");
	printf("释放内存ok\n");
	printf("2222222222222222222\n");


	printf("hello...\n");
	//system("pause");
	return 0;
}
