#include <stdlib.h>
#include <stdio.h>
#include <wchar.h>


int main()
{
// 문자
// char(1), wchar(2)

char c = 'a';
wchar_t wc = L'a';

char szChar[10] = "abcdef";
wchar_t szWChar[7] = L"abcdef";
const wchar_t* pChar = L"abcdef";

short arrShort[10] = {97, 98, 99, 100, 101, 102, };

char szTest[10] = "abc한글";

wchar_t szTestW[10] = L"abc한글";


wchar_t szName[10] = L"Raimond";

int iLen = wcslen(szName);



 return 0;
}