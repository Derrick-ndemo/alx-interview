# Pascal's Triangle

### Rescource
- [Working with Arrays in Javascript](https://www.digitalocean.com/community/tutorial-series/working-with-arrays-in-javascript)

## Task

0. Pascal's Triangle

Create a function `def pascal_tiangle(n)` that returns a list of integers representing the Pascal's triangle of `n`:
- Retruns an empty list if `n <= 0`
- You can assume `n` will always be an integer

```
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ 
```
