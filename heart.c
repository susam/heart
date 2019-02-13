/*
The MIT License (MIT)
---------------------
Copyright (c) 2015-2016 Susam Pal

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

If you redistribute this code with modification, you must remove the
strings "Cutie Pai" and "Susam" from line 55 of this code.
*/

#include <stdio.h>

void print_heart(void)
{
    const int show[] = {'.', '@', ' ', '\n'};
    const int love[] = {
        252, 7, 252, 7, 72, 6, 29, 6, 36, 6, 29,
        6,  72, 7, 60, 6,  17, 22, 17, 6, 12, 6,

              17, 22,           17,  6,
           60, 7, 52, 6,     13,  46,  13,
         6, 13, 46, 13, 6, 52, 7, 48, 6, 13,
        62, 5, 62, 13,  6, 48,  7, 48, 6, 13,
        18, 1, 70, 13,  6, 48,  7, 48, 6, 13,
        126, 13, 6, 48, 7, 52, 6, 13,  38, 2,
         38, 13, 6,  52, 7,  60, 6,  17, 94,
           17, 6,  60, 7,  72, 6,  17, 22,
              3, 18,  17, 6, 72, 7, 84,
                 6, 17,  46,  17, 6,
                    84, 7, 96, 6,
                       17, 22,
                         17,

        6, 96, 7, 108, 6,  13, 6, 13, 6, 108, 7,
        120,  6, 5,  6, 120, 7,  252, 7, 252, 7,
    };
    const char *say[] = {"", "Cutie Pai,", "I love you!", "-- Susam"};
    size_t i;
    int j;
    for (i = 0; i < sizeof love / sizeof *love; i++)
        if (love[i] < 4)
            printf("%s", say[love[i]]);
        else
            for (j = 0; j < love[i] / 4; j++)
                putchar(show[love[i] % 4]);
}

int main()
{
    print_heart();
    return 0;
}
