# Java Generator
Java Generator for automated Testing, written in Python.

## Quickstart

To generate a temporary Java file and compile it, run the following code:

```python
# Create random java file (in a temporary directory)
f = RandomTemporaryJavaFile()
print(f)

# Compile the java file with javac
c = f.compile()
print(c)

# Delete both files from the disk
del f
del c
```