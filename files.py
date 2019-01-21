import shutil
import subprocess
import tempfile

from generator.java_class import RandomClass


class TemporaryFile:
    def __init__(self, name, contents, suffix):
        self.dir = tempfile.mkdtemp()
        self.file, self.path = tempfile.mkstemp(suffix=suffix, prefix=name, dir=self.dir)
        self.name = name
        with open(self.path, "wb") as f:
            f.write(contents)

    def __str__(self):
        with open(self.path, "rb") as f:
            return str(f.read())

    def __del__(self):
        shutil.rmtree(self.dir)


class TemporaryJavaFile(TemporaryFile):
    def __init__(self, name, contents):
        super().__init__(name, contents, ".java")

    def compile(self):
        p = subprocess.Popen(["javac", self.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p.communicate()
        print("COMPILING...")
        print("STDOUT: " + str(output))
        print("STDERR: " + str(error))
        class_file_path = "{dir}/{name}.class".format(dir=str(self.dir), name=self.name)
        with open(class_file_path, "rb") as f:
            return TemporaryClassFile(self.name, f.read())


class TemporaryClassFile(TemporaryFile):
    def __init__(self, name, contents):
        super().__init__(name, contents, ".class")


class RandomTemporaryJavaFile(TemporaryJavaFile):
    def __init__(self):
        random_class = RandomClass()
        contents = str(random_class)
        name = random_class.name
        super().__init__(name, str.encode(contents))


if __name__ == "__main__":
    f = RandomTemporaryJavaFile()
    print(f)
    c = f.compile()
    print(c)
    del f
    del c
